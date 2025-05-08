<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-07T15:21:17+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "zh"
}
-->
# 欢迎使用您的 VS Code 扩展

## 文件夹内容

* 该文件夹包含您扩展所需的所有文件。
* `package.json` - 这是声明扩展和命令的清单文件。
  * 示例插件注册了一个命令，并定义了它的标题和命令名称。借助这些信息，VS Code 可以在命令面板中显示该命令。此时还不需要加载插件。
* `src/extension.ts` - 这是实现命令的主文件。
  * 该文件导出一个函数 `activate`，这是扩展首次激活时调用的函数（本例中通过执行命令激活）。在 `activate` 函数内部，我们调用了 `registerCommand`。
  * 我们将包含命令实现的函数作为第二个参数传递给 `registerCommand`。

## 设置

* 安装推荐的扩展（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner 和 dbaeumer.vscode-eslint）

## 立即开始使用

* 按 `F5` 打开一个加载了您的扩展的新窗口。
* 通过按 (`Ctrl+Shift+P` 或 Mac 上的 `Cmd+Shift+P`) 并输入 `Hello World`，从命令面板运行您的命令。
* 在 `src/extension.ts` 中设置断点以调试您的扩展。
* 在调试控制台查看扩展的输出。

## 修改代码

* 修改 `src/extension.ts` 中的代码后，可以从调试工具栏重新启动扩展。
* 您也可以通过重新加载 (`Ctrl+R` 或 Mac 上的 `Cmd+R`) VS Code 窗口来加载扩展的更改。

## 探索 API

* 打开 `node_modules/@types/vscode/index.d.ts` 文件即可查看完整的 API。

## 运行测试

* 安装 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 通过 **Tasks: Run Task** 命令运行“watch”任务。确保该任务正在运行，否则测试可能无法被发现。
* 从活动栏打开测试视图，点击“Run Test”按钮，或使用快捷键 `Ctrl/Cmd + ; A`。
* 在测试结果视图中查看测试输出。
* 修改 `src/test/extension.test.ts` 或在 `test` 文件夹中创建新的测试文件。
  * 提供的测试运行器只会识别匹配 `**.test.ts` 名称模式的文件。
  * 您可以在 `test` 文件夹内创建子文件夹，以任意方式组织测试。

## 进阶操作

* 通过[打包您的扩展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo)来减小扩展体积并提升启动速度。
* 在 VS Code 扩展市场[发布您的扩展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo)。
* 通过设置[持续集成](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo)实现自动构建。

**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。尽管我们力求准确，但请注意，自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。