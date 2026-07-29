# **Quantizzare la famiglia Phi utilizzando le estensioni di Intelligenza Artificiale Generativa per onnxruntime**

## **Cosa sono le estensioni di Intelligenza Artificiale Generativa per onnxruntime**

Queste estensioni ti aiutano a eseguire l'IA generativa con ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Forniscono il ciclo di intelligenza artificiale generativa per i modelli ONNX, inclusa l'inferenza con ONNX Runtime, l'elaborazione dei logits, la ricerca e il campionamento e la gestione della cache KV. Gli sviluppatori possono chiamare un metodo di alto livello generate() o eseguire ogni iterazione del modello in un ciclo, generando un token alla volta e aggiornando opzionalmente i parametri di generazione all'interno del ciclo. Supporta la ricerca greedy/beam e il campionamento TopP, TopK per generare sequenze di token e l'elaborazione integrata dei logits come le penalità di ripetizione. Puoi anche aggiungere facilmente una valutazione personalizzata.

A livello di applicazione, puoi usare le estensioni di Intelligenza Artificiale Generativa per onnxruntime per costruire applicazioni utilizzando C++/ C# / Python. A livello di modello, puoi usarle per unire modelli fine-tuned e svolgere lavori correlati di distribuzione quantitativa.


## **Quantizzazione di Phi-3.5 con le estensioni di Intelligenza Artificiale Generativa per onnxruntime**

### **Modelli supportati**

Le estensioni di Intelligenza Artificiale Generativa per onnxruntime supportano la conversione di quantizzazione di Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Model Builder nelle estensioni di Intelligenza Artificiale Generativa per onnxruntime**

Il model builder accelera notevolmente la creazione di modelli ONNX ottimizzati e quantizzati che funzionano con l'API generate() di ONNX Runtime.

Attraverso Model Builder, puoi quantizzare il modello in INT4, INT8, FP16, FP32 e combinare diversi metodi di accelerazione hardware come CPU, CUDA, DirectML, Mobile, ecc.

Per usare Model Builder è necessario installare

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Dopo l'installazione, puoi eseguire lo script Model Builder dal terminale per effettuare la conversione del formato e della quantizzazione del modello.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Comprendi i parametri rilevanti

1. **model_name** Questo è il modello su Hugging Face, come microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, ecc. Può anche essere il percorso dove memorizzi il modello

2. **path_to_output_folder** Percorso dove salvare la conversione quantizzata

3. **execution_provider** Supporto per diverse accelerazioni hardware, come cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Scarichiamo il modello da Hugging Face e lo memorizziamo nella cache localmente




***Nota：*** <ul>Anche se le estensioni di Intelligenza Artificiale Generativa per onnxruntime sono in anteprima, sono state incorporate in Microsoft Olive, e puoi anche chiamare le funzioni Model Builder delle estensioni di Intelligenza Artificiale Generativa per onnxruntime tramite Microsoft Olive.</ul>

## **Come usare Model Builder per quantizzare Phi-3.5**

Model Builder ora supporta la quantizzazione del modello ONNX per Phi-3.5 Instruct e Phi-3.5-Vision

### **Phi-3.5-Instruct**


**Conversione accelerata CPU di quantizzazione INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Conversione accelerata CUDA di quantizzazione INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Imposta l'ambiente nel terminale

```bash

mkdir models

cd models 

```

2. Scarica microsoft/Phi-3.5-vision-instruct nella cartella models
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Per favore scarica questi file nella tua cartella Phi-3.5-vision-instruct

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Scarica questo file nella cartella models
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Vai nel terminale

    Converti il supporto ONNX con FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Nota：**

1. Model Builder attualmente supporta la conversione di Phi-3.5-Instruct e Phi-3.5-Vision, ma non Phi-3.5-MoE

2. Per utilizzare il modello quantizzato ONNX, puoi usarlo tramite l’SDK delle estensioni di Intelligenza Artificiale Generativa per onnxruntime

3. Dobbiamo considerare un’IA più responsabile, quindi dopo la conversione di quantizzazione del modello si consiglia di effettuare test più efficaci sui risultati

4. Quantizzando il modello CPU INT4, possiamo distribuirlo su Edge Device, che ha migliori scenari applicativi, quindi abbiamo completato Phi-3.5-Instruct intorno a INT 4


## **Risorse**

1. Per saperne di più sulle estensioni di Intelligenza Artificiale Generativa per onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Repository GitHub delle estensioni di Intelligenza Artificiale Generativa per onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->