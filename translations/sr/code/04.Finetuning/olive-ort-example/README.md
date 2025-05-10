<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:47:29+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "sr"
}
-->
# Fino podešavanje Phi3 koristeći Olive

U ovom primeru koristićete Olive da:

1. Fino podesite LoRA adapter da klasifikuje fraze u Sad, Joy, Fear, Surprise.
1. Spojite težine adaptera u osnovni model.
1. Optimizujete i kvantizujete model u `int4`.

Takođe ćemo vam pokazati kako da izvršite inferencu fino podešenog modela koristeći ONNX Runtime (ORT) Generate API.

> **⚠️ Za fino podešavanje biće vam potrebna odgovarajuća GPU kartica - na primer, A10, V100, A100.**

## 💾 Instalacija

Kreirajte novi Python virtuelni okruženje (na primer, koristeći `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Zatim instalirajte Olive i zavisnosti za workflow fino podešavanja:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fino podešavanje Phi3 koristeći Olive  
[Olive konfiguracioni fajl](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) sadrži *workflow* sa sledećim *koracima*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Na visokom nivou, ovaj workflow će:

1. Fino podesiti Phi3 (za 150 koraka, što možete promeniti) koristeći podatke iz [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Spojiti težine LoRA adaptera u osnovni model. Time dobijate jedinstveni model u ONNX formatu.
1. Model Builder će optimizovati model za ONNX runtime *i* kvantizovati model u `int4`.

Da biste pokrenuli workflow, izvršite:

```bash
olive run --config phrase-classification.json
```

Kada Olive završi, vaš optimizovani `int4` fino podešeni Phi3 model biće dostupan u: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integracija fino podešenog Phi3 u vašu aplikaciju

Da pokrenete aplikaciju:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Odgovor treba da bude klasifikacija fraze u jednoj reči (Sad/Joy/Fear/Surprise).

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korišćenjem AI prevodilačke usluge [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo tačnosti, imajte na umu da automatski prevodi mogu sadržavati greške ili netačnosti. Originalni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prevod. Ne snosimo odgovornost za bilo kakva nesporazumevanja ili pogrešna tumačenja nastala korišćenjem ovog prevoda.