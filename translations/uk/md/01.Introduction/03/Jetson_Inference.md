<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be4101a30d98e95a71d42c276e8bcd37",
  "translation_date": "2025-07-16T20:46:26+00:00",
  "source_file": "md/01.Introduction/03/Jetson_Inference.md",
  "language_code": "uk"
}
-->
# **Інференс Phi-3 на Nvidia Jetson**

Nvidia Jetson — це серія вбудованих обчислювальних плат від Nvidia. Моделі Jetson TK1, TX1 та TX2 оснащені процесором Tegra (або SoC) від Nvidia, який інтегрує центральний процесор (CPU) на базі архітектури ARM. Jetson — це енергоефективна система, розроблена для прискорення застосунків машинного навчання. Nvidia Jetson використовується професійними розробниками для створення проривних AI-продуктів у різних галузях, а також студентами та ентузіастами для практичного вивчення AI та реалізації вражаючих проєктів. SLM розгортається на edge-пристроях, таких як Jetson, що дозволяє краще реалізовувати промислові сценарії застосування генеративного AI.

## Розгортання на NVIDIA Jetson:
Розробники, які працюють над автономною робототехнікою та вбудованими пристроями, можуть скористатися Phi-3 Mini. Відносно невеликий розмір Phi-3 робить його ідеальним для edge-розгортання. Параметри були ретельно налаштовані під час тренування, що забезпечує високу точність відповідей.

### Оптимізація TensorRT-LLM:
Бібліотека [TensorRT-LLM від NVIDIA](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) оптимізує інференс великих мовних моделей. Вона підтримує довге контекстне вікно Phi-3 Mini, покращуючи як пропускну здатність, так і затримку. Оптимізації включають такі технології, як LongRoPE, FP8 та inflight batching.

### Доступність та розгортання:
Розробники можуть ознайомитися з Phi-3 Mini з контекстним вікном 128K на [NVIDIA AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/). Він упакований як NVIDIA NIM — мікросервіс зі стандартним API, який можна розгортати будь-де. Також доступні [реалізації TensorRT-LLM на GitHub](https://github.com/NVIDIA/TensorRT-LLM).

## **1. Підготовка**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+

c. Cuda 11.8

d. Python 3.8+

## **2. Запуск Phi-3 на Jetson**

Можна обрати [Ollama](https://ollama.com) або [LlamaEdge](https://llamaedge.com)

Якщо ви хочете використовувати gguf одночасно в хмарі та на edge-пристроях, LlamaEdge можна розглядати як WasmEdge (WasmEdge — це легковагове, високопродуктивне, масштабоване середовище виконання WebAssembly, яке підходить для cloud native, edge та децентралізованих застосунків. Воно підтримує безсерверні застосунки, вбудовані функції, мікросервіси, смарт-контракти та IoT-пристрої). Ви можете розгорнути кількісну модель gguf на edge-пристроях і в хмарі через LlamaEdge.

![llamaedge](../../../../../translated_images/uk/llamaedge.e9d6ff96dff11cf7.jpg)

Ось кроки для використання

1. Встановіть і завантажте необхідні бібліотеки та файли

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**Примітка**: llama-api-server.wasm та chatbot-ui мають бути в одній директорії

2. Запустіть скрипти в терміналі

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

Ось результат запуску

![llamaedgerun](../../../../../translated_images/uk/llamaedgerun.bed921516c9a821c.png)

***Приклад коду*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

Підсумовуючи, Phi-3 Mini — це значний крок уперед у моделюванні мови, що поєднує ефективність, розуміння контексту та оптимізації NVIDIA. Незалежно від того, чи створюєте ви роботів або edge-застосунки, Phi-3 Mini — це потужний інструмент, про який варто знати.

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.