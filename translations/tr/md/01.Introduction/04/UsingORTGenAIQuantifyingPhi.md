# **Onnxruntime için Generatif AI uzantıları kullanarak Phi Ailesini Kantitleme**

## **Onnxruntime için Generatif AI uzantıları nedir**

Bu uzantılar, ONNX Runtime ile generatif AI çalıştırmanıza yardımcı olur ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). ONNX modelleri için generatif AI döngüsü sağlar; bu döngü ONNX Runtime ile çıkarım, logits işleme, arama ve örnekleme ile KV önbellek yönetimini içerir. Geliştiriciler yüksek seviyeli generate() metodunu çağırabilir veya döngü içinde modelin her iterasyonunu çalıştırarak, token'ları birer birer üretebilir ve isteğe bağlı olarak döngü içinde üretim parametrelerini güncelleyebilir. Greedy/beam araması ve TopP, TopK örnekleme desteği ile token dizileri üretebilir ve tekrar cezaları gibi yerleşik logits işlemleri uygular. Ayrıca kolayca özel skorlama ekleyebilirsiniz.

Uygulama düzeyinde, C++/ C# / Python kullanarak uygulamalar oluşturmak için Onnxruntime için Generatif AI uzantılarını kullanabilirsiniz. Model düzeyinde ise, ince ayarlı modelleri birleştirmek ve ilgili nicel dağıtım çalışmalarını yapmak için kullanabilirsiniz.


## **Onnxruntime için Generatif AI uzantıları ile Phi-3.5'i Kantitleme**

### **Desteklenen Modeller**

Onnxruntime için Generatif AI uzantıları, Microsoft Phi, Google Gemma, Mistral, Meta LLaMA modellerinin kantitleme dönüşümünü destekler.


### **Onnxruntime için Generatif AI uzantılarında Model Oluşturucu**

Model oluşturucu, ONNX Runtime generate() API ile çalışan optimize ve kantitle edilmiş ONNX modelleri oluşturmayı büyük ölçüde hızlandırır.

Model Oluşturucu ile modeli INT4, INT8, FP16, FP32'ye kantitleyebilir ve CPU, CUDA, DirectML, Mobil gibi farklı donanım hızlandırma yöntemlerini birleştirebilirsiniz.

Model Oluşturucu'yu kullanmak için şunları yüklemeniz gerekir:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Yüklemeden sonra, terminalden Model Oluşturucu betiğini çalıştırarak model formatı ve kantitleme dönüşümü yapabilirsiniz.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

İlgili parametreleri anlama

1. **model_name** Bu, Hugging face üzerindeki modeldir, örneğin microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct vb. Ayrıca modeli depoladığınız yol da olabilir.

2. **path_to_output_folder** Kantitleme dönüşümünün kaydedileceği yol

3. **execution_provider** CPU, CUDA, DirectML gibi farklı donanım hızlandırma desteği

4. **cache_dir_to_save_hf_files** Modeli Hugging face'den indiriyoruz ve yerel olarak önbelleğe alıyoruz




***Not:*** <ul>Onnxruntime için Generatif AI uzantıları önizleme aşamasında olsa da Microsoft Olive'a dahil edilmiştir ve Microsoft Olive aracılığıyla Model Oluşturucu işlevlerini çağırabilirsiniz.</ul>

## **Model Oluşturucu ile Phi-3.5'i Kantitleme Nasıl Yapılır**

Model Oluşturucu şu anda Phi-3.5 Instruct ve Phi-3.5-Vision için ONNX model kantitlemesini desteklemektedir.

### **Phi-3.5-Instruct**


**Kantitlemiş INT 4 için CPU hızlandırmalı dönüşüm**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Kantitlemiş INT 4 için CUDA hızlandırmalı dönüşüm**

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

    FP32 desteği ile ONNX dönüşümü yapın


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Not:**

1. Model Oluşturucu şu anda Phi-3.5-Instruct ve Phi-3.5-Vision dönüşümlerini destekliyor, ancak Phi-3.5-MoE'yi desteklemiyor.

2. ONNX'in kantitlemiş modelini kullanmak için Onnxruntime için Generatif AI uzantıları SDK'sını kullanabilirsiniz.

3. Daha sorumlu AI düşünmemiz gerektiğinden, modelin kantitleme dönüşümünden sonra daha etkili sonuç testleri yapılması önerilir.

4. CPU INT4 modeli kantitleyerek, kenar cihazlarda dağıtabiliriz, bu da daha iyi uygulama senaryoları sağlar; bu nedenle Phi-3.5-Instruct'i INT 4 çevresinde tamamladık.


## **Kaynaklar**

1. Onnxruntime için Generatif AI uzantıları hakkında daha fazla bilgi [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Onnxruntime için Generatif AI uzantıları GitHub Deposu [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->