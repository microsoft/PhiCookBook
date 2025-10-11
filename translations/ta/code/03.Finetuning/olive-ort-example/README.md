<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-10-11T11:36:51+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "ta"
}
-->
# Olive மூலம் Phi3-ஐ நன்றாகத் தகுவாக்குதல்

இந்த உதாரணத்தில், Olive-ஐ பயன்படுத்தி நீங்கள் செய்யப்போகிறீர்கள்:

1. Sad, Joy, Fear, Surprise ஆகியவற்றில் வாக்கியங்களை வகைப்படுத்த LoRA adapter-ஐ நன்றாகத் தகுவாக்குதல்.
1. Adapter எடைகளைக் அடிப்படை மாதிரியில் இணைத்தல்.
1. மாதிரியை `int4`-ஆக மேம்படுத்தி மற்றும் அளவீடு செய்தல்.

மேலும், ONNX Runtime (ORT) Generate API-யை பயன்படுத்தி நன்றாகத் தகுவாக்கப்பட்ட மாதிரியை inference செய்வது எப்படி என்பதை உங்களுக்குக் காட்டுவோம்.

> **⚠️ Fine-tuning செய்ய, உங்களுக்கு ஏற்ற GPU கிடைக்க வேண்டும் - உதாரணமாக, A10, V100, A100.**

## 💾 நிறுவல்

புதிய Python மெய்நிகர் சூழலை உருவாக்கவும் (உதாரணமாக, `conda` பயன்படுத்தி):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

அடுத்ததாக, Olive மற்றும் fine-tuning வேலைப்பாடுகளுக்கான சார்புகளை நிறுவவும்:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive மூலம் Phi3-ஐ நன்றாகத் தகுவாக்குதல்
[Olive configuration file](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) *workflow* கொண்டுள்ளது, இதில் பின்வரும் *passes* உள்ளன:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

இந்த workflow-ன் முக்கிய அம்சங்கள்:

1. [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) தரவைக் கொண்டு Phi3-ஐ (150 படிகள், நீங்கள் மாற்றலாம்) நன்றாகத் தகுவாக்குதல்.
1. LoRA adapter எடைகளை அடிப்படை மாதிரியில் இணைத்தல். இதனால் ONNX வடிவத்தில் ஒரு மாதிரி கலைப்பொருள் கிடைக்கும்.
1. Model Builder ONNX runtime-க்கு மாதிரியை மேம்படுத்தும் *மற்றும்* மாதிரியை `int4`-ஆக அளவீடு செய்யும்.

இந்த workflow-ஐ இயக்க, கீழே உள்ளதை இயக்கவும்:

```bash
olive run --config phrase-classification.json
```

Olive முடிந்தவுடன், உங்கள் `int4` நன்றாகத் தகுவாக்கப்பட்ட Phi3 மாதிரி கிடைக்கும்: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 உங்கள் பயன்பாட்டில் நன்றாகத் தகுவாக்கப்பட்ட Phi3-ஐ ஒருங்கிணைத்தல் 

அப்பிளிக்கேஷனை இயக்க:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

இந்த பதில் வாக்கியத்தின் வகைப்படுத்தலுக்கான ஒரு சொல் (Sad/Joy/Fear/Surprise) ஆக இருக்க வேண்டும்.

---

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.