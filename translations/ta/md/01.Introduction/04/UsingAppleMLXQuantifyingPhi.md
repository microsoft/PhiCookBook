<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-10-11T12:25:57+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "ta"
}
-->
# **Apple MLX Framework-ஐ பயன்படுத்தி Phi-3.5-ஐ குவாண்டைஸ் செய்வது**

MLX என்பது ஆப்பிள் சிலிகான் சாதனங்களில் இயங்கும் மெஷின் லெர்னிங் ஆராய்ச்சிக்கான ஒரு அரே பிரேம்வொர்க் ஆகும், இது ஆப்பிள் மெஷின் லெர்னிங் ஆராய்ச்சியால் உருவாக்கப்பட்டது.

MLX மெஷின் லெர்னிங் ஆராய்ச்சியாளர்களால், மெஷின் லெர்னிங் ஆராய்ச்சியாளர்களுக்காக வடிவமைக்கப்பட்டுள்ளது. இந்த பிரேம்வொர்க் பயனர் நட்பு முறை கொண்டதாகவும், அதே நேரத்தில் மாடல்களை பயிற்சி மற்றும் செயல்படுத்துவதில் திறமையாகவும் இருக்க வேண்டும். பிரேம்வொர்க் வடிவமைப்பு தற்காலிகமாக எளிமையானது. புதிய யோசனைகளை விரைவாக ஆராய்வதற்கான நோக்கத்துடன் MLX-ஐ ஆராய்ச்சியாளர்கள் விரிவாக்கம் மற்றும் மேம்படுத்த எளிதாக இருக்க வேண்டும்.

Apple Silicon சாதனங்களில் MLX மூலம் LLM-களை வேகமாக செயல்படுத்தலாம், மேலும் மாடல்களை உள்ளூர் முறையில் மிகவும் வசதியாக இயக்கலாம்.

இப்போது Apple MLX Framework Phi-3.5-Instruct(**Apple MLX Framework support**), Phi-3.5-Vision(**MLX-VLM Framework support**) மற்றும் Phi-3.5-MoE(**Apple MLX Framework support**) ஆகியவற்றின் குவாண்டைசேஷன் மாற்றத்தை ஆதரிக்கிறது. அதை அடுத்ததாக முயற்சிக்கலாம்:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```


### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```


### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```


### **🤖 Apple MLX Framework-ஐ பயன்படுத்தி Phi-3.5-க்கு மாதிரிகள்**

| ஆய்வகங்கள் | அறிமுகம் | செல்லவும் |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Apple MLX Framework-ஐ பயன்படுத்தி Phi-3.5 Instruct-ஐ எப்படி பயன்படுத்துவது என்பதை கற்றுக்கொள்ளுங்கள்   |  [செல்லவும்](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (படம்) | Apple MLX Framework-ஐ பயன்படுத்தி படங்களை பகுப்பாய்வு செய்ய Phi-3.5 Vision-ஐ எப்படி பயன்படுத்துவது என்பதை கற்றுக்கொள்ளுங்கள்     |  [செல்லவும்](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Apple MLX Framework-ஐ பயன்படுத்தி Phi-3.5 MoE-ஐ எப்படி பயன்படுத்துவது என்பதை கற்றுக்கொள்ளுங்கள்  |  [செல்லவும்](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **வளங்கள்**

1. Apple MLX Framework பற்றி அறிய [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Rep [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.