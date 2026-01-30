Phi-3-mini ಸಂದರ್ಭದಲ್ಲಿ, ಇನ್ಫರನ್ಸ್ ಎಂದರೆ ಮಾದರಿಯನ್ನು ಬಳಸಿ ಇನ್‌ಪುಟ್ ಡೇಟಾ ಆಧಾರವಾಗಿ ಭವಿಷ್ಯವಾಣಿ ಮಾಡುವ ಅಥವಾ ಔಟ್‌ಪುಟ್‌ಗಳನ್ನು ರಚಿಸುವ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಸೂಚಿಸುತ್ತದೆ. ನಾನು Phi-3-mini ಮತ್ತು ಅದರ ಇನ್ಫರನ್ಸ್ ಸಾಮರ್ಥ್ಯಗಳ ಬಗ್ಗೆ ನಿಮಗೆ ಹೆಚ್ಚಿನ ವಿವರಗಳನ್ನು ನೀಡುತ್ತೇನೆ.

Phi-3-mini Microsoft ಬಿಡುಗಡೆ ಮಾಡಿದ Phi-3 ಸರಣಿಯ ಮಾದರಿಗಳ ಒಂದು ಭಾಗವಾಗಿದೆ. ಈ ಮಾದರಿಗಳನ್ನು ಸಣ್ಣ ಭಾಷಾ ಮಾದರಿಗಳ (SLMs) ಮೂಲಕ ಸಾಧ್ಯವಿರುವುದನ್ನು ಮರುವ್ಯಾಖ್ಯಾನಿಸಲು ವಿನ್ಯಾಸಗೊಳಿಸಲಾಗಿದೆ. 

Here are some key points about Phi-3-mini and its inference capabilities:

## **Phi-3-mini Overview:**
- Phi-3-mini ನ ಪ್ಯಾರಾಮೀಟರ್ ಗಾತ್ರವು 3.8 ಬಿಲಿಯನ್.
- ಇದು ಪರಂಪರাগত ಗಣನಾ ಸಾಧನಗಳ ಮೇಲೆ ಮಾತ್ರವಲ್ಲದೆ ಮೊಬೈಲ್ ಸಾಧನಗಳು ಮತ್ತು IoT ಸಾಧನಗಳಂತಹ ಎಡ್ಜ್ ಸಾಧನಗಳಲ್ಲಿಯೂ ಕಾರ್ಯನಿರ್ವಹಿಸಬಹುದು.
- Phi-3-mini ಬಿಡುಗಡೆ ಮಾಡುವುದರಿಂದ ವೈಯಕ್ತಿಕರು ಮತ್ತು ಉದ್ಯಮಗಳು ವಿಭಿನ್ನ ಹಾರ್ಡ್‌ವೇರ್ ಸಾಧನಗಳಲ್ಲಿ, ವಿಶೇಷವಾಗಿ ಸಂಪನ್ಮೂಲ-ಕಡಿತ ಪರಿಸರಗಳಲ್ಲಿ SLMಗಳನ್ನು ನಿಯೋಜಿಸಲು (deploy) ಸಾಧ್ಯವಾಗುತ್ತದೆ.
- ಇದು ಪರಂಪರাগত PyTorch ಫಾರ್ಮ್ಯಾಟ್, gguf ಫಾರ್ಮ್ಯಾಟ್‌ನ ಕ್ವಾಂಟೈಸ್ ಮಾಡಿದ ಆವೃತ್ತಿ ಮತ್ತು ONNX ಆಧಾರಿತ ಕ್ವಾಂಟೈಸ್ ಆವೃತ್ತಿ ಸೇರಿದಂತೆ ವಿವಿಧ ಮಾದರಿ ಫಾರ್ಮ್ಯಾಟ್‌ಗಳನ್ನು ಒಳಗೊಂಡಿದೆ.

