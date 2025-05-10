<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:46:41+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "sw"
}
-->
# Fine-tune Phi3 kwa kutumia Olive

Katika mfano huu utatumia Olive ili:

1. Kufinyaza LoRA adapter ili kuainisha misemo kuwa Sad, Joy, Fear, Surprise.
1. Kuunganisha uzito wa adapter kwenye modeli ya msingi.
1. Kuboresha na Kuquantize modeli kuwa `int4`.

Pia tutaonyesha jinsi ya kufanya inference kwa modeli iliyofinyazwa kwa kutumia ONNX Runtime (ORT) Generate API.

> **⚠️ Kwa Fine-tuning, utahitaji GPU inayofaa - kwa mfano, A10, V100, A100.**

## 💾 Sakinisha

Tengeneza mazingira mapya ya Python virtual (kwa mfano, ukitumia `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Kisha, sakinisha Olive na utegemezi wa workflow ya fine-tuning:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fine-tune Phi3 kwa kutumia Olive
[Olive configuration file](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) ina *workflow* yenye *passes* zifuatazo:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Kwa ujumla, workflow hii itafanya:

1. Kufinyaza Phi3 (kwa hatua 150, unaweza kubadilisha) kwa kutumia data ya [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Kuunganisha uzito wa LoRA adapter kwenye modeli ya msingi. Hii itakupa kificho kimoja cha modeli katika muundo wa ONNX.
1. Model Builder itaboresha modeli kwa ONNX runtime *na* kuquantize modeli kuwa `int4`.

Ili kuendesha workflow, tumia amri:

```bash
olive run --config phrase-classification.json
```

Baada ya Olive kumaliza, modeli yako iliyofinyazwa, iliyoboreshwa na kuquantizewa ya `int4` itapatikana katika: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Unganisha Phi3 iliyofinyazwa kwenye programu yako

Ili kuendesha app:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Jibu litakuwa neno moja linaloainisha hali ya msemo (Sad/Joy/Fear/Surprise).

**Kisahafu**:  
Hati hii imetafsiriwa kwa kutumia huduma ya utafsiri wa AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuwa sahihi, tafadhali fahamu kuwa utafsiri wa kiotomatiki unaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.