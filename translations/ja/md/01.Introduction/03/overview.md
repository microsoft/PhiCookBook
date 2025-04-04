<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d570fac7029d6697ad8ab1c963b43811",
  "translation_date": "2025-04-04T12:07:59+00:00",
  "source_file": "md\\01.Introduction\\03\\overview.md",
  "language_code": "ja"
}
-->
Phi-3-miniにおける推論とは、入力データに基づいてモデルを使用し、予測や出力を生成するプロセスを指します。ここでは、Phi-3-miniとその推論機能について詳しく説明します。

Phi-3-miniは、MicrosoftがリリースしたPhi-3シリーズのモデルの一部です。このシリーズは、小型言語モデル（SLM）の可能性を再定義することを目的としています。

以下は、Phi-3-miniとその推論機能に関する主なポイントです。

## **Phi-3-miniの概要:**
- Phi-3-miniのパラメータサイズは38億です。
- 従来のコンピューティングデバイスだけでなく、モバイルデバイスやIoTデバイスなどのエッジデバイスでも動作可能です。
- Phi-3-miniのリリースにより、個人や企業がSLMをさまざまなハードウェアデバイス、特にリソースが限られた環境で展開できるようになりました。
- モデル形式には、従来のPyTorch形式、量子化されたgguf形式、およびONNXベースの量子化バージョンが含まれています。

## **Phi-3-miniへのアクセス方法:**
Phi-3-miniにアクセスするには、Copilotアプリケーション内で[Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)を使用できます。Semantic Kernelは、Azure OpenAI Service、Hugging Face上のオープンソースモデル、ローカルモデルと一般的に互換性があります。
また、[Ollama](https://ollama.com)や[LlamaEdge](https://llamaedge.com)を使用して量子化モデルを呼び出すことも可能です。Ollamaは個々のユーザーが異なる量子化モデルを呼び出すことを可能にし、LlamaEdgeはGGUFモデルのクロスプラットフォーム対応を提供します。

## **量子化モデル:**
多くのユーザーはローカル推論のために量子化モデルを使用することを好みます。例えば、Ollamaを直接実行してPhi-3を使用したり、Modelfileを使用してオフラインで設定することができます。ModelfileはGGUFファイルのパスとプロンプト形式を指定します。

## **生成AIの可能性:**
Phi-3-miniのようなSLMを組み合わせることで、生成AIの新たな可能性が広がります。推論はその第一歩であり、これらのモデルはリソース制約、低遅延、コスト制約のあるシナリオでさまざまなタスクに利用できます。

## **Phi-3-miniで生成AIを解き放つ: 推論と展開のガイド**
Semantic Kernel、Ollama/LlamaEdge、ONNX Runtimeを使用してPhi-3-miniモデルにアクセスし、推論を行い、さまざまなアプリケーションシナリオで生成AIの可能性を探る方法を学びましょう。

**特徴**
Phi-3-miniモデルの推論を以下で実現:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

まとめると、Phi-3-miniは開発者がさまざまなモデル形式を探求し、生成AIをさまざまなアプリケーションシナリオで活用することを可能にします。

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご承知おきください。原文の母国語での文書が正式な情報源として考慮されるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。