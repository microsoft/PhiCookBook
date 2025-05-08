<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-05-08T05:24:55+00:00",
  "source_file": "md/03.FineTuning/03.Inference/MLX_Inference.md",
  "language_code": "ja"
}
-->
# **Apple MLX FrameworkによるPhi-3の推論**

## **MLX Frameworkとは**

MLXはAppleシリコン上での機械学習研究向けの配列フレームワークで、Appleの機械学習研究チームによって開発されました。

MLXは機械学習研究者のために機械学習研究者が設計したものです。ユーザーフレンドリーでありながら、モデルのトレーニングやデプロイを効率的に行えるように設計されています。フレームワーク自体の設計も概念的にシンプルで、新しいアイデアを素早く試せるように研究者がMLXを拡張・改善しやすいことを目指しています。

LLMはAppleシリコンデバイス上でMLXを通じて高速化でき、モデルをローカルで非常に便利に実行可能です。

## **MLXを使ったPhi-3-miniの推論**

### **1. MLX環境のセットアップ**

1. Python 3.11.x  
2. MLXライブラリのインストール  


```bash

pip install mlx-lm

```

### **2. ターミナルでMLXを使ってPhi-3-miniを実行**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

結果（私の環境はApple M1 Max、64GB）は以下の通りです。

![Terminal](../../../../../translated_images/01.5cf57df8f7407cf9281c0237f4e69c3728b8817253aad0835d14108b07c83c88.ja.png)

### **3. ターミナルでMLXを使ってPhi-3-miniを量子化**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** モデルはmlx_lm.convertで量子化可能で、デフォルトの量子化はINT4です。この例ではPhi-3-miniをINT4に量子化しています。

モデルはmlx_lm.convertで量子化でき、デフォルトはINT4です。この例ではPhi-3-miniをINT4に量子化し、量子化後はデフォルトのディレクトリ ./mlx_model に保存されます。

量子化したモデルはターミナルからMLXでテストできます。

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

結果は以下の通りです。

![INT4](../../../../../translated_images/02.7b188681a8eadbc111aba8d8006e4b3671788947a99a46329261e169dd2ec29f.ja.png)

### **4. Jupyter NotebookでMLXを使ってPhi-3-miniを実行**

![Notebook](../../../../../translated_images/03.b9705a3a5aaa89f9eb0ca04c1a4565dfe4a5e8cc68604227d2eab149fef1d3c7.ja.png)

***Note:*** サンプルは[こちらのリンク](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)からご覧ください。


## **リソース**

1. Apple MLX Frameworkについて学ぶ [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHubリポジトリ [https://github.com/ml-explore](https://github.com/ml-explore)

**免責事項**:  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や解釈の相違について、当方は一切責任を負いません。