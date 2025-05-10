<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-09T12:22:46+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "pa"
}
-->
Phi-3-mini ਦੇ ਸੰਦਰਭ ਵਿੱਚ, inference ਦਾ ਮਤਲਬ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਨਪੁੱਟ ਡਾਟਾ ਦੇ ਆਧਾਰ 'ਤੇ ਅਨੁਮਾਨ ਲਗਾਉਣ ਜਾਂ ਨਤੀਜੇ ਬਣਾਉਣ ਦੀ ਪ੍ਰਕਿਰਿਆ ਹੈ। ਆਓ ਮੈਂ ਤੁਹਾਨੂੰ Phi-3-mini ਅਤੇ ਇਸ ਦੀ inference ਸਮਰੱਥਾ ਬਾਰੇ ਹੋਰ ਵੇਰਵੇ ਦਿੰਦਾ ਹਾਂ।

Phi-3-mini Microsoft ਵੱਲੋਂ ਜਾਰੀ ਕੀਤੇ ਗਏ Phi-3 ਸੀਰੀਜ਼ ਦੇ ਮਾਡਲਾਂ ਦਾ ਹਿੱਸਾ ਹੈ। ਇਹ ਮਾਡਲ ਛੋਟੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ (SLMs) ਦੀ ਸੰਭਾਵਨਾਵਾਂ ਨੂੰ ਨਵੀਂ ਪਰਿਭਾਸ਼ਾ ਦੇਣ ਲਈ ਬਣਾਏ ਗਏ ਹਨ।

ਇੱਥੇ Phi-3-mini ਅਤੇ ਇਸ ਦੀ inference ਸਮਰੱਥਾ ਬਾਰੇ ਕੁਝ ਮੁੱਖ ਗੱਲਾਂ ਹਨ:

## **Phi-3-mini ਦਾ ਜਾਇਜ਼ਾ:**
- Phi-3-mini ਦਾ ਪੈਰਾਮੀਟਰ ਆਕਾਰ 3.8 ਬਿਲੀਅਨ ਹੈ।
- ਇਹ ਸਿਰਫ ਪਰੰਪਰਾਗਤ ਕੰਪਿਊਟਿੰਗ ਡਿਵਾਈਸਾਂ 'ਤੇ ਹੀ ਨਹੀਂ, ਬਲਕਿ ਮੋਬਾਈਲ ਅਤੇ IoT ਜਿਹੇ edge ਡਿਵਾਈਸਾਂ 'ਤੇ ਵੀ ਚੱਲ ਸਕਦਾ ਹੈ।
- Phi-3-mini ਦੇ ਜਾਰੀ ਹੋਣ ਨਾਲ ਵਿਅਕਤੀਗਤ ਅਤੇ ਕਾਰੋਬਾਰੀ ਦੋਹਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਡਿਵਾਈਸਾਂ 'ਤੇ SLMs ਨੂੰ ਤਾਇਨਾਤ ਕਰਨ ਦੀ ਸਹੂਲਤ ਮਿਲੀ ਹੈ, ਖ਼ਾਸ ਕਰਕੇ ਜਿੱਥੇ ਸਰੋਤ ਸੀਮਿਤ ਹਨ।
- ਇਹ ਵੱਖ-ਵੱਖ ਮਾਡਲ ਫਾਰਮੈਟਾਂ ਨੂੰ ਕਵਰ ਕਰਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਪਰੰਪਰਾਗਤ PyTorch ਫਾਰਮੈਟ, gguf ਫਾਰਮੈਟ ਦਾ quantized ਵਰਜਨ, ਅਤੇ ONNX ਅਧਾਰਿਤ quantized ਵਰਜਨ।

