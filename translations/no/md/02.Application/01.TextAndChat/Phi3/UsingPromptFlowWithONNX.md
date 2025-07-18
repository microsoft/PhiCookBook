<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T03:01:18+00:00",
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
- Forbedre samarbeid: Legg til rette for bedre samarbeid mellom teammedlemmer ved å tilby et samlet utviklingsmiljø.

**Prompt flow** er en samling utviklingsverktøy som er laget for å effektivisere hele utviklingssyklusen for LLM-baserte AI-applikasjoner, fra idéutvikling, prototyping, testing, evaluering til produksjonsdistribusjon og overvåking. Det gjør prompt engineering mye enklere og gjør det mulig å bygge LLM-apper med produksjonskvalitet.

Prompt flow kan koble til OpenAI, Azure OpenAI Service og tilpassbare modeller (Huggingface, lokale LLM/SLM). Vi håper å distribuere Phi-3.5 sin kvantiserte ONNX-modell til lokale applikasjoner. Prompt flow kan hjelpe oss med å planlegge virksomheten bedre og fullføre lokale løsninger basert på Phi-3.5. I dette eksemplet vil vi kombinere ONNX Runtime GenAI Library for å fullføre Prompt flow-løsningen basert på Windows GPU.

## **Installasjon**

### **ONNX Runtime GenAI for Windows GPU**

Les denne veiledningen for å sette opp ONNX Runtime GenAI for Windows GPU [klikk her](./ORTWindowGPUGuideline.md)

### **Sett opp Prompt flow i VSCode**

1. Installer Prompt flow VS Code Extension

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.no.png)

2. Etter å ha installert Prompt flow VS Code Extension, klikk på utvidelsen og velg **Installation dependencies**. Følg denne veiledningen for å installere Prompt flow SDK i ditt miljø.

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.no.png)

3. Last ned [Sample Code](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) og åpne dette eksempelet i VS Code

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.no.png)

4. Åpne **flow.dag.yaml** for å velge ditt Python-miljø

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.no.png)

   Åpne **chat_phi3_ort.py** for å endre plasseringen av din Phi-3.5-instruct ONNX-modell

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.no.png)

5. Kjør din prompt flow for testing

Åpne **flow.dag.yaml** og klikk på visual editor

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.no.png)

etter å ha klikket på dette, kjør den for å teste

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.no.png)

1. Du kan kjøre batch i terminalen for å sjekke flere resultater


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Du kan sjekke resultatene i din standard nettleser


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.no.png)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.