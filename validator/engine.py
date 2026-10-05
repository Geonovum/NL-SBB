"""NL-SBB-validatie in de browser (Pyodide).

Dezelfde controles als de skill validatie-nl-sbb:
  1. SHACL-validatie tegen skos-ap-nl 1.0.0 + extensie (advanced, rdfs-inferentie)
  2. Inhoudelijke scan van alle termen en definities (inhoudelijke-scan.py)
Geeft een JSON-string terug die de pagina rendert.

Ook bruikbaar vanaf de commandoregel, met dezelfde uitkomst als de pagina:
  python engine.py data.ttl                 # samenvatting per ernstniveau
  python engine.py data.ttl --json          # volledig resultaat als JSON
  python engine.py data.ttl --profiel ../profiles/skos-ap-nl.ttl
Exitcode 1 als er een sh:Violation is, 2 als het bestand niet te lezen is.
"""
import json, re, time, unicodedata
from collections import defaultdict, Counter
from rdflib import Graph, Namespace, RDF, URIRef, Literal
import sparqlcache  # noqa: F401  (versnelt pySHACL ~7x)
from pyshacl import validate

SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
DCT = Namespace("http://purl.org/dc/terms/")
SH = Namespace("http://www.w3.org/ns/shacl#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")

SHAPES = None
META = {}


def init(profiel_ttl, extensie_ttl):
    """Laad profiel en extensie in één shapes-graaf (nooit via -e/ont_graph)."""
    global SHAPES, META
    g = Graph().parse(data=profiel_ttl, format="turtle")
    n_profiel = len(g)
    versie = next((str(o) for o in g.objects(None, OWL.versionInfo)), "onbekend")
    g.parse(data=extensie_ttl, format="turtle")
    SHAPES = g
    import pyshacl, rdflib
    META = {
        "profielVersie": versie,
        "triplesProfiel": n_profiel,
        "triplesProfielPlusExtensie": len(g),
        "pyshacl": pyshacl.__version__,
        "rdflib": rdflib.__version__,
    }
    return json.dumps(META)


def kort(u):
    s = str(u).rstrip("/")
    return re.split(r"[/#]", s)[-1] or s


def label_van(g, u):
    for p in (SKOS.prefLabel, DCT.title, URIRef("http://www.w3.org/2000/01/rdf-schema#label")):
        for o in g.objects(u, p):
            return str(o)
    return None


SEV = {"Violation": "fout", "Warning": "waarschuwing", "Info": "info"}


def shacl(g):
    conforms, res, _ = validate(
        g, shacl_graph=SHAPES, inference="rdfs", advanced=True,
        abort_on_first=False, allow_warnings=False, allow_infos=False,
    )
    rijen = []
    for r in res.subjects(RDF.type, SH.ValidationResult):
        sev = str(res.value(r, SH.resultSeverity)).split("#")[-1]
        focus = res.value(r, SH.focusNode)
        shape = res.value(r, SH.sourceShape)
        path = res.value(r, SH.resultPath)
        val = res.value(r, SH.value)
        rijen.append({
            "ernst": SEV.get(sev, sev.lower()),
            "shape": kort(shape) if isinstance(shape, URIRef) else "(anonieme shape)",
            "extensie": kort(shape) in EXT_SHAPES if isinstance(shape, URIRef) else False,
            "focus": str(focus),
            "focusKort": kort(focus),
            "term": label_van(g, focus),
            "pad": kort(path) if isinstance(path, URIRef) else None,
            "waarde": str(val) if val is not None else None,
            "melding": str(res.value(r, SH.resultMessage) or ""),
        })
    rijen.sort(key=lambda x: (["fout", "waarschuwing", "info"].index(x["ernst"]) if x["ernst"] in SEV.values() else 9, x["shape"], x["focusKort"]))
    return conforms, rijen


