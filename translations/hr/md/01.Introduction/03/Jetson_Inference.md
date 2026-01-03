<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be4101a30d98e95a71d42c276e8bcd37",
  "translation_date": "2025-07-16T20:45:51+00:00",
  "source_file": "md/01.Introduction/03/Jetson_Inference.md",
  "language_code": "hr"
}
-->
# **Inferencija Phi-3 na Nvidia Jetsonu**

Nvidia Jetson je serija ugrađenih računalnih ploča tvrtke Nvidia. Modeli Jetson TK1, TX1 i TX2 svi koriste Tegra procesor (ili SoC) iz Nvidie koji integrira ARM arhitekturu centralne procesorske jedinice (CPU). Jetson je sustav niske potrošnje energije i dizajniran je za ubrzavanje primjena strojnog učenja. Nvidia Jetson koriste profesionalni developeri za stvaranje revolucionarnih AI proizvoda u svim industrijama, kao i studenti i entuzijasti za praktično učenje AI-ja i izradu impresivnih projekata. SLM se implementira na edge uređajima poput Jetsona, što omogućuje bolju primjenu industrijskih scenarija generativne AI.

## Implementacija na NVIDIA Jetsonu:
Razvojni inženjeri koji rade na autonomnoj robotici i ugrađenim uređajima mogu iskoristiti Phi-3 Mini. Relativno mala veličina Phi-3 čini ga idealnim za edge implementaciju. Parametri su pažljivo podešeni tijekom treniranja, osiguravajući visoku točnost u odgovorima.

### TensorRT-LLM Optimizacija:
NVIDIA-ina [TensorRT-LLM biblioteka](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) optimizira inferenciju velikih jezičnih modela. Podržava dugi kontekstni prozor Phi-3 Mini modela, poboljšavajući i propusnost i latenciju. Optimizacije uključuju tehnike poput LongRoPE, FP8 i inflight batching.

### Dostupnost i implementacija:
Razvojni inženjeri mogu isprobati Phi-3 Mini s 128K kontekstnim prozorom na [NVIDIA AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/). Paket dolazi kao NVIDIA NIM, mikroservis sa standardnim API-jem koji se može implementirati bilo gdje. Također, [TensorRT-LLM implementacije na GitHubu](https://github.com/NVIDIA/TensorRT-LLM).

## **1. Priprema**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+

c. Cuda 11.8

d. Python 3.8+

## **2. Pokretanje Phi-3 na Jetsonu**

Možemo odabrati [Ollama](https://ollama.com) ili [LlamaEdge](https://llamaedge.com)

Ako želite koristiti gguf u oblaku i na edge uređajima istovremeno, LlamaEdge se može shvatiti kao WasmEdge (WasmEdge je lagano, visokoučinkovito i skalabilno WebAssembly runtime okruženje pogodno za cloud native, edge i decentralizirane aplikacije. Podržava serverless aplikacije, ugrađene funkcije, mikroservise, pametne ugovore i IoT uređaje. Kroz LlamaEdge možete implementirati kvantitativni model gguf-a na edge uređaje i u oblak.

![llamaedge](../../../../../translated_images/llamaedge.e9d6ff96dff11cf7.hr.jpg)

Evo koraka za korištenje:

1. Instalirajte i preuzmite povezane biblioteke i datoteke

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**Napomena**: llama-api-server.wasm i chatbot-ui moraju biti u istom direktoriju

2. Pokrenite skripte u terminalu

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

Ovo je rezultat pokretanja

![llamaedgerun](../../../../../translated_images/llamaedgerun.bed921516c9a821c.hr.png)

***Primjer koda*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

Ukratko, Phi-3 Mini predstavlja veliki iskorak u modeliranju jezika, spajajući učinkovitost, svijest o kontekstu i NVIDIA-ine optimizacijske sposobnosti. Bilo da gradite robote ili edge aplikacije, Phi-3 Mini je moćan alat koji vrijedi imati na umu.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.