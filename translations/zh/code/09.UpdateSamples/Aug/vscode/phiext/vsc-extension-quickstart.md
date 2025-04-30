<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6a7479104914787e4f0976e39131e8e3",
  "translation_date": "2025-04-03T06:31:35+00:00",
  "source_file": "code\\09.UpdateSamples\\Aug\\vscode\\phiext\\vsc-extension-quickstart.md",
  "language_code": "zh"
}
-->
# 欢迎使用您的 VS Code 扩展

## 文件夹内容

* 这个文件夹包含了您扩展所需的所有文件。
* `package.json` - 这是声明扩展和命令的清单文件。
  * 示例插件注册了一个命令，并定义了其标题和命令名称。通过这些信息，VS Code 可以在命令面板中显示该命令，但暂时不需要加载插件。
* `src/extension.ts` - 这是您实现命令的主文件。
  * 该文件导出了一个函数 `activate`，它会在您的扩展首次激活时被调用（例如通过执行命令激活）。在 `activate` 函数内部，我们调用了 `registerCommand`。
  * 我们将包含命令实现的函数作为第二个参数传递给 `registerCommand`。

## 设置

* 安装推荐的扩展（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner 和 dbaeumer.vscode-eslint）。

## 立即开始运行

* 按 `F5` 打开一个加载了您的扩展的新窗口。
* 在命令面板中运行您的命令，按下 (`Ctrl+Shift+P` 或 Mac 上的 `Cmd+Shift+P`) 并输入 `Hello World`。
* 在 `src/extension.ts` 中设置断点以调试您的扩展。
* 在调试控制台中找到您的扩展输出。

## 进行修改

* 修改 `src/extension.ts` 中的代码后，您可以通过调试工具栏重新启动扩展。
* 您也可以重新加载 (`Ctrl+R` 或 Mac 上的 `Cmd+R`) VS Code 窗口以加载您的更改。

## 探索 API

* 打开文件 `node_modules/@types/vscode/index.d.ts` 即可查看完整的 API 集。

## 运行测试

* 安装 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)。
* 通过 **Tasks: Run Task** 命令运行 "watch" 任务。确保任务正在运行，否则测试可能无法被发现。
* 从活动栏打开测试视图，点击“运行测试”按钮，或使用快捷键 `Ctrl/Cmd + ; A`。
* 在测试结果视图中查看测试结果输出。
* 修改 `src/test/extension.test.ts` 或在 `test` 文件夹中创建新的测试文件。
  * 提供的测试运行器只会考虑名称模式匹配 `**.test.ts` 的文件。
  * 您可以在 `test` 文件夹中创建子文件夹，以任何您喜欢的方式组织测试。

## 深入了解

* 通过 [打包您的扩展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) 来减少扩展大小并提升启动速度。
* 在 VS Code 扩展市场上 [发布您的扩展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 设置 [持续集成](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) 来自动化构建过程。

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。应以原文档的母语版本作为权威来源。对于关键性信息，建议使用专业的人类翻译服务。因使用本翻译而引起的任何误解或误读，我们概不负责。