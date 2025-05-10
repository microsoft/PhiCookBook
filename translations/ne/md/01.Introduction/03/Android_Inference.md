<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-05-09T10:42:54+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "ne"
}
-->
# **Inference Phi-3 in Android**

Chaliye dekhiye kaise aap Phi-3-mini ke saath Android devices par inference kar sakte hain. Phi-3-mini Microsoft ki ek nayi series hai jo Large Language Models (LLMs) ko edge devices aur IoT devices par deploy karne mein madad karti hai.

## Semantic Kernel aur Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) ek application framework hai jo aapko Azure OpenAI Service, OpenAI models, aur local models ke saath compatible applications banane deta hai. Agar aap Semantic Kernel mein naye hain, toh hum aapko [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) dekhne ki salah dete hain.

### Semantic Kernel ke zariye Phi-3-mini ko Access Karna

Aap ise Semantic Kernel ke Hugging Face Connector ke saath combine kar sakte hain. Iska example aapko is [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) mein milega.

Default taur par yeh Hugging Face par model ID se connect hota hai. Lekin aap locally banaye gaye Phi-3-mini model server se bhi connect kar sakte hain.

### Quantized Models ko Ollama ya LlamaEdge ke saath Call Karna

Kai users quantized models ko pasand karte hain taaki models ko local machine par chalaya ja sake. [Ollama](https://ollama.com/) aur [LlamaEdge](https://llamaedge.com) individual users ko alag-alag quantized models call karne ki suvidha dete hain:

#### Ollama

Aap seedha `ollama run Phi-3` chala sakte hain ya offline configuration ke liye apne `.gguf` file ka path dete hue `Modelfile` bana sakte hain.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Agar aap cloud aur edge devices dono par `.gguf` files istemal karna chahte hain, toh LlamaEdge ek behtareen option hai. Shuruat karne ke liye aap is [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) ko dekh sakte hain.

### Android Phones par Install aur Run Karna

1. **MLC Chat app download karein** (Muft) Android phones ke liye.
2. APK file (148MB) download karke apne device par install karein.
3. MLC Chat app launch karein. Aapko AI models ki list dikhai degi, jisme Phi-3-mini bhi shamil hai.

Mukhtasar mein, Phi-3-mini edge devices par generative AI ke naye mauke kholta hai, aur aap Android par iski capabilities ko explore karna shuru kar sakte hain.

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयास गर्छौं, तर कृपया जानकार हुनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धिहरू हुन सक्छन्। मूल दस्तावेज यसको मूल भाषामा नै आधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीको लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।