<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:34:14+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "br"
}
-->
# Degemer mat ho koulzadenn VS Code

## Petra zo e-barzh al lec'hienn

* Ar lec'hienn-mañ en deus tout ar restroù ezhomm evit ho koulzadenn.
* `package.json` - file manifest eo, e-lec'h ma tiskouezit ho koulzadenn hag ho komand.
  * Ar plugin skouer enroll a ra ur komand ha diskouez a ra e anv hag e titel. Gant an titouroù-se e c'hall VS Code diskouez ar komand er paletenn komand. N'eo ket ret kargañ ar plugin c'hoazh.
* `src/extension.ts` - ar file pennañ eo, amañ e roit implijout ho komand.
  * Ar file a allañ un doare, `activate`, a vo galvet alies e-pad an aktivadenn gentañ eus ho koulzadenn (dre lakaat ar komand da vont war-raok). E-barzh `activate` e galon `registerCommand`.
  * Roiñ a reomp ar funktion o kinnig implij ar komand evel eil paramet war-lerc'h `registerCommand`.

## Krouiñ an aozadur

* lakaat ar c'houlzadenn ezhomm (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, ha dbaeumer.vscode-eslint)


## Krogit a-benn da vont gant ar skol

* Klichañ `F5` evit digeriñ ur prenestr nevez gant ho koulzadenn karget.
* Rannañ ho komand er paletenn komand dre lakaat (`Ctrl+Shift+P` pe `Cmd+Shift+P` war Mac) ha skrivañ `Hello World`.
* Lakaat breakpoints e ho kod e-barzh `src/extension.ts` evit debugiañ ho koulzadenn.
* Kavout an disoc'hoù eus ho koulzadenn er c'honsole debug.

## Ober kemmoù

* Gallout a rit adkargañ ar koulzadenn dre ar bara debug goude bezañ kemmet ho kod e `src/extension.ts`.
* Gallout a rit ivez adkargañ (`Ctrl+R` pe `Cmd+R` war Mac) prenestr VS Code gant ho koulzadenn evit kargañ ho kemmoù.


## Diskouez ar API

* Gallout a rit digeriñ ar set leun eus hon API pa digeriñ ar file `node_modules/@types/vscode/index.d.ts`.

## Mont war-raok gant ar testennoù

* Lakaat da vont ar [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Mont war-raok gant ar "watch" task dre ar komand **Tasks: Run Task**. Gwiriit ma vez aozet mat evit ma vo kavet ar testennoù.
* Digeriñ ar gweledva testañ eus ar bar aktivite ha klikañ war ar bouton "Run Test", pe implijout ar hotkey `Ctrl/Cmd + ; A`
* Gwelet disoc'hoù ar test e gweledva Test Results.
* Ober kemmoù e `src/test/extension.test.ts` pe krouiñ restroù test nevez e-barzh ar lec'hienn `test`.
  * Ar test runner kinniget a glask nemet restroù o anv gant ar patrom `**.test.ts`.
  * Gallout a rit krouiñ lec'hiennoù e-barzh `test` evit aozañ ho testennoù hervez ho c'hoant.

## Dont pelloc'h

* Leuc'hiañ ment ar koulzadenn ha gwellañ an amzer kentañ kargañ dre [bundling ho koulzadenn](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Embann ho koulzadenn](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) war ar marc'had koulzadennoù VS Code.
* Ober automatismañ an aozadurioù dre staliañ [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.