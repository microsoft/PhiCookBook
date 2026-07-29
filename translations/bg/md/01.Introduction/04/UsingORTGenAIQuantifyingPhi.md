# **Квантизиране на семейство Phi с разширения за Generative AI за onnxruntime**

## **Какво са разширенията за Generative AI за onnxruntime**

Тези разширения ви помагат да стартирате generative AI с ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Те предоставят generative AI цикъл за ONNX модели, включително инференция с ONNX Runtime, обработка на логити, търсене и семплиране, както и управление на KV кеш. Разработчиците могат да извикат високоефективния метод generate() или да изпълняват всяка итерация на модела в цикъл, генерирайки по един токен наведнъж и по избор да актуализират параметрите на генериране в рамките на цикъла. Поддържа greedy/beam търсене и TopP, TopK семплиране за генериране на последователности от токени и вградена обработка на логити като наказания за повторения. Можете също така лесно да добавяте персонализирано оценяване.

На приложение ниво можете да използвате разширенията за Generative AI за onnxruntime за изграждане на приложения с C++/ C# / Python. На ниво модел можете да ги използвате за сливане на финно настроени модели и извършване на свързана количествена подготовка.


## **Квантизиране на Phi-3.5 с разширения за Generative AI за onnxruntime**

### **Поддържани модели**

Разширенията за Generative AI за onnxruntime поддържат конверсия в квантизация на Microsoft Phi, Google Gemma, Mistral, Meta LLaMA。


### **Конструктор на модели в разширенията за Generative AI за onnxruntime**

Конструкторът на модели значително ускорява създаването на оптимизирани и квантизирани ONNX модели, които работят с ONNX Runtime generate() API.

Чрез Конструктор на модели можете да квантизирате модела до INT4, INT8, FP16, FP32 и да комбинирате различни методи за ускорение на хардуера като CPU, CUDA, DirectML, Mobile и др.

За да използвате Конструктор на модели, трябва да инсталирате

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

След инсталацията можете да стартирате скрипта Конструктор на модели от терминала, за да изпълните конверсия на формат и квантизация на модела.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Разберете съответните параметри

1. **model_name** Това е моделът в Hugging face, като microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct и др. Може да бъде и пътят, където съхранявате модела

2. **path_to_output_folder** Път за запазване на квантизирания конвертиран модел

3. **execution_provider** Поддръжка на различен хардуерен ускорител, като cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Ние изтегляме модела от Hugging face и го кешираме локално




***Забележка：*** <ul>Въпреки че разширенията за Generative AI за onnxruntime са в предварителен преглед, те вече са внедрени в Microsoft Olive и също така можете да извиквате функциите на Конструктор на модели от разширенията за Generative AI за onnxruntime чрез Microsoft Olive.</ul>

## **Как да използвате Конструктор на модели за квантизиране на Phi-3.5**

Конструкторът на модели вече поддържа квантизация на ONNX модел за Phi-3.5 Instruct и Phi-3.5-Vision

### **Phi-3.5-Instruct**


**Ускорена с CPU конверсия на квантизиран INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Ускорена с CUDA конверсия на квантизиран INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Настройте средата в терминала

```bash

mkdir models

cd models 

```

2. Изтеглете microsoft/Phi-3.5-vision-instruct в папка models
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Моля изтеглете тези файлове във вашата папка Phi-3.5-vision-instruct

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Изтеглете този файл в папка models
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Отидете в терминала

    Конвертирайте ONNX с поддръжка на FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Забележка：**

1. Конструкторът на модели в момента поддържа конверсия на Phi-3.5-Instruct и Phi-3.5-Vision, но не и Phi-3.5-MoE

2. За да използвате квантизирания модел на ONNX, можете да го използвате чрез SDK на разширенията за Generative AI за onnxruntime

3. Трябва да вземем предвид по-отговорния AI, затова след квантизацията на модела се препоръчва да се направят по-ефективни тестове на резултатите

4. Чрез квантизиране на CPU INT4 модела, можем да го разположим на Edge устройства, които имат по-добри сценарии за приложение, затова сме завършили Phi-3.5-Instruct около INT 4


## **Ресурси**

1. Научете повече за разширенията за Generative AI за onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. GitHub хранилище на разширенията за Generative AI за onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->