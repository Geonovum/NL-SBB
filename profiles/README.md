# profiles/ (legacy)

Deze map blijft staan om historische redenen. **Wijzig de bestanden hier niet.**

`skos-ap-nl.ttl` in deze map is versie **1.0.0** van het SHACL-profiel. De vastgestelde versie 1.0.0 van de standaard (<https://docs.geostandaarden.nl/nl-sbb/nl-sbb/>) verwijst rechtstreeks naar dit bestand:

<https://raw.githubusercontent.com/geonovum/NL-SBB/main/profiles/skos-ap-nl.ttl>

Daarom moet dit bestand gelijk blijven aan versie 1.0.0. Het is byte voor byte gelijk aan `shacl/1.0.0/skos-ap-nl.ttl` en aan <https://register.geostandaarden.nl/shacl/nl-sbb/1.0.0/skos-ap-nl.ttl>.

## Het SHACL-profiel bijhouden

Het SHACL-profiel wordt bijgehouden in de map [`shacl/`](../shacl/), met per versie een eigen submap (bijvoorbeeld `shacl/1.0.1-cv/`). Bij een release van de standaard publiceert de autodeploy van het technisch register die map op `https://register.geostandaarden.nl/shacl/nl-sbb/{versie}/skos-ap-nl.ttl`.

- Een nieuwe versie maak je in een nieuwe submap van `shacl/`.
- Een gepubliceerde versie wijzig je niet meer.
- Verwijs in documentatie naar het adres op register.geostandaarden.nl, niet naar dit bestand of naar GitHub.

`Nederlands Profiel voor Catalogi.xlsx` stamt uit de PLDN-periode (laatst gewijzigd in 2021).
