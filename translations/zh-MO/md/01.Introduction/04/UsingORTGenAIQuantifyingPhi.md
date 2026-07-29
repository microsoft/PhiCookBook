# **使用 onnxruntime 的 Generative AI 擴展進行 Phi 家族量化**

## **什麼是 onnxruntime 的 Generative AI 擴展**

此擴展幫助您使用 ONNX Runtime 來運行生成式 AI（[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)）。它為 ONNX 模型提供生成式 AI 循環，包括 ONNX Runtime 推理、logits 處理、搜索和採樣，以及 KV 緩存管理。開發者可以調用高階的 generate() 方法，或者在迴圈中逐次運行模型，每次生成一個 token，並且可選擇在迴圈內更新生成參數。它支持貪婪/束搜索以及 TopP、TopK 採樣來生成 token 序列，並內建如重複懲罰的 logits 處理。您也可以輕鬆新增自訂評分機制。

在應用層面，您可以使用 onnxruntime 的 Generative AI 擴展，利用 C++/C#/Python 构建應用程式。在模型層面，您可以用它來合併微調模型並進行相關的量化部署工作。


## **使用 onnxruntime 的 Generative AI 擴展對 Phi-3.5 進行量化**

### <strong>支援模型</strong>

onnxruntime 的 Generative AI 擴展支援 Microsoft Phi、Google Gemma、Mistral、Meta LLaMA 的量化轉換。


### **onnxruntime 的 Generative AI 擴展中的模型建構器**

模型建構器大大加速了創建可用 ONNX Runtime generate() API 運行的優化與量化 ONNX 模型的過程。

通過模型建構器，您可以將模型量化到 INT4、INT8、FP16、FP32, 並結合 CPU、CUDA、DirectML、Mobile 等不同硬體加速方式。

使用模型建構器您需要安裝

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

安裝完成後，您可以從終端運行模型建構器腳本來執行模型格式與量化轉換。


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

了解相關參數

1. **model_name** 指 Hugging Face 上的模型，例如 microsoft/Phi-3.5-mini-instruct、microsoft/Phi-3.5-vision-instruct 等。也可以是您存放模型的路徑

2. **path_to_output_folder** 量化轉換後保存的路徑

3. **execution_provider** 不同硬體加速支持，如 cpu、cuda、DirectML

4. **cache_dir_to_save_hf_files** 我們會從 Hugging Face 下載模型並本地緩存




***注意：*** <ul>雖然 onnxruntime 的 Generative AI 擴展仍處於預覽階段，但它們已整合入 Microsoft Olive，您也可以透過 Microsoft Olive 調用 onnxruntime 的 Generative AI 擴展模型建構器功能。</ul>

## **如何使用模型建構器量化 Phi-3.5**

模型建構器目前支持 Phi-3.5 Instruct 與 Phi-3.5-Vision 的 ONNX 模型量化。

### **Phi-3.5-Instruct**


**CPU 加速轉換量化 INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA 加速轉換量化 INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. 在終端設置環境

```bash

mkdir models

cd models 

```

2. 下載 microsoft/Phi-3.5-vision-instruct 至 models 文件夾
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. 請將以下檔案下載到您的 Phi-3.5-vision-instruct 文件夾

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. 下載此檔案到 models 文件夾
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. 進入終端

    轉換支持 FP32 的 ONNX


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **注意：**

1. 模型建構器目前支援 Phi-3.5-Instruct 與 Phi-3.5-Vision 的轉換，但不支援 Phi-3.5-MoE

2. 使用 ONNX 量化模型，可以透過 onnxruntime 的 Generative AI 擴展 SDK 來使用

3. 我們需要更多負責任的 AI，因此模型量化轉換後，建議進行更有效的結果測試

4. 透過量化 CPU INT4 模型，我們可以部署到邊緣設備，擁有更好的應用場景，因此我們已完成 Phi-3.5-Instruct 約 INT 4 的部分


## <strong>資源</strong>

1. 了解更多 onnxruntime 的 Generative AI 擴展 [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. onnxruntime 的 Generative AI 擴展 GitHub 倉庫 [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->