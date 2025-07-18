<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-07-16T22:06:42+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "mo"
}
-->
# **使用 llama.cpp 量化 Phi 系列**

## **什麼是 llama.cpp**

llama.cpp 是一個主要以 C++ 編寫的開源軟體庫，能對多種大型語言模型（LLM）進行推理，例如 Llama。它的主要目標是在各種硬體上以最少的設定提供先進的 LLM 推理效能。此外，該庫還提供 Python 綁定，提供高階的文字補全 API 以及與 OpenAI 相容的網頁伺服器。

llama.cpp 的核心目標是讓 LLM 推理能在本地和雲端的多種硬體上，以最少設定達到頂尖效能。

- 純 C/C++ 實作，無任何依賴
- Apple Silicon 為重點優化對象，透過 ARM NEON、Accelerate 和 Metal 框架加速
- 支援 x86 架構的 AVX、AVX2 和 AVX512
- 支援 1.5-bit、2-bit、3-bit、4-bit、5-bit、6-bit 及 8-bit 整數量化，加快推理並減少記憶體使用
- 自訂 CUDA 核心用於 NVIDIA GPU 執行 LLM（透過 HIP 支援 AMD GPU）
- 支援 Vulkan 和 SYCL 後端
- CPU+GPU 混合推理，可部分加速超出 VRAM 容量的模型

## **使用 llama.cpp 量化 Phi-3.5**

Phi-3.5-Instruct 模型可以使用 llama.cpp 進行量化，但 Phi-3.5-Vision 和 Phi-3.5-MoE 尚未支援。llama.cpp 轉換的格式為 gguf，這也是目前最廣泛使用的量化格式。

Hugging Face 上有大量量化的 GGUF 格式模型。AI Foundry、Ollama 和 LlamaEdge 都依賴 llama.cpp，因此 GGUF 模型也經常被使用。

### **什麼是 GGUF**

GGUF 是一種二進位格式，優化了模型的快速載入與儲存，使其在推理時非常高效。GGUF 設計用於 GGML 及其他執行器。GGUF 由 @ggerganov 開發，他同時也是 llama.cpp 的開發者，llama.cpp 是一個流行的 C/C++ LLM 推理框架。最初在 PyTorch 等框架開發的模型，可以轉換成 GGUF 格式以供這些引擎使用。

### **ONNX 與 GGUF 的比較**

ONNX 是傳統的機器學習／深度學習格式，在多種 AI 框架中有良好支援，且在邊緣裝置上有不錯的應用場景。GGUF 則基於 llama.cpp，可以說是生成式 AI 時代的產物。兩者用途相似。如果你想在嵌入式硬體和應用層獲得更佳效能，ONNX 可能是你的選擇；若你使用 llama.cpp 的衍生框架和技術，GGUF 可能更適合。

### **使用 llama.cpp 量化 Phi-3.5-Instruct**

**1. 環境配置**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. 量化**

使用 llama.cpp 將 Phi-3.5-Instruct 轉換為 FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

將 Phi-3.5 量化為 INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. 測試**

安裝 llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***注意***

如果你使用 Apple Silicon，請用以下方式安裝 llama-cpp-python


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

測試


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **資源**

1. 進一步了解 llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. 進一步了解 onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. 進一步了解 GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。