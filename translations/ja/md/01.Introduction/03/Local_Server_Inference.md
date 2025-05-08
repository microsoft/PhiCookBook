<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-05-08T05:56:44+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "ja"
}
-->
# **ローカルサーバーでの Phi-3 推論**

Phi-3 をローカルサーバーにデプロイできます。ユーザーは [Ollama](https://ollama.com) や [LM Studio](https://llamaedge.com) のソリューションを選択するか、自分でコードを書くことも可能です。Phi-3 のローカルサービスは [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) や [Langchain](https://www.langchain.com/) を通じて接続し、Copilot アプリケーションを構築できます。

## **Semantic Kernel を使って Phi-3-mini にアクセスする**

Copilot アプリケーションでは、Semantic Kernel や LangChain を通じてアプリケーションを作成します。この種のアプリケーションフレームワークは、一般的に Azure OpenAI Service や OpenAI モデルに対応しており、Hugging Face のオープンソースモデルやローカルモデルもサポート可能です。Semantic Kernel を使って Phi-3-mini にアクセスしたい場合はどうすればよいでしょうか？.NET を例に挙げると、Semantic Kernel の Hugging Face Connector と組み合わせることができます。デフォルトでは Hugging Face 上のモデル ID に対応しており（初回使用時は Hugging Face からモデルをダウンロードするため時間がかかります）、自分で構築したローカルサービスにも接続可能です。この二つを比較すると、特に企業向けアプリケーションでは、自律性が高い後者の利用を推奨します。

![sk](../../../../../translated_images/sk.d03785c25edc6d445a2e9ae037979e544e0b0c482f43c7617b0324e717b9af62.ja.png)

図のように、Semantic Kernel を通じてローカルサービスにアクセスすることで、自分で構築した Phi-3-mini モデルサーバーに簡単に接続できます。以下は実行結果です。

![skrun](../../../../../translated_images/skrun.5aafc1e7197dca2020eefcaeaaee184d29bb0cf1c37b00fd9c79acc23a6dc8d2.ja.png)

***Sample Code*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の言語によるオリジナル文書が権威ある情報源とみなされます。重要な情報については、専門の人間翻訳を推奨いたします。本翻訳の使用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。