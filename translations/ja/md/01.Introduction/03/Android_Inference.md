<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b909b4ac6465d33e81adb17df38deef3",
  "translation_date": "2025-04-04T12:00:01+00:00",
  "source_file": "md\\01.Introduction\\03\\Android_Inference.md",
  "language_code": "ja"
}
-->
# **AndroidでPhi-3の推論を行う**

AndroidデバイスでPhi-3-miniを使用して推論を行う方法を見ていきましょう。Phi-3-miniは、Microsoftが提供する新しいモデルシリーズで、大規模言語モデル（LLM）をエッジデバイスやIoTデバイスで展開できるようにします。

## Semantic Kernelと推論

[Semantic Kernel](https://github.com/microsoft/semantic-kernel)は、Azure OpenAI Service、OpenAIモデル、さらにはローカルモデルと互換性のあるアプリケーションを作成できるアプリケーションフレームワークです。Semantic Kernelを初めて使う方は、[Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)をご覧になることをお勧めします。

### Semantic Kernelを使用してPhi-3-miniにアクセスするには

Semantic KernelのHugging Face Connectorと組み合わせることができます。この[サンプルコード](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)を参照してください。

デフォルトでは、Hugging Face上のモデルIDに対応していますが、ローカルに構築したPhi-3-miniモデルサーバーにも接続できます。

### OllamaやLlamaEdgeを使用した量子化モデルの呼び出し

多くのユーザーは、モデルをローカルで実行するために量子化モデルを使用することを好みます。[Ollama](https://ollama.com/)や[LlamaEdge](https://llamaedge.com)を使用すると、さまざまな量子化モデルを個別に呼び出すことができます。

#### Ollama

`ollama run Phi-3`を直接実行するか、`.gguf`ファイルへのパスを指定した`Modelfile`を作成してオフラインで構成することができます。

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[サンプルコード](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

クラウドとエッジデバイスの両方で`.gguf`ファイルを使用したい場合は、LlamaEdgeが優れた選択肢です。開始するには、この[サンプルコード](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)を参照してください。

### Androidスマートフォンへのインストールと実行

1. **MLC Chatアプリ**（無料）をAndroidスマートフォンにダウンロードします。
2. APKファイル（148MB）をダウンロードし、デバイスにインストールします。
3. MLC Chatアプリを起動します。Phi-3-miniを含むAIモデルのリストが表示されます。

まとめると、Phi-3-miniはエッジデバイスで生成AIを活用するためのエキサイティングな可能性を提供します。Androidでその機能を探索し始めてみましょう。

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文（元の言語で書かれた文書）が正式な情報源として考慮されるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の利用に起因する誤解や誤認について、当方は一切の責任を負いません。