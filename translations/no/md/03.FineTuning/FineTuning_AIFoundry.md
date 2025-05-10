<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c1559c5af6caccf6f623fd43a6b3a9a3",
  "translation_date": "2025-05-09T20:32:44+00:00",
  "source_file": "md/03.FineTuning/FineTuning_AIFoundry.md",
  "language_code": "no"
}
-->
# Finjustering av Phi-3 med Azure AI Foundry

La oss utforske hvordan du kan finjustere Microsofts Phi-3 Mini språkmodell ved hjelp av Azure AI Foundry. Finjustering gjør det mulig å tilpasse Phi-3 Mini til spesifikke oppgaver, noe som gjør den enda mer kraftfull og kontekstbevisst.

## Vurderinger

- **Muligheter:** Hvilke modeller kan finjusteres? Hva kan grunnmodellen finjusteres til å gjøre?
- **Kostnad:** Hva er prismodellen for finjustering?
- **Tilpasningsmuligheter:** Hvor mye kan jeg endre grunnmodellen – og på hvilke måter?
- **Bekvemmelighet:** Hvordan skjer finjusteringen i praksis – må jeg skrive egendefinert kode? Må jeg ha egen datakraft?
- **Sikkerhet:** Finjusterte modeller kan ha sikkerhetsrisikoer – finnes det noen sikkerhetsmekanismer for å beskytte mot utilsiktet skade?

![AIFoundry Models](../../../../translated_images/AIFoundryModels.4440430c9f07dbd6c625971422e7b9a5b9cb91fa046e447ba9ea41457860532f.no.png)

## Forberedelser til finjustering

### Forutsetninger

> [!NOTE]
> For Phi-3-familien er finjusteringstilbudet basert på betalingsmodell kun tilgjengelig for hubs opprettet i **East US 2** regioner.

- Et Azure-abonnement. Hvis du ikke har et Azure-abonnement, opprett en [betalt Azure-konto](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) for å komme i gang.

