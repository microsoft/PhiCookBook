<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2faa9c6d61c5aa2708aec02a39ec464b",
  "translation_date": "2025-04-04T06:31:46+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "tw"
}
-->
# **使用 Microsoft Phi-3.5 tflite 建立 Android 應用程式**

這是一個使用 Microsoft Phi-3.5 tflite 模型的 Android 範例。

## **📚 知識**

Android LLM Inference API 讓您能在 Android 應用程式中完全於裝置上執行大型語言模型（LLMs），可以用來完成多種任務，例如生成文字、以自然語言形式檢索資訊，以及摘要文件。該任務內建支援多種文字到文字的大型語言模型，因此您可以將最新的裝置端生成式 AI 模型應用於您的 Android 應用程式。

Google AI Edge Torch 是一個 Python 函式庫，支援將 PyTorch 模型轉換為 .tflite 格式，然後可以使用 TensorFlow Lite 和 MediaPipe 來執行。這使得 Android、iOS 和物聯網應用程式能完全在裝置上執行模型。AI Edge Torch 提供廣泛的 CPU 支援，並初步支援 GPU 和 NPU。AI Edge Torch 致力於與 PyTorch 緊密整合，基於 torch.export() 並提供良好的 Core ATen 運算符覆蓋。

## **🪬 指南**

### **🔥 將 Microsoft Phi-3.5 轉換為 tflite 格式**

0. 此範例適用於 Android 14+

1. 安裝 Python 3.10.12

***建議：*** 使用 conda 安裝您的 Python 環境

2. Ubuntu 20.04 / 22.04 （請專注於 [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch)）

***建議：*** 使用 Azure Linux VM 或第三方雲端 VM 建立您的環境

3. 進入您的 Linux bash，安裝 Python 函式庫

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. 從 Hugging Face 下載 Microsoft-3.5-Instruct

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. 將 Microsoft Phi-3.5 轉換為 tflite 格式

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 將 Microsoft Phi-3.5 轉換為 Android Mediapipe Bundle**

請先安裝 mediapipe

```bash

pip install mediapipe

```

在 [您的 notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) 中執行以下程式碼

```python

import mediapipe as mp
from mediapipe.tasks.python.genai import bundler

config = bundler.BundleConfig(
    tflite_model='Your Phi-3.5 tflite model path',
    tokenizer_model='Your Phi-3.5 tokenizer model path',
    start_token='start_token',
    stop_tokens=[STOP_TOKENS],
    output_filename='Your Phi-3.5 task model path',
    enable_bytes_to_unicode_mapping=True or Flase,
)
bundler.create_bundle(config)

```

### **🔥 使用 adb push 將模型推送至 Android 裝置路徑**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 執行您的 Android 程式碼**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.tw.png)

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提高準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。