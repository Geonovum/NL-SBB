# Over het adopteren van NL-SBB en het verbinden met SKOS begrippen 

Het beschrijven en uitwisselen van begrippen is geen nieuwe aanpak.
Het is dan ook niet verassend dat er verschillende standaarden en methodieken bestaan voor het vastleggen van begrippen.
Huidige beschrijvingen van begrippen zijn dan ook divers.
NL-SBB is gebaseerd op een aantal van deze standaarden.
Met name vanuit SKOS en ISO 25964 is er een duidelijke samenhang met NL-SBB.
Bij reeds bestaande begrippenkaders is de kans groot dat of ISO 25964 danwel SKOS toegepast is.
Hoe maak je zelf de overstap naar NL-SBB en hoe kan je begrippen van derden toepassen die wellicht geen NL-SBB hanteren?
In dit hoofdstuk kijken we vooral naar SKOS, een PTOLU-standaard, en minder naar ISO25964 omdat bij de ontwikkeling van SKOS en de doorontwikkeling van ISO25964 reeds keken is naar de compatibiliteit tussen deze standaarden (zie [Correspondence](https://groups.niso.org/higherlogic/ws/public/download/12351/Correspondence%20ISO25964-SKOSXL-MADS-2013-12-11.pdf).

## Aanvullingen en aanscherpingen
Aanvullingen en aanscherpingen t.o.v. SKOS worden per objecttype (begrip, begrippenkader, collectie en brondocument) in NL-SBB weergegeven.

### Begrip

Aanscherpingen t.o.v. SKOS:
- Een begrip MOET een voorkeursterm hebben. In SKOS is dit optioneel.
- Een begrip MOET in een begrippenkader vallen. In SKOS kunnen begrippen los van een begrippenkader gedefinieerd worden.
- Een begrip MOET een definitie hebben. In SKOS is dit optioneel.
- Voor lexicale labels MOET expliciet vermeld worden in welke taal ze zijn opgesteld.
  Dit geldt voor «voorkeursterm», «alternatieve term» en «zoekterm». In SKOS is dit optioneel.
- Een code MOET een literal zijn. In SKOS is het bereik effectief iedere rdfs:Resource.
- Voor notities MOET expliciet vermeld in welke taal ze zijn opgesteld. 
  Dit geldt voor «definitie», «wijzigingsnotitie», «redactionele notitie», «historie notitie», «toelichting» en «voorbeeld». In SKOS wordt tevens een IRI als waardebereik toegestaan.
- Een topconcept MOET geen bovenliggende begrippen hebben. In SKOS mag dit wel.

Aanvullend t.o.v. SKOS:
- Voor een begrip MAG een uitleg gegeven worden.
- Voor een begrip MAG een brondocument gegeven worden.
- Voor een begrip MAG een naam gegeven worden.
- Voor een begrip MOGEN hiërarchische relaties uitgedrukt worden in de specifieke vormen die gedefinieerd worden in ISO 25964.
  Dit zijn «is specialisatie van», «is generalisatie van», «is onderdeel van», «omvat», «is exemplaar van» en «is categorie van».

De aanscherpingen en aanvullingen zijn weergegeven in de volgende tabel.

| NL-SBB - term                     | SKOS - term                | NL-SBB waardebereik | SKOS waardebereik  | NL-SBB kardinaliteit | SKOS-kardinaliteit |
| --------------------------------- | -------------------------- | ------------------- | ------------------ | -------------------- | ------------------ |
| voorkeursterm                     | skos:prefLabel             | **rdf:langString**  | plain literal      | **1..***             | 0..*               |
| alternatieve term                 | skos:altLabel              | **rdf:langString**  | plain literal      | 0..*                 | 0..*               |
| zoekterm                          | skos:hiddenLabel           | **rdf:langString**  | plain literal      | 0..*                 | 0..*               |
| code                              | skos:notation              | sh:Literal          | typed literal      | 0..*                 | 0..*               |
| in kader                          | skos:inScheme              | skos:ConceptScheme  | skos:ConceptScheme | **1..***             | 0..*               |
| is topbegrip van                  | skos:topConceptOf          | skos:ConceptScheme  | skos:ConceptScheme | 0..*                 | 0..*               |
| **uitleg**                        | rdfs:comment               | rdf:langString      | --                 | 0..*                 | --                 |
| definitie                         | skos:definition            | **rdf:langString**  | rdfs:Resource      | **1..***             | 0..*               |
| **heeft bron**                    | dct:source                 | foaf:Document       | --                 | 0..*                 | --                 |
| heeft bovenliggend begrip         | skos:broader               | skos:Concept        | skos:Concept       | 0..*                 | 0..*               |
| heeft onderliggend begrip         | skos:narrower              | skos:Concept        | skos:Concept       | 0..*                 | 0..*               |
| is gerelateerd aan                | skos:related               | skos:Concept        | skos:Concept       | 0..*                 | 0..*               |
| wijzigingsnotitie                 | skos:changeNote            | **rdf:langString**  | rdfs:Resource      | 0..*                 | 0..*               |
| redactionele notitie              | skos:editorialNote         | **rdf:langString**  | rdfs:Resource      | 0..*                 | 0..*               |
| historie notitie                  | skos:historyNote           | **rdf:langString**  | rdfs:Resource      | 0..*                 | 0..*               |
| toelichting                       | skos:scopeNote             | **rdf:langString**  | rdfs:Resource      | 0..*                 | 0..*               |
| voorbeeld                         | skos:example               | **rdf:langString**  | rdfs:Resource      | 0..*                 | 0..*               |
| heeft overeenkomstig bovenliggend | skos:broadMatch            | skos:Concept        | skos:Concept       | 0..*                 | 0..*               |
| heeft overeenkomstig onderliggend | skos:narrowMatch           | skos:Concept        | skos:Concept       | 0..*                 | 0..*               |
| is vrijwel overeenkomstig         | skos:closeMatch            | skos:Concept        | skos:Concept       | 0..*                 | 0..*               |
| is exact overeenkomstig           | skos:exactMatch            | skos:Concept        | skos:Concept       | 0..*                 | 0..*               |
| is overeenkomstig verwant         | skos:relatedMatch          | skos:Concept        | skos:Concept       | 0..*                 | 0..*               |
| **is specialisatie van**          | isothes:broaderGeneric     | skos:Concept        | skos:Concept       | 0..*                 | --                 |
| **is generalisatie van**          | isothes:narrowerGeneric    | skos:Concept        | skos:Concept       | 0..*                 | --                 |
| **is onderdeel van**              | isothes:broaderPartitive   | skos:Concept        | skos:Concept       | 0..*                 | --                 |
| **omvat**                         | isothes:narrowerPartitive  | skos:Concept        | skos:Concept       | 0..*                 | --                 |
| **is exemplaar van**              | isothes:broaderInstantial  | skos:Concept        | skos:Concept       | 0..*                 | --                 |
| **is categorie van**              | isothes:narrowerInstantial | skos:Concept        | skos:Concept       | 0..*                 | --                 |
| **naam**                          | rdfs:label                 | rdf:langString      | ---                | 0..*                 | --                 |

### Begrippenkader

Aanvullingen
- Een begrippenkader MOET een naam hebben. SKOS doet hier geen uitspraken over.
- Een begrippenkader MAG een uitleg hebben. SKOS doet hier geen uitspraken over.

| NL-SBB - term   | SKOS - term        | NL-SBB waardebereik | SKOS waardebereik | NL-SBB kardinaliteit | SKOS-kardinaliteit |
| --------------- | ------------------ | ------------------- | ----------------- | -------------------- | ------------------ |
| **naam**        |                    | rdf:langString      |                   | 1..*                 |                    |
| **uitleg**      |                    | rdf:langString      |                   | 0..*                 |                    |
| heeft topbegrip | skos:hasTopConcept | skos:Concept        | skos:Concept      | 0..*                 | 0..*               |

### Collecties

Aanvullingen
- Een collectie MOET een naam hebben. SKOS doet hier geen uitspraken over.
- Een collectie MAG een uitleg hebben. SKOS doet hier geen uitspraken over.

Aanscherpingen
- NL-SBB doet geen uitspraken over geordende collecties. SKOS wel.

| NL-SBB - term | SKOS - term | NL-SBB waardebereik             | SKOS waardebereik               | NL-SBB kardinaliteit | SKOS-kardinaliteit |
| ------------- | ----------- | ------------------------------- | ------------------------------- | -------------------- | ------------------ |
| **naam**      |             | rdf:langString                  |                                 | 1..*                 |                    |
| **uitleg**    |             | rdf:langString                  |                                 | 0..*                 |                    |
| bevat         | skos:member | skos:Concept OR skos:Collection | skos:Concept OR skos:Collection | 0..*                 | 0..*               |


### Brondocument

| NL-SBB - term      | SKOS - term | NL-SBB waardebereik | SKOS waardebereik | NL-SBB kardinaliteit | SKOS-kardinaliteit |
| ------------------ | ----------- | ------------------- | ----------------- | -------------------- | ------------------ |
| **naam**           |             | rdf:langString      |                   | 1..*                 |                    |
| **uitleg**         |             | rdf:langString      |                   | 0..*                 |                    |
| **url**            |             | sh:IRI              |                   | 0..*                 |                    |
| **bronverwijzing** |             | xsd:string          |                   | 0..*                 |                    |

Aanvullingen
- Een brondocument MOET een naam hebben. SKOS kent brondocumenten niet.
- Een brondocument MAG een uitleg hebben. SKOS kent brondocumenten niet.
- Een brondocument MAG een url hebben. SKOS kent brondocumenten niet.
- Een brondocument MAG een bronverwijzing hebben. SKOS kent brondocumenten niet.

## Adoptie van NL-SBB
Zoals gesteld bestaan er veel beschrijvingen van begrippen en over het algemeen wordt hier SKOS toegepast.
Voor steeds meer begrippen, waaronder de bestaande begrippen, zal NL-SBB geadopteerd worden.
Hierbij komen er een drietal vragen naar voren vanuit het perspectief van beheerders van begrippen:
1) Wat zijn de implicaties als ik de overstap van SKOS naar NL-SBB maak?
2) Als ik dat heb gedaan; kan ik dan nog begrippen van anderen gebruiken die niet op basis van NL-SBB zijn beschreven?
3) Kunnen anderen (die geen NL-SBB gebruiken) mijn begrippen nog gebruiken?

