<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-07T14:11:14+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "zh"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## 概述

Interactive Phi 3 Mini 4K Instruct Chatbot 是一个工具，允许用户通过文本或语音输入与 Microsoft Phi 3 Mini 4K 指令演示进行交互。该聊天机器人可以用于多种任务，如翻译、天气更新和一般信息查询。

### 快速开始

使用此聊天机器人，只需按照以下步骤操作：

1. 打开新的 [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. 在笔记本的主窗口中，你会看到一个带有文本输入框和“Send”按钮的聊天框界面。
3. 要使用基于文本的聊天机器人，只需在文本输入框中输入消息，然后点击“Send”按钮。聊天机器人将以音频文件形式回应，音频文件可以直接在笔记本中播放。

**Note**：该工具需要 GPU 以及访问 Microsoft Phi-3 和 OpenAI Whisper 模型，这些模型用于语音识别和翻译。

### GPU 要求

运行此演示需要 12GB 的 GPU 内存。

运行 **Microsoft-Phi-3-Mini-4K instruct** 演示时所需的 GPU 内存取决于多个因素，比如输入数据的大小（音频或文本）、翻译所用语言、模型速度以及 GPU 上可用的内存。

一般来说，Whisper 模型设计用于在 GPU 上运行。运行 Whisper 模型的推荐最低 GPU 内存为 8 GB，但如果需要也能支持更大内存。

需要注意的是，处理大量数据或高请求量时，可能需要更多的 GPU 内存，且可能会导致性能问题。建议根据具体需求测试不同配置，并监控内存使用情况，以确定最佳设置。

## Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper 的端到端示例

名为 [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) 的 Jupyter 笔记本展示了如何使用 Microsoft Phi 3 Mini 4K 指令演示，从音频或文本输入生成文本。笔记本定义了几个函数：

1. `tts_file_name(text)`：根据输入文本生成文件名，用于保存生成的音频文件。
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`：使用 Edge TTS API 从一系列文本片段生成音频文件。输入参数包括文本片段列表、语速、语音名称和保存生成音频文件的路径。
1. `talk(input_text)`：通过 Edge TTS API 生成音频文件，并保存到 /content/audio 目录下的随机文件名。输入参数是要转换为语音的文本。
1. `run_text_prompt(message, chat_history)`：使用 Microsoft Phi 3 Mini 4K 指令演示，从消息输入生成音频文件，并将其添加到聊天记录中。
1. `run_audio_prompt(audio, chat_history)`：使用 Whisper 模型 API 将音频文件转换为文本，并将结果传递给 `run_text_prompt()` 函数。
1. 代码启动了一个 Gradio 应用，允许用户通过输入消息或上传音频文件与 Phi 3 Mini 4K 指令演示交互。输出以文本消息形式显示在应用内。

## 故障排除

安装 Cuda GPU 驱动

1. 确保你的 Linux 应用程序是最新的

    ```bash
    sudo apt update
    ```

1. 安装 Cuda 驱动

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. 注册 cuda 驱动位置

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. 检查 Nvidia GPU 内存大小（需要 12GB GPU 内存）

    ```bash
    nvidia-smi
    ```

1. 清理缓存：如果你使用 PyTorch，可以调用 torch.cuda.empty_cache() 来释放所有未使用的缓存内存，以供其他 GPU 应用使用

    ```python
    torch.cuda.empty_cache() 
    ```

1. 检查 Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. 执行以下操作以创建 Hugging Face 令牌。

    - 访问 [Hugging Face Token 设置页面](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo)。
    - 选择 **New token**。
    - 输入你想使用的项目 **Name**。
    - 将 **Type** 选择为 **Write**。

> **Note**
>
> 如果你遇到以下错误：
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> 解决方法是在终端中输入以下命令。
>
> ```bash
> sudo ldconfig
> ```

**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。尽管我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原始语言版本的文件应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们概不负责。