# **Apple MLX Framework மூலம் Phi-3 inference செய்யுதல்**

## **MLX Framework என்றால் என்ன**

MLX என்பது Apple silicon-ல் இயங்கக்கூடிய மெஷின் லர்னிங் ஆராய்ச்சிக்கான ஒரு array framework ஆகும், இது Apple மெஷின் லர்னிங் ஆராய்ச்சியாளர்களால் உருவாக்கப்பட்டது.

MLX மெஷின் லர்னிங் ஆராய்ச்சியாளர்களுக்காகவே வடிவமைக்கப்பட்டுள்ளது. இந்த framework பயனர்களுக்கு எளிதாக பயன்படுத்தக்கூடியதாக இருக்கும், அதேசமயம் மாடல்களை பயிற்சி மற்றும் deploy செய்யும் போது திறமையாக செயல்படும். இந்த framework-இன் வடிவமைப்பு தத்துவ ரீதியாக எளிமையானது. புதிய யோசனைகளை விரைவாக ஆராய்வதற்காக MLX-ஐ ஆராய்ச்சியாளர்கள் விரிவுபடுத்தவும் மேம்படுத்தவும் எளிதாக்குவதே எங்கள் நோக்கம்.

Apple Silicon சாதனங்களில் MLX மூலம் LLM-களை வேகமாக செயல்படுத்தலாம், மேலும் மாடல்களை உள்ளூர் முறையில் மிகவும் வசதியாக இயக்கலாம்.

## **MLX மூலம் Phi-3-mini inference செய்யுதல்**

### **1. உங்கள் MLX சூழலை அமைத்தல்**

1. Python 3.11.x
2. MLX Library-ஐ நிறுவுதல்

```bash

pip install mlx-lm

```

### **2. MLX மூலம் Terminal-ல் Phi-3-mini இயக்குதல்**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

என் சூழல் (Apple M1 Max, 64GB) மூலம் பெறப்பட்ட முடிவு:

![Terminal](../../../../../imgs/01/03/MLX/01.png)

### **3. MLX மூலம் Terminal-ல் Phi-3-mini-ஐ Quantize செய்தல்**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***குறிப்பு:*** மாடலை mlx_lm.convert மூலம் quantize செய்யலாம், மேலும் இயல்புநிலை quantization என்பது INT4 ஆகும். இந்த எடுத்துக்காட்டில் Phi-3-mini-ஐ INT4 ஆக quantize செய்யப்படுகிறது.

மாடலை mlx_lm.convert மூலம் quantize செய்யலாம், மேலும் இயல்புநிலை quantization என்பது INT4 ஆகும். இந்த எடுத்துக்காட்டில் Phi-3-mini-ஐ INT4 ஆக quantize செய்யப்படுகிறது. Quantization செய்யப்பட்ட பிறகு, அது இயல்புநிலை கோப்பகமான ./mlx_model-ல் சேமிக்கப்படும்.

MLX மூலம் quantize செய்யப்பட்ட மாடலை Terminal-ல் சோதிக்கலாம்.

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

முடிவு:

![INT4](../../../../../imgs/01/03/MLX/02.png)

### **4. Jupyter Notebook-ல் MLX மூலம் Phi-3-mini இயக்குதல்**

![Notebook](../../../../../imgs/01/03/MLX/03.png)

***குறிப்பு:*** இந்த எடுத்துக்காட்டை படிக்க [இந்த இணைப்பை கிளிக் செய்யவும்](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **வளங்கள்**

1. Apple MLX Framework பற்றி அறிய [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)

---

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.