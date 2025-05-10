<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-05-09T10:49:42+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "tl"
}
-->
# **Inference Phi-3 sa Android**

Tuklasin natin kung paano ka makakapag-inference gamit ang Phi-3-mini sa mga Android device. Ang Phi-3-mini ay bagong serye ng mga modelo mula sa Microsoft na nagbibigay-daan para mag-deploy ng Large Language Models (LLMs) sa mga edge device at IoT device.

## Semantic Kernel at Inference

Ang [Semantic Kernel](https://github.com/microsoft/semantic-kernel) ay isang application framework na nagpapahintulot sa'yo na gumawa ng mga app na compatible sa Azure OpenAI Service, OpenAI models, at pati na rin sa mga lokal na modelo. Kung bago ka sa Semantic Kernel, inirerekomenda naming tingnan mo ang [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Para Ma-access ang Phi-3-mini Gamit ang Semantic Kernel

Pwede mo itong pagsamahin sa Hugging Face Connector sa Semantic Kernel. Tingnan ang [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Sa default, naka-link ito sa model ID sa Hugging Face. Pero pwede ka rin kumonekta sa locally built na Phi-3-mini model server.

### Pagtawag sa Quantized Models gamit ang Ollama o LlamaEdge

Maraming gumagamit ang mas gusto ang quantized models para patakbuhin ang mga modelo nang lokal. Pinapayagan ng [Ollama](https://ollama.com/) at [LlamaEdge](https://llamaedge.com) ang mga indibidwal na user na tumawag sa iba't ibang quantized models:

#### Ollama

Pwede mong patakbuhin nang direkta ang `ollama run Phi-3` o i-configure ito offline sa pamamagitan ng paggawa ng `Modelfile` na may path papunta sa iyong `.gguf` file.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Kung gusto mong gamitin ang `.gguf` files sa cloud at edge devices nang sabay, magandang option ang LlamaEdge. Pwede kang sumangguni sa [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) para makapagsimula.

### I-install at Patakbuhin sa Android Phones

1. **I-download ang MLC Chat app** (Libre) para sa Android phones.  
2. I-download ang APK file (148MB) at i-install ito sa iyong device.  
3. Buksan ang MLC Chat app. Makikita mo ang listahan ng mga AI model, kabilang ang Phi-3-mini.

Sa kabuuan, binubuksan ng Phi-3-mini ang mga kapanapanabik na posibilidad para sa generative AI sa mga edge device, at pwede mo nang simulan ang pag-explore ng mga kakayahan nito sa Android.

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong salin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng salin na ito.