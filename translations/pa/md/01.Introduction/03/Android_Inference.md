<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-07-16T20:12:52+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "pa"
}
-->
# **ਐਂਡਰਾਇਡ ਵਿੱਚ Inference Phi-3**

ਆਓ ਵੇਖੀਏ ਕਿ ਤੁਸੀਂ ਐਂਡਰਾਇਡ ਡਿਵਾਈਸਾਂ 'ਤੇ Phi-3-mini ਨਾਲ ਕਿਵੇਂ inference ਕਰ ਸਕਦੇ ਹੋ। Phi-3-mini ਮਾਈਕ੍ਰੋਸਾਫਟ ਦੀ ਇੱਕ ਨਵੀਂ ਮਾਡਲ ਸੀਰੀਜ਼ ਹੈ ਜੋ ਐਜ ਡਿਵਾਈਸਾਂ ਅਤੇ IoT ਡਿਵਾਈਸਾਂ 'ਤੇ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ (LLMs) ਨੂੰ ਡਿਪਲੋਇ ਕਰਨ ਦੀ ਸਹੂਲਤ ਦਿੰਦੀ ਹੈ।

## Semantic Kernel ਅਤੇ Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) ਇੱਕ ਐਪਲੀਕੇਸ਼ਨ ਫਰੇਮਵਰਕ ਹੈ ਜੋ ਤੁਹਾਨੂੰ ਐਜਰ OpenAI ਸਰਵਿਸ, OpenAI ਮਾਡਲਾਂ ਅਤੇ ਇੱਥੋਂ ਤੱਕ ਕਿ ਲੋਕਲ ਮਾਡਲਾਂ ਨਾਲ ਕੰਪੈਟਿਬਲ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਜੇ ਤੁਸੀਂ Semantic Kernel ਵਿੱਚ ਨਵੇਂ ਹੋ, ਤਾਂ ਅਸੀਂ ਤੁਹਾਨੂੰ [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) ਵੇਖਣ ਦੀ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ।

### Semantic Kernel ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3-mini ਤੱਕ ਪਹੁੰਚ

ਤੁਸੀਂ ਇਸਨੂੰ Semantic Kernel ਵਿੱਚ Hugging Face Connector ਨਾਲ ਜੋੜ ਸਕਦੇ ਹੋ। ਇਸ [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) ਨੂੰ ਦੇਖੋ।

ਡਿਫਾਲਟ ਤੌਰ 'ਤੇ, ਇਹ Hugging Face 'ਤੇ ਮਾਡਲ ID ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ। ਪਰ ਤੁਸੀਂ ਲੋਕਲ ਤੌਰ 'ਤੇ ਬਣਾਏ ਗਏ Phi-3-mini ਮਾਡਲ ਸਰਵਰ ਨਾਲ ਵੀ ਕਨੈਕਟ ਕਰ ਸਕਦੇ ਹੋ।

### Ollama ਜਾਂ LlamaEdge ਨਾਲ Quantized ਮਾਡਲਾਂ ਨੂੰ ਕਾਲ ਕਰਨਾ

ਕਈ ਯੂਜ਼ਰ ਲੋਕਲ ਤੌਰ 'ਤੇ ਮਾਡਲ ਚਲਾਉਣ ਲਈ quantized ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਪਸੰਦ ਕਰਦੇ ਹਨ। [Ollama](https://ollama.com/) ਅਤੇ [LlamaEdge](https://llamaedge.com) ਵੱਖ-ਵੱਖ quantized ਮਾਡਲਾਂ ਨੂੰ ਕਾਲ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ:

#### Ollama

ਤੁਸੀਂ ਸਿੱਧਾ `ollama run Phi-3` ਚਲਾ ਸਕਦੇ ਹੋ ਜਾਂ ਆਪਣੇ `.gguf` ਫਾਇਲ ਦੇ ਪਾਥ ਨਾਲ ਇੱਕ `Modelfile` ਬਣਾਕੇ ਇਸਨੂੰ ਆਫਲਾਈਨ ਕਨਫਿਗਰ ਕਰ ਸਕਦੇ ਹੋ।

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

ਜੇ ਤੁਸੀਂ ਕਲਾਉਡ ਅਤੇ ਐਜ ਡਿਵਾਈਸਾਂ 'ਤੇ ਇਕੱਠੇ `.gguf` ਫਾਇਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਨੀ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ LlamaEdge ਇੱਕ ਵਧੀਆ ਚੋਣ ਹੈ। ਸ਼ੁਰੂਆਤ ਕਰਨ ਲਈ ਇਸ [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) ਨੂੰ ਵੇਖੋ।

### ਐਂਡਰਾਇਡ ਫੋਨਾਂ 'ਤੇ ਇੰਸਟਾਲ ਅਤੇ ਚਲਾਉਣਾ

1. **MLC Chat ਐਪ (ਮੁਫ਼ਤ) ਡਾਊਨਲੋਡ ਕਰੋ** ਐਂਡਰਾਇਡ ਫੋਨਾਂ ਲਈ।  
2. APK ਫਾਇਲ (148MB) ਡਾਊਨਲੋਡ ਕਰਕੇ ਆਪਣੇ ਡਿਵਾਈਸ 'ਤੇ ਇੰਸਟਾਲ ਕਰੋ।  
3. MLC Chat ਐਪ ਲਾਂਚ ਕਰੋ। ਤੁਹਾਨੂੰ AI ਮਾਡਲਾਂ ਦੀ ਸੂਚੀ ਵੇਖਣ ਨੂੰ ਮਿਲੇਗੀ, ਜਿਸ ਵਿੱਚ Phi-3-mini ਵੀ ਸ਼ਾਮਲ ਹੈ।

ਸਾਰ ਵਿੱਚ, Phi-3-mini ਐਜ ਡਿਵਾਈਸਾਂ 'ਤੇ ਜਨਰੇਟਿਵ AI ਲਈ ਨਵੇਂ ਮੌਕੇ ਖੋਲ੍ਹਦਾ ਹੈ, ਅਤੇ ਤੁਸੀਂ ਇਸ ਦੀਆਂ ਖੂਬੀਆਂ ਐਂਡਰਾਇਡ 'ਤੇ ਅਨੁਭਵ ਕਰਨਾ ਸ਼ੁਰੂ ਕਰ ਸਕਦੇ ਹੋ।

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਨਾਲ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।