Voor het gemak gebruiken we de term `SKOS-begrip` wanneer we het over één of meerdere begrippen of geheel begrippenkader hebben die zijn beschreven op basis van SKOS en `NL-SBB-begrip` wanneer deze zijn beschreven op basis van NL-SBB.

###  1. Wat zijn de implicaties als ik de overstap van SKOS naar NL-SBB maak?
In de veel gevallen hoeft er voor de overstap niks gedaan te worden, SKOS wordt ondersteund in NL-SBB.
Het conceptueel model van SKOS en NL-SBB zijn in lijn met elkaar.
De informatie die een SKOS-begrip vangt kan dan ook begrepen worden met een NL-SBB bril.
Van omzetting is eigenlijk ook geen sprake.
Waar het vooral om gaat is het toepassen van de afspraken die in NL-SBB beschreven zijn.
Alhoewel er grote overlap is tussen NL-SBB en SKOS, is het zo dat NL-SBB op logisch niveau eisen stelt aan de beschrijving van een begrip die niet afgedwongen worden vanuit SKOS.
Je kan er daarom niet vanuit gaan dat een willekeurig begrip; waarvan de beschrijving voldoet aan SKOS, deze óók voldoet aan NL-SBB.
Met name de aanscherpingen, die reeds benoemd zijn, kunnen om aanvullende aandacht vragen.
Wanneer een SKOS-begrip niet conform het toepassingsprofiel van NL-SBB blijkt (bijvoorbeeld omdat deze geen definitie heeft) is menselijke tussenkomst nodig om de problemen op te lossen.

