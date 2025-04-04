<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b96f9dc2389500e24a2c2c4debf30908",
  "translation_date": "2025-04-04T12:15:44+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingORTGenAIQuantifyingPhi.md",
  "language_code": "mo"
}
-->
# **Phi Ailesini Generative AI Uzantıları ile Kuantize Etme**

## **Generative AI Uzantıları nedir?**

Bu uzantılar, ONNX Runtime ile generative AI çalıştırmanıza yardımcı olur ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). ONNX modelleri için generative AI döngüsü sağlar; buna ONNX Runtime ile çıkarım, logits işleme, arama ve örnekleme, KV önbellek yönetimi dahildir. Geliştiriciler yüksek seviyeli bir generate() metodunu çağırabilir veya modeli bir döngü içinde her iterasyonda bir token üreterek çalıştırabilir ve döngü içinde üretim parametrelerini güncelleyebilir. Greedy/beam arama, TopP ve TopK örnekleme yöntemlerini kullanarak token dizileri oluşturmayı destekler ve tekrarlama cezaları gibi dahili logits işleme özellikleri sunar. Ayrıca, kolayca özel puanlama ekleyebilirsiniz.

Uygulama seviyesinde, Generative AI uzantılarını C++/C#/Python kullanarak uygulamalar geliştirmek için kullanabilirsiniz. Model seviyesinde ise, ince ayar yapılmış modelleri birleştirmek ve ilgili kuantitatif dağıtım çalışmalarını yapmak için kullanabilirsiniz.

## **Generative AI Uzantıları ile Phi-3.5 Kuantizasyonu**

### **Desteklenen Modeller**

Generative AI uzantıları, Microsoft Phi, Google Gemma, Mistral, Meta LLaMA gibi modellerin kuantizasyon dönüşümünü destekler.

### **Generative AI Uzantılarındaki Model Builder**

Model Builder, ONNX Runtime generate() API ile çalışan optimize edilmiş ve kuantize edilmiş ONNX modelleri oluşturmayı büyük ölçüde hızlandırır.

Model Builder aracılığıyla modeli INT4, INT8, FP16, FP32'ye kuantize edebilir ve CPU, CUDA, DirectML, Mobile gibi farklı donanım hızlandırma yöntemlerini birleştirebilirsiniz.

Model Builder'ı kullanmak için aşağıdaki kurulumları yapmanız gerekir:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Kurulumdan sonra, terminalden Model Builder scriptini çalıştırarak model formatı ve kuantizasyon dönüşümü yapabilirsiniz.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

İlgili parametreleri anlayın:

1. **model_name** Hugging Face üzerindeki model, örneğin microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct gibi. Ayrıca modeli sakladığınız yol da olabilir.

2. **path_to_output_folder** Kuantize dönüşümün kayıt yolu.

3. **execution_provider** Farklı donanım hızlandırma destekleri, örneğin cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Hugging Face'den modeli indirip yerel olarak önbelleğe alıyoruz.

***Not:***  

## **Model Builder ile Phi-3.5 Kuantizasyonu Nasıl Yapılır?**

Model Builder artık Phi-3.5 Instruct ve Phi-3.5-Vision için ONNX model kuantizasyonunu destekliyor.

### **Phi-3.5-Instruct**

**CPU ile INT4 Kuantize Dönüşüm**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA ile INT4 Kuantize Dönüşüm**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Terminalde ortamı ayarlayın:

```bash

mkdir models

cd models 

```

2. microsoft/Phi-3.5-vision-instruct modelini models klasörüne indirin:  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Aşağıdaki dosyaları Phi-3.5-vision-instruct klasörüne indirin:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Bu dosyayı models klasörüne indirin:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Terminale gidin:

    ONNX desteğini FP32 ile dönüştürün:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Not:**

1. Model Builder şu anda Phi-3.5-Instruct ve Phi-3.5-Vision dönüşümünü destekliyor, ancak Phi-3.5-MoE desteklenmiyor.

2. ONNX'in kuantize edilmiş modelini kullanmak için Generative AI uzantıları SDK'sı aracılığıyla kullanabilirsiniz.

3. Daha sorumlu bir AI yaklaşımı için, model kuantizasyon dönüşümünden sonra daha etkili sonuç testleri yapılması önerilir.

4. CPU INT4 modeli kuantize ederek, Edge Device'a dağıtım yapabiliriz; bu daha iyi uygulama senaryoları sunar. Bu nedenle Phi-3.5-Instruct modelini INT4 çevresinde tamamladık.

## **Kaynaklar**

1. Generative AI uzantıları hakkında daha fazla bilgi edinin:  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI uzantıları GitHub deposu:  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

It seems like "mo" isn't a widely recognized language abbreviation. Could you clarify what language you would like the text translated into? For example, are you referring to Maori, Mongolian, or another language?