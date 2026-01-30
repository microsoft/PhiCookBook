# **Android ನಲ್ಲಿ Phi-3 ಇನ್ಫರೆನ್ಸ್**

ನಾವು Android ಸಾಧನಗಳಲ್ಲಿ Phi-3-mini ಬಳಸಿ ನೀವು ಹೇಗೆ ಇನ್ಫರೆನ್ಸ್ ನಡೆಸಬಹುದು ಎಂದು ನೋಡೋಣ. Phi-3-mini Microsoft ನಿಂದ ಹೊಸ ಮಾದರಿಗಳ ಸರಣಿಯಾಗಿದೆ, ಇದು ಎಡ್ಜ್ ಮತ್ತು IoT ಸಾಧನಗಳಲ್ಲಿ ದೊಡ್ಡ ಭಾಷಾ ಮಾದರಿಗಳು (LLMs) ಅನ್ನು ನಿಯೋಜಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.

## Semantic Kernel ಮತ್ತು ಇನ್ಫರೆನ್ಸ್

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) ಒಂದು ಅಪ್ಲಿಕೇಶನ್ ಫ್ರೇಮ್ವರ್ಕ್ ಆಗಿದ್ದು ಇದು Azure OpenAI Service, OpenAI ಮಾದರಿಗಳು, ಮತ್ತು ಸ್ಥಳೀಯ ಮಾದರಿಗಳೊಂದಿಗೆ ಹೊಂದಾಣಿಕೆಯಾಗುವ ಅಪ್ಲಿಕೇಶನ್ಗಳನ್ನು ರಚಿಸಲು ಅವಕಾಶ ನೀಡುತ್ತದೆ. ನೀವು Semantic Kernel ಗೆ ಹೊಸವರಾದರೆ, ನಾವು [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) ಅನ್ನು ನೋಡಿ ಎಂದು ಸಲಹೆ ನೀಡುತ್ತೇವೆ.

### Semantic Kernel ಬಳಸಿ Phi-3-mini ಪ್ರವೇಶಿಸುವುದು

ನೀವು ಅದನ್ನು Semantic Kernel ನಲ್ಲಿನ Hugging Face Connector ಜೊತೆಗೆ ಸಂಯೋಜಿಸಬಹುದು. ಇದರ ಬಗ್ಗೆ ಈ [ಉದಾಹರಣೆ ಕೋಡ್](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) ನೋಡಿ.

ಆಮೂಲಾಗ್ರವಾಗಿ, ಇದು Hugging Face上的 ಮಾದರಿ ID ಗೆ ಹೊಂದಿಕೆಯಾಗುತ್ತದೆ. ಆದಾಗ್ಯೂ, ನೀವು ಸ್ಥಳೀಯವಾಗಿ ನಿರ್ಮಿಸಲಾದ Phi-3-mini ಮಾದರಿ ಸರ್ವರ್‌ಗೂ ಸಂಪರ್ಕಿಸಬಹುದು.

### Ollama ಅಥವಾ LlamaEdge ಬಳಸಿ ಕ್ವಾಂಟೈಜ್ಡ್ ಮಾದರಿಗಳನ್ನು ಕರೆಯುವುದು

ಬಹುತೇಕ ಬಳಕೆದಾರರು ಸ್ಥಳೀಯವಾಗಿ ಮಾದರಿಗಳನ್ನು ಚಾಲನೆ ಮಾಡಲು ಕ್ವಾಂಟೈಜ್ಡ್ ಮಾದರಿಗಳನ್ನು ಬಳಸುವುದನ್ನು ಇಷ್ಟಪಡುತ್ತಾರೆ. [Ollama](https://ollama.com/) ಮತ್ತು [LlamaEdge](https://llamaedge.com) ವೈಯಕ್ತಿಕ ಬಳಕೆದಾರರಿಗೆ ವಿಭಿನ್ನ ಕ್ವಾಂಟೈಜ್ಡ್ ಮಾದರಿಗಳನ್ನು ಕರೆಯಲು ಅನುಮತಿಸುತ್ತವೆ:

#### Ollama

ನೀವು ನೇರವಾಗಿ `ollama run Phi-3` ಅನ್ನು ಚಲಾಯಿಸಬಹುದು ಅಥವಾ ನಿಮ್ಮ `.gguf` ಫೈಲ್‌ನ ಮಾರ್ಗವನ್ನು ಹೊಂದಿರುವ `Modelfile` ಅನ್ನು ಸೃಜಿಸಿ ಅದನ್ನು ಆಫ್‌ಲೈನ್‌ನಲ್ಲಿ ಸಂರಚಿಸಬಹುದು.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

ನೀವು ಕ್ಲೌಡ್ ಮತ್ತು ಎಡ್ಜ್ ಸಾಧನಗಳಲ್ಲಿ ಒಂದೇ ವೇಳೆಗೆ `.gguf` ಫೈಲ್‌ಗಳನ್ನು ಬಳಸಲು ಬಯಸಿದರೆ, LlamaEdge ಅತ್ಯುತ್ತಮ ಆಯ್ಕೆಯಾಗುತ್ತದೆ. ಪ್ರಾರಂಭಿಸಲು ಈ [ಉದಾಹರಣೆ ಕೋಡ್](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) ನೋಡಿ.

### Android ಫೋನ್‌ಗಳಲ್ಲಿ ಸ್ಥಾಪಿಸಿ ಮತ್ತು ಓಡಿಸಿ

1. **MLC Chat ಆಪ್ ಡೌನ್ಲೋಡ್ ಮಾಡಿ** (ಉಚಿತ) Android ಫೋನ್ಗಳಿಗಾಗಿ.
2. APK ಫೈಲ್ (148MB) ಅನ್ನು ಡೌನ್ಲೋಡ್ ಮಾಡಿ ಮತ್ತು ನಿಮ್ಮ ಸಾಧನದಲ್ಲಿ ಸ್ಥಾಪಿಸಿ.
3. MLC Chat ಆಪ್ ಪ್ರಾರಂಭಿಸಿ. ನೀವು Phi-3-mini ಸೇರಿಸಿ AI ಮಾದರಿಗಳ ಪಟ್ಟಿಯನ್ನು ಕಾಣುತ್ತೀರಿ.

ಸಾರಾಂಶವಾಗಿ, Phi-3-mini ಎಡ್ಜ್ ಸಾಧನಗಳ ಮೇಲೆ ಜನರೇಟಿವ್ AI ಗೆ ರೋಚಕ ಸಾಧ್ಯತೆಗಳನ್ನು ತೆರೆಯುತ್ತದೆ, ಮತ್ತು ನೀವು ಅದರ ಸಾಮರ್ಥ್ಯವನ್ನು Android ಮೇಲೆ ಅನ್ವೇಷಿಸಲು ಪ್ರಾರಂಭಿಸಬಹುದು.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ನಿರಾಕರಣೆ:
ಈ ದಾಖಲೆ AI ಭಾಷಾಂತರ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಭಾಷಾಂತರಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಗೆ ಪ್ರಯತ್ನಿಸಿದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ ಸ್ವಯಂಚಾಲಿತ ಭಾಷಾಂತರಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅನಿಖರತೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ಪರಿಶುದ್ಧ ದಾಖಲೆನ್ನು ಅಧಿಕಾರಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಭಾಷಾಂತರವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಭಾಷಾಂತರವನ್ನು ಬಳಕೆಮಾಡುವುದರಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗೊಳ್ಳಿಕೆಗಳು ಅಥವಾ ವ್ಯಾಖ್ಯಾನದ ದೋಷಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->