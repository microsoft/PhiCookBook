<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c1559c5af6caccf6f623fd43a6b3a9a3",
  "translation_date": "2025-07-17T06:06:54+00:00",
  "source_file": "md/03.FineTuning/FineTuning_AIFoundry.md",
  "language_code": "da"
}
-->
# Finjustering af Phi-3 med Azure AI Foundry

Lad os udforske, hvordan man finjusterer Microsofts sprogmodel Phi-3 Mini ved hjælp af Azure AI Foundry. Finjustering gør det muligt at tilpasse Phi-3 Mini til specifikke opgaver, hvilket gør den endnu mere kraftfuld og kontekstbevidst.

## Overvejelser

- **Funktioner:** Hvilke modeller kan finjusteres? Hvad kan basismodellen finjusteres til at gøre?
- **Omkostninger:** Hvad er prismodellen for finjustering?
- **Tilpasning:** Hvor meget kan jeg ændre i basismodellen – og på hvilke måder?
- **Bekvemmelighed:** Hvordan foregår finjusteringen egentlig – skal jeg skrive brugerdefineret kode? Skal jeg medbringe egen regnekraft?
- **Sikkerhed:** Finjusterede modeller kan have sikkerhedsrisici – findes der nogen sikkerhedsforanstaltninger for at beskytte mod utilsigtet skade?

![AIFoundry Models](../../../../translated_images/AIFoundryModels.0e1b16f7d0b09b73e15278aa4351740ed2076b3bdde88c48e6839f8f8cf640c7.da.png)

## Forberedelse til finjustering

### Forudsætninger

> [!NOTE]
> For Phi-3 familie modeller er pay-as-you-go finjustering kun tilgængelig for hubs oprettet i **East US 2** regionerne.

- Et Azure-abonnement. Hvis du ikke har et Azure-abonnement, opret en [betalt Azure-konto](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) for at komme i gang.

