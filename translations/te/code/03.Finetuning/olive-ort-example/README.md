<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-12-21T16:49:40+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "te"
}
-->
# Olive ఉపయోగించి Phi3 ఫైన్‑ట్యూన్ చేయండి

ఈ ఉదాహరణలో మీరు Olive ను ఉపయోగించి చేయబోతున్నవి:

1. వాక్యాలను Sad/Joy/Fear/Surprise గా వర్గీకరించడానికి LoRA అడాప్టర్‌ను ఫైన్‑ట్యూన్ చేయండి.
1. అడాప్టర్ వెయిట్స్‌ను బేస్ మోడల్‌లో మిళితం చేయండి.
1. మోడల్‌ను ఆప్టిమైజ్ చేసి `int4`లో క్వాంటైజ్ చేయండి.

> **⚠️ ఫైన్‑ట్యూనింగ్‌కు, మీ వద్ద ఒక అనుకూల GPU ఉండాలి — ఉదాహరణకు, A10, V100, A100.**

## 💾 Install

కొత్త Python వర్చువల్ పరిసరాన్ని సృష్టించండి (ఉదాహరణకి, `conda` ఉపయోగించి):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Next, install the Olive and the dependencies for a fine-tuning workflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive ఉపయోగించి Phi3 ఫైన్‑ట్యూన్ చేయండి
The [Olive configuration file](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) contains a *వర్క్‌ఫ్లో* with the following *పాస్‌లు*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

సామాన్యంగా, ఈ వర్క్‌ఫ్లో ఈ క్రింది పనులను చేస్తుంది:

1. Phi3 ను ఫైన్‑ట్యూన్ చేయండి (150 స్టెప్స్ కోసం, మీరు మార్చవచ్చు) using the [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) data.
1. Merge the LoRA adapter weights into the base model. This will give you a single model artifact in the ONNX format.
1. Model Builder will optimize the model for the ONNX runtime *and* quantize the model into `int4`.

To execute the workflow, run:

```bash
olive run --config phrase-classification.json
```

When Olive has completed, you're optimized `int4` fine-tuned Phi3 model is available in: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 ఫైన్‑ట్యూన్ చేయబడిన Phi3 ను మీ అప్లికేషన్‌లో ఇంటిగ్రేట్ చేయండి

యాప్‌ను চালించడానికి:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

This response should be a single word classification of the phrase (Sad/Joy/Fear/Surprise).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టం**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, స్వయంచాలక అనువాదాలలో తప్పులు లేదా లోపాలు ఉండవచ్చు అన్న విషయం దయచేసి గమనించండి. స్థానిక భాషలో ఉన్న మూల పత్రాన్ని అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి వృత్తిపరులైన మానవ అనువాదాన్ని సూచిస్తాము. ఈ అనువాదం వినియోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుగా అర్థం చేసుకోవడంపై మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->