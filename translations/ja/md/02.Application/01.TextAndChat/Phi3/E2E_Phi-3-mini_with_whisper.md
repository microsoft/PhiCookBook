<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f72d7981ed3640865700f51ae407da4",
  "translation_date": "2026-01-14T15:19:55+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "ja"
}
-->
# インタラクティブPhi 3 Mini 4Kインストラクションチャットボット with Whisper

## 概要

インタラクティブPhi 3 Mini 4Kインストラクションチャットボットは、ユーザーがテキストまたは音声入力を使ってMicrosoft Phi 3 Mini 4Kインストラクションデモとやり取りできるツールです。このチャットボットは、翻訳、天気情報、一般情報収集など、さまざまなタスクに利用できます。

### はじめに

このチャットボットを使うには、以下の手順に従ってください：

1. 新しい [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) を開く  
2. ノートブックのメインウィンドウに、テキスト入力ボックスと「Send」ボタンがあるチャットボックスインターフェイスが表示されます。  
3. テキストベースのチャットボットを使うには、テキスト入力ボックスにメッセージを入力し、「Send」ボタンをクリックします。チャットボットはノートブック内で直接再生できるオーディオファイルで応答します。

**注意**：このツールはGPUとMicrosoft Phi-3およびOpenAI Whisperモデル（音声認識および翻訳に使用）へのアクセスが必要です。

### GPU要件

このデモを実行するには12GBのGPUメモリが必要です。

**Microsoft-Phi-3-Mini-4K instruct**デモをGPU上で実行する際のメモリ要件は、入力データ（音声またはテキスト）のサイズ、翻訳に使用する言語、モデルの速度およびGPUの利用可能なメモリなど複数の要因に依存します。

一般的に、WhisperモデルはGPU上での実行を想定しています。Whisperモデルを実行するための推奨最低GPUメモリは8GBですが、必要に応じてより大きなメモリも扱えます。

大量のデータや高頻度のリクエストをモデルで処理する場合は、より多くのGPUメモリが必要になるか、パフォーマンスの問題が発生する可能性があります。異なる設定でユースケースのテストを行い、メモリ使用量を監視して特定のニーズに最適な設定を決定することをお勧めします。

## Whisper搭載インタラクティブPhi 3 Mini 4KインストラクションチャットボットのE2Eサンプル

[Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) というタイトルのJupyterノートブックは、Microsoft Phi 3 Mini 4K instructデモを使って音声または書かれたテキスト入力からテキストを生成する方法を示しています。ノートブックにはいくつかの関数が定義されています：

1. `tts_file_name(text)`: 入力テキストに基づいて生成された音声ファイルを保存するためのファイル名を生成します。  
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Edge TTS APIを使用して、入力テキストのチャンクリストから音声ファイルを生成します。入力パラメータはチャンクのリスト、音声速度、音声名、生成した音声ファイルの保存パスです。  
1. `talk(input_text)`: Edge TTS APIを使い、入力テキストを音声に変換して/content/audioディレクトリのランダムなファイル名で保存します。  
1. `run_text_prompt(message, chat_history)`: Microsoft Phi 3 Mini 4K instructデモを使ってメッセージ入力から音声ファイルを生成し、チャット履歴に追加します。  
1. `run_audio_prompt(audio, chat_history)`: WhisperモデルAPIを使用して音声ファイルをテキストに変換し、その結果を`run_text_prompt()`関数に渡します。  
1. このコードはGradioアプリを起動し、ユーザーがメッセージを入力するか音声ファイルをアップロードしてPhi 3 Mini 4K instructデモと対話できるようにします。出力はアプリ内にテキストメッセージとして表示されます。

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
  
1. キャッシュのクリア：PyTorchを使用している場合は、torch.cuda.empty_cache()を呼び出して未使用のキャッシュメモリを解放し、他のGPUアプリケーションで利用可能にします

    ```python
    torch.cuda.empty_cache() 
    ```
  
1. Nvidia Cudaを確認します

    ```bash
    nvcc --version
    ```
  
1. Hugging Faceトークンを作成するには以下の作業を行います。

    - [Hugging Faceトークン設定ページ](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo)にアクセスします。  
    - **New token**を選択します。  
    - 使用したいプロジェクトの**Name**を入力します。  
    - **Type**を**Write**に選択します。

> [!NOTE]
>
> 以下のエラーが発生した場合：
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> これを解決するには、ターミナル内で次のコマンドを入力してください。  
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な表現が含まれる可能性があります。原文の言語による文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じたいかなる誤解や誤訳についても当社は一切責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->