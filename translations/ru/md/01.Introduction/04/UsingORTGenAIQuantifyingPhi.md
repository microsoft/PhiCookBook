# **Квантование семейства Phi с использованием расширений Generative AI для onnxruntime**

## **Что такое расширения Generative AI для onnxruntime**

Эти расширения помогают запускать генеративный ИИ с ONNX Runtime ( [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Они обеспечивают цикл генеративного ИИ для моделей ONNX, включая вывод с помощью ONNX Runtime, обработку логитов, поиск и семплирование, а также управление кешем KV. Разработчики могут вызвать метод высокого уровня generate() или запускать каждую итерацию модели в цикле, генерируя по одному токену за раз и, при необходимости, обновляя параметры генерации внутри цикла. Поддерживаются жадный и лучевой поиск, а также семплирование TopP, TopK для генерации последовательностей токенов и встроенная обработка логитов, например, штрафы за повторения. Также можно легко добавить собственную оценку.

На уровне приложений можно использовать расширения Generative AI для onnxruntime для создания приложений на C++/C#/Python. На уровне модели можно использовать их для слияния дообученных моделей и выполнения связанных с этим количественных задач развертывания.


## **Квантование Phi-3.5 с использованием расширений Generative AI для onnxruntime**

### **Поддерживаемые модели**

Расширения Generative AI для onnxruntime поддерживают конвертацию квантования моделей Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Создатель моделей в расширениях Generative AI для onnxruntime**

Создатель моделей значительно ускоряет создание оптимизированных и квантованных моделей ONNX, работающих с API generate() ONNX Runtime.

Через Создатель моделей вы можете квантовать модель в INT4, INT8, FP16, FP32 и комбинировать различные методы аппаратного ускорения, такие как CPU, CUDA, DirectML, Mobile и др.

Для использования Создателя моделей необходимо установить

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

После установки вы можете запустить скрипт Создателя моделей из терминала для конвертации формата модели и квантования.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Пояснение параметров

1. **model_name** Это модель в Hugging face, например microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct и т.д. Также может быть путь, где хранится модель

2. **path_to_output_folder** Путь сохранения конвертированной квантованной модели

3. **execution_provider** Поддержка различного аппаратного ускорения, например cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Каталог для локального кеширования скачиваемой модели из Hugging face




***Примечание:*** <ul>Хотя расширения Generative AI для onnxruntime находятся в превью, они уже интегрированы в Microsoft Olive, и вы также можете вызывать функции Создателя моделей расширений Generative AI для onnxruntime через Microsoft Olive.</ul>

## **Как использовать Создатель моделей для квантования Phi-3.5**

Создатель моделей сейчас поддерживает квантование ONNX моделей для Phi-3.5 Instruct и Phi-3.5-Vision

### **Phi-3.5-Instruct**


**Квантование INT4 с ускорением на CPU**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Квантование INT4 с ускорением на CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Установите окружение в терминале

```bash

mkdir models

cd models 

```

2. Скачайте microsoft/Phi-3.5-vision-instruct в папку models
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Пожалуйста, скачайте эти файлы в папку Phi-3.5-vision-instruct

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Скачайте этот файл в папку models
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Перейдите в терминал

    Конвертация модели ONNX с поддержкой FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Примечание:**

1. В настоящее время Создатель моделей поддерживает конвертацию Phi-3.5-Instruct и Phi-3.5-Vision, но не Phi-3.5-MoE

2. Для использования квантованной модели ONNX можно использовать расширения Generative AI для onnxruntime SDK

3. Необходимо учитывать более ответственное использование ИИ, поэтому после квантования модели рекомендуется проводить более тщательное тестирование результатов

4. Квантованная модель CPU INT4 может быть развернута на Edge Device с лучшими сценариями применения, поэтому мы завершили квантование Phi-3.5-Instruct с использованием INT4


## **Ресурсы**

1. Подробнее о расширениях Generative AI для onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Репозиторий расширений Generative AI для onnxruntime в GitHub [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->