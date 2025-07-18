<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-16T16:26:59+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "fi"
}
-->
# Hienosäädä Phi3 Olivea käyttäen

Tässä esimerkissä käytät Olivea:

1. Hienosäätämään LoRA-adapterin luokittelemaan lauseita Sad, Joy, Fear, Surprise -luokkiin.
1. Yhdistämään adapterin painot perusmalliin.
1. Optimoimaan ja kvantisoimaan malli `int4`-muotoon.

Näytämme myös, miten hienosäädettyä mallia käytetään ONNX Runtime (ORT) Generate API:n avulla.

> **⚠️ Hienosäätöä varten tarvitset sopivan GPU:n, esimerkiksi A10, V100 tai A100.**

## 💾 Asennus

Luo uusi Python-virtuaaliympäristö (esim. `conda`-komennolla):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Asenna sitten Olive ja hienosäätöön tarvittavat riippuvuudet:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Hienosäädä Phi3 Olivea käyttäen
[Olive-konfiguraatiotiedosto](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) sisältää *työnkulun*, jossa on seuraavat *vaiheet*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Yksinkertaisesti sanottuna tämä työnkulku:

1. Hienosäätää Phi3:n (150 askelta, jonka voit muuttaa) käyttäen [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) aineistoa.
1. Yhdistää LoRA-adapterin painot perusmalliin. Saat näin yhden mallin ONNX-muodossa.
1. ModelBuilder optimoi mallin ONNX Runtimea varten *ja* kvantisoi sen `int4`-muotoon.

Suorita työnkulku komennolla:

```bash
olive run --config phrase-classification.json
```

Kun Olive on valmis, optimoitu ja `int4`-kvantisoitu hienosäädetty Phi3-malli löytyy polusta: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integroi hienosäädetty Phi3 sovellukseesi

Käynnistä sovellus komennolla:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Vastaus on yksittäinen sana, joka luokittelee lauseen (Sad/Joy/Fear/Surprise).

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.