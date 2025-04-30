<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "340bd4c009524ef84102b78d06eea735",
  "translation_date": "2025-04-04T12:13:05+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingAppleMLXQuantifyingPhi.md",
  "language_code": "ja"
}
-->
# **Apple MLXフレームワークを使用したPhi-3.5の量子化**

MLXは、Appleシリコン上での機械学習研究のための配列フレームワークで、Appleの機械学習研究チームによって提供されています。

MLXは、機械学習研究者のために設計されており、使いやすさを重視しつつも、モデルのトレーニングやデプロイを効率的に行えるように作られています。このフレームワークの設計は概念的にもシンプルで、研究者がMLXを拡張したり改善したりすることで、新しいアイデアを迅速に試せるようにすることを目指しています。

LLMはAppleシリコンデバイス上でMLXを通じて高速化でき、モデルをローカルで非常に便利に実行できます。

現在、Apple MLXフレームワークはPhi-3.5-Instruct（**Apple MLX Frameworkサポート**）、Phi-3.5-Vision（**MLX-VLM Frameworkサポート**）、Phi-3.5-MoE（**Apple MLX Frameworkサポート**）の量子化変換をサポートしています。それでは試してみましょう：

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

### **🤖 Apple MLXを使用したPhi-3.5のサンプル**

| ラボ    | 紹介 | 移動 |
| -------- | ------- |  ------- |
| 🚀 Lab-Phi-3.5 Instructの紹介  | Apple MLXフレームワークを使用してPhi-3.5 Instructを活用する方法を学ぶ   |  [移動](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Phi-3.5 Vision（画像）の紹介 | Apple MLXフレームワークを使用してPhi-3.5 Visionで画像を分析する方法を学ぶ     |  [移動](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Phi-3.5 MoEの紹介   | Apple MLXフレームワークを使用してPhi-3.5 MoEを活用する方法を学ぶ  |  [移動](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **リソース**

1. Apple MLXフレームワークについて学ぶ [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHubリポジトリ [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHubリポジトリ [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてご確認ください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤った解釈について、当方は責任を負いません。