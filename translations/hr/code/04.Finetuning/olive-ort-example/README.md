# Fino podešavanje Phi3 pomoću Olive

U ovom primjeru koristit ćete Olive za:

1. Fino podešavanje LoRA adaptera za klasifikaciju fraza u Tužno, Radost, Strah, Iznenađenje.
1. Spajanje težina adaptera u osnovni model.
1. Optimizaciju i kvantizaciju modela u `int4`.

Također ćemo vam pokazati kako izvršiti inferenciju fino podešenog modela koristeći ONNX Runtime (ORT) Generate API.

> **⚠️ Za fino podešavanje potrebno je imati odgovarajuću GPU karticu - na primjer, A10, V100, A100.**

## 💾 Instalacija

Kreirajte novo Python virtualno okruženje (na primjer, koristeći `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Zatim instalirajte Olive i ovisnosti za tijek rada fino podešavanja:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fino podešavanje Phi3 pomoću Olive
[Olive konfiguracijska datoteka](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) sadrži *workflow* sa sljedećim *koracima*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Na visokoj razini, ovaj workflow će:

1. Fino podesiti Phi3 (za 150 koraka, što možete promijeniti) koristeći podatke iz [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Spojiti težine LoRA adaptera u osnovni model. Time ćete dobiti jedan model u ONNX formatu.
1. Model Builder će optimizirati model za ONNX runtime *i* kvantizirati model u `int4`.

Za pokretanje workflowa, izvršite:

```bash
olive run --config phrase-classification.json
```

Kada Olive završi, vaš optimizirani `int4` fino podešeni Phi3 model bit će dostupan u: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integracija fino podešenog Phi3 u vašu aplikaciju

Za pokretanje aplikacije:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Ovaj odgovor trebao bi biti jedinstvena riječ koja klasificira frazu (Tužno/Radost/Strah/Iznenađenje).

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.