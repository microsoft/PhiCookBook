<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-07-17T05:01:15+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "zh"
}
-->
本演示展示了如何使用预训练模型，根据图像和文本提示生成 Python 代码。

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

以下是逐步说明：

1. **导入和设置**：
   - 导入所需的库和模块，包括用于图像处理的 `requests`、`PIL`，以及用于模型和处理的 `transformers`。

2. **加载并显示图像**：
   - 使用 `PIL` 库打开图像文件（`demo.png`）并显示。

3. **定义提示**：
   - 创建一条消息，包含图像和请求生成用于处理图像并使用 `plt`（matplotlib）保存的 Python 代码。

4. **加载处理器**：
   - 从指定的 `out_dir` 目录加载预训练模型的 `AutoProcessor`。该处理器将处理文本和图像输入。

5. **创建提示**：
   - 使用 `apply_chat_template` 方法将消息格式化为适合模型的提示。

6. **处理输入**：
   - 将提示和图像处理成模型可理解的张量。

7. **设置生成参数**：
   - 定义模型生成过程的参数，包括最大生成新标记数和是否采样输出。

8. **生成代码**：
   - 模型根据输入和生成参数生成 Python 代码。使用 `TextStreamer` 处理输出，跳过提示和特殊标记。

9. **输出**：
   - 打印生成的代码，代码应包含用于处理图像并按提示保存的 Python 代码。

本演示说明了如何利用基于 OpenVino 的预训练模型，根据用户输入和图像动态生成代码。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们概不负责。