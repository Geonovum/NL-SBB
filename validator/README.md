# NL-SBB Browservalidator

> **Bèta, concept.** Een hulpmiddel in ontwikkeling voor review, geen officieel product van Geonovum. De
> [publicatie van NL-SBB](https://docs.geostandaarden.nl/nl-sbb/nl-sbb/) en het
> SHACL-profiel in het [register](https://register.geostandaarden.nl/) zijn leidend.

Valideert een begrippenkader tegen NL-SBB, volledig in de browser:
<https://geonovum.github.io/NL-SBB/validator/>

Het begrippenkader verlaat de computer van de gebruiker niet. Python (pySHACL, rdflib)
draait via [Pyodide](https://pyodide.org) als WebAssembly in een Web Worker; alleen de
Python-runtime wordt van jsDelivr geladen.

## Wat wordt gecontroleerd

1. **SHACL-validatie** met pySHACL tegen het profiel `skos-ap-nl`, plus een extensie
   met aanvullende regels. Profiel en extensie worden samengevoegd tot één
   shapes-graaf. Instellingen: `advanced=True` (nodig voor de SHACL-SPARQL-regels),
   `inference=rdfs`, geen `allow_warnings`.
2. **Inhoudelijke scan** van alle termen en definities: termconventies (hoofdletter,
   CamelCase, leestekens, afkortingen, mogelijk meervoud), identieke definities,
   definitie die de eigen term bevat, tekstcoderingsfouten, stuurtekens.

Te kiezen profiel:

| Keuze | Bestand | Status |
|---|---|---|
| 1.0.0 uit het register (standaard) | `rules/skos-ap-nl-1.0.0.ttl` | Kopie van `https://register.geostandaarden.nl/shacl/nl-sbb/1.0.0/skos-ap-nl.ttl`, normatief |
| Werkversie in deze repository | `../profiles/skos-ap-nl.ttl` | Het profiel op de branch die GitHub Pages serveert, niet normatief |

Met de werkversie kunnen beheerders zien wat een profielwijziging doet met een
bestaand begrippenkader.

## Niet gecontroleerd

Inhoudelijk oordeel (vaagheid, begripsafbakening, of relaties kloppen),
bereikbaarheid van bronnen, Excel/Word-invoer, totaaloordeel of publicatieadvies.

## Bestanden

| Pad | Inhoud |
|---|---|
| `index.html` | Pagina |
| `worker.js` | Laadt Pyodide, installeert de wheels, draait de validatie |
| `engine.py` | SHACL-validatie, inhoudelijke scan, statistiek; geeft JSON terug |
| `sparqlcache.py` | Cache voor de SPARQL-parser van rdflib; pySHACL parseert anders per begrip dezelfde query opnieuw. Ongeveer 7x sneller, zelfde uitkomst |
| `wheels/` | pyshacl 0.40.1, rdflib 7.6.0, owlrl 7.6.2, pyparsing, prettytable, wcwidth, packaging (pure-Python wheels van PyPI) |
| `rules/skos-ap-nl-1.0.0.ttl` | Normatief profiel 1.0.0 |
| `rules/skos-ap-nl-extensie.ttl` | Aanvullende regels: topbegrip met bovenliggend begrip (ook via `isothes:broader*`), harmonisatierelatie binnen hetzelfde kader, dubbele `skos:notation`, verweesd begrip, identieke definities, ontbrekende bron |
| `rules/voorbeeld-imgeo-mini.ttl` | Testset afgeleid van IMGeo, met opzettelijk aangebrachte fouten |

## Vanaf de commandoregel

`engine.py` is dezelfde code als in de browser en geeft dus dezelfde uitkomst. Nodig:
Python 3.10+ met `pip install pyshacl rdflib`.

```bash
python validator/engine.py mijn-kader.ttl                  # samenvatting per ernstniveau
python validator/engine.py mijn-kader.ttl --json           # volledig resultaat als JSON
python validator/engine.py mijn-kader.ttl --profiel profiles/skos-ap-nl.ttl
```

Het formaat wordt afgeleid van de bestandsextensie (`--format` om te overschrijven).
Exitcode `1` als er een `sh:Violation` is, `2` als het bestand niet te lezen is; zo
is de validator ook in een CI-stap te gebruiken.

## Vanuit een script of AI-assistent

De pagina stelt het resultaat machineleesbaar beschikbaar, zodat een script of een
AI-assistent die de browser bedient de uitkomst niet van het scherm hoeft af te lezen:

| | |
|---|---|
| `<html data-nlsbb-status="…">` | `laden`, `klaar`, `bezig`, `resultaat`, `fout` of `kan-niet-starten` |
| `window.nlsbbResultaat` | Laatste resultaat; dezelfde JSON als `engine.py --json`, plus `samenvatting` met de aantallen |
| `window.nlsbbValideer({ data, format, profiel, naam })` | Valideert en geeft een Promise met het resultaat; de pagina toont het ook. `format`: `turtle` (standaard), `xml`, `json-ld`, `nt`, `trig`. `profiel`: `register` (standaard) of `werkversie` |
| event `nlsbb:resultaat` op `window` | Het resultaat in `event.detail` |

```js
const r = await window.nlsbbValideer({ data: turtleTekst });
r.samenvatting.shacl;   // { fout: 3, waarschuwing: 17, info: 20 }
```

## Lokaal draaien

Openen via `file://` werkt niet; elke statische webserver volstaat. Vanuit de root van
deze repository (zodat `../profiles/` bereikbaar is):

```bash
python -m http.server 8000
```

en open <http://localhost:8000/validator/>.

## Relatie met de publicatie van de standaard

De map staat los van de ReSpec-publicatie. De build- en publicatieworkflows uit
NL-ReSpec-template gebruiken alleen `index.html` en de mappen `data`, `media`, `js` en
`css`; `validator/` wordt dus niet meegenomen naar docs.geostandaarden.nl.
