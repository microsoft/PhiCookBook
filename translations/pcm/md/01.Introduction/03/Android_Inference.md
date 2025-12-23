<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-12-22T01:19:30+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "pcm"
}
-->
# **Inference Phi-3 for Android**

Make we explore how you fit perform inference with Phi-3-mini for Android devices. Phi-3-mini na new series of models from Microsoft wey dey enable deployment of Large Language Models (LLMs) for edge devices and IoT devices.

## Semantic Kernel and Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) na application framework wey dey allow you create applications wey dey compatible with Azure OpenAI Service, OpenAI models, and even local models. If you new to Semantic Kernel, we suggest make you check the [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### To Access Phi-3-mini Using Semantic Kernel

You fit combine am with the Hugging Face Connector for Semantic Kernel. Check this [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

By default, e dey correspond to the model ID for Hugging Face. But you fit also connect to a locally built Phi-3-mini model server.

### Calling Quantized Models with Ollama or LlamaEdge

Plenty users prefer to use quantized models to run models locally. [Ollama](https://ollama.com/) and [LlamaEdge](https://llamaedge.com) dey allow individual users to call different quantized models:

#### Ollama

You fit run `ollama run Phi-3` directly or configure am offline by creating a `Modelfile` with the path to your `.gguf` file.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

If you wan use `.gguf` files for the cloud and on edge devices at the same time, LlamaEdge na great choice. You fit refer to this [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) to start.

### Install and Run on Android Phones

1. **Download the MLC Chat app** (Free) for Android phones.
2. Download the APK file (148MB) and install am on your device.
3. Launch the MLC Chat app. You go see a list of AI models, including Phi-3-mini.

In summary, Phi-3-mini dey open exciting possibilities for generative AI on edge devices, and you fit start explore im capabilities on Android.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Abeg note:
Dis document don translate wit AI translation service Co-op Translator (https://github.com/Azure/co-op-translator). Even though we dey try make everything correct, abeg sabi say automated translations fit get mistakes or no too correct. Make una still regard the original document for im original language as the official source. For important information, we recommend say una use professional human translator. We no dey responsible for any misunderstanding or wrong interpretation wey fit come from using this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->