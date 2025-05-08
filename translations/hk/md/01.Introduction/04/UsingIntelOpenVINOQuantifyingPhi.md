<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-05-08T06:08:30+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "hk"
}
-->
# **用 Intel OpenVINO 量化 Phi-3.5**

Intel 係最傳統嘅 CPU 製造商，擁有好多用戶。隨住機器學習同深度學習嘅興起，Intel 都加入咗 AI 加速嘅競爭。喺模型推理方面，Intel 唔單止用 GPU 同 CPU，仲用埋 NPU。

我哋希望將 Phi-3.x 家族部署喺終端設備，希望成為 AI PC 同 Copilot PC 最重要嘅一部分。終端設備嘅模型載入依賴唔同硬件廠商嘅合作。今章主要聚焦喺用 Intel OpenVINO 做量化模型嘅應用場景。

## **乜嘢係 OpenVINO**

OpenVINO 係一個開源工具包，用嚟優化同部署深度學習模型，從雲端到邊緣設備。佢可以加速各種場景嘅深度學習推理，好似生成式 AI、視頻、音頻同語言等，支援 PyTorch、TensorFlow、ONNX 等流行框架嘅模型。可以轉換同優化模型，並喺 Intel® 硬件同多種環境中部署，包括本地、設備端、瀏覽器或雲端。

而家用 OpenVINO，你可以快速喺 Intel 硬件度量化 GenAI 模型，加快模型參考速度。

而家 OpenVINO 支援 Phi-3.5-Vision 同 Phi-3.5 Instruct 嘅量化轉換。

### **環境設置**

請確保已安裝以下環境依賴，呢啲係 requirement.txt 內容

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **用 OpenVINO 量化 Phi-3.5-Instruct**

喺終端機運行以下腳本

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **用 OpenVINO 量化 Phi-3.5-Vision**

請喺 Python 或 Jupyter lab 運行以下腳本

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

### **🤖 Intel OpenVINO 嘅 Phi-3.5 範例**

| Labs    | 介紹 | 前往 |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | 學習點樣喺你嘅 AI PC 使用 Phi-3.5 Instruct    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | 學習點樣用 Phi-3.5 Vision 喺你嘅 AI PC 分析圖片      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | 學習點樣用 Phi-3.5 Vision 喺你嘅 AI PC 分析影片    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **資源**

1. 深入了解 Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原文的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。對於因使用此翻譯而引起的任何誤解或誤釋，我們概不負責。