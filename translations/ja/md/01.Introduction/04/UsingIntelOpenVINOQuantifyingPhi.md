# **Intel OpenVINOを使ったPhi-3.5の量子化**

Intelは最も伝統的なCPUメーカーで、多くのユーザーを持っています。機械学習や深層学習の台頭に伴い、IntelもAIアクセラレーションの競争に参入しました。モデル推論において、IntelはGPUやCPUだけでなく、NPUも活用しています。

私たちはPhi-3.xファミリーをエッジ側に展開し、AI PCやCopilot PCの最重要部分になることを目指しています。エッジ側でのモデルの読み込みは、さまざまなハードウェアメーカーの協力に依存しています。本章では主にIntel OpenVINOを用いた量子化モデルの適用シナリオに焦点を当てます。

## **OpenVINOとは**

OpenVINOは、クラウドからエッジまでの深層学習モデルの最適化と展開のためのオープンソースツールキットです。PyTorch、TensorFlow、ONNXなどの人気フレームワークのモデルを使い、生成AI、動画、音声、言語など多様なユースケースで深層学習推論を高速化します。モデルの変換と最適化を行い、Intel®のハードウェアや環境の組み合わせで、オンプレミスやデバイス上、ブラウザやクラウドで展開可能です。

OpenVINOを使えば、Intelハードウェア上でGenAIモデルを素早く量子化し、モデルの高速化が可能です。

現在、OpenVINOはPhi-3.5-VisionとPhi-3.5 Instructの量子化変換をサポートしています。

### **環境構築**

以下の環境依存関係がインストールされていることを確認してください。これはrequirement.txtです。

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **OpenVINOを使ったPhi-3.5-Instructの量子化**

ターミナルで以下のスクリプトを実行してください。

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **OpenVINOを使ったPhi-3.5-Visionの量子化**

PythonまたはJupyter labで以下のスクリプトを実行してください。

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

### **🤖 Intel OpenVINO対応Phi-3.5のサンプル**

| ラボ    | 説明 | 移動 |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | AI PCでPhi-3.5 Instructの使い方を学ぶ    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (画像) | AI PCでPhi-3.5 Visionを使って画像解析を学ぶ      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (動画)   | AI PCでPhi-3.5 Visionを使って動画解析を学ぶ    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |



## **参考資料**

1. Intel OpenVINOについて詳しくはこちら [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHubリポジトリ [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。