<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T02:59:54+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "it"
}
-->
# Utilizzo della GPU Windows per creare una soluzione Prompt flow con Phi-3.5-Instruct ONNX

Il documento seguente è un esempio di come utilizzare PromptFlow con ONNX (Open Neural Network Exchange) per sviluppare applicazioni AI basate sui modelli Phi-3.

PromptFlow è una suite di strumenti di sviluppo progettata per semplificare l’intero ciclo di sviluppo di applicazioni AI basate su LLM (Large Language Model), dalla fase di ideazione e prototipazione fino a test e valutazione.

Integrando PromptFlow con ONNX, gli sviluppatori possono:

- Ottimizzare le prestazioni del modello: sfruttare ONNX per un’inferenza e un deployment efficienti del modello.
- Semplificare lo sviluppo: utilizzare PromptFlow per gestire il flusso di lavoro e automatizzare le attività ripetitive.
- Migliorare la collaborazione: facilitare una migliore collaborazione tra i membri del team offrendo un ambiente di sviluppo unificato.

**Prompt flow** è una suite di strumenti di sviluppo pensata per semplificare l’intero ciclo di sviluppo di applicazioni AI basate su LLM, dall’ideazione, prototipazione, test, valutazione fino al deployment in produzione e monitoraggio. Rende molto più semplice l’ingegneria dei prompt e permette di costruire app LLM con qualità da produzione.

Prompt flow può connettersi a OpenAI, Azure OpenAI Service e modelli personalizzabili (Huggingface, LLM/SLM locali). L’obiettivo è distribuire il modello ONNX quantizzato di Phi-3.5 su applicazioni locali. Prompt flow ci aiuta a pianificare meglio il nostro business e a completare soluzioni locali basate su Phi-3.5. In questo esempio, combineremo ONNX Runtime GenAI Library per realizzare la soluzione Prompt flow basata su GPU Windows.

## **Installazione**

### **ONNX Runtime GenAI per GPU Windows**

Leggi questa guida per configurare ONNX Runtime GenAI per GPU Windows [clicca qui](./ORTWindowGPUGuideline.md)

### **Configurare Prompt flow in VSCode**

1. Installa l’estensione Prompt flow per VS Code

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbe.it.png)

2. Dopo aver installato l’estensione Prompt flow per VS Code, clicca sull’estensione e scegli **Installation dependencies**; segui questa guida per installare il Prompt flow SDK nel tuo ambiente

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f.it.png)

3. Scarica il [Codice di esempio](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) e apri questo esempio con VS Code

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4.it.png)

4. Apri **flow.dag.yaml** per selezionare il tuo ambiente Python

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff.it.png)

   Apri **chat_phi3_ort.py** per modificare la posizione del tuo modello Phi-3.5-instruct ONNX

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45f.it.png)

5. Esegui il tuo prompt flow per il test

Apri **flow.dag.yaml** e clicca su visual editor

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603.it.png)

dopo aver cliccato, esegui il flusso per testarlo

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b.it.png)

1. Puoi eseguire batch nel terminale per verificare più risultati


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Puoi controllare i risultati nel tuo browser predefinito


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cb.it.png)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.