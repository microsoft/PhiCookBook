<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2a7aaeb42235207ba74581473b305581",
  "translation_date": "2025-04-04T17:58:58+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingLlamacppQuantifyingPhi.md",
  "language_code": "hk"
}
-->
# **使用 llama.cpp 量化 Phi 家族**

## **什麼是 llama.cpp**

llama.cpp 是一個主要用 C++ 編寫的開源軟件庫，能夠對多種大型語言模型（LLMs）進行推理，例如 Llama。它的主要目標是提供最先進的 LLM 推理性能，適用於多種硬件並且只需最少的設置。此外，該庫還提供了 Python 綁定，提供用於文本補全的高級 API，以及一個兼容 OpenAI 的網絡服務器。

llama.cpp 的主要目標是實現最少設置、最先進性能的 LLM 推理，並支持多種硬件，無論是本地還是雲端。

- 純 C/C++ 實現，無需任何依賴
- Apple Silicon 是一級支持，通過 ARM NEON、Accelerate 和 Metal 框架進行優化
- 支持 x86 架構的 AVX、AVX2 和 AVX512
- 提供 1.5-bit、2-bit、3-bit、4-bit、5-bit、6-bit 和 8-bit 整數量化，提升推理速度並減少內存使用
- 定制 CUDA 核心，用於在 NVIDIA GPU 上運行 LLM（支持 AMD GPU 通過 HIP）
- 支持 Vulkan 和 SYCL 後端
- CPU+GPU 混合推理，能部分加速超過 VRAM 容量的模型

## **使用 llama.cpp 量化 Phi-3.5**

Phi-3.5-Instruct 模型可以使用 llama.cpp 進行量化，但目前 Phi-3.5-Vision 和 Phi-3.5-MoE 尚不支持。llama.cpp 轉換的格式是 GGUF，也是目前最廣泛使用的量化格式。

在 Hugging Face 上有大量使用 GGUF 格式量化的模型。AI Foundry、Ollama 和 LlamaEdge 都依賴於 llama.cpp，因此 GGUF 模型也被廣泛使用。

### **什麼是 GGUF**

GGUF 是一種二進制格式，專為快速加載和保存模型而優化，非常適合推理使用。GGUF 是為 GGML 和其他執行器設計的。GGUF 是由 @ggerganov 開發的，他同時也是 llama.cpp 的開發者，一個受歡迎的 C/C++ LLM 推理框架。最初在 PyTorch 等框架中開發的模型可以轉換為 GGUF 格式，以便在這些引擎中使用。

### **ONNX vs GGUF**

ONNX 是一種傳統的機器學習/深度學習格式，在不同的 AI 框架中有良好的支持，並在邊緣設備中有不錯的使用場景。而 GGUF 則基於 llama.cpp，可以說是在生成式 AI 時代誕生的。兩者用途相似。如果您希望在嵌入式硬件和應用層中獲得更好的性能，ONNX 可能是您的選擇。如果您使用 llama.cpp 的衍生框架和技術，那麼 GGUF 可能會更好。

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

如果您使用 Apple Silicon，請按照以下方式安裝 llama-cpp-python


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

測試 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **資源**

1. 瞭解更多有關 llama.cpp 的信息 [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. 瞭解更多有關 GGUF 的信息 [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**免責聲明**:  
此文件使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。