<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7b4235159486df4000e16b7b46ddfec3",
  "translation_date": "2025-07-16T22:29:33+00:00",
  "source_file": "md/01.Introduction/05/AIFoundry.md",
  "language_code": "ja"
}
-->
# **Azure AI Foundryを使った評価方法**

![aistudo](../../../../../translated_images/ja/AIFoundry.9e0b513e999a1c5a.png)

[Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo)を使って生成AIアプリケーションを評価する方法です。シングルターンやマルチターンの会話を評価する際に、Azure AI Foundryはモデルの性能や安全性を評価するためのツールを提供します。

![aistudo](../../../../../translated_images/ja/AIPortfolio.69da59a8e1eaa70f.png)

## Azure AI Foundryで生成AIアプリを評価する方法
詳細な手順については、[Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)をご覧ください。

以下は評価を始めるためのステップです：

## Azure AI Foundryで生成AIモデルを評価する

**前提条件**

- CSVまたはJSON形式のテストデータセット
- デプロイ済みの生成AIモデル（Phi-3、GPT 3.5、GPT 4、Davinciモデルなど）
- 評価を実行するためのコンピュートインスタンスを備えたランタイム

## 組み込みの評価指標

Azure AI Foundryでは、シングルターンだけでなく複雑なマルチターン会話の評価も可能です。  
特定のデータに基づくRetrieval Augmented Generation（RAG）シナリオでは、組み込みの評価指標を使って性能を評価できます。  
また、一般的なシングルターンの質問応答シナリオ（非RAG）も評価可能です。

## 評価実行の作成

Azure AI FoundryのUIから、EvaluateページまたはPrompt Flowページに移動します。  
評価作成ウィザードに従って評価実行を設定します。評価に任意の名前を付けることができます。  
アプリケーションの目的に合ったシナリオを選択してください。  
モデルの出力を評価するために、1つ以上の評価指標を選択します。

## カスタム評価フロー（任意）

より柔軟に評価を行いたい場合は、カスタム評価フローを作成できます。  
特定の要件に合わせて評価プロセスをカスタマイズ可能です。

## 結果の確認

評価を実行した後、Azure AI Foundryで詳細な評価指標のログを確認し、分析できます。  
アプリケーションの能力や限界についての洞察を得ることができます。

**注意** Azure AI Foundryは現在パブリックプレビュー段階のため、実験や開発目的での利用を推奨します。  
本番環境での利用には他の選択肢を検討してください。  
詳しい情報や手順については、公式の[AI Foundryドキュメント](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo)を参照してください。

**免責事項**：
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。


