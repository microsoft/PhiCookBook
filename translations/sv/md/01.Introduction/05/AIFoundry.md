<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7b4235159486df4000e16b7b46ddfec3",
  "translation_date": "2025-05-09T14:58:37+00:00",
  "source_file": "md/01.Introduction/05/AIFoundry.md",
  "language_code": "sv"
}
-->
# **Använda Azure AI Foundry för utvärdering**

![aistudo](../../../../../translated_images/AIFoundry.61da8c74bccc0241ce9a4cb53a170912245871de9235043afcb796ccbc076fdc.sv.png)

Hur du utvärderar din generativa AI-applikation med [Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Oavsett om du bedömer enkla eller flerstegs-konversationer, erbjuder Azure AI Foundry verktyg för att utvärdera modellens prestanda och säkerhet.

![aistudo](../../../../../translated_images/AIPortfolio.5aaa2b25e9157624a4542fe041d66a96a1c1ec6007e4e5aadd926c6ec8ce18b3.sv.png)

## Hur man utvärderar generativa AI-appar med Azure AI Foundry
För mer detaljerade instruktioner, se [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Här är stegen för att komma igång:

## Utvärdera Generativa AI-Modeller i Azure AI Foundry

**Förutsättningar**

- En testdataset i CSV- eller JSON-format.
- En distribuerad generativ AI-modell (som Phi-3, GPT 3.5, GPT 4 eller Davinci-modeller).
- En runtime med en beräkningsinstans för att köra utvärderingen.

## Inbyggda utvärderingsmått

Azure AI Foundry låter dig utvärdera både enkla och komplexa flerstegs-konversationer.
För Retrieval Augmented Generation (RAG)-scenarier, där modellen är baserad på specifik data, kan du bedöma prestanda med hjälp av inbyggda utvärderingsmått.
Du kan även utvärdera generella enkla frågesvarsscenarier (icke-RAG).

## Skapa en utvärderingskörning

Från Azure AI Foundry-gränssnittet, gå till antingen sidan Evaluate eller Prompt Flow.
Följ guiden för att skapa en utvärderingskörning. Ange ett valfritt namn för din utvärdering.
Välj det scenario som bäst matchar din applikations mål.
Välj en eller flera utvärderingsmått för att bedöma modellens resultat.

## Anpassad utvärderingsflöde (valfritt)

För större flexibilitet kan du skapa ett anpassat utvärderingsflöde. Anpassa utvärderingsprocessen efter dina specifika behov.

## Visa resultat

Efter att ha kört utvärderingen kan du logga, visa och analysera detaljerade utvärderingsmått i Azure AI Foundry. Få insikter om din applikations kapacitet och begränsningar.

**Note** Azure AI Foundry är för närvarande i public preview, så använd det för experiment och utveckling. För produktionsarbetsbelastningar bör du överväga andra alternativ. Utforska den officiella [AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) för mer information och steg-för-steg-instruktioner.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För viktig information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår från användningen av denna översättning.