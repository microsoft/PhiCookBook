<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2a7aaeb42235207ba74581473b305581",
  "translation_date": "2025-04-04T06:08:06+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingLlamacppQuantifyingPhi.md",
  "language_code": "tw"
}
-->
# **使用 llama.cpp 量化 Phi 系列模型**

## **什麼是 llama.cpp**

llama.cpp 是一個主要使用 C++ 編寫的開源軟體庫，用於對多種大型語言模型 (LLMs) 進行推論，例如 Llama。它的主要目標是提供在各種硬體上進行 LLM 推論的最先進效能，且僅需最少的設定。此外，該庫還提供 Python 綁定，提供高階 API 用於文本生成以及一個兼容 OpenAI 的網頁伺服器。

llama.cpp 的主要目標是以最少的設定和最先進的效能，實現本地和雲端上的多種硬體 LLM 推論。

- 純 C/C++ 實現，無需依賴其他庫
- 對 Apple Silicon 提供一流支持 - 通過 ARM NEON、Accelerate 和 Metal 框架進行優化
- 支持 x86 架構的 AVX、AVX2 和 AVX512
- 支持 1.5-bit、2-bit、3-bit、4-bit、5-bit、6-bit 和 8-bit 整數量化，以加速推論並減少記憶體使用
- 自訂 CUDA 核心，用於在 NVIDIA GPU 上運行 LLM（支持 AMD GPU 通過 HIP）
- 支持 Vulkan 和 SYCL 後端
- CPU+GPU 混合推論，可加速超過 VRAM 容量的大型模型

## **使用 llama.cpp 量化 Phi-3.5**

Phi-3.5-Instruct 模型可以使用 llama.cpp 進行量化，但目前不支持 Phi-3.5-Vision 和 Phi-3.5-MoE。llama.cpp 轉換的格式是 gguf，這也是目前最廣泛使用的量化格式。

在 Hugging Face 上有大量使用 GGUF 格式量化的模型。AI Foundry、Ollama 和 LlamaEdge 都依賴於 llama.cpp，因此 GGUF 模型也經常被使用。

### **什麼是 GGUF**

GGUF 是一種二進制格式，經過優化以快速載入和保存模型，非常適合推論用途。GGUF 專為 GGML 和其他執行器設計。GGUF 是由 @ggerganov 開發的，他也是流行的 C/C++ LLM 推論框架 llama.cpp 的開發者。最初在 PyTorch 等框架中開發的模型可以轉換為 GGUF 格式，以便與這些引擎一起使用。

### **ONNX vs GGUF**

ONNX 是一種傳統的機器學習/深度學習格式，在不同的 AI 框架中具有良好的支持，並且在邊緣設備中有良好的使用場景。至於 GGUF，它基於 llama.cpp，可以說是在生成式 AI 時代誕生的。兩者的用途相似。如果您希望在嵌入式硬體和應用層中獲得更好的效能，ONNX 可能是您的選擇。如果您使用 llama.cpp 的衍生框架和技術，那麼 GGUF 可能更適合。

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

量化 Phi-3.5 為 INT4

```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```

**3. 測試**

安裝 llama-cpp-python

```bash

pip install llama-cpp-python -U

```

***注意***  

如果您使用 Apple Silicon，請按照以下方式安裝 llama-cpp-python

```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

測試

```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```

## **資源**

1. 了解更多有關 llama.cpp 的資訊 [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. 了解更多有關 GGUF 的資訊 [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**免責聲明**：  
本文檔使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，機器翻譯可能會包含錯誤或不精確之處。原始語言的文件應被視為具有權威性的來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀不承擔責任。