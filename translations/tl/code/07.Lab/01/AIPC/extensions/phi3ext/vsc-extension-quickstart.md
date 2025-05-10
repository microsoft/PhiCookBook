<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-09T04:58:04+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "tl"
}
-->
# Maligayang pagdating sa iyong VS Code Extension

## Ano ang nasa folder

* Ang folder na ito ay naglalaman ng lahat ng mga file na kinakailangan para sa iyong extension.
* `package.json` - ito ang manifest file kung saan ide-declare mo ang iyong extension at command.
  * Ang sample plugin ay nagrerehistro ng isang command at tinutukoy ang title at pangalan ng command. Sa impormasyong ito, maipapakita ng VS Code ang command sa command palette. Hindi pa nito kailangang i-load ang plugin.
* `src/extension.ts` - ito ang pangunahing file kung saan mo ibibigay ang implementasyon ng iyong command.
  * Nag-e-export ang file ng isang function, `activate`, na tinatawag sa unang pagkakataon na na-activate ang iyong extension (sa kasong ito sa pagpapatakbo ng command). Sa loob ng `activate` function, tinatawag natin ang `registerCommand`.
  * Pinapasa natin ang function na naglalaman ng implementasyon ng command bilang pangalawang parameter sa `registerCommand`.

## Setup

* i-install ang mga inirerekomendang extension (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, at dbaeumer.vscode-eslint)

## Magsimula agad

* Pindutin ang `F5` para magbukas ng bagong window na naka-load ang iyong extension.
* Patakbuhin ang iyong command mula sa command palette sa pamamagitan ng pagpindot (`Ctrl+Shift+P` o `Cmd+Shift+P` sa Mac) at i-type ang `Hello World`.
* Maglagay ng breakpoints sa iyong code sa loob ng `src/extension.ts` para i-debug ang iyong extension.
* Hanapin ang output ng iyong extension sa debug console.

## Gumawa ng mga pagbabago

* Maaari mong i-relaunch ang extension mula sa debug toolbar pagkatapos baguhin ang code sa `src/extension.ts`.
* Maaari mo ring i-reload (`Ctrl+R` o `Cmd+R` sa Mac) ang VS Code window na may naka-load na extension para maipakita ang mga pagbabago.

## Tuklasin ang API

* Maaari mong buksan ang buong set ng aming API kapag binuksan mo ang file na `node_modules/@types/vscode/index.d.ts`.

## Patakbuhin ang mga tests

* I-install ang [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Patakbuhin ang "watch" task gamit ang **Tasks: Run Task** command. Siguraduhing tumatakbo ito, kung hindi ay maaaring hindi ma-detect ang mga tests.
* Buksan ang Testing view mula sa activity bar at pindutin ang "Run Test" button, o gamitin ang hotkey na `Ctrl/Cmd + ; A`
* Tingnan ang output ng resulta ng test sa Test Results view.
* Gumawa ng mga pagbabago sa `src/test/extension.test.ts` o gumawa ng mga bagong test file sa loob ng `test` folder.
  * Tanging mga file na tumutugma sa pattern ng pangalan na `**.test.ts` lamang ang isasaalang-alang ng test runner.
  * Maaari kang gumawa ng mga folder sa loob ng `test` folder para ayusin ang iyong mga tests ayon sa gusto mo.

## Magpatuloy pa

* Bawasan ang laki ng extension at pagbutihin ang oras ng pagsisimula sa pamamagitan ng [pag-bundle ng iyong extension](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [I-publish ang iyong extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) sa VS Code extension marketplace.
* I-automate ang builds sa pamamagitan ng pagsasaayos ng [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kaming maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.