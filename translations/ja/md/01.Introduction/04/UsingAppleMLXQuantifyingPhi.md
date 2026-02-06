# **Apple MLXフレームワークを使ったPhi-3.5の量子化**

MLXはAppleシリコン上での機械学習研究のための配列フレームワークで、Appleの機械学習研究チームによって開発されました。

MLXは機械学習研究者による、機械学習研究者のための設計です。このフレームワークは使いやすさを重視しつつ、モデルのトレーニングやデプロイを効率的に行えるように設計されています。フレームワーク自体の設計も概念的にシンプルで、研究者がMLXを拡張・改良しやすく、新しいアイデアを素早く試せることを目指しています。

Appleシリコン搭載デバイス上でMLXを使うことでLLMの高速化が可能で、モデルをローカルで手軽に実行できます。

現在、Apple MLXフレームワークはPhi-3.5-Instruct（**Apple MLX Framework support**）、Phi-3.5-Vision（**MLX-VLM Framework support**）、Phi-3.5-MoE（**Apple MLX Framework support**）の量子化変換をサポートしています。さっそく試してみましょう。

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

### **🤖 Apple MLXで使うPhi-3.5のサンプル**

| ラボ    | 内容紹介 | 実行 |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Apple MLXフレームワークでPhi-3.5 Instructを使う方法を学ぶ   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Apple MLXフレームワークでPhi-3.5 Visionを使って画像解析を行う方法を学ぶ     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Apple MLXフレームワークでPhi-3.5 MoEを使う方法を学ぶ  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **リソース**

1. Apple MLXフレームワークについて学ぶ [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHubリポジトリ [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHubリポジトリ [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。