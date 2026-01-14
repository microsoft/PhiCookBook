<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be4101a30d98e95a71d42c276e8bcd37",
  "translation_date": "2025-07-16T20:44:52+00:00",
  "source_file": "md/01.Introduction/03/Jetson_Inference.md",
  "language_code": "cs"
}
-->
# **Inference Phi-3 na Nvidia Jetson**

Nvidia Jetson je řada vestavěných výpočetních desek od Nvidia. Modely Jetson TK1, TX1 a TX2 všechny obsahují procesor Tegra (nebo SoC) od Nvidia, který integruje centrální procesorovou jednotku (CPU) s architekturou ARM. Jetson je nízkonapěťový systém navržený pro zrychlení aplikací strojového učení. Nvidia Jetson využívají profesionální vývojáři k vytváření průlomových AI produktů napříč všemi odvětvími, a také studenti a nadšenci pro praktické učení AI a tvorbu úžasných projektů. SLM je nasazeno v edge zařízeních, jako je Jetson, což umožní lepší implementaci průmyslových scénářů generativní AI.

## Nasazení na NVIDIA Jetson:
Vývojáři pracující na autonomních robotech a vestavěných zařízeních mohou využít Phi-3 Mini. Relativně malá velikost Phi-3 ji činí ideální pro nasazení na edge. Parametry byly pečlivě laděny během tréninku, což zajišťuje vysokou přesnost odpovědí.

### Optimalizace TensorRT-LLM:
NVIDIA [TensorRT-LLM knihovna](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) optimalizuje inference velkých jazykových modelů. Podporuje dlouhé kontextové okno Phi-3 Mini, čímž zlepšuje jak propustnost, tak latenci. Optimalizace zahrnují techniky jako LongRoPE, FP8 a inflight batching.

### Dostupnost a nasazení:
Vývojáři mohou vyzkoušet Phi-3 Mini s 128K kontextovým oknem na [NVIDIA AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/). Je balena jako NVIDIA NIM, mikroservis se standardním API, který lze nasadit kdekoli. Navíc jsou k dispozici [implementace TensorRT-LLM na GitHubu](https://github.com/NVIDIA/TensorRT-LLM).

## **1. Příprava**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+

c. Cuda 11.8

d. Python 3.8+

## **2. Spuštění Phi-3 na Jetson**

Můžeme zvolit [Ollama](https://ollama.com) nebo [LlamaEdge](https://llamaedge.com)

Pokud chcete používat gguf současně v cloudu i na edge zařízeních, LlamaEdge lze chápat jako WasmEdge (WasmEdge je lehké, vysoce výkonné a škálovatelné runtime prostředí WebAssembly vhodné pro cloud native, edge a decentralizované aplikace. Podporuje serverless aplikace, vestavěné funkce, mikroservisy, smart kontrakty a IoT zařízení). Pomocí LlamaEdge můžete nasadit kvantitativní model gguf na edge zařízení i do cloudu.

![llamaedge](../../../../../translated_images/cs/llamaedge.e9d6ff96dff11cf7.jpg)

Zde jsou kroky k použití

1. Nainstalujte a stáhněte související knihovny a soubory

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**Poznámka**: llama-api-server.wasm a chatbot-ui musí být ve stejném adresáři

2. Spusťte skripty v terminálu

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

Zde je výsledek spuštění

![llamaedgerun](../../../../../translated_images/cs/llamaedgerun.bed921516c9a821c.png)

***Ukázkový kód*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

Shrnuto, Phi-3 Mini představuje významný krok vpřed v modelování jazyka, kombinující efektivitu, povědomí o kontextu a optimalizační schopnosti NVIDIA. Ať už stavíte roboty nebo edge aplikace, Phi-3 Mini je mocný nástroj, který stojí za to znát.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.