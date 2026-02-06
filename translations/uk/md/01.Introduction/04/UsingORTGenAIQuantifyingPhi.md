## **Як використовувати Model Builder для квантизації Phi-3.5**

Model Builder тепер підтримує квантизацію ONNX моделей для Phi-3.5 Instruct та Phi-3.5-Vision

### **Phi-3.5-Instruct**

**Конвертація з прискоренням на CPU для квантизації INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Конвертація з прискоренням на CUDA для квантизації INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Налаштуйте середовище в терміналі

```bash

mkdir models

cd models 

```

2. Завантажте microsoft/Phi-3.5-vision-instruct у папку models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Будь ласка, завантажте ці файли у вашу папку Phi-3.5-vision-instruct

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Завантажте цей файл у папку models  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Перейдіть у термінал

    Конвертуйте ONNX з підтримкою FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Примітка:**

1. Наразі Model Builder підтримує конвертацію Phi-3.5-Instruct та Phi-3.5-Vision, але не Phi-3.5-MoE

2. Для використання квантизованої моделі ONNX можна застосовувати Generative AI extensions for onnxruntime SDK

3. Важливо враховувати відповідальне використання AI, тому після квантизації моделі рекомендується провести більш ретельне тестування результатів

4. Квантизуючи модель CPU INT4, ми можемо розгортати її на Edge-пристроях, що відкриває кращі сценарії застосування, тому ми завершили роботу над Phi-3.5-Instruct у форматі INT4

## **Ресурси**

1. Дізнайтеся більше про Generative AI extensions for onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Репозиторій Generative AI extensions for onnxruntime на GitHub [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.