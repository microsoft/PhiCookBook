# **Inference Phi-3 with Apple MLX Framework**

## **MLX Framework என்றால் என்ன**

MLX என்பது Apple silicon-ல் இயங்கும் மெஷின் லெர்னிங் ஆராய்ச்சிக்கான ஒரு array framework ஆகும், இது Apple machine learning research மூலம் உருவாக்கப்பட்டது.

MLX மெஷின் லெர்னிங் ஆராய்ச்சியாளர்களால், மெஷின் லெர்னிங் ஆராய்ச்சியாளர்களுக்காக வடிவமைக்கப்பட்டுள்ளது. இந்த framework பயனர் நட்பு (user-friendly) ஆகவும், மாடல்களை பயிற்சி மற்றும் deploy செய்ய திறமையாகவும் இருக்க வேண்டும். Framework-இன் வடிவமைப்பு தற்காலிகமாக எளிமையானது. புதிய யோசனைகளை விரைவாக ஆராய்வதற்கான நோக்கத்துடன் MLX-ஐ விரிவாக்கவும் மேம்படுத்தவும் ஆராய்ச்சியாளர்களுக்கு எளிதாக இருக்க வேண்டும்.

LLMs Apple Silicon சாதனங்களில் MLX மூலம் வேகமாக செயல்படுத்தப்படலாம், மேலும் மாடல்கள் உள்ளூர் முறையில் மிகவும் வசதியாக இயக்கப்படலாம்.

## **MLX மூலம் Phi-3-mini-ஐ inference செய்வது**

### **1. உங்கள் MLX சூழலை அமைக்கவும்**

1. Python 3.11.x
2. MLX Library-ஐ நிறுவவும்

```bash

pip install mlx-lm

```


### **2. MLX மூலம் Terminal-ல் Phi-3-mini-ஐ இயக்குவது**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```


எனது சூழல் (Apple M1 Max, 64GB) முடிவுகள்:

![Terminal](../../../../../imgs/01/03/MLX/01.png)

### **3. MLX மூலம் Terminal-ல் Phi-3-mini-ஐ Quantize செய்வது**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```


***குறிப்பு:*** mlx_lm.convert மூலம் மாடலை quantize செய்யலாம், மேலும் இயல்புநிலை quantization என்பது INT4 ஆகும். இந்த எடுத்துக்காட்டில் Phi-3-mini-ஐ INT4-ஆக quantize செய்யப்படுகிறது.

mlx_lm.convert மூலம் மாடலை quantize செய்யலாம், மேலும் இயல்புநிலை quantization என்பது INT4 ஆகும். இந்த எடுத்துக்காட்டில் Phi-3-mini-ஐ INT4-ஆக quantize செய்யப்படுகிறது. Quantization முடிந்த பிறகு, அது இயல்புநிலை அடைவு ./mlx_model-ல் சேமிக்கப்படும்.

MLX மூலம் quantize செய்யப்பட்ட மாடலை Terminal-ல் சோதிக்கலாம்.

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```


முடிவுகள்:

![INT4](../../../../../imgs/01/03/MLX/02.png)

### **4. Jupyter Notebook-ல் MLX மூலம் Phi-3-mini-ஐ இயக்குவது**

![Notebook](../../../../../imgs/01/03/MLX/03.png)

***குறிப்பு:*** இந்த எடுத்துக்காட்டை படிக்க [இந்த இணைப்பை கிளிக் செய்யவும்](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **வளங்கள்**

1. Apple MLX Framework பற்றி அறிய [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.