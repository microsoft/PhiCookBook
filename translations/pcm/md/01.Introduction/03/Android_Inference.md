# **Inference Phi-3 for Android**

Make we check how you fit do inference wit Phi-3-mini for Android devices. Phi-3-mini na new series models wey Microsoft create wey dey allow make you fit put Large Language Models (LLMs) for edge devices and IoT devices.

## Semantic Kernel and Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) na application framework wey make e easy for you to create apps wey fit work with Azure OpenAI Service, OpenAI models, and even local models. If you be new for Semantic Kernel, we recommend say you check the [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### How To Access Phi-3-mini Using Semantic Kernel

You fit combine am wit the Hugging Face Connector for Semantic Kernel. Check this [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

By default, e dey linked to the model ID for Hugging Face. But you fit still connect to Phi-3-mini model server wey you build for your side.

### How To Call Quantized Models wit Ollama or LlamaEdge

Plenty people like to use quantized models to run models locally. [Ollama](https://ollama.com/) and [LlamaEdge](https://llamaedge.com) make am possible for individual users to call different quantized models:

#### Ollama

You fit run `ollama run Phi-3` directly or you fit configure am offline by creating a `Modelfile` wey get the path to your `.gguf` file.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

If you want to use `.gguf` files for cloud and edge devices at the same time, LlamaEdge na better option. You fit check this [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) to start.

### How To Install and Run for Android Phones

1. **Download the MLC Chat app** (Free) for Android phones.
2. Download the APK file (148MB) then install am for your phone.
3. Open the MLC Chat app. You go see list of AI models, including Phi-3-mini.

### Run Phi-4-mini-reasoning wit LiteRT-LM

[Phi-4-mini-reasoning](https://huggingface.co/litert-community/Phi-4-mini-reasoning) dey available as community-converted int4 `.litertlm` bundle for Google's [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) on-device runtime. For Android, e fit run for CPU or GPU through the [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) app (you fit import the bundle from Hugging Face inside the app) or through the LiteRT-LM Kotlin API; the same bundle fit run for iOS, macOS, Linux and Windows. The model card get the measured speeds and the commands to run am.

To summarize, Phi-3-mini open better chance for generative AI on edge devices, and you fit start to dey explore wetin e fit do for Android.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->