- Et [AI Foundry-projekt](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Azure rollebaseret adgangskontrol (Azure RBAC) bruges til at give adgang til operationer i Azure AI Foundry. For at udføre trinene i denne artikel skal din brugerrolle have __Azure AI Developer-rollen__ på ressourcegruppen.

### Registrering af abonnementets udbyder

Bekræft, at abonnementet er registreret til `Microsoft.Network` resource provider.

1. Log ind på [Azure-portalen](https://portal.azure.com).
1. Vælg **Subscriptions** i venstremenuen.
1. Vælg det abonnement, du vil bruge.
1. Vælg **AI project settings** > **Resource providers** i venstremenuen.
1. Bekræft, at **Microsoft.Network** er på listen over resource providers. Hvis ikke, tilføj det.

### Dataforberedelse

Forbered dine trænings- og valideringsdata til at finjustere din model. Dine trænings- og valideringsdatasæt består af input- og outputeksempler, der viser, hvordan du ønsker, modellen skal præstere.

Sørg for, at alle dine træningseksempler følger det forventede format for inferens. For effektiv finjustering skal datasættet være balanceret og varieret.

Det indebærer at opretholde databalancen, inkludere forskellige scenarier og løbende forbedre træningsdata for at matche virkelige forventninger, hvilket i sidste ende fører til mere præcise og balancerede modelrespons.

Forskellige modeltyper kræver forskelligt format på træningsdata.

### Chat Completion

De trænings- og valideringsdata, du bruger, **skal** være formateret som et JSON Lines (JSONL) dokument. For `Phi-3-mini-128k-instruct` skal finjusteringsdatasættet være i det konversationsformat, som Chat completions API’en bruger.

### Eksempel på filformat

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Den understøttede filtype er JSON Lines. Filer uploades til standarddatabutikken og gøres tilgængelige i dit projekt.

## Finjustering af Phi-3 med Azure AI Foundry

Azure AI Foundry giver dig mulighed for at tilpasse store sprogmodeller til dine egne datasæt ved hjælp af en proces kaldet finjustering. Finjustering giver stor værdi ved at muliggøre tilpasning og optimering til specifikke opgaver og anvendelser. Det fører til forbedret ydeevne, omkostningseffektivitet, reduceret latenstid og skræddersyede output.

![Finetune AI Foundry](../../../../translated_images/AIFoundryfinetune.193aaddce48d553ce078eabed1526dfa300ae7fac7840e10b38fb50ea86b436c.da.png)

### Opret et nyt projekt

1. Log ind på [Azure AI Foundry](https://ai.azure.com).

1. Vælg **+New project** for at oprette et nyt projekt i Azure AI Foundry.

    ![FineTuneSelect](../../../../translated_images/select-new-project.cd31c0404088d7a32ee9018978b607dfb773956b15a88606f45579d3bc23c155.da.png)

1. Udfør følgende opgaver:

    - Projektets **Hub name**. Det skal være en unik værdi.
    - Vælg den **Hub**, der skal bruges (opret en ny, hvis nødvendigt).

    ![FineTuneSelect](../../../../translated_images/create-project.ca3b71298b90e42049ce8f6f452313bde644c309331fd728fcacd8954a20e26d.da.png)

1. Udfør følgende opgaver for at oprette en ny hub:

    - Indtast **Hub name**. Det skal være en unik værdi.
    - Vælg dit Azure **Subscription**.
    - Vælg den **Resource group**, der skal bruges (opret en ny, hvis nødvendigt).
    - Vælg den **Location**, du ønsker at bruge.
    - Vælg **Connect Azure AI Services** (opret en ny, hvis nødvendigt).
    - Vælg **Connect Azure AI Search** og vælg **Skip connecting**.

    ![FineTuneSelect](../../../../translated_images/create-hub.49e53d235e80779e95293c08654daf213e003b942a2fa81045b994c088acad7f.da.png)

1. Vælg **Next**.
1. Vælg **Create a project**.

### Dataforberedelse

Inden finjustering skal du samle eller oprette et datasæt, der er relevant for din opgave, såsom chatinstruktioner, spørgsmål-svar-par eller andre relevante tekstdata. Rens og forbehandl disse data ved at fjerne støj, håndtere manglende værdier og tokenisere teksten.

### Finjuster Phi-3 modeller i Azure AI Foundry

> [!NOTE]
> Finjustering af Phi-3 modeller understøttes i øjeblikket kun i projekter placeret i East US 2.

1. Vælg **Model catalog** i venstre sidepanel.

1. Skriv *phi-3* i **søgefeltet** og vælg den phi-3 model, du ønsker at bruge.

    ![FineTuneSelect](../../../../translated_images/select-model.60ef2d4a6a3cec57c3c45a8404613f25f8ad41534a209a88f5549e95d21320f8.da.png)

1. Vælg **Fine-tune**.

    ![FineTuneSelect](../../../../translated_images/select-finetune.a976213b543dd9d8d621e322d186ff670c3fb92bbba8435e6bcd4e79b9aab251.da.png)

1. Indtast navnet på den **Fine-tuned model**.

    ![FineTuneSelect](../../../../translated_images/finetune1.c2b39463f0d34148be1473af400e30e936c425f1cb8d5dbefcf9454008923402.da.png)

1. Vælg **Next**.

1. Udfør følgende opgaver:

    - Vælg **task type** til **Chat completion**.
    - Vælg de **Training data**, du vil bruge. Du kan uploade dem via Azure AI Foundrys data eller fra dit lokale miljø.

    ![FineTuneSelect](../../../../translated_images/finetune2.43cb099b1a94442df8f77c70e22fce46849329882a9e278ab1d87df196a63c4c.da.png)

1. Vælg **Next**.

1. Upload de **Validation data**, du vil bruge, eller vælg **Automatic split of training data**.

    ![FineTuneSelect](../../../../translated_images/finetune3.fd96121b67dcdd928568f64970980db22685ef54a4e48d1cc8d139c1ecb8c99f.da.png)

1. Vælg **Next**.

1. Udfør følgende opgaver:

    - Vælg den ønskede **Batch size multiplier**.
    - Vælg den ønskede **Learning rate**.
    - Vælg det ønskede antal **Epochs**.

    ![FineTuneSelect](../../../../translated_images/finetune4.e18b80ffccb5834a2690f855223a6e007bd8ca771663f7b0f5dbefb3c47850c3.da.png)

1. Vælg **Submit** for at starte finjusteringsprocessen.

    ![FineTuneSelect](../../../../translated_images/select-submit.0a3802d581bac27168ae1a8667026ad7f6c5f9188615113968272dbe1f7f774d.da.png)

1. Når din model er finjusteret, vises status som **Completed**, som vist på billedet nedenfor. Nu kan du implementere modellen og bruge den i din egen applikation, i playground eller i prompt flow. For mere information, se [How to deploy Phi-3 family of small language models with Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/completed.4dc8d2357144cdef5ba7303f42e9f1fca2baa37049bcededb5392d51cb21cc03.da.png)

> [!NOTE]
> For mere detaljeret information om finjustering af Phi-3, besøg venligst [Fine-tune Phi-3 models in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Ryd op i dine finjusterede modeller

Du kan slette en finjusteret model fra listen over finjusterede modeller i [Azure AI Foundry](https://ai.azure.com) eller fra modeldetaljesiden. Vælg den finjusterede model, du vil slette, på finjusteringssiden, og vælg derefter knappen Slet for at fjerne modellen.

> [!NOTE]
> Du kan ikke slette en brugerdefineret model, hvis den har en eksisterende implementering. Du skal først slette din modelimplementering, før du kan slette den brugerdefinerede model.

## Omkostninger og kvoter

### Omkostnings- og kvotebetragtninger for Phi-3 modeller finjusteret som en service

Phi-modeller finjusteret som en service tilbydes af Microsoft og er integreret med Azure AI Foundry til brug. Du kan finde priserne, når du [implementerer](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) eller finjusterer modellerne under fanen Pricing and terms i implementeringsguiden.

## Indholdsfiltrering

Modeller, der implementeres som en pay-as-you-go service, er beskyttet af Azure AI Content Safety. Når de implementeres til realtidsendpoints, kan du vælge at fravælge denne funktion. Med Azure AI Content Safety aktiveret, passerer både prompt og completion gennem en række klassifikationsmodeller, der har til formål at opdage og forhindre output af skadeligt indhold. Indholdsfiltreringssystemet opdager og reagerer på specifikke kategorier af potentielt skadeligt indhold i både input-prompter og output-completions. Læs mere om [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Finjusteringskonfiguration**

Hyperparametre: Definer hyperparametre som læringsrate, batchstørrelse og antal trænings-epochs.

**Loss-funktion**

Vælg en passende loss-funktion til din opgave (f.eks. cross-entropy).

**Optimizer**

Vælg en optimizer (f.eks. Adam) til gradientopdateringer under træning.

**Finjusteringsproces**

- Indlæs fortrænet model: Indlæs Phi-3 Mini checkpoint.
- Tilføj brugerdefinerede lag: Tilføj opgavespecifikke lag (f.eks. klassifikationshoved til chatinstruktioner).

**Træn modellen**  
Finjuster modellen med dit forberedte datasæt. Overvåg træningsforløbet og juster hyperparametre efter behov.

**Evaluering og validering**

Valideringssæt: Del dine data op i trænings- og valideringssæt.

**Evaluer ydeevne**

Brug metrikker som nøjagtighed, F1-score eller perplexity til at vurdere modellens ydeevne.

## Gem finjusteret model

**Checkpoint**  
Gem checkpoint for den finjusterede model til fremtidig brug.

## Implementering

- Implementer som webservice: Implementer din finjusterede model som en webservice i Azure AI Foundry.
- Test endpoint: Send testforespørgsler til det implementerede endpoint for at verificere funktionaliteten.

## Iterer og forbedr

Iterer: Hvis ydeevnen ikke er tilfredsstillende, kan du justere hyperparametre, tilføje mere data eller finjustere i flere epochs.

## Overvåg og forfin

Overvåg løbende modellens adfærd og forfin efter behov.

## Tilpas og udvid

Brugerdefinerede opgaver: Phi-3 Mini kan finjusteres til mange forskellige opgaver ud over chatinstruktioner. Udforsk andre anvendelsestilfælde!  
Eksperimenter: Prøv forskellige arkitekturer, lagkombinationer og teknikker for at forbedre ydeevnen.

> [!NOTE]
> Finjustering er en iterativ proces. Eksperimenter, lær og tilpas din model for at opnå de bedste resultater til din specifikke opgave!

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.