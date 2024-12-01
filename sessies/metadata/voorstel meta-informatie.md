# Voorstel meta-informatie

We richten ons in dit voorstel op de **publicatieset**, dat wil zeggen: die verzameling van beschrijvingen (van begrippen, begrippenkader(s) en collectie(s)) die als één geheel wordt gepubliceerd.

Bij de voorstel zien we een dergelijke verzameling als een **dataset** (```dcat:Dataset```), overeenkomstig DCAT. Daarnaast zien we dat een dergelijke verzameling beschikbaar zal zijn in één of meerdere formaten, dat wil zeggen: **distributies** (```dcat:Distribution```).

Als uitgangspunt gaan we uit van een voorstel dat *voldoet* aan de [DCAT-AP-NL 3.0 standaard](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/). Aspecten die we daarbij niet relevant achten voor NL-SBB hebben we weggelaten. Daarbij staat het de uitgever van dergelijke publicaties vrij om deze aspecten (en ook andere) toe te voegen aan de meta-informatie. In een enkel geval hebben we zelf ook aspecten toegevoegd, daarbij grijpen we slechts terug naar bovenliggende standaarden, zoals [W3c DCAT 3](https://www.w3.org/TR/vocab-dcat-3/) of de [originele Dublin Core standaard](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/).

In dit voorstel gaan we uit van de volgende defacto standaard manier om met begrippenkaders om te gaan, waarbij het voorstel dusdanig vrij is opgezet dat ook andere manieren mogelijk zijn:

1. Elke publicatieset is een dataset en betreft een versie van de beschrijving van begrippen uit een begrippenkader;
2. Elke publicatieset voldoet aan de NL-SBB specificatie;
3. Elke publicatieset is voor mensen leesbaar gepubliceerd op een webpagina (de *landingspagina*)
4. Een publicatieset kent mogelijk distributies waarmee de volledige beschrijving is te downloaden, conform de taalbinding van NL-SBB.
5. Elk van deze distributies afzonderlijk betreft een serialisatie van deze taalbinding, bijvoorbeeld TTL, XML of JSON.

Merk op: de XML en JSON serialisaties dienen een correcte taalbinding te bevatten. Praktisch gezien komt dit neer op RDF/XML en JSON-LD. Daarbij kunnen wel inperkingen worden gemaakt op de vorm (bijvoorbeeld een specifieke strikte vorm van XML of JSON-LD, zodat deze eenvoudig met standaard XML of JSON programmatuur is in te lezen).

## Publicatieset (dataset)

De meta-informatie MOET per publicatieset invulling geven aan de metadata-rubrieken, zoals opgenomen in onderstaande tabel. Waar de kolom "optionaliteit" een **vetgedrukte** waarde bevat, is de eis met betrekking tot die rubriek strikter dan in [DCAT-AP-NL3.0](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30). Waar de kolom "naam in NL-SBB" een *schuingedrukte* waarde bevat, is een extra rubriek toegevoegd. Rubrieken die in DCAT-AP-NL3.0 niet verplicht zijn en voor NL-SBB niet relevant, zijn weggelaten. In alle andere gevallen is DCAT-AP-NL3.0 gevolgd.

Een dataset kan in DCAT zowel betrekking hebben op een versie van een dataset als een abstractie daarvan die zelf versies heeft (bijvoorbeeld de dataset van gemeentenamen, en daar dan verschillende versies van). Voor publicatiesets speelt dit niet. We zien het begrippenkader *zelf* (skos:ConceptScheme) als de abstractie en een publicatieset als een *versie van* zo'n begrippenkader. Het staat een ieder vrij om toch een versie-loze dataset te introduceren en daarbij de eigenschap dcat:hasVersion te gebruiken om te verwijzen naar een specifieke publicatieset.

|Naam in NL-SBB|Naam in DCAT-AP-NL3.0|Taalbinding|Kardinaliteit|Optionaliteit|Toelichting|
|--------------|---------------------|-----------|-------------|-------------|-----------|
|toegangsrechten|[access rights](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-access-rights)|[dct:accessRights](http://purl.org/dc/terms/accessRights)|1..1|Verplicht|Zal in veel gevallen de categorie [«public»](http://publications.europa.eu/resource/authority/access-right/PUBLIC) zijn.|
|betreft regelgeving|[applicable legislation](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-applicable-legislation)|[dcatap:applicableLegislation](http://data.europa.eu/r5r/applicableLegislation)|0..n|Optioneel|Hiermee kun je aangeven welke regelgeving in deze publicatie is uitgewerkt. Dit zal ook op het niveau van begrippen gebeuren, indien gewenst kan dit hier worden samengevat|
|voldoet aan specificatie|[conforms to](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-conforms-to)|[dct:conformsTo](http://purl.org/dc/terms/conformsTo)|**1**..n|**Verplicht**|Moet de URL bevatten van de betreffende versie van NL-SBB|
|contactpunt|[contact point](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-contact-point)|[dcat:contactPoint](http://www.w3.org/ns/dcat#contactPoint)|1..1|Verplicht||
|bronhouder|[creator](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-creator)|[dct:creator](http://purl.org/dc/terms/creator)|1..n|Verplicht||
|beschrijving|[description](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-description)|[dct:description](http://purl.org/dc/terms/description)|1..n|Verplicht||
|distributie|[distribution](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-dataset-distribution)|[dct:distribution](http://www.w3.org/ns/dcat#distribution)|0..n|Conditioneel|Verplicht voor elk formaat waarin de publicatie beschikbaar wordt gesteld|
|identificatie|[identifier](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-identifier)|[dct:identifier](http://purl.org/dc/terms/identifier)|1..1|Verplicht||
|*naam*|[label](https://www.w3.org/TR/rdf11-schema/#ch_label)|[rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)|1..n|**Verplicht**|Gelijk aan «titel»|
|trefwoord|[keyword](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-keyword)|[dcat:keyword](http://www.w3.org/ns/dcat#keyword)|0..n|Aanbevolen||
|webpagina|[landing page](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-landing-page)|[dcat:landingPage](http://www.w3.org/ns/dcat#landingPage)|**1**..n|**Verplicht**|Dit is de webpagina waar de publicatie gevonden kan worden|
|taal|[language](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-language)|[dct:language](http://purl.org/dc/terms/language)|0..n|Aanbevolen||
|*licentie*|[license](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-licence)|[dct:license](http://purl.org/dc/terms/license)|0..1|Conditioneel|Verplicht, tenzij de licentie verschilt per distributie. De verwachting is dat dit vrijwel nooit zal gebeuren en in veel gevallen zal hier de categorie [«publiek domein»](http://creativecommons.org/publicdomain/mark/1.0/deed.nl) gekozen zijn.|
|versiedatum|[modification date](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-modification-date)|[dct:modified](http://purl.org/dc/terms/modified)|0..1|**Aanbevolen**|Aanbevolen is om deze altijd te gebruiken. Mag gelijk zijn aan «publicatiedatum»|
|*voorgaande versie*|[previous version](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_previous_version)|[dcat:previousVersion](https://www.w3.org/ns/dcat#previousVersion)|0..1|Optioneel|Gebruik deze om de vorige versie van deze publicatieset aan te geven, bijvoorbeeld een vorige ter review aangeboden versie. Gebruik juist «vervangt» om de verbinding te leggen met eerder gepubliceerde versies.|
|uitgever|[publisher](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-publisher)|[dct:publisher](http://purl.org/dc/terms/publisher)|1..1|Verplicht||
|publicatiedatum|[release date](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-release-date)|[dct:issued](http://purl.org/dc/terms/issued)|0..1|**Conditioneel**|Verplicht indien sprake is van een (definitieve) publicatie|
|*vervangt*|[replaces](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_replaces)|[dct:replaces](http://purl.org/dc/terms/replaces)|0..n|Optioneel|Gebruik deze om van een publicatieversie aan te geven welke (oudere) publicatie(s) deze vervangt.|
|status|[status](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-status)|[adms:status](http://www.w3.org/ns/adms#status)|0..1|Optioneel||
|thema|[theme](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-theme)|[dcat:theme](http://www.w3.org/ns/dcat#theme)|1..1|Verplicht||
|titel|[title](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-title)|[dct:title](http://purl.org/dc/terms/title)|1..n|Verplicht||
|versie|[version](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-version)|[dcat:version](http://www.w3.org/ns/dcat#version)|0..1|**Aanbevolen**|Aanbevolen wordt om naast de publicatiedatum ook een versie(aanduiding) op te nemen.|
|versienotities|[version notes](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-version-notes)|[adms:versionNotes](http://www.w3.org/ns/adms#versionNotes)|0..n|Optioneel||

Ter volledigheid geeft onderstaande tabel aan wat de aanpassingen zijn ten opzichte van [DCAT-AP-NL3.0](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30). Waar rubrieken niet zijn gebruikt, betreffen dit altijd rubriek die optioneel zijn in DCAT-AP-NL3.0:

|Naam in DCAT-AP-NL3.0|Afwijking|Rationale|
|---------------------|---------|---------|
|[conforms to](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-conforms-to)|Verplicht gemaakt|Dient te verwijzen naar de NL-SBB standaard, maakt duidelijk *dat* je NL-SBB volgt|
|[documentation](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-documentation)|Niet gebruikt|Voor NL-SBB lijkt deze overbodig t.o.v. landing page|
|[frequency](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-frequency)|Niet gebruikt|Weinig zinvol bij begrippen|
|[geographical coverage](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-geographical-coverage)|Niet gebruikt|Weinig zinvol bij begrippen|
|[has version](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-has-version)|Niet gebruikt|Een publicatieset *is* een versie|
|[HVD category](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-hvd-category)|Niet gebruikt|Niet van toepassing voor begrippen|
|[in series](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-in-series)|Niet gebruikt|Weinig zinvol bij begrippen|
|[is reference by](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-is-referenced-by)|Niet gebruikt|Nu nog niet in gebruik. Mogelijk zou je dit kunnen gebruiken om lineage mee te beschrijven met een MIM-model|
|[label](https://www.w3.org/TR/rdf11-schema/#ch_label)|Toegevoegd|Het is een best-practice om altijd een rdfs:label toe te voegen aan een resource, zoals de naam van een html-link bij een URL. Dit is in DCAT niet expliciet opgenomen, in NL-SBB is dit expliciet gemaakt om deze best-practice niet te vergeten|
|[landing page](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-landing-page)|Verplicht gemaakt|Dit moet de pagina zijn waar de publicatie te vinden is|
|[license](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-licence)|Herstelt vanuit DCAT|Voor begrippen is een licentie op dataset-niveau in de meeste gevallen voldoende (en niet nodig om dit per distributie te specificeren)|
|[modification date](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-modification-date)|Aanbevolen gemaakt|Bij begrippen is deze eigenschap vaak duidelijk en bijzonder relevant|
|[other identifier](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-other-identifier)|Niet gebruikt|Voor NL-SBB lijkt deze overbodig t.o.v. identifier|
|[provenance](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-provenance)|Niet gebruikt|Weinig zinvol bij begrippen. Herkomstinformatie wordt afzonderlijk beschreven|
|[qualified attribution](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-qualified-attribution)|Niet gebruikt|Lijkt niet nodig bij begrippen|
|[qualified relation](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-qualified-relation)|Niet gebruikt|Lijkt niet nodig bij begrippen|
|[related resource](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-related-resource)|Niet gebruikt|Lijkt niet nodig bij begrippen|
|[release date](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-release-date)|Conditoneel verplicht gemaakt|Elke publicatie heeft altijd een publicatiedatum, anders is er immers geen sprake van een publicatie|
|[replaces](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_replaces)|Herstelt vanuit DCAT|Voor begrippen is het relevant hoe publicaties elkaar opvolgen|
|[previous version](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_previous_version)|Herstelt vanuit DCAT|Voor begrippen kan het relevant zijn om te verwijzen naar een vorige versie (dit kan ook een conceptversie zijn)|
|[sample](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-sample)|Niet gebruikt|Niet van toepassing bij begrippen|
|[source](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-source)|Niet gebruikt|Weinig zinvol bij de publicatie zelf. Dit wordt bij de begrippen zelf bijgehouden|
|[spatial resolution](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-spatial-resolution)|Niet gebruikt|Weinig zinvol bij begrippen|
|[temporal coverage](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-temporal-coverage)|Niet gebruikt|Weinig zinvol bij begrippen. Deze eigenschap is niet bedoeld voor de geldigheidsperiode van begrippen|
|[temporal resolution](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-temporal-resolution)|Niet gebruikt|Weinig zinvol bij begrippen. Deze eigenschap is niet bedoeld voor de geldigheidsperiode van begrippen|
|[type](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-type)|Niet gebruikt|Lijkt niet nodig bij begrippen|
|[version](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-version)|Aanbevolen gemaakt|Bij publicaties is de versie(aanduiding) vaak aanwezig en bijzonder relevant|
|[was generated by](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-was-generated-by)|Niet gebruikt|Weinig zinvol bij begrippen. Herkomstinformatie wordt afzonderlijk beschreven|

## Distribution

Publicaties van begripsbeschrijvingen behoren niet alleen als voor mensen leesbare variant beschikbaar te zijn, maar ook in één of meerdere technische, machine-leesbare formaten. Voor elk van deze formaten dient een distributie beschreven te zijn in de metadata. De tabel hieronder volgt dezelfde opbouw en structuur zoals bij datasets is beschreven.

|Naam in NL-SBB|Naam in DCAT-AP-NL3.0|Taalbinding|Kardinaliteit|Optionaliteit|Toelichting|
|--------------|---------------------|-----------|-------------|-------------|-----------|
|toegangs-URL|[access URL](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-access-url)|[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL)|1..1|Verplicht|Mag gelijk zijn aan download-URL|
|download-URL|[download URL](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-download-url)|[dcat:downloadURL](http://www.w3.org/ns/dcat#downloadURL)|0..1|**Conditioneel**|Verplicht indien de distributie te downloaden is. Dit zal vrijwel altijd het geval zijn|
|bestandsformaat|[format](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-format)|[dct:format](http://purl.org/dc/terms/format)|0..1|Optioneel||
|*naam*|[label](https://www.w3.org/TR/rdf11-schema/#ch_label)|[rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)|1..n|**Verplicht**|Aanbevolen is om deze gelijk te maken aan «bestandsindeling» of aan «titel» als hiervoor is gekozen.|
|taal|[language](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-language)|[dct:language](http://purl.org/dc/terms/language)|0..1|Aanbevolen|Aanbevolen als de distributie in één taal is en/of als distributies van elkaar gescheiden zijn door taal. Gebruik taal juist niet als sprake is van meerdere talen in één distributie|
|licentie|[license](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-licence)|[dct:license](http://purl.org/dc/terms/license)|1..1|Verplicht|Neem deze over van de dataset indien deze per distributie niet verschilt|
|voldoet aan schema|[linked schemas](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-linked-schemas)|[dct:conformsTo](http://purl.org/dc/terms/conformsTo)|0..n|Aanbevolen|Aanbevolen wordt om minimaal te verwijzen naar de shape-graph van NL-SBB. Daarnaast kunnen ook berichtschemas voor technische formaten worden toegevoegd|
|bestandsindeling|[media type](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-media-type)|[dcat:mediaType](http://www.w3.org/ns/dcat#mediaType)|0..1|Conditioneel|Verplicht indien een download-URL bestaat. Dit zal vrijwel altijd het geval zijn|
|titel|[title](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataset-title)|[dct:title](http://purl.org/dc/terms/title)|0..n|Optioneel|Gebruik deze als distributies meer van elkaar verschillen dan alleen de bestandsindeling|

Ter volledigheid geeft onderstaande tabel aan wat de aanpassingen zijn ten opzichte van [DCAT-AP-NL3.0](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30). Waar rubrieken niet zijn gebruikt, betreffen dit altijd rubriek die optioneel zijn in DCAT-AP-NL3.0:

|Naam in DCAT-AP-NL3.0|Afwijking|Rationale|
|---------------------|---------|---------|
|[access service](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-access-service)|Niet gebruikt|Voor NL-SBB maken we niet gebruik van data services|
|[applicable legislation](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-applicable-legislation)|Niet gebruikt|Wordt voor begrippen op het niveau van datasets beschreven|
|[availability](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-availability)|Niet gebruikt|Weinig zinvol bij begrippen|
|[byte size](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-byte-size)|Niet gebruikt|Weinig zinvol bij begrippen|
|[checksum](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-checksum)|Niet gebruikt|Lijkt niet nodig bij begrippen|
|[compression format](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-compression-format)|Niet gebruikt|Weinig zinvol bij begrippen|
|[description](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-description)|Niet gebruikt|Weinig zinvol op het niveau van distributie|
|[documentation](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-documentation)|Niet gebruikt|Weinig zinvol bij distributies van begrippen|
|[download URL](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-download-url)|Conditioneel verplicht gemaakt|Bij distributies van begrippen zal er vrijwel altijd een download-URL zijn|
|[has policy](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-has-policy)|Niet gebruikt|Weinig zinvol bij begrippen|
|[label](https://www.w3.org/TR/rdf11-schema/#ch_label)|Toegevoegd|Het is een best-practice om altijd een rdfs:label toe te voegen aan een resource, zoals de naam van een html-link bij een URL. Dit is in DCAT niet expliciet opgenomen, in NL-SBB is dit expliciet gemaakt om deze best-practice niet te vergeten|
|[modification date](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-modification-date)|Niet gebruikt|Deze eigenschap wordt op het niveau van de dataset bijgehouden|
|[packaging format](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-packaging-format)|Niet gebruikt|Weinig zinvol bij begrippen|
|[release date](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-release-date)|Niet gebruikt|Weinig zinvol bij begrippen|
|[rights](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-rights)|Niet gebruikt|Weinig zinvol op het niveau van distributie|
|[spatial resolution](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-spatial-resolution)|Niet gebruikt|Weinig zinvol bij begrippen|
|[status](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-status)|Niet gebruikt|Weinig zinvol op het niveau van distributie|
|[temporal resolution](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#distribution-temporal-resolution)|Niet gebruikt|Weinig zinvol bij begrippen|
