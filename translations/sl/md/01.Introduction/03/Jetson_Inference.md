<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be4101a30d98e95a71d42c276e8bcd37",
  "translation_date": "2025-05-09T11:47:26+00:00",
  "source_file": "md/01.Introduction/03/Jetson_Inference.md",
  "language_code": "sl"
}
-->
# **Inference Phi-3 v Nvidia Jetson**

Nvidia Jetson je serija vgrajenih računalniških plošč iz Nvidie. Modeli Jetson TK1, TX1 in TX2 vsi uporabljajo Tegra procesor (ali SoC) iz Nvidie, ki vključuje ARM arhitekturo centralne procesne enote (CPU). Jetson je nizkoenergijski sistem, zasnovan za pospeševanje aplikacij strojnega učenja. Nvidia Jetson uporabljajo profesionalni razvijalci za ustvarjanje prelomnih AI produktov v vseh industrijah, pa tudi študentje in navdušenci za praktično učenje AI ter izdelavo izjemnih projektov. SLM je nameščen na robnih napravah, kot je Jetson, kar omogoča boljšo implementacijo industrijskih scenarijev generativne AI.

## Namestitev na NVIDIA Jetson:
Razvijalci, ki delajo na avtonomni robotiki in vgrajenih napravah, lahko izkoristijo Phi-3 Mini. Njegova relativno majhna velikost je idealna za robno nameščanje. Parametri so bili skrbno prilagojeni med treningom, kar zagotavlja visoko natančnost odgovorov.

### TensorRT-LLM Optimizacija:
NVIDIA-jeva [TensorRT-LLM knjižnica](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) optimizira inferenco velikih jezikovnih modelov. Podpira dolgo kontekstno okno Phi-3 Mini, kar izboljša tako prepustnost kot zakasnitev. Optimizacije vključujejo tehnike kot so LongRoPE, FP8 in inflight batching.

### Razpoložljivost in namestitev:
Razvijalci lahko preizkusijo Phi-3 Mini z 128K kontekstnim oknom na [NVIDIA AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/). Paket je na voljo kot NVIDIA NIM, mikroservis s standardnim API-jem, ki ga lahko namestite kjerkoli. Prav tako so na voljo [TensorRT-LLM implementacije na GitHubu](https://github.com/NVIDIA/TensorRT-LLM).

## **1. Priprava**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+

c. Cuda 11.8

d. Python 3.8+

## **2. Zagon Phi-3 na Jetson**

Lahko izberemo [Ollama](https://ollama.com) ali [LlamaEdge](https://llamaedge.com)

Če želite hkrati uporabljati gguf v oblaku in na robnih napravah, lahko LlamaEdge razumemo kot WasmEdge (WasmEdge je lahka, visoko zmogljiva in skalabilna WebAssembly runtime okolje, primerno za cloud native, edge in decentralizirane aplikacije. Podpira brezstrežniške aplikacije, vgrajene funkcije, mikroservise, pametne pogodbe in IoT naprave. Z LlamaEdge lahko na robne naprave in v oblak namestite kvantitativni model gguf.

![llamaedge](../../../../../translated_images/llamaedge.1356a35c809c5e9d89d8168db0c92161e87f5e2c34831f2fad800f00fc4e74dc.sl.jpg)

Tukaj so koraki za uporabo:

1. Namestite in prenesite ustrezne knjižnice in datoteke

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**Opomba**: llama-api-server.wasm in chatbot-ui morata biti v isti mapi

2. Zaženite skripte v terminalu

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

Tukaj je rezultat zagona

![llamaedgerun](../../../../../translated_images/llamaedgerun.66eb2acd7f14e814437879522158b9531ae7c955014d48d0708d0e4ce6ac94a6.sl.png)

***Vzorec kode*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

Na kratko, Phi-3 Mini predstavlja velik napredek na področju jezikovnih modelov, saj združuje učinkovitost, zavedanje konteksta in NVIDIA-jeve optimizacijske zmogljivosti. Ne glede na to, ali gradite robote ali robne aplikacije, je Phi-3 Mini močno orodje, ki ga je vredno poznati.

**Izjava o omejitvi odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvorno jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.