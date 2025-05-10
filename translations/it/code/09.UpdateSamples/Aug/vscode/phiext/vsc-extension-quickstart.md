<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:34:41+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "it"
}
-->
# Benvenuto nella tua estensione VS Code

## Cosa c'è nella cartella

* Questa cartella contiene tutti i file necessari per la tua estensione.
* `package.json` - questo è il file manifest in cui dichiari la tua estensione e il comando.
  * Il plugin di esempio registra un comando e ne definisce il titolo e il nome. Con queste informazioni VS Code può mostrare il comando nella command palette. Non è ancora necessario caricare il plugin.
* `src/extension.ts` - questo è il file principale dove fornirai l’implementazione del tuo comando.
  * Il file esporta una funzione, `activate`, che viene chiamata la prima volta che la tua estensione viene attivata (in questo caso eseguendo il comando). All’interno della funzione `activate` chiamiamo `registerCommand`.
  * Passiamo la funzione contenente l’implementazione del comando come secondo parametro a `registerCommand`.

## Configurazione

* installa le estensioni consigliate (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner e dbaeumer.vscode-eslint)

## Inizia subito

* Premi `F5` per aprire una nuova finestra con la tua estensione caricata.
* Esegui il tuo comando dalla command palette premendo (`Ctrl+Shift+P` o `Cmd+Shift+P` su Mac) e digitando `Hello World`.
* Imposta breakpoint nel tuo codice all’interno di `src/extension.ts` per fare il debug della tua estensione.
* Trova l’output della tua estensione nella console di debug.

## Apporta modifiche

* Puoi rilanciare l’estensione dalla toolbar di debug dopo aver modificato il codice in `src/extension.ts`.
* Puoi anche ricaricare (`Ctrl+R` o `Cmd+R` su Mac) la finestra di VS Code con la tua estensione per caricare le modifiche.

## Esplora l’API

* Puoi aprire l’intero set della nostra API aprendo il file `node_modules/@types/vscode/index.d.ts`.

## Esegui i test

* Installa [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Esegui il task "watch" tramite il comando **Tasks: Run Task**. Assicurati che sia in esecuzione, altrimenti i test potrebbero non essere rilevati.
* Apri la vista Testing dalla barra delle attività e clicca il pulsante "Run Test", oppure usa la scorciatoia `Ctrl/Cmd + ; A`
* Visualizza l’output dei risultati del test nella vista Test Results.
* Modifica `src/test/extension.test.ts` o crea nuovi file di test all’interno della cartella `test`.
  * Il test runner fornito considererà solo i file che corrispondono al pattern di nome `**.test.ts`.
  * Puoi creare cartelle all’interno della cartella `test` per organizzare i tuoi test come preferisci.

## Vai oltre

* Riduci le dimensioni dell’estensione e migliora i tempi di avvio [bundling your extension](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Pubblica la tua estensione](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) sul marketplace delle estensioni di VS Code.
* Automatizza le build configurando [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale effettuata da un umano. Non ci assumiamo responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.