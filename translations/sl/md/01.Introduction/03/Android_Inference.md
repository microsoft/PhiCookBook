<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-05-09T10:53:09+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "sl"
}
-->
# **Inference Phi-3 in Android**

Chaliye dekhte hain ki aap Android devices par Phi-3-mini ke saath inference kaise kar sakte hain. Phi-3-mini Microsoft ki ek nayi model series hai jo Large Language Models (LLMs) ko edge devices aur IoT devices par deploy karne mein madad karti hai.

## Semantic Kernel aur Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) ek application framework hai jo aapko Azure OpenAI Service, OpenAI models, aur local models ke saath compatible applications banane deta hai. Agar aap Semantic Kernel mein naye hain, to hum aapko [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) dekhne ki salah dete hain.

### Semantic Kernel ke zariye Phi-3-mini ko Access karna

Aap ise Semantic Kernel ke Hugging Face Connector ke saath combine kar sakte hain. Iska reference aap is [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) mein dekh sakte hain.

By default, ye Hugging Face par model ID ke saath kaam karta hai. Lekin aap locally banaye gaye Phi-3-mini model server se bhi connect kar sakte hain.

### Ollama ya LlamaEdge ke zariye Quantized Models ko Call karna

Kai users quantized models ko pasand karte hain taaki models ko local level par chala sakein. [Ollama](https://ollama.com/) aur [LlamaEdge](https://llamaedge.com) individual users ko alag-alag quantized models call karne ka option dete hain:

#### Ollama

Aap seedha `ollama run Phi-3` chala sakte hain ya phir offline configuration ke liye apne `.gguf` file ke path ke saath ek `Modelfile` bana sakte hain.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Agar aap cloud aur edge devices dono par ek saath `.gguf` files use karna chahte hain, to LlamaEdge ek achha option hai. Iske liye aap is [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) ko refer kar sakte hain.

### Android Phones par Install aur Run karna

1. **MLC Chat app download karein** (Free) Android phones ke liye.  
2. APK file (148MB) download karke apne device par install karein.  
3. MLC Chat app launch karein. Aapko AI models ki list nazar aayegi, jisme Phi-3-mini bhi shamil hai.

Saaransh yeh hai ki Phi-3-mini edge devices par generative AI ke liye naye mauke kholta hai, aur aap Android par iske features explore karna shuru kar sakte hain.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI prevajanja [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.