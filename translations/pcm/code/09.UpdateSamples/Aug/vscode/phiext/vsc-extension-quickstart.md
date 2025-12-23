<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-12-21T16:32:06+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "pcm"
}
-->
# Welcome to your VS Code Extension

## Wetin dey inside di folder

* Dis folder get all di files wey you need for your extension.
* `package.json` - na di manifest file wey you go declare your extension and command.
  * Di sample plugin dey register one command and define im title and command name. With dis information VS Code fit show di command for di command palette. E no still need to load di plugin yet.
* `src/extension.ts` - na di main file wey you go provide di implementation of your command.
  * Di file export one function, `activate`, wey dem go call di very first time wey your extension dey activated (for dis case by executing di command). Inside di `activate` function we dey call `registerCommand`.
  * We pass di function wey contain di implementation of di command as di second parameter to `registerCommand`.

## Setup

* Install di recommended extensions (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, and dbaeumer.vscode-eslint)


## Start quick

* Press `F5` to open a new window with your extension loaded.
* Run your command from di command palette by pressing (`Ctrl+Shift+P` or `Cmd+Shift+P` on Mac) and typing `Hello World`.
* Put breakpoints for your code inside `src/extension.ts` to debug your extension.
* You fit find output from your extension in the debug console.

## Make changes

* You fit relaunch the extension from the debug toolbar after you change code in `src/extension.ts`.
* You fit also reload (`Ctrl+R` or `Cmd+R` on Mac) the VS Code window with your extension to load your changes.


## Explore di API

* You fit open di full set of our API when you open the file `node_modules/@types/vscode/index.d.ts`.

## Run tests

* Install di [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Run di "watch" task via di **Tasks: Run Task** command. Make sure say dis one dey run, or tests no go fit get discovered.
* Open di Testing view from di activity bar and click di Run Test" button, or use the hotkey `Ctrl/Cmd + ; A`
* See di output of di test result in di Test Results view.
* Make changes to `src/test/extension.test.ts` or create new test files inside di `test` folder.
  * Di provided test runner go only consider files wey match di name pattern `**.test.ts`.
  * You fit create folders inside di `test` folder to organize your tests any way you want.

## Go further

* Reduce di extension size and improve di startup time by [bundling your extension](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publish your extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) on the VS Code extension marketplace.
* Automate builds by setting up [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi sey automated translations fit get mistakes or no dey fully accurate. Di original document for im native language na di main/authoritative source. If na important gist, we recommend make una use professional human translator. We no dey liable for any misunderstanding or wrong interpretation wey fit happen from using dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->