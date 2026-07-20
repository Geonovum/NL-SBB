
# Conformiteit

Naast onderdelen die als niet-normatief gemarkeerd zijn, zijn ook alle diagrammen, voorbeelden, en noten in dit document niet-normatief. Verder is alles in dit document normatief.


## SHACL-validatiemeldingen

Voor het valideren van begrippenkaders conform de NL-SBB-standaard wordt gebruikgemaakt van SHACL-validatieregels. Bij een validatie kunnen drie typen meldingen voorkomen: `sh:Violation`, `sh:Warning` en `sh:Info`  .

- **`sh:Violation`** – Geeft aan dat een verplichte validatieregel uit de NL-SBB-standaard is overtreden. Een begrippenkader met één of meer `sh:Violation`-meldingen is niet conform de standaard.
- **`sh:Warning`** – Geeft aan dat niet wordt voldaan aan een aanbevolen kwaliteitsregel of best practice. `sh:Warning`-meldingen hebben geen gevolgen voor de conformiteit met de standaard, maar het wordt aanbevolen deze te beoordelen en waar mogelijk op te lossen.
- **`sh:Info`** – Geeft aanvullende informatie of suggesties ter verbetering van de kwaliteit, consistentie of herbruikbaarheid van het begrippenkader. `sh:Info`-meldingen hebben geen gevolgen voor de conformiteit met de standaard.
