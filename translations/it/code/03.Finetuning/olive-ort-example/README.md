<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:31:50+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "it"
}
-->
# Affina Phi3 usando Olive

In questo esempio userai Olive per:

1. Affinare un adattatore LoRA per classificare le frasi in Sad, Joy, Fear, Surprise.
1. Unire i pesi dell’adattatore al modello base.
1. Ottimizzare e quantizzare il modello in `int4`.

Ti mostreremo anche come eseguire l’inferenza sul modello affinato usando l’API Generate di ONNX Runtime (ORT).

> **⚠️ Per l’affinamento, è necessario disporre di una GPU adeguata - ad esempio, una A10, V100, A100.**

## 💾 Installazione

Crea un nuovo ambiente virtuale Python (ad esempio, usando `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Successivamente, installa Olive e le dipendenze per il workflow di affinamento:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Affina Phi3 usando Olive
Il [file di configurazione Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) contiene un *workflow* con le seguenti *fasi*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

In sintesi, questo workflow:

1. Affina Phi3 (per 150 step, modificabili) usando i dati in [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Unisce i pesi dell’adattatore LoRA nel modello base, ottenendo un unico artefatto modello in formato ONNX.
1. Model Builder ottimizza il modello per ONNX runtime *e* lo quantizza in `int4`.

Per eseguire il workflow, lancia:

```bash
olive run --config phrase-classification.json
```

Al termine di Olive, il modello Phi3 affinato e ottimizzato in `int4` sarà disponibile in: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integra Phi3 affinato nella tua applicazione

Per eseguire l’app:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

La risposta sarà una classificazione a parola singola della frase (Sad/Joy/Fear/Surprise).

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale umana. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.