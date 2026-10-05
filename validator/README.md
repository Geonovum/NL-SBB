# NL-SBB Browservalidator

> **Concept.** Een hulpmiddel voor review, geen officieel product van Geonovum. De
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
