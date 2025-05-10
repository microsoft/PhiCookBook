<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-05-09T18:53:21+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "da"
}
-->
# Brug af Windows GPU til at skabe Prompt flow-løsning med Phi-3.5-Instruct ONNX

Dette dokument er et eksempel på, hvordan man bruger PromptFlow med ONNX (Open Neural Network Exchange) til udvikling af AI-applikationer baseret på Phi-3-modeller.

PromptFlow er en samling udviklingsværktøjer designet til at strømline hele udviklingscyklussen for LLM-baserede (Large Language Model) AI-applikationer, fra idéudvikling og prototyping til test og evaluering.

Ved at integrere PromptFlow med ONNX kan udviklere:

- Optimere modelydelse: Udnyt ONNX til effektiv modelinference og implementering.
- Forenkle udvikling: Brug PromptFlow til at styre workflow og automatisere gentagne opgaver.
- Forbedre samarbejde: Fremme bedre samarbejde blandt teammedlemmer ved at tilbyde et samlet udviklingsmiljø.

**Prompt flow** er en samling udviklingsværktøjer designet til at strømline hele udviklingscyklussen for LLM-baserede AI-applikationer, fra idéudvikling, prototyping, test, evaluering til produktionsimplementering og overvågning. Det gør prompt engineering meget nemmere og giver dig mulighed for at bygge LLM-apps med produktionskvalitet.

Prompt flow kan forbindes til OpenAI, Azure OpenAI Service og tilpassede modeller (Huggingface, lokale LLM/SLM). Vi håber at implementere Phi-3.5's kvantiserede ONNX-model til lokale applikationer. Prompt flow kan hjælpe os med bedre at planlægge vores forretning og færdiggøre lokale løsninger baseret på Phi-3.5. I dette eksempel vil vi kombinere ONNX Runtime GenAI Library for at færdiggøre Prompt flow-løsningen baseret på Windows GPU.

## **Installation**

### **ONNX Runtime GenAI for Windows GPU**

Læs denne vejledning for at sætte ONNX Runtime GenAI op til Windows GPU [klik her](./ORTWindowGPUGuideline.md)

### **Opsæt Prompt flow i VSCode**

1. Installer Prompt flow VS Code Extension

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.da.png)

2. Efter installation af Prompt flow VS Code Extension, klik på udvidelsen og vælg **Installation dependencies** følg denne vejledning for at installere Prompt flow SDK i dit miljø

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.da.png)

3. Download [Sample Code](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) og brug VS Code til at åbne dette eksempel

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.da.png)

4. Åbn **flow.dag.yaml** for at vælge dit Python-miljø

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.da.png)

   Åbn **chat_phi3_ort.py** for at ændre placeringen af din Phi-3.5-instruct ONNX-model

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.da.png)

5. Kør din prompt flow til test

Åbn **flow.dag.yaml** og klik på visual editor

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.da.png)

efter klik, kør den for at teste

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.da.png)

1. Du kan køre batch i terminalen for at tjekke flere resultater


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Du kan se resultaterne i din standardbrowser


![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.da.png)

**Ansvarsfraskrivelse**:  
Dette dokument er oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.