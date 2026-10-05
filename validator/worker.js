// Draait Pyodide + pySHACL buiten de UI-thread. De Python-runtime komt van de
// jsDelivr-CDN; de wheels, regels en validatiecode staan in deze map.
// Het begrippenkader zelf gaat nergens heen: het wordt in de browser gevalideerd.
const PYODIDE = "https://cdn.jsdelivr.net/pyodide/v0.27.7/full/";
const BASE = new URL("./", self.location).href;
const WHEELS = [
  "pyparsing-3.3.3-py3-none-any.whl",
  "rdflib-7.6.0-py3-none-any.whl",
  "owlrl-7.6.2-py3-none-any.whl",
  "packaging-26.3-py3-none-any.whl",
  "wcwidth-0.9.1-py3-none-any.whl",
  "prettytable-3.18.0-py3-none-any.whl",
  "pyshacl-0.40.1-py3-none-any.whl",
];
const PROFIELEN = {
  register: "rules/skos-ap-nl-1.0.0.ttl",   // kopie van het normatieve profiel uit het register
  werkversie: "../profiles/skos-ap-nl.ttl", // profiel op de branch die GitHub Pages serveert
};

let py = null, engine = null, profielNu = null, extensie = null;
const status = (stap, pct) => postMessage({ type: "status", stap, pct });

async function fetchOk(path, as = "text") {
  const r = await fetch(new URL(path, BASE));
  if (!r.ok) throw new Error(`${path}: HTTP ${r.status}`);
  return as === "buf" ? r.arrayBuffer() : r.text();
}

async function boot() {
  status("Python-runtime laden", 5);
  importScripts(PYODIDE + "pyodide.js");
  py = await loadPyodide({ indexURL: PYODIDE });
  const site = py.runPython("import site; site.getsitepackages()[0]");
  for (let i = 0; i < WHEELS.length; i++) {
    status(`Pakket ${WHEELS[i].split("-")[0]} installeren`, 45 + Math.round((i / WHEELS.length) * 30));
    py.unpackArchive(await fetchOk("wheels/" + WHEELS[i], "buf"), "zip", { extractDir: site });
  }
  for (const f of ["engine.py", "sparqlcache.py"]) py.FS.writeFile(f, await fetchOk(f));
  py.runPython("import sys; sys.path.insert(0, '.')");
  engine = py.pyimport("engine");
  extensie = await fetchOk("rules/skos-ap-nl-extensie.ttl");
  engine.registreer_extensie(extensie);
  await kiesProfiel("register");
  postMessage({ type: "ready" });
}

async function kiesProfiel(naam) {
  if (naam === profielNu) return;
  status("Profiel laden", 85);
  const meta = JSON.parse(engine.init(await fetchOk(PROFIELEN[naam]), extensie));
  meta.profielBron = naam;
  meta.profielPad = PROFIELEN[naam];
  profielNu = naam;
  postMessage({ type: "profiel", meta });
}

const klaar = boot().catch((e) => postMessage({ type: "bootError", message: String((e && e.message) || e) }));

onmessage = async (ev) => {
  const { type, id, data, fmt, profiel } = ev.data;
  if (type !== "run") return;
  await klaar;
  try {
    await kiesProfiel(profiel || "register");
    const t0 = performance.now();
    const out = JSON.parse(engine.run(data, fmt));
    out.meta.profielBron = profielNu;
    out.meta.profielPad = PROFIELEN[profielNu];
    out.duurTotaal = Math.round(performance.now() - t0) / 1000;
    postMessage({ type: "result", id, out });
  } catch (e) {
    postMessage({ type: "result", id, out: { fout: String((e && e.message) || e) } });
  }
};
