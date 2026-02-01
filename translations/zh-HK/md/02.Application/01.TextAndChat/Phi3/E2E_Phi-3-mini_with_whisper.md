# Interactive Phi 3 Mini 4K 指令聊天機械人配合 Whisper

## 概覽

Interactive Phi 3 Mini 4K 指令聊天機械人是一個工具，允許用戶使用文字或音頻輸入與 Microsoft Phi 3 Mini 4K 指令演示進行互動。該聊天機械人可用於多種任務，例如翻譯、天氣更新以及一般資訊蒐集。

### 快速開始

要使用此聊天機械人，請依照以下說明操作：

1. 打開新的 [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. 在筆記本的主視窗中，您將看到一個聊天框介面，包含文字輸入框和「Send」按鈕。
3. 若要使用文字聊天機械人，只需在文字輸入框中輸入您的訊息，然後點擊「Send」按鈕。聊天機械人將回應一個音訊文件，可直接在筆記本內播放。

**注意**：此工具需要 GPU 以及對 Microsoft Phi-3 和 OpenAI Whisper 模型的存取權限，Whisper 模型用於語音識別與翻譯。

### GPU 要求

要運行此示範，您需要 12GB 的 GPU 記憶體。

執行 **Microsoft-Phi-3-Mini-4K 指令** 示範時的 GPU 記憶體需求取決於多項因素，例如輸入資料大小（音頻或文字）、翻譯語言、模型速度及 GPU 可用記憶體等。

一般而言，Whisper 模型設計為在 GPU 上運行。建議的最低 GPU 記憶體為 8 GB，但如果需要可支援更多記憶體。

請注意，若在模型上運行大量數據或高流量請求，可能需要更多 GPU 記憶體且可能導致效能問題。建議您使用不同配置測試您的用例，並監控記憶體使用情況，以確定最適合您需求的設定。

## Interactive Phi 3 Mini 4K 指令聊天機械人配合 Whisper 端到端範例

名為 [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) 的 Jupyter 筆記本示範了如何使用 Microsoft Phi 3 Mini 4K 指令演示，透過音訊或文字輸入產生文字。筆記本定義了數個函式：

1. `tts_file_name(text)`: 此函式根據輸入文字產生檔案名稱，用於保存生成的音訊文件。
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: 此函式使用 Edge TTS API 從一串文字片段生成音訊文件。輸入參數為文字片段清單、語速、聲音名稱及輸出檔案儲存路徑。
1. `talk(input_text)`: 此函式利用 Edge TTS API 生成音訊文件，並以隨機檔名保存於 /content/audio 資料夾。輸入參數為需轉換為語音的文字。
1. `run_text_prompt(message, chat_history)`: 此函式使用 Microsoft Phi 3 Mini 4K 指令演示根據輸入訊息生成音訊文件，並附加到聊天歷史紀錄中。
1. `run_audio_prompt(audio, chat_history)`: 此函式使用 Whisper 模型 API 將音訊文件轉成文字，並傳入 `run_text_prompt()` 函式處理。
1. 程式啟動 Gradio 應用，允許用戶透過輸入文字或上傳音訊文件與 Phi 3 Mini 4K 指令演示互動。輸出以文字訊息形式顯示在應用中。

## 疑難排解

安裝 Cuda GPU 驅動程式

1. 確保 Linux 應用程式已更新

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

1. 檢查 Nvidia GPU 記憶體大小（需 12GB GPU 記憶體）

    ```bash
    nvidia-smi
    ```

1. 清除快取：如果您使用 PyTorch，可以呼叫 torch.cuda.empty_cache() 釋放所有未使用的快取記憶體，讓其他 GPU 應用程式能使用

    ```python
    torch.cuda.empty_cache() 
    ```

1. 檢查 Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. 執行以下步驟以建立 Hugging Face 令牌。

    - 前往 [Hugging Face 令牌設定頁面](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo)。
    - 選擇 **New token**。
    - 輸入您想使用的專案 **名稱**。
    - 選擇 **類型** 為 **Write**。

> [!NOTE]
>
> 如果您遇到以下錯誤：
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> 要解決此問題，請在終端機中輸入以下指令。
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件乃使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原文應被視為具權威性的資料來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引致的任何誤解或錯誤詮釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->