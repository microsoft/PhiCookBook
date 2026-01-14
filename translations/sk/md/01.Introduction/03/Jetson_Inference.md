<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be4101a30d98e95a71d42c276e8bcd37",
  "translation_date": "2025-07-16T20:45:03+00:00",
  "source_file": "md/01.Introduction/03/Jetson_Inference.md",
  "language_code": "sk"
}
-->
# **Inference Phi-3 na Nvidia Jetson**

Nvidia Jetson je séria zabudovaných výpočtových dosiek od Nvidia. Modely Jetson TK1, TX1 a TX2 všetky obsahujú Tegra procesor (alebo SoC) od Nvidia, ktorý integruje centrálnu procesorovú jednotku (CPU) s architektúrou ARM. Jetson je nízkoenergetický systém navrhnutý na zrýchlenie aplikácií strojového učenia. Nvidia Jetson používajú profesionálni vývojári na vytváranie prelomových AI produktov v rôznych odvetviach, ako aj študenti a nadšenci na praktické učenie AI a tvorbu úžasných projektov. SLM je nasadený v edge zariadeniach ako Jetson, čo umožní lepšiu implementáciu priemyselných scenárov generatívnej AI.

## Nasadenie na NVIDIA Jetson:
Vývojári pracujúci na autonómnej robotike a zabudovaných zariadeniach môžu využiť Phi-3 Mini. Relatívne malá veľkosť Phi-3 ho robí ideálnym pre edge nasadenie. Parametre boli počas tréningu starostlivo doladené, čo zabezpečuje vysokú presnosť odpovedí.

### Optimalizácia TensorRT-LLM:
NVIDIA [TensorRT-LLM knižnica](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) optimalizuje inferenciu veľkých jazykových modelov. Podporuje dlhé kontextové okno Phi-3 Mini, čím zlepšuje priepustnosť aj latenciu. Optimalizácie zahŕňajú techniky ako LongRoPE, FP8 a inflight batching.

### Dostupnosť a nasadenie:
Vývojári môžu preskúmať Phi-3 Mini s 128K kontextovým oknom na [NVIDIA AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/). Je zabalený ako NVIDIA NIM, mikroservis so štandardným API, ktorý je možné nasadiť kdekoľvek. Okrem toho sú k dispozícii [implementácie TensorRT-LLM na GitHube](https://github.com/NVIDIA/TensorRT-LLM).

## **1. Príprava**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+

c. Cuda 11.8

d. Python 3.8+

## **2. Spustenie Phi-3 na Jetson**

Môžeme si vybrať [Ollama](https://ollama.com) alebo [LlamaEdge](https://llamaedge.com)

Ak chcete používať gguf súčasne v cloude aj na edge zariadeniach, LlamaEdge možno chápať ako WasmEdge (WasmEdge je ľahké, vysoko výkonné a škálovateľné runtime prostredie WebAssembly vhodné pre cloud native, edge a decentralizované aplikácie. Podporuje serverless aplikácie, zabudované funkcie, mikroservisy, smart kontrakty a IoT zariadenia). Pomocou LlamaEdge môžete nasadiť kvantifikovaný model gguf na edge zariadenia aj do cloudu.

![llamaedge](../../../../../translated_images/sk/llamaedge.e9d6ff96dff11cf7.jpg)

Tu sú kroky na použitie

1. Nainštalujte a stiahnite súvisiace knižnice a súbory

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**Poznámka**: llama-api-server.wasm a chatbot-ui musia byť v rovnakom adresári

2. Spustite skripty v termináli

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

Tu je výsledok spustenia

![llamaedgerun](../../../../../translated_images/sk/llamaedgerun.bed921516c9a821c.png)

***Ukážkový kód*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

Na záver, Phi-3 Mini predstavuje významný pokrok v modelovaní jazyka, kombinujúc efektivitu, kontextové povedomie a optimalizačné schopnosti NVIDIA. Či už budujete roboty alebo edge aplikácie, Phi-3 Mini je silný nástroj, ktorý stojí za to poznať.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.