## **Accessing Phi-3-mini:**
To access Phi-3-mini, you can use [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) in a Copilot application. Semantic Kernel is generally compatible with Azure OpenAI Service, open-source models on Hugging Face, and local models.
You can also use [Ollama](https://ollama.com) or [LlamaEdge](https://llamaedge.com) to call quantized models. Ollama allows individual users to call different quantized models, while LlamaEdge provides cross-platform availability for GGUF models.

## **Quantized Models:**
ಬಹುतेಕ ಬಳಕೆದಾರರು ಸ್ಥಳೀಯ ಇನ್ಫರನ್ಸ್‌ಗಾಗಿ ಕ್ವಾಂಟೈಸ್ ಮಾಡಿದ ಮಾದರಿಗಳನ್ನು ಬಳಸಲು ಪ್ರಯೋಜನಗೊಳ್ಳುತ್ತಾರೆ. ಉದಾಹರಣೆಗೆ, ನೀವು ನೇರವಾಗಿ Ollama run Phi-3 ಅನ್ನು ಚಲಾಯಿಸಬಹುದು ಅಥವಾ Modelfile ಅನ್ನು ಬಳಸಿ ಅದನ್ನು ಆಫ್‌ಲೈನ್‌ನಲ್ಲಿ ಸಂರಚಿಸಬಹುದು. Modelfile ನಲ್ಲಿ GGUF ಫೈಲ್ ಪಥ ಮತ್ತು ಪ್ರಾಂಪ್ಟ್ ಫಾರ್ಮ್ಯಾಟ್ ಅನ್ನು ನಿರ್ದಿಷ್ಟಪಡಿಸಲಾಗುತ್ತದೆ.

## **Generative AI Possibilities:**
Phi-3-mini ಮತ್ತು ಇತರ SLMಗಳನ್ನು ಸಂಯೋಜಿಸುವುದು ಜನರೇಟಿವ್ AIಗೆ ಹೊಸ ಸಾಧ್ಯತೆಗಳನ್ನು ತೆರೆಯುತ್ತದೆ. ಇನ್ಫರನ್ಸ್ ಕೇವಲ ಮೊದಲನೆಯ ಹಂತವೇ; ಈ ಮಾದರಿಗಳನ್ನು ಸಂಪನ್ಮೂಲ-ಕಡಿತ, ವಿಳಂಬ-ಬಂಧಿತ ಮತ್ತು ವೆಚ್ಚ-ಕಡಿತ ಸಂದರ್ಭಗಳಲ್ಲಿ ವಿವಿಧ ಕಾರ್ಯಗಳಿಗಾಗಿ ಬಳಸಬಹುದು.

## **Unlocking Generative AI with Phi-3-mini: A Guide to Inference and Deployment** 
Semantic Kernel, Ollama/LlamaEdge, ಮತ್ತು ONNX Runtime ಅನ್ನು ಬಳಸಿಕೊಂಡು Phi-3-mini ಮಾದರಿಗಳಿಗೆ ಹೇಗೆ ಪ್ರವೇಶಿಸಿ ಇನ್ಫರನ್ಸ್ ಮಾಡುವುದು ಎಂಬುದನ್ನು ಕಲಿಯಿರಿ, ಮತ್ತು ವಿವಿಧ ಅಪ್ಲಿಕೇಶನ್ ಸಂದರ್ಭಗಳಲ್ಲಿ ಜನರೇಟಿವ್ AI ಸಾಧ್ಯತೆಗಳನ್ನು ಅನ್ವೇಷಿಸಿ.

**Features**
phi3-mini ಮಾದರಿಯಲ್ಲಿ ಇನ್ಫರನ್ಸ್:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

ಸಾರಾಂಶವಾಗಿ, Phi-3-mini ಅಭಿವೃದ್ಧಿಕರ್ತಿಗಳಿಗೆ ವಿಭಿನ್ನ ಮಾದರಿ ಫಾರ್ಮ್ಯಾಟ್‌ಗಳನ್ನು ಅನ್ವೇಷಿಸಲು ಮತ್ತು ವಿವಿಧ ಅಪ್ಲಿಕೇಶನ್ ಸಂದರ್ಭಗಳಲ್ಲಿ ಜನರೇಟಿವ್ AI ಅನ್ನು ಉಪಯೋಗಿಸಲು ಅನುಮತಿಸುತ್ತದೆ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಜವಾಬ್ದಾರಿ ನಿರಾಕರಣೆ:
ಈ ದಸ್ತಾವೇಜನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯತ್ತ ಪ್ರಯತ್ನಿಸಿದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ—ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಆಧಾರವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ನಿರ್ಣಾಯಕ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಗ್ರಹಿಕೆಗಳು ಅಥವಾ ತಪ್ಪಾಗಿ ವ್ಯಾಖ್ಯಾನವಾದ ವಿಷಯಗಳiklikಾಗಿಯೂ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->