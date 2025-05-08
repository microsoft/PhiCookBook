<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-08T05:44:01+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "ja"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## 概要

Interactive Phi 3 Mini 4K Instruct Chatbot は、Microsoft Phi 3 Mini 4K instruct デモとテキストまたは音声入力で対話できるツールです。このチャットボットは、翻訳、天気情報、一般的な情報収集など、さまざまなタスクに利用できます。

### はじめに

このチャットボットを使うには、以下の手順に従ってください：

1. 新しい [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) を開きます。
2. ノートブックのメインウィンドウに、テキスト入力ボックスと「Send」ボタンがあるチャットボックスインターフェースが表示されます。
3. テキストベースのチャットボットを使う場合は、テキスト入力ボックスにメッセージを入力し、「Send」ボタンをクリックしてください。チャットボットはノートブック内で直接再生可能な音声ファイルで応答します。

**Note**: このツールはGPUと、音声認識および翻訳に使用される Microsoft Phi-3 と OpenAI Whisper モデルへのアクセスが必要です。

### GPU 要件

このデモを実行するには12GBのGPUメモリが必要です。

**Microsoft-Phi-3-Mini-4K instruct** デモのGPUでのメモリ要件は、入力データ（音声またはテキスト）のサイズ、翻訳に使用する言語、モデルの速度、GPUの利用可能メモリなど複数の要因によって変わります。

一般的に、WhisperモデルはGPU上での実行を想定しています。Whisperモデルを動かすための推奨最低GPUメモリは8GBですが、必要に応じてより多くのメモリも扱えます。

大量のデータや高頻度のリクエストを処理すると、より多くのGPUメモリが必要になったり、パフォーマンスに影響が出る場合があります。使用ケースに応じて異なる設定でテストし、メモリ使用状況を監視して最適な設定を見つけることをお勧めします。

## Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper の E2E サンプル

[Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) というタイトルのJupyterノートブックは、Microsoft Phi 3 Mini 4K instruct デモを使って音声またはテキスト入力からテキストを生成する方法を示しています。ノートブックにはいくつかの関数が定義されています：

1. `tts_file_name(text)`: 入力テキストに基づいて生成された音声ファイルの保存用ファイル名を生成する関数。
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Edge TTS API を使って、入力テキストのチャンクリストから音声ファイルを生成する関数。入力パラメータはチャンクリスト、話速、音声名、生成音声ファイルの保存先パスです。
1. `talk(input_text)`: Edge TTS API を使い、/content/audio ディレクトリのランダムなファイル名で音声ファイルを生成・保存する関数。入力パラメータは音声変換するテキストです。
1. `run_text_prompt(message, chat_history)`: Microsoft Phi 3 Mini 4K instruct デモを使い、メッセージ入力から音声ファイルを生成し、チャット履歴に追加する関数。
1. `run_audio_prompt(audio, chat_history)`: WhisperモデルAPIを使って音声ファイルをテキストに変換し、その結果を `run_text_prompt()` 関数に渡す関数。
1. このコードはGradioアプリを起動し、ユーザーがメッセージを入力するか音声ファイルをアップロードしてPhi 3 Mini 4K instruct デモと対話できるようにします。出力はアプリ内でテキストメッセージとして表示されます。

## トラブルシューティング

Cuda GPU ドライバーのインストール

1. Linuxアプリケーションが最新であることを確認してください

    ```bash
    sudo apt update
    ```

1. Cudaドライバーをインストールする

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. cudaドライバーの場所を登録する

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Nvidia GPUのメモリサイズを確認する（12GBのGPUメモリが必要）

    ```bash
    nvidia-smi
    ```

1. キャッシュを空にする: PyTorchを使用している場合は、torch.cuda.empty_cache() を呼び出して未使用のキャッシュメモリを解放し、他のGPUアプリケーションで使用できるようにします。

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cudaを確認する

    ```bash
    nvcc --version
    ```

1. Hugging Faceトークンを作成するために以下の手順を実行してください。

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
> 解決するには、ターミナル内で次のコマンドを入力してください。
>
> ```bash
> sudo ldconfig
> ```

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご了承ください。原文の母国語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じた誤解や誤訳について、一切の責任を負いかねます。