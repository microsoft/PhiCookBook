<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-07-16T14:40:27+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "it"
}
-->
# Contribuire

Questo progetto accoglie contributi e suggerimenti. La maggior parte dei contributi richiede l'accettazione di un
Contributor License Agreement (CLA) che dichiara che hai il diritto e effettivamente concedi a noi
i diritti di utilizzare il tuo contributo. Per maggiori dettagli, visita [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Quando invii una pull request, un bot CLA determinerà automaticamente se è necessario fornire
un CLA e decorerà la PR di conseguenza (ad esempio, controllo dello stato, commento). Segui semplicemente le istruzioni
fornite dal bot. Dovrai farlo solo una volta per tutti i repository che utilizzano il nostro CLA.

## Codice di Condotta

Questo progetto ha adottato il [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Per maggiori informazioni leggi le [FAQ sul Codice di Condotta](https://opensource.microsoft.com/codeofconduct/faq/) o contatta [opencode@microsoft.com](mailto:opencode@microsoft.com) per domande o commenti aggiuntivi.

## Avvertenze per la creazione di issue

Per favore, non aprire issue su GitHub per domande di supporto generali, poiché la lista GitHub dovrebbe essere usata per richieste di funzionalità e segnalazioni di bug. In questo modo possiamo tracciare più facilmente problemi o bug reali nel codice e mantenere la discussione generale separata dal codice vero e proprio.

## Come Contribuire

### Linee guida per le Pull Request

Quando invii una pull request (PR) al repository Phi-3 CookBook, segui queste linee guida:

- **Fork del Repository**: Effettua sempre il fork del repository sul tuo account prima di apportare modifiche.

- **Pull request separate (PR)**:
  - Invia ogni tipo di modifica in una pull request separata. Ad esempio, correzioni di bug e aggiornamenti della documentazione dovrebbero essere inviati in PR distinte.
  - Correzioni di refusi e aggiornamenti minori della documentazione possono essere combinati in un’unica PR quando appropriato.

- **Gestione dei conflitti di merge**: Se la tua pull request mostra conflitti di merge, aggiorna il tuo branch `main` locale per rispecchiare il repository principale prima di apportare modifiche.

- **Invio di traduzioni**: Quando invii una PR di traduzione, assicurati che la cartella della traduzione includa le traduzioni di tutti i file presenti nella cartella originale.

### Linee guida di scrittura

Per garantire coerenza in tutti i documenti, utilizza le seguenti indicazioni:

- **Formattazione URL**: Inserisci tutti gli URL tra parentesi quadre seguite da parentesi tonde, senza spazi aggiuntivi dentro o intorno. Ad esempio: `[example](https://www.microsoft.com)`.

- **Link relativi**: Usa `./` per link relativi a file o cartelle nella directory corrente, e `../` per quelli nella directory superiore. Ad esempio: `[example](../../path/to/file)` o `[example](../../../path/to/file)`.

- **Locali non specifici per paese**: Assicurati che i tuoi link non includano locali specifici per paese. Ad esempio, evita `/en-us/` o `/en/`.

- **Archiviazione immagini**: Conserva tutte le immagini nella cartella `./imgs`.

- **Nomi descrittivi per le immagini**: Dai alle immagini nomi descrittivi usando caratteri inglesi, numeri e trattini. Ad esempio: `example-image.jpg`.

## Workflow di GitHub

Quando invii una pull request, i seguenti workflow verranno attivati per convalidare le modifiche. Segui le istruzioni qui sotto per assicurarti che la tua pull request superi i controlli del workflow:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Questo workflow verifica che tutti i percorsi relativi nei tuoi file siano corretti.

1. Per assicurarti che i tuoi link funzionino correttamente, esegui le seguenti operazioni usando VS Code:
    - Passa il mouse su qualsiasi link nei tuoi file.
    - Premi **Ctrl + Click** per navigare al link.
    - Se clicchi su un link e non funziona localmente, attiverà il workflow e non funzionerà su GitHub.

1. Per risolvere questo problema, esegui le seguenti operazioni usando i suggerimenti di percorso forniti da VS Code:
    - Digita `./` o `../`.
    - VS Code ti proporrà le opzioni disponibili in base a quanto digitato.
    - Segui il percorso cliccando sul file o sulla cartella desiderata per assicurarti che il percorso sia corretto.

Una volta aggiunto il percorso relativo corretto, salva e invia le modifiche.

### Check URLs Don't Have Locale

Questo workflow verifica che nessun URL web includa un locale specifico per paese. Poiché questo repository è accessibile globalmente, è importante assicurarsi che gli URL non contengano il locale del tuo paese.

1. Per verificare che i tuoi URL non contengano locali di paese, esegui le seguenti operazioni:

    - Controlla la presenza di testi come `/en-us/`, `/en/` o qualsiasi altro locale linguistico negli URL.
    - Se questi non sono presenti nei tuoi URL, supererai questo controllo.

1. Per risolvere questo problema, esegui le seguenti operazioni:
    - Apri il file indicato dal workflow.
    - Rimuovi il locale di paese dagli URL.

Una volta rimosso il locale di paese, salva e invia le modifiche.

### Check Broken Urls

Questo workflow verifica che ogni URL web nei tuoi file funzioni correttamente e restituisca un codice di stato 200.

1. Per verificare che i tuoi URL funzionino correttamente, esegui le seguenti operazioni:
    - Controlla lo stato degli URL nei tuoi file.

2. Per correggere eventuali URL non funzionanti, esegui le seguenti operazioni:
    - Apri il file che contiene l’URL non funzionante.
    - Aggiorna l’URL con quello corretto.

Una volta corretto l’URL, salva e invia le modifiche.

> [!NOTE]
>
> Potrebbero verificarsi casi in cui il controllo degli URL fallisce anche se il link è accessibile. Questo può accadere per diversi motivi, tra cui:
>
> - **Restrizioni di rete:** I server delle GitHub actions potrebbero avere restrizioni di rete che impediscono l’accesso a certi URL.
> - **Problemi di timeout:** URL che impiegano troppo tempo a rispondere possono causare un errore di timeout nel workflow.
> - **Problemi temporanei del server:** Interruzioni occasionali o manutenzioni del server possono rendere un URL temporaneamente non disponibile durante la validazione.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.