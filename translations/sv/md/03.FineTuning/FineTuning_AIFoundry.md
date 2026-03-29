# Finjustera Phi-3 med Microsoft Foundry

 Låt oss utforska hur man finjusterar Microsofts språkmodell Phi-3 Mini med Microsoft Foundry. Finjustering låter dig anpassa Phi-3 Mini till specifika uppgifter, vilket gör den ännu mer kraftfull och kontextmedveten.

## Överväganden

- **Kapaciteter:** Vilka modeller kan finjusteras? Vad kan basmodellen finjusteras för att göra?
- **Kostnad:** Hur ser prissättningsmodellen ut för finjustering?
- **Anpassningsbarhet:** Hur mycket kan jag modifiera basmodellen – och på vilka sätt?
- **Bekvämlighet:** Hur sker finjusteringen egentligen – måste jag skriva egen kod? Måste jag tillhandahålla egen beräkningskapacitet?
- **Säkerhet:** Finjusterade modeller är kända för att ha säkerhetsrisker – finns det några skyddsåtgärder på plats för att förhindra oavsiktlig skada?

![AIFoundry Models](../../../../translated_images/sv/AIFoundryModels.0e1b16f7d0b09b73.webp)

## Förberedelse för finjustering

### Förutsättningar

> [!NOTE]
> För Phi-3-familjens modeller är pay-as-you-go-modellen för finjustering endast tillgänglig med nav skapade i regionen **East US 2**.

- Ett Azure-abonnemang. Om du inte har ett Azure-abonnemang, skapa ett [betalt Azure-konto](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) för att börja.

