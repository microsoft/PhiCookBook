<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:09:44+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "sw"
}
-->
# Karibu kwenye Upanuzi wako wa VS Code

## Kile kilicho kwenye folda

* Folda hii ina faili zote muhimu kwa upanuzi wako.
* `package.json` - huu ni faili la manifest ambapo unatangaza upanuzi na amri yako.
  * Plugin ya mfano hujisajili na kuainisha kichwa na jina la amri. Kwa taarifa hii VS Code inaweza kuonyesha amri kwenye orodha ya amri. Haijalazimika bado kupakia plugin.
* `src/extension.ts` - huu ni faili kuu ambapo utatekeleza amri yako.
  * Faili hutoa kazi moja, `activate`, ambayo huitwa mara ya kwanza upanuzi wako unapoanzishwa (hapa ni kwa kutekeleza amri). Ndani ya kazi `activate` tunaita `registerCommand`.
  * Tunapita kazi inayotekeleza amri kama kipengele cha pili kwa `registerCommand`.

## Usanidi

* sakinisha upanuzi unaopendekezwa (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, na dbaeumer.vscode-eslint)

## Anza mara moja

* Bonyeza `F5` kufungua dirisha jipya lenye upanuzi wako umebeba.
* Tekeleza amri yako kutoka kwenye orodha ya amri kwa kubonyeza (`Ctrl+Shift+P` au `Cmd+Shift+P` kwenye Mac) na kuandika `Hello World`.
* Weka breakpoints kwenye msimbo wako ndani ya `src/extension.ts` kwa ajili ya kufuatilia upanuzi wako.
* Tafuta matokeo kutoka kwa upanuzi wako kwenye koni ya ufuatiliaji.

## Fanya mabadiliko

* Unaweza kuanzisha upya upanuzi kutoka kwenye zana ya ufuatiliaji baada ya kubadilisha msimbo ndani ya `src/extension.ts`.
* Pia unaweza upya (`Ctrl+R` au `Cmd+R` kwenye Mac) dirisha la VS Code lenye upanuzi wako ili kupakia mabadiliko.

## Chunguza API

* Unaweza kufungua seti kamili ya API yetu unapo fungua faili `node_modules/@types/vscode/index.d.ts`.

## Endesha majaribio

* Sakinisha [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Endesha kazi ya "watch" kupitia amri **Tasks: Run Task**. Hakikisha hii inaendelea, vinginevyo majaribio hayataonekana.
* Fungua mtazamo wa Testing kutoka kwenye bar ya shughuli na bonyeza kitufe cha Run Test, au tumia kitufe cha haraka `Ctrl/Cmd + ; A`
* Angalia matokeo ya majaribio kwenye mtazamo wa Test Results.
* Fanya mabadiliko kwenye `src/test/extension.test.ts` au tengeneza faili mpya za majaribio ndani ya folda ya `test`.
  * Mchezaji wa majaribio aliyepewa atazingatia tu faili zenye muundo wa jina `**.test.ts`.
  * Unaweza kutengeneza folda ndani ya `test` kuandaa majaribio yako kwa namna unayotaka.

## Endelea zaidi

* Punguza ukubwa wa upanuzi na boresha muda wa kuanzisha kwa [kuunganisha upanuzi wako](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Chapisha upanuzi wako](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) kwenye soko la upanuzi la VS Code.
* Panga ujenzi wa moja kwa moja kwa kuweka [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Kiarifu cha Kutengwa**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za moja kwa moja zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubeba dhima kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.