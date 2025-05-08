<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-08T05:41:52+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "hk"
}
-->
# **使用 Microsoft Phi-3.5 tflite 來建立 Android 應用程式**

呢個係一個用 Microsoft Phi-3.5 tflite 模型嘅 Android 範例。

## **📚 知識**

Android LLM Inference API 令你可以喺 Android 應用程式上完全本地執行大型語言模型（LLMs），可以用嚟做唔同嘅任務，例如生成文字、用自然語言形式檢索資訊，仲可以做文件摘要。呢個任務內建支援多個 text-to-text 大型語言模型，咁你就可以喺 Android app 上應用最新嘅本地生成式 AI 模型。

Google AI Edge Torch 係一個 Python 庫，支援將 PyTorch 模型轉換成 .tflite 格式，之後可以用 TensorFlow Lite 同 MediaPipe 執行。呢個功能令 Android、iOS 同 IoT 應用可以完全本地運行模型。AI Edge Torch 提供廣泛嘅 CPU 支援，仲有初步嘅 GPU 同 NPU 支援。AI Edge Torch 旨喺同 PyTorch 緊密整合，基於 torch.export()，並且提供 Core ATen 運算子嘅良好覆蓋。

## **🪬 指引**

### **🔥 將 Microsoft Phi-3.5 轉成 tflite 支援**

0. 呢個範例適用於 Android 14+

1. 安裝 Python 3.10.12

***建議：*** 用 conda 安裝 Python 環境

2. Ubuntu 20.04 / 22.04（請留意 [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch)）

***建議：*** 用 Azure Linux VM 或第三方雲端 VM 建立環境

3. 喺 Linux bash 入面安裝 Python 庫

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

5. 將 Microsoft Phi-3.5 轉成 tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 轉成 Microsoft Phi-3.5 Android Mediapipe Bundle**

請先安裝 mediapipe

```bash

pip install mediapipe

```

喺 [你嘅 notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) 執行呢段代碼

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

### **🔥 用 adb push 將任務模型推送到你嘅 Android 裝置路徑**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 執行你嘅 Android 代碼**

![demo](../../../../../../translated_images/demo.06d5a4246f057d1be99ffad0cbf22f4ac0c41530774d51ff903cfaa1d3cd3c8e.hk.png)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋盡力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件嘅母語版本應視為權威來源。對於重要資訊，建議使用專業人工翻譯。我哋對因使用此翻譯而引致嘅任何誤解或誤釋概不負責。