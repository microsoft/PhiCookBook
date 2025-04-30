<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f737bf207e1691cdc654535c48dd2df4",
  "translation_date": "2025-04-04T18:20:26+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_Phi-3-mini_with_whisper.md",
  "language_code": "hk"
}
-->
# 互動式 Phi 3 Mini 4K 指導聊天機器人配合 Whisper

## 概覽

互動式 Phi 3 Mini 4K 指導聊天機器人是一個工具，讓用戶可以使用文字或語音輸入與 Microsoft Phi 3 Mini 4K 指導示範進行互動。這個聊天機器人可用於多種任務，例如翻譯、天氣更新和一般信息收集。

### 開始使用

要使用這個聊天機器人，請按照以下指示：

1. 打開新的 [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. 在筆記本的主窗口中，您會看到一個聊天框界面，帶有文字輸入框和“發送”按鈕。
3. 要使用基於文字的聊天機器人，只需在文字輸入框中輸入您的消息，然後點擊“發送”按鈕。聊天機器人將以音頻文件回應，並可直接在筆記本中播放。

**注意**：此工具需要 GPU 並訪問 Microsoft Phi-3 和 OpenAI Whisper 模型，用於語音識別和翻譯。

### GPU 要求

運行此示範需要 12GB 的 GPU 記憶。

運行 **Microsoft-Phi-3-Mini-4K 指導**示範所需的 GPU 記憶將取決於多種因素，例如輸入數據的大小（音頻或文字）、翻譯使用的語言、模型的速度以及 GPU 的可用記憶。

一般來說，Whisper 模型設計為在 GPU 上運行。運行 Whisper 模型所需的最低 GPU 記憶建議為 8GB，但如果需要，它可以處理更大的記憶量。

請注意，運行大量數據或高頻率請求可能需要更多 GPU 記憶，並可能導致性能問題。建議使用不同配置測試您的使用情況，並監控記憶使用情況，以確定適合您特定需求的最佳設置。

## 互動式 Phi 3 Mini 4K 指導聊天機器人配合 Whisper 的 E2E 示例

名為 [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) 的 Jupyter 筆記本展示了如何使用 Microsoft Phi 3 Mini 4K 指導示範，通過音頻或文字輸入生成文字。筆記本定義了幾個函數：

1. `tts_file_name(text)`：此函數根據輸入文字生成文件名，用於保存生成的音頻文件。
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`：此函數使用 Edge TTS API 從輸入文字的塊列表生成音頻文件。輸入參數包括塊列表、語速、語音名稱和保存生成音頻文件的輸出路徑。
1. `talk(input_text)`：此函數使用 Edge TTS API 生成音頻文件，並保存到 /content/audio 目錄中的隨機文件名。輸入參數是要轉換為語音的輸入文字。
1. `run_text_prompt(message, chat_history)`：此函數使用 Microsoft Phi 3 Mini 4K 指導示範，從消息輸入生成音頻文件並將其附加到聊天記錄中。
1. `run_audio_prompt(audio, chat_history)`：此函數使用 Whisper 模型 API 將音頻文件轉換為文字，並將其傳遞給 `run_text_prompt()` 函數。
1. 此代碼啟動了一個 Gradio 應用，允許用戶通過輸入消息或上傳音頻文件與 Phi 3 Mini 4K 指導示範進行互動。輸出以文本消息形式顯示在應用內。

## 疑難排解

安裝 Cuda GPU 驅動程序

1. 確保您的 Linux 應用已更新

    ```bash
    sudo apt update
    ```

1. 安裝 Cuda 驅動程序

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. 註冊 Cuda 驅動程序位置

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. 檢查 Nvidia GPU 記憶大小（需要 12GB 的 GPU 記憶）

    ```bash
    nvidia-smi
    ```

1. 清空緩存：如果您使用 PyTorch，可以調用 torch.cuda.empty_cache() 釋放所有未使用的緩存記憶，以便其他 GPU 應用使用。

    ```python
    torch.cuda.empty_cache() 
    ```

1. 檢查 Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. 執行以下任務以創建 Hugging Face 令牌。

    - 前往 [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo)。
    - 選擇 **New token**。
    - 輸入您想使用的項目 **Name**。
    - 將 **Type** 設為 **Write**。

> **注意**
>
> 如果您遇到以下錯誤：
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> 為了解決此問題，請在終端中輸入以下命令：
>
> ```bash
> sudo ldconfig
> ```

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於重要信息，建議使用專業的人類翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。