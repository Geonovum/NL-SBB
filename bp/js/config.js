let respecConfig = {
    useLogo: true,
    useLabel: true,
    // title is verplicht! Neem hier de titel van het document op ----------------------
    title: "Best Practices en aanvullingen voor NL-SBB - Standaard voor het beschrijven van begrippen",
    //-- specStatus is verplicht! (activeer 1 van de volgende) --------------------------
    specStatus: "wv",                   // Werkversie
    //specStatus: "cv",               // Consultatieversie
    //specStatus: "vv",               // Versie ter vaststelling
    //specStatus: "def",              // Vastgestelde versie
    //specStatus: "basis",            // Basis Document
    //-- specType is verplicht bij alle andere dan BASIS ---------------------------------
    //specType: "NO",                 // Norm
    //specType: "ST",                 // Standaard
    //specType: "IM",                 // Informatie Model
    //specType: "PR",                 // Praktijkrichtlijn
    specType: "HR",                     // HandReiking
    //specType: "WA",                 // Werkafspraak
    //specType: "BD",                 // Beheer Documentatie
    //specType: "AL",                 // Algemeen document
    //specType: "BP",                 // Best Practice
    //-- pubDomain is verplicht! (komt in de URL) -------------------------------------
    //-- zie: https://geonovum.github.io/handleiding-tooling/ReSpec/#pubdomain
    pubDomain: "NL-SBB",
    //-- license: voor de geldende gebruiksvoorwaarden. Default is cc-by.
    //license: "cc-by-nd",            // bronvermelding, geen afgeleide werken (default)
    //license: "cc0",                 // Public Domain Dedication
    license: "cc-by",                 // Attribution, met bronvermelding
    //-- TODO shortName is verplicht! (komt in de URL: kies logische afkorting)--------------
    shortName: "bp",
    
    //edDraftURI = De URI van de draft version. Deze wordt automatisch afgeleid van de github URI; maar kan hier overschreven worden. 
    edDraftURI: ["https://geonovum.github.io", "/", "pubDomain", "/", "bp"],
  
    //-- publishDate is verplicht -------------------------------------------------------
    //-- NB: in de werkversie uitzetten, want dan pakt Respec de pushdate ---------------
    //publishDate: "2023-03-28",
    //eventueel is het mogelijk een versienummer mee te geven, maar bij Geonovum werken we gewoonlijk alleen met datum als onderdeel van de permanente URI.
    //publishVersion: "0.0.2",
    //previousVersion: "0.0.1",
    //-- Voor dit blok geldt: alleen als er eerdere versies zijn en altijd beiden aan/uit! 
    //previousPublishDate: "2014-05-01",
    //previousMaturity: "CV",
    //-- TODO: de namen van de Editor(s) / Redacteur(en)---------------------------------------
    //-- vul in: per Editor: name:, company:, companyURL: -------------------------------
    authors: [
        {
            name: "Jos van der Arend (Kennisnet)"
        },
        {
            name: "Jesse Bakker (Kadaster)"
        },
        {
            name: "Koos Boersma (IHW)"
        },
        {
            name: "Marco Brattinga (Nationale Politie)"
        },
        {
            name: "Linda van den Brink (Geonovum)"
        },
        {
            name: "Pieter van Everdingen (PLDN)"
        },
        {
            name: "Roeland Euwens (KNB)"
        },
        {
            name: "Casper le Gras (KOOP)"
        },
        {
            name: "Gerald Groot Roessink (DUO)"
        },
        {
            name: "Pano Maria (Skemu)"
        },
        {
            name: "Rik (CROW)"
        },
        {
            name: "Hans Overbeek (KOOP)"
        },
        {
            name: "Viyanti Ramdhiansing (Kennisnet)"
        },
        {
            name: "Arjen Santema (Kadaster)"
        },
        {
            name: "Frank Terpstra (Geonovum)"
        },
        {
            name: "Kees Trautwein (Logius)"
        },
        {
            name: "Jan Willem van Veen (ArchiXL)"
        }
  ],
  editors: [
        {
            name: "Jesse Bakker"
        },
        {
            name: "Arjen Santema"
        },
        {
            name: "Kees Trautwein"
        }
  ],
  
    // TODO: Vul de github URL in.
    //neem hier de URL van de github repository op waar het respec document in staat
    github: "https://github.com/Geonovum/NL-SBB/bp",
    // Create PDF and link to file in header (optional):
    // TODO: Change the filename as preferred.
   // alternateFormats: [
   //     {
   //         label: "pdf",
   //         uri: "template.pdf",
   //     },
   // ],
   
  localBiblio: {
    WETTENNL: {
        title: "Wetten.nl",
        href: "https://linkeddata.overheid.nl/terms/",
        publisher: "KOOP",
    },
    SKOSLEX: {
        title: "Skos-lex",
        href: "http://bp4mc2.org/def/skos-lex",
        publisher: "bp4mc2",
    },
    NLSBB: {
        title: "NL-SBB - Standaard voor het beschrijven van begrippen",
        href: "https://docs.geostandaarden.nl/nl-sbb/nl-sbb/",
        publisher: "Geonovum",
        authors: ["Jesse Bakker", "Arjen Santema", "Kees Trautwein"
        ]
    }
  }
};