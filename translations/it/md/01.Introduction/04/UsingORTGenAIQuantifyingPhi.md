<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-05-09T14:27:52+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "it"
}
-->
## **Cómo usar Model Builder para cuantizar Phi-3.5**

Model Builder ahora soporta la cuantización de modelos ONNX para Phi-3.5 Instruct y Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**Conversión acelerada por CPU a INT4 cuantizado**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Conversión acelerada por CUDA a INT4 cuantizado**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Configura el entorno en la terminal

```bash

mkdir models

cd models 

```

2. Descarga microsoft/Phi-3.5-vision-instruct en la carpeta models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Descarga estos archivos a tu carpeta Phi-3.5-vision-instruct

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Descarga este archivo a la carpeta models  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. En la terminal

    Convierte el soporte ONNX a FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Nota:**

1. Model Builder actualmente soporta la conversión de Phi-3.5-Instruct y Phi-3.5-Vision, pero no de Phi-3.5-MoE.

2. Para usar el modelo cuantizado ONNX, puedes hacerlo a través del SDK Generative AI extensions for onnxruntime.

3. Debemos considerar una IA más responsable, por lo que después de la conversión de cuantización del modelo, se recomienda realizar pruebas de resultados más efectivas.

4. Al cuantizar el modelo CPU INT4, podemos desplegarlo en dispositivos Edge, lo que ofrece mejores escenarios de aplicación, por eso hemos completado Phi-3.5-Instruct en torno a INT4.

## **Recursos**

1. Aprende más sobre Generative AI extensions for onnxruntime en [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Repositorio GitHub de Generative AI extensions for onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di considerare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.