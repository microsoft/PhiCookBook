<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-16T16:03:17+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "it"
}
-->
# Fine-tune Phi3 usando Olive

In questo esempio userai Olive per:

1. Fine-tunare un adattatore LoRA per classificare frasi in Sad, Joy, Fear, Surprise.  
1. Unire i pesi dell’adattatore nel modello base.  
1. Ottimizzare e quantizzare il modello in `int4`.  

Ti mostreremo anche come eseguire l’inferenza sul modello fine-tunato usando l’ONNX Runtime (ORT) Generate API.

> **⚠️ Per il fine-tuning, è necessario disporre di una GPU adatta - ad esempio, una A10, V100, A100.**

## 💾 Installazione

Crea un nuovo ambiente virtuale Python (ad esempio, usando `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Successivamente, installa Olive e le dipendenze per un flusso di lavoro di fine-tuning:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fine-tune Phi3 usando Olive  
Il [file di configurazione Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) contiene un *workflow* con le seguenti *fasi*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

A grandi linee, questo workflow:

1. Fine-tunerà Phi3 (per 150 step, modificabili) usando i dati di [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).  
1. Fonderà i pesi dell’adattatore LoRA nel modello base, ottenendo un singolo artefatto modello in formato ONNX.  
1. Model Builder ottimizzerà il modello per l’ONNX runtime *e* lo quantizzerà in `int4`.  

Per eseguire il workflow, lancia:

```bash
olive run --config phrase-classification.json
```

Al termine di Olive, il modello Phi3 fine-tunato ottimizzato in `int4` sarà disponibile in: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrare Phi3 fine-tunato nella tua applicazione

Per eseguire l’app:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

La risposta sarà una classificazione a parola singola della frase (Sad/Joy/Fear/Surprise).

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.