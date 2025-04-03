<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "69d48385b1f1b31dd20dbb2405031bff",
  "translation_date": "2025-04-03T07:54:43+00:00",
  "source_file": "md\\02.Application\\04.Vision\\Phi3\\E2E_OpenVino_Phi3Vision.md",
  "language_code": "zh"
}
-->
本示例展示了如何使用预训练模型根据图像和文本提示生成Python代码。

[示例代码](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

以下是逐步的说明：

1. **导入和设置**：
   - 导入必要的库和模块，包括用于图像处理的`requests`和`PIL`，以及用于处理模型和数据的`transformers`。

2. **加载和显示图像**：
   - 使用`PIL`库打开图像文件(`demo.png`)并显示。

3. **定义提示**：
   - 创建一条消息，包含图像以及生成Python代码的请求，要求处理图像并使用`plt`（matplotlib）保存图像。

4. **加载处理器**：
   - 从`out_dir`目录指定的预训练模型中加载`AutoProcessor`。该处理器负责处理文本和图像输入。

5. **创建提示**：
   - 使用`apply_chat_template`方法将消息格式化为适合模型的提示。

6. **处理输入**：
   - 将提示和图像处理为模型可以理解的张量。

7. **设置生成参数**：
   - 定义模型生成过程的参数，包括生成的新标记的最大数量以及是否对输出进行采样。

8. **生成代码**：
   - 模型根据输入和生成参数生成Python代码。使用`TextStreamer`处理输出，跳过提示和特殊标记。

9. **输出**：
   - 打印生成的代码，其中应包含按照提示要求处理图像并保存的Python代码。

本示例展示了如何使用OpenVino的预训练模型，根据用户输入和图像动态生成代码。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们尽力确保翻译的准确性，但请注意，自动翻译可能会包含错误或不准确之处。原始语言版本的文件应被视为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译导致的任何误解或错误解释，我们不承担责任。