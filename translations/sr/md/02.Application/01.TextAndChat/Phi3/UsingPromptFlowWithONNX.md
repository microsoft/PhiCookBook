<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-05-09T18:55:39+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "sr"
}
-->
# Korišćenje Windows GPU za kreiranje Prompt flow rešenja sa Phi-3.5-Instruct ONNX

Sledeći dokument je primer kako koristiti PromptFlow sa ONNX (Open Neural Network Exchange) za razvoj AI aplikacija zasnovanih na Phi-3 modelima.

PromptFlow je paket razvojnih alata dizajniran da pojednostavi ceo razvojni ciklus AI aplikacija zasnovanih na LLM (Large Language Model), od ideje i prototipa do testiranja i evaluacije.

Integracijom PromptFlow sa ONNX, programeri mogu:

- Optimizovati performanse modela: Iskoristiti ONNX za efikasno izvođenje modela i implementaciju.
- Pojednostaviti razvoj: Koristiti PromptFlow za upravljanje radnim tokovima i automatizaciju ponavljajućih zadataka.
- Poboljšati saradnju: Omogućiti bolju saradnju među članovima tima kroz jedinstveno razvojno okruženje.

**Prompt flow** je paket razvojnih alata dizajniran da pojednostavi ceo razvojni ciklus AI aplikacija zasnovanih na LLM, od ideje, prototipa, testiranja, evaluacije do implementacije u produkciju i praćenja. Olakšava prompt inženjering i omogućava vam da pravite LLM aplikacije sa kvalitetom za produkciju.

Prompt flow može da se poveže sa OpenAI, Azure OpenAI Service i prilagodljivim modelima (Huggingface, lokalni LLM/SLM). Planiramo da implementiramo kvantizovani Phi-3.5 ONNX model u lokalne aplikacije. Prompt flow nam može pomoći da bolje isplaniramo poslovanje i završimo lokalna rešenja bazirana na Phi-3.5. U ovom primeru ćemo kombinovati ONNX Runtime GenAI biblioteku da završimo Prompt flow rešenje bazirano na Windows GPU.

## **Instalacija**

### **ONNX Runtime GenAI za Windows GPU**

Pročitajte ovaj vodič za podešavanje ONNX Runtime GenAI za Windows GPU [kliknite ovde](./ORTWindowGPUGuideline.md)

### **Podešavanje Prompt flow u VSCode**

1. Instalirajte Prompt flow VS Code ekstenziju

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.sr.png)

2. Nakon instalacije Prompt flow VS Code ekstenzije, kliknite na ekstenziju i izaberite **Installation dependencies** pratite ovaj vodič da instalirate Prompt flow SDK u vašem okruženju

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.sr.png)

3. Preuzmite [Sample Code](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) i otvorite ovaj primer u VS Code

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.sr.png)

4. Otvorite **flow.dag.yaml** da izaberete vaše Python okruženje

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.sr.png)

   Otvorite **chat_phi3_ort.py** da promenite lokaciju Phi-3.5-instruct ONNX modela

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.sr.png)

5. Pokrenite vaš prompt flow za testiranje

Otvorite **flow.dag.yaml** i kliknite na vizuelni editor

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.sr.png)

nakon klika, pokrenite da testirate

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.sr.png)

1. Možete pokrenuti batch u terminalu da proverite više rezultata


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Rezultate možete proveriti u vašem podrazumevanom pregledaču


![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.sr.png)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешне тумачења која произилазе из употребе овог превода.