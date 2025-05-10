<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-05-09T10:43:19+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "pa"
}
-->
# **Android 'ਚ Phi-3 ਦਾ ਅਨੁਮਾਨ ਲਗਾਉਣਾ**

ਆਓ ਵੇਖੀਏ ਕਿ ਤੁਸੀਂ Android ਡਿਵਾਈਸਾਂ 'ਤੇ Phi-3-mini ਨਾਲ ਅਨੁਮਾਨ ਕਿਵੇਂ ਲਗਾ ਸਕਦੇ ਹੋ। Phi-3-mini ਮਾਈਕਰੋਸਾਫਟ ਵੱਲੋਂ ਨਵਾਂ ਮਾਡਲ ਸੀਰੀਜ਼ ਹੈ ਜੋ ਇਜ.edge ਅਤੇ IoT ਡਿਵਾਈਸਾਂ 'ਤੇ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲ (LLMs) ਨੂੰ ਡਿਪਲੋਇ ਕਰਨ ਦੀ ਸਹੂਲਤ ਦਿੰਦਾ ਹੈ।

## Semantic Kernel ਅਤੇ ਅਨੁਮਾਨ

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) ਇੱਕ ਐਪਲੀਕੇਸ਼ਨ ਫਰੇਮਵਰਕ ਹੈ ਜੋ ਤੁਹਾਨੂੰ Azure OpenAI Service, OpenAI ਮਾਡਲਾਂ ਅਤੇ ਇੱਥੋਂ ਤੱਕ ਕਿ ਲੋਕਲ ਮਾਡਲਾਂ ਨਾਲ ਕੰਪੈਟਿਬਲ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਜੇ ਤੁਸੀਂ Semantic Kernel ਨਾਲ ਨਵੇਂ ਹੋ, ਤਾਂ ਅਸੀਂ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ ਕਿ ਤੁਸੀਂ [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) ਨੂੰ ਵੇਖੋ।

### Semantic Kernel ਦੇ ਨਾਲ Phi-3-mini ਤੱਕ ਪਹੁੰਚ

ਤੁਸੀਂ ਇਸਨੂੰ Semantic Kernel ਵਿੱਚ Hugging Face Connector ਨਾਲ ਜੋੜ ਸਕਦੇ ਹੋ। ਇਸ [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) ਨੂੰ ਵੇਖੋ।

ਡਿਫੌਲਟ ਤੌਰ 'ਤੇ ਇਹ Hugging Face 'ਤੇ ਮਾਡਲ ID ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ। ਪਰ ਤੁਸੀਂ ਆਪਣੇ ਲੋਕਲ ਤਿਆਰ ਕੀਤੇ Phi-3-mini ਮਾਡਲ ਸਰਵਰ ਨਾਲ ਵੀ ਕਨੈਕਟ ਕਰ ਸਕਦੇ ਹੋ।

### Ollama ਜਾਂ LlamaEdge ਨਾਲ Quantized ਮਾਡਲਾਂ ਨੂੰ ਕਾਲ ਕਰਨਾ

ਕਈ ਯੂਜ਼ਰ ਲੋਕਲ ਤੌਰ 'ਤੇ ਮਾਡਲ ਚਲਾਉਣ ਲਈ quantized ਮਾਡਲਾਂ ਨੂੰ ਵਰਤਣਾ ਪਸੰਦ ਕਰਦੇ ਹਨ। [Ollama](https://ollama.com/) ਅਤੇ [LlamaEdge](https://llamaedge.com) ਵਿਅਕਤੀਗਤ ਯੂਜ਼ਰਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ quantized ਮਾਡਲਾਂ ਨੂੰ ਕਾਲ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ:

#### Ollama

ਤੁਸੀਂ ਸਿੱਧਾ `ollama run Phi-3` ਚਲਾ ਸਕਦੇ ਹੋ ਜਾਂ ਆਪਣੇ `.gguf` ਫਾਇਲ ਦੇ ਰਸਤੇ ਨਾਲ ਇੱਕ `Modelfile` ਬਣਾ ਕੇ ਆਫਲਾਈਨ ਵੀ ਕਨਫਿਗਰ ਕਰ ਸਕਦੇ ਹੋ।

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

ਜੇ ਤੁਸੀਂ ਕਲਾਉਡ ਅਤੇ edge ਡਿਵਾਈਸਾਂ 'ਤੇ ਇੱਕੋ ਸਮੇਂ `.gguf` ਫਾਇਲਾਂ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ LlamaEdge ਇੱਕ ਵਧੀਆ ਚੋਣ ਹੈ। ਸ਼ੁਰੂਆਤ ਲਈ ਤੁਸੀਂ ਇਸ [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) ਨੂੰ ਦੇਖ ਸਕਦੇ ਹੋ।

### Android ਫੋਨਾਂ 'ਤੇ ਇੰਸਟਾਲ ਅਤੇ ਚਲਾਉਣਾ

1. **MLC Chat ਐਪ (ਮੁਫ਼ਤ) ਡਾਊਨਲੋਡ ਕਰੋ** Android ਫੋਨਾਂ ਲਈ।  
2. APK ਫਾਇਲ (148MB) ਡਾਊਨਲੋਡ ਕਰਕੇ ਆਪਣੇ ਡਿਵਾਈਸ 'ਤੇ ਇੰਸਟਾਲ ਕਰੋ।  
3. MLC Chat ਐਪ ਲਾਂਚ ਕਰੋ। ਤੁਹਾਨੂੰ AI ਮਾਡਲਾਂ ਦੀ ਲਿਸਟ ਮਿਲੇਗੀ, ਜਿਸ ਵਿੱਚ Phi-3-mini ਵੀ ਸ਼ਾਮਿਲ ਹੈ।  

ਸਾਰ ਵਿੱਚ, Phi-3-mini edge ਡਿਵਾਈਸਾਂ 'ਤੇ ਜਨਰੇਟਿਵ AI ਲਈ ਨਵੇਂ ਮੌਕੇ ਖੋਲ੍ਹਦਾ ਹੈ, ਅਤੇ ਤੁਸੀਂ ਇਸਦੀ ਸਮਰੱਥਾ Android 'ਤੇ ਖੋਜਣਾ ਸ਼ੁਰੂ ਕਰ ਸਕਦੇ ਹੋ।

**ਇਸ ਗਲਤੀ ਦੀ ਸੂਚਨਾ**:  
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸਵੈਚਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰੱਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਉੱਪਜਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਭ੍ਰਮਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।