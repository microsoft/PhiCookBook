<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6a7479104914787e4f0976e39131e8e3",
  "translation_date": "2025-04-04T11:34:40+00:00",
  "source_file": "code\\07.Lab\\01\\Apple\\phi3ext\\vsc-extension-quickstart.md",
  "language_code": "mo"
}
-->
# Sannu da zuwa ga ƙarin na'urar VS Code ɗinka

## Abubuwan da ke cikin babban fayil

* Wannan babban fayil ɗin yana ɗauke da duk fayilolin da ake buƙata don ƙarin na'urar.
* `package.json` - wannan shi ne fayil na manifest inda kake bayyana ƙarin na'urar da umarni.
  * Misalin plugin yana yin rijista na umarni da bayyana sunansa da kuma taken umarni. Da wannan bayanin VS Code zai iya nuna umarni a cikin menu na umarni. Har yanzu ba lallai ba ne ya ɗora plugin.
* `src/extension.ts` - wannan shi ne babban fayil inda za ka samar da aiwatar da umarninka.
  * Fayil ɗin yana fitar da aiki ɗaya, `activate`, wanda ake kira a karon farko lokacin da ƙarin na'urar ta kunna (a wannan yanayin ta hanyar aiwatar da umarni). A cikin `activate` muna kira `registerCommand`.
  * Muna mika aikin da ke ɗauke da aiwatar da umarni a matsayin sigar ta biyu zuwa `registerCommand`.

## Saita

* shigar da ƙarin na'urorin da aka ba da shawara (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, da dbaeumer.vscode-eslint)

## Fara aiki kai tsaye

* Danna `F5` don buɗe sabon taga tare da ƙarin na'urar da aka ɗora.
* Gudanar da umarninka daga menu na umarni ta hanyar danna (`Ctrl+Shift+P` ko `Cmd+Shift+P` a Mac) da rubuta `Hello World`.
* Sanya wuraren tsayawa a cikin lambar a cikin `src/extension.ts` don yin debugging na ƙarin na'urar.
* Nemo fitarwa daga ƙarin na'urar a cikin kwamitin debugging.

## Yi gyare-gyare

* Za ka iya sake ɗora ƙarin na'urar daga kayan aikin debugging bayan ka yi gyare-gyare a cikin `src/extension.ts`.
* Hakanan za ka iya sake ɗora (`Ctrl+R` ko `Cmd+R` a Mac) taga na VS Code tare da ƙarin na'urar don ɗora gyare-gyarenka.

## Bincika API

* Za ka iya buɗe cikakken jerin API ɗinmu lokacin da ka buɗe fayil ɗin `node_modules/@types/vscode/index.d.ts`.

## Gudanar da gwaje-gwaje

* Shigar da [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Gudanar da aikin "watch" ta hanyar umarnin **Tasks: Run Task**. Tabbatar da cewa yana gudana, ko gwaje-gwaje ba za a gano ba.
* Buɗe ra'ayin Testing daga mashaya ayyuka kuma danna maɓallin "Run Test", ko amfani da maɓallin umarni `Ctrl/Cmd + ; A`.
* Duba fitarwa na sakamakon gwaji a cikin ra'ayin Test Results.
* Yi gyare-gyare a cikin `src/test/extension.test.ts` ko ƙirƙiri sabbin fayilolin gwaji a cikin babban fayil ɗin `test`.
  * Mai gudanar da gwaji da aka bayar zai ɗauki fayilolin da suka dace da sunan alamu `**.test.ts`.
  * Za ka iya ƙirƙirar manyan fayiloli a cikin babban fayil ɗin `test` don tsara gwaje-gwajen yadda kake so.

## Yi ƙarin bincike

* Rage girman ƙarin na'urar da inganta lokacin farawa ta hanyar [bundling your extension](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publish your extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) a kasuwar ƙarin na'urar VS Code.
* Daidaita gina-gina ta hanyar kafa [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

It seems like "mo" isn't a widely recognized language code or name for a language. Could you clarify or specify which language you mean by "mo"? For instance, are you referring to Maori, Moldovan, or something else?