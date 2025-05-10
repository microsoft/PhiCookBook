<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-05-09T14:29:45+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "tr"
}
-->
## **Model Builder kullanarak Phi-3.5 nasıl kuantize edilir**

Model Builder artık Phi-3.5 Instruct ve Phi-3.5-Vision için ONNX model kuantizasyonunu destekliyor.

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

3. Bu dosyaları Phi-3.5-vision-instruct klasörünüze indiriniz

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Bu dosyayı models klasörüne indirin  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Terminale gidin

    FP32 destekli ONNX dönüşümünü yapın

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Not:**

1. Model Builder şu anda Phi-3.5-Instruct ve Phi-3.5-Vision dönüşümünü destekliyor, ancak Phi-3.5-MoE desteklemiyor.

2. ONNX kuantize modeli kullanmak için Generative AI extensions for onnxruntime SDK üzerinden erişebilirsiniz.

3. Daha sorumlu AI uygulamaları için, model kuantizasyon dönüşümünden sonra daha etkili sonuç testleri yapılması önerilir.

4. CPU INT4 modelini kuantize ederek, Edge cihazlara dağıtım yapabiliriz, bu da daha iyi uygulama senaryoları sunar. Böylece Phi-3.5-Instruct INT4 etrafında tamamlanmıştır.

## **Kaynaklar**

1. Generative AI extensions for onnxruntime hakkında daha fazla bilgi için [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub deposu [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmemektedir.