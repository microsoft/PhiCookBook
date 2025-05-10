<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:34:38+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "hr"
}
-->
# Fino podešavanje Phi3 pomoću Olive

U ovom primjeru koristit ćete Olive za:

1. Fino podešavanje LoRA adaptera za klasifikaciju fraza u Sad, Joy, Fear, Surprise.
1. Spajanje težina adaptera u osnovni model.
1. Optimizaciju i kvantizaciju modela u `int4`.

Također ćemo vam pokazati kako izvesti inferenciju fino podešenog modela koristeći ONNX Runtime (ORT) Generate API.

> **⚠️ Za fino podešavanje, potrebno je imati odgovarajuću GPU karticu - na primjer, A10, V100, A100.**

## 💾 Instalacija

Kreirajte novo Python virtualno okruženje (na primjer, koristeći `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Zatim instalirajte Olive i ovisnosti za tijek fino podešavanja:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fino podešavanje Phi3 pomoću Olive
[Olive konfiguracijska datoteka](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) sadrži *workflow* sa sljedećim *passovima*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Na visokoj razini, ovaj workflow će:

1. Fino podesiti Phi3 (za 150 koraka, što možete promijeniti) koristeći podatke iz [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Spojiti LoRA adapter težine u osnovni model. To će vam dati jedan model u ONNX formatu.
1. Model Builder će optimizirati model za ONNX runtime *i* kvantizirati model u `int4`.

Za pokretanje workflowa, pokrenite:

```bash
olive run --config phrase-classification.json
```

Kada Olive završi, vaš optimizirani i fino podešeni Phi3 model u `int4` formatu dostupan je u: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integracija fino podešenog Phi3 u vašu aplikaciju

Za pokretanje aplikacije:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Ovaj odgovor trebao bi biti jednoredna klasifikacija fraze (Sad/Joy/Fear/Surprise).

**Odricanje od odgovornosti**:  
Ovaj dokument preveden je korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili kriva tumačenja proizašla iz korištenja ovog prijevoda.