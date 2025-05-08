<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-05-08T05:01:50+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "ja"
}
-->
﻿## C#を使ったPhiラボへようこそ

.NET環境で強力なさまざまなバージョンのPhiモデルを統合する方法を紹介するラボの選択肢があります。

## 前提条件

サンプルを実行する前に、以下がインストールされていることを確認してください：

**.NET 9:** お使いのマシンに[最新の.NETバージョン](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo)がインストールされていることを確認してください。

**（任意）Visual StudioまたはVisual Studio Code:** .NETプロジェクトを実行できるIDEまたはコードエディタが必要です。[Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo)または[Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo)を推奨します。

**gitを使用して** [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c)からPhi-3、Phi3.5、またはPhi-4のいずれかのバージョンをローカルにクローンしてください。

**Phi-4 ONNXモデルを** ローカルマシンにダウンロードします：

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

**Phi-3 ONNXモデルを** ローカルマシンにダウンロードします：

### Phi-3 mini 4K instructモデルとPhi-3 vision 128Kモデルをクローンしてダウンロード

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**重要:** 現在のデモはモデルのONNXバージョンを使用するよう設計されています。上記の手順で以下のモデルがクローンされます。

## ラボについて

メインのソリューションには、C#でPhiモデルの機能を示すいくつかのサンプルラボがあります。

| プロジェクト | モデル | 説明 |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 または Phi-3.5 | ユーザーが質問できるサンプルのコンソールチャット。プロジェクトはローカルのONNX Phi-3モデルを`Microsoft.ML.OnnxRuntime` libraries. |
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

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime`を使って読み込みます。

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. 次のコマンドでプロジェクトを実行します

    ```bash
    dotnet run
    ```

1. サンプルプロジェクトはユーザーの入力を求め、ローカルモデルを使って応答します。

   実行中のデモは以下のようなものです：

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**免責事項**:  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご承知ください。原文の言語で記載されたオリジナル文書が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や解釈の相違について、当方は一切の責任を負いかねます。