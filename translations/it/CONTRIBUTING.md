<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:28:08+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "it"
}
-->
# Contributing

Questo progetto accoglie contributi e suggerimenti. La maggior parte dei contributi richiede di accettare un Contributor License Agreement (CLA) che dichiari di avere il diritto e di concederci effettivamente i diritti per utilizzare il tuo contributo. Per maggiori dettagli, visita [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Quando invii una pull request, un bot CLA determinerà automaticamente se devi fornire un CLA e decorerà la PR di conseguenza (ad esempio, controllo dello stato, commento). Segui semplicemente le istruzioni fornite dal bot. Dovrai farlo una sola volta per tutti i repository che usano il nostro CLA.

## Codice di Condotta

Questo progetto ha adottato il [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
Per maggiori informazioni, leggi la [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) o contatta [opencode@microsoft.com](mailto:opencode@microsoft.com) per qualsiasi domanda o commento aggiuntivo.

## Avvertenze per la creazione di issue

Per favore, non aprire issue su GitHub per domande di supporto generali, poiché la lista GitHub dovrebbe essere utilizzata per richieste di funzionalità e segnalazioni di bug. In questo modo possiamo monitorare più facilmente i problemi o bug reali del codice e mantenere la discussione generale separata dal codice effettivo.

## Come contribuire

### Linee guida per le Pull Request

Quando invii una pull request (PR) al repository Phi-3 CookBook, segui queste linee guida:

- **Fork del repository**: Fai sempre il fork del repository nel tuo account prima di apportare modifiche.

- **Pull request separate (PR)**:
  - Invia ogni tipo di modifica in una PR separata. Per esempio, correzioni di bug e aggiornamenti della documentazione dovrebbero essere inviati in PR distinte.
  - Correzioni di refusi e piccoli aggiornamenti alla documentazione possono essere combinati in una singola PR quando appropriato.

- **Gestisci i conflitti di merge**: Se la tua pull request mostra conflitti di merge, aggiorna il tuo branch locale `main` per rispecchiare il repository principale prima di apportare modifiche.

- **Invio di traduzioni**: Quando invii una PR di traduzione, assicurati che la cartella di traduzione includa le traduzioni di tutti i file presenti nella cartella originale.

### Linee guida per la traduzione

> [!IMPORTANT]
>
> Quando traduci il testo in questo repository, non utilizzare traduzioni automatiche. Offriti come volontario solo per le lingue in cui sei competente.

Se conosci bene una lingua diversa dall’inglese, puoi aiutare a tradurre i contenuti. Segui questi passaggi per garantire che i tuoi contributi di traduzione vengano integrati correttamente, utilizzando le seguenti linee guida:

- **Crea la cartella di traduzione**: Vai alla cartella della sezione appropriata e crea una cartella di traduzione per la lingua a cui contribuisci. Per esempio:
  - Per la sezione introduttiva: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Per la sezione quick start: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Continua con questo schema per le altre sezioni (03.Inference, 04.Finetuning, ecc.)

- **Aggiorna i percorsi relativi**: Durante la traduzione, modifica la struttura delle cartelle aggiungendo `../../` all’inizio dei percorsi relativi all’interno dei file markdown per assicurarti che i link funzionino correttamente. Per esempio, modifica come segue:
  - Cambia `(../../imgs/01/phi3aisafety.png)` in `(../../../../imgs/01/phi3aisafety.png)`

- **Organizza le traduzioni**: Ogni file tradotto deve essere posizionato nella cartella di traduzione corrispondente della sezione. Per esempio, se traduci la sezione introduttiva in spagnolo, creerai:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Invia una PR completa**: Assicurati che tutti i file tradotti per una sezione siano inclusi in una sola PR. Non accettiamo traduzioni parziali per una sezione. Quando invii una PR di traduzione, assicurati che la cartella di traduzione includa tutte le traduzioni dei file presenti nella cartella originale.

### Linee guida per la scrittura

Per garantire coerenza tra tutti i documenti, usa le seguenti indicazioni:

- **Formattazione URL**: Inserisci tutti gli URL tra parentesi quadre seguite da parentesi tonde, senza spazi extra dentro o intorno. Per esempio: `[example](https://www.microsoft.com)`.

- **Link relativi**: Usa `./` per i link relativi a file o cartelle nella directory corrente e `../` per quelli nella directory superiore. Per esempio: `[example](../../path/to/file)` o `[example](../../../path/to/file)`.

- **Non usare localizzazioni specifiche per paese**: Assicurati che i tuoi link non includano localizzazioni specifiche per paese. Per esempio, evita `/en-us/` o `/en/`.

- **Archiviazione immagini**: Conserva tutte le immagini nella cartella `./imgs`.

- **Nomi descrittivi per le immagini**: Dai alle immagini nomi descrittivi usando caratteri inglesi, numeri e trattini. Per esempio: `example-image.jpg`.

## GitHub Workflows

Quando invii una pull request, i seguenti workflow verranno attivati per validare le modifiche. Segui le istruzioni qui sotto per assicurarti che la tua pull request superi i controlli:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Questo workflow verifica che tutti i percorsi relativi nei tuoi file siano corretti.

1. Per assicurarti che i tuoi link funzionino correttamente, esegui le seguenti operazioni usando VS Code:
    - Passa con il mouse su qualsiasi link nei tuoi file.
    - Premi **Ctrl + Click** per navigare al link.
    - Se clicchi su un link e non funziona localmente, attiverà il workflow e non funzionerà su GitHub.

1. Per risolvere questo problema, esegui le seguenti operazioni utilizzando i suggerimenti di percorso forniti da VS Code:
    - Digita `./` o `../`.
    - VS Code ti chiederà di scegliere tra le opzioni disponibili in base a quanto digitato.
    - Segui il percorso cliccando sul file o cartella desiderata per assicurarti che il percorso sia corretto.

Una volta aggiunto il percorso relativo corretto, salva e invia le modifiche.

### Check URLs Don't Have Locale

Questo workflow verifica che nessun URL web includa una localizzazione specifica per paese. Poiché questo repository è accessibile globalmente, è importante che gli URL non contengano la localizzazione del tuo paese.

1. Per verificare che i tuoi URL non abbiano localizzazioni di paese, esegui le seguenti operazioni:

    - Controlla testi come `/en-us/`, `/en/` o qualsiasi altra localizzazione linguistica negli URL.
    - Se questi non sono presenti nei tuoi URL, supererai questo controllo.

1. Per risolvere questo problema, esegui le seguenti operazioni:
    - Apri il file evidenziato dal workflow.
    - Rimuovi la localizzazione del paese dagli URL.

Una volta rimossa la localizzazione del paese, salva e invia le modifiche.

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
> Potrebbero verificarsi casi in cui il controllo degli URL fallisce anche se il link è accessibile. Questo può succedere per diversi motivi, tra cui:
>
> - **Restrizioni di rete:** I server di GitHub Actions potrebbero avere restrizioni di rete che impediscono l’accesso a certi URL.
> - **Problemi di timeout:** URL che impiegano troppo tempo a rispondere possono generare un errore di timeout nel workflow.
> - **Problemi temporanei del server:** Periodici downtime o manutenzioni possono rendere un URL temporaneamente non disponibile durante la validazione.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di considerare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale effettuata da un essere umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.