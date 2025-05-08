<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-08T06:04:12+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "ja"
}
-->
Phi-3-miniの文脈では、推論とは入力データに基づいてモデルを使って予測や出力を生成するプロセスを指します。ここでは、Phi-3-miniとその推論機能について詳しく説明します。

Phi-3-miniはMicrosoftがリリースしたPhi-3シリーズの一部です。これらのモデルは、小規模言語モデル（SLM）の可能性を再定義することを目指して設計されています。

以下はPhi-3-miniとその推論機能に関する主なポイントです：

## **Phi-3-miniの概要：**
- Phi-3-miniは38億パラメータを持ちます。
- 従来のコンピューティングデバイスだけでなく、モバイルデバイスやIoTデバイスなどのエッジデバイスでも動作可能です。
- Phi-3-miniのリリースにより、個人や企業が特にリソース制約のある環境で異なるハードウェア上にSLMを展開できるようになりました。
- 従来のPyTorchフォーマット、量子化されたggufフォーマット、ONNXベースの量子化フォーマットなど、さまざまなモデルフォーマットに対応しています。

## **Phi-3-miniへのアクセス：**
Phi-3-miniにアクセスするには、Copilotアプリケーション内で[Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)を利用できます。Semantic Kernelは一般的にAzure OpenAI Service、Hugging Faceのオープンソースモデル、ローカルモデルと互換性があります。  
また、量子化モデルの呼び出しには[Ollama](https://ollama.com)や[LlamaEdge](https://llamaedge.com)も利用可能です。Ollamaは個人ユーザーがさまざまな量子化モデルを呼び出せる一方、LlamaEdgeはGGUFモデルのクロスプラットフォーム対応を提供します。

## **量子化モデルについて：**
多くのユーザーはローカル推論に量子化モデルを好んで使用します。例えば、Ollamaを使って直接Phi-3を実行したり、Modelfileでオフライン設定を行うことが可能です。ModelfileにはGGUFファイルのパスやプロンプト形式が指定されています。

## **生成AIの可能性：**
Phi-3-miniのようなSLMを組み合わせることで、生成AIの新たな可能性が広がります。推論は最初のステップに過ぎず、これらのモデルはリソース制約やレイテンシ制約、コスト制約のあるシナリオでさまざまなタスクに活用できます。

## **Phi-3-miniで生成AIを解き放つ：推論と展開のガイド**  
Semantic Kernel、Ollama/LlamaEdge、ONNX Runtimeを使ってPhi-3-miniモデルにアクセスし推論を行う方法を学び、さまざまなアプリケーションシナリオでの生成AIの可能性を探ります。

**特徴**  
以下でphi3-miniモデルの推論が可能です：

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

まとめると、Phi-3-miniは開発者がさまざまなモデルフォーマットを試し、さまざまなアプリケーションシナリオで生成AIを活用できるようにします。

**免責事項**：  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語で記載された元の文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。