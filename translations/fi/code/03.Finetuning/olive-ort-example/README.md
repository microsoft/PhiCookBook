<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:32:49+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "fi"
}
-->
# Hienosäädä Phi3 Olivea käyttäen

Tässä esimerkissä käytät Olivea:

1. Hienosäätämään LoRA-adapteria luokittelemaan lauseita Sad, Joy, Fear, Surprise.
1. Yhdistämään adapterin painot perusmalliin.
1. Optimoimaan ja kvantisoimaan malli `int4`-muotoon.

Näytämme myös, miten hienosäädettyä mallia käytetään ONNX Runtime (ORT) Generate API:n avulla.

> **⚠️ Hienosäätöä varten tarvitset sopivan GPU:n, esimerkiksi A10, V100, A100.**

## 💾 Asennus

Luo uusi Python-virtuaaliympäristö (esimerkiksi käyttämällä `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Asenna sen jälkeen Olive ja hienosäätöön tarvittavat riippuvuudet:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Hienosäädä Phi3 Olivea käyttäen
[Olive-konfiguraatiotiedosto](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) sisältää *työnkulun*, jossa on seuraavat *vaiheet*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Yksinkertaisesti tämä työnkulku:

1. Hienosäätää Phi3:ta (150 askelta, jota voit muuttaa) käyttäen dataa tiedostosta [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Yhdistää LoRA-adapterin painot perusmalliin. Saat näin yhden mallin ONNX-muodossa.
1. Model Builder optimoi mallin ONNX-ajoympäristölle *ja* kvantisoi sen `int4`-muotoon.

Suorita työnkulku komennolla:

```bash
olive run --config phrase-classification.json
```

Kun Olive on valmis, optimoitu ja hienosäädetty `int4`-malli löytyy polusta: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integroi hienosäädetty Phi3 sovellukseesi

Suorita sovellus komennolla:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Vastaus on yksittäinen sanaluokitus lauseelle (Sad/Joy/Fear/Surprise).

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virhetulkinnoista.