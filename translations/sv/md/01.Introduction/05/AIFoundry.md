# **Använda Microsoft Foundry för utvärdering**

![aistudo](../../../../../translated_images/sv/AIFoundry.9e0b513e999a1c5a.webp)

Hur du utvärderar din generativa AI-applikation med [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Oavsett om du bedömer enkla eller flerstegssamtal, erbjuder Microsoft Foundry verktyg för att utvärdera modellens prestanda och säkerhet.

![aistudo](../../../../../translated_images/sv/AIPortfolio.69da59a8e1eaa70f.webp)

## Hur man utvärderar generativa AI-appar med Microsoft Foundry  
För mer detaljerade instruktioner se [Microsoft Foundry-dokumentationen](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Här är stegen för att komma igång:

## Utvärdera generativa AI-modeller i Microsoft Foundry

**Förutsättningar**

- En testdataset i antingen CSV- eller JSON-format.
- En distribuerad generativ AI-modell (såsom Phi-3, GPT 3.5, GPT 4, eller Davinci-modeller).
- En runtime med en compute-instans för att köra utvärderingen.

## Inbyggda utvärderingsmått

Microsoft Foundry låter dig utvärdera både enkla och komplexa flerstegssamtal.  
För Retrieval Augmented Generation (RAG)-scenarier, där modellen är baserad på specifik data, kan du bedöma prestanda med hjälp av inbyggda utvärderingsmått.  
Dessutom kan du utvärdera generella enkla fråge-svarsscenarier (icke-RAG).

## Skapa en utvärderingskörning

Från Microsoft Foundry UI, navigera till sidan Evaluate eller sidan Prompt Flow.  
Följ guiden för att skapa en utvärderingskörning. Ange ett valfritt namn för din utvärdering.  
Välj det scenario som stämmer överens med ditt applikationsmål.  
Välj ett eller flera utvärderingsmått för att bedöma modellens resultat.

## Anpassad utvärderingsflöde (Valfritt)

För större flexibilitet kan du skapa ett anpassat utvärderingsflöde. Anpassa utvärderingsprocessen baserat på dina specifika krav.

## Visa resultat

Efter att ha kört utvärderingen, logga, visa och analysera detaljerade utvärderingsmått i Microsoft Foundry. Få insikter om din applikations förmågor och begränsningar.

**Note** Microsoft Foundry är för närvarande i offentlig förhandsgranskning, så använd den för experiment och utvecklingsändamål. För produktionsarbetsbelastningar bör du överväga andra alternativ. Utforska den officiella [AI Foundry-dokumentationen](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) för mer information och steg-för-steg-instruktioner.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->