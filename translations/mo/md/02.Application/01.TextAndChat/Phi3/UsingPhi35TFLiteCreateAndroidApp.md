<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:50:21+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "mo"
}
-->
# **使用 Microsoft Phi-3.5 tflite 建立 Android 應用程式**

這是一個使用 Microsoft Phi-3.5 tflite 模型的 Android 範例。

## **📚 知識**

Android LLM 推論 API 讓你能在 Android 裝置上完全離線執行大型語言模型（LLM），可用於多種任務，例如生成文字、以自然語言形式檢索資訊，以及文件摘要。此任務內建支援多種文字轉文字的大型語言模型，讓你能將最新的離線生成式 AI 模型應用於 Android 應用程式。

Google AI Edge Torch 是一個 Python 函式庫，支援將 PyTorch 模型轉換成 .tflite 格式，之後可用 TensorFlow Lite 和 MediaPipe 執行。這使得 Android、iOS 和物聯網應用能完全在裝置端執行模型。AI Edge Torch 提供廣泛的 CPU 支援，並初步支援 GPU 和 NPU。AI Edge Torch 致力於與 PyTorch 緊密整合，基於 torch.export() 並提供良好的 Core ATen 運算子覆蓋。

## **🪬 指南**

### **🔥 將 Microsoft Phi-3.5 轉換為 tflite 支援**

0. 本範例適用於 Android 14 以上版本

1. 安裝 Python 3.10.12

***建議：*** 使用 conda 來建立你的 Python 環境

2. Ubuntu 20.04 / 22.04（請參考 [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch)）

***建議：*** 使用 Azure Linux VM 或第三方雲端虛擬機建立環境

3. 進入你的 Linux bash，安裝 Python 函式庫

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. 從 Hugging face 下載 Microsoft-3.5-Instruct

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. 將 Microsoft Phi-3.5 轉換為 tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 將 Microsoft Phi-3.5 轉換為 Android Mediapipe Bundle**

請先安裝 mediapipe

```bash

pip install mediapipe

```

在你的 [notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) 執行此程式碼

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

### **🔥 使用 adb 將任務模型推送到你的 Android 裝置路徑**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 執行你的 Android 程式碼**

![demo](../../../../../../translated_images/demo.06d5a4246f057d1b.mo.png)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。