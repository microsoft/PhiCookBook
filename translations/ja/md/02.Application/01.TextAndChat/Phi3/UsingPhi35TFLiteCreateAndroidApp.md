<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-08T05:41:59+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "ja"
}
-->
# **Microsoft Phi-3.5 tflite を使って Android アプリを作成する方法**

これは Microsoft Phi-3.5 tflite モデルを使った Android のサンプルです。

## **📚 知識**

Android LLM Inference API は、大規模言語モデル（LLM）を完全にデバイス上で実行できるようにし、テキスト生成や自然言語での情報取得、ドキュメントの要約など幅広いタスクに利用できます。このタスクは複数のテキスト・ツー・テキスト大規模言語モデルを標準でサポートしており、最新のオンデバイス生成AIモデルを Android アプリに適用可能です。

Googld AI Edge Torch は、PyTorch モデルを .tflite 形式に変換できる Python ライブラリで、TensorFlow Lite と MediaPipe で実行可能にします。これにより、Android、iOS、IoT 向けにモデルを完全にオンデバイスで動かすアプリケーションが作れます。AI Edge Torch は幅広い CPU をサポートし、初期段階で GPU と NPU のサポートも備えています。PyTorch と密接に連携し、torch.export() をベースに Core ATen オペレーターを幅広くカバーすることを目指しています。

## **🪬 ガイドライン**

### **🔥 Microsoft Phi-3.5 を tflite に変換する手順**

0. このサンプルは Android 14 以上向けです。

1. Python 3.10.12 をインストールしてください。

***おすすめ:*** conda を使って Python 環境を構築するのが便利です。

2. Ubuntu 20.04 / 22.04 を使用してください（[google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) に注目）

***おすすめ:*** Azure Linux VM やサードパーティのクラウド VM で環境を作るのが良いでしょう。

3. Linux の bash で Python ライブラリをインストールします。

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Hugging face から Microsoft-3.5-Instruct をダウンロードします。

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Microsoft Phi-3.5 を tflite に変換します。

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5 を Android Mediapipe バンドルに変換する**

まず mediapipe をインストールしてください。

```bash

pip install mediapipe

```

このコードは [your notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) で実行します。

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

### **🔥 adb push でタスクモデルを Android デバイスのパスに送る**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Android コードの実行**

![demo](../../../../../../translated_images/demo.06d5a4246f057d1be99ffad0cbf22f4ac0c41530774d51ff903cfaa1d3cd3c8e.ja.png)

**免責事項**:  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご承知ください。原文の母国語版が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨いたします。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。