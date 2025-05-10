<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:34:16+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "ro"
}
-->
# Ajusta fin Phi3 folosind Olive

În acest exemplu vei folosi Olive pentru a:

1. Ajusta fin un adaptor LoRA pentru a clasifica fraze în Sad, Joy, Fear, Surprise.
1. Comasa greutățile adaptorului în modelul de bază.
1. Optimiza și cuantiza modelul în `int4`.

De asemenea, îți vom arăta cum să faci inferența modelului ajustat fin folosind ONNX Runtime (ORT) Generate API.

> **⚠️ Pentru ajustarea fină, vei avea nevoie de un GPU potrivit - de exemplu, un A10, V100, A100.**

## 💾 Instalare

Creează un nou mediu virtual Python (de exemplu, folosind `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Apoi, instalează Olive și dependențele pentru un flux de lucru de ajustare fină:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Ajustează fin Phi3 folosind Olive
Fișierul de configurare [Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) conține un *workflow* cu următoarele *pași*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

La un nivel înalt, acest workflow va:

1. Ajusta fin Phi3 (pentru 150 de pași, pe care îi poți modifica) folosind datele din [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Comasa greutățile adaptorului LoRA în modelul de bază. Acest lucru îți va oferi un singur artefact de model în format ONNX.
1. Model Builder va optimiza modelul pentru runtime-ul ONNX *și* va cuantiza modelul în `int4`.

Pentru a executa workflow-ul, rulează:

```bash
olive run --config phrase-classification.json
```

Când Olive a terminat, modelul tău Phi3 ajustat fin, optimizat și `int4` este disponibil în: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrează Phi3 ajustat fin în aplicația ta

Pentru a rula aplicația:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Răspunsul ar trebui să fie o clasificare într-un singur cuvânt a frazei (Sad/Joy/Fear/Surprise).

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.