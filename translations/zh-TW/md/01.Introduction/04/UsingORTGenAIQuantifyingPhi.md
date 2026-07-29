# **使用 onnxruntime 的生成式 AI 擴充功能進行 Phi 系列量化**

## **什麼是 onnxruntime 的生成式 AI 擴充功能**

此擴充功能可幫助您使用 ONNX Runtime 運行生成式 AI（[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)）。它為 ONNX 模型提供生成式 AI 迴圈，包括使用 ONNX Runtime 進行推斷、logits 處理、搜尋與采樣以及 KV 緩存管理。開發者可呼叫高階的 generate() 方法，或在迴圈中逐次執行模型，每次生成一個 token，並可選擇在迴圈內更新生成參數。支持貪心/束搜索和 TopP、TopK 采樣生成 token 序列，還內建了如重複懲罰的 logits 處理。您也能輕鬆添加自訂評分。

在應用層級，您可以使用 onnxruntime 的生成式 AI 擴充功能，採用 C++ / C# / Python 建立應用程式。在模型層級，您可以用它來合併微調模型並進行相關量化部署工作。


## **使用 onnxruntime 的生成式 AI 擴充功能對 Phi-3.5 量化**

### <strong>支持的模型</strong>

onnxruntime 的生成式 AI 擴充功能支持 Microsoft Phi、Google Gemma、Mistral、Meta LLaMA 的量化轉換。


### **onnxruntime 生成式 AI 擴充功能中的模型建立工具**

模型建立工具大幅加速建立經過優化且量化的 ONNX 模型，這些模型可搭配 ONNX Runtime 的 generate() API 執行。

透過模型建立工具，您可以將模型量化為 INT4、INT8、FP16、FP32，並結合不同硬體加速方式如 CPU、CUDA、DirectML、Mobile 等。

使用模型建立工具前，您需要安裝

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

安裝後，您可以從終端機執行模型建立工具腳本，進行模型格式與量化轉換。


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

了解相關參數

1. **model_name** 這是 Hugging Face 上的模型，例如 microsoft/Phi-3.5-mini-instruct、microsoft/Phi-3.5-vision-instruct 等。也可以是您儲存模型的路徑

2. **path_to_output_folder** 量化轉換的儲存路徑

3. **execution_provider** 不同的硬體加速支持，如 cpu、cuda、DirectML

4. **cache_dir_to_save_hf_files** 我們從 Hugging Face 下載模型並在本地快取




***注意：*** <ul>雖然 onnxruntime 的生成式 AI 擴充功能仍屬預覽版，但已納入 Microsoft Olive，您也可以透過 Microsoft Olive 呼叫生成式 AI 擴充功能的模型建立工具功能。</ul>

## **如何使用模型建立工具量化 Phi-3.5**

模型建立工具目前支持 Phi-3.5 Instruct 和 Phi-3.5-Vision 的 ONNX 模型量化

### **Phi-3.5-Instruct**


**CPU 加速的 INT4 量化轉換**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA 加速的 INT4 量化轉換**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. 在終端機設定環境

```bash

mkdir models

cd models 

```

2. 在 models 資料夾下載 microsoft/Phi-3.5-vision-instruct
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. 請將這些檔案下載到您的 Phi-3.5-vision-instruct 資料夾

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. 將此檔案下載到 models 資料夾
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. 切換到終端機

    轉換支援 FP32 的 ONNX


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **注意：**

1. 模型建立工具目前支援 Phi-3.5-Instruct 和 Phi-3.5-Vision 的轉換，但不支援 Phi-3.5-MoE

2. 若要使用 ONNX 的量化模型，可透過 onnxruntime 的生成式 AI 擴充功能 SDK 使用

3. 我們需要更謹慎考慮負責任的 AI，因此量化轉換後，建議做更有效的結果測試

4. 透過量化 CPU INT4 模型，能部署到 Edge 裝置，擁有更好的應用場景，因此我們已完成 Phi-3.5-Instruct 的 INT4 量化


## <strong>資源</strong>

1. 瞭解更多 onnxruntime 的生成式 AI 擴充功能 [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. onnxruntime 的生成式 AI 擴充功能 GitHub 倉庫 [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->