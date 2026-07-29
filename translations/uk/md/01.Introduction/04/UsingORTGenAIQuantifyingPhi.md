# **Квантизація сімейства Phi за допомогою розширень Generative AI для onnxruntime**

## **Що таке розширення Generative AI для onnxruntime**

Ці розширення допомагають запускати генеративний AI з ONNX Runtime ( [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Вони забезпечують цикл генеративного AI для моделей ONNX, включаючи виведення з ONNX Runtime, обробку логітів, пошук і вибірку, а також управління KV кешем. Розробники можуть викликати високорівневий метод generate(), або запускати кожну ітерацію моделі у циклі, генеруючи по одному токену за раз, і при необхідності оновлювати параметри генерації всередині циклу. Підтримується жадібний/пошук променів та вибірка TopP, TopK для генерації послідовностей токенів та вбудована обробка логітів, наприклад, покарання за повторення. Ви також легко можете додати власне оцінювання.

На рівні застосунку ви можете використовувати розширення Generative AI для onnxruntime для створення застосунків з використанням C++/ C# / Python. На рівні моделі ви можете об’єднувати доопрацьовані моделі та виконувати пов’язані роботи з кількісного розгортання.


## **Квантизація Phi-3.5 за допомогою розширень Generative AI для onnxruntime**

### **Підтримувані моделі**

Розширення Generative AI для onnxruntime підтримують конвертацію квантизації Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Побудовник моделей у розширеннях Generative AI для onnxruntime**

Побудовник моделей значно прискорює створення оптимізованих і квантизованих ONNX моделей, які працюють за допомогою API generate() ONNX Runtime.

За допомогою Побудовника моделей ви можете квантизувати модель до INT4, INT8, FP16, FP32, а також комбінувати різні методи апаратного прискорення, такі як CPU, CUDA, DirectML, Mobile тощо.

Для використання Побудовника моделей потрібно встановити

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Після встановлення ви можете запустити скрипт Побудовника моделей з терміналу для конвертації формату моделі та квантизації.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Зрозумійте відповідні параметри

1. **model_name** Це модель з Hugging face, наприклад microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct тощо. Це також може бути шлях, де ви зберігаєте модель

2. **path_to_output_folder** Шлях збереження конвертованої квантизованої моделі

3. **execution_provider** Підтримка різних апаратних прискорень, таких як cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Ми завантажуємо модель з Hugging face та кешуємо її локально




***Примітка：*** <ul>Хоча розширення Generative AI для onnxruntime знаходяться в прев’ю, вони були інтегровані у Microsoft Olive, також можна викликати функції Побудовника моделей розширень Generative AI для onnxruntime через Microsoft Olive.</ul>

## **Як використовувати Побудовник моделей для квантизації Phi-3.5**

Побудовник моделей наразі підтримує квантизацію моделі ONNX для Phi-3.5 Instruct і Phi-3.5-Vision

### **Phi-3.5-Instruct**


**Акселерація на CPU для конвертації в квантизований INT4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Акселерація на CUDA для конвертації в квантизований INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Встановіть середовище в терміналі

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

5. Перейдіть до терміналу

    Конвертуйте підтримку ONNX з FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Примітка：**

1. Побудовник моделей наразі підтримує конвертацію Phi-3.5-Instruct і Phi-3.5-Vision, але не Phi-3.5-MoE

2. Для використання квантизованої моделі ONNX, ви можете використовувати її через Generative AI extensions for onnxruntime SDK

3. Треба більше враховувати відповідальний AI, тому після конвертації квантизації моделі рекомендується проводити більш ефективне тестування результатів

4. Квантизуючи модель CPU INT4, ми можемо розгортати її на Edge пристроях, що мають кращі сценарії застосування, тому ми завершили Phi-3.5-Instruct навколо INT4


## **Ресурси**

1. Дізнайтеся більше про розширення Generative AI для onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Репозиторій Generative AI extensions для onnxruntime на GitHub [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->