<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-08T06:10:23+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "ja"
}
-->
# **Apple MLXフレームワークを使ったPhi-3.5の量子化**

MLXはAppleシリコン上での機械学習研究のための配列フレームワークで、Appleの機械学習研究チームによって提供されています。

MLXは機械学習研究者によって機械学習研究者のために設計されています。このフレームワークは使いやすさを重視しつつ、モデルのトレーニングやデプロイが効率的に行えるように設計されています。フレームワーク自体の設計も概念的にシンプルです。研究者がMLXを簡単に拡張・改良できるようにし、新しいアイデアを素早く試せることを目指しています。

Appleシリコン搭載デバイスではMLXを通じてLLMを高速化でき、モデルをローカルで非常に便利に実行できます。

現在、Apple MLXフレームワークはPhi-3.5-Instruct(**Apple MLX Framework support**)、Phi-3.5-Vision(**MLX-VLM Framework support**)およびPhi-3.5-MoE(**Apple MLX Framework support**)の量子化変換をサポートしています。次に試してみましょう：

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 Apple MLX対応Phi-3.5のサンプル**

| ラボ    | 内容紹介 | 実行 |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Apple MLXフレームワークでPhi-3.5 Instructの使い方を学ぶ   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Apple MLXフレームワークでPhi-3.5 Visionを使って画像解析を学ぶ     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Apple MLXフレームワークでPhi-3.5 MoEの使い方を学ぶ  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **リソース**

1. Apple MLXフレームワークについて学ぶ [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHubリポジトリ [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHubリポジトリ [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**免責事項**：  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の言語による文書が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、一切の責任を負いかねます。