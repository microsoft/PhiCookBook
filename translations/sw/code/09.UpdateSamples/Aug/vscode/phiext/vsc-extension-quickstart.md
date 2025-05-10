<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:41:42+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "sw"
}
-->
# Karibu kwenye Upanuzi wako wa VS Code

## Kile kilicho kwenye folda

* Folda hii ina faili zote muhimu kwa upanuzi wako.
* `package.json` - hili ni faili la manifesti ambapo unatangaza upanuzi na amri zako.
  * Plugin ya mfano hujiandikisha amri na kuweka kichwa na jina la amri. Kwa taarifa hii VS Code inaweza kuonyesha amri kwenye orodha ya amri. Haina haja ya kupakia plugin bado.
* `src/extension.ts` - hili ni faili kuu ambapo utatoa utekelezaji wa amri yako.
  * Faili hii hutoa kazi moja, `activate`, ambayo huitwa mara ya kwanza upanuzi wako unapowashwa (katika kesi hii kwa kutekeleza amri). Ndani ya kazi ya `activate` tunaita `registerCommand`.
  * Tunapitia kazi inayotekeleza amri kama parameta ya pili kwa `registerCommand`.

## Usanidi

* sakinisha upanuzi zinazopendekezwa (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, na dbaeumer.vscode-eslint)

## Anza mara moja

* Bonyeza `F5` kufungua dirisha jipya na upanuzi wako umewekwa.
* Endesha amri yako kutoka kwenye orodha ya amri kwa kubonyeza (`Ctrl+Shift+P` au `Cmd+Shift+P` kwenye Mac) na kuandika `Hello World`.
* Weka breakpoints kwenye msimbo wako ndani ya `src/extension.ts` ili kufuatilia upanuzi wako.
* Pata matokeo kutoka kwa upanuzi wako kwenye debug console.

## Fanya mabadiliko

* Unaweza kuanzisha upanuzi tena kutoka kwenye zana ya debug baada ya kubadilisha msimbo ndani ya `src/extension.ts`.
* Pia unaweza kupakia upya (`Ctrl+R` au `Cmd+R` kwenye Mac) dirisha la VS Code lenye upanuzi wako ili kupakia mabadiliko.

## Chunguza API

* Unaweza kufungua API nzima ukiwa umefungua faili `node_modules/@types/vscode/index.d.ts`.

## Endesha majaribio

* Sakinisha [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Endesha kazi ya "watch" kupitia amri ya **Tasks: Run Task**. Hakikisha inaendelea kuendesha, vinginevyo majaribio hayataonekana.
* Fungua mtazamo wa Testing kutoka kwenye activity bar na bonyeza kitufe cha Run Test, au tumia kitufe cha haraka `Ctrl/Cmd + ; A`
* Tazama matokeo ya majaribio kwenye Test Results view.
* Fanya mabadiliko kwenye `src/test/extension.test.ts` au tengeneza faili mpya za majaribio ndani ya folda ya `test`.
  * Msimamizi wa majaribio atazingatia tu faili zenye muundo wa jina `**.test.ts`.
  * Unaweza kutengeneza folda ndani ya `test` kupanga majaribio yako kwa njia yoyote unayotaka.

## Endelea zaidi

* Punguza ukubwa wa upanuzi na boresha muda wa kuanzisha kwa [kufunga upanuzi wako](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Chapisha upanuzi wako](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) kwenye soko la upanuzi la VS Code.
* Fanya ujenzi wa kiotomatiki kwa kuanzisha [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Kiepile**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za moja kwa moja zinaweza kuwa na makosa au upotovu wa maana. Nyaraka ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha kuaminika. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatuna wajibu kwa kutokuelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.