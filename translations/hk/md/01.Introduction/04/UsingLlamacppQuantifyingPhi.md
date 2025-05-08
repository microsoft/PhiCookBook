<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-08T06:10:54+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "hk"
}
-->
# **用 llama.cpp 量化 Phi 系列**

## **咩係 llama.cpp**

llama.cpp 係一個主要用 C++ 撰寫嘅開源軟件庫，專門用嚟對各種大型語言模型（LLMs），例如 Llama，進行推理。佢嘅主要目標係喺唔同硬件上提供頂尖嘅 LLM 推理效能，同時簡化設定流程。另外，呢個庫亦有 Python 綁定，提供高階嘅文本補全 API 同埋一個兼容 OpenAI 嘅網絡伺服器。

llama.cpp 嘅核心目標係喺本地或者雲端，喺各種硬件上用最少嘅設定實現先進嘅 LLM 推理效能。

- 純 C/C++ 實現，無需任何依賴
- Apple Silicon 原生支援，透過 ARM NEON、Accelerate 同 Metal 框架優化
- 支援 x86 架構嘅 AVX、AVX2 同 AVX512
- 支援 1.5-bit、2-bit、3-bit、4-bit、5-bit、6-bit 同 8-bit 整數量化，加快推理同減少記憶體使用
- 自訂 CUDA 核心，支援 NVIDIA GPU 運行 LLM（AMD GPU 透過 HIP 支援）
- 支援 Vulkan 同 SYCL 後端
- CPU+GPU 混合推理，部分加速超出 VRAM 容量嘅大型模型

## **用 llama.cpp 量化 Phi-3.5**

Phi-3.5-Instruct 模型可以用 llama.cpp 量化，但 Phi-3.5-Vision 同 Phi-3.5-MoE 暫時未支援。llama.cpp 轉換嘅格式係 gguf，呢個格式亦係目前最廣泛使用嘅量化格式。

Hugging Face 上有大量量化咗嘅 GGUF 格式模型。AI Foundry、Ollama 同 LlamaEdge 都係用 llama.cpp，所以 GGUF 模型都好常用。

### **咩係 GGUF**

GGUF 係一種二進制格式，專為快速載入同保存模型而優化，非常適合推理使用。GGUF 係為 GGML 同其他執行器設計。GGUF 係由 @ggerganov 開發，佢亦係 llama.cpp 嘅作者，一個流行嘅 C/C++ LLM 推理框架。原本喺 PyTorch 等框架開發嘅模型，可以轉換成 GGUF 格式，用喺呢啲引擎上。

### **ONNX 同 GGUF 比較**

ONNX 係一種傳統嘅機器學習／深度學習格式，喺唔同 AI 框架有好好嘅支援，亦適合用喺邊緣設備。GGUF 基於 llama.cpp，可以話係 GenAI 時代嘅產物。兩者用途相似。如果你想喺嵌入式硬件同應用層面獲得更好效能，ONNX 可能係你嘅選擇。如果你用 llama.cpp 衍生嘅框架同技術，GGUF 會更合適。

### **用 llama.cpp 量化 Phi-3.5-Instruct**

**1. 環境設定**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. 量化**

用 llama.cpp 將 Phi-3.5-Instruct 轉成 FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

量化成 INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. 測試**

安裝 llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***注意***

如果用 Apple Silicon，請咁樣安裝 llama-cpp-python


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

測試


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **資源**

1. 深入了解 llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. 深入了解 onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. 深入了解 GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**免責聲明**：  
本文件乃使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原文文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用此翻譯而引起的任何誤解或誤釋承擔責任。