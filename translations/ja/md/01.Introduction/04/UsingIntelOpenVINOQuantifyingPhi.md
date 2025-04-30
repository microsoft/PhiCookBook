<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f766ec7e68d97f6009b58794b471d66",
  "translation_date": "2025-04-04T12:14:25+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "ja"
}
-->
# **Intel OpenVINOを使用したPhi-3.5の量子化**

Intelは、最も伝統的なCPUメーカーであり、多くのユーザーを抱えています。機械学習や深層学習の台頭に伴い、IntelもAIアクセラレーション競争に参加しています。モデル推論において、IntelはGPUやCPUだけでなく、NPUも使用しています。

私たちはPhi-3.xファミリーをエンド側に展開し、AI PCやCopilot PCの最重要部分になることを目指しています。エンド側でのモデルの読み込みは、異なるハードウェアメーカーの協力に依存します。本章では、Intel OpenVINOを量子化モデルの適用シナリオとして主に取り上げます。

## **OpenVINOとは**

OpenVINOは、クラウドからエッジまでの深層学習モデルを最適化し展開するためのオープンソースツールキットです。PyTorch、TensorFlow、ONNXなどの人気フレームワークのモデルを使用して、生成AI、ビデオ、音声、言語などさまざまなユースケースで深層学習推論を高速化します。モデルを変換して最適化し、オンプレミスやデバイス上、ブラウザやクラウド内など、Intel®のハードウェアと環境の組み合わせで展開できます。

現在、OpenVINOを使用することで、Intelのハードウェア上でGenAIモデルを迅速に量子化し、モデルの推論を高速化できます。

OpenVINOはPhi-3.5-VisionおよびPhi-3.5 Instructの量子化変換をサポートしています。

### **環境セットアップ**

以下の環境依存関係がインストールされていることを確認してください。これがrequirement.txtです。

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **OpenVINOを使用したPhi-3.5-Instructの量子化**

ターミナルで以下のスクリプトを実行してください。

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **OpenVINOを使用したPhi-3.5-Visionの量子化**

PythonまたはJupyter Labで以下のスクリプトを実行してください。

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

### **🤖 Intel OpenVINOを使用したPhi-3.5のサンプル**

| ラボ    | 説明 | リンク |
| -------- | ------- |  ------- |
| 🚀 Lab-Phi-3.5 Instructの紹介  | AI PCでPhi-3.5 Instructを使用する方法を学ぶ    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Phi-3.5 Vision (画像)の紹介 | AI PCでPhi-3.5 Visionを使用して画像を分析する方法を学ぶ      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Phi-3.5 Vision (動画)の紹介   | AI PCでPhi-3.5 Visionを使用して動画を分析する方法を学ぶ    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **リソース**

1. Intel OpenVINOについて詳しく知る [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHubリポジトリ [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で作成された文書を正式な情報源とみなしてください。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。