- Ett [AI Foundry-projekt](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Azure rollbaserade åtkomstkontroller (Azure RBAC) används för att ge åtkomst till operationer i Microsoft Foundry. För att utföra stegen i denna artikel måste ditt användarkonto tilldelas __Azure AI Developer-rollen__ på resursgruppen.

### Registrering av prenumerationsleverantör

Verifiera att prenumerationen är registrerad hos resursleverantören `Microsoft.Network`.

1. Logga in på [Azure-portalen](https://portal.azure.com).
1. Välj **Prenumerationer** från vänstermenyn.
1. Välj den prenumeration du vill använda.
1. Välj **AI-projektinställningar** > **Resursleverantörer** från vänstermenyn.
1. Bekräfta att **Microsoft.Network** finns i listan över resursleverantörer. Annars lägg till den.

### Datapreparation

Förbered din tränings- och valideringsdata för att finjustera din modell. Dina tränings- och valideringsdataset består av in- och utgångsexempel på hur du vill att modellen ska prestera.

Se till att alla dina träningsdata följer formatet som förväntas vid inferens. För att finjustera modeller effektivt, säkerställ en balanserad och mångsidig datamängd.

Detta innebär att bibehålla databalans, inkludera olika scenarier och med jämna mellanrum förbättra träningsdata för att stämma överens med verkliga förväntningar, vilket slutligen leder till mer korrekta och balanserade modellrespons.

Olika modelltyper kräver olika format på träningsdata.

### Chat Completion

Den tränings- och valideringsdata du använder **måste** vara formaterad som ett JSON Lines (JSONL) dokument. För `Phi-3-mini-128k-instruct` måste finjusteringsdatasetet formateras i det konversationsformat som används av API:et för chattslutföranden.

### Exempel på filformat

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Det stödda filformatet är JSON Lines. Filer laddas upp till standarddatabasen och görs tillgängliga i ditt projekt.

## Finjustera Phi-3 med Microsoft Foundry

Microsoft Foundry låter dig anpassa stora språkmodeller till dina personliga datamängder genom en process som kallas finjustering. Finjustering ger stort värde genom att möjliggöra anpassning och optimering för specifika uppgifter och applikationer. Det leder till förbättrad prestanda, kostnadseffektivitet, minskad latens och skräddarsydda resultat.

![Finetune AI Foundry](../../../../translated_images/sv/AIFoundryfinetune.193aaddce48d553c.webp)

### Skapa ett nytt projekt

1. Logga in på [Microsoft Foundry](https://ai.azure.com).

1. Välj **+New project** för att skapa ett nytt projekt i Microsoft Foundry.

    ![FineTuneSelect](../../../../translated_images/sv/select-new-project.cd31c0404088d7a3.webp)

1. Utför följande uppgifter:

    - Projektets **Hub-namn**. Det måste vara ett unikt värde.
    - Välj den **Hub** som ska användas (skapa en ny vid behov).

    ![FineTuneSelect](../../../../translated_images/sv/create-project.ca3b71298b90e420.webp)

1. Utför följande uppgifter för att skapa en ny hub:

    - Ange **Hub-namn**. Det måste vara ett unikt värde.
    - Välj din Azure-**prenumeration**.
    - Välj den **resursgrupp** som ska användas (skapa en ny vid behov).
    - Välj den **plats** du vill använda.
    - Välj **Anslut Azure AI Services** som ska användas (skapa en ny vid behov).
    - Välj **Anslut Azure AI Search** till **Hoppa över anslutning**.

    ![FineTuneSelect](../../../../translated_images/sv/create-hub.49e53d235e80779e.webp)

1. Välj **Nästa**.
1. Välj **Skapa projekt**.

### Datapreparation

Innan finjustering, samla eller skapa en datamängd relevant för din uppgift, såsom chatinstruktioner, fråga-svar-par eller annan relevant textdata. Rensa och förbehandla denna data genom att ta bort brus, hantera saknade värden och tokenisera texten.

### Finjustera Phi-3-modeller i Microsoft Foundry

> [!NOTE]
> Finjustering av Phi-3-modeller stöds för närvarande endast i projekt som är belägna i East US 2.

1. Välj **Modellkatalog** från vänstra sidofältet.

1. Skriv *phi-3* i **sökrutan** och välj den Phi-3-modell du vill använda.

    ![FineTuneSelect](../../../../translated_images/sv/select-model.60ef2d4a6a3cec57.webp)

1. Välj **Fine-tune**.

    ![FineTuneSelect](../../../../translated_images/sv/select-finetune.a976213b543dd9d8.webp)

1. Ange **Namn på finjusterad modell**.

    ![FineTuneSelect](../../../../translated_images/sv/finetune1.c2b39463f0d34148.webp)

1. Välj **Nästa**.

1. Utför följande uppgifter:

    - Välj **uppgiftstyp** till **Chat completion**.
    - Välj den **träningsdata** du vill använda. Du kan ladda upp den genom Microsoft Foundrys datahantering eller från din lokala miljö.

    ![FineTuneSelect](../../../../translated_images/sv/finetune2.43cb099b1a94442d.webp)

1. Välj **Nästa**.

1. Ladda upp den **valideringsdata** du vill använda, eller välj **Automatisk uppdelning av träningsdata**.

    ![FineTuneSelect](../../../../translated_images/sv/finetune3.fd96121b67dcdd92.webp)

1. Välj **Nästa**.

1. Utför följande uppgifter:

    - Välj den **multiplikator för batch-storlek** du vill använda.
    - Välj den **inlärningshastighet** du vill använda.
    - Välj antal **epoker** du vill använda.

    ![FineTuneSelect](../../../../translated_images/sv/finetune4.e18b80ffccb5834a.webp)

1. Välj **Skicka** för att starta finjusteringsprocessen.

    ![FineTuneSelect](../../../../translated_images/sv/select-submit.0a3802d581bac271.webp)

1. När din modell är finjusterad kommer status att visas som **Komplett**, som i bilden nedan. Nu kan du distribuera modellen och använda den i din egen applikation, i playground eller i prompt flow. För mer information, se [Hur man distribuerar Phi-3-familjen av små språkmodeller med Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/sv/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> För mer detaljerad information om finjustering av Phi-3, besök [Finjustera Phi-3-modeller i Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Rensa upp dina finjusterade modeller

Du kan ta bort en finjusterad modell från listan för finjusteringsmodeller i [Microsoft Foundry](https://ai.azure.com) eller från modellens detaljsida. Välj den finjusterade modell du vill ta bort från finjusteringssidan och klicka sedan på knappen Ta bort för att radera modellen.

> [!NOTE]
> Du kan inte ta bort en anpassad modell om den har en befintlig distribution. Du måste först ta bort modellens distribution innan du kan ta bort den anpassade modellen.

## Kostnader och kvoter

### Kostnads- och kvotöverväganden för Phi-3-modeller finjusterade som en tjänst

Phi-modeller finjusterade som en tjänst erbjuds av Microsoft och är integrerade med Microsoft Foundry för användning. Du kan hitta prissättning när du [distribuerar](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) eller finjusterar modellerna under fliken Priser och villkor i distributionsguiden.

## Innehållsfiltrering

Modeller som distribueras som en tjänst med pay-as-you-go skyddas av Azure AI Content Safety. När de distribueras till realtidsendpunkter kan du välja att avstå från denna funktion. Med Azure AI Content Safety aktiverat passerar både prompt och slutförande genom en ensemble av klassificeringsmodeller som syftar till att upptäcka och förhindra utskick av skadligt innehåll. Innehållsfiltreringssystemet upptäcker och agerar på specifika kategorier av potentiellt skadligt innehåll i både ingångsprompter och utdata. Läs mer om [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Finjusteringskonfiguration**

Hyperparametrar: Definiera hyperparametrar såsom inlärningshastighet, batchstorlek och antal tränings-epoker.

**Förlustfunktion**

Välj en lämplig förlustfunktion för din uppgift (t.ex. korsentropi).

**Optimerare**

Välj en optimerare (t.ex. Adam) för gradientuppdateringar under träning.

**Finjusteringsprocess**

- Ladda förtränad modell: Ladda Phi-3 Mini checkpoints.
- Lägg till anpassade lager: Lägg till uppgiftsspecifika lager (t.ex. klassificeringshuvud för chatinstruktioner).

**Träna modellen**

Finjustera modellen med din förberedda datamängd. Övervaka träningsförlopp och justera hyperparametrar vid behov.

**Utvärdering och validering**

Valideringsset: Dela upp din data i tränings- och valideringsset.

**Utvärdera prestanda**

Använd mätvärden som noggrannhet, F1-poäng eller perplexitet för att bedöma modellens prestanda.

## Spara finjusterad modell

**Checkpunkt**

Spara checkpoint för finjusterad modell för framtida användning.

## Distribution

- Distribuera som en webbservice: Distribuera din finjusterade modell som en webbservice i Microsoft Foundry.
- Testa endpunkten: Skicka testfrågor till den distribuerade endpunkten för att verifiera dess funktionalitet.

## Iterera och förbättra

Iterera: Om prestandan inte är tillfredsställande, iterera genom att justera hyperparametrar, lägga till mer data eller finjustera fler epoker.

## Övervaka och förfina

Övervaka kontinuerligt modellens beteende och förfina vid behov.

## Anpassa och utöka

Anpassade uppgifter: Phi-3 Mini kan finjusteras för olika uppgifter utöver chatinstruktioner. Utforska andra användningsområden!
Experimentera: Prova olika arkitekturer, lagerkombinationer och tekniker för att förbättra prestandan.

> [!NOTE]
> Finjustering är en iterativ process. Experimentera, lär dig och anpassa din modell för att nå bästa resultat för din specifika uppgift!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess modersmål ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår genom användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->