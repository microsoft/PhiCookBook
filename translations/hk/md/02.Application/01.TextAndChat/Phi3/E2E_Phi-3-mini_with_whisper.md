<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-08T05:43:50+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "hk"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## 概覽

Interactive Phi 3 Mini 4K Instruct Chatbot 係一個工具，讓用戶可以用文字或語音輸入同 Microsoft Phi 3 Mini 4K instruct demo 互動。呢個 chatbot 可以用嚟做唔同嘅任務，好似翻譯、天氣更新同一般資訊查詢。

### 快速開始

使用呢個 chatbot，只需要跟住以下步驟：

1. 開啟一個新嘅 [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. 喺 notebook 嘅主視窗，你會見到一個聊天框介面，有文字輸入框同「Send」按鈕。
3. 如果想用文字版 chatbot，只要喺文字輸入框打字，然後撳「Send」按鈕。chatbot 會回應一個可以喺 notebook 直接播放嘅音訊檔案。

**Note**：呢個工具需要 GPU 同 Microsoft Phi-3 同 OpenAI Whisper 模型嘅存取權限，用嚟做語音識別同翻譯。

### GPU 需求

要運行呢個 demo，你需要 12Gb 嘅 GPU 記憶體。

運行 **Microsoft-Phi-3-Mini-4K instruct** demo 嘅 GPU 記憶體需求會因多種因素而異，例如輸入資料大小（音訊或文字）、翻譯語言、模型速度同 GPU 可用記憶體。

一般嚟講，Whisper 模型係設計用嚟喺 GPU 上運行。建議嘅最低 GPU 記憶體係 8 GB，但如果需要，可以支援更大嘅記憶體。

要注意係，如果處理大量資料或者大量請求，可能需要更多 GPU 記憶體，或者可能會影響效能。建議用戶用唔同設定測試，並監察記憶體使用情況，搵出最適合自己需求嘅設定。

## Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper 嘅 E2E 範例

呢個名為 [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) 嘅 jupyter notebook 示範點樣用 Microsoft Phi 3 Mini 4K instruct Demo 由音訊或文字輸入產生文字。notebook 定義咗幾個函數：

1. `tts_file_name(text)`：根據輸入文字產生檔案名，用嚟儲存產生嘅音訊檔案。
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`：用 Edge TTS API 從一串文字片段產生音訊檔案。輸入參數包括文字片段清單、語速、語音名稱同輸出路徑。
1. `talk(input_text)`：用 Edge TTS API 產生音訊檔案，並儲存喺 /content/audio 目錄隨機檔案名。輸入係要轉成語音嘅文字。
1. `run_text_prompt(message, chat_history)`：用 Microsoft Phi 3 Mini 4K instruct demo 從輸入訊息產生音訊檔案，並加到聊天記錄。
1. `run_audio_prompt(audio, chat_history)`：用 Whisper 模型 API 將音訊檔案轉成文字，並傳遞畀 `run_text_prompt()` 函數。
1. 程式碼啟動咗一個 Gradio app，讓用戶可以打字或上載音訊檔案同 Phi 3 Mini 4K instruct demo 互動，輸出會喺 app 裡面以文字訊息顯示。

## 疑難排解

安裝 Cuda GPU 驅動程式

1. 確保你嘅 Linux 系統係最新嘅

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

1. 檢查 Nvidia GPU 記憶體大小（需要 12GB GPU 記憶體）

    ```bash
    nvidia-smi
    ```

1. 清除快取：如果你用緊 PyTorch，可以呼叫 torch.cuda.empty_cache() 釋放所有未用嘅快取記憶體，咁其他 GPU 程式都可以用到。

    ```python
    torch.cuda.empty_cache() 
    ```

1. 檢查 Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. 做以下步驟去建立 Hugging Face token。

    - 去 [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo)。
    - 選擇 **New token**。
    - 輸入你想用嘅專案 **Name**。
    - 將 **Type** 選成 **Write**。

> **Note**
>
> 如果你遇到以下錯誤：
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> 解決方法係喺終端機入以下指令。
>
> ```bash
> sudo ldconfig
> ```

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我哋致力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原文文件嘅母語版本應被視為權威來源。對於重要資料，建議採用專業人手翻譯。因使用本翻譯而引起嘅任何誤解或錯誤詮釋，我哋概不負責。