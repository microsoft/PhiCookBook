<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-05-09T18:53:29+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "no"
}
-->
# Bruke Windows GPU for å lage Prompt flow-løsning med Phi-3.5-Instruct ONNX

Følgende dokument er et eksempel på hvordan man bruker PromptFlow med ONNX (Open Neural Network Exchange) for å utvikle AI-applikasjoner basert på Phi-3-modeller.

PromptFlow er en samling utviklingsverktøy designet for å effektivisere hele utviklingssyklusen for LLM-baserte (Large Language Model) AI-applikasjoner, fra idéutvikling og prototyping til testing og evaluering.

Ved å integrere PromptFlow med ONNX kan utviklere:

- Optimalisere modellens ytelse: Utnytt ONNX for effektiv modellinferenz og distribusjon.
- Forenkle utviklingen: Bruk PromptFlow til å administrere arbeidsflyten og automatisere repeterende oppgaver.
- Forbedre samarbeid: Legge til rette for bedre samarbeid blant teammedlemmer ved å tilby et enhetlig utviklingsmiljø.

**Prompt flow** er en samling utviklingsverktøy som er laget for å effektivisere hele utviklingssyklusen for LLM-baserte AI-applikasjoner, fra idéutvikling, prototyping, testing, evaluering til produksjonsdistribusjon og overvåking. Det gjør prompt engineering mye enklere og gjør det mulig å bygge LLM-apper med produksjonskvalitet.

Prompt flow kan kobles til OpenAI, Azure OpenAI Service, og tilpassbare modeller (Huggingface, lokale LLM/SLM). Vi håper å distribuere Phi-3.5 sin kvantiserte ONNX-modell til lokale applikasjoner. Prompt flow kan hjelpe oss med å planlegge virksomheten bedre og fullføre lokale løsninger basert på Phi-3.5. I dette eksemplet vil vi kombinere ONNX Runtime GenAI Library for å fullføre Prompt flow-løsningen basert på Windows GPU.

## **Installasjon**

### **ONNX Runtime GenAI for Windows GPU**

Les denne veiledningen for å sette opp ONNX Runtime GenAI for Windows GPU [klikk her](./ORTWindowGPUGuideline.md)

### **Sett opp Prompt flow i VSCode**

1. Installer Prompt flow VS Code Extension

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.no.png)

2. Etter at du har installert Prompt flow VS Code Extension, klikk på utvidelsen, og velg **Installation dependencies** og følg denne veiledningen for å installere Prompt flow SDK i ditt miljø

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.no.png)

3. Last ned [Sample Code](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) og åpne dette eksemplet i VS Code

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.no.png)

4. Åpne **flow.dag.yaml** for å velge ditt Python-miljø

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.no.png)

   Åpne **chat_phi3_ort.py** for å endre plasseringen av din Phi-3.5-instruct ONNX-modell

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.no.png)

5. Kjør din prompt flow for testing

Åpne **flow.dag.yaml** og klikk på visual editor

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.no.png)

etter å ha klikket her, kjør det for å teste

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.no.png)

1. Du kan kjøre batch i terminalen for å sjekke flere resultater


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Du kan sjekke resultatene i din standard nettleser


![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.no.png)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.