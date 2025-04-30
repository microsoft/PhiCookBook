<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b96f9dc2389500e24a2c2c4debf30908",
  "translation_date": "2025-04-04T06:09:08+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingORTGenAIQuantifyingPhi.md",
  "language_code": "tw"
}
-->
# **使用 Generative AI extensions for onnxruntime 量化 Phi 家族**

## **什麼是 Generative AI extensions for onnxruntime**

此擴展幫助您使用 ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) 運行生成式 AI。它為 ONNX 模型提供生成式 AI 迴圈，包括使用 ONNX Runtime 推理、logits 處理、搜索與採樣以及 KV 緩存管理。開發者可以調用高級的 generate() 方法，也可以在迴圈中逐步運行模型的每次迭代，一次生成一個 token，並可選擇在迴圈中更新生成參數。它支持貪婪/束搜索以及 TopP、TopK 採樣生成 token 序列，並內置 logits 處理，例如重複懲罰。您還可以輕鬆添加自定義評分。

在應用層面，您可以使用 Generative AI extensions for onnxruntime 用 C++/C#/Python 構建應用程序。在模型層面，您可以用它來合併微調模型並進行相關的量化部署工作。

## **使用 Generative AI extensions for onnxruntime 量化 Phi-3.5**

### **支持的模型**

Generative AI extensions for onnxruntime 支持 Microsoft Phi、Google Gemma、Mistral、Meta LLaMA 的量化轉換。

### **Generative AI extensions for onnxruntime 中的 Model Builder**

Model Builder 大大加速了使用 ONNX Runtime generate() API 創建優化和量化的 ONNX 模型。

通過 Model Builder，您可以將模型量化為 INT4、INT8、FP16、FP32，並結合不同的硬件加速方法，如 CPU、CUDA、DirectML、Mobile 等。

使用 Model Builder 您需要先安裝：

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

安裝完成後，您可以在終端中運行 Model Builder 腳本來進行模型格式和量化轉換。

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

了解相關參數：

1. **model_name** 這是 Hugging Face 上的模型，例如 microsoft/Phi-3.5-mini-instruct、microsoft/Phi-3.5-vision-instruct 等，也可以是您存儲模型的路徑。

2. **path_to_output_folder** 量化轉換的保存路徑。

3. **execution_provider** 不同的硬件加速支持，例如 cpu、cuda、DirectML。

4. **cache_dir_to_save_hf_files** 我們從 Hugging Face 下載模型並緩存到本地。

***注意：***

## **如何使用 Model Builder 量化 Phi-3.5**

Model Builder 現在支持 Phi-3.5 Instruct 和 Phi-3.5-Vision 的 ONNX 模型量化。

### **Phi-3.5-Instruct**

**CPU 加速的量化 INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA 加速的量化 INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. 在終端中設置環境：

```bash

mkdir models

cd models 

```

2. 在 models 文件夾中下載 microsoft/Phi-3.5-vision-instruct：
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. 請將以下文件下載到您的 Phi-3.5-vision-instruct 文件夾：

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. 將以下文件下載到 models 文件夾：
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. 在終端中執行：

    使用 FP32 進行 ONNX 支持轉換：

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **注意：**

1. Model Builder 目前支持 Phi-3.5-Instruct 和 Phi-3.5-Vision 的轉換，但不支持 Phi-3.5-MoE。

2. 要使用 ONNX 的量化模型，您可以通過 Generative AI extensions for onnxruntime SDK 使用。

3. 我們需要更多負責任的 AI，因此在模型量化轉換後，建議進行更有效的結果測試。

4. 通過量化 CPU INT4 模型，我們可以將其部署到邊緣設備，這樣可以有更好的應用場景，因此我們已完成圍繞 INT4 的 Phi-3.5-Instruct。

## **資源**

1. 了解更多關於 Generative AI extensions for onnxruntime 的信息：[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime 的 GitHub Repo：[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**免責聲明**：  
本文檔使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文檔應被視為權威來源。對於關鍵信息，建議使用專業的人工翻譯。我們不對因使用此翻譯而產生的任何誤解或錯誤解釋負責。