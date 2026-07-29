# **使用 onnxruntime 的生成式 AI 擴展對 Phi 系列進行量化**

## **什麼是 onnxruntime 的生成式 AI 擴展**

該擴展幫助您使用 ONNX Runtime（[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)）運行生成式 AI。它為 ONNX 模型提供生成式 AI 流程，包括使用 ONNX Runtime 進行推理、logits 處理、搜尋與採樣，以及 KV 快取管理。開發者可以呼叫高階的 generate() 方法，或者在循環中逐次執行模型來生成一個 token，並可選擇在循環中更新生成參數。它支援貪婪/束搜索（beam search）以及 TopP、TopK 採樣，以生成 token 序列，並內建了重複懲罰等 logits 處理。您也可以輕鬆添加自訂評分。

在應用層面，您可以使用 onnxruntime 的生成式 AI 擴展以 C++/ C# / Python 建構應用程式。在模型層面，您可以用它來合併已微調的模型並進行相應的量化部署工作。


## **使用 onnxruntime 的生成式 AI 擴展對 Phi-3.5 進行量化**

### <strong>支援的模型</strong>

onnxruntime 的生成式 AI 擴展支援 Microsoft Phi、Google Gemma、Mistral、Meta LLaMA 的量化轉換。


### **onnxruntime 的生成式 AI 擴展中的模型建構器**

模型建構器大幅加速了建構可使用 ONNX Runtime generate() API 執行的優化與量化 ONNX 模型。

透過模型建構器，您可以將模型量化至 INT4、INT8、FP16、FP32，並結合 CPU、CUDA、DirectML、行動裝置等不同硬體加速方式。

使用模型建構器，您需要安裝

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

安裝完成後，您可以從終端機執行模型建構器腳本來執行模型格式及量化轉換。


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

了解相關參數

1. **model_name** 這是 Hugging face 上的模型名稱，如 microsoft/Phi-3.5-mini-instruct、microsoft/Phi-3.5-vision-instruct 等，也可以是您存放模型的路徑

2. **path_to_output_folder** 量化轉換的儲存路徑

3. **execution_provider** 不同的硬體加速支援，如 cpu、cuda、DirectML

4. **cache_dir_to_save_hf_files** 從 Hugging face 下載模型並進行本地快取的位置




***注意：*** <ul>雖然 onnxruntime 的生成式 AI 擴展目前仍為預覽版，但已被納入 Microsoft Olive，您也可以透過 Microsoft Olive 呼叫 onnxruntime 的生成式 AI 擴展模型建構器功能。</ul>

## **如何使用模型建構器對 Phi-3.5 進行量化**

模型建構器目前支援 Phi-3.5 Instruct 和 Phi-3.5-Vision 的 ONNX 模型量化

### **Phi-3.5-Instruct**


**使用 CPU 加速轉換至量化 INT4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**使用 CUDA 加速轉換至量化 INT4**

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

2. 在 models 資料夾中下載 microsoft/Phi-3.5-vision-instruct
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. 請將下列檔案下載至您的 Phi-3.5-vision-instruct 資料夾

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. 將此檔案下載至 models 資料夾
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. 進到終端機

    轉換 ONNX 支援 FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **注意：**

1. 模型建構器目前支援 Phi-3.5-Instruct 與 Phi-3.5-Vision 的轉換，但不支援 Phi-3.5-MoE

2. 若要使用 ONNX 的量化模型，可以透過 onnxruntime 的生成式 AI 擴展 SDK 使用

3. 因為我們需要更多負責任的 AI，模型量化轉換後，建議進行更有效的結果測試

4. 透過量化的 CPU INT4 模型，我們可以將它部署到 Edge 裝置，擁有更好的應用場景，因此我們已完成 Phi-3.5-Instruct 約 INT4 的量化


## <strong>資源</strong>

1. 進一步了解 onnxruntime 的生成式 AI 擴展 [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. onnxruntime 的生成式 AI 擴展 GitHub 倉庫 [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->