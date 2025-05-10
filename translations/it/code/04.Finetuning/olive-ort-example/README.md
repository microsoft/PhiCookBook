<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:44:51+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "it"
}
-->
# Messa a punto di Phi3 usando Olive

In questo esempio userai Olive per:

1. Messa a punto di un adattatore LoRA per classificare frasi in Sad, Joy, Fear, Surprise.
1. Unire i pesi dell’adattatore nel modello base.
1. Ottimizzare e quantizzare il modello in `int4`.

Ti mostreremo anche come effettuare l’inferenza con il modello messo a punto usando l’ONNX Runtime (ORT) Generate API.

> **⚠️ Per la messa a punto, è necessario disporre di una GPU adeguata - ad esempio, una A10, V100, A100.**

## 💾 Installazione

Crea un nuovo ambiente virtuale Python (ad esempio, usando `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Poi, installa Olive e le dipendenze per il workflow di messa a punto:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Messa a punto di Phi3 usando Olive
Il [file di configurazione Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) contiene un *workflow* con le seguenti *fasi*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

A grandi linee, questo workflow:

1. Mette a punto Phi3 (per 150 step, modificabili) usando i dati di [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Unisce i pesi dell’adattatore LoRA nel modello base, ottenendo un singolo artefatto modello in formato ONNX.
1. Model Builder ottimizza il modello per l’ONNX runtime *e* quantizza il modello in `int4`.

Per eseguire il workflow, lancia:

```bash
olive run --config phrase-classification.json
```

Al termine di Olive, il modello Phi3 ottimizzato e messo a punto in `int4` sarà disponibile in: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrare Phi3 messo a punto nella tua applicazione

Per eseguire l’app:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

La risposta sarà una classificazione a parola singola della frase (Sad/Joy/Fear/Surprise).

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di considerare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua madre deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.