## **Phi-3-mini ਤੱਕ ਪਹੁੰਚ:**
Phi-3-mini ਤੱਕ ਪਹੁੰਚ ਲਈ, ਤੁਸੀਂ Copilot ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ। Semantic Kernel ਆਮ ਤੌਰ 'ਤੇ Azure OpenAI Service, Hugging Face ਤੇ ਖੁੱਲ੍ਹੇ ਸ੍ਰੋਤ ਮਾਡਲਾਂ ਅਤੇ ਲੋਕਲ ਮਾਡਲਾਂ ਨਾਲ ਸੰਗਤ ਹੈ।  
ਤੁਸੀਂ quantized ਮਾਡਲਾਂ ਨੂੰ ਕਾਲ ਕਰਨ ਲਈ [Ollama](https://ollama.com) ਜਾਂ [LlamaEdge](https://llamaedge.com) ਦੀ ਵੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ। Ollama ਵਿਅਕਤੀਗਤ ਯੂਜ਼ਰਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ quantized ਮਾਡਲਾਂ ਨੂੰ ਕਾਲ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ, ਜਦਕਿ LlamaEdge GGUF ਮਾਡਲਾਂ ਲਈ ਕ੍ਰਾਸ-ਪਲੇਟਫਾਰਮ ਉਪਲਬਧਤਾ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

## **Quantized ਮਾਡਲ:**
ਬਹੁਤ ਸਾਰੇ ਯੂਜ਼ਰ ਲੋਕਲ inference ਲਈ quantized ਮਾਡਲਾਂ ਦੀ ਪਸੰਦ ਕਰਦੇ ਹਨ। ਉਦਾਹਰਨ ਵਜੋਂ, ਤੁਸੀਂ ਸਿੱਧਾ Ollama 'ਚ Phi-3 ਚਲਾ ਸਕਦੇ ਹੋ ਜਾਂ Modelfile ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਫਲਾਈਨ ਕਨਫਿਗਰ ਕਰ ਸਕਦੇ ਹੋ। Modelfile ਵਿੱਚ GGUF ਫਾਈਲ ਪਾਥ ਅਤੇ prompt ਫਾਰਮੈਟ ਦਰਸਾਇਆ ਜਾਂਦਾ ਹੈ।

## **Generative AI ਦੀਆਂ ਸੰਭਾਵਨਾਵਾਂ:**
Phi-3-mini ਵਰਗੇ SLMs ਨੂੰ ਮਿਲਾ ਕੇ generative AI ਲਈ ਨਵੀਆਂ ਸੰਭਾਵਨਾਵਾਂ ਖੁਲਦੀਆਂ ਹਨ। Inference ਸਿਰਫ ਪਹਿਲਾ ਕਦਮ ਹੈ; ਇਹ ਮਾਡਲ ਸਰੋਤ ਸੀਮਿਤ, ਲੈਟੈਂਸੀ ਬਾਊਂਡ ਅਤੇ ਖ਼ਰਚਾ ਸੀਮਿਤ ਹਾਲਾਤਾਂ ਵਿੱਚ ਵੱਖ-ਵੱਖ ਕੰਮਾਂ ਲਈ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ।

## **Phi-3-mini ਨਾਲ Generative AI ਖੋਲ੍ਹਣਾ: Inference ਅਤੇ ਤਾਇਨਾਤੀ ਲਈ ਇੱਕ ਗਾਈਡ**  
ਸਿੱਖੋ ਕਿ ਕਿਵੇਂ Semantic Kernel, Ollama/LlamaEdge, ਅਤੇ ONNX Runtime ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3-mini ਮਾਡਲਾਂ ਤੱਕ ਪਹੁੰਚ ਅਤੇ inference ਕਰਨੀ ਹੈ, ਅਤੇ ਵੱਖ-ਵੱਖ ਐਪਲੀਕੇਸ਼ਨ ਸਿਨਾਰਿਓਜ਼ ਵਿੱਚ generative AI ਦੀਆਂ ਸੰਭਾਵਨਾਵਾਂ ਦਾ ਪਤਾ ਲਗਾਓ।

**ਖਾਸੀਅਤਾਂ**  
Phi3-mini ਮਾਡਲ ਦੀ inference:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

ਸੰਖੇਪ ਵਿੱਚ, Phi-3-mini ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ ਮਾਡਲ ਫਾਰਮੈਟਾਂ ਦੀ ਖੋਜ ਕਰਨ ਅਤੇ ਵੱਖ-ਵੱਖ ਐਪਲੀਕੇਸ਼ਨ ਸਿਨਾਰਿਓਜ਼ ਵਿੱਚ generative AI ਦਾ ਲਾਭ ਉਠਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਨਾਲ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਪਸ਼ਟਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜ਼ਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਇਸਤੇਮਾਲ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਭ੍ਰਮਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।