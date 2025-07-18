<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-16T16:06:05+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "sr"
}
-->
# Фино подешавање Phi3 користећи Olive

У овом примеру ћете користити Olive да:

1. Фино подесите LoRA адаптер за класификацију фраза у Тужан, Радост, Страх, Изненађење.
1. Спојите тежине адаптера у основни модел.
1. Оптимизујете и квантујете модел у `int4`.

Такође ћемо вам показати како да извршите инференцу фино подешеног модела користећи ONNX Runtime (ORT) Generate API.

> **⚠️ За фино подешавање потребно је да имате одговарајућу GPU картицу - на пример, A10, V100, A100.**

## 💾 Инсталација

Креирајте ново Python виртуелно окружење (на пример, користећи `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Затим инсталирајте Olive и зависности за фино подешавање:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Фино подешавање Phi3 користећи Olive
[Olive конфигурациони фајл](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) садржи *workflow* са следећим *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

На високом нивоу, овај workflow ће:

1. Фино подесити Phi3 (за 150 корака, што можете променити) користећи податке из [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Спојити тежине LoRA адаптера у основни модел. Ово ће вам дати један модел у ONNX формату.
1. Model Builder ће оптимизовати модел за ONNX runtime *и* квантовати модел у `int4`.

Да бисте покренули workflow, извршите:

```bash
olive run --config phrase-classification.json
```

Када Olive заврши, ваш оптимизовани `int4` фино подешени Phi3 модел биће доступан у: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Интегрисање фино подешеног Phi3 у вашу апликацију

Да покренете апликацију:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Овај одговор треба да буде једна реч која класификује фразу (Тужан/Радост/Страх/Изненађење).

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.