def scan(g):
    concepts = sorted(g.subjects(RDF.type, SKOS.Concept))
    termen, definities, ontbreekt = {}, {}, defaultdict(list)
    for c in concepts:
        pl = [str(o) for o in g.objects(c, SKOS.prefLabel)]
        df = [str(o) for o in g.objects(c, SKOS.definition)]
        if pl: termen[c] = pl[0]
        else: ontbreekt["skos:prefLabel"].append(c)
        if df: definities[c] = df[0]
        else: ontbreekt["skos:definition"].append(c)
        if not list(g.objects(c, SKOS.inScheme)): ontbreekt["skos:inScheme"].append(c)
        if not list(g.objects(c, DCT.source)): ontbreekt["dct:source"].append(c)

    def item(c, tekst=None):
        return {"focus": str(c), "focusKort": kort(c), "term": termen.get(c), "tekst": tekst}

    cats = []

    def cat(id_, titel, ernst, uitleg, items, oordeel=False):
        cats.append({"id": id_, "titel": titel, "ernst": ernst, "uitleg": uitleg,
                     "items": items, "oordeel": oordeel})

    for k, v in ontbreekt.items():
        ernst = "info" if k == "dct:source" else "fout"
        cat("ontbreekt-" + k, f"Ontbrekende {k}", ernst,
            "Verplichte eigenschap ontbreekt." if ernst == "fout" else "Een bronverwijzing maakt de definitie herleidbaar.",
            [item(c) for c in v])

    t = termen.items()
    cat("hoofdletter", "Term begint met een hoofdletter", "waarschuwing",
        "Best Practice 1: termen in kleine letters, tenzij het een eigennaam is.",
        [item(c, x) for c, x in t if x[:1].isupper()])
    cat("camelcase", "Term in CamelCase", "waarschuwing",
        "Een term is natuurlijke taal, geen technische naam.",
        [item(c, x) for c, x in t if re.search(r"[a-z][A-Z]", x)])
    cat("leesteken", "Term bevat een leesteken", "waarschuwing",
        "Best Practice 1: geen leestekens. Een komma of schuine streep wijst vaak op twee termen in één veld; gebruik skos:altLabel.",
        [item(c, x) for c, x in t if re.search(r"[.,;:()/\\]", x)])
    cat("afkorting", "Term bevat een afkorting", "waarschuwing",
        "Best Practice 1: schrijf afkortingen voluit; leg de afkorting vast als skos:altLabel.",
        [item(c, x) for c, x in t if re.search(r"\b[A-Z]{2,}\b", x)])
    cat("meervoud", "Term eindigt mogelijk op meervoud of werkwoord (-en)", "te beoordelen",
        "Best Practice 1: zelfstandig naamwoord in enkelvoud. Deze controle is grof; beoordeel elk geval zelf.",
        [item(c, x) for c, x in t if re.search(r"\w{4,}en\b", x)], oordeel=True)

    groepen = defaultdict(list)
    for c, d in definities.items():
        groepen[d].append(c)
    dubbel = [item(c, d) for d, cs in sorted(groepen.items(), key=lambda x: -len(x[1])) if len(cs) > 1 for c in cs]
    cat("identiek", "Identieke definitie bij meerdere begrippen", "waarschuwing",
        "Een definitie moet het begrip onderscheiden van andere begrippen.", dubbel)
    cat("circulair", "Definitie bevat de term zelf", "te beoordelen",
        "Mogelijk circulair. Beoordeel of de definitie meer zegt dan de term herhalen.",
        [item(c, d) for c, d in definities.items()
         if termen.get(c) and re.search(rf"\b{re.escape(termen[c])}\b", d, re.I)], oordeel=True)
    cat("mojibake", "Tekstcoderingsfout in definitie", "waarschuwing",
        "UTF-8 die als Latin-1 is gelezen laat reeksen als 'Ã©' achter.",
        [item(c, d) for c, d in definities.items() if re.search(r"[ÃÂ][\u0080-¿ -ÿ]", d)])
    cat("stuurteken", "Stuurtekens in definitie", "waarschuwing",
        "Onzichtbare tekens verstoren zoeken en weergave.",
        [item(c, d) for c, d in definities.items() if any(unicodedata.category(ch)[0] == "C" for ch in d)])
    cat("kort", "Zeer korte definitie (minder dan 20 tekens)", "te beoordelen",
        "Een heel korte definitie beschrijft het begrip vaak onvoldoende.",
        [item(c, d) for c, d in definities.items() if len(d) < 20], oordeel=True)
    cat("punt", "Definitie eindigt niet op een punt", "aanbeveling",
        "Consistente opmaak van definities.",
        [item(c, d) for c, d in definities.items() if d.strip() and not d.strip().endswith(".")])
    return cats


def statistiek(g):
    talen = Counter(o.language or "(geen)" for o in g.objects(None, SKOS.prefLabel) if isinstance(o, Literal))
    rel = Counter()
    for p in g.predicates():
        s = str(p)
        if s.startswith("http://purl.org/iso25964/skos-thes#") or s.split("#")[-1] in (
                "broader", "narrower", "related", "exactMatch", "closeMatch", "broadMatch", "narrowMatch", "relatedMatch"):
            rel[kort(p)] = len(set(g.subject_objects(p)))
    return {
        "triples": len(g),
        "begrippenkaders": len(set(g.subjects(RDF.type, SKOS.ConceptScheme))),
        "begrippen": len(set(g.subjects(RDF.type, SKOS.Concept))),
        "collecties": len(set(g.subjects(RDF.type, SKOS.Collection))),
        "topbegrippen": len(set(g.subject_objects(SKOS.topConceptOf)) | {(o, s) for s, o in g.subject_objects(SKOS.hasTopConcept)}),
        "talen": dict(talen),
        "relaties": dict(rel),
    }


