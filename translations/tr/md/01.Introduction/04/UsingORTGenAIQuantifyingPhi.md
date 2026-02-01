## **Model Builder kullanarak Phi-3.5 nasıl kuantize edilir**

Model Builder artık Phi-3.5 Instruct ve Phi-3.5-Vision için ONNX model kuantizasyonunu desteklemektedir.

### **Phi-3.5-Instruct**

**CPU hızlandırmalı kuantize INT4 dönüşümü**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA hızlandırmalı kuantize INT4 dönüşümü**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Terminalde ortamı ayarlayın

```bash

mkdir models

cd models 

```

2. microsoft/Phi-3.5-vision-instruct modelini models klasörüne indirin  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Lütfen bu dosyaları Phi-3.5-vision-instruct klasörünüze indirin

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Bu dosyayı models klasörüne indirin  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Terminale gidin

    FP32 ile ONNX desteğini dönüştürün

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Notlar:**

1. Model Builder şu anda Phi-3.5-Instruct ve Phi-3.5-Vision dönüşümünü desteklemekte, ancak Phi-3.5-MoE desteklememektedir.

2. ONNX’in kuantize edilmiş modelini kullanmak için Generative AI extensions for onnxruntime SDK üzerinden erişebilirsiniz.

3. Daha sorumlu yapay zeka için, model kuantizasyon dönüşümünden sonra daha etkili sonuç testleri yapılması önerilir.

4. CPU INT4 modelini kuantize ederek, Edge Cihazlara dağıtım yapabiliriz; bu da daha iyi uygulama senaryoları sağlar. Bu nedenle Phi-3.5-Instruct INT4 çevresinde tamamlanmıştır.

## **Kaynaklar**

1. Generative AI extensions for onnxruntime hakkında daha fazla bilgi edinin [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub Deposu [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.