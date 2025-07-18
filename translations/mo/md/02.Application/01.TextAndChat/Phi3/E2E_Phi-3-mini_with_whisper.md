<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:14:38+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "mo"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## 概覽

Interactive Phi 3 Mini 4K Instruct Chatbot 是一個工具，讓使用者可以透過文字或語音輸入與 Microsoft Phi 3 Mini 4K instruct 示範進行互動。這個聊天機器人可用於多種任務，例如翻譯、天氣更新以及一般資訊查詢。

### 快速開始

使用此聊天機器人，只需按照以下步驟操作：

1. 開啟新的 [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. 在筆記本的主視窗中，你會看到一個聊天框介面，包含文字輸入框和「Send」按鈕。
3. 若要使用文字聊天機器人，只需在文字輸入框中輸入訊息，然後點擊「Send」按鈕。聊天機器人會回應一個音訊檔案，可直接在筆記本中播放。

**Note**：此工具需要 GPU 以及對 Microsoft Phi-3 和 OpenAI Whisper 模型的存取權限，Whisper 用於語音識別和翻譯。

### GPU 要求

執行此示範需要 12GB 的 GPU 記憶體。

執行 **Microsoft-Phi-3-Mini-4K instruct** 示範時，GPU 記憶體需求會依多種因素而異，例如輸入資料大小（音訊或文字）、翻譯語言、模型速度以及 GPU 可用記憶體。

一般來說，Whisper 模型是設計在 GPU 上運行的。建議執行 Whisper 模型的最低 GPU 記憶體為 8GB，但若需要也能支援更大記憶體。

需要注意的是，處理大量資料或高頻率請求時，可能需要更多 GPU 記憶體，或可能導致效能問題。建議針對你的使用情境進行不同配置的測試，並監控記憶體使用情況，以找出最適合的設定。

## Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper 的 E2E 範例

名為 [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) 的 Jupyter 筆記本示範如何使用 Microsoft Phi 3 Mini 4K instruct Demo 從音訊或文字輸入產生文字。筆記本定義了幾個函式：

1. `tts_file_name(text)`：根據輸入文字產生檔案名稱，用於儲存生成的音訊檔案。
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`：使用 Edge TTS API 從一串文字片段產生音訊檔案。輸入參數包含文字片段清單、語速、語音名稱，以及儲存生成音訊檔案的路徑。
1. `talk(input_text)`：使用 Edge TTS API 產生音訊檔案，並將其儲存到 /content/audio 目錄下的隨機檔名。輸入參數為要轉換成語音的文字。
1. `run_text_prompt(message, chat_history)`：使用 Microsoft Phi 3 Mini 4K instruct 示範從訊息輸入產生音訊檔案，並將結果附加到聊天記錄中。
1. `run_audio_prompt(audio, chat_history)`：使用 Whisper 模型 API 將音訊檔案轉換成文字，並傳遞給 `run_text_prompt()` 函式。
1. 程式碼啟動一個 Gradio 應用，讓使用者可以透過輸入訊息或上傳音訊檔與 Phi 3 Mini 4K instruct 示範互動。輸出會以文字訊息形式顯示在應用中。

## 疑難排解

安裝 Cuda GPU 驅動程式

1. 確保你的 Linux 系統已更新

    ```bash
    sudo apt update
    ```

1. 安裝 Cuda 驅動程式

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. 註冊 cuda 驅動程式位置

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. 檢查 Nvidia GPU 記憶體大小（需要 12GB GPU 記憶體）

    ```bash
    nvidia-smi
    ```

1. 清空快取：如果你使用 PyTorch，可以呼叫 torch.cuda.empty_cache() 釋放所有未使用的快取記憶體，讓其他 GPU 應用程式使用

    ```python
    torch.cuda.empty_cache() 
    ```

1. 檢查 Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. 執行以下步驟以建立 Hugging Face 令牌。

    - 前往 [Hugging Face Token Settings 頁面](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo)。
    - 選擇 **New token**。
    - 輸入你想使用的專案 **Name**。
    - 將 **Type** 設為 **Write**。

> **Note**
>
> 如果你遇到以下錯誤：
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> 解決方法是在終端機中輸入以下指令。
>
> ```bash
> sudo ldconfig
> ```

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。