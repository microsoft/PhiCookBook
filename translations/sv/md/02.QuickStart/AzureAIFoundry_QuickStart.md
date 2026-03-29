# **Använda Phi-3 i Microsoft Foundry**

Med utvecklingen av Generativ AI hoppas vi använda en enhetlig plattform för att hantera olika LLM och SLM, företagsdataintegration, finjustering/RAG-operationer och utvärdering av olika företagsverksamheter efter integrering av LLM och SLM, etc., så att generativ AI kan implementeras bättre i smarta applikationer. [Microsoft Foundry](https://ai.azure.com) är en företagsnivåplattform för generativa AI-applikationer.

![aistudo](../../../../translated_images/sv/aifoundry_home.f28a8127c96c7d93.webp)

Med Microsoft Foundry kan du utvärdera stora språkmodellsvar (LLM) och orkestrera promptapplikationskomponenter med promptflöde för bättre prestanda. Plattformen underlättar skalbarhet för att förvandla proof of concepts till fullfjädrad produktion med lätthet. Kontinuerlig övervakning och förfining stödjer långsiktig framgång.

Vi kan snabbt distribuera Phi-3-modellen på Microsoft Foundry genom enkla steg, och sedan använda Microsoft Foundry för att slutföra Phi-3 relaterade Playground/Chat, finjustering, utvärdering och annat relaterat arbete.

## **1. Förberedelse**

Om du redan har [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) installerad på din dator är det lika enkelt som att köra detta kommando i en ny katalog för att använda denna mall.

## Manuell skapning

Att skapa ett Microsoft Foundry-projekt och hub är ett utmärkt sätt att organisera och hantera ditt AI-arbete. Här är en steg-för-steg-guide för att komma igång:

### Skapa ett projekt i Microsoft Foundry

1. **Gå till Microsoft Foundry**: Logga in på Microsoft Foundry-portalen.
2. **Skapa ett projekt**:
   - Om du är i ett projekt, välj "Microsoft Foundry" längst upp till vänster på sidan för att gå till startsidan.
   - Välj "+ Skapa projekt".
   - Ange ett namn för projektet.
   - Om du har en hubb kommer den att väljas som standard. Om du har tillgång till mer än en hubb kan du välja en annan från rullgardinsmenyn. Om du vill skapa en ny hubb, välj "Skapa ny hubb" och ange ett namn.
   - Välj "Skapa".

### Skapa en hubb i Microsoft Foundry

1. **Gå till Microsoft Foundry**: Logga in med ditt Azure-konto.
2. **Skapa en hubb**:
   - Välj Management center från vänstermenyn.
   - Välj "Alla resurser", sedan nedåtpilen bredvid "+ Nytt projekt" och välj "+ Ny hubb".
   - I dialogrutan "Skapa en ny hubb" anger du ett namn för din hubb (t.ex. contoso-hub) och justerar övriga fält efter önskemål.
   - Välj "Nästa", granska informationen och välj sedan "Skapa".

För mer detaljerade instruktioner kan du hänvisa till den officiella [Microsoft-dokumentationen](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Efter framgångsrik skapning kan du komma åt studion du skapat via [ai.azure.com](https://ai.azure.com/)

Det kan finnas flera projekt på en AI Foundry. Skapa ett projekt i AI Foundry för att förbereda.

Skapa Microsoft Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. Distribuera en Phi-modell i Microsoft Foundry**

Klicka på Utforska-alternativet för projektet för att gå in i Modellkatalogen och välj Phi-3

Välj Phi-3-mini-4k-instruct

Klicka på 'Distribuera' för att distribuera Phi-3-mini-4k-instruct modellen

> [!NOTE]
>
> Du kan välja beräkningskraft vid distribution

## **3. Playground Chat Phi i Microsoft Foundry**

Gå till distributionssidan, välj Playground, och chatta med Phi-3 i Microsoft Foundry

## **4. Distribuera modellen från Microsoft Foundry**

För att distribuera en modell från Azure Model Catalog kan du följa dessa steg:

- Logga in på Microsoft Foundry.
- Välj den modell du vill distribuera från Microsoft Foundrys modellkatalog.
- På modellens detaljsida, välj Distribuera och sedan Serverless API med Azure AI Content Safety.
- Välj det projekt där du vill distribuera dina modeller. För att använda Serverless API-erbjudandet måste din arbetsyta tillhöra regionen East US 2 eller Sweden Central. Du kan anpassa namn på distributionen.
- På distributionsguiden, välj Pris och villkor för att lära dig om pris och användningsvillkor.
- Välj Distribuera. Vänta tills distributionen är klar och du omdirigeras till sidan för Distributioner.
- Välj Öppna i playground för att börja interagera med modellen.
- Du kan återvända till sidan Distributioner, välja distributionen, och notera slutpunktens Mål-URL och Hemliga nyckel, som du kan använda för att anropa distributionen och generera svar.
- Du kan alltid hitta slutpunktens detaljer, URL och åtkomstnycklar genom att gå till fliken Bygg och välja Distributioner från komponentavsnittet.

> [!NOTE]
> Observera att ditt konto måste ha rollen Azure AI Developer med behörigheter för Resursgruppen för att utföra dessa steg.

## **5. Använda Phi API i Microsoft Foundry**

Du kan komma åt https://{Ditt projektnamn}.region.inference.ml.azure.com/swagger.json via Postman GET och kombinera det med nyckel för att lära dig om de tillhandahållna gränssnitten

Du kan mycket enkelt få reda på begäransparametrar liksom svarsparametrar.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->