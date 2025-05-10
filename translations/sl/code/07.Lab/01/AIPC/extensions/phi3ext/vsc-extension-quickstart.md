<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-09T04:59:35+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "sl"
}
-->
# ඔබේ VS Code විස්තාරණයට සාදරයෙන් පිළිගනිමු

## ෆෝල්ඩරයේ ඇති දේ

* මෙම ෆෝල්ඩරය තුළ ඔබේ විස්තාරණය සඳහා අවශ්‍ය සියලු ගොනු අඩංගු වේ.
* `package.json` - මෙය manifest ගොනුව වන අතර මෙහි ඔබ ඔබේ විස්තාරණය සහ විධානය ප්‍රකාශ කරයි.
  * නියැදි ප්ලගිනයක් විධානයක් ලියාපදිංචි කර එහි මාතෘකාව සහ විධානයේ නම නියම කරයි. මේ මගින් VS Code විධානය command palette එකේ පෙන්විය හැක. තවමත් ප්ලගිනය ලෝඩ් කිරීම අවශ්‍ය නැත.
* `src/extension.ts` - මෙය ප්‍රධාන ගොනුව වන අතර ඔබ මෙහි ඔබේ විධානයේ ක්‍රියාත්මක කිරීම සපයයි.
  * ගොනුවෙන් එක් function එකක්, `activate`, අපනයනය කරයි. මෙය ඔබේ විස්තාරණය පළවෙනි වතාවට සක්‍රීය වූ විට (මෙම අවස්ථාවේ විධානය ක්‍රියාත්මක කිරීමෙන්) කැඳවෙයි. `activate` function එක තුළ අපි `registerCommand` කැඳවයි.
  * විධානයේ ක්‍රියාත්මක කිරීම අඩංගු function එක දෙවන පරාමිතිය ලෙස `registerCommand` වෙත යවයි.

## සැකසීම

* නිර්දේශිත විස්තාරණ ස්ථාපනය කරන්න (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, සහ dbaeumer.vscode-eslint)


## සෘජුවම ආරම්භ කරන්න

* ඔබේ විස්තාරණය සමඟ නව කවුළුවක් විවෘත කිරීමට `F5` ඔබන්න.
* විධානය command palette එකෙන් ධාවනය කරන්න (Mac හි `Ctrl+Shift+P` හෝ `Cmd+Shift+P` ඔබා) සහ `Hello World` ටයිප් කරන්න.
* ඔබේ කේතයේ `src/extension.ts` තුළ breakpoints සකසන්න ඔබේ විස්තාරණය නිවැරදි කිරීම සඳහා.
* debug console එකේ ඔබේ විස්තාරණයෙන් ප්‍රතිදානය සොයා ගන්න.

## වෙනස්කම් කරන්න

* `src/extension.ts` හි කේතය වෙනස් කිරීමෙන් පසු debug toolbar එකෙන් විස්තාරණය නැවත ආරම්භ කළ හැක.
* VS Code කවුළුව නැවත ලෝඩ් කිරීමට (`Ctrl+R` හෝ Mac හි `Cmd+R`) ඔබේ විස්තාරණය සමඟ ඔබේ වෙනස්කම් පූරණය කර ගත හැක.

## API සොයා බලන්න

* `node_modules/@types/vscode/index.d.ts` ගොනුව විවෘත කළ විට අපගේ API සම්පූර්ණ කට්ටලය ඔබට විවෘත කළ හැක.

## පරීක්ෂණ ධාවනය කරන්න

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) ස්ථාපනය කරන්න
* **Tasks: Run Task** විධානයෙන් "watch" task එක ධාවනය කරන්න. මෙය ක්‍රියාත්මක නොවුවහොත් පරීක්ෂණ හඳුනාගැනීම සිදු නොවනු ඇත.
* activity bar හි Testing දර්ශනය විවෘත කර "Run Test" බොත්තම ඔබන්න, හෝ හොට්කි `Ctrl/Cmd + ; A` භාවිතා කරන්න
* Test Results දර්ශනයේ පරීක්ෂණ ප්‍රතිඵල ප්‍රතිදානය බලන්න.
* `src/test/extension.test.ts` හෝ `test` ෆෝල්ඩරය තුළ නව පරීක්ෂණ ගොනු සාදන්න.
  * සපයන ලද test runner එකේ නාම රටාවට `**.test.ts` ගොනු පමණක් සලකා බලයි.
  * ඔබට `test` ෆෝල්ඩරය තුළ නව ෆෝල්ඩර සාදා ඔබේ පරීක්ෂණ ව්‍යුහගත කළ හැක.

## තවදුරටත් යන්න

* ඔබේ විස්තාරණයේ ප්‍රමාණය අඩු කර ආරම්භක කාලය වැඩි දියුණු කිරීමට [ඔබේ විස්තාරණය bundle කිරීම](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo) කරන්න.
* VS Code විස්තාරණ වෙළඳපොළේ ඔබේ විස්තාරණය [ප්‍රකාශනය](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) කරන්න.
* [අඛණ්ඩ ඒකාබද්ධ කිරීම](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo) සකස් කර ගොඩනැගීම් ස්වයංක්‍රීය කරන්න.

**Izjava o omejitvi odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za kritične informacije priporočamo strokovni prevod, opravljen s strani človeka. Ne odgovarjamo za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.