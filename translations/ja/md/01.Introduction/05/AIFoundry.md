# **Microsoft Foundryを使用した評価**

![aistudo](../../../../../translated_images/ja/AIFoundry.9e0b513e999a1c5a.webp)

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo) を使用してジェネレーティブAIアプリケーションをどのように評価するか。シングルターンまたはマルチターンの会話を評価する場合でも、Microsoft Foundryはモデルのパフォーマンスと安全性を評価するためのツールを提供します。

![aistudo](../../../../../translated_images/ja/AIPortfolio.69da59a8e1eaa70f.webp)

## Microsoft FoundryでジェネレーティブAIアプリを評価する方法
詳細な手順は [Microsoft Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo) を参照してください。

はじめるためのステップは以下の通りです：

## Microsoft FoundryでジェネレーティブAIモデルを評価する

<strong>前提条件</strong>

- CSVまたはJSON形式のテストデータセット。
- デプロイ済みのジェネレーティブAIモデル（Phi-3、GPT 3.5、GPT 4、またはDavinciモデルなど）。
- 評価を実行するためのコンピュートインスタンスを備えたランタイム。

## 組み込みの評価指標

Microsoft Foundryはシングルターンおよび複雑なマルチターンの会話の両方を評価できます。
モデルが特定のデータに基づくRetrieval Augmented Generation（RAG）シナリオでは、組み込みの評価指標を使用してパフォーマンスを評価できます。
また、一般的なシングルターンの質問応答シナリオ（非RAG）も評価できます。

## 評価実行の作成

Microsoft FoundryのUIからEvaluateページまたはPrompt Flowページに移動します。
評価作成ウィザードに従って評価実行を設定します。評価の名前を任意で指定できます。
アプリケーションの目的に合ったシナリオを選択します。
モデルの出力を評価するための1つ以上の評価指標を選択します。

## カスタム評価フロー（オプション）

より柔軟に評価を行うために、カスタム評価フローを作成できます。特定の要件に応じて評価プロセスをカスタマイズしてください。

## 結果の確認

評価を実行した後、Microsoft Foundryで詳細な評価指標をログ、表示、および分析できます。アプリケーションの能力と制限について洞察を得ることができます。



**Note** Microsoft Foundryは現在パブリックプレビュー中のため、実験および開発目的での利用を推奨します。本番環境のワークロードには他の選択肢を検討してください。詳しい手順については公式の [AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) をご参照ください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。原文の母国語による文書が権威ある情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用に起因する誤解や誤訳について当方は責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->