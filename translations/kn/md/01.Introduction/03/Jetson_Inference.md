<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be4101a30d98e95a71d42c276e8bcd37",
  "translation_date": "2025-12-22T01:09:34+00:00",
  "source_file": "md/01.Introduction/03/Jetson_Inference.md",
  "language_code": "kn"
}
-->
# **Nvidia Jetson ನಲ್ಲಿ Phi-3 ಇನ್ಫರೆನ್ಸ್**

Nvidia Jetson ialah Nvidia ನಿಂದ ಬಂದ ಎम्बೆಡ್ಡೆಡ್ ಕಂಪ್ಯೂಟಿಂಗ್ ಬೋರ್ಡ್ಸ್ ಸರಣಿ. Jetson TK1, TX1 ಮತ್ತು TX2 ಮಾದರಿಗಳು ಎಲ್ಲವೂ Nvidia ನ Tegra ಪ್ರೋಸೆಸರ್ (ಅಥವಾ SoC) ಅನ್ನು ಹೊಂದಿವೆ, ಇದು ARM ವಾಸ್ತುಶಿಲ್ಪದ ಸೆಂಟ್ರಲ್ ಪ್ರೊಸೆಸಿಂಗ್ ಯುನಿಟ್ (CPU) ಅನ್ನು ಏಕೀಕರಿಸುತ್ತದೆ. Jetson ಕಡಿಮೆ ಶಕ್ತಿ ಬಳಕೆಯ ವ್ಯವಸ್ಥೆಯಾಗಿದ್ದು ಯಂತ್ರಶಿಕ್ಷಣ ಅನ್ವಯಗಳನ್ನು ವೇಗವರ್ಧಿಸಲು ವಿನ್ಯಾಸಗೊಳಿಸಲಾಗಿದೆ. Nvidia Jetson ವೃತ್ತಿಪರ ಡೆವಲಪರ್ ಗಾಗಿ ಎಲ್ಲಾ ಉದ್ಯಮಗಳಲ್ಲಿ ಮುಂಚೂಣಿಯ AI ಉತ್ಪನ್ನಗಳನ್ನು ರಚಿಸಲು ಮತ್ತು ವಿದ್ಯಾರ್ಥಿಗಳು ಹಾಗೂ ಔತ್ಸಾಹಿಕರು ಕೈಹಾಕಿ AI ಕಲಿಕೆಗೆ ಮತ್ತು ಅದ್ಭುತ ಪ್ರોજೆಕ್ಟುಗಳನ್ನು ನಿರ್ಮಿಸಲು ಬಳಸುತ್ತಾರೆ. SLM ಅನ್ನು Jetson ಹೀಗೆ ಎಡ್ಜ್ ಸಾಧನಗಳಲ್ಲಿ ನಿಯೋಜಿಸಲಾಗುತ್ತದೆ, ಇದು ಕೈಗಾರಿಕಾ ಜನರೇಟಿವ್ AI ಅನ್ವಯ ದೃಶ್ಯಾವಳಿಗಳನ್ನು ಉತ್ತಮವಾಗಿ ಅನುಷ್ಠಾನಗೊಳಿಸಲು ಸಾಧ್ಯವಾಗಿಸುತ್ತದೆ.

## NVIDIA Jetsonನಲ್ಲಿ ನಿಯೋಜನೆ:
ಸ್ವಯಂಚಾಲಿತ ರೋಬೋಟಿಕ್ಸ್ ಮತ್ತು ಎಂಬೆಡ್ಡೆಡ್ ಸಾಧನಗಳ ಮೇಲೆ ಕೆಲಸ ಮಾಡುವ ಡೆವಲಪರ್ ಗಳು Phi-3 Mini ಅನ್ನು ಬಳಸಬಹುದು. Phi-3 の relativement ಸಣ್ಣ ಗಾತ್ರ ಎಡ್ಜ್ ನಿಯೋಜನೆಗೆ ಅನುಕೂಲವಾಗಿದೆ. ತರಬೇತಿ ಸಮಯದಲ್ಲಿ ಪ್ಯಾರಾಮೀಟರ್ ಗಳನ್ನು ತಕ್ಷಣ ಸೌಕ್ಷ್ಮವಾಗಿ ಟ್ಯೂನು ಮಾಡಲಾಗಿದೆ, ಇದರಿಂದ ಉತ್ತರಗಳಲ್ಲಿ ಉನ್ನತ ನಿಖರತೆ ಖಚಿತವಾಗುತ್ತದೆ.