def run(data, fmt):
    t0 = time.time()
    g = Graph()
    try:
        g.parse(data=data, format=fmt)
    except Exception as e:
        return json.dumps({"fout": f"Het bestand kon niet als {fmt} worden gelezen: {e}"})
    t1 = time.time()
    conforms, rijen = shacl(g)
    t2 = time.time()
    cats = scan(g)
    ext_shapes = {r["shape"] for r in rijen if r["shape"] in EXT_SHAPES}
    return json.dumps({
        "meta": META,
        "stat": statistiek(g),
        "conforms": conforms,
        "shacl": rijen,
        "scan": cats,
        "extensieShapesGeraakt": sorted(ext_shapes),
        "duur": {"inlezen": round(t1 - t0, 2), "shacl": round(t2 - t1, 2), "scan": round(time.time() - t2, 2)},
    }, ensure_ascii=False)


EXT_SHAPES = set()


def registreer_extensie(extensie_ttl):
    """Onthoud welke shapes uit de extensie komen, om ze in de UI te markeren."""
    e = Graph().parse(data=extensie_ttl, format="turtle")
    for s in set(e.subjects(RDF.type, SH.NodeShape)) | set(e.subjects(RDF.type, SH.PropertyShape)):
        if isinstance(s, URIRef):
            EXT_SHAPES.add(kort(s))
    return json.dumps(sorted(EXT_SHAPES))


def _samenvatting(out):
    sh = Counter(r["ernst"] for r in out["shacl"])
    m, st = out["meta"], out["stat"]
    regels = [
        f"Profiel: {m.get('profielPad', '?')} (owl:versionInfo {m['profielVersie']}, {m['triplesProfiel']} triples)"
        f" + extensie ({m['triplesProfielPlusExtensie'] - m['triplesProfiel']} triples)",
        f"Instellingen: advanced=True, inference=rdfs · pySHACL {m['pyshacl']}, rdflib {m['rdflib']}",
        f"Begrippen: {st['begrippen']}, topbegrippen: {st['topbegrippen']}, collecties: {st['collecties']}",
        "",
        f"SHACL: {sh['fout']} sh:Violation, {sh['waarschuwing']} sh:Warning, {sh['info']} sh:Info",
    ]
    groepen = Counter((r["ernst"], r["shape"]) for r in out["shacl"])
    for (ernst, shape), n in sorted(groepen.items(), key=lambda x: (["fout", "waarschuwing", "info"].index(x[0][0]), -x[1])):
        ext = " [extensie]" if shape in EXT_SHAPES else ""
        regels.append(f"  {ernst:<13}{n:>4}  {shape}{ext}")
    regels += ["", "Inhoudelijke scan (alle termen en definities):"]
    for k in out["scan"]:
        regels.append(f"  {k['ernst']:<15}{len(k['items']):>4}  {k['titel']}")
        for i in k["items"][:5]:
            tekst = i["tekst"] if i["tekst"] and i["tekst"] != i["term"] else ""
            regels.append(f"{'':>21}- {i['term'] or i['focusKort']}{': ' + tekst[:70] if tekst else ''}")
        if len(k["items"]) > 5:
            regels.append(f"{'':>21}  ... en {len(k['items']) - 5} meer")
    return "\n".join(regels)


def main(argv=None):
    import argparse, os, sys
    from rdflib.util import guess_format
    hier = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description="Valideer een begrippenkader tegen NL-SBB (SHACL + inhoudelijke scan).")
    ap.add_argument("data", help="begrippenkader (Turtle, RDF/XML, JSON-LD, N-Triples, TriG)")
    ap.add_argument("--profiel", default=os.path.join(hier, "rules", "skos-ap-nl-1.0.0.ttl"),
                    help="SHACL-profiel (standaard: 1.0.0 uit het register)")
    ap.add_argument("--extensie", default=os.path.join(hier, "rules", "skos-ap-nl-extensie.ttl"))
    ap.add_argument("--format", help="RDF-formaat; standaard afgeleid van de extensie")
    ap.add_argument("--json", action="store_true", help="volledig resultaat als JSON")
    a = ap.parse_args(argv)
    lees = lambda p: open(p, encoding="utf-8").read()
    extensie = lees(a.extensie)
    init(lees(a.profiel), extensie)
    META["profielPad"] = os.path.relpath(a.profiel)
    registreer_extensie(extensie)
    out = json.loads(run(lees(a.data), a.format or guess_format(a.data) or "turtle"))
    if "fout" in out:
        print(out["fout"], file=sys.stderr)
        return 2
    if a.json:
        sys.stdout.reconfigure(encoding="utf-8")
        print(json.dumps(out, ensure_ascii=False, indent=1))
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(_samenvatting(out))
    return 1 if any(r["ernst"] == "fout" for r in out["shacl"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
