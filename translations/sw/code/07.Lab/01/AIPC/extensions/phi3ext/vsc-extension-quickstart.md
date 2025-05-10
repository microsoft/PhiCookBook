<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-09T04:58:13+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "sw"
}
-->
# Karibu kwenye VS Code Extension yako

## Kile kilicho kwenye folda

* Folda hii ina faili zote muhimu kwa extension yako.
* `package.json` - hii ni faili ya manifest ambapo unatangaza extension yako na amri zake.
  * Plugin ya mfano inasajili amri na kuweka kichwa na jina la amri. Kwa taarifa hii, VS Code inaweza kuonyesha amri kwenye command palette. Haina haja ya kupakia plugin bado.
* `src/extension.ts` - hii ni faili kuu ambapo utatekeleza amri yako.
  * Faili hutoa function moja, `activate`, ambayo huitwa mara ya kwanza extension yako inapowashwa (hapa ni kwa kutekeleza amri). Ndani ya function `activate` tunaita `registerCommand`.
  * Tunapitia function yenye utekelezaji wa amri kama parameter ya pili kwa `registerCommand`.

## Usanidi

* sakinisha extensions zinazopendekezwa (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, na dbaeumer.vscode-eslint)

## Anza mara moja

* Bonyeza `F5` kufungua dirisha jipya na extension yako ikiwa imepakuliwa.
* Endesha amri yako kutoka kwenye command palette kwa kubonyeza (`Ctrl+Shift+P` au `Cmd+Shift+P` kwenye Mac) na kuandika `Hello World`.
* Weka breakpoints kwenye msimbo wako ndani ya `src/extension.ts` ili kufuatilia extension yako.
* Tafuta matokeo kutoka kwa extension yako kwenye debug console.

## Fanya mabadiliko

* Unaweza kuwasha upya extension kutoka kwenye debug toolbar baada ya kubadilisha msimbo ndani ya `src/extension.ts`.
* Pia unaweza reload (`Ctrl+R` au `Cmd+R` kwenye Mac) dirisha la VS Code na extension yako ili kupakia mabadiliko.

## Chunguza API

* Unaweza kufungua seti kamili ya API yetu unapofungua faili `node_modules/@types/vscode/index.d.ts`.

## Endesha majaribio

* Sakinisha [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Endesha task ya "watch" kupitia amri **Tasks: Run Task**. Hakikisha inaendelea kuendesha, vinginevyo majaribio hayataonekana.
* Fungua Testing view kutoka kwenye activity bar na bonyeza kitufe cha Run Test, au tumia hotkey `Ctrl/Cmd + ; A`
* Angalia matokeo ya majaribio kwenye Test Results view.
* Fanya mabadiliko kwenye `src/test/extension.test.ts` au tengeneza faili mpya za majaribio ndani ya folda ya `test`.
  * Test runner iliyotolewa itazingatia tu faili zilizo na jina linalolingana na pattern ya `**.test.ts`.
  * Unaweza kutengeneza folda ndani ya `test` kupanga majaribio yako kwa namna yoyote unayotaka.

## Endelea zaidi

* Punguza ukubwa wa extension na boresha muda wa kuanza kwa [kubundling extension yako](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Chapisha extension yako](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) kwenye soko la VS Code extension.
* Fanya ujenzi wa otomatiki kwa kuanzisha [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Kiaruhusi**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatubeba dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.