### TensorRT-LLM ಆಪ್ಟಿಮೈಜೆಷನ್:
NVIDIA ರ [TensorRT-LLM library](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) ದೊಡ್ಡ ಭಾಷಾ ಮಾದರಿ ಇನ್ಫರೆನ್ಸ್ ಅನ್ನು ಆಪ್ಟಿಮೈಸ್ ಮಾಡುತ್ತದೆ. ಇದು Phi-3 Mini ಯ ದೀರ್ಘ context window ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ,Throughput ಮತ್ತು latency ಎರಡನ್ನೂ ಸುಧಾರಿಸುತ್ತದೆ. ಆಪ್ಟಿಮೈಜೇಶನ್ ಗಳಲ್ಲಿ LongRoPE, FP8 ಮತ್ತು inflight batching వంటి ತಂತ್ರಗಳನ್ನು ಸೇರಿಸಲಾಗಿದೆ.

### ಲಭ್ಯತೆ ಮತ್ತು ನಿಯೋಜನೆ:
ಡೆವಲಪರ್ ಗಳು 128K context window ಹೊಂದಿರುವ Phi-3 Mini ಅನ್ನು [NVIDIA's AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/) ನಲ್ಲಿ ಅನ್ವೇಷಿಸಬಹುದು. ಇದನ್ನು NVIDIA NIM ಆಗಿ ಪ್ಯಾಕೇಜ್ ಮಾಡಲಾಗಿದೆ, ಇದು ಯಾವುದೇ ಕಡೆ ನಿಯೋಜಿಸಬಹುದಾದ ಸ್ಟ್ಯಾಂಡರ್ಡ್ API ಇರುವ ಮೈಕ್ರೋಸರ್ವಿಸ್ ಆಗಿದೆ. ತಕರಾರು ಮಾತ್ರವಲ್ಲದೆ, [TensorRT-LLM implementations on GitHub](https://github.com/NVIDIA/TensorRT-LLM) ನಲ್ಲಿ ಕೂಡ ಲಭ್ಯವಿದೆ.


 ## **1. ತಯಾರಿ**


a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+
   
c. Cuda 11.8
   
d. Python 3.8+

 ## **2. Jetson ನಲ್ಲಿ Phi-3 ಅನ್ನು ಓಡಿಸುವುದು**

ನಾವು [Ollama](https://ollama.com) ಅಥವಾ [LlamaEdge](https://llamaedge.com) ಅನ್ನು ಆಯ್ಕೆ ಮಾಡಬಹುದು

ನೀವು ಸಮಕಾಲೀನವಾಗಿ ಕ್ಲೌಡ್ ಮತ್ತು ಎಡ್ಜ್ ಸಾಧನಗಳಲ್ಲಿ gguf ಬಳಸಲು ಬಯಸಿದರೆ, LlamaEdge ಅನ್ನು WasmEdge ಆಗಿ ಅರ್ಥಮಾಡಿಕೊಳ್ಳಬಹುದು (WasmEdge ಒಂದು ತೂಕ ತಗ್ಗಿದ, ಉನ್ನತ ಕಾರ್ಯಕ್ಷಮತೆಗಿರುವ, ಸ್ಕೇಲಬಲ್ WebAssembly ರೈಂಟೈಮ್ ಆಗಿದ್ದು ಕ್ಲೌಡ್ ನೆಟಿವ್, ಎಡ್ಜ್ ಮತ್ತು ಹಿಂದಿನಹೊಂದಾಣಿಕೆಯ ಅಪ್ಲಿಕೇಶನ್ ಗಳಿಗೆ ಸೂಕ್ತವಾಗಿದೆ. ಇದು ಸರ್ವರ್‍ಲೆಸ್ ಅಪ್ಲಿಕೇಶನ್ಗಳು, ಎम्बೆಡ್ಡೆಡ್ ಫಂಕ್ಷನ್ಗಳು, ಮೈಕ್ರೋಸರ್ವೀಸ್ಗಳು, ಸ್ಮಾರ್ಟ್ ಕಾನ್ಟ್ರಾಕ್ಟ್ ಗಳು ಮತ್ತು IoT ಸಾಧನಗಳನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ. ನೀವು gguf ಯ количеitative ಮಾದರಿಯನ್ನು LlamaEdge ಮೂಲಕ ಎಡ್ಜ್ ಸಾಧನಗಳು ಮತ್ತು ಕ್ಲೌಡ್ ಗೆ ನಿಯೋಜಿಸಬಹುದು.)

![llamaedge](../../../../../translated_images/llamaedge.e9d6ff96dff11cf729d0c895601ffb284d46998dd44022f5a3ebd3745c91e7db.kn.jpg)

ಇದು ಬಳಸಲು ಹಂತಗಳು ಹೀಗೆ:

1. ಸಂಬಂಧಿತ ಲೈಬ್ರರಿ ಗಳು ಮತ್ತು ಫೈಲ್ ಗಳನ್ನು ಇನ್ಸ್ಟಾಲ್ ಮತ್ತು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿರಿ

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**ಗಮನಿಸಿ**: llama-api-server.wasm ಮತ್ತು chatbot-ui ಗೊಂದ ۾ ಒಂದೇ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ ಇರಬೇಕು

2. ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಸ್ಕ್ರಿಪ್ಟ್ ಗಳನ್ನು ರನ್ ಮಾಡಿ


```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

ಇದು ರನ್ ಮಾಡಿದ ಫಲಿತಾಂಶವಾಗಿದೆ


![llamaedgerun](../../../../../translated_images/llamaedgerun.bed921516c9a821cf23486eee46e18241c442f862976040c2681b36b905125a6.kn.png)

***ಸ್ಯಾಂಪಲ್ ಕೋಡ್*** [Phi-3 mini WASM ನೋಟ್‌ಬುಕ್ ಉದಾಹರಣೆ](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

ಸಂಗ್ರಹವಾಗಿ, Phi-3 Mini ಭಾಷಾ ಮಾದರಿಯಲ್ಲಿ ಒಂದು ಪ್ರಗತಿಯನ್ನು ಪ್ರತಿನಿಧಿಸುತ್ತದೆ, ಇದು ಕಾರ್ಯಕ್ಷಮತೆ,context ಅರಿವು ಮತ್ತು NVIDIA ಯ ಆಪ್ಟಿಮೈಸೇಷನ್ ಸಾಮರ್ಥ್ಯವನ್ನು ಒಟ್ಟುಗೂಡಿಸುತ್ತದೆ. ನೀವು ರೋಬೋಟ್ಸ್ ಅಥವಾ ಎಡ್ಜ್ ಅನ್ವಯಗಳನ್ನು ನಿರ್ಮಿಸುತ್ತಿದ್ದೀರಾ ಎಂಬುದರ ಕುರಿತು, Phi-3 Mini ಒಂದು ಗಮನಾರ್ಹ ಮತ್ತು ಶಕ್ತಿಶಾಲಿ ಸಾಧನವಾಗಿದೆ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ನಿರಾಕರಣೆ:
ಈ ದಾಖಲೆ AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಗೆ ಪ್ರಯತ್ನಿಸಿದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಮರ್ಪಕತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿನ ಮೂಲದಾಖಲೆ ಇದನ್ನೇ ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಗಂಭೀರ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೆಗಳು ಅಥವಾ ದುರವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಜವಾಬ್ದಾರಿಯಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->