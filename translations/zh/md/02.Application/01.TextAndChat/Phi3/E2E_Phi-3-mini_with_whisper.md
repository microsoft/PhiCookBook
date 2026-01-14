<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f72d7981ed3640865700f51ae407da4",
  "translation_date": "2026-01-14T15:11:26+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "zh"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## 概述

Interactive Phi 3 Mini 4K Instruct Chatbot 是一个允许用户使用文本或音频输入与 Microsoft Phi 3 Mini 4K 指令演示进行交互的工具。该聊天机器人可用于多种任务，例如翻译、天气更新和一般信息收集。

### 入门指南

要使用此聊天机器人，只需按照以下说明操作：

1. 打开一个新的 [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. 在笔记本主窗口中，您会看到一个带有文本输入框和“发送”按钮的聊天框界面。
3. 要使用基于文本的聊天机器人，只需在文本输入框中输入您的消息并点击“发送”按钮。聊天机器人将以音频文件形式响应，可以直接在笔记本中播放。

**注意**：该工具需要 GPU 和对 Microsoft Phi-3 及 OpenAI Whisper 模型的访问权限，后者用于语音识别和翻译。

### GPU 要求

运行此演示需要 12GB 的 GPU 内存。

运行 **Microsoft-Phi-3-Mini-4K instruct** 演示所需的 GPU 内存取决于多个因素，例如输入数据的大小（音频或文本）、用于翻译的语言、模型的速度以及 GPU 上的可用内存。

通常，Whisper 模型设计用于在 GPU 上运行。推荐运行 Whisper 模型的最低 GPU 内存为 8 GB，但如果需要，也可以支持更大的内存。

需要注意的是，处理大量数据或高并发请求时，可能需要更多的 GPU 内存和/或可能导致性能问题。建议针对您的使用场景测试不同配置，并监控内存使用情况，以确定特定需求的最佳设置。

## 交互式 Phi 3 Mini 4K Instruct Chatbot with Whisper 的端到端示例

名为 [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) 的 Jupyter 笔记本演示了如何使用 Microsoft Phi 3 Mini 4K 指令演示从音频或文本输入生成文本。笔记本定义了多个函数：

1. `tts_file_name(text)`: 根据输入文本生成文件名，用于保存生成的音频文件。
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: 使用 Edge TTS API 从输入文本块列表生成音频文件。输入参数是块列表、语速、语音名称和输出路径。
1. `talk(input_text)`: 通过 Edge TTS API 生成音频文件，并保存到 /content/audio 目录的随机文件名中。输入参数是要转换为语音的文本。
1. `run_text_prompt(message, chat_history)`: 使用 Microsoft Phi 3 Mini 4K 指令演示根据消息输入生成音频文件，并将其追加到聊天记录中。
1. `run_audio_prompt(audio, chat_history)`: 使用 Whisper 模型 API 将音频文件转换为文本，并传递给 `run_text_prompt()` 函数。
1. 代码启动一个 Gradio 应用，允许用户通过输入文本消息或上传音频文件与 Phi 3 Mini 4K 指令演示进行交互。输出结果作为文本消息显示在应用内。

## 故障排除

安装 Cuda GPU 驱动

1. 确保您的 Linux 应用程序已更新

    ```bash
    sudo apt update
    ```

1. 安装 Cuda 驱动

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. 注册 cuda 驱动路径

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. 检查 Nvidia GPU 内存大小（需 12GB GPU 内存）

    ```bash
    nvidia-smi
    ```

1. 清空缓存：如果您使用 PyTorch，可以调用 torch.cuda.empty_cache() 释放所有未使用的缓存内存，以供其他 GPU 应用使用

    ```python
    torch.cuda.empty_cache() 
    ```

1. 检查 Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. 执行以下操作创建 Hugging Face 令牌。

    - 访问 [Hugging Face 令牌设置页面](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo)。
    - 选择 **New token**。
    - 输入您想使用的项目名称。
    - 将 **Type** 选择为 **Write**。

> [!NOTE]
>
> 如果您遇到以下错误：
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> 解决方法是在终端输入以下命令。
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或误译，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->