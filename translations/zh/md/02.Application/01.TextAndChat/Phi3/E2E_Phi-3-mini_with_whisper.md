<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f737bf207e1691cdc654535c48dd2df4",
  "translation_date": "2025-04-03T07:33:48+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_Phi-3-mini_with_whisper.md",
  "language_code": "zh"
}
-->
# 互动式 Phi 3 Mini 4K 指令聊天机器人与 Whisper

## 概述

互动式 Phi 3 Mini 4K 指令聊天机器人是一款工具，允许用户通过文本或语音输入与 Microsoft Phi 3 Mini 4K 指令演示进行交互。该聊天机器人可用于多种任务，例如翻译、天气更新以及信息收集。

### 入门指南

要使用此聊天机器人，请按照以下步骤操作：

1. 打开 [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)。
2. 在 notebook 的主界面中，你会看到一个带有文本输入框和“发送”按钮的聊天界面。
3. 要使用基于文本的聊天机器人，只需在文本输入框中输入消息，然后点击“发送”按钮。聊天机器人会以音频文件形式回复，你可以直接在 notebook 中播放该音频。

**注意**：此工具需要 GPU，并访问 Microsoft Phi-3 和 OpenAI Whisper 模型，这些模型用于语音识别和翻译。

### GPU 要求

运行此演示需要 12GB 的 GPU 内存。

运行 **Microsoft-Phi-3-Mini-4K 指令**演示所需的 GPU 内存取决于多个因素，例如输入数据的大小（音频或文本）、翻译所使用的语言、模型的速度以及 GPU 的可用内存。

通常，Whisper 模型设计为在 GPU 上运行。运行 Whisper 模型推荐的最低 GPU 内存为 8 GB，但如果需要，它可以处理更大的内存。

需要注意的是，运行大量数据或高请求量可能需要更多 GPU 内存，并可能导致性能问题。建议根据不同配置测试你的用例，并监控内存使用情况，以确定适合你具体需求的最佳设置。

## 互动式 Phi 3 Mini 4K 指令聊天机器人与 Whisper 的端到端示例

标题为 [互动式 Phi 3 Mini 4K 指令聊天机器人与 Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) 的 Jupyter Notebook 展示了如何使用 Microsoft Phi 3 Mini 4K 指令演示从音频或文本输入生成文本。Notebook 定义了以下几个函数：

1. `tts_file_name(text)`：此函数根据输入文本生成文件名，用于保存生成的音频文件。
2. `edge_free_tts(chunks_list,speed,voice_name,save_path)`：此函数使用 Edge TTS API 从输入文本片段列表生成音频文件。输入参数包括片段列表、语速、语音名称和保存生成音频文件的输出路径。
3. `talk(input_text)`：此函数通过 Edge TTS API 生成音频文件，并将其保存到 /content/audio 目录中的随机文件名。输入参数是要转换为语音的文本。
4. `run_text_prompt(message, chat_history)`：此函数使用 Microsoft Phi 3 Mini 4K 指令演示从消息输入生成音频文件，并将其添加到聊天记录中。
5. `run_audio_prompt(audio, chat_history)`：此函数使用 Whisper 模型 API 将音频文件转换为文本，并将其传递给 `run_text_prompt()` 函数。
6. 代码启动了一个 Gradio 应用程序，允许用户通过输入消息或上传音频文件与 Phi 3 Mini 4K 指令演示进行交互。输出以文本消息形式显示在应用程序中。

## 故障排除

安装 Cuda GPU 驱动程序

1. 确保你的 Linux 应用程序是最新的

    ```bash
    sudo apt update
    ```

2. 安装 Cuda 驱动程序

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

3. 注册 Cuda 驱动程序位置

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

4. 检查 Nvidia GPU 内存大小（需要 12GB GPU 内存）

    ```bash
    nvidia-smi
    ```

5. 清空缓存：如果你使用的是 PyTorch，可以调用 torch.cuda.empty_cache() 来释放所有未使用的缓存内存，以便其他 GPU 应用程序使用。

    ```python
    torch.cuda.empty_cache() 
    ```

6. 检查 Nvidia Cuda

    ```bash
    nvcc --version
    ```

7. 执行以下任务以创建 Hugging Face 令牌：

    - 访问 [Hugging Face Token 设置页面](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo)。
    - 选择 **New token**。
    - 输入你想使用的项目 **名称**。
    - 将 **类型** 设置为 **Write**。

> **注意**
>
> 如果你遇到以下错误：
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> 要解决此问题，请在终端中输入以下命令：
>
> ```bash
> sudo ldconfig
> ```

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于重要信息，建议使用专业人工翻译。我们对于因使用此翻译而导致的任何误解或错误解释不承担责任。