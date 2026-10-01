# Verslag NL-SBB werkgroep redactionele status

> N.B. Dit verslag is gegenereerd met behulp van AI en beperkt verbeterd en gecontroleerd op juistheid door Frank.

## Meta-informatie en profielen voor begrippenkaders

Frank, Pano, Niels, Brian en Hans bespraken uitgebreid de noodzaak, uitwerking en het beheer van metadata en profielen voor begrippenkaders. Pano lichtte toe dat het voorgestelde profiel compatibel is met DCAT-AP-NL 3.0, terwijl Niels uitleg gaf over huidige en experimentele methoden om profielen en hun gelaagdheid te beheren binnen OGC en NL-SBB.

### Profiel op basis van DCAT-AP-NL

Pano bevestigde dat het voorgestelde profiel voor begrippenkaders volledig aansluit op DCAT-AP-NL 3.0, waarbij aangescherpte eisen en kardinaliteiten expliciet zijn vastgelegd. Het profiel is bedoeld om metadata over begrippenkaders op een uniforme wijze te beschrijven en te publiceren.

### Gelaagdheid en beheer van profielen

Niels gaf aan dat er momenteel geen algemeen geaccepteerd mechanisme bestaat om profielhiërarchieën en afhankelijkheden formeel te beheren. Wel bestaan hiervoor initiatieven, zoals het OGC Building Blocks Framework. Besproken werd of aanvullende profielen beheerd moeten worden binnen NL-SBB of binnen het DCAT-AP-NL-ecosysteem. De conclusie was dat dit afhankelijk kan zijn van de beheerorganisatie en het toepassingsdomein.

### Governance en afhankelijkheden

De werkgroep besprak governance-vraagstukken rond profielbeheer, zoals het behouden van overzicht wanneer meerdere profielen voortbouwen op een gezamenlijk basisprofiel en het synchroniseren van versies tussen NL-SBB en DCAT-AP-NL. Niels gaf aan dat een aanpak op basis van building blocks kan helpen om dergelijke afhankelijkheden beter beheersbaar en inzichtelijk te maken.

### Praktische uitwerking en best practices

Brian en Frank benadrukten het belang van duidelijke best practices en invulrichtlijnen, zodat gebruikers weten welke metadata-elementen wanneer en hoe moeten worden ingevuld. Afgesproken werd om een volledig ingevuld voorbeeld uit te werken en aanvullende richtlijnen op te stellen, zodat het profiel praktisch toepasbaar wordt.

---

## Status en lifecycle van begrippenkaders

Hans, Frank, Brian, Pano en Niels bespraken de invulling van het veld *status* voor begrippenkaders, de relatie met bestaande statusvelden binnen DCAT-AP-NL en de behoefte aan een waardenlijst en duidelijke gebruiksrichtlijnen.

### Statusveld en waardenlijsten

Hans vroeg naar de invulling van het statusveld en de compatibiliteit met bestaande statusaanduidingen uit de DCAT-AP-familie. De groep concludeerde dat er momenteel geen breed geaccepteerde waardenlijst bestaat voor de status van begrippenkaders als linked-data-publicatie. Het statusveld heeft primair betrekking op het begrippenkader als geheel en niet op individuele begrippen.

### Begrippenkader versus publicatieset

Niels en Brian lichtten toe dat onderscheid gemaakt moet worden tussen de status van een begrippenkader en de status van een publicatieset of specifieke publicatieversie. Een publicatieset vertegenwoordigt een vastgelegde versie en heeft daardoor een statisch karakter, terwijl een begrippenkader als standaard of kennisbron een eigen levenscyclus kent.

### Organisatiespecifieke invulling

Pano en Hans merkten op dat de interpretatie en toepassing van statussen vaak organisatiespecifiek zijn. Hierdoor kan een verplichte statuslijst binnen de standaard te beperkend zijn. Als mogelijke oplossing werd besproken om het statusveld optioneel te houden en best practices op te stellen voor veelgebruikte waarden.

### Aansluiting op standaardisatieprocessen

Brian en Hans constateerden dat lifecycle-informatie aansluit bij gebruikelijke standaardisatieprocessen, waarbij bijvoorbeeld statussen als *aangemeld*, *in behandeling*, *vastgesteld* en *verouderd* worden onderscheiden. Belangrijk hierbij is dat de lifecycle van een begrippenkader los staat van de status van individuele begrippen.

