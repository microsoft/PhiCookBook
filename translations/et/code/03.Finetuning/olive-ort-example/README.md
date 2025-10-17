<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-10-11T11:37:00+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "et"
}
-->
# Kohanda Phi3 Olive'i abil

Selles näites kasutad Olive'i, et:

1. Kohandada LoRA adapterit fraaside klassifitseerimiseks kategooriatesse Kurb, Rõõm, Hirm, Üllatus.
2. Ühendada adapteri kaalud baasmudeliga.
3. Optimeerida ja kvantiseerida mudel `int4` formaati.

Näitame ka, kuidas teha järeldusi kohandatud mudeliga, kasutades ONNX Runtime (ORT) Generate API-d.

> **⚠️ Kohandamiseks on vaja sobivat GPU-d - näiteks A10, V100, A100.**

## 💾 Paigaldamine

Loo uus Python'i virtuaalne keskkond (näiteks kasutades `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Seejärel paigalda Olive ja sõltuvused kohandamise töövoo jaoks:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Kohanda Phi3 Olive'i abil
[Olive'i konfiguratsioonifail](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) sisaldab *töövoogu* järgmiste *etappidega*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Kõrgtasemel teeb see töövoog järgmist:

1. Kohandab Phi3 (150 sammu jooksul, mida saab muuta) kasutades [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) andmeid.
2. Ühendab LoRA adapteri kaalud baasmudeliga. Selle tulemusena saad ühe mudeli artefakti ONNX formaadis.
3. Model Builder optimeerib mudeli ONNX runtime'i jaoks *ja* kvantiseerib mudeli `int4` formaati.

Töövoo käivitamiseks käivita:

```bash
olive run --config phrase-classification.json
```

Kui Olive on lõpetanud, on optimeeritud `int4` kohandatud Phi3 mudel saadaval: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Kohandatud Phi3 integreerimine oma rakendusse 

Rakenduse käivitamiseks:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Vastus peaks olema fraasi ühe sõnaga klassifikatsioon (Kurb/Rõõm/Hirm/Üllatus).

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.