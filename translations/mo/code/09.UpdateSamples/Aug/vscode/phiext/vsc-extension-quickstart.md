<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6a7479104914787e4f0976e39131e8e3",
  "translation_date": "2025-04-04T11:39:47+00:00",
  "source_file": "code\\09.UpdateSamples\\Aug\\vscode\\phiext\\vsc-extension-quickstart.md",
  "language_code": "mo"
}
-->
# Ku soo dhawow kordhintaada VS Code

## Maxaa ku jira galka

* Galkaan wuxuu ka kooban yahay dhammaan faylasha lagama maarmaanka u ah kordhintaada.
* `package.json` - waa faylka manifest oo aad ku qeexeyso kordhintaada iyo amarkaaga.
  * Plugin-ka tusaalaha ah wuxuu diiwaan gelinayaa amar wuxuuna qeexayaa cinwaankiisa iyo magaca amarka. Macluumaadkan VS Code wuxuu ku soo bandhigi karaa amarka liiska amarrada. Ma jiro baahi uu plugin-ka u leeyahay inuu hadda soo shubto.
* `src/extension.ts` - waa faylka ugu muhiimsan halkaas oo aad ku bixin doonto hirgelinta amarkaaga.
  * Faylku wuxuu dhoofinayaa hal shaqo, `activate`, taas oo la wacayo markii ugu horreysay ee kordhintaada la hawlgeliyo (kiiskan iyadoo la fulinayo amarka). Gudaha shaqada `activate` waxaan wacnaa `registerCommand`.
  * Waxaan u gudbinnaa shaqada ka kooban hirgelinta amarka sida halbeeg labaad ee `registerCommand`.

## Dejinta

* Ku rakib kordhinta lagula taliyay (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, iyo dbaeumer.vscode-eslint)

## Si degdeg ah uga shaqee

* Riix `F5` si aad u furto daaqad cusub oo kordhintaada ku shuban tahay.
* Ka ful amar liiska amarrada adigoo riixaya (`Ctrl+Shift+P` ama `Cmd+Shift+P` ee Mac) oo ku qoraya `Hello World`.
* Ku dejiso goobo jebin gudaha koodkaaga `src/extension.ts` si aad u baarto kordhintaada.
* Raadi wax soo saarka kordhintaada gudaha console-ka debug.

## Wax ka beddel

* Waxaad dib u hawlgelin kartaa kordhinta adigoo ka soo bilowaya toolbar-ka debug ka dib markaad wax ka beddesho koodka `src/extension.ts`.
* Sidoo kale waad dib u shubi kartaa (`Ctrl+R` ama `Cmd+R` ee Mac) daaqadda VS Code oo leh kordhintaada si aad u shubto isbeddeladaada.

## Sahamin API-ga

* Waxaad furi kartaa dhammaan API-ga markaad furto faylka `node_modules/@types/vscode/index.d.ts`.

## Tijaabi

* Ku rakib [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Ku socodsii hawsha "watch" adoo adeegsanaya amarka **Tasks: Run Task**. Hubi inay socoto, haddii kale tijaabooyinka lama ogaan karo.
* Fur muuqaalka Tijaabinta ee baraha howlaha oo guji badhanka "Run Test", ama isticmaal furaha `Ctrl/Cmd + ; A`.
* Fiiri natiijada tijaabada ee muuqaalka Natiijooyinka Tijaabada.
* Samee isbeddelo `src/test/extension.test.ts` ama samee faylasha cusub ee tijaabada gudaha galka `test`.
  * Socodsiiyaha tijaabada ee la bixiyay wuxuu kaliya tixgelin doonaa faylasha u dhigma qaabka magaca `**.test.ts`.
  * Waxaad ka abuuri kartaa galal gudaha galka `test` si aad u dhisto tijaabooyinkaaga qaab kasta oo aad rabto.

## Ku sii soco

* Yaree cabbirka kordhinta oo hagaaji waqtiga bilowga adigoo [isku xiraya kordhintaada](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Ku daabac kordhintaada](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) suuqa kordhinta ee VS Code.
* Si toos ah u samee dhismayaal adigoo dejinaya [Isku-darka Joogtada ah](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

It seems you are requesting a translation to "mo," but could you clarify what language "mo" refers to? It could be shorthand for a specific language or dialect. Let me know so I can assist you better!