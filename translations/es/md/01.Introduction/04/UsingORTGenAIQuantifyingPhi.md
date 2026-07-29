# **Cuantificación de la familia Phi usando extensiones de IA generativa para onnxruntime**

## **Qué son las extensiones de IA generativa para onnxruntime**

Estas extensiones te ayudan a ejecutar IA generativa con ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Proporcionan el ciclo de IA generativa para modelos ONNX, incluyendo inferencia con ONNX Runtime, procesamiento de logits, búsqueda y muestreo, y gestión de caché KV. Los desarrolladores pueden llamar a un método generate() de alto nivel, o ejecutar cada iteración del modelo en un bucle, generando un token a la vez y opcionalmente actualizando parámetros de generación dentro del bucle. Tiene soporte para búsqueda greedy/beam y muestreo TopP, TopK para generar secuencias de tokens y procesamiento de logits incorporado como penalizaciones por repetición. También puedes añadir facilidad para puntuación personalizada.

A nivel de aplicación, puedes usar las extensiones de IA generativa para onnxruntime para crear aplicaciones usando C++ / C# / Python. A nivel de modelo, puedes usarlas para fusionar modelos afinados y realizar trabajos relacionados de despliegue cuantitativo.


## **Cuantificación de Phi-3.5 con extensiones de IA generativa para onnxruntime**

### **Modelos compatibles**

Las extensiones de IA generativa para onnxruntime soportan la conversión de cuantificación de Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Constructor de modelos en las extensiones de IA generativa para onnxruntime**

El constructor de modelos acelera enormemente la creación de modelos ONNX optimizados y cuantificados que funcionan con la API generate() de ONNX Runtime.

A través del Constructor de Modelos, puedes cuantificar el modelo a INT4, INT8, FP16, FP32, y combinar diferentes métodos de aceleración de hardware como CPU, CUDA, DirectML, Mobile, etc.

Para usar el Constructor de Modelos necesitas instalar

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Después de la instalación, puedes ejecutar el script del Constructor de Modelos desde la terminal para realizar la conversión de formato y cuantificación del modelo.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Entiende los parámetros relevantes

1. **model_name** Este es el modelo en Hugging Face, como microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, etc. También puede ser la ruta donde almacenas el modelo.

2. **path_to_output_folder** Ruta donde se guarda la conversión cuantificada.

3. **execution_provider** Diferente soporte para aceleración de hardware, como cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Descargamos el modelo desde Hugging Face y lo almacenamos en caché local.




***Nota：*** <ul>Aunque las extensiones de IA generativa para onnxruntime están en vista previa, ya han sido incorporadas en Microsoft Olive, y también puedes llamar a las funciones del Constructor de Modelos de las extensiones de IA generativa para onnxruntime a través de Microsoft Olive.</ul>

## **Cómo usar el Constructor de Modelos para cuantificar Phi-3.5**

El Constructor de Modelos actualmente soporta la cuantificación de modelos ONNX para Phi-3.5 Instruct y Phi-3.5-Vision.

### **Phi-3.5-Instruct**


**Conversión acelerada por CPU de la cuantificación INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Conversión acelerada por CUDA de la cuantificación INT 4**

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

3. Por favor, descarga estos archivos en tu carpeta Phi-3.5-vision-instruct

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Descarga este archivo en la carpeta models
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Ve a la terminal

    Convierte soporte ONNX con FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Nota：**

1. Actualmente el Constructor de Modelos soporta la conversión de Phi-3.5-Instruct y Phi-3.5-Vision, pero no Phi-3.5-MoE

2. Para usar el modelo cuantificado ONNX, puedes usarlo a través del SDK de las extensiones de IA generativa para onnxruntime

3. Necesitamos considerar una IA más responsable, por lo que después de la conversión de cuantificación del modelo, es recomendable realizar pruebas de resultados más efectivas

4. Cuantificando el modelo CPU INT4, podemos desplegarlo en dispositivos Edge, que tienen mejores escenarios de aplicación, por lo que hemos completado Phi-3.5-Instruct alrededor de INT 4


## **Recursos**

1. Aprende más sobre las extensiones de IA generativa para onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Repositorio GitHub de las extensiones de IA generativa para onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->