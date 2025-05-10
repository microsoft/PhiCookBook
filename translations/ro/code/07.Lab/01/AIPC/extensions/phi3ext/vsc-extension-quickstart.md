<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-09T04:58:53+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "ro"
}
-->
# Welcome to your VS Code Extension

## Ce conține dosarul

* Acest dosar conține toate fișierele necesare pentru extensia ta.
* `package.json` - acesta este fișierul manifest în care îți declari extensia și comanda.
  * Pluginul exemplu înregistrează o comandă și definește titlul și numele comenzii. Cu aceste informații, VS Code poate afișa comanda în paleta de comenzi. Nu este nevoie să încarce pluginul încă.
* `src/extension.ts` - acesta este fișierul principal în care vei implementa comanda ta.
  * Fișierul exportă o funcție, `activate`, care este apelată prima dată când extensia este activată (în acest caz prin executarea comenzii). În interiorul funcției `activate` apelăm `registerCommand`.
  * Transmitem funcția care conține implementarea comenzii ca al doilea parametru către `registerCommand`.

## Configurare

* instalează extensiile recomandate (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner și dbaeumer.vscode-eslint)


## Pornește rapid

* Apasă `F5` pentru a deschide o fereastră nouă cu extensia ta încărcată.
* Rulează comanda ta din paleta de comenzi apăsând (`Ctrl+Shift+P` sau `Cmd+Shift+P` pe Mac) și tastând `Hello World`.
* Setează puncte de întrerupere în codul tău din `src/extension.ts` pentru a depana extensia.
* Găsește ieșirea extensiei în consola de depanare.

## Fă modificări

* Poți relansa extensia din bara de instrumente de depanare după ce modifici codul în `src/extension.ts`.
* De asemenea, poți reîncărca (`Ctrl+R` sau `Cmd+R` pe Mac) fereastra VS Code cu extensia ta pentru a încărca modificările.


## Explorează API-ul

* Poți deschide setul complet de API-uri când deschizi fișierul `node_modules/@types/vscode/index.d.ts`.

## Rulează teste

* Instalează [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Rulează task-ul "watch" prin comanda **Tasks: Run Task**. Asigură-te că acesta rulează, altfel testele s-ar putea să nu fie detectate.
* Deschide vizualizarea Testing din bara de activități și apasă butonul Run Test, sau folosește combinația de taste `Ctrl/Cmd + ; A`
* Vezi rezultatul testului în vizualizarea Test Results.
* Fă modificări în `src/test/extension.test.ts` sau creează fișiere noi de test în dosarul `test`.
  * Test runner-ul furnizat va lua în considerare doar fișierele care corespund modelului de nume `**.test.ts`.
  * Poți crea dosare în interiorul `test` pentru a-ți organiza testele cum dorești.

## Mergi mai departe

* Redu dimensiunea extensiei și îmbunătățește timpul de pornire prin [bundling-ul extensiei tale](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Publică extensia ta](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) pe marketplace-ul de extensii VS Code.
* Automatizează build-urile configurând [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere automată AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea în urma utilizării acestei traduceri.