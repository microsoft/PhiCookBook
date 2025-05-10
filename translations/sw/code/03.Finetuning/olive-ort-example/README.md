<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:33:43+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "sw"
}
-->
# Fine-tune Phi3 kutumia Olive

Katika mfano huu utatumia Olive kufanya:

1. Fine-tune LoRA adapter ili kuainisha misemo kuwa Sad, Joy, Fear, Surprise.
1. Unganisha uzito wa adapter kwenye modeli ya msingi.
1. Boreshaji na Quantize modeli kuwa `int4`.

Pia tutaonyesha jinsi ya kufanya inference ya modeli iliyofine-tune kutumia ONNX Runtime (ORT) Generate API.

> **⚠️ Kwa Fine-tuning, utahitaji kuwa na GPU inayofaa - kwa mfano, A10, V100, A100.**

## 💾 Sakinisha

Tengeneza mazingira mapya ya Python (kwa mfano, ukitumia `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Kisha, sakinisha Olive na utegemezi wa mtiririko wa fine-tuning:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fine-tune Phi3 kutumia Olive
[Olive configuration file](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) ina *workflow* yenye *passes* zifuatazo:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Kwa ujumla, workflow hii itafanya:

1. Fine-tune Phi3 (kwa hatua 150, unaweza kubadilisha) kwa kutumia data ya [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Unganisha uzito wa LoRA adapter kwenye modeli ya msingi. Hii itakupa kificho kimoja cha modeli kwa muundo wa ONNX.
1. Model Builder itaboresha modeli kwa ONNX runtime *na* kuitumia quantize kuwa `int4`.

Ili kuendesha workflow, tumia amri:

```bash
olive run --config phrase-classification.json
```

Baada ya Olive kumaliza, modeli yako ya Phi3 iliyofine-tune na kuboreshwa kwa `int4` itapatikana katika: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Unganisha Phi3 iliyofine-tune kwenye programu yako

Ili kuendesha app:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Jibu litakuwa aina moja ya maneno ya aina ya hisia ya msemo (Sad/Joy/Fear/Surprise).

**Kisahafu**:  
Hati hii imetafsiriwa kwa kutumia huduma ya utafsiri wa AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Nyaraka ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo halali. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatuna dhamana kwa maelewano mabaya au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.