<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-07-16T16:45:26+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "sw"
}
-->
# Karibu kwenye Upanuzi wako wa VS Code

## Kile kilicho kwenye folda

* Folda hii ina faili zote muhimu kwa upanuzi wako.
* `package.json` - hii ni faili ya maelezo ambapo unatangaza upanuzi wako na amri.
  * Kiongezi cha mfano hujiandikisha amri na kuainisha kichwa na jina la amri. Kwa taarifa hii VS Code inaweza kuonyesha amri kwenye orodha ya amri. Haina haja ya kupakia kiongezi bado.
* `src/extension.ts` - hii ni faili kuu ambapo utatoa utekelezaji wa amri yako.
  * Faili hii hupeana kazi moja, `activate`, ambayo huitwa mara ya kwanza upanuzi wako unapoanzishwa (katika kesi hii kwa kutekeleza amri). Ndani ya kazi ya `activate` tunaita `registerCommand`.
  * Tunapita kazi inayotekeleza amri kama kigezo cha pili kwa `registerCommand`.

## Usanidi

* sakinisha upanuzi unaopendekezwa (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, na dbaeumer.vscode-eslint)

## Anza mara moja

* Bonyeza `F5` kufungua dirisha jipya na upanuzi wako umewekwa.
* Endesha amri yako kutoka kwenye orodha ya amri kwa kubonyeza (`Ctrl+Shift+P` au `Cmd+Shift+P` kwenye Mac) na kuandika `Hello World`.
* Weka alama za kusimama (breakpoints) kwenye msimbo wako ndani ya `src/extension.ts` kwa ajili ya kufuatilia upanuzi wako.
* Tafuta matokeo kutoka kwa upanuzi wako kwenye koni ya ufuatiliaji.

## Fanya mabadiliko

* Unaweza kuanzisha upanuzi tena kutoka kwenye zana ya ufuatiliaji baada ya kubadilisha msimbo katika `src/extension.ts`.
* Pia unaweza kupakia upya (`Ctrl+R` au `Cmd+R` kwenye Mac) dirisha la VS Code na upanuzi wako ili kupakia mabadiliko yako.

## Chunguza API

* Unaweza kufungua seti kamili ya API yetu unapo fungua faili `node_modules/@types/vscode/index.d.ts`.

## Endesha majaribio

* Sakinisha [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Endesha kazi ya "watch" kupitia amri ya **Tasks: Run Task**. Hakikisha hii inaendelea, vinginevyo majaribio hayataonekana.
* Fungua mtazamo wa Testing kutoka kwenye upau wa shughuli na bonyeza kitufe cha "Run Test", au tumia kitufe cha haraka `Ctrl/Cmd + ; A`
* Tazama matokeo ya jaribio kwenye mtazamo wa Test Results.
* Fanya mabadiliko kwenye `src/test/extension.test.ts` au tengeneza faili mpya za majaribio ndani ya folda ya `test`.
  * Mwendeshaji wa majaribio aliyepewa atazingatia tu faili zinazolingana na muundo wa jina `**.test.ts`.
  * Unaweza kutengeneza folda ndani ya folda ya `test` kupanga majaribio yako kwa njia yoyote unayotaka.

## Endelea zaidi

* Punguza ukubwa wa upanuzi na boresha muda wa kuanzisha kwa [kuunganisha upanuzi wako](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Chapisha upanuzi wako](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) kwenye soko la upanuzi la VS Code.
* Fanya ujenzi wa kiotomatiki kwa kuanzisha [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.