<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "99474e9687279d0657412c806856b559",
  "translation_date": "2025-04-03T07:53:43+00:00",
  "source_file": "md\\02.Application\\04.Vision\\Phi3\\E2E_Nvidia_NIM_Vision.md",
  "language_code": "zh"
}
-->
### 示例场景

假设你有一张图片 (`demo.png`)，你希望生成处理这张图片并保存新版本的 Python 代码 (`phi-3-vision.jpg`)。

上面的代码通过以下步骤实现了这一过程：

1. 设置环境和必要的配置。
2. 创建一个提示，指示模型生成所需的 Python 代码。
3. 将提示发送给模型并收集生成的代码。
4. 提取并运行生成的代码。
5. 显示原始图片和处理后的图片。

这种方法利用了 AI 的强大能力来自动化图像处理任务，使实现目标变得更简单、更快捷。

[示例代码解决方案](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

让我们逐步拆解整个代码的功能：

1. **安装所需的包**：
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    该命令安装 `langchain_nvidia_ai_endpoints` 包，确保使用最新版本。

2. **导入必要的模块**：
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    这些导入引入了与 NVIDIA AI 端点交互、密码安全处理、操作系统交互以及 Base64 格式数据编码/解码所需的模块。

3. **设置 API 密钥**：
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    这段代码检查环境变量 `NVIDIA_API_KEY` 是否已设置。如果没有，则提示用户安全输入 API 密钥。

4. **定义模型和图片路径**：
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    这里设置了要使用的模型，创建了一个指定模型的 `ChatNVIDIA` 实例，并定义了图片文件的路径。

5. **创建文本提示**：
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    这段代码定义了一个文本提示，指示模型生成用于处理图片的 Python 代码。

6. **以 Base64 编码图片**：
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    这段代码读取图片文件，将其编码为 Base64，并创建一个包含编码数据的 HTML 图片标签。

7. **将文本和图片合并到提示中**：
    ```python
    prompt = f"{text} {image}"
    ```
    这段代码将文本提示和 HTML 图片标签合并为一个字符串。

8. **使用 ChatNVIDIA 生成代码**：
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    这段代码将提示发送给 `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` 字符串。

9. **从生成的内容中提取 Python 代码**：
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    这段代码通过移除 Markdown 格式，从生成的内容中提取实际的 Python 代码。

10. **运行生成的代码**：
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    这段代码以子进程运行提取的 Python 代码并捕获其输出。

11. **显示图片**：
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    这些代码行使用 `IPython.display` 模块显示图片。

**免责声明**:  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原文档的原始语言版本应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。