<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:33:08+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "ja"
}
-->
﻿## C#で使うPhiラボへようこそ

.NET環境で強力なPhiモデルのさまざまなバージョンを統合する方法を紹介するラボがいくつか用意されています。

## 前提条件

サンプルを実行する前に、以下がインストールされていることを確認してください：

**.NET 9:** マシンに[最新の.NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo)がインストールされていることを確認してください。

**（任意）Visual Studio または Visual Studio Code:** .NETプロジェクトを実行できるIDEまたはコードエディタが必要です。[Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo)または[Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo)がおすすめです。

**gitを使って** [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c)から利用可能なPhi-3、Phi3.5、またはPhi-4のいずれかのバージョンをローカルにクローンしてください。

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

**重要:** 現在のデモはモデルのONNXバージョンを使用するように設計されています。上記の手順で以下のモデルがクローンされます。

## ラボについて

メインのソリューションには、C#でPhiモデルの機能を示すいくつかのサンプルラボがあります。

| プロジェクト | モデル | 説明 |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 または Phi-3.5 | ユーザーが質問できるサンプルコンソールチャット。`Microsoft.ML.OnnxRuntime`ライブラリを使ってローカルのONNX Phi-3モデルを読み込みます。 |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 または Phi-3.5 | ユーザーが質問できるサンプルコンソールチャット。`Microsoft.Semantic.Kernel`ライブラリを使ってローカルのONNX Phi-3モデルを読み込みます。 |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 または Phi-3.5 | ローカルのphi3 visionモデルを使って画像を解析するサンプルプロジェクト。`Microsoft.ML.OnnxRuntime`ライブラリを使ってローカルのONNX Phi-3 Visionモデルを読み込みます。 |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 または Phi-3.5 | ローカルのphi3 visionモデルを使って画像を解析するサンプルプロジェクト。`Microsoft.ML.OnnxRuntime`ライブラリを使ってローカルのONNX Phi-3 Visionモデルを読み込みます。ユーザーと対話するためのメニューも表示します。 | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | ユーザーが質問できるサンプルコンソールチャット。`Microsoft.ML.OnnxRuntime`ライブラリを使ってローカルのONNX Phi-4モデルを読み込みます。 |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | ユーザーが質問できるサンプルコンソールチャット。`Semantic Kernel`ライブラリを使ってローカルのONNX Phi-4モデルを読み込みます。 |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | ユーザーが質問できるサンプルコンソールチャット。`Microsoft.ML.OnnxRuntimeGenAI`ライブラリを使ってローカルのONNX Phi-4モデルを読み込み、`Microsoft.Extensions.AI`の`IChatClient`を実装しています。 |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | ユーザーが質問できるサンプルコンソールチャット。チャットにメモリ機能を実装しています。 |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | ローカルのPhi-4モデルを使って画像を解析し、結果をコンソールに表示するサンプルプロジェクト。`Microsoft.ML.OnnxRuntime`ライブラリを使ってローカルのPhi-4-`multimodal-instruct-onnx`モデルを読み込みます。 |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | ローカルのPhi-4モデルを使って音声ファイルを解析し、文字起こしを生成してコンソールに表示するサンプルプロジェクト。`Microsoft.ML.OnnxRuntime`ライブラリを使ってローカルのPhi-4-`multimodal-instruct-onnx`モデルを読み込みます。 |

## プロジェクトの実行方法

プロジェクトを実行するには、以下の手順に従ってください：

1. リポジトリをローカルマシンにクローンします。

1. ターミナルを開き、実行したいプロジェクトのフォルダに移動します。例として、`LabsPhi4-Chat-01OnnxRuntime`を実行します。

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. 次のコマンドでプロジェクトを実行します。

    ```bash
    dotnet run
    ```

1. サンプルプロジェクトはユーザー入力を求め、ローカルモデルを使って応答します。

   実行中のデモは以下のようなものです：

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。