- Et [AI Foundry-prosjekt](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Azure rollebasert tilgangskontroll (Azure RBAC) brukes for å gi tilgang til operasjoner i Azure AI Foundry. For å utføre stegene i denne artikkelen må brukerkontoen din ha tildelt __Azure AI Developer-rollen__ på ressursgruppen.

### Registrering av abonnementets leverandør

Sjekk at abonnementet er registrert for `Microsoft.Network` ressursleverandøren.

1. Logg inn på [Azure-portalen](https://portal.azure.com).
1. Velg **Subscriptions** i venstremenyen.
1. Velg abonnementet du vil bruke.
1. Velg **AI project settings** > **Resource providers** i venstremenyen.
1. Bekreft at **Microsoft.Network** finnes i listen over ressursleverandører. Hvis ikke, legg det til.

### Datapreparering

Forbered trenings- og valideringsdataene dine for å finjustere modellen. Trenings- og valideringsdatasett består av input- og output-eksempler som viser hvordan du ønsker at modellen skal prestere.

Sørg for at alle trenings-eksemplene følger forventet format for inferens. For effektiv finjustering må datasettet være balansert og variert.

Dette innebærer å opprettholde databalansen, inkludere ulike scenarioer, og jevnlig forbedre treningsdataene for å samsvare med virkelige forventninger, noe som til slutt gir mer nøyaktige og balanserte modellrespons.

Ulike modelltyper krever ulikt format på treningsdata.

### Chat Completion

Trenings- og valideringsdataene du bruker **må** være formatert som et JSON Lines (JSONL) dokument. For `Phi-3-mini-128k-instruct` må finjusteringsdatasettet være formatert i det samtaleformatet som brukes av Chat completions API.

### Eksempel på filformat

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Støttet filtype er JSON Lines. Filene lastes opp til standard datalager og gjøres tilgjengelig i prosjektet ditt.

## Finjustering av Phi-3 med Azure AI Foundry

Azure AI Foundry lar deg tilpasse store språkmodeller til dine egne datasett ved hjelp av en prosess kalt finjustering. Finjustering gir betydelig verdi ved å muliggjøre tilpasning og optimalisering for spesifikke oppgaver og applikasjoner. Det fører til bedre ytelse, kostnadseffektivitet, redusert ventetid og skreddersydde resultater.

![Finetune AI Foundry](../../../../translated_images/AIFoundryfinetune.69ddc22d1ab08167a7e53a911cd33c749d99fea4047801a836ceb6eec66c5719.no.png)

### Opprett et nytt prosjekt

1. Logg inn på [Azure AI Foundry](https://ai.azure.com).

1. Velg **+New project** for å opprette et nytt prosjekt i Azure AI Foundry.

    ![FineTuneSelect](../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.no.png)

1. Gjør følgende:

    - Prosjektets **Hub name**. Det må være unikt.
    - Velg **Hub** som skal brukes (opprett ny om nødvendig).

    ![FineTuneSelect](../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.no.png)

1. Gjør følgende for å opprette en ny hub:

    - Skriv inn **Hub name**. Det må være unikt.
    - Velg din Azure **Subscription**.
    - Velg **Resource group** som skal brukes (opprett ny om nødvendig).
    - Velg **Location** du ønsker å bruke.
    - Velg **Connect Azure AI Services** som skal brukes (opprett ny om nødvendig).
    - Velg **Connect Azure AI Search** og velg **Skip connecting**.

    ![FineTuneSelect](../../../../translated_images/create-hub.b93d390a6d3eebd4c33eb7e4ea6ef41fd69c4d39f21339d4bda51af9ed70505f.no.png)

1. Velg **Next**.
1. Velg **Create a project**.

### Datapreparering

Før finjustering, samle eller lag et datasett relevant for oppgaven din, som chat-instruksjoner, spørsmål-svar-par eller annen relevant tekstdata. Rens og forhåndsbehandle dataene ved å fjerne støy, håndtere manglende verdier og tokenisere teksten.

### Finjuster Phi-3 modeller i Azure AI Foundry

> [!NOTE]
> Finjustering av Phi-3 modeller støttes for øyeblikket kun i prosjekter lokalisert i East US 2.

1. Velg **Model catalog** fra venstre tab.

1. Skriv *phi-3* i **søkelinjen** og velg phi-3 modellen du ønsker å bruke.

    ![FineTuneSelect](../../../../translated_images/select-model.02eef2cbb5b7e61a86526b05bd5ec9822fd6b2abae4e38fd5d9bdef541dfb967.no.png)

1. Velg **Fine-tune**.

    ![FineTuneSelect](../../../../translated_images/select-finetune.88cf562034f78baf0b7f41511fd4c45e1f068104238f1397661b9402ff9e2e09.no.png)

1. Skriv inn navnet på den **finjusterte modellen**.

    ![FineTuneSelect](../../../../translated_images/finetune1.8a20c66f797cc7ede7feb789a45c42713b7aeadfeb01dbc34446019db5c189d4.no.png)

1. Velg **Next**.

1. Gjør følgende:

    - Velg **task type** til **Chat completion**.
    - Velg **Training data** du ønsker å bruke. Du kan laste opp data via Azure AI Foundry eller fra ditt lokale miljø.

    ![FineTuneSelect](../../../../translated_images/finetune2.47df1aa177096dbaa01e4d64a06eb3f46a29718817fa706167af3ea01419a32f.no.png)

1. Velg **Next**.

1. Last opp **Validation data** du ønsker å bruke, eller velg **Automatic split of training data**.

    ![FineTuneSelect](../../../../translated_images/finetune3.e887e47240626c31f969532610c965594635c91cf3f94639fa60fb5d2bbd8f93.no.png)

1. Velg **Next**.

1. Gjør følgende:

    - Velg ønsket **Batch size multiplier**.
    - Velg ønsket **Learning rate**.
    - Velg ønsket antall **Epochs**.

    ![FineTuneSelect](../../../../translated_images/finetune4.9f47c2fad66fddd0f091b62a2fa6ac23260226ab841287805d843ebc83761801.no.png)

1. Velg **Submit** for å starte finjusteringsprosessen.

    ![FineTuneSelect](../../../../translated_images/select-submit.b5344fd77e49bfb6d4efe72e713f6a46f04323d871c118bbf59bf0217698dfee.no.png)

1. Når modellen din er finjustert, vises status som **Completed**, som vist under. Nå kan du distribuere modellen og bruke den i din egen applikasjon, i playground eller i prompt flow. For mer informasjon, se [How to deploy Phi-3 family of small language models with Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/completed.f4be2c6e660d8ba908d1d23e2102925cc31e57cbcd60fb10e7ad3b7925f585c4.no.png)

> [!NOTE]
> For mer detaljert informasjon om finjustering av Phi-3, besøk [Fine-tune Phi-3 models in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Rydd opp i dine finjusterte modeller

Du kan slette en finjustert modell fra finjusteringsmodellslisten i [Azure AI Foundry](https://ai.azure.com) eller fra modellens detaljside. Velg den finjusterte modellen du vil slette på Fine-tuning-siden, og velg deretter Slett-knappen for å fjerne modellen.

> [!NOTE]
> Du kan ikke slette en egendefinert modell hvis den har en aktiv distribusjon. Du må først slette modellens distribusjon før du kan slette den egendefinerte modellen.

## Kostnader og kvoter

### Kostnads- og kvotahensyn for Phi-3 modeller finjustert som tjeneste

Phi-modeller finjustert som tjeneste tilbys av Microsoft og er integrert med Azure AI Foundry. Du finner priser når du [distribuerer](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) eller finjusterer modeller under fanen Pricing and terms i distribusjonsveiviseren.

## Innholdsfiltrering

Modeller som distribueres som tjeneste med betalingsmodell er beskyttet av Azure AI Content Safety. Når de distribueres til sanntid-endepunkter, kan du velge å deaktivere denne funksjonen. Med Azure AI Content Safety aktivert, passerer både prompt og fullføring gjennom en rekke klassifiseringsmodeller som har som mål å oppdage og forhindre skadelig innhold. Innholdsfiltreringssystemet oppdager og håndterer spesifikke kategorier av potensielt skadelig innhold både i input-prompt og output-fullføringer. Les mer om [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Konfigurasjon for finjustering**

Hyperparametere: Definer hyperparametere som læringsrate, batch-størrelse og antall trenings-epoker.

**Tapfunksjon**

Velg en passende tapfunksjon for oppgaven din (f.eks. kryssentropi).

**Optimizer**

Velg en optimizer (f.eks. Adam) for gradientoppdateringer under trening.

**Finjusteringsprosess**

- Last inn forhåndstrent modell: Last inn Phi-3 Mini sjekkpunkt.
- Legg til egendefinerte lag: Legg til oppgavespesifikke lag (f.eks. klassifiseringshode for chat-instruksjoner).

**Tren modellen**  
Finjuster modellen med ditt forberedte datasett. Overvåk treningsprosessen og juster hyperparametere ved behov.

**Evaluering og validering**

Valideringssett: Del dataene dine inn i trenings- og valideringssett.

**Evaluer ytelse**

Bruk metrikker som nøyaktighet, F1-score eller perplexity for å vurdere modellens ytelse.

## Lagre finjustert modell

**Sjekkpunkt**  
Lagre sjekkpunktet for den finjusterte modellen for fremtidig bruk.

## Distribusjon

- Distribuer som webtjeneste: Distribuer din finjusterte modell som en webtjeneste i Azure AI Foundry.
- Test endepunkt: Send testspørringer til det distribuerte endepunktet for å verifisere funksjonalitet.

## Iterer og forbedre

Iterer: Hvis ytelsen ikke er tilfredsstillende, iterer ved å justere hyperparametere, legge til mer data eller finjustere flere epoker.

## Overvåk og forbedre

Overvåk modellens oppførsel kontinuerlig og forbedre ved behov.

## Tilpass og utvid

Egendefinerte oppgaver: Phi-3 Mini kan finjusteres for ulike oppgaver utover chat-instruksjoner. Utforsk flere bruksområder!  
Eksperimenter: Prøv ulike arkitekturer, lagkombinasjoner og teknikker for å forbedre ytelsen.

> [!NOTE]
> Finjustering er en iterativ prosess. Eksperimenter, lær og tilpass modellen for å oppnå best mulig resultat for din spesifikke oppgave!

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.