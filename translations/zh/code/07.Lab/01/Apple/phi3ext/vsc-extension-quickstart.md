<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6a7479104914787e4f0976e39131e8e3",
  "translation_date": "2025-04-03T06:26:34+00:00",
  "source_file": "code\\07.Lab\\01\\Apple\\phi3ext\\vsc-extension-quickstart.md",
  "language_code": "zh"
}
-->
# 欢迎使用您的 VS Code 扩展

## 文件夹内容

* 此文件夹包含您的扩展所需的所有文件。
* `package.json` - 这是清单文件，您可以在其中声明您的扩展和命令。
  * 示例插件注册了一个命令，并定义了其标题和命令名称。通过这些信息，VS Code 可以在命令面板中显示该命令，但尚无需加载插件。
* `src/extension.ts` - 这是您提供命令实现的主文件。
  * 该文件导出一个函数 `activate`，它会在您的扩展首次被激活时调用（在本例中通过执行命令激活）。在 `activate` 函数内部，我们调用 `registerCommand`。
  * 我们将包含命令实现的函数作为第二个参数传递给 `registerCommand`。

## 设置

* 安装推荐的扩展 (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, 和 dbaeumer.vscode-eslint)。

## 立即开始运行

* 按 `F5` 打开一个加载了您的扩展的新窗口。
* 在命令面板中运行您的命令，方法是按下 (`Ctrl+Shift+P` 或 Mac 上的 `Cmd+Shift+P`)，然后输入 `Hello World`。
* 在 `src/extension.ts` 文件中设置断点以调试您的扩展。
* 在调试控制台中查看扩展的输出。

## 修改代码

* 修改 `src/extension.ts` 中的代码后，可以通过调试工具栏重新启动扩展。
* 您也可以重新加载 (`Ctrl+R` 或 Mac 上的 `Cmd+R`) VS Code 窗口以加载您的更改。

## 探索 API

* 打开文件 `node_modules/@types/vscode/index.d.ts`，可以查看我们的完整 API 集。

## 运行测试

* 安装 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 通过 **Tasks: Run Task** 命令运行 "watch" 任务。确保任务正在运行，否则可能无法发现测试。
* 从活动栏中打开测试视图，点击 "Run Test" 按钮，或使用快捷键 `Ctrl/Cmd + ; A`。
* 在测试结果视图中查看测试结果的输出。
* 修改 `src/test/extension.test.ts` 或在 `test` 文件夹内创建新的测试文件。
  * 提供的测试运行器仅会考虑文件名模式匹配 `**.test.ts` 的文件。
  * 您可以在 `test` 文件夹内创建文件夹，以任意方式组织您的测试。

## 更进一步

* 通过 [打包您的扩展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) 来减小扩展体积并优化启动时间。
* 在 VS Code 扩展市场上 [发布您的扩展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 通过设置 [持续集成](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) 来自动化构建流程。

**免责声明**:  
本文档使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文档的母语版本应被视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用此翻译而引起的任何误解或误读，我们概不负责。