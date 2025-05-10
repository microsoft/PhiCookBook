<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-05-09T19:59:59+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "it"
}
-->
Questa demo mostra come utilizzare un modello pretrained per generare codice Python basato su un'immagine e un prompt di testo.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Ecco una spiegazione passo passo:

1. **Importazioni e configurazione**:
   - Vengono importate le librerie e i moduli necessari, inclusi `requests`, `PIL` per l'elaborazione delle immagini, e `transformers` per la gestione del modello e del processamento.

2. **Caricamento e visualizzazione dell'immagine**:
   - Un file immagine (`demo.png`) viene aperto utilizzando la libreria `PIL` e visualizzato.

3. **Definizione del prompt**:
   - Viene creato un messaggio che include l'immagine e la richiesta di generare codice Python per elaborare l'immagine e salvarla usando `plt` (matplotlib).

4. **Caricamento del Processor**:
   - Il `AutoProcessor` viene caricato da un modello pretrained specificato dalla directory `out_dir`. Questo processor gestirà gli input di testo e immagine.

5. **Creazione del prompt**:
   - Il metodo `apply_chat_template` viene utilizzato per formattare il messaggio in un prompt adatto al modello.

6. **Elaborazione degli input**:
   - Il prompt e l'immagine vengono trasformati in tensori comprensibili dal modello.

7. **Impostazione degli argomenti di generazione**:
   - Vengono definiti gli argomenti per il processo di generazione del modello, inclusi il numero massimo di nuovi token da generare e se effettuare il campionamento dell'output.

8. **Generazione del codice**:
   - Il modello genera il codice Python basato sugli input e sugli argomenti di generazione. Il `TextStreamer` viene utilizzato per gestire l'output, saltando il prompt e i token speciali.

9. **Output**:
   - Viene stampato il codice generato, che dovrebbe includere codice Python per elaborare l'immagine e salvarla come specificato nel prompt.

Questa demo illustra come sfruttare un modello pretrained usando OpenVino per generare codice dinamicamente basato sull'input dell'utente e sulle immagini.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di considerare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale umana. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.