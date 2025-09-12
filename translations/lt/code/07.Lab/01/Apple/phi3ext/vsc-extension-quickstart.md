<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-09-12T15:01:06+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "lt"
}
-->
# Sveiki atvykę į jūsų VS Code plėtinį

## Kas yra aplanke

* Šiame aplanke yra visi failai, reikalingi jūsų plėtiniui.
* `package.json` - tai manifestas, kuriame deklaruojate savo plėtinį ir komandą.
  * Pavyzdinis įskiepis registruoja komandą ir apibrėžia jos pavadinimą bei komandos pavadinimą. Remdamasis šia informacija, VS Code gali parodyti komandą komandų paletėje. Šiuo metu įskiepis dar nėra įkeltas.
* `src/extension.ts` - tai pagrindinis failas, kuriame pateikiate savo komandos įgyvendinimą.
  * Failas eksportuoja vieną funkciją, `activate`, kuri yra iškviečiama pirmą kartą aktyvuojant jūsų plėtinį (šiuo atveju vykdant komandą). Viduje `activate` funkcijos mes iškviečiame `registerCommand`.
  * Mes perduodame funkciją, kurioje yra komandos įgyvendinimas, kaip antrąjį parametrą `registerCommand`.

## Nustatymas

* Įdiekite rekomenduojamus plėtinius (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner ir dbaeumer.vscode-eslint).

## Pradėkite naudotis iš karto

* Paspauskite `F5`, kad atidarytumėte naują langą su įkeltu jūsų plėtiniu.
* Vykdykite savo komandą iš komandų paletės paspausdami (`Ctrl+Shift+P` arba `Cmd+Shift+P` Mac kompiuteryje) ir įvesdami `Hello World`.
* Nustatykite pertraukos taškus savo kode, esančiame `src/extension.ts`, kad galėtumėte derinti savo plėtinį.
* Suraskite savo plėtinio išvestį derinimo konsolėje.

## Darykite pakeitimus

* Po pakeitimų `src/extension.ts` faile galite iš naujo paleisti plėtinį iš derinimo įrankių juostos.
* Taip pat galite iš naujo įkelti (`Ctrl+R` arba `Cmd+R` Mac kompiuteryje) VS Code langą su jūsų plėtiniu, kad įkeltumėte pakeitimus.

## Tyrinėkite API

* Galite atidaryti visą mūsų API rinkinį, kai atidarote failą `node_modules/@types/vscode/index.d.ts`.

## Vykdykite testus

* Įdiekite [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Vykdykite "watch" užduotį per **Tasks: Run Task** komandą. Įsitikinkite, kad ji veikia, kitaip testai gali būti nerasti.
* Atidarykite Testavimo vaizdą iš veiklos juostos ir paspauskite mygtuką "Run Test" arba naudokite sparčiuosius klavišus `Ctrl/Cmd + ; A`.
* Peržiūrėkite testų rezultatų išvestį Testų Rezultatų vaizde.
* Darykite pakeitimus `src/test/extension.test.ts` faile arba kurkite naujus testų failus aplanke `test`.
  * Pateiktas testų vykdytojas atsižvelgs tik į failus, atitinkančius pavadinimo šabloną `**.test.ts`.
  * Galite kurti aplankus aplanke `test`, kad struktūrizuotumėte savo testus taip, kaip norite.

## Eikite toliau

* Sumažinkite plėtinio dydį ir pagerinkite paleidimo laiką [sukurdami plėtinio paketą](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publikuokite savo plėtinį](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) VS Code plėtinių rinkoje.
* Automatizuokite kūrimą nustatydami [Nuolatinę integraciją](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.