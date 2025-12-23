<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-12-21T15:59:35+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "pcm"
}
-->
# Welcome to your VS Code Extension

## Wetin dey for di folder

* Dis folder get all di files wey you need for your extension.
* `package.json` - na di manifest file wey you declare your extension and command.
  * Di sample plugin dey register one command an dey define im title and command name. Wit dis info VS Code fit show di command for di command palette. E no need load di plugin yet.
* `src/extension.ts` - na di main file where you go provide di implementation of your command.
  * Di file dey export one function, `activate`, wey dem go call di very first time your extension dey activated (for dis case by executing di command). Inside di `activate` function we call `registerCommand`.
  * We pass di function wey contain di implementation of di command as di second parameter to `registerCommand`.

## Setup

* install di recommended extensions (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, and dbaeumer.vscode-eslint)


## Get up and running straight away

* Press `F5` to open a new window wey get your extension loaded.
* Run your command from the command palette by pressing (`Ctrl+Shift+P` or `Cmd+Shift+P` on Mac) and typing `Hello World`.
* Put breakpoints for your code inside `src/extension.ts` make you fit debug your extension.
* You go find output from your extension for di debug console.

## Make changes

* You fit relaunch the extension from the debug toolbar after you don change code for `src/extension.ts`.
* You fit also reload (`Ctrl+R` or `Cmd+R` on Mac) di VS Code window wey get your extension to load your changes.


## Explore the API

* You fit open di full set of our API when you open di file `node_modules/@types/vscode/index.d.ts`.

## Run tests

* Install di [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Run di "watch" task via di **Tasks: Run Task** command. Make sure dis dey running, or tests fit no be discovered.
* Open di Testing view from di activity bar and click di Run Test" button, or use di hotkey `Ctrl/Cmd + ; A`
* See di output of di test result for di Test Results view.
* Make changes to `src/test/extension.test.ts` or create new test files inside di `test` folder.
  * Di provided test runner go only consider files wey match di name pattern `**.test.ts`.
  * You fit create folders inside di `test` folder to structure your tests any how you want.

## Go further

* Reduce di extension size an improve di startup time by [bundling your extension](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Publish your extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) on di VS Code extension marketplace.
* Make builds automatic by setting up [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis dokument don translate by AI translation service Co-op Translator (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg note say automated translations fit get errors or no too accurate. Di original dokument for im original language na di authoritative source. If na important matter, make you use professional human translator. We no go responsible for any misunderstanding or wrong interpretation wey fit follow from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->