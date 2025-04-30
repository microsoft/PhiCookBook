<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0e3a4453db505856d5d991285dd6001",
  "translation_date": "2025-04-04T13:38:50+00:00",
  "source_file": "md\\04.HOL\\dotnet\\readme.md",
  "language_code": "ja"
}
-->
## Phi Labs C#へようこそ

.NET環境で強力なPhiモデルのさまざまなバージョンを統合する方法を紹介する複数のラボがあります。

## 前提条件

サンプルを実行する前に、以下がインストールされていることを確認してください：

**.NET 9:** [最新バージョンの.NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo)をお使いのマシンにインストールしてください。

**（任意）Visual StudioまたはVisual Studio Code:** .NETプロジェクトを実行可能なIDEまたはコードエディタが必要です。[Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo)または[Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo)をお勧めします。

**gitを使用して** Phi-3、Phi-3.5、またはPhi-4バージョンのいずれかを[Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c)からローカルにクローンしてください。

**Phi-4 ONNXモデルをダウンロード**してローカルマシンに保存します：

### モデルを保存するフォルダに移動

```bash
cd c:\phi\models
```

### lfsのサポートを追加

```bash
git lfs install 
```

### Phi-4 mini instructモデルとPhi-4マルチモーダルモデルをクローンしてダウンロード

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNXモデルをダウンロード**してローカルマシンに保存します：

### Phi-3 mini 4K instructモデルとPhi-3 vision 128Kモデルをクローンしてダウンロード

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**重要:** 現在のデモはONNXバージョンのモデルを使用するよう設計されています。上記の手順で以下のモデルがクローンされます。

## ラボについて

メインのソリューションには、C#を使用してPhiモデルの機能を実証する複数のサンプルラボが含まれています。

| プロジェクト | モデル | 説明 |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3またはPhi-3.5 | ユーザーが質問できるサンプルコンソールチャット。このプロジェクトは、`Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-3 model using the `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Semantic Kernel` libraries. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntimeGenAI` libraries and implements the `IChatClient` from `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Sample console chat that allows the user to ask questions. The chat implements memory. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | This is a sample project that uses a local Phi-4 model to analyze images showing the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 |This is a sample project that uses a local Phi-4 model to analyze an audio file, generate the transcript of the file and show the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |

## How to Run the Projects

To run the projects, follow these steps:

1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime`を使用してローカルONNX Phi-3モデルを読み込みます。

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. 以下のコマンドでプロジェクトを実行

    ```bash
    dotnet run
    ```

1. サンプルプロジェクトはユーザー入力を求め、ローカルモードを使用して応答します。

   実行中のデモは以下のようなものです：

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期するよう努めておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があります。原文の母国語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の利用により生じた誤解や誤認に関して、当方は一切の責任を負いかねます。