# **使用 Intel OpenVINO 量化 Phi-3.5**

Intel 是最傳統的 CPU 製造商，擁有眾多用戶。隨著機器學習和深度學習的興起，Intel 也加入了 AI 加速的競爭。對於模型推理，Intel 不僅使用 GPU 和 CPU，還使用 NPU。

我們希望將 Phi-3.x 系列部署在終端設備上，期望成為 AI PC 和 Copilot PC 最重要的部分。終端設備上的模型加載依賴於不同硬體製造商的合作。本章主要聚焦於 Intel OpenVINO 作為量化模型的應用場景。

## **什麼是 OpenVINO**

OpenVINO 是一套開源工具包，用於優化和部署從雲端到邊緣的深度學習模型。它加速了各種應用場景下的深度學習推理，如生成式 AI、視頻、音頻和語言，支援來自 PyTorch、TensorFlow、ONNX 等熱門框架的模型。可轉換並優化模型，並在多種 Intel® 硬體和環境中部署，無論是在本地、設備端、瀏覽器還是雲端。

現在，透過 OpenVINO，您可以快速在 Intel 硬體上量化 GenAI 模型並加速模型參考。

目前 OpenVINO 支援 Phi-3.5-Vision 和 Phi-3.5 Instruct 的量化轉換。

### **環境設置**

請確保已安裝以下環境依賴，這是 requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **使用 OpenVINO 量化 Phi-3.5-Instruct**

在終端機中，請執行此腳本

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **使用 OpenVINO 量化 Phi-3.5-Vision**

請在 Python 或 Jupyter lab 中執行此腳本

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

### **🤖 Phi-3.5 與 Intel OpenVINO 範例**

| 實驗室    | 介紹 | 前往 |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | 學習如何在您的 AI PC 中使用 Phi-3.5 Instruct    |  [前往](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (影像) | 學習如何使用 Phi-3.5 Vision 在您的 AI PC 中分析影像      |  [前往](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (影片)   | 學習如何使用 Phi-3.5 Vision 在您的 AI PC 中分析影片    |  [前往](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **資源**

1. 了解更多 Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub 倉庫 [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。