<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-07-17T08:07:07+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "ja"
}
-->
# Phi-3-Vision-128K-Instruct プロジェクト概要

## モデルについて

Phi-3-Vision-128K-Instruct は、軽量で最先端のマルチモーダルモデルであり、本プロジェクトの中核を担っています。Phi-3 モデルファミリーの一部であり、最大128,000トークンのコンテキスト長をサポートします。このモデルは、合成データや厳選された公開ウェブサイトを含む多様なデータセットでトレーニングされており、高品質で推論力を要するコンテンツに重点を置いています。トレーニングには、教師ありファインチューニングと直接的な好みの最適化が含まれ、指示への正確な対応と堅牢な安全対策が確保されています。

## サンプルデータ作成が重要な理由

1. **テスト**: サンプルデータを使うことで、実際のデータに影響を与えずに様々なシナリオでアプリケーションをテストできます。これは特に開発やステージング段階で重要です。

2. **パフォーマンス調整**: 実データの規模や複雑さを模したサンプルデータを用いることで、パフォーマンスのボトルネックを特定し、最適化が可能になります。

3. **プロトタイピング**: サンプルデータはプロトタイプやモックアップの作成に利用でき、ユーザー要件の理解やフィードバック取得に役立ちます。

4. **データ分析**: データサイエンスの分野では、探索的データ分析やモデルのトレーニング、アルゴリズムのテストにサンプルデータがよく使われます。

5. **セキュリティ**: 開発やテスト環境でサンプルデータを使用することで、実際の機密データの漏洩を防ぐことができます。

6. **学習**: 新しい技術やツールを学ぶ際に、サンプルデータを使うことで実践的に学んだことを応用できます。

サンプルデータの品質はこれらの活動に大きな影響を与えます。構造や多様性の面で実データにできるだけ近いものにすることが望ましいです。

### サンプルデータ作成
[Generate DataSet Script](./CreatingSampleData.md)

## データセット

良いサンプルデータセットの例として、[DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States)（Huggingfaceで利用可能）があります。  
このサンプルデータセットは、Burberry製品のカテゴリ、価格、タイトルに関するメタデータとともに、3,040行のユニークな製品情報を含んでいます。このデータセットを使うことで、モデルが視覚データを理解・解釈し、細かな視覚的特徴やブランド固有の特性を捉えた説明文を生成する能力をテストできます。

**Note:** 画像を含む任意のデータセットを使用可能です。

## 複雑な推論

モデルは画像のみから価格や名称について推論する必要があります。これは、視覚的特徴を認識するだけでなく、それらが製品の価値やブランドにどのように影響するかを理解することを意味します。画像から正確なテキスト記述を合成することで、本プロジェクトは視覚データを統合し、実世界の応用におけるモデルの性能と多様性を高める可能性を示しています。

## Phi-3 Vision アーキテクチャ

このモデルのアーキテクチャは Phi-3 のマルチモーダル版です。テキストと画像の両方を処理し、これらの入力を統合したシーケンスとして扱うことで、包括的な理解と生成タスクを実現します。モデルはテキストと画像それぞれに別々の埋め込み層を使用します。テキストトークンは密なベクトルに変換され、画像はCLIPビジョンモデルを通じて特徴埋め込みを抽出します。これらの画像埋め込みはテキスト埋め込みの次元に合わせて射影され、シームレスに統合できるようにしています。

## テキストと画像埋め込みの統合

テキストシーケンス内の特殊トークンが画像埋め込みを挿入する位置を示します。処理時にこれらの特殊トークンは対応する画像埋め込みに置き換えられ、モデルはテキストと画像を一つのシーケンスとして扱います。データセットのプロンプトは、特殊な <|image|> トークンを使って以下のようにフォーマットされています。

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## サンプルコード
- [Phi-3-Vision トレーニングスクリプト](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。