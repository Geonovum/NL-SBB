# Notulen

> Gegenereerd door AI – beperkt gecontroleerd door Frank op nauwkeurigheid.

## Generieke Verwijzingen naar Kennisbronnen

Annemieke, Frank, Hans, Theun en anderen bespraken de behoefte aan een generieke manier om te verwijzen naar kennisbronnen. Hierbij gaat het niet alleen om wetten.nl, maar ook om andere bronnen zoals handleidingen, XSD-beschrijvingen en niet-online documenten, met aandacht voor digitale beschikbaarheid, context en betekenis.

### Belangrijkste punten

- **Breedte van kennisbronnen**
  - Verwijzingen zijn niet beperkt tot wetten.nl
  - Ook handleidingen, XSD-beschrijvingen en andere digitale bronnen vallen hieronder
  - Voorwaarde: bron moet ergens digitaal beschikbaar zijn (niet alleen impliciet aanwezig)

- **Context en betekenis van verwijzingen**
  - Niet alleen verwijzen naar een document
  - Ook expliciet maken wat context en betekenis van de verwijzing is
  - Doel: eenduidige interpretatie

- **Beperkingen van huidige standaard**
  - Richt zich primair op directe verwijzingen naar wetsartikelen
  - Uitbreiding nodig voor complexere en bredere verwijzingen
  - Meer metadata gewenst
  - Ondersteuning van verschillende typen bronnen nodig

- **Digitale beschikbaarheid en afbakening**
  - Kennisbron moet digitaal herleidbaar zijn
  - Heldere definitie nodig van wat als kennisbron geldt

---

## Uitwerking en Aanscherping van de Standaard

Hans, Frank, Annemieke, Theun en Marco bespraken mogelijke aanscherpingen van de standaard.

### Voorstellen en inzichten

- **Best practices documentatie**
  - Behoefte aan praktisch toepasbare richtlijnen
  - Document is in ontwikkeling

- **Toelichting en rationale**
  - Toelichtingen moeten explicieter worden
  - Vooral het doel en de betekenis van eigenschappen zoals `heeft bron`
  - Verschil tussen definitie en interpretatie verduidelijken

- **Gebruik van subproperties**
  - Mogelijkheid om subproperties te definiëren, zoals:
    - `verwijzing voluit`
    - `verwijzing kort`
  - Voordeel: uitbreiding zonder wijziging van de hoofdstandaard

- **Type-aanduidingen voor verwijzingen**
  - Als beste oplossing gezien
  - Bronverwijzingen krijgen een type
  - Voorbeelden:
    - wetten.nl
    - Europese regelgeving
    - overige bronnen

---

## Technische Implementatie en Modellering

Besproken door Hans, Theun, Annemieke en Frank.

### Technische aandachtspunten

- **Object property vs. data type property**
  - `heeft bron` wordt nu dubbel gebruikt:
    - als string/URL (data type)
    - als object property
  - Dit leidt tot verwarring en beperkte machineleesbaarheid

- **Gebruik van RDF comment**
  - Toelichting wordt opgeslagen als string
  - Generiek toepasbaar op alle elementen
  - Niet specifiek per relatie

- **Dublin Core termen**
  - Gebruik van `dc:source` in NL-SBB
  - Flexibel qua domein en range
  - Zowel kracht als zwakte

- **Naamgeving en breaking changes**
  - Wijzigen van propertynamen (bv. `brondocument` → `bronverwijzing`)
  - Wordt gezien als breaking change
  - Alleen mogelijk bij major versie-update

---

## Voorbeelden en Best Practices Uitwerken

Afspraken tussen Frank, Hans, Theun, Annemieke, Lotte en Tanja.

### Afspraken

- **Uitwerken van voorbeelden**
  - Issue aanmaken voor rationale van naamgeving
  - Concrete voorbeelden uitwerken

- **Delen en verbeteren**
  - Voorbeelden worden gedeeld binnen de groep
  - Eventueel aangepast op basis van feedback
  - Delen via e-mail vooraf aan volgende meeting

- **Variatie in voorbeelden**
  - Verwijzingen naar:
    - wetten.nl
    - Europese regelgeving
    - modelverordeningen
    - documentatie
    - niet-wettelijke bronnen

- **Planning vervolg**
  - Vervolgafspraak:
    - **Datum:** donderdag 23 juli  
    - **Tijd:** 15:00 – 16:00

---

## Toepassing en Uitbreiding van Verwijzingsmethodiek

Besproken door Annemieke, Hans, Frank en Theun.

### Belangrijk inzicht

- **Uniforme verwijzingsmethodiek**
  - Toepasbaar op meerdere elementen:
    - concepten
    - objecten
    - regels
  - Doel:
    - consistentie
    - hergebruik
    - generieke modellering

---

## Op te volgen taken

### 1. Rationale brondocument vs. bronverwijzing
- Maak een issue aan voor de onderbouwing van de gekozen naamgeving  
- **Verantwoordelijke:** Frank

### 2. Best practices documentatie verwijzingen
- Stuur besproken plaatjes en presentaties naar Frank  
- Doel: opnemen in verslag en documentatie  
- **Verantwoordelijke:** Hans Annemieke

### 3. Voorbeelden kennisbronverwijzingen
- Werk voorbeelden uit (verschillende bronsoorten)
- Deel deze ter voorbereiding op volgende meeting  
- **Verantwoordelijken:** Theun, Annemieke

### 4. Toepasbaarheid verwijzingsmethodiek buiten NL-SBB toetsen
- Afspraak binnen Geonovum met Tanja, Linda, Joost en Frank
- Kan deze methodiek ook worden toegepast in MIM, JSON-schema of andere plekken?
- Deel inzichten ter voorbereiding op volgende meeting  
- **Verantwoordelijken:** Frank

### 5. Vergaderplanning volgende sessie
- Plan meeting op:
  - donderdag 23 juli
  - 15:00 – 16:00  
- **Verantwoordelijke:** Frank
