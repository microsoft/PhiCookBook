<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-08T05:44:13+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "tw"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## 概覽

Interactive Phi 3 Mini 4K Instruct Chatbot 是一個工具，讓使用者能透過文字或語音輸入與 Microsoft Phi 3 Mini 4K instruct 示範互動。這個聊天機器人可以用於多種任務，例如翻譯、天氣更新和一般資訊查詢。

### 快速開始

要使用這個聊天機器人，只要按照以下步驟操作：

1. 開啟新的 [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. 在筆記本的主視窗中，你會看到一個帶有文字輸入框和「Send」按鈕的聊天介面。
3. 若要使用文字聊天機器人，只要在文字輸入框輸入訊息，然後點擊「Send」按鈕。聊天機器人會回覆一個可以直接在筆記本中播放的音訊檔案。

**Note**：此工具需要 GPU 以及 Microsoft Phi-3 和 OpenAI Whisper 模型的存取權限，這些模型用於語音辨識和翻譯。

### GPU 需求

執行此示範需要 12GB 的 GPU 記憶體。

執行 **Microsoft-Phi-3-Mini-4K instruct** 示範時，GPU 記憶體需求會依多種因素而異，例如輸入資料大小（音訊或文字）、翻譯語言、模型速度以及 GPU 可用記憶體。

一般來說，Whisper 模型是設計用於 GPU 運行。建議執行 Whisper 模型的最低 GPU 記憶體為 8 GB，但如果需要也能支援更大容量。

需要注意的是，處理大量資料或高頻率請求時，可能需要更多 GPU 記憶體，或可能會造成效能問題。建議根據實際使用情況測試不同設定，並監控記憶體使用情況，以找出最佳配置。

## Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper 的 E2E 範例

這個名為 [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) 的 Jupyter 筆記本示範如何使用 Microsoft Phi 3 Mini 4K instruct Demo 從音訊或文字輸入產生文字。筆記本定義了幾個函式：

1. `tts_file_name(text)`：此函式根據輸入文字產生檔名，用來儲存產生的音訊檔案。
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`：此函式使用 Edge TTS API，從多段輸入文字清單產生音訊檔案。輸入參數包含文字段落清單、語速、聲音名稱，以及儲存音訊檔案的路徑。
1. `talk(input_text)`：此函式利用 Edge TTS API 產生音訊檔案，並將其儲存在 /content/audio 目錄下的隨機檔名中。輸入參數是要轉成語音的文字。
1. `run_text_prompt(message, chat_history)`：此函式使用 Microsoft Phi 3 Mini 4K instruct demo，從訊息輸入產生音訊檔案，並將結果加入聊天紀錄。
1. `run_audio_prompt(audio, chat_history)`：此函式使用 Whisper 模型 API 將音訊檔轉成文字，並將結果傳給 `run_text_prompt()` 函式。
1. 這段程式碼啟動一個 Gradio 應用，讓使用者可以透過輸入訊息或上傳音訊檔與 Phi 3 Mini 4K instruct demo 互動。輸出會以文字訊息顯示在應用中。

## 疑難排解

安裝 Cuda GPU 驅動程式

1. 確保你的 Linux 系統是最新版本

    ```bash
    sudo apt update
    ```

1. 安裝 Cuda 驅動程式

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. 註冊 cuda 驅動程式路徑

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. 檢查 Nvidia GPU 記憶體大小（需要 12GB GPU 記憶體）

    ```bash
    nvidia-smi
    ```

1. 清空快取：如果你使用 PyTorch，可以呼叫 torch.cuda.empty_cache() 釋放所有未使用的快取記憶體，讓其他 GPU 應用程式能使用

    ```python
    torch.cuda.empty_cache() 
    ```

1. 檢查 Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. 執行以下步驟以建立 Hugging Face token。

    - 前往 [Hugging Face Token 設定頁面](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo)。
    - 選擇 **New token**。
    - 輸入你想使用的專案 **Name**。
    - 選擇 **Type** 為 **Write**。

> **Note**
>
> 如果你遇到以下錯誤：
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> 解決方法是在終端機輸入以下指令。
>
> ```bash
> sudo ldconfig
> ```

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不精確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所引起之任何誤解或誤譯負責。