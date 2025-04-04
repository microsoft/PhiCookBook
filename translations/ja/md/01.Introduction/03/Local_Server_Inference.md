<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "12c0d9afaa23861ad5be655fcff4f71d",
  "translation_date": "2025-04-04T12:05:58+00:00",
  "source_file": "md\\01.Introduction\\03\\Local_Server_Inference.md",
  "language_code": "ja"
}
-->
# **ローカルサーバーでのPhi-3推論**

Phi-3をローカルサーバーにデプロイすることが可能です。ユーザーは、[Ollama](https://ollama.com)や[LM Studio](https://llamaedge.com)のソリューションを選択するか、自分自身でコードを書くことができます。[Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo)や[Langchain](https://www.langchain.com/)を通じてPhi-3のローカルサービスに接続し、Copilotアプリケーションを構築できます。

## **Semantic Kernelを使用してPhi-3-miniにアクセスする**

Copilotアプリケーションでは、Semantic KernelやLangChainを使用してアプリケーションを作成します。この種のアプリケーションフレームワークは、Azure OpenAI Service / OpenAIモデルと互換性があり、Hugging Faceのオープンソースモデルやローカルモデルにも対応可能です。では、Semantic Kernelを使用してPhi-3-miniにアクセスするにはどうすればよいでしょうか？.NETを例にすると、Semantic KernelのHugging Face Connectorと組み合わせて使用することができます。デフォルトでは、Hugging Face上のモデルIDに対応します（初回使用時にはモデルがHugging Faceからダウンロードされるため、時間がかかります）。また、構築したローカルサービスに接続することも可能です。この2つを比較すると、特に企業向けアプリケーションでは、後者を使用することを推奨します。後者の方が自律性が高いからです。

![sk](../../../../../translated_images/sk.c244b32f4811c6f0938b9e95b0b2f4b28105bff6495bdc3b24cd42b3e3e89bb9.ja.png)

図のように、Semantic Kernelを介してローカルサービスにアクセスすると、自分で構築したPhi-3-miniモデルサーバーに簡単に接続できます。以下はその実行結果です。

![skrun](../../../../../translated_images/skrun.fb7a635a22ae8b7919d6e15c0eb27262526ed69728c5a1d2773a97d4562657c7.ja.png)

***サンプルコード*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確さが含まれる可能性があります。元の言語で記載された文書が信頼できる正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用に起因する誤解や誤認について、当社は一切の責任を負いません。