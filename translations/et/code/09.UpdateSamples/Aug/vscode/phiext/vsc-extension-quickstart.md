# Tere tulemast oma VS Code laiendusse

## Mis on kaustas

* See kaust sisaldab kõiki faile, mis on vajalikud sinu laienduse jaoks.
* `package.json` - see on manifestifail, kus sa deklareerid oma laienduse ja käsu.
  * Näidisplugin registreerib käsu ja määratleb selle pealkirja ning käsu nime. Selle teabe abil saab VS Code kuvada käsu käsupaletis. Pluginat ei ole veel vaja laadida.
* `src/extension.ts` - see on peamine fail, kus sa rakendad oma käsu.
  * Fail ekspordib ühe funktsiooni, `activate`, mida kutsutakse esimest korda, kui sinu laiendus aktiveeritakse (antud juhul käsu täitmisega). `activate` funktsiooni sees kutsume `registerCommand`.
  * Me edastame funktsiooni, mis sisaldab käsu rakendust, `registerCommand` teisele parameetrile.

## Seadistamine

* Paigalda soovitatud laiendused (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner ja dbaeumer.vscode-eslint).

## Alusta kohe

* Vajuta `F5`, et avada uus aken, kus sinu laiendus on laaditud.
* Käivita oma käsk käsupaletist, vajutades (`Ctrl+Shift+P` või Macil `Cmd+Shift+P`) ja sisestades `Hello World`.
* Sea katkestuspunkte oma koodis `src/extension.ts` failis, et siluda oma laiendust.
* Leia oma laienduse väljund silumiskonsoolist.

## Tee muudatusi

* Sa saad laienduse uuesti käivitada silumistööriistaribalt pärast muudatuste tegemist `src/extension.ts` failis.
* Sa saad ka uuesti laadida (`Ctrl+R` või Macil `Cmd+R`) VS Code akna, et laadida oma muudatused.

## Uuri API-d

* Sa saad avada meie API täieliku komplekti, kui avad faili `node_modules/@types/vscode/index.d.ts`.

## Käivita testid

* Paigalda [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Käivita "watch" ülesanne **Tasks: Run Task** käsu kaudu. Veendu, et see töötab, vastasel juhul teste ei pruugita avastada.
* Ava Testimise vaade tegevusribalt ja vajuta "Run Test" nuppu või kasuta kiirklahvi `Ctrl/Cmd + ; A`.
* Vaata testi tulemuste väljundit Test Results vaates.
* Tee muudatusi `src/test/extension.test.ts` failis või loo uusi testifaile `test` kausta sees.
  * Pakutud testijooksja arvestab ainult faile, mis vastavad nime mustrile `**.test.ts`.
  * Sa saad luua kaustu `test` kausta sees, et struktureerida oma teste vastavalt soovile.

## Mine kaugemale

* Vähenda laienduse suurust ja paranda käivitusaega, [pakendades oma laienduse](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Avalda oma laiendus](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) VS Code laienduste turul.
* Automatiseeri ehitused, seadistades [Jätkuva Integratsiooni](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.