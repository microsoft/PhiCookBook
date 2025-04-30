<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f737bf207e1691cdc654535c48dd2df4",
  "translation_date": "2025-04-04T06:28:43+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_Phi-3-mini_with_whisper.md",
  "language_code": "tw"
}
-->
# 互動式 Phi 3 Mini 4K 指令聊天機器人與 Whisper

## 概述

互動式 Phi 3 Mini 4K 指令聊天機器人是一個工具，讓使用者可以使用文字或語音輸入與 Microsoft Phi 3 Mini 4K 指令演示進行互動。該聊天機器人可以用於各種任務，例如翻譯、天氣更新和一般資訊收集。

### 入門指南

要使用此聊天機器人，請按照以下步驟操作：

1. 開啟 [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. 在筆記本的主視窗中，你會看到一個聊天框介面，包含文字輸入框和「發送」按鈕。
3. 若要使用文字聊天機器人，只需在文字輸入框中輸入你的訊息並點擊「發送」按鈕。聊天機器人會回應一個音頻檔案，可直接在筆記本中播放。

**注意**：此工具需要 GPU 和 Microsoft Phi-3 以及 OpenAI Whisper 模型的存取權，這些模型用於語音識別和翻譯。

### GPU 要求

要運行此演示，你需要 12GB 的 GPU 記憶體。

運行 **Microsoft-Phi-3-Mini-4K 指令**演示所需的 GPU 記憶體取決於多種因素，例如輸入資料（音頻或文字）的大小、翻譯所用的語言、模型的速度以及 GPU 的可用記憶體。

一般來說，Whisper 模型設計為在 GPU 上運行。運行 Whisper 模型的建議最低 GPU 記憶體為 8 GB，但如果需要，可以處理更大的記憶體。

需要注意的是，若處理大量資料或高頻率的請求，可能需要更多的 GPU 記憶體，並可能導致性能問題。建議針對你的使用案例進行不同配置的測試，並監控記憶體使用情況，以確定最佳設定。

## 使用 Whisper 的互動式 Phi 3 Mini 4K 指令聊天機器人 E2E 範例

名為 [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) 的 Jupyter 筆記本展示如何使用 Microsoft Phi 3 Mini 4K 指令演示，通過音頻或文字輸入生成文字。該筆記本定義了以下幾個函數：

1. `tts_file_name(text)`：此函數根據輸入文字生成文件名，用於保存生成的音頻文件。
2. `edge_free_tts(chunks_list,speed,voice_name,save_path)`：此函數使用 Edge TTS API 從輸入文字塊列表生成音頻文件。輸入參數包括文字塊列表、語速、語音名稱以及保存音頻文件的輸出路徑。
3. `talk(input_text)`：此函數使用 Edge TTS API 生成音頻文件，並保存到 /content/audio 目錄中的隨機文件名。輸入參數是要轉換為語音的文字。
4. `run_text_prompt(message, chat_history)`：此函數使用 Microsoft Phi 3 Mini 4K 指令演示從訊息輸入生成音頻文件，並將其附加到聊天歷史中。
5. `run_audio_prompt(audio, chat_history)`：此函數使用 Whisper 模型 API 將音頻文件轉換為文字，並將文字傳遞給 `run_text_prompt()` 函數。
6. 該程式碼啟動了一個 Gradio 應用，讓使用者可以通過輸入文字訊息或上傳音頻文件與 Phi 3 Mini 4K 指令演示互動。輸出會以文字訊息形式顯示在應用中。

## 疑難排解

安裝 Cuda GPU 驅動

1. 確保你的 Linux 應用程式是最新的

    ```bash
    sudo apt update
    ```

2. 安裝 Cuda 驅動

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

3. 註冊 Cuda 驅動位置

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

4. 檢查 Nvidia GPU 記憶體大小（需要 12GB GPU 記憶體）

    ```bash
    nvidia-smi
    ```

5. 清空快取：如果你使用的是 PyTorch，可以呼叫 torch.cuda.empty_cache() 來釋放所有未使用的快取記憶體，讓其他 GPU 應用程式使用。

    ```python
    torch.cuda.empty_cache() 
    ```

6. 檢查 Nvidia Cuda

    ```bash
    nvcc --version
    ```

7. 執行以下步驟以建立 Hugging Face token。

    - 前往 [Hugging Face Token Settings 頁面](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo)。
    - 選擇 **New token**。
    - 輸入你想使用的專案 **名稱**。
    - 將 **類型** 選擇為 **Write**。

> **注意**
>
> 如果遇到以下錯誤：
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> 要解決此問題，請在終端中輸入以下命令：
>
> ```bash
> sudo ldconfig
> ```

**免責聲明**：  
本文檔使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能會包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。