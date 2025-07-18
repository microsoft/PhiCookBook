<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-07-16T17:34:34+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "zh"
}
-->
# 欢迎使用您的 VS Code 扩展

## 文件夹内容

* 该文件夹包含扩展所需的所有文件。
* `package.json` - 这是清单文件，用于声明您的扩展和命令。
  * 示例插件注册了一个命令，并定义了其标题和命令名称。凭借这些信息，VS Code 可以在命令面板中显示该命令。此时还不需要加载插件。
* `src/extension.ts` - 这是主要文件，您将在这里实现命令的具体功能。
  * 该文件导出一个函数 `activate`，当扩展首次激活时（本例中是执行命令时）调用。在 `activate` 函数内部，我们调用了 `registerCommand`。
  * 我们将包含命令实现的函数作为第二个参数传递给 `registerCommand`。

## 设置

* 安装推荐的扩展（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner 和 dbaeumer.vscode-eslint）

## 立即开始使用

* 按 `F5` 打开一个加载了您扩展的新窗口。
* 通过按 (`Ctrl+Shift+P` 或 Mac 上的 `Cmd+Shift+P`) 并输入 `Hello World`，从命令面板运行您的命令。
* 在 `src/extension.ts` 中设置断点，调试您的扩展。
* 在调试控制台查看扩展的输出。

## 进行修改

* 修改 `src/extension.ts` 中的代码后，可以从调试工具栏重新启动扩展。
* 也可以通过重新加载 VS Code 窗口（`Ctrl+R` 或 Mac 上的 `Cmd+R`）来加载您的更改。

## 探索 API

* 打开文件 `node_modules/@types/vscode/index.d.ts`，即可查看完整的 API 集合。

## 运行测试

* 安装 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 通过 **Tasks: Run Task** 命令运行 “watch” 任务。确保该任务正在运行，否则测试可能无法被发现。
* 从活动栏打开测试视图，点击 “Run Test” 按钮，或使用快捷键 `Ctrl/Cmd + ; A`
* 在测试结果视图中查看测试输出。
* 修改 `src/test/extension.test.ts`，或在 `test` 文件夹内创建新的测试文件。
  * 提供的测试运行器只会识别符合 `**.test.ts` 命名模式的文件。
  * 您可以在 `test` 文件夹内创建子文件夹，自由组织测试结构。

## 深入了解

* 通过[打包您的扩展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)来减小扩展体积并提升启动速度。
* 在 VS Code 扩展市场[发布您的扩展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 通过设置[持续集成](https://code.visualstudio.com/api/working-with-extensions/continuous-integration)实现构建自动化。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。