<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2faa9c6d61c5aa2708aec02a39ec464b",
  "translation_date": "2025-04-04T12:44:25+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "ja"
}
-->
# **Microsoft Phi-3.5 tfliteを使用したAndroidアプリの作成**

これは、Microsoft Phi-3.5 tfliteモデルを使用したAndroidサンプルです。

## **📚 知識**

Android LLM Inference APIを使用すると、Androidアプリケーション向けに大規模言語モデル（LLM）を完全にオンデバイスで実行できます。このAPIを使用して、テキスト生成、自然言語形式での情報検索、ドキュメントの要約など、幅広いタスクを実行できます。このタスクは、複数のテキスト間の大規模言語モデルをサポートしており、最新のオンデバイス生成AIモデルをAndroidアプリに適用することが可能です。

Google AI Edge Torchは、PyTorchモデルを.tflite形式に変換することをサポートするPythonライブラリであり、この形式はTensorFlow LiteやMediaPipeで実行できます。これにより、完全にオンデバイスでモデルを実行できるAndroid、iOS、IoT向けのアプリケーションが可能になります。AI Edge Torchは幅広いCPUカバレッジを提供し、初期段階のGPUおよびNPUサポートも備えています。AI Edge TorchはPyTorchとの密接な統合を目指しており、torch.export()を基盤に構築し、Core ATenオペレーターの良好なカバレッジを提供します。

## **🪬 ガイドライン**

### **🔥 Microsoft Phi-3.5をtflite対応に変換**

0. このサンプルはAndroid 14以上向けです。

1. Python 3.10.12をインストールする

***提案:*** condaを使用してPython環境をインストールすることを推奨

2. Ubuntu 20.04 / 22.04 (詳細は [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) を参照)

***提案:*** Azure Linux VMやサードパーティのクラウドVMを使用して環境を構築することを推奨

3. Linux bashでPythonライブラリをインストールする

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Hugging FaceからMicrosoft-3.5-Instructをダウンロードする

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Microsoft Phi-3.5をtfliteに変換する

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5をAndroid Mediapipeバンドルに変換**

まず、mediapipeをインストールしてください。

```bash

pip install mediapipe

```

[ノートブック](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)でこのコードを実行してください。

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

### **🔥 adb pushを使用してモデルをAndroidデバイスのパスに転送**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Androidコードを実行する**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.ja.png)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があります。元の言語で記載された原文が公式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤った解釈について、当方は一切の責任を負いません。