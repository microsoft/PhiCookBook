<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:50:13+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "zh"
}
-->
# **使用 Microsoft Phi-3.5 tflite 创建 Android 应用**

这是一个使用 Microsoft Phi-3.5 tflite 模型的 Android 示例。

## **📚 知识**

Android LLM 推理 API 允许你在 Android 设备上完全本地运行大型语言模型（LLM），你可以用它来执行各种任务，比如生成文本、以自然语言形式检索信息以及总结文档。该任务内置支持多种文本到文本的大型语言模型，因此你可以将最新的本地生成式 AI 模型应用到你的 Android 应用中。

Google AI Edge Torch 是一个 Python 库，支持将 PyTorch 模型转换为 .tflite 格式，之后可以用 TensorFlow Lite 和 MediaPipe 运行。这使得 Android、iOS 和物联网设备上的应用能够完全本地运行模型。AI Edge Torch 提供广泛的 CPU 支持，并初步支持 GPU 和 NPU。AI Edge Torch 致力于与 PyTorch 深度集成，基于 torch.export() 构建，并对 Core ATen 操作符提供良好支持。

## **🪬 指南**

### **🔥 将 Microsoft Phi-3.5 转换为 tflite 支持**

0. 本示例适用于 Android 14 及以上版本

1. 安装 Python 3.10.12

***建议：*** 使用 conda 来安装你的 Python 环境

2. Ubuntu 20.04 / 22.04（请重点关注 [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch)）

***建议：*** 使用 Azure Linux 虚拟机或第三方云虚拟机来创建你的环境

3. 进入你的 Linux bash，安装 Python 库

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. 从 Hugging Face 下载 Microsoft-3.5-Instruct

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. 将 Microsoft Phi-3.5 转换为 tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 转换 Microsoft Phi-3.5 为 Android Mediapipe Bundle**

请先安装 mediapipe

```bash

pip install mediapipe

```

在你的 [notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) 中运行此代码

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

### **🔥 使用 adb 将任务模型推送到你的 Android 设备路径**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 运行你的 Android 代码**

![demo](../../../../../../translated_images/zh/demo.06d5a4246f057d1b.webp)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。