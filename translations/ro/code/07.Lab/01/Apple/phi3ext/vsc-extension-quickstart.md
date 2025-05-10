<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:10:22+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "ro"
}
-->
# Bine ai venit la extensia ta VS Code

## Ce conține folderul

* Acest folder conține toate fișierele necesare pentru extensia ta.
* `package.json` - acesta este fișierul manifest în care îți declari extensia și comanda.
  * Pluginul exemplu înregistrează o comandă și definește titlul și numele comenzii. Cu aceste informații, VS Code poate afișa comanda în paleta de comenzi. Nu este necesar să încarce pluginul încă.
* `src/extension.ts` - acesta este fișierul principal unde vei oferi implementarea comenzii tale.
  * Fișierul exportă o funcție, `activate`, care este apelată prima dată când extensia ta este activată (în acest caz prin executarea comenzii). În interiorul funcției `activate` apelăm `registerCommand`.
  * Transmitem funcția care conține implementarea comenzii ca al doilea parametru pentru `registerCommand`.

## Configurare

* instalează extensiile recomandate (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner și dbaeumer.vscode-eslint)


## Pornește rapid

* Apasă `F5` pentru a deschide o fereastră nouă cu extensia ta încărcată.
* Rulează comanda din paleta de comenzi apăsând (`Ctrl+Shift+P` sau `Cmd+Shift+P` pe Mac) și tastând `Hello World`.
* Setează puncte de întrerupere în codul tău din `src/extension.ts` pentru a depana extensia.
* Găsește ieșirea extensiei tale în consola de depanare.

## Fă modificări

* Poți relansa extensia din bara de instrumente de depanare după ce modifici codul din `src/extension.ts`.
* De asemenea, poți reîncărca (`Ctrl+R` sau `Cmd+R` pe Mac) fereastra VS Code cu extensia ta pentru a încărca modificările.


## Explorează API-ul

* Poți deschide setul complet al API-ului nostru când deschizi fișierul `node_modules/@types/vscode/index.d.ts`.

## Rulează teste

* Instalează [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Rulează task-ul "watch" prin comanda **Tasks: Run Task**. Asigură-te că rulează, altfel testele s-ar putea să nu fie detectate.
* Deschide vizualizarea Testing din bara de activități și apasă butonul Run Test, sau folosește combinația de taste rapidă `Ctrl/Cmd + ; A`
* Vezi rezultatul testelor în vizualizarea Test Results.
* Fă modificări în `src/test/extension.test.ts` sau creează fișiere noi de test în folderul `test`.
  * Test runner-ul oferit va lua în considerare doar fișierele care corespund pattern-ului de nume `**.test.ts`.
  * Poți crea foldere în interiorul folderului `test` pentru a-ți structura testele cum dorești.

## Mergi mai departe

* Redu dimensiunea extensiei și îmbunătățește timpul de pornire prin [împachetarea extensiei](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publică extensia ta](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) pe marketplace-ul de extensii VS Code.
* Automatizează build-urile configurând [Integrarea Continuă](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un traducător uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea ca urmare a utilizării acestei traduceri.