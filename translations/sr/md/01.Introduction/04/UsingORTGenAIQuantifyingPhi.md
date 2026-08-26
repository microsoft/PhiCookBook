# **Квантизација Phi породице користећи Generative AI додатке за onnxruntime**

## **Шта су Generative AI додаци за onnxruntime**

Ови додаци вам помажу да покренете генеративни AI са ONNX Runtime ( [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Они пружају генеративну AI петљу за ONNX моделе, укључујући извођење са ONNX Runtime, обраду логита, претрагу и узорковање, и управљање KV кешом. Програмери могу позвати виши ниво generate() метод, или покренути сваки циклус модела у петљи, генеришући један токен по један и по избору ажурирати параметре генерисања унутар петље. Подржавају greedy/beam претрагу и TopP, TopK узорковање за генерисање низа токена као и уграђену обраду логита попут казни за понављање. Такође можете лако додати прилагођено оцењивање.

На нивоу апликација, можете користити Generative AI додатке за onnxruntime за изградњу апликација користећи C++/ C# / Python. На нивоу модела, можете их користити за спајање финално обучених модела и извршити повезани квантитативни рад на имплементацији.


## **Квантизација Phi-3.5 са Generative AI додацима за onnxruntime**

### **Подржани модели**

Generative AI додаци за onnxruntime подржавају конверзију квантизације Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Model Builder у Generative AI додацима за onnxruntime**

Model Builder значајно убрзава креирање оптимизованих и квантованих ONNX модела који раде са ONNX Runtime generate() API.

Кроз Model Builder, можете квантизовати модел у INT4, INT8, FP16, FP32, и комбиновати различите методе хардверског убрзања као што су CPU, CUDA, DirectML, Mobile, итд.

За коришћење Model Builder-а потребно је да инсталирате

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Након инсталације, можете покренути скрипту Model Builder из терминала да бисте извршили конверзију формата модела и квантизацију.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Разумевање релевантних параметара

1. **model_name** Ово је модел са Hugging face-а, као што су microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, итд. Такође може бити и путања где чувате модел

2. **path_to_output_folder** Путања за чување квантизоване конверзије

3. **execution_provider** Подршка за различите хардверске акцелераторе, као што су cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Преузимамо модел са Hugging face-а и кеширамо га локално




***Напомена：*** <ul>Иако су Generative AI додаци за onnxruntime у прегледу, они су интегрисани у Microsoft Olive, и такође можете позвати функције Model Builder-а из Generative AI додатака за onnxruntime кроз Microsoft Olive.</ul>

## **Како користити Model Builder за квантизацију Phi-3.5**

Model Builder тренутно подржава квантизацију ONNX модела за Phi-3.5 Instruct и Phi-3.5-Vision

### **Phi-3.5-Instruct**


**ЦПУ убрзана конверзија квантизованог INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA убрзана конверзија квантизованог INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Поставите окружење у терминалу

```bash

mkdir models

cd models 

```

2. Преузмите microsoft/Phi-3.5-vision-instruct у фасциклу models
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Молимо преузмите ове датотеке у Вашу Phi-3.5-vision-instruct фасциклу

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Преузмите ову датотеку у фасциклу models
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Идите у терминал

    Конвертујте ONNX подршку са FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Напомена：**

1. Model Builder тренутно подржава конверзију Phi-3.5-Instruct и Phi-3.5-Vision, али не и Phi-3.5-MoE

2. За коришћење квантизованог модела ONNX, можете га користити преко Generative AI додатака за onnxruntime SDK

3. Потребно је да се више води рачуна о одговорном коришћењу AI, па се након квантизационе конверзије модела препоручује обављање ефикаснијих тестова резултата

4. Квантизовањем CPU INT4 модела, можемо га имплементирати на Edge уређајима, који имају боље сценарије примене, тако да смо завршили Phi-3.5-Instruct око INT 4


## **Ресурси**

1. Сазнајте више о Generative AI додацима за onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Репозиторијум Generative AI додатака за onnxruntime на GitHub [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->