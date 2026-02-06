# **Inference Phi-3 on Android**

Let's explore how you can perform inference with Phi-3-mini on Android devices. Phi-3-mini is a new series of models from Microsoft that enables deployment of Large Language Models (LLMs) on edge devices and IoT devices.

## Semantic Kernel and Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) is an application framework that allows you to create applications compatible with Azure OpenAI Service, OpenAI models, and even local models. If you are new to Semantic Kernel, we recommend checking out the [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Accessing Phi-3-mini Using Semantic Kernel

You can integrate it with the Hugging Face Connector in Semantic Kernel. See this [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

By default, it connects to the model ID on Hugging Face. However, you can also connect to a locally hosted Phi-3-mini model server.

### Running Quantized Models with Ollama or LlamaEdge

Many users prefer using quantized models to run them locally. [Ollama](https://ollama.com/) and [LlamaEdge](https://llamaedge.com) allow individual users to run various quantized models:

#### Ollama

You can run `ollama run Phi-3` directly or set it up offline by creating a `Modelfile` pointing to your `.gguf` file.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

If you want to use `.gguf` files both in the cloud and on edge devices, LlamaEdge is a great option. Check out this [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) to get started.

### Install and Run on Android Phones

1. **Download the MLC Chat app** (Free) for Android phones.  
2. Download the APK file (148MB) and install it on your device.  
3. Launch the MLC Chat app. You’ll see a list of AI models, including Phi-3-mini.

In summary, Phi-3-mini opens up exciting possibilities for generative AI on edge devices, and you can start exploring its capabilities on Android.

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.