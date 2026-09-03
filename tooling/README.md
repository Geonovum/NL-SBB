# Software die NL-SBB ondersteunt

Dit overzicht helpt organisaties die een begrippenkader volgens de [Nederlandse standaard voor het
beschrijven van begrippen (NL-SBB)](https://docs.geostandaarden.nl/nl-sbb/nl-sbb/) willen vastleggen
en publiceren bij het kiezen van gereedschap.

**Status van dit document:** informatief. Het maakt geen deel uit van de standaard en heeft geen
normatieve status. Geonovum certificeert of keurt geen software: opname in dit overzicht is
géén goedkeuring, aanbeveling of conformiteitsverklaring. De informatie is gebaseerd op
openbare informatie van leveranciers en op meldingen uit de werkgroep, en is niet door Geonovum
getest. Controleer bij een keuze altijd zelf bij de leverancier wat een product actueel ondersteunt.

**Peildatum:** 2 september 2026.

## Soorten ondersteuning

| Aanduiding | Betekenis |
| --- | --- |
| **Specifiek** | Het product is (mede) voor NL-SBB gemaakt: de kenmerken uit de standaard zitten er ingebouwd in en je kunt er zonder eigen inrichtingswerk NL-SBB-conforme begrippenkaders in vastleggen. |
| **Configureerbaar** | Het product is een generieke thesaurus-, taxonomie- of ontologie-omgeving die niet specifiek voor NL-SBB is gemaakt, maar die met eigen schema's — in de meeste gevallen met het [SHACL-profiel van NL-SBB](https://register.geostandaarden.nl/shacl/nl-sbb/1.0.0/skos-ap-nl.ttl) — voor gebruik met de standaard ingericht kan worden. |
| **Publicatie en ontsluiting** | Het product is niet bedoeld om begrippen te maken of te bewerken, maar om een bestaand begrippenkader te publiceren, te doorzoeken en te doorbladeren. |

Omdat de taalbinding van NL-SBB op SKOS gebaseerd is, kan in principe elk hulpmiddel dat SKOS
kan lezen en schrijven met NL-SBB-begrippenkaders werken. Het verschil zit in hoeveel je zelf
moet inrichten en hoe goed de tool je helpt de verplichte kenmerken en de kwaliteitsregels van
de standaard te halen. Zie ook de [mapping tussen NL-SBB en SKOS](https://github.com/Geonovum/nl-sbb-bp/blob/main/mapping-skos.md)
in de best practices.

## Licentiemodel en herkomst

| Aanduiding | Betekenis |
| --- | --- |
| **Overheid** | Ontwikkeld en/of beheerd door een overheidsorganisatie of door de beheerorganisatie van de standaard, en als voorziening of hulpmiddel aangeboden. Geen licentiekosten. |
| **Open source** | De broncode is openbaar en onder een opensourcelicentie te gebruiken. Je installeert en beheert de software zelf, of gebruikt een instantie die een ander beheert. |
| **Commercieel** | Broncode niet openbaar; gebruik op basis van een betaalde licentie of abonnement. |

De categorieën sluiten elkaar niet uit: VocBench 3 is open source *en* wordt door een
overheidsorganisatie beheerd, namelijk het Publications Office van de Europese Unie.

| Product | Categorie | Bijzonderheden |
| --- | --- | --- |
| Excel-sjabloon NL-SBB | Overheid (beheerorganisatie) | Geleverd door Geonovum als beheerder van NL-SBB; vrij te gebruiken. |
| Begrippeneditor (Begrippenvoorziening) | Overheid | Voorziening van Logius; geen licentiekosten. Broncode is niet openbaar gepubliceerd. |
| VocBench 3 | Open source, beheer door overheidsorganisatie | Zelf te installeren; er zijn ook instanties van de EU en van PLDN. |
| Skosmos | Open source | MIT-licentie; zelf te installeren, met PHP en een SPARQL-endpoint. |
| BegrippenXL | Commercieel | SaaS |
| ModelDesk | Commercieel | SaaS, licentie per seat |
| PoolParty Semantic Suite | Commercieel | Licentie in bundels |
| Progress Semaphore | Commercieel | — |
| TopBraid EDG | Commercieel | Licentie per pakket, uit te breiden |
| TriplyDB | Commercieel | Gratis account voor open data; eigen instanties mogelijk |

## Specifiek voor NL-SBB gemaakte producten en hulpmiddelen

| Product | Aanbieder | Soort | Licentiemodel |
| --- | --- | --- | --- |
| [Excel-sjabloon NL-SBB](#excel-sjabloon-nl-sbb) | Geonovum (beheerder van NL-SBB) | Spreadsheet-sjabloon | Vrij te gebruiken |
| [Begrippeneditor (Begrippenvoorziening)](#begrippeneditor--begrippenvoorziening) | Logius | Webapplicatie, overheidsvoorziening | Overheid, geen licentiekosten |
| [BegrippenXL](#begrippenxl) | ArchiXL | Thesaurusplatform (SaaS) | Commercieel |
| [ModelDesk](#modeldesk) | ModelDesk | Webapplicatie (SaaS) | Commercieel, licentie per seat |

### Excel-sjabloon NL-SBB

- **Aanbieder:** Geonovum, beheerder van de standaard
- **Bestand:** [`Template_NL_SBB.xlsx`](Template_NL_SBB.xlsx) in deze repository
- **Wat het is:** een spreadsheet-sjabloon om begrippen op een uniforme manier vast te leggen volgens
  NL-SBB. Het bevat de bladen *Overzicht*, *Begrippenkaders*, *Begrippen*, *Collecties*,
  *Brondocumenten* en *Legenda*. De kolommen volgen de kenmerken uit de standaard — onder meer URI,
  voorkeursterm, definitie, uitleg, alternatieve en zoektermen, code, hiërarchische en associatieve
  relaties, mapping-relaties, notities en herkomstgegevens. Het blad *Legenda* legt elke eigenschap uit.
- **Bedoeld gebruik:** de laagdrempelige manier om te beginnen, en als bron voor een latere conversie
  naar RDF, zodat het begrippenkader als linked data gepubliceerd en hergebruikt kan worden. Die
  conversie zit niet in het sjabloon zelf.
- **Niet bedoeld voor:** complexere begrippenkaders met veel relaties, grootschalige bewerkingen, of
  gebruik als import- en uitwisselformaat tussen tools. Gebruik daarvoor een begrippeneditor of een
  linked-datatool, met RDF in combinatie met het NL-SBB SHACL-profiel als uitwisselformaat.
- **Licentiemodel:** vrij te gebruiken, geen licentiekosten. De standaard zelf wordt onder
  CC BY gepubliceerd.

### Begrippeneditor / Begrippenvoorziening

- **Aanbieder:** Logius
- **Website:** [editor.stelselcatalogus.nl](https://editor.stelselcatalogus.nl/), achtergrond op
  [logius.nl](https://www.logius.nl/onze-dienstverlening/gegevensuitwisseling/begrippenvoorziening/over-begrippenvoorziening)
- **Wat het is:** de Begrippenvoorziening bestaat uit twee delen: de **Begrippeneditor**, waarmee
  data leverende organisaties hun begrippen volgens NL-SBB beschrijven, en de **Begrippencatalogus**
  ([begrippen.stelselcatalogus.nl](https://begrippen.stelselcatalogus.nl)), waarin gebruikers
  begrippen en begrippenkaders kunnen zoeken. De catalogus is voor iedereen vrij toegankelijk.
- **NL-SBB-ondersteuning:** de invoervelden van de editor volgen de standaard; de veldtoelichting
  verwijst naar de NL-SBB-documentatie.
- **Uitwisseling:** een in de editor opgesteld begrippenkader kan omgezet worden naar linked data
  en aan de eigenaar geleverd worden. De organisatie die het kader aanmaakt blijft eigenaar.
  Publiceren in de Begrippencatalogus is niet verplicht, maar wel gewenst en gaat via een verzoek
  aan Logius.
- **Aandachtspunt:** de voorziening richt zich op organisaties die overheidsdata leveren en
  ondersteunt het Federatief Datastelsel. Neem voor toegang contact op met Logius.
- **Licentiemodel:** overheidsvoorziening, geen licentiekosten. De broncode is niet openbaar
  gepubliceerd.

### BegrippenXL

- **Aanbieder:** ArchiXL
- **Website:** [BegrippenXL-thesaurusplatform](https://www.archixl.nl/nl/producten/begrippenxl-thesaurusplatform/),
  platform op [begrippenxl.nl](https://www.begrippenxl.nl/)
- **Wat het is:** een thesaurusplatform om begrippen vast te leggen, aan elkaar te relateren, te
  doorzoeken en gebruikersvriendelijk te publiceren. Het platform bestaat uit meerdere onderdelen:
  - de **[begrippenmanager](https://www.archixl.nl/nl/producten/begrippenxl-thesaurusplatform/begrippenxl-begrippenmanager/)**,
    een losse module om begrippen — desgewenst meertalig — te definiëren, te relateren en over te
    nemen uit andere begrippenkaders;
  - het **beheerportaal**, waarin je begrippenkaders als bestand kunt uploaden en activeren;
  - het **publicatieplatform**, dat de begrippen doorzoekbaar en toegankelijk publiceert.
- **NL-SBB-ondersteuning:** ArchiXL noemt NL-SBB expliciet als ondersteunde standaard voor de
  begrippenmanager.
- **Uitwisseling:** RDF/Turtle en CSV; bulkbewerkingen via een Excel-achtige interface. Het
  beheerportaal ondersteunt de gangbare linked-dataformaten, waaronder TTL en RDF/XML.
- **Onderscheidend punt:** de integratie tussen begrippen en de inhoud die een organisatie in
  WikiXL of ArchiMedes vastlegt: die kunnen aan elkaar gerelateerd en integraal getoond worden.
- **Licentiemodel:** commercieel, als SaaS-dienst.

### ModelDesk

- **Aanbieder:** ModelDesk
- **Website:** [modeldesk.io](https://modeldesk.io/nl/product)
- **Wat het is:** webomgeving voor informatiemodelleurs om modellen te importeren, modelleren,
  transformeren, valideren en publiceren, met automatisch gegenereerde klassendiagrammen en
  formuliergebaseerd bewerken.
- **NL-SBB-ondersteuning:** de leverancier meldt NL-SBB-functionaliteit waarmee informatiemodellen
  direct aan NL-SBB-begrippen gekoppeld kunnen worden. Op de productpagina zelf worden MIM, UML,
  ER, RDFS/OWL/SHACL, XSD en JSON Schema als ondersteunde standaarden genoemd; NL-SBB staat daar
  (nog) niet bij. Vraag de actuele stand na bij de leverancier.
- **Uitwisseling:** import van XMI, RDF (Turtle, RDF/XML, JSON-LD) en XSD; export naar MIM-XML, XMI,
  RDF (Turtle, RDF/XML, JSON-LD, N-Triples, N3), XSD en JSON Schema.
- **Onderscheidend punt:** de combinatie met informatiemodellering (MIM).
- **Aandachtspunt:** de omgeving is cloudgebaseerd met opslag in de EU en kent versiebeheer met
  commits en benoemde versies.
- **Licentiemodel:** commercieel, seat-gebaseerd per organisatie. Prijzen zijn niet openbaar.

## Generieke tools die met het NL-SBB SHACL-profiel ingericht kunnen worden

| Product | Aanbieder | Soort | Licentiemodel |
| --- | --- | --- | --- |
| [VocBench 3](#vocbench-3) | Publications Office of the EU / Universiteit van Rome Tor Vergata | Webapplicatie, zelf te installeren | Open source (overheid) |
| [TopBraid EDG](#topbraid-edg) | TopQuadrant | Webapplicatie | Commercieel, licentie per pakket |
| [PoolParty Semantic Suite](#poolparty-semantic-suite) | Graphwise (Semantic Web Company) | Webapplicatie | Commercieel |
| [Progress Semaphore](#progress-semaphore) | Progress Software | Webapplicatie | Commercieel |
| [TriplyDB](#triplydb) | Triply B.V. | Webapplicatie (publieke of eigen instantie) | Commercieel, gratis account voor open data |

### VocBench 3

- **Aanbieder:** beheerd door het Publications Office of the European Union; de onderliggende
  technologie (Semantic Turkey) wordt ontwikkeld door de ART Research Group van de Universiteit van
  Rome Tor Vergata. De ontwikkeling wordt gefinancierd uit het Digital Europe Programme.
- **Website:** [vocbench.uniroma2.it](https://vocbench.uniroma2.it/) (documentatie en download),
  [vocbench.op.europa.eu](https://vocbench.op.europa.eu/) (instantie van de EU). PLDN heeft een
  eigen instantie op [vocbench.pldn.nl](http://vocbench.pldn.nl/vocbench3).
- **Wat het is:** meertalig, collaboratief webplatform voor het beheren van OWL-ontologieën,
  SKOS(-XL)-thesauri, OntoLex-lemon-lexicons en generieke RDF-datasets.
- **Inrichting voor NL-SBB:** de SKOS(-XL)-basis sluit direct aan op de taalbinding van NL-SBB.
  Extra NL-SBB-kenmerken kunnen met Custom Forms in de invoerschermen worden opgenomen. Validatie
  tegen het SHACL-profiel is geen gedocumenteerde kernfunctie; reken erop dat je daarvoor een
  aparte SHACL-validatiestap inricht.
- **Licentiemodel:** open source; broncode en binaries staan op de downloadpagina.

### TopBraid EDG

- **Aanbieder:** TopQuadrant
- **Website:** [topquadrant.com](https://www.topquadrant.com/), documentatie op
  [docs.topquadrant.com](https://docs.topquadrant.com/)
- **Wat het is:** webgebaseerde omgeving voor data governance, met onder meer business glossaries,
  taxonomieën, ontologieën en referentiegegevens als beheerobjecten.
- **Inrichting voor NL-SBB:** SHACL is de kern van het product. Taxonomieën zijn op SKOS en
  SKOS-XL gebaseerd, en eigen SHACL-shapes bepalen zowel de validatieregels als de opbouw van de
  invoerformulieren. Het NL-SBB-profiel kan daarmee als shapes-graaf worden ingebracht.
  Ondersteunde standaarden: RDF, OWL, SKOS, SHACL, SPARQL en GraphQL.
- **Licentiemodel:** commercieel, met pakketten (bijvoorbeeld alleen glossaries of referentiedata)
  die later uitgebreid kunnen worden.

### PoolParty Semantic Suite

- **Aanbieder:** Graphwise, ontstaan uit de samenvoeging van Semantic Web Company en Ontotext
- **Website:** [poolparty.biz](https://www.poolparty.biz/)
- **Wat het is:** platform voor taxonomie- en thesaurusbeheer, tekstmining, kennisgrafen en
  semantisch zoeken.
- **Inrichting voor NL-SBB:** PoolParty werkt met SKOS en SKOS-XL en heeft een ingebouwde validator
  die de SKOS-conformiteit van de uitvoer controleert. Aanvullende NL-SBB-kenmerken leg je vast met
  een eigen ontologie en een *custom scheme*; de standaard-SKOS(-XL)-schema's zelf zijn niet
  aanpasbaar. Of het NL-SBB SHACL-profiel rechtstreeks als validatieregels ingelezen kan worden,
  is uit de openbare documentatie niet vast te stellen — navragen bij de leverancier.
- **Licentiemodel:** commercieel, in bundels.

### Progress Semaphore

- **Aanbieder:** Progress Software (voorheen Smartlogic)
- **Website:** [progress.com/semaphore](https://www.progress.com/semaphore)
- **Wat het is:** no-code metadata-platform voor semantische kennismodellen, met geautomatiseerde
  classificatie en informatie-extractie uit ongestructureerde bronnen.
- **Inrichting voor NL-SBB:** het kerndatamodel omvat SKOS-XL, RDF(S), OWL en SHACL-shapes,
  waarmee het NL-SBB-profiel als model ingebracht kan worden. De productpagina zelf specificeert de
  ondersteunde standaarden niet; de productdocumentatie is daarvoor de bron.
- **Licentiemodel:** commercieel.

### TriplyDB

- **Aanbieder:** Triply B.V. (Nederland)
- **Website:** [triply.cc](https://triply.cc/), documentatie op
  [docs.triply.cc](https://docs.triply.cc/), publieke instantie
  [triplydb.com](https://triplydb.com/). PLDN heeft een eigen instantie op
  [data.pldn.nl](https://data.pldn.nl/).
- **Wat het is:** platform om linked data op te slaan, te structureren, te bevragen met SPARQL en
  te publiceren, inclusief API's, zoekindexen en data stories.
- **Inrichting voor NL-SBB:** TriplyDB heeft een **Editor** die invoerformulieren genereert op basis
  van de SHACL node shapes in de shapes graph van een dataset; de documentatie noemt expliciet het
  vastleggen van SKOS-conceptschema's en DCAT-catalogi op deze manier. Door het NL-SBB-profiel als
  shapes graph te gebruiken krijg je dus formulieren met de NL-SBB-kenmerken, waarbij verplichte
  velden bij het opslaan worden afgedwongen. Voor klassen zonder shape kunnen node shapes vanuit het
  datamodel gegenereerd worden. Validatie tegen een shapes graph is daarnaast beschikbaar in
  TriplyETL.
- **Uitwisseling:** RDF, met publicatie via SPARQL-endpoints, API's en downloadbare bestanden.
- **Aandachtspunt:** de Editor is niet in alle instanties van TriplyDB beschikbaar. Ga bij Triply na
  of hij in jouw instantie of abonnement zit.
- **Licentiemodel:** commercieel. Er is een gratis account voor open data, waarbij de eerste miljoen
  triples gratis gehost worden; verder abonnementen en eigen instanties.

## Publicatie en ontsluiting

| Product | Aanbieder | Soort | Licentiemodel |
| --- | --- | --- | --- |
| [Skosmos](#skosmos) | Nationale Bibliotheek van Finland | Webapplicatie, zelf te installeren | Open source (MIT) |

Publiceren kan ook onderdeel zijn van een product uit de vorige twee categorieën: de
[Begrippencatalogus](https://begrippen.stelselcatalogus.nl) hoort bij de Begrippenvoorziening van
Logius, BegrippenXL heeft een eigen publicatieplatform, en TriplyDB publiceert via
SPARQL-endpoints en API's.

### Skosmos

- **Aanbieder:** Nationale Bibliotheek van Finland (NatLibFi)
- **Website:** [skosmos.org](https://skosmos.org/), broncode op
  [github.com/NatLibFi/Skosmos](https://github.com/NatLibFi/Skosmos). De bekendste instantie is de
  Finse vocabulairedienst [Finto](https://finto.fi/).
- **Wat het is:** een webapplicatie om SKOS-vocabulaires te publiceren, doorzoekbaar te maken en te
  doorbladeren, met een meertalige gebruikersinterface, visualisatie van begrippenhiërarchieën, een
  REST-API en linked-data-ontsluiting. Het is een viewer en publicatieplatform: je bewerkt de
  begrippen elders en publiceert het resultaat met Skosmos.
- **Inrichting voor NL-SBB:** Skosmos leest de begrippen uit een SPARQL-endpoint (in de praktijk vaak
  Jena Fuseki) en wordt per vocabulaire ingericht met een klein configuratiebestand in Turtle:
  naam, endpoint, ondersteunde talen, weergave van de hiërarchie en het gebruik van
  SKOS-collecties. Skosmos is niet beperkt tot SKOS Core — het ondersteunt ook Dublin
  Core-eigenschappen en ISO-uitbreidingen op SKOS, wat aansluit bij de taalbinding van NL-SBB. Voor
  kenmerken die daarbuiten vallen is aanvullende configuratie of maatwerk in de templates nodig.
- **Aandachtspunt:** je beheert zelf de installatie (PHP en een SPARQL-endpoint). Valideren tegen het
  SHACL-profiel doe je vooraf, in de editor of met een aparte validator.
- **Licentiemodel:** open source onder de MIT-licentie.

## Aan de slag met een generieke tool

Wil je een generieke tool voor NL-SBB inrichten, dan zijn dit de onderdelen die je zelf regelt:

1. **Het profiel inlezen.** Het SHACL-profiel staat op
   [register.geostandaarden.nl/shacl/nl-sbb/1.0.0/skos-ap-nl.ttl](https://register.geostandaarden.nl/shacl/nl-sbb/1.0.0/skos-ap-nl.ttl)
   en in deze repository in [`profiles/skos-ap-nl.ttl`](../profiles/skos-ap-nl.ttl). In tools die
   SHACL als schema gebruiken bepaalt het profiel meteen welke velden in de formulieren verschijnen.
2. **Verplichte en aanbevolen kenmerken.** Zorg dat de kenmerken uit
   [hoofdstuk 2](https://docs.geostandaarden.nl/nl-sbb/nl-sbb/#kenmerken-van-begrippen) vastgelegd
   kunnen worden, inclusief de publieksvriendelijke definitie.
3. **URI-strategie.** Kies persistente URI's voor begrippen en begrippenkader, zodat andere
   catalogi naar je begrippen kunnen verwijzen.
4. **Validatie inrichten.** Valideer de uitvoer tegen het SHACL-profiel. Een begrippenkader met een
   of meer `sh:Violation`-meldingen is niet conform de standaard; `sh:Warning` en `sh:Info` gaan over
   kwaliteit en aanbevelingen. Zie
   [hoofdstuk 5](https://docs.geostandaarden.nl/nl-sbb/nl-sbb/#conformiteit). Kan de tool zelf niet
   tegen SHACL valideren, dan kun je daarvoor een losse opensource-validator gebruiken, zoals
   [pySHACL](https://github.com/RDFLib/pySHACL) of de
   [SHACL API van TopQuadrant](https://github.com/TopQuadrant/shacl) — beide Apache 2.0.
5. **Publicatie.** Bepaal hoe het begrippenkader beschikbaar komt, bijvoorbeeld als linked data via
   een eigen catalogus of via de [Begrippencatalogus](https://begrippen.stelselcatalogus.nl) van Logius.

Wil je klein beginnen, zonder meteen een tool in te richten? Gebruik dan het
[Excel-sjabloon](#excel-sjabloon-nl-sbb) van Geonovum als tussenstap.

## Aanvullingen en correcties

Ontbreekt er software, of is informatie verouderd? Help dit overzicht dan actueel te houden.

1. **Bij voorkeur: een pull request.** Werk dit bestand bij en dien de wijziging in als
   [pull request](https://github.com/Geonovum/NL-SBB/compare). Je kunt het bestand ook
   [direct in GitHub bewerken](https://github.com/Geonovum/NL-SBB/edit/main/tooling/README.md);
   GitHub maakt dan zelf een fork en een pull request voor je aan.
2. **Als dat niet lukt:** meld het dan via een
   [issue](https://github.com/Geonovum/NL-SBB/issues/new).

Vermeld in beide gevallen in ieder geval: naam en aanbieder, een openbare verwijzing naar de
NL-SBB- of SKOS-ondersteuning, het licentiemodel en de ondersteunde uitwisselingsformaten.
