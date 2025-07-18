<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T03:02:50+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "sw"
}
-->
# Kutumia Windows GPU kuunda suluhisho la Prompt flow na Phi-3.5-Instruct ONNX

Hati ifuatayo ni mfano wa jinsi ya kutumia PromptFlow na ONNX (Open Neural Network Exchange) kwa ajili ya kuendeleza programu za AI zinazotegemea mifano ya Phi-3.

PromptFlow ni seti ya zana za maendeleo zilizoundwa kurahisisha mzunguko mzima wa maendeleo ya programu za AI zinazotegemea LLM (Large Language Model), kuanzia mawazo na uundaji wa prototipu hadi upimaji na tathmini.

Kwa kuunganisha PromptFlow na ONNX, waendelezaji wanaweza:

- Kuboresha Utendaji wa Mfano: Tumia ONNX kwa ufanisi wa utambuzi na usambazaji wa modeli.
- Kurahisisha Maendeleo: Tumia PromptFlow kusimamia mtiririko wa kazi na kuendesha kazi zinazojirudia kiotomatiki.
- Kuongeza Ushirikiano: Rahisisha ushirikiano kati ya wanachama wa timu kwa kutoa mazingira ya maendeleo yaliyojumuishwa.

**Prompt flow** ni seti ya zana za maendeleo zilizoundwa kurahisisha mzunguko mzima wa maendeleo ya programu za AI zinazotegemea LLM, kuanzia mawazo, uundaji wa prototipu, upimaji, tathmini hadi usambazaji wa uzalishaji na ufuatiliaji. Inafanya uhandisi wa prompt kuwa rahisi zaidi na inakuwezesha kujenga programu za LLM zenye ubora wa uzalishaji.

Prompt flow inaweza kuunganishwa na OpenAI, Azure OpenAI Service, na mifano inayoweza kubadilishwa (Huggingface, LLM/SLM za ndani). Tunatarajia kusambaza modeli ya ONNX ya Phi-3.5 iliyopimwa kwa programu za ndani. Prompt flow inaweza kutusaidia kupanga biashara yetu vizuri na kukamilisha suluhisho za ndani zinazotegemea Phi-3.5. Katika mfano huu, tutachanganya ONNX Runtime GenAI Library kukamilisha suluhisho la Prompt flow linalotegemea Windows GPU.

## **Usanidi**

### **ONNX Runtime GenAI kwa Windows GPU**

Soma mwongozo huu kuweka ONNX Runtime GenAI kwa Windows GPU  [bonyeza hapa](./ORTWindowGPUGuideline.md)

### **Sanidi Prompt flow katika VSCode**

1. Sakinisha Prompt flow VS Code Extension

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.sw.png)

2. Baada ya kusakinisha Prompt flow VS Code Extension, bonyeza extension hiyo, kisha chagua **Installation dependencies** fuata mwongozo huu kusakinisha Prompt flow SDK katika mazingira yako

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.sw.png)

3. Pakua [Sample Code](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) na tumia VS Code kufungua sampuli hii

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.sw.png)

4. Fungua **flow.dag.yaml** kuchagua mazingira yako ya Python

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.sw.png)

   Fungua **chat_phi3_ort.py** kubadilisha eneo la Phi-3.5-instruct ONNX Model yako

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.sw.png)

5. Endesha prompt flow yako kwa ajili ya upimaji

Fungua **flow.dag.yaml** bonyeza mhariri wa kuona

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.sw.png)

baada ya kubonyeza hii, endesha kujaribu

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.sw.png)

1. Unaweza kuendesha batch kwenye terminal kuangalia matokeo zaidi


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Unaweza kuangalia matokeo katika kivinjari chako cha kawaida


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.sw.png)

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatuna dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.