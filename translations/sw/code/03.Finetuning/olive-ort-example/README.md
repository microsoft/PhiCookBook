# Fanya marekebisho ya Phi3 kwa kutumia Olive

Katika mfano huu utatumia Olive ili:

1. Fanya marekebisho ya kipekee ya kiambatisho cha LoRA kwa ajili ya kuainisha misemo kuwa Huzuni, Furaha, Hofu, Mshangao.
1. Unganisha uzito wa kiambatisho kwenye mfano wa msingi.
1. Boresha na fanyia modeli Quantize kuwa `int4`.

Pia tutaonyesha jinsi ya kutekeleza modeli iliyorekebishwa kwa kutumia ONNX Runtime (ORT) Generate API.

> **⚠️ Kwa ajili ya marekebisho, utahitaji kuwa na GPU inayofaa - kwa mfano, A10, V100, A100.**

## 💾 Sakinisha

Tengeneza mazingira mapya ya Python (kwa mfano, ukitumia `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Kisha, sakinisha Olive na utegemezi wa mchakato wa marekebisho:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fanya marekebisho ya Phi3 kwa kutumia Olive
[Faili la usanidi la Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) lina *mchakato* wenye *hatua* zifuatazo:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Kwa muhtasari, mchakato huu uta:

1. Fanya marekebisho ya Phi3 (kwa hatua 150, ambazo unaweza kubadilisha) ukitumia data ya [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Unganisha uzito wa kiambatisho cha LoRA kwenye mfano wa msingi. Hii itakupa kifaa kimoja cha mfano katika muundo wa ONNX.
1. Model Builder itaboresha mfano kwa ajili ya ONNX runtime *na* kufanyia modeli Quantize kuwa `int4`.

Ili kuendesha mchakato, tumia amri:

```bash
olive run --config phrase-classification.json
```

Baada ya Olive kumaliza, modeli yako iliyorekebishwa na kuboreshwa ya `int4` itapatikana katika: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Unganisha Phi3 iliyorekebishwa kwenye programu yako

Ili kuendesha programu:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Jibu hili linapaswa kuwa aina moja ya maneno ya kuainisha msemo (Huzuni/Furaha/Hofu/Mshangao).

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.