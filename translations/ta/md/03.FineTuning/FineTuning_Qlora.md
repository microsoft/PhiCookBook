**Phi-3 மாடலை QLoRA மூலம் நன்றாக அமைத்தல்**

Microsoft இன் Phi-3 Mini மொழி மாடலை [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) பயன்படுத்தி நன்றாக அமைத்தல்.

QLoRA உரையாடல் புரிதல் மற்றும் பதில் உருவாக்கத்தை மேம்படுத்த உதவும்.

transformers மற்றும் bitsandbytes மூலம் 4bits மாடல்களை ஏற்ற, நீங்கள் accelerate மற்றும் transformers-ஐ மூலத்திலிருந்து நிறுவ வேண்டும், மேலும் bitsandbytes நூலகத்தின் சமீபத்திய பதிப்பு உங்களிடம் இருக்க வேண்டும் என்பதை உறுதிப்படுத்த வேண்டும்.

**மாதிரிகள்**
- [இந்த மாதிரி நோட்புக் மூலம் மேலும் அறிக](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python FineTuning மாதிரி உதாரணம்](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub Fine Tuning உதாரணம் LORA உடன்](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Hub Fine Tuning உதாரணம் QLORA உடன்](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.