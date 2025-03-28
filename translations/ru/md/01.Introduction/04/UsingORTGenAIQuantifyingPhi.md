<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-03-27T08:45:33+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingORTGenAIQuantifyingPhi.md",
  "language_code": "ru"
}
-->
## **Как использовать Model Builder для квантования Phi-3.5**

Model Builder теперь поддерживает квантование ONNX-моделей Phi-3.5 Instruct и Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**Квантование INT 4 с ускорением на CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Квантование INT 4 с ускорением на CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Настройте окружение в терминале

```bash

mkdir models

cd models 

```

2. Скачайте модель microsoft/Phi-3.5-vision-instruct в папку models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Скачайте следующие файлы в папку Phi-3.5-vision-instruct:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Скачайте этот файл в папку models:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Откройте терминал

    Конвертация в ONNX с поддержкой FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Примечания:**

1. Model Builder в настоящее время поддерживает конвертацию Phi-3.5-Instruct и Phi-3.5-Vision, но не Phi-3.5-MoE.

2. Для использования квантованной модели ONNX вы можете воспользоваться Generative AI extensions for onnxruntime SDK.

3. Необходимо учитывать аспекты ответственного ИИ, поэтому после квантования модели рекомендуется провести тщательное тестирование результатов.

4. Квантовав модель CPU INT4, мы можем развернуть её на устройствах Edge, что открывает более широкие сценарии применения. Поэтому мы сосредоточились на реализации Phi-3.5-Instruct с INT4.

## **Ресурсы**

1. Узнайте больше о Generative AI extensions for onnxruntime:  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Репозиторий Generative AI extensions for onnxruntime на GitHub:  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, обратите внимание, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникающие в результате использования этого перевода.