<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be4101a30d98e95a71d42c276e8bcd37",
  "translation_date": "2025-05-09T11:43:50+00:00",
  "source_file": "md/01.Introduction/03/Jetson_Inference.md",
  "language_code": "hu"
}
-->
# **Phi-3 következtetés Nvidia Jetsonon**

Az Nvidia Jetson az Nvidia beágyazott számítástechnikai lapkáinak sorozata. A Jetson TK1, TX1 és TX2 modellek mindegyike egy Nvidia Tegra processzort (vagy SoC-t) tartalmaz, amely integrál egy ARM architektúrás központi feldolgozó egységet (CPU). A Jetson alacsony fogyasztású rendszer, amelyet gépi tanulási alkalmazások gyorsítására terveztek. Az Nvidia Jetson professzionális fejlesztők által használatos, hogy áttörő AI termékeket hozzanak létre minden iparágban, valamint diákok és lelkes amatőrök számára is, akik kézzel fogható AI tanulásra és lenyűgöző projektek készítésére törekednek. Az SLM-t élő eszközökön, például Jetsonon telepítik, amely jobb megvalósítást tesz lehetővé ipari generatív AI alkalmazási forgatókönyvekben.

## Telepítés NVIDIA Jetsonon:
Az autonóm robotikával és beágyazott eszközökkel foglalkozó fejlesztők kihasználhatják a Phi-3 Mini előnyeit. A Phi-3 viszonylag kicsi mérete miatt ideális élvégponti telepítéshez. A paramétereket gondosan hangolták a tanítás során, biztosítva a válaszok magas pontosságát.

### TensorRT-LLM optimalizáció:
Az NVIDIA [TensorRT-LLM könyvtára](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) optimalizálja a nagy nyelvi modellek következtetését. Támogatja a Phi-3 Mini hosszú kontextusablakát, javítva a feldolgozási sebességet és a késleltetést. Az optimalizációk között szerepelnek olyan technikák, mint a LongRoPE, FP8 és az inflight batchelés.

### Elérhetőség és telepítés:
A fejlesztők felfedezhetik a Phi-3 Mini 128K kontextusablakos változatát az [NVIDIA AI oldalán](https://www.nvidia.com/en-us/ai-data-science/generative-ai/). Ez egy NVIDIA NIM-ként van csomagolva, egy szabványos API-val rendelkező mikroszolgáltatás, amely bárhol telepíthető. Ezen felül elérhetők a [TensorRT-LLM implementációk a GitHubon](https://github.com/NVIDIA/TensorRT-LLM).

## **1. Előkészületek**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+

c. Cuda 11.8

d. Python 3.8+

## **2. Phi-3 futtatása Jetsonon**

Választhatunk [Ollama](https://ollama.com) vagy [LlamaEdge](https://llamaedge.com) között.

Ha egyszerre szeretnéd használni a gguf-ot felhőben és élvégponti eszközökön, a LlamaEdge értelmezhető úgy, mint a WasmEdge (a WasmEdge egy könnyű, nagy teljesítményű, skálázható WebAssembly futtatókörnyezet, amely alkalmas felhő natív, élvégponti és decentralizált alkalmazásokhoz. Támogatja a szerver nélküli alkalmazásokat, beágyazott funkciókat, mikroszolgáltatásokat, okosszerződéseket és IoT eszközöket. A gguf kvantitatív modelljét a LlamaEdge segítségével telepítheted élvégponti eszközökre és a felhőbe egyaránt.

![llamaedge](../../../../../translated_images/llamaedge.1356a35c809c5e9d89d8168db0c92161e87f5e2c34831f2fad800f00fc4e74dc.hu.jpg)

Íme a használat lépései:

1. Telepítsd és töltsd le a kapcsolódó könyvtárakat és fájlokat

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**Megjegyzés**: a llama-api-server.wasm és a chatbot-ui ugyanabban a könyvtárban kell legyenek

2. Futtasd a szkripteket a terminálban

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

Íme a futtatási eredmény

![llamaedgerun](../../../../../translated_images/llamaedgerun.66eb2acd7f14e814437879522158b9531ae7c955014d48d0708d0e4ce6ac94a6.hu.png)

***Minta kód*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

Összefoglalva, a Phi-3 Mini jelentős előrelépést képvisel a nyelvi modellezésben, ötvözve a hatékonyságot, a kontextus-érzékenységet és az NVIDIA optimalizációs képességeit. Akár robotokat építesz, akár élvégponti alkalmazásokat fejlesztesz, a Phi-3 Mini egy erőteljes eszköz, amit érdemes ismerni.

**Nyilatkozat**:  
Ezt a dokumentumot az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.