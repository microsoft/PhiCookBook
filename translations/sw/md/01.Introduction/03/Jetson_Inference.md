<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be4101a30d98e95a71d42c276e8bcd37",
  "translation_date": "2025-05-09T11:43:19+00:00",
  "source_file": "md/01.Introduction/03/Jetson_Inference.md",
  "language_code": "sw"
}
-->
# **Inference Phi-3 katika Nvidia Jetson**

Nvidia Jetson ni mfululizo wa bodi za kompyuta zilizojengwa kutoka Nvidia. Modeli za Jetson TK1, TX1 na TX2 zote zina processor ya Tegra (au SoC) kutoka Nvidia inayojumuisha CPU yenye usanifu wa ARM. Jetson ni mfumo wa nguvu kidogo na umeundwa kwa ajili ya kuharakisha matumizi ya mashine kujifunza. Nvidia Jetson hutumiwa na watengenezaji wa kitaalamu kuunda bidhaa za AI za kisasa katika sekta zote, na pia na wanafunzi na wapenzi kwa ajili ya kujifunza AI kwa vitendo na kutengeneza miradi ya kuvutia. SLM imewekwa kwenye vifaa vya edge kama Jetson, ambayo itasaidia utekelezaji bora wa matukio ya matumizi ya AI ya kizazi katika viwanda.

## Utekelezaji kwenye NVIDIA Jetson:
Watengenezaji wanaofanya kazi kwenye roboti zisizo na rubani na vifaa vilivyojengwa wanaweza kutumia Phi-3 Mini. Ukubwa mdogo wa Phi-3 unafanya iwe bora kwa utekelezaji kwenye edge. Vigezo vimeboreshwa kwa makini wakati wa mafunzo, kuhakikisha usahihi mkubwa katika majibu.

### Uboreshaji wa TensorRT-LLM:
Maktaba ya NVIDIA [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) huboresha utendaji wa mifano mikubwa ya lugha. Inasaidia dirisha refu la muktadha la Phi-3 Mini, ikiongeza throughput na latency. Uboreshaji unajumuisha mbinu kama LongRoPE, FP8, na inflight batching.

### Upatikanaji na Utekelezaji:
Watengenezaji wanaweza kujaribu Phi-3 Mini yenye dirisha la muktadha la 128K kwenye [NVIDIA's AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/). Imefungwa kama NVIDIA NIM, microservice yenye API ya kawaida inayoweza kupelekwa popote. Zaidi ya hayo, [utekelezaji wa TensorRT-LLM kwenye GitHub](https://github.com/NVIDIA/TensorRT-LLM).

## **1. Maandalizi**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+

c. Cuda 11.8

d. Python 3.8+

## **2. Kuendesha Phi-3 kwenye Jetson**

Tunaweza kuchagua [Ollama](https://ollama.com) au [LlamaEdge](https://llamaedge.com)

Ikiwa unataka kutumia gguf katika wingu na vifaa vya edge kwa wakati mmoja, LlamaEdge inaweza kueleweka kama WasmEdge (WasmEdge ni runtime nyepesi, yenye utendaji wa juu na inayoweza kupanuka ya WebAssembly inayofaa kwa programu za cloud native, edge na za usambazaji. Inasaidia programu zisizo na seva, kazi zilizojengwa ndani, microservices, mikataba smart na vifaa vya IoT. Unaweza kupeleka mfano wa kiasi cha gguf kwa vifaa vya edge na wingu kupitia LlamaEdge.

![llamaedge](../../../../../translated_images/llamaedge.1356a35c809c5e9d89d8168db0c92161e87f5e2c34831f2fad800f00fc4e74dc.sw.jpg)

Hapa ni hatua za kutumia

1. Sakinisha na pakua maktaba na faili zinazohusiana

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**Note**: llama-api-server.wasm na chatbot-ui lazima ziwe kwenye saraka moja

2. Endesha script kwenye terminal

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

Huu ni matokeo ya kuendesha

![llamaedgerun](../../../../../translated_images/llamaedgerun.66eb2acd7f14e814437879522158b9531ae7c955014d48d0708d0e4ce6ac94a6.sw.png)

***Sample code*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

Kwa muhtasari, Phi-3 Mini ni hatua kubwa mbele katika uundaji wa mifano ya lugha, ikichanganya ufanisi, ufahamu wa muktadha, na nguvu za uboreshaji za NVIDIA. Iwe unajenga roboti au programu za edge, Phi-3 Mini ni chombo chenye nguvu unachopaswa kufahamu.

**Kiarabu**:  
Hati hii imetafsiriwa kwa kutumia huduma ya utafsiri wa AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha kuaminika. Kwa taarifa muhimu, tafsiri ya mtaalamu wa binadamu inashauriwa. Hatuna wajibu wowote kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.