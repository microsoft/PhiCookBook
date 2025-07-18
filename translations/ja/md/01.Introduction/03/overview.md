<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-07-16T21:08:03+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "ja"
}
-->
Phi-3-miniの文脈では、推論とはモデルを使って入力データに基づき予測や出力を生成するプロセスを指します。ここではPhi-3-miniとその推論機能について詳しく説明します。

Phi-3-miniはMicrosoftがリリースしたPhi-3シリーズの一部です。これらのモデルは、小型言語モデル（SLM）の可能性を再定義することを目的としています。

以下はPhi-3-miniとその推論機能に関する主なポイントです。

## **Phi-3-miniの概要:**
- Phi-3-miniは38億パラメータを持ちます。
- 従来のコンピューティングデバイスだけでなく、モバイルデバイスやIoTデバイスなどのエッジデバイスでも動作可能です。
- Phi-3-miniのリリースにより、個人や企業がリソース制約のある環境でもさまざまなハードウェア上でSLMを展開できるようになりました。
- 従来のPyTorch形式、gguf形式の量子化バージョン、ONNXベースの量子化バージョンなど、複数のモデル形式に対応しています。

## **Phi-3-miniへのアクセス:**
Phi-3-miniには、Copilotアプリケーションで[Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)を使ってアクセスできます。Semantic Kernelは一般的にAzure OpenAI Service、Hugging Faceのオープンソースモデル、ローカルモデルと互換性があります。  
また、[Ollama](https://ollama.com)や[LlamaEdge](https://llamaedge.com)を使って量子化モデルを呼び出すことも可能です。Ollamaは個人ユーザーがさまざまな量子化モデルを呼び出せる一方、LlamaEdgeはGGUFモデルのクロスプラットフォーム対応を提供します。

## **量子化モデル:**
多くのユーザーはローカル推論に量子化モデルを好んで使用します。例えば、Ollamaで直接Phi-3を実行したり、Modelfileを使ってオフラインで設定したりできます。ModelfileにはGGUFファイルのパスやプロンプト形式が指定されています。

## **生成AIの可能性:**
Phi-3-miniのようなSLMを組み合わせることで、生成AIの新たな可能性が広がります。推論はその第一歩に過ぎず、これらのモデルはリソース制約やレイテンシ制約、コスト制約のあるシナリオでさまざまなタスクに活用できます。

## **Phi-3-miniで生成AIを解き放つ：推論と展開のガイド**  
Semantic Kernel、Ollama/LlamaEdge、ONNX Runtimeを使ってPhi-3-miniモデルにアクセスし推論する方法を学び、さまざまなアプリケーションシナリオにおける生成AIの可能性を探りましょう。

**特徴**  
以下でphi3-miniモデルの推論が可能です：

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

まとめると、Phi-3-miniは開発者がさまざまなモデル形式を試し、さまざまなアプリケーションシナリオで生成AIを活用することを可能にします。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。