<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:50:48+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "ja"
}
-->
# **Microsoft Phi-3.5 tfliteを使ってAndroidアプリを作成する方法**

これはMicrosoft Phi-3.5 tfliteモデルを使用したAndroidのサンプルです。

## **📚 知識**

Android LLM Inference APIは、Androidアプリ上で大規模言語モデル（LLM）を完全にデバイス内で実行できるようにし、テキスト生成、自然言語での情報取得、文書の要約など幅広いタスクに利用できます。このタスクは複数のテキスト・トゥ・テキスト大規模言語モデルを標準でサポートしており、最新のオンデバイス生成AIモデルをAndroidアプリに適用可能です。

Googld AI Edge Torchは、PyTorchモデルを.tflite形式に変換できるPythonライブラリで、TensorFlow LiteやMediaPipeで実行できます。これにより、Android、iOS、IoT向けに完全にデバイス内でモデルを動かすアプリケーションが可能になります。AI Edge Torchは幅広いCPUをサポートし、初期段階でGPUやNPUも対応しています。PyTorchとの密接な統合を目指し、torch.export()を基盤にCore ATenオペレーターのカバー率を高めています。

## **🪬 ガイドライン**

### **🔥 Microsoft Phi-3.5をtfliteに変換する方法**

0. このサンプルはAndroid 14以上向けです

1. Python 3.10.12をインストールしてください

***おすすめ:*** condaを使ってPython環境を構築することを推奨します

2. Ubuntu 20.04 / 22.04（[google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch)に注目してください）

***おすすめ:*** Azure Linux VMやサードパーティのクラウドVMを使って環境を作成するのが便利です

3. Linuxのbashに移動し、Pythonライブラリをインストールします

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Hugging faceからMicrosoft-3.5-Instructをダウンロードします

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Microsoft Phi-3.5をtfliteに変換します

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5をAndroid Mediapipeバンドルに変換する方法**

まずはmediapipeをインストールしてください

```bash

pip install mediapipe

```

このコードは[your notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)で実行します

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

### **🔥 adb pushでモデルをAndroidデバイスのパスに転送する方法**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Androidコードの実行**

![demo](../../../../../../translated_images/ja/demo.06d5a4246f057d1b.png)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。