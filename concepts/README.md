# concepts/

Deze map bevat de thesaurus van NL-SBB: alle begrippen die in de standaard zijn gedefinieerd, beschreven volgens NL-SBB zelf.

## Versies

| Bestand | Versie | Gepubliceerd op |
|---|---|---|
| `1.0.0/thesaurus.ttl` | 1.0.0 | <https://register.geostandaarden.nl/concepts/nl-sbb/1.0.0/thesaurus.ttl> |
| `1.0.1-cv/thesaurus.ttl` | 1.0.1-cv (consultatieversie) | <https://staging-definities.geostandaarden.nl/stelsel/nl/> (mensleesbaar) en <https://staging-definities.geostandaarden.nl/rest/v1/stelsel/data?format=text/turtle> (Turtle), zie [#122](https://github.com/Geonovum/NL-SBB/issues/122) |

De thesaurus wordt bijgehouden in een submap per versie, zoals het SHACL-profiel in [`shacl/`](../shacl/).

- Een nieuwe versie maak je in een nieuwe submap.
- Een gepubliceerde versie wijzig je niet meer.
- Verwijs in documentatie naar de publicatieplek, niet naar een bestand op GitHub.

Anders dan het SHACL-profiel wordt de thesaurus vanaf 1.0.1 niet op register.geostandaarden.nl gepubliceerd, maar alleen op definities.geostandaarden.nl (BegrippenXL), conform het Geonovum-beleid voor begrippenkaders. De consultatieversie staat op de stagingomgeving; de vastgestelde versie komt in productie. Versie 1.0.0 blijft op het register staan. Publicatie gebeurt met de hand; de autodeploy van het technisch register pakt `concepts/` niet op.

## `thesaurus.ttl` in deze map (legacy)

**Wijzig `concepts/thesaurus.ttl` niet.** Dit bestand blijft staan om historische redenen. De vastgestelde versie 1.0.0 van de standaard (<https://docs.geostandaarden.nl/nl-sbb/nl-sbb/>) verwijst er rechtstreeks naar:

- <https://raw.githubusercontent.com/geonovum/NL-SBB/main/concepts/thesaurus.ttl>
- <https://github.com/Geonovum/NL-SBB/blob/main/concepts/thesaurus.ttl>

Daarom moet dit bestand gelijk blijven aan versie 1.0.0. Het is byte voor byte gelijk aan `1.0.0/thesaurus.ttl` en aan het bestand op het register.

## Identifier

Vanaf versie 1.0.1-cv heeft het begrippenkader als `dct:identifier` zijn eigen persistente URI (als literal, conform DCAT-AP-NL 3.0):

- begrippenkader: `"http://begrippen.nlbegrip.nl/id/begrippenkader/nlbegrip"`
- versie: `"http://begrippen.nlbegrip.nl/id/begrippenkader/nlbegrip/1.0.1-cv"` (met `dcat:version`, en gekoppeld via `dcat:hasVersion` / `dct:isVersionOf`)

Versie 1.0.0 houdt de oorspronkelijke identifier (een link naar dit bestand op GitHub). Die is bewust niet aangepast.
