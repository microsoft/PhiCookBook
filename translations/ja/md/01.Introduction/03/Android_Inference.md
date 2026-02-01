# **AndroidでのPhi-3推論**

AndroidデバイスでPhi-3-miniを使った推論方法を見ていきましょう。Phi-3-miniはMicrosoftの新しいモデルシリーズで、エッジデバイスやIoTデバイス上で大規模言語モデル（LLM）を展開できるように設計されています。

## Semantic Kernelと推論

[Semantic Kernel](https://github.com/microsoft/semantic-kernel)は、Azure OpenAI ServiceやOpenAIモデル、さらにはローカルモデルにも対応したアプリケーションを作成できるフレームワークです。Semantic Kernelを初めて使う方は、[Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)を参照することをおすすめします。

### Semantic KernelでPhi-3-miniにアクセスする方法

Semantic KernelのHugging Face Connectorと組み合わせて利用できます。こちらの[サンプルコード](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)を参考にしてください。

デフォルトではHugging Face上のモデルIDに対応していますが、ローカルで構築したPhi-3-miniモデルサーバーに接続することも可能です。

### OllamaやLlamaEdgeで量子化モデルを呼び出す

多くのユーザーはローカルでモデルを動かすために量子化モデルを利用しています。[Ollama](https://ollama.com/)や[LlamaEdge](https://llamaedge.com)は、個人ユーザーがさまざまな量子化モデルを呼び出せるようにしています。

#### Ollama

`ollama run Phi-3`を直接実行するか、`.gguf`ファイルのパスを記載した`Modelfile`を作成してオフラインで設定できます。

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[サンプルコード](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

クラウドとエッジデバイスの両方で`.gguf`ファイルを使いたい場合、LlamaEdgeが最適です。こちらの[サンプルコード](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)を参考にしてください。

### Androidスマホへのインストールと実行

1. Androidスマホ向けの無料アプリ「MLC Chat」をダウンロードします。  
2. APKファイル（148MB）をダウンロードしてデバイスにインストールします。  
3. MLC Chatアプリを起動すると、Phi-3-miniを含むAIモデルの一覧が表示されます。

まとめると、Phi-3-miniはエッジデバイス上での生成AIに新たな可能性をもたらし、Android上でその機能を手軽に試すことができます。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。