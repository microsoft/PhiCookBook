# Interactive Phi 3 Mini 4K 指令聊天機械人搭配 Whisper

## 概覽

Interactive Phi 3 Mini 4K 指令聊天機械人是一個工具，讓用戶可以透過文字或語音輸入與 Microsoft Phi 3 Mini 4K 指令示範互動。該聊天機械人可用於多種任務，例如翻譯、天氣更新及一般資訊蒐集。

### 快速開始

使用此聊天機械人，請依照以下指示：

1. 開啟新的 [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. 在筆記本的主要視窗中，您會看到一個帶有文字輸入框和「Send」按鈕的聊天介面。
3. 若要使用文字聊天機械人，只需將訊息輸入文字框，然後點擊「Send」按鈕。聊天機械人會回覆一個音訊檔案，您可以直接在筆記本中播放。

**注意**：此工具需要 GPU 及存取 Microsoft Phi-3 與 OpenAI Whisper 模型，用於語音識別和翻譯。

### GPU 要求

要執行此示範，您需要 12GB GPU 記憶體。

執行 **Microsoft-Phi-3-Mini-4K instruct** 示範在 GPU 上所需的記憶體會依據多項因素而有所不同，例如輸入資料（語音或文字）的大小、翻譯使用的語言、模型速度以及 GPU 可用記憶體。

一般而言，Whisper 模型設計用於在 GPU 上運行。建議執行 Whisper 模型的最低 GPU 記憶體為 8 GB，但若需要亦可處理更大容量的記憶體。

值得注意的是，處理大量資料或高頻請求時，模型可能需要更多 GPU 記憶體和/或可能導致效能問題。建議您針對您的使用情況測試不同設定並監控記憶體使用，以決定最適設定。

## Interactive Phi 3 Mini 4K 指令聊天機械人搭配 Whisper 的 E2E 範例

名為 [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) 的 jupyter 筆記本示範如何使用 Microsoft Phi 3 Mini 4K 指令示範，從語音或文字輸入產生文字。筆記本定義了多個函數：

1. `tts_file_name(text)`: 此函數根據輸入文字生成用於儲存產生語音檔案的檔名。
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: 此函數使用 Edge TTS API 從一串文字切片生成音訊檔案。輸入參數為字串切片列表、語速、語音名稱與輸出路徑來儲存音訊檔案。
1. `talk(input_text)`: 此函數使用 Edge TTS API 產生語音檔案並存到 /content/audio 目錄下一個隨機檔名。輸入參數為欲轉語音的文字。
1. `run_text_prompt(message, chat_history)`: 此函數使用 Microsoft Phi 3 Mini 4K 指令示範，從訊息輸入產生音訊檔並附加至聊天記錄。
1. `run_audio_prompt(audio, chat_history)`: 此函數使用 Whisper 模型 API 將音訊檔轉成文字，再傳遞給 `run_text_prompt()` 函數。
1. 程式碼啟動 Gradio 應用，讓用戶可藉由輸入文字訊息或上傳音訊檔與 Phi 3 Mini 4K 指令示範互動。輸出結果以文字訊息形式呈現在應用中。

## 疑難排解

安裝 Cuda GPU 驅動程式

1. 確保您的 Linux 應用程式已更新至最新版本

    ```bash
    sudo apt update
    ```

1. 安裝 Cuda 驅動程式

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. 登記 cuda 驅動程式位置

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. 檢查 Nvidia GPU 記憶體大小（需 12GB GPU 記憶體）

    ```bash
    nvidia-smi
    ```

1. 清空快取：如果您正在使用 PyTorch，可以呼叫 torch.cuda.empty_cache() 來釋放所有未使用的快取記憶體，供其他 GPU 應用程式使用

    ```python
    torch.cuda.empty_cache() 
    ```

1. 檢查 Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. 執行以下步驟以建立 Hugging Face 令牌：

    - 前往 [Hugging Face Token Settings 頁面](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo)。
    - 選擇 **New token**。
    - 輸入您想使用的專案 **Name**。
    - 選擇 **Type** 為 **Write**。

> [!NOTE]
>
> 若您遇到以下錯誤：
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> 解決方式是，在您的終端機內輸入以下指令。
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件經由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應視為具權威性的資料來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而導致的任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->