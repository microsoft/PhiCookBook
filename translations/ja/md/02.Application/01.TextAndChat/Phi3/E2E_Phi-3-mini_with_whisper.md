<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:15:23+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "ja"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## 概要

Interactive Phi 3 Mini 4K Instruct Chatbotは、Microsoft Phi 3 Mini 4K instructデモとテキストまたは音声入力で対話できるツールです。このチャットボットは、翻訳、天気情報、一般的な情報収集など、さまざまなタスクに利用できます。

### はじめに

このチャットボットを使うには、以下の手順に従ってください：

1. 新しい [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) を開きます。
2. ノートブックのメインウィンドウに、テキスト入力ボックスと「Send」ボタンがあるチャットボックスインターフェースが表示されます。
3. テキストベースのチャットボットを使うには、テキスト入力ボックスにメッセージを入力し、「Send」ボタンをクリックしてください。チャットボットはノートブック内で直接再生可能な音声ファイルで応答します。

**Note**: このツールはGPUと、音声認識および翻訳に使用されるMicrosoft Phi-3およびOpenAI Whisperモデルへのアクセスが必要です。

### GPU要件

このデモを実行するには12GBのGPUメモリが必要です。

**Microsoft-Phi-3-Mini-4K instruct**デモをGPUで実行する際のメモリ要件は、入力データ（音声またはテキスト）のサイズ、翻訳に使用する言語、モデルの速度、GPUの利用可能メモリなど、いくつかの要因によって異なります。

一般的に、WhisperモデルはGPU上での実行を想定しています。Whisperモデルを動かすための推奨最低GPUメモリは8GBですが、必要に応じてより多くのメモリも扱えます。

大量のデータや高頻度のリクエストをモデルにかける場合、より多くのGPUメモリが必要になったり、パフォーマンスに影響が出る可能性があります。使用ケースに応じて異なる設定でテストし、メモリ使用量を監視して最適な設定を見つけることをお勧めします。

## Whisper対応 Interactive Phi 3 Mini 4K Instruct Chatbot のE2Eサンプル

[Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) というタイトルのJupyterノートブックは、Microsoft Phi 3 Mini 4K instructデモを使って音声またはテキスト入力からテキストを生成する方法を示しています。ノートブックには以下の関数が定義されています：

1. `tts_file_name(text)`: 入力テキストに基づいて生成される音声ファイルのファイル名を作成します。
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Edge TTS APIを使い、入力テキストのチャンクリストから音声ファイルを生成します。入力パラメータはチャンクリスト、話速、音声名、生成音声ファイルの保存パスです。
1. `talk(input_text)`: Edge TTS APIを使って音声ファイルを生成し、/content/audioディレクトリにランダムなファイル名で保存します。入力パラメータは音声変換するテキストです。
1. `run_text_prompt(message, chat_history)`: Microsoft Phi 3 Mini 4K instructデモを使い、メッセージ入力から音声ファイルを生成し、チャット履歴に追加します。
1. `run_audio_prompt(audio, chat_history)`: WhisperモデルAPIを使って音声ファイルをテキストに変換し、`run_text_prompt()`関数に渡します。
1. コードはGradioアプリを起動し、ユーザーがメッセージを入力したり音声ファイルをアップロードしてPhi 3 Mini 4K instructデモと対話できるようにします。出力はアプリ内でテキストメッセージとして表示されます。

## トラブルシューティング

Cuda GPUドライバーのインストール

1. Linuxアプリケーションが最新であることを確認してください

    ```bash
    sudo apt update
    ```

1. Cudaドライバーをインストールします

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. cudaドライバーの場所を登録します

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Nvidia GPUのメモリサイズを確認します（12GBのGPUメモリが必要）

    ```bash
    nvidia-smi
    ```

1. キャッシュのクリア：PyTorchを使用している場合は、torch.cuda.empty_cache()を呼び出して未使用のキャッシュメモリを解放し、他のGPUアプリケーションで使用できるようにします

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cudaの確認

    ```bash
    nvcc --version
    ```

1. Hugging Faceトークンを作成するために以下の手順を行います。

    - [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo) にアクセスします。
    - **New token** を選択します。
    - 使用したいプロジェクトの **Name** を入力します。
    - **Type** を **Write** に設定します。

> **Note**
>
> 以下のエラーが発生した場合：
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> 解決するには、ターミナルで以下のコマンドを入力してください。
>
> ```bash
> sudo ldconfig
> ```

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。