<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f766ec7e68d97f6009b58794b471d66",
  "translation_date": "2025-04-04T06:07:06+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "tw"
}
-->
# **使用 Intel OpenVINO 量化 Phi-3.5**

Intel 是最傳統的 CPU 製造商之一，擁有眾多用戶。隨著機器學習和深度學習的崛起，Intel 也加入了 AI 加速的競爭。對於模型推理，Intel 不僅使用 GPU 和 CPU，還使用 NPU。

我們希望將 Phi-3.x 家族部署在終端側，並成為 AI PC 和 Copilot PC 的核心部分。在終端側載入模型需要不同硬件製造商的合作。本章主要聚焦於 Intel OpenVINO 作為量化模型的應用場景。

## **什麼是 OpenVINO**

OpenVINO 是一個開源工具包，用於優化和部署從雲端到邊緣的深度學習模型。它能加速深度學習推理，涵蓋多種使用場景，例如生成式 AI、視頻、音頻以及語言，並支持來自 PyTorch、TensorFlow、ONNX 等流行框架的模型。通過轉換和優化模型，可以在 Intel® 硬件和多種環境中部署，包括本地、設備端、瀏覽器或雲端。

現在使用 OpenVINO，您可以快速在 Intel 硬件上量化 GenAI 模型，並加速模型推理。

目前 OpenVINO 支持 Phi-3.5-Vision 和 Phi-3.5-Instruct 的量化轉換。

### **環境設置**

請確保已安裝以下環境依賴項，這是 requirement.txt 

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **使用 OpenVINO 量化 Phi-3.5-Instruct**

在終端中，請運行以下腳本

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **使用 OpenVINO 量化 Phi-3.5-Vision**

請在 Python 或 Jupyter lab 中運行以下腳本

```python

import requests
from pathlib import Path
from ov_phi3_vision import convert_phi3_model
import nncf

if not Path("ov_phi3_vision.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/ov_phi3_vision.py")
    open("ov_phi3_vision.py", "w").write(r.text)


if not Path("gradio_helper.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/gradio_helper.py")
    open("gradio_helper.py", "w").write(r.text)

if not Path("notebook_utils.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/utils/notebook_utils.py")
    open("notebook_utils.py", "w").write(r.text)



model_id = "microsoft/Phi-3.5-vision-instruct"
out_dir = Path("../model/phi-3.5-vision-128k-instruct-ov")
compression_configuration = {
    "mode": nncf.CompressWeightsMode.INT4_SYM,
    "group_size": 64,
    "ratio": 0.6,
}
if not out_dir.exists():
    convert_phi3_model(model_id, out_dir, compression_configuration)

```

### **🤖 使用 Intel OpenVINO 的 Phi-3.5 示例**

| 實驗室    | 介紹 | 前往 |
| -------- | ------- |  ------- |
| 🚀 Lab-介紹 Phi-3.5 Instruct  | 學習如何在您的 AI PC 中使用 Phi-3.5 Instruct    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-介紹 Phi-3.5 Vision (圖像) | 學習如何在您的 AI PC 中使用 Phi-3.5 Vision 進行圖像分析      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-介紹 Phi-3.5 Vision (視頻)   | 學習如何在您的 AI PC 中使用 Phi-3.5 Vision 進行視頻分析    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **資源**

1. 了解更多 Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**免責聲明**：  
本文檔使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們努力確保翻譯的準確性，但請注意，機器翻譯可能會包含錯誤或不精確之處。應以原始語言的文件作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。