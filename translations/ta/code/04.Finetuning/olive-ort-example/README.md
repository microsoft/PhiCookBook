<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-10-11T11:38:53+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "ta"
}
-->
# Olive-ஐ பயன்படுத்தி Phi3-ஐ Fine-tune செய்யவும்

இந்த எடுத்துக்காட்டில், Olive-ஐ பயன்படுத்தி நீங்கள் செய்யப்போகிறீர்கள்:

1. LoRA adapter-ஐ fine-tune செய்து Sad, Joy, Fear, Surprise ஆகிய பிரிவுகளாக வாக்கியங்களை வகைப்படுத்தவும்.
2. Adapter எடைகளைக் அடிப்படை மாதிரியில் இணைக்கவும்.
3. மாதிரியை `int4` ஆக Optimize மற்றும் Quantize செய்யவும்.

மேலும், ONNX Runtime (ORT) Generate API-யை பயன்படுத்தி fine-tuned மாதிரியை எவ்வாறு inference செய்யலாம் என்பதையும் காண்பிக்கிறோம்.

> **⚠️ Fine-tuning செய்ய, உங்களுக்கு ஏற்ற GPU தேவைப்படும் - உதாரணமாக, A10, V100, A100.**

## 💾 நிறுவல்

புதிய Python virtual environment ஒன்றை உருவாக்கவும் (உதாரணமாக, `conda` பயன்படுத்தி):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

அடுத்ததாக, Olive மற்றும் fine-tuning வேலைப்பாட்டிற்கான dependencies-ஐ நிறுவவும்:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive-ஐ பயன்படுத்தி Phi3-ஐ Fine-tune செய்யவும்
[Olive configuration file](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) *workflow* உடன் பின்வரும் *passes* உள்ளடக்கியுள்ளது:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

மேல்நிலையத்தில், இந்த workflow செய்யும் செயல்கள்:

1. [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) தரவுகளைப் பயன்படுத்தி Phi3-ஐ (150 படிகள் வரை, நீங்கள் இதை மாற்றலாம்) fine-tune செய்யும்.
2. LoRA adapter எடைகளை அடிப்படை மாதிரியில் இணைக்கும். இதன் மூலம் ONNX வடிவத்தில் ஒரு மாதிரி கலைப்பொருள் கிடைக்கும்.
3. Model Builder மாதிரியை ONNX runtime-க்கு Optimize செய்யும் *மற்றும்* மாதிரியை `int4` ஆக Quantize செய்யும்.

இந்த workflow-ஐ இயக்க, கீழே உள்ளதை இயக்கவும்:

```bash
olive run --config phrase-classification.json
```

Olive முடிந்தவுடன், நீங்கள் Optimize செய்யப்பட்ட `int4` fine-tuned Phi3 மாதிரியை இங்கே பெறலாம்: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Fine-tuned Phi3-ஐ உங்கள் பயன்பாட்டில் ஒருங்கிணைக்கவும் 

பயன்பாட்டை இயக்க:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

இந்த பதில் வாக்கியத்தின் வகைப்பாட்டை (Sad/Joy/Fear/Surprise) ஒரு சொல் வடிவில் வழங்கும்.

---

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.