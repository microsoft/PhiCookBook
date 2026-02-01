# Interactive Phi 3 Mini 4K Instruct 聊天機器人搭配 Whisper

## 概述

Interactive Phi 3 Mini 4K Instruct 聊天機器人是一個工具，允許用戶使用文字或語音輸入與 Microsoft Phi 3 Mini 4K 指令示範互動。該聊天機器人可用於各種任務，例如翻譯、天氣更新和一般資訊收集。

### 快速開始

要使用此聊天機器人，只需按照以下說明：

1. 開啟新的 [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. 在筆記本的主視窗中，您會看到一個帶有文字輸入框和「Send」按鈕的聊天框介面。
3. 若要使用基於文字的聊天機器人，只需在文字輸入框中鍵入您的訊息，然後點擊「Send」按鈕。聊天機器人將回應一個可以直接在筆記本中播放的音訊檔案。

**注意**：此工具需要 GPU 且能存取 Microsoft Phi-3 及 OpenAI Whisper 模型，此模型用於語音識別和翻譯。

### GPU 要求

執行此示範需要 12GB 的 GPU 記憶體。

在 GPU 上執行 **Microsoft-Phi-3-Mini-4K instruct** 示範的記憶體需求會依多種因素而異，例如輸入資料大小（音訊或文字）、翻譯所用語言、模型速度及 GPU 可用記憶體。

一般來說，Whisper 模型設計用於在 GPU 上執行。推薦的 Whisper 模型最低 GPU 記憶體為 8 GB，但如有需要可處理更大記憶體。

請注意，處理大量資料或高頻率請求可能需要更多 GPU 記憶體，並可能造成性能問題。建議您針對您的使用情況進行不同配置測試並監控記憶體使用，找出最佳設定。

## Interactive Phi 3 Mini 4K Instruct 聊天機器人搭配 Whisper 的 E2E 範例

名為 [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) 的 Jupyter 筆記本示範如何使用 Microsoft Phi 3 Mini 4K instruct Demo 從音訊或文字輸入生成文字。該筆記本定義了多個函式：

1. `tts_file_name(text)`: 此函式根據輸入的文字產生檔案名稱，用來儲存產生的語音檔案。
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: 此函式使用 Edge TTS API，從文字片段列表產生語音檔案。輸入參數為片段列表、語速、語音名稱與輸出檔案儲存路徑。
1. `talk(input_text)`: 此函式利用 Edge TTS API 將輸入文字轉成語音並儲存至 /content/audio 目錄中的隨機檔名。輸入參數是要轉換成語音的文字。
1. `run_text_prompt(message, chat_history)`: 此函式使用 Microsoft Phi 3 Mini 4K instruct demo 從訊息輸入生成語音檔案，並將其附加到聊天紀錄中。
1. `run_audio_prompt(audio, chat_history)`: 此函式使用 Whisper 模型 API 將音訊檔轉成文字，然後傳給 `run_text_prompt()` 函式。
1. 程式碼啟動一個 Gradio 應用，允許用戶透過輸入文字訊息或上傳音訊檔與 Phi 3 Mini 4K instruct demo 互動，輸出將以文字訊息形式顯示於應用中。

## 疑難排解

安裝 Cuda GPU 驅動程式

1. 確保您的 Linux 應用程式是最新的

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

1. 清空快取：如果您使用 PyTorch，可以呼叫 torch.cuda.empty_cache() 釋放所有未使用的快取記憶體，以供其他 GPU 應用程式使用

    ```python
    torch.cuda.empty_cache() 
    ```

1. 檢查 Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. 執行以下步驟以建立 Hugging Face 代幣。

    - 前往 [Hugging Face Token 設定頁面](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo)。
    - 選擇 **New token**。
    - 輸入您想使用的專案 **名稱**。
    - 選擇 **Type** 為 **Write**。

> [!NOTE]
>
> 如果您遇到以下錯誤：
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> 解決方法是在終端機內輸入以下指令。
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提升準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原文文件應視為權威來源。對於重要資訊，建議採用專業人工翻譯。因使用此翻譯所導致的任何誤解或誤釋，我們概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->