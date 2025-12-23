<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-12-21T16:15:01+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "pcm"
}
-->
# Welkam to your VS Code Extension

## Wetin dey inside di folder

* Dis folder get all di files wey necessary for your extension.
* `package.json` - na di manifest file wey you go use declare your extension and command.
  * Di sample plugin dey register one command and e define im title and command name. Wit dis info VS Code fit show di command for di command palette. E no need load di plugin yet.
* `src/extension.ts` - na di main file wey you go provide di implementation of your command.
  * Di file exports one function, `activate`, wey dem go call di very first time your extension dey activated (for dis case by executing di command). Inside di `activate` function we call `registerCommand`.
  * We pass di function wey contain di implementation of di command as di second parameter to `registerCommand`.

## Setup

* install di recommended extensions (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, and dbaeumer.vscode-eslint)


## Make you start quick

* Press `F5` to open a new window wey your extension don load.
* Run your command from di command palette by pressing (`Ctrl+Shift+P` or `Cmd+Shift+P` on Mac) and typing `Hello World`.
* Set breakpoints for your code inside `src/extension.ts` to debug your extension.
* You fit find output from your extension for di debug console.

## Make changes

* You fit relaunch di extension from di debug toolbar after you change code in `src/extension.ts`.
* You fit also reload (`Ctrl+R` or `Cmd+R` on Mac) di VS Code window wey get your extension to load your changes.


## Explore di API

* You fit open di full set of our API when you open di file `node_modules/@types/vscode/index.d.ts`.

## Run tests

* Install the [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Run di "watch" task via di **Tasks: Run Task** command. Make sure say dis one dey run, or tests fit no get discovered.
* Open di Testing view from di activity bar and click di Run Test" button, or use di hotkey `Ctrl/Cmd + ; A`"
* See di output of di test result in di Test Results view.
* Make changes to `src/test/extension.test.ts` or create new test files inside di `test` folder.
  * Di provided test runner go only consider files wey match di name pattern `**.test.ts`.
  * You fit create folders inside di `test` folder to structure your tests any way you want.

## Go further

* Reduce di extension size and improve di startup time by [bundling your extension](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publish your extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) for di VS Code extension marketplace.
* Automate di builds by setting up [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document don translate with AI translation service [Co-op Translator] (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automated translations fit get mistakes or no too accurate. The original document for im native language na the authoritative source wey you suppose trust. If na critical information, better make professional human translator check or translate am. We no go take responsibility for any misunderstanding or misinterpretation wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->