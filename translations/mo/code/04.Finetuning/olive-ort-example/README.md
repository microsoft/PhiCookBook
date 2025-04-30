<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aed7639909ebbd1960507880cff2ae4c",
  "translation_date": "2025-04-04T11:28:38+00:00",
  "source_file": "code\\04.Finetuning\\olive-ort-example\\README.md",
  "language_code": "mo"
}
-->
# Fine-tune Phi3 mo Olive

A cikin wannan misali za ku yi amfani da Olive don:

1. Yin gyaran LoRA adapter don rarraba jimloli zuwa Sad, Joy, Fear, Surprise.
1. Haɗa nauyin adapter zuwa samfurin asali.
1. Inganta da Quantize samfurin cikin `int4`.

Za mu kuma nuna muku yadda za ku yi amfani da samfurin da aka gyara ta amfani da ONNX Runtime (ORT) Generate API.

> **⚠️ Don yin gyara, kuna buƙatar samun GPU mai dacewa - misali, A10, V100, A100.**

## 💾 Shigarwa

Ƙirƙiri sabuwar yanayin Python virtual (misali, ta amfani da `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Bayan haka, shigar da Olive da kuma abubuwan da ake buƙata don tsarin gyaran aiki:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Yin gyara Phi3 ta amfani da Olive
[Olive configuration file](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) tana ɗauke da *workflow* tare da waɗannan *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

A matakin gabaɗaya, wannan workflow ɗin zai:

1. Yi gyaran Phi3 (na matakai 150, wanda za ku iya canzawa) ta amfani da [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) bayanai.
1. Haɗa nauyin LoRA adapter zuwa samfurin asali. Wannan zai ba ku samfur guda ɗaya a cikin ONNX format.
1. Model Builder zai inganta samfurin don ONNX runtime *da* quantize samfurin cikin `int4`.

Don aiwatar da workflow ɗin, gudu:

```bash
olive run --config phrase-classification.json
```

Lokacin da Olive ta gama, an gyara `int4` samfurin Phi3 ɗinku wanda aka inganta yana samuwa a: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Haɗa Phi3 da aka gyara cikin aikinku 

Don gudu da app ɗin:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Wannan amsa ya kamata ya kasance kalma ɗaya wanda ke rarraba jimlar (Sad/Joy/Fear/Surprise).

It seems like you've asked to translate the text to "mo," but could you clarify what "mo" refers to? Are you referring to a specific language or dialect? Examples might include Maori, Montenegrin, or something else. Let me know so I can assist you accurately!