---

## Uitwerking van voorbeelden en handreiking

Frank, Niels en Brian spraken af een volledig ingevuld voorbeeld van een begrippenkader uit te werken op basis van het profiel en de voorgestelde best practices. Brian zal dit voorbeeld toetsen op toepasbaarheid binnen het ROSA-begrippenkader.

### Voorbeeld uitwerken

Frank en Niels werken gezamenlijk een voorbeeld uit op basis van een recent begrippenkader. Hierbij worden de DCAT-AP-NL best practices en het conceptprofiel als uitgangspunt gebruikt. Het voorbeeld moet dienen als praktische handreiking voor zowel de werkgroep als toekomstige implementaties.

### Validatie door Brian

Brian beoordeelt het uitgewerkte voorbeeld op begrijpelijkheid, volledigheid en toepasbaarheid binnen het ROSA-begrippenkader. Eventuele vragen en bevindingen worden teruggekoppeld aan Frank en Niels.

### Handreiking en best practices

Mogelijk willen we na uitwerking van het voorbeeld een handreiking maken.
De handreiking zal bestaan uit een concreet ingevuld voorbeeld en een verzameling best practices. Daarbij wordt onder meer uitgelegd:

- welke velden verplicht zijn;
- welke velden optioneel zijn;
- hoe velden worden ingevuld;
- welke vuistregels gelden voor de toepassing van het profiel.

### Terugkoppeling aan de werkgroep

Na validatie worden de resultaten teruggekoppeld aan de bredere werkgroep. Daarbij wordt besproken of aanvullende specificatie noodzakelijk is of dat het profiel als optionele uitbreiding bij NL-SBB kan worden opgenomen.

---

## Planning en vervolgacties

Frank, Hans, Brian, Pano en Niels maakten afspraken over de planning van de volgende bijeenkomst, de uitwerking van voorbeelden en het verzamelen van feedback binnen de eigen organisaties.

### Volgende bijeenkomst

De volgende werkgroepbijeenkomst staat gepland voor **31 augustus**. Tijdens deze sessie zal ook het onderwerp worden besproken dat tijdens de huidige bijeenkomst niet aan bod is gekomen.

### Feedback verzamelen

Brian zal binnen zijn organisatie feedback ophalen over het gebruik van metadata voor begrippenkaders en de resultaten delen met de werkgroep.

### Parallelle uitwerking

Afgesproken is dat Frank en Niels het voorbeeldprofiel verder uitwerken, terwijl Brian op basis van dit voorbeeld als het er tijdig is een toepassing op het ROSA-begrippenkader voorbereidt. Beide voorbeelden worden tijdens de volgende bijeenkomst besproken.

---

# Actiepunten

## Voorbeeld begrippenkader uitwerken
Werk een volledig ingevuld voorbeeld van een begrippenkader uit op basis van de DKTPNL-best practices en het besproken profiel.

**Eigenaren:** Frank, Niels

## Voorbeeld valideren
Valideer het uitgewerkte voorbeeld en werk waar mogelijk een vergelijkbaar voorbeeld uit voor het ROSA-begrippenkader. Koppel vragen en bevindingen terug.

**Eigenaar:** Brian

## Best practices opstellen
Formuleer best practices en invulrichtlijnen voor de verschillende metadata-elementen in het profiel, inclusief toelichting op verplichte en optionele velden. N.B. dit wordt pas opgepakt na terugkoppeling aan de NL-SBB werkgroep indien deze daar noodzaak voor ziet.

**Eigenaren:** Frank, Niels

## Terugkoppeling voorbereiden
Bereid een terugkoppeling voor aan de brede werkgroep over de uitgewerkte voorbeelden, de best practices en de mogelijke positionering als optionele uitbreiding binnen NL-SBB.

**Eigenaar:** Frank

## Volgende subwerkgroep plannen
Plan een volgende bijeenkomst van de subwerkgroep eind augustus.

**Eigenaar:** Frank

## Organisatiebrede feedback verzamelen
Verzamel feedback binnen de eigen organisatie over metadata voor begrippenkaders en deel relevante inzichten met de werkgroep.

**Eigenaar:** Brian