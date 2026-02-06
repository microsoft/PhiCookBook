## **Paano Gamitin ang Model Builder para sa Pag-quantize ng Phi-3.5**

Suportado na ngayon ng Model Builder ang ONNX model quantization para sa Phi-3.5 Instruct at Phi-3.5-Vision

### **Phi-3.5-Instruct**

**CPU accelerated conversion ng quantized INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA accelerated conversion ng quantized INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. I-set ang environment sa terminal

```bash

mkdir models

cd models 

```

2. I-download ang microsoft/Phi-3.5-vision-instruct sa models folder  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Pakidownload ang mga sumusunod na files sa iyong Phi-3.5-vision-instruct folder

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. I-download ang file na ito sa models folder  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Pumunta sa terminal

    I-convert ang ONNX support gamit ang FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Tandaan:**

1. Sa kasalukuyan, sinusuportahan ng Model Builder ang conversion ng Phi-3.5-Instruct at Phi-3.5-Vision, ngunit hindi pa ang Phi-3.5-MoE

2. Para magamit ang quantized na ONNX model, maaari itong gamitin sa pamamagitan ng Generative AI extensions para sa onnxruntime SDK

3. Kailangan nating isaalang-alang ang mas responsableng AI, kaya pagkatapos ng model quantization conversion, inirerekomenda ang mas masusing pagsusuri ng mga resulta

4. Sa pamamagitan ng pag-quantize ng CPU INT4 model, maaari natin itong i-deploy sa Edge Device, na may mas angkop na mga senaryo ng aplikasyon, kaya natapos na namin ang Phi-3.5-Instruct sa paligid ng INT 4

## **Mga Resources**

1. Matuto pa tungkol sa Generative AI extensions para sa onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions para sa onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.