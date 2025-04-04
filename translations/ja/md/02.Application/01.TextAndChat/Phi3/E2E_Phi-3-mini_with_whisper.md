<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f737bf207e1691cdc654535c48dd2df4",
  "translation_date": "2025-04-04T12:41:15+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_Phi-3-mini_with_whisper.md",
  "language_code": "ja"
}
-->
# インタラクティブ Phi 3 Mini 4K Instruct Chatbot with Whisper

## 概要

インタラクティブ Phi 3 Mini 4K Instruct Chatbotは、Microsoft Phi 3 Mini 4K instructデモとテキストまたは音声入力でやり取りできるツールです。このチャットボットは、翻訳、天気情報の更新、一般的な情報収集など、さまざまなタスクに使用できます。

### はじめに

このチャットボットを使用するには、以下の手順に従ってください：

1. [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) を開きます。
2. ノートブックのメインウィンドウには、テキスト入力ボックスと「送信」ボタンを備えたチャットボックスインターフェースが表示されます。
3. テキストベースのチャットボットを使用するには、テキスト入力ボックスにメッセージを入力し、「送信」ボタンをクリックします。チャットボットは、ノートブック内で直接再生可能な音声ファイルで応答します。

**注**: このツールを使用するには、GPUとMicrosoft Phi-3およびOpenAI Whisperモデルへのアクセスが必要です。これらは音声認識と翻訳に使用されます。

### GPU要件

このデモを実行するには、12GBのGPUメモリが必要です。

**Microsoft-Phi-3-Mini-4K instruct**デモをGPU上で実行する際のメモリ要件は、入力データのサイズ（音声またはテキスト）、使用言語、モデルの速度、およびGPUの利用可能なメモリなど、いくつかの要因に依存します。

一般に、WhisperモデルはGPU上での実行を前提に設計されています。このモデルを実行するための推奨最小GPUメモリは8GBですが、必要に応じてより大容量のメモリにも対応できます。

大量のデータや高いリクエスト量でモデルを実行すると、より多くのGPUメモリが必要になったり、パフォーマンスに影響を与える可能性があります。さまざまな構成でユースケースをテストし、メモリ使用量を監視して、特定のニーズに最適な設定を決定することをお勧めします。

## Whisperを使用したインタラクティブ Phi 3 Mini 4K Instruct ChatbotのE2Eサンプル

[Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)というタイトルのJupyterノートブックでは、Microsoft Phi 3 Mini 4K instructデモを使用して、音声またはテキスト入力からテキストを生成する方法を示しています。このノートブックでは、以下のいくつかの関数が定義されています：

1. `tts_file_name(text)`: 入力テキストに基づいて生成された音声ファイルを保存するためのファイル名を生成します。
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Edge TTS APIを使用して、入力テキストのチャンクリストから音声ファイルを生成します。入力パラメータには、チャンクリスト、話速、音声名、および生成された音声ファイルを保存する出力パスが含まれます。
1. `talk(input_text)`: Edge TTS APIを使用して音声ファイルを生成し、/content/audioディレクトリ内のランダムなファイル名に保存します。入力パラメータは、音声に変換する入力テキストです。
1. `run_text_prompt(message, chat_history)`: Microsoft Phi 3 Mini 4K instructデモを使用してメッセージ入力から音声ファイルを生成し、それをチャット履歴に追加します。
1. `run_audio_prompt(audio, chat_history)`: WhisperモデルAPIを使用して音声ファイルをテキストに変換し、それを`run_text_prompt()`関数に渡します。
1. コードはGradioアプリを起動し、ユーザーがPhi 3 Mini 4K instructデモとメッセージを入力するか音声ファイルをアップロードすることでやり取りできるようにします。出力はアプリ内にテキストメッセージとして表示されます。

## トラブルシューティング

Cuda GPUドライバーのインストール

1. Linuxアプリケーションが最新であることを確認します。

    ```bash
    sudo apt update
    ```

1. Cudaドライバーをインストールします。

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Cudaドライバーの場所を登録します。

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Nvidia GPUメモリサイズを確認します（12GBのGPUメモリが必要）。

    ```bash
    nvidia-smi
    ```

1. キャッシュのクリア: PyTorchを使用している場合、torch.cuda.empty_cache()を呼び出して、未使用のキャッシュメモリを解放し、他のGPUアプリケーションで使用できるようにします。

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cudaを確認します。

    ```bash
    nvcc --version
    ```

1. 以下の手順でHugging Faceトークンを作成します。

    - [Hugging Face Token Settingsページ](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo) に移動します。
    - **New token**を選択します。
    - 使用したいプロジェクトの**名前**を入力します。
    - **タイプ**を**Write**に設定します。

> **注**
>
> 以下のエラーが発生した場合：
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> 解決するには、ターミナル内で以下のコマンドを入力してください：
>
> ```bash
> sudo ldconfig
> ```

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご理解ください。原文（元の言語の文書）が公式な情報源として考慮されるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用により生じた誤解や誤解釈について、当社は責任を負いません。