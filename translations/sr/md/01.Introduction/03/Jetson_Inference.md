<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be4101a30d98e95a71d42c276e8bcd37",
  "translation_date": "2025-07-16T20:45:40+00:00",
  "source_file": "md/01.Introduction/03/Jetson_Inference.md",
  "language_code": "sr"
}
-->
# **Инференција Phi-3 на Nvidia Jetson**

Nvidia Jetson је серија уграђених рачунарских плоча компаније Nvidia. Модели Jetson TK1, TX1 и TX2 сви користе Tegra процесор (или SoC) из Nvidia који интегрише ARM архитектуру централне процесорске јединице (CPU). Jetson је систем ниске потрошње енергије и дизајниран је за убрзавање апликација машинског учења. Nvidia Jetson користе професионални програмери за креирање револуционарних AI производа у свим индустријама, као и студенти и ентузијасти за практично учење AI и прављење импресивних пројеката. SLM се примењује на уређајима на ивици мреже као што је Jetson, што омогућава бољу имплементацију индустријских сценарија генеративне AI примене.

## Деплојмент на NVIDIA Jetson:
Програмери који раде на аутономној роботики и уграђеним уређајима могу искористити Phi-3 Mini. Релативно мала величина Phi-3 чини га идеалним за деплојмент на ивици мреже. Параметри су пажљиво подешени током тренинга, што обезбеђује високу прецизност у одговорима.

### TensorRT-LLM оптимизација:
NVIDIA-ина [TensorRT-LLM библиотека](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) оптимизује инференцију великих језичких модела. Подржава дуги контекстни прозор Phi-3 Mini, побољшавајући и пропусност и латенцију. Оптимизације укључују технике као што су LongRoPE, FP8 и inflight batching.

### Доступност и деплојмент:
Програмери могу испробати Phi-3 Mini са 128K контекстним прозором на [NVIDIA AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/). Пакован је као NVIDIA NIM, микросервис са стандардним API-јем који се може деплојовати било где. Поред тога, ту су и [TensorRT-LLM имплементације на GitHub-у](https://github.com/NVIDIA/TensorRT-LLM).

## **1. Припрема**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+

c. Cuda 11.8

d. Python 3.8+

## **2. Покретање Phi-3 на Jetson**

Можемо изабрати [Ollama](https://ollama.com) или [LlamaEdge](https://llamaedge.com)

Ако желите да користите gguf и у облаку и на уређајима на ивици мреже истовремено, LlamaEdge се може схватити као WasmEdge (WasmEdge је лагано, високо перформантно и скалабилно WebAssembly окружење погодно за cloud native, edge и децентрализоване апликације. Подржава serverless апликације, уграђене функције, микросервисе, паметне уговоре и IoT уређаје). Можете деплојовати квантитативни модел gguf на уређаје на ивици и у облак преко LlamaEdge.

![llamaedge](../../../../../translated_images/sr/llamaedge.e9d6ff96dff11cf7.jpg)

Ево корака за коришћење

1. Инсталирајте и преузмите релевантне библиотеке и фајлове

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**Напомена**: llama-api-server.wasm и chatbot-ui морају бити у истом директоријуму

2. Покрените скрипте у терминалу

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

Ово је резултат покретања

![llamaedgerun](../../../../../translated_images/sr/llamaedgerun.bed921516c9a821c.png)

***Пример кода*** [Phi-3 mini WASM Notebook пример](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

Укратко, Phi-3 Mini представља велики искорак у моделовању језика, комбинујући ефикасност, свест о контексту и NVIDIA-ину оптимизациону снагу. Без обзира да ли правите роботе или апликације на ивици мреже, Phi-3 Mini је моћан алат који треба имати на уму.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.