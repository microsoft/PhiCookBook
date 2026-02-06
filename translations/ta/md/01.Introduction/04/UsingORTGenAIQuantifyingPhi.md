# **Phi குடும்பத்தை Quantizing செய்வது Generative AI extensions for onnxruntime மூலம்**

## **Generative AI extensions for onnxruntime என்றால் என்ன?**

இந்த extensions உங்களுக்கு ONNX Runtime மூலம் Generative AI இயக்க உதவுகிறது ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). இது ONNX மாடல்களுக்கு Generative AI loop வழங்குகிறது, அதில் ONNX Runtime மூலம் inference, logits செயலாக்கம், தேடல் மற்றும் sampling, மற்றும் KV cache மேலாண்மை அடங்கும். Developers ஒரு உயர்நிலை generate() முறை அழைக்கலாம் அல்லது மாடலின் ஒவ்வொரு iteration-ஐ loop-ல் இயக்கலாம், ஒவ்வொரு முறையும் ஒரு token உருவாக்கி, loop-இல் generation parameters-ஐ விருப்பமாக update செய்யலாம். இது greedy/beam search மற்றும் TopP, TopK sampling-ஐ token sequences உருவாக்கவும், repetition penalties போன்ற built-in logits செயலாக்கத்தையும் ஆதரிக்கிறது. நீங்கள் எளிதாக custom scoring-ஐ சேர்க்கவும் முடியும்.

Application அளவில், Generative AI extensions for onnxruntime-ஐ பயன்படுத்தி C++/ C# / Python மூலம் applications உருவாக்கலாம். Model அளவில், fine-tuned models-ஐ இணைத்து தொடர்புடைய quantitative deployment பணிகளை செய்யலாம்.

## **Generative AI extensions for onnxruntime மூலம் Phi-3.5 Quantizing செய்வது**

### **ஆதரவு மாடல்கள்**

Generative AI extensions for onnxruntime Microsoft Phi, Google Gemma, Mistral, Meta LLaMA ஆகியவற்றின் quantization conversion-ஐ ஆதரிக்கிறது.

### **Generative AI extensions for onnxruntime-ல் Model Builder**

Model Builder ONNX Runtime generate() API-யுடன் இயங்கும் optimized மற்றும் quantized ONNX மாடல்களை உருவாக்குவதில் வேகத்தை அதிகரிக்கிறது.

Model Builder மூலம், நீங்கள் மாடலை INT4, INT8, FP16, FP32-க்கு quantize செய்யலாம், மேலும் CPU, CUDA, DirectML, Mobile போன்ற hardware acceleration முறைகளை இணைக்கலாம்.

Model Builder-ஐ பயன்படுத்த, நீங்கள் கீழே உள்ளதை நிறுவ வேண்டும்:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```
  
நிறுவலுக்குப் பிறகு, மாடல் வடிவமைப்பு மற்றும் quantization conversion செய்ய terminal-ல் இருந்து Model Builder script-ஐ இயக்கலாம்.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```
  
தொடர்புடைய அளவுருக்களைப் புரிந்து கொள்ளுங்கள்:

1. **model_name** இது Hugging face-ல் உள்ள மாடல், உதாரணமாக microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct போன்றவை. இது நீங்கள் மாடலை சேமிக்கும் பாதையாகவும் இருக்கலாம்.

2. **path_to_output_folder** Quantized conversion சேமிக்கும் பாதை.

3. **execution_provider** CPU, CUDA, DirectML போன்ற hardware acceleration ஆதரவு.

4. **cache_dir_to_save_hf_files** Hugging face-ல் இருந்து மாடலை பதிவிறக்கம் செய்து உள்ளூரில் cache செய்கிறோம்.

***குறிப்பு:*** <ul>Generative AI extensions for onnxruntime தற்போது preview நிலையில் இருந்தாலும், இது Microsoft Olive-ல் இணைக்கப்பட்டுள்ளது, மேலும் Microsoft Olive மூலம் Generative AI extensions for onnxruntime Model Builder functions-ஐ அழைக்கலாம்.</ul>

## **Model Builder-ஐ பயன்படுத்தி Phi-3.5 Quantizing செய்வது எப்படி?**

Model Builder தற்போது Phi-3.5 Instruct மற்றும் Phi-3.5-Vision-க்கு ONNX மாடல் quantization-ஐ ஆதரிக்கிறது.

### **Phi-3.5-Instruct**

**Quantized INT 4-க்கு CPU மூலம் conversion**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```
  
**Quantized INT 4-க்கு CUDA மூலம் conversion**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```
  

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```
  

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Terminal-ல் சூழலை அமைக்கவும்

```bash

mkdir models

cd models 

```
  
2. microsoft/Phi-3.5-vision-instruct-ஐ models folder-ல் பதிவிறக்கவும்  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. இந்த கோப்புகளை உங்கள் Phi-3.5-vision-instruct folder-க்கு பதிவிறக்கவும்:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. இந்த கோப்பை models folder-க்கு பதிவிறக்கவும்:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Terminal-க்கு செல்லவும்  

    FP32-ஐ ஆதரிக்கும் ONNX conversion செய்யவும்  

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```
  

### **குறிப்பு:**

1. Model Builder தற்போது Phi-3.5-Instruct மற்றும் Phi-3.5-Vision-ஐ மாற்றுவதற்கு ஆதரிக்கிறது, ஆனால் Phi-3.5-MoE-ஐ ஆதரிக்கவில்லை.

2. ONNX-ன் quantized மாடலை பயன்படுத்த, Generative AI extensions for onnxruntime SDK மூலம் பயன்படுத்தலாம்.

3. நாங்கள் மேலும் பொறுப்பான AI-ஐ பரிசீலிக்க வேண்டும், எனவே மாடல் quantization conversion பிறகு, மேலும் பயனுள்ள முடிவுகளை சோதனை செய்ய பரிந்துரைக்கப்படுகிறது.

4. CPU INT4 மாடலை quantize செய்வதன் மூலம், அதை Edge Device-க்கு deploy செய்யலாம், இது சிறந்த பயன்பாட்டு சூழல்களை வழங்குகிறது, எனவே INT 4-ஐ சுற்றி Phi-3.5-Instruct-ஐ முடித்துவிட்டோம்.

## **வளங்கள்**

1. Generative AI extensions for onnxruntime பற்றி மேலும் அறிக  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub Repo  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்தவொரு தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.