Daarnaast biedt NL-SBB kaders voor het vastleggen van informatie die niet in SKOS worden gedefinieerd. 
Denk aan het verwijzen naar bronnen en het bieden van een toelichting bij een begrip. 
Deze toevoegingen zijn optioneel en vormen geen hindernis in het kader van de overstap. 
Als deze toevoegingen al onderdeel zijn van het SKOS-begrip; maar niet conform NL-SBB blijken is hier wel een omzetting noodzakelijk. Een voorbeeld zou zijn dat een andere taalbinding is gekozen voor «heeft bron».

Als we niet vanuit data maar vanuit de presentatie kijken zien we dat ook hier impact is.
Een doel van NL-SBB is dat we dezelfde taal spreken als we het hebben over begrippen en dat zo begrippencatalogi onderling meer interoperabel zijn en beter begrepen worden door gebruikers.
Dit wordt bereikt omdat gebruikers dezelfde termen tegen komen met steeds dezelfde betekenis.
Dit is een gevolg van het consistent gebruiken van eenzelfde conceptueel model.
Mogelijk moet de presentatie (de user interface) van begrippencatalogi aangepast worden om de vastgestelde (Nederlandse) termen te hanteren bij het presenteren van beschrijvingen van begrippen.
Deze aanpassing heeft geen verdere invloed op beschrijvingen zelf.

### 2. Kan ik begrippen van anderen (die alleen SKOS volgen) gebruiken?
Met NL-SBB-begrippen kan je nog steeds gebruik maken van SKOS-begrippen. 
Wel blijven de afwegingen die bij vraag 1 benoemd zijn. 
Het gebruik van (externe) SKOS-begrippen kan op twee manieren 1) door ernaar te verwijzen met harmonisatierelaties of 2) door ze op te nemen in het eigen begrippenkader (met «in kader»).
Een SKOS-begrip (let op dat we het hier over de beschrijving hebben) is niet direct óók een NL-SBB-begrip.
Met name bij het opnemen van een extern begrip in je eigen begrippenkader zal dit een aandachtspunt zijn.
Wanneer problemen ontstaan, kan (met passende metadatering) het SKOS-begrip aangevuld worden om fouten te mitigeren.
Er kan ook gekozen worden om een nieuw begrip te beschrijven die geharmoniseerd wordt (bijvoorbeeld met «is exact overeenkomstig») met het externe begrip. 
Voor externe begrippen kan er ook gekozen worden om deze niet te valideren. De best-practice hierin moet nog gekozen worden.
Bij het verbinden van begrippenkaders is het belangrijkste dat het conceptueel model (de ontologie) aansluit. En dat is het geval.

### 3. Kunnen anderen (die geen NL-SBB gebruiken) mijn begrippen nog gebruiken?
Hergebruik van een begrip uit een NL-SBB beschrijving binnen een SKOS-begrip is altijd mogelijk.
Toepassing van NL-SBB leidt tot een beschrijving die uitgedrukt kan worden in (en conformeert aan) SKOS.
Iedere tool die SKOS ondersteund kan hiermee overweg.
SKOS staat toe dat het conceptueel model wordt uitgbreid.
De aanvullingen in NL-SBB ten opzichte van SKOS kunnen moeiteloos gebruikt worden in een SKOS-systeem.
Een voorbeeld hiervan binnen NL-SBB is het kunnen relateren van begrippen aan brondocumenten.
Dit kan al binnen SKOS; NL-SBB zorgt ervoor dat deze (veel voorkomende) uitbreindingen consistent toegepast worden.
