<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "700b9a537ce4426de5a7ccfa8e96e581",
  "translation_date": "2025-04-04T12:06:58+00:00",
  "source_file": "md\\01.Introduction\\03\\MLX_Inference.md",
  "language_code": "ja"
}
-->
# **Apple MLXフレームワークでPhi-3を推論**

## **MLXフレームワークとは**

MLXは、Appleシリコン上で機械学習研究を行うための配列フレームワークで、Appleの機械学習研究チームによって提供されています。

MLXは、機械学習研究者のために設計されており、使いやすさと効率性を兼ね備えています。モデルのトレーニングやデプロイが効率的に行えるだけでなく、フレームワーク自体の設計も概念的にシンプルです。研究者がMLXを拡張し改善しやすいように設計されており、新しいアイデアを迅速に探求することが目的です。

LLMはMLXを使用することでAppleシリコンデバイス上で加速され、ローカル環境で非常に便利に実行できます。

## **MLXを使用してPhi-3-miniを推論する**

### **1. MLX環境のセットアップ**

1. Python 3.11.x
2. MLXライブラリをインストール


```bash

pip install mlx-lm

```

### **2. ターミナルでMLXを使ってPhi-3-miniを実行する**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

結果（私の環境はApple M1 Max, 64GB）は以下の通りです。

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.ja.png)

### **3. ターミナルでMLXを使ってPhi-3-miniを量子化する**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***注意：*** モデルはmlx_lm.convertを使用して量子化することができ、デフォルトの量子化形式はINT4です。この例ではPhi-3-miniをINT4に量子化します。

モデルはmlx_lm.convertを使用して量子化可能で、デフォルトの量子化形式はINT4です。この例ではPhi-3-miniをINT4に量子化します。量子化後、デフォルトのディレクトリ ./mlx_model に保存されます。

ターミナルでMLXを使用して量子化されたモデルをテストできます。


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

結果は以下の通りです。

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.ja.png)


### **4. Jupyter NotebookでMLXを使ってPhi-3-miniを実行する**


![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.ja.png)

***注意:*** このサンプルをご覧ください [こちらをクリック](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **リソース**

1. Apple MLXフレームワークについて学ぶ [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHubリポジトリ [https://github.com/ml-explore](https://github.com/ml-explore)

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を目指していますが、自動翻訳には誤りや不正確な部分が含まれる場合があります。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳を利用したことによる誤解や解釈の違いについて、当社は一切の責任を負いません。