*waardelijst* is een wat misleidende term. Het is beter is onderscheid te maken tussen:

* Referentielijsten, die zelf uit twee soorten kunnen bestaan: 
	* Lijsten met referenties naar *dingen*.
    * Een voorbeeld hiervan is de lijst met Nederlandse gemeenten. Dit zijn instanties van de klasse gemeente. Gemeenten met hun bestuurlijke gebieden en andere relevante kenmerking worden in een of ander informatiesysteem bijgehouden. Vanuit zo'n registratie wordt een lijst gepubliceerd die buiten de context van dat systeem kan worden gebruikt. 
	* Lijsten met referenties naar begrippen (concepten).
    * Een voorbeeld hiervan is de lijst met zakelijke rechten in de Basisregistratie Kadaster. Dit deze bevat verwijzingen naar de betreffende concepten, die worden gedefieerd en uitgelegd in het begippenkader voor deze basisregistratie.
* 'zuivere' waardelijsten, dat wil zeggen Lijsten met termen en/of bijbehorende codes.  Volgens naamgeving NEN3610: 
	* Enumeraties: intern beheerd.
    * Enumeraties worden als onderdeel van het informatiemodel beheerd. Vaak wordt de keuze man/vrouw/x/onbekend als enumeratie opgenomen.
    * Enumeraties worden gebruikt voor coderingen die vrijwel nooit veranderen en daarmee geen eigen beheersysteem nodig hebben.
    * Enumeraties horen op de laag van de technische oplossing. Enumeraties vind je in databases en Front-end e.d.
    * Het kan zijn dat een partij een koppeling bijhoudt tussen een lijst van begrippen en een enumeratie in een (IT) oplossing, maar binnen NL-SBB doen we daarover geen uitspraak. In NL-SBB hebben we het dus niet over enumraties.
	* Codelijsten: extern beheerd.
    * Codelijsten zijn vergelijkbaar met enumeraties, maar worden als lijstje buiten het informatiemodel beheerd.
    * Daardoor hoeft bij een nieuwe, gewijzigde of vervallen code geen nieuwe versie van het informatiemodel te worden gemaakt.
    * Een voorbeeld is het AfsluitmiddelType in de aquo standaard, met als waarden 'niet afsluitbaar', 'tolklep', 'terugslagklep', 'schuif', 'zandzakken', 'schotbalk sponning', 'deur'.  Deze termen worden niet gedefinieerd, hoewel je dat hier wel zou kunnen doen ze ook kunnen worden opgevat als begrippen.
    * Een ander voorbeeld is de breedteklasse in de Basisregistratie Topografie (0,5 - 3 meter, 3 - 6 meter, 6 - 12 meter, 12 - 50 meter, 50 - 125 meter, > 125 meter). Dit is letterlijk een lijstje met waarden (van de breedteklasse).

Enumeraties en codelijsten vallen buiten het kader van NL-SBB. 
Referentielijsten met referenties naar 'dingen' kennen een informatiemodel conform MIM en vallen eveneens buiten het kader van NL-SBB.

Referentielijsten met referenties naar concepten kunnen worden bijgehouden als begrippenkader of als collectie, maar ook als gewoon een lijst van concepten. 
* EU referentielijsten worden meestal als 1 geheel gepubliceerd. In feite is iedere referentielijst dan een begrippenkader.
* Als zo'n lijst niet expliciet als begrippenkader wordt gedefinieerd is het gewoon een lijst met concepten.
* Een collectie kan worden gebruikt om begrippen in een lijst te ordenen.
  * Een voorbeeld is een lijst die je kunt maken van alle zakelijke rechten die in de BRK zijn gedefinieerd. Deze lijst kun je vervolgens publiceren als waardelijst. In dit voorbeeld is het een lijst van concepten die tot hetzelfde begrippenkader behoren.
  * Maar een collectie kan ook een lijst van begrippen uit verschillende begrippenkaders zijn. Een voorbeeld is de lijst met publiekrechtelijke beperkingen in het Digitaal Stelsel Omgevingswet. Deze beperkingen kunnen in allerlei contexten worden gedefinieerd, bijvoorbeeld rijksmonument (als begrip binnen de momunmentenwet), NSW landgoed (als begrip in de omgevingswet), etc.
 
We sluiten aan bij bestaande standaarden:
aarvoor kijken we met name naar:
  * https://standaarden.overheid.nl/tooi/doc/tooi-waardelijstontologie/#subklassen-van-tooiontwaardelijst voor Registerwaardelijsten vs Conceptwaardelijsten
  * https://interoperable-europe.ec.europa.eu/sites/default/files/custom-page/attachment/methodology_and_tools_for_metadata_governance_and_management_for_eu_institutions.pdf

In het kader van de NL-SBB is met name de TOOI standaard voor conceptwaardelijsten relevant. Deze beschrijft ook de metadata, die vergelijkbaar zijn met de metadata die in de werkgroep 'metadata' binnen NL-SBB worden beschreven en een waardelijst als 'semantic asset', inclusief een stukje provenance beschrijven.


