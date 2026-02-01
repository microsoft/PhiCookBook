Questa demo mostra come utilizzare un modello pretrained per generare codice Python basato su un'immagine e un prompt testuale.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Ecco una spiegazione passo passo:

1. **Importazioni e Configurazione**:
   - Vengono importate le librerie e i moduli necessari, inclusi `requests`, `PIL` per l'elaborazione delle immagini, e `transformers` per la gestione del modello e del processamento.

2. **Caricamento e Visualizzazione dell'Immagine**:
   - Un file immagine (`demo.png`) viene aperto usando la libreria `PIL` e mostrato.

3. **Definizione del Prompt**:
   - Viene creato un messaggio che include l'immagine e una richiesta di generare codice Python per elaborare l'immagine e salvarla usando `plt` (matplotlib).

4. **Caricamento del Processor**:
   - L'`AutoProcessor` viene caricato da un modello pretrained specificato dalla directory `out_dir`. Questo processor gestirà gli input di testo e immagine.

5. **Creazione del Prompt**:
   - Il metodo `apply_chat_template` viene usato per formattare il messaggio in un prompt adatto al modello.

6. **Elaborazione degli Input**:
   - Il prompt e l'immagine vengono processati in tensori comprensibili dal modello.

7. **Impostazione degli Argomenti di Generazione**:
   - Vengono definiti gli argomenti per il processo di generazione del modello, inclusi il numero massimo di nuovi token da generare e se effettuare il campionamento dell'output.

8. **Generazione del Codice**:
   - Il modello genera il codice Python basandosi sugli input e sugli argomenti di generazione. Il `TextStreamer` viene utilizzato per gestire l'output, saltando il prompt e i token speciali.

9. **Output**:
   - Viene stampato il codice generato, che dovrebbe includere codice Python per elaborare l'immagine e salvarla come specificato nel prompt.

Questa demo illustra come sfruttare un modello pretrained usando OpenVino per generare codice dinamicamente basato su input utente e immagini.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.