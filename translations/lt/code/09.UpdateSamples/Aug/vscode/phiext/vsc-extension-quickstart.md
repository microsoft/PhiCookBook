# Sveiki atvykę į savo VS Code plėtinį

## Kas yra aplanke

* Šiame aplanke yra visi failai, reikalingi jūsų plėtiniui.
* `package.json` - tai manifestinis failas, kuriame deklaruojate savo plėtinį ir komandą.
  * Pavyzdinis įskiepis registruoja komandą ir apibrėžia jos pavadinimą bei komandos pavadinimą. Remdamasis šia informacija, VS Code gali parodyti komandą komandų paletėje. Įskiepis dar nereikalingas įkrovimui.
* `src/extension.ts` - tai pagrindinis failas, kuriame pateikiate savo komandos įgyvendinimą.
  * Failas eksportuoja vieną funkciją, `activate`, kuri yra iškviečiama pirmą kartą aktyvuojant jūsų plėtinį (šiuo atveju vykdant komandą). Viduje `activate` funkcijos mes iškviečiame `registerCommand`.
  * Mes perduodame funkciją, kurioje yra komandos įgyvendinimas, kaip antrąjį parametrą `registerCommand`.

## Nustatymas

* Įdiekite rekomenduojamus plėtinius (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner ir dbaeumer.vscode-eslint).

## Pradėkite naudotis iš karto

* Paspauskite `F5`, kad atidarytumėte naują langą su įkeltu plėtiniu.
* Vykdykite savo komandą iš komandų paletės paspausdami (`Ctrl+Shift+P` arba `Cmd+Shift+P` Mac kompiuteryje) ir įvesdami `Hello World`.
* Nustatykite pertraukos taškus savo kode, esančiame `src/extension.ts`, kad galėtumėte derinti savo plėtinį.
* Suraskite savo plėtinio išvestį derinimo konsolėje.

## Darykite pakeitimus

* Po kodo pakeitimų `src/extension.ts` galite iš naujo paleisti plėtinį iš derinimo įrankių juostos.
* Taip pat galite iš naujo įkelti (`Ctrl+R` arba `Cmd+R` Mac kompiuteryje) VS Code langą su savo plėtiniu, kad įkeltumėte pakeitimus.

## Tyrinėkite API

* Galite atidaryti visą mūsų API rinkinį, kai atidarote failą `node_modules/@types/vscode/index.d.ts`.

## Vykdykite testus

* Įdiekite [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Vykdykite "watch" užduotį per **Tasks: Run Task** komandą. Įsitikinkite, kad ji veikia, kitaip testai gali būti nerasti.
* Atidarykite Testavimo vaizdą iš veiklos juostos ir spustelėkite mygtuką "Run Test" arba naudokite sparčiuosius klavišus `Ctrl/Cmd + ; A`.
* Peržiūrėkite testo rezultatų išvestį Testo Rezultatų vaizde.
* Darykite pakeitimus `src/test/extension.test.ts` arba kurkite naujus testų failus aplanke `test`.
  * Pateiktas testų vykdytojas atsižvelgs tik į failus, atitinkančius pavadinimo šabloną `**.test.ts`.
  * Galite kurti aplankus aplanke `test`, kad struktūrizuotumėte savo testus taip, kaip norite.

## Eikite toliau

* Sumažinkite plėtinio dydį ir pagerinkite paleidimo laiką [sukurdami plėtinio paketą](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publikuokite savo plėtinį](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) VS Code plėtinių parduotuvėje.
* Automatizuokite kūrimą nustatydami [Nuolatinę integraciją](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.