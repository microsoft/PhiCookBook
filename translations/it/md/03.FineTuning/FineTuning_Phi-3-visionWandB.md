<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-07-17T08:09:27+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "it"
}
-->
# Panoramica del Progetto Phi-3-Vision-128K-Instruct

## Il Modello

Il Phi-3-Vision-128K-Instruct, un modello multimodale leggero e all’avanguardia, è il cuore di questo progetto. Fa parte della famiglia di modelli Phi-3 e supporta una lunghezza di contesto fino a 128.000 token. Il modello è stato addestrato su un dataset variegato che include dati sintetici e siti web pubblici accuratamente filtrati, con un’enfasi su contenuti di alta qualità e ad alto livello di ragionamento. Il processo di addestramento ha previsto un fine-tuning supervisionato e un’ottimizzazione diretta delle preferenze per garantire un’aderenza precisa alle istruzioni, oltre a robuste misure di sicurezza.

## Creare dati di esempio è fondamentale per diversi motivi:

1. **Test**: I dati di esempio permettono di testare l’applicazione in vari scenari senza influenzare i dati reali. Questo è particolarmente importante nelle fasi di sviluppo e staging.

2. **Ottimizzazione delle prestazioni**: Con dati di esempio che riproducono scala e complessità dei dati reali, è possibile individuare colli di bottiglia nelle prestazioni e ottimizzare l’applicazione di conseguenza.

3. **Prototipazione**: I dati di esempio possono essere usati per creare prototipi e mockup, utili per comprendere le esigenze degli utenti e raccogliere feedback.

4. **Analisi dei dati**: In ambito data science, i dati di esempio sono spesso utilizzati per analisi esplorative, addestramento di modelli e test di algoritmi.

5. **Sicurezza**: Usare dati di esempio negli ambienti di sviluppo e test aiuta a prevenire perdite accidentali di dati sensibili reali.

6. **Apprendimento**: Se stai imparando una nuova tecnologia o strumento, lavorare con dati di esempio offre un modo pratico per applicare quanto appreso.

Ricorda che la qualità dei dati di esempio può influenzare significativamente queste attività. Devono essere il più possibile simili ai dati reali in termini di struttura e variabilità.

### Creazione di dati di esempio
[Generate DataSet Script](./CreatingSampleData.md)

## Dataset

Un buon esempio di dataset di esempio è il [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (disponibile su Huggingface).  
Il dataset di esempio dei prodotti Burberry include anche i metadati relativi alla categoria del prodotto, prezzo e titolo, con un totale di 3.040 righe, ciascuna rappresentante un prodotto unico. Questo dataset ci permette di testare la capacità del modello di comprendere e interpretare dati visivi, generando testi descrittivi che catturano dettagli visivi complessi e caratteristiche specifiche del brand.

**Note:** Puoi utilizzare qualsiasi dataset che includa immagini.

## Ragionamento Complesso

Il modello deve ragionare su prezzi e denominazioni basandosi solo sull’immagine. Questo richiede al modello non solo di riconoscere le caratteristiche visive, ma anche di comprenderne le implicazioni in termini di valore del prodotto e branding. Sintetizzando descrizioni testuali accurate dalle immagini, il progetto mette in luce il potenziale dell’integrazione dei dati visivi per migliorare le prestazioni e la versatilità dei modelli in applicazioni reali.

## Architettura Phi-3 Vision

L’architettura del modello è una versione multimodale di Phi-3. Elabora sia dati testuali che immagini, integrando questi input in una sequenza unificata per compiti di comprensione e generazione completi. Il modello utilizza layer di embedding separati per testo e immagini. I token testuali vengono convertiti in vettori densi, mentre le immagini sono elaborate tramite un modello di visione CLIP per estrarre embedding delle caratteristiche. Questi embedding delle immagini vengono poi proiettati per corrispondere alle dimensioni degli embedding testuali, garantendo un’integrazione fluida.

## Integrazione degli Embedding di Testo e Immagine

Token speciali all’interno della sequenza testuale indicano dove inserire gli embedding delle immagini. Durante l’elaborazione, questi token speciali vengono sostituiti con gli embedding corrispondenti, permettendo al modello di gestire testo e immagini come un’unica sequenza. Il prompt per il nostro dataset è formattato usando il token speciale <|image|> come segue:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Codice di esempio
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Esempio walkthrough di Weights and Bias](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.