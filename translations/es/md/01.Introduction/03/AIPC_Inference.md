<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e08ce816e23ad813244a09ca34ebb8ac",
  "translation_date": "2025-07-16T19:53:21+00:00",
  "source_file": "md/01.Introduction/03/AIPC_Inference.md",
  "language_code": "es"
}
-->
# **Inferencia Phi-3 en AI PC**

Con el avance de la IA generativa y la mejora en las capacidades de hardware de los dispositivos edge, cada vez más modelos de IA generativa pueden integrarse en los dispositivos Bring Your Own Device (BYOD) de los usuarios. Los AI PCs están entre estos modelos. A partir de 2024, Intel, AMD y Qualcomm han colaborado con fabricantes de PC para introducir AI PCs que facilitan el despliegue de modelos generativos locales mediante modificaciones de hardware. En esta discusión, nos centraremos en los AI PCs de Intel y exploraremos cómo desplegar Phi-3 en un AI PC de Intel.

### Qué es una NPU

Una NPU (Unidad de Procesamiento Neural) es un procesador o unidad de procesamiento dedicada dentro de un SoC más grande, diseñada específicamente para acelerar operaciones de redes neuronales y tareas de IA. A diferencia de las CPU y GPU de propósito general, las NPU están optimizadas para computación paralela basada en datos, lo que las hace muy eficientes para procesar grandes volúmenes de datos multimedia como videos e imágenes, así como para procesar datos para redes neuronales. Son especialmente hábiles en tareas relacionadas con IA, como reconocimiento de voz, desenfoque de fondo en videollamadas y procesos de edición de fotos o videos como la detección de objetos.

## NPU vs GPU

Aunque muchas cargas de trabajo de IA y aprendizaje automático se ejecutan en GPUs, existe una diferencia clave entre GPUs y NPUs.  
Las GPUs son conocidas por sus capacidades de computación paralela, pero no todas son igualmente eficientes más allá del procesamiento gráfico. Por otro lado, las NPUs están diseñadas específicamente para los cálculos complejos involucrados en operaciones de redes neuronales, lo que las hace muy efectivas para tareas de IA.

En resumen, las NPUs son los genios matemáticos que aceleran las computaciones de IA y juegan un papel clave en la nueva era de los AI PCs.

***Este ejemplo está basado en el último procesador Intel Core Ultra de Intel***

## **1. Usar NPU para ejecutar el modelo Phi-3**

El dispositivo Intel® NPU es un acelerador de inferencia de IA integrado con CPUs cliente de Intel, a partir de la generación Intel® Core™ Ultra (anteriormente conocida como Meteor Lake). Permite la ejecución eficiente en energía de tareas de redes neuronales artificiales.

![Latencia](../../../../../translated_images/es/aipcphitokenlatency.2be14f04f30a3bf7.png)

![Latencia770](../../../../../translated_images/es/aipcphitokenlatency770.e923609a57c5d394.png)

**Intel NPU Acceleration Library**

La Intel NPU Acceleration Library [https://github.com/intel/intel-npu-acceleration-library](https://github.com/intel/intel-npu-acceleration-library) es una biblioteca en Python diseñada para mejorar la eficiencia de tus aplicaciones aprovechando el poder de la Unidad de Procesamiento Neural (NPU) de Intel para realizar cálculos de alta velocidad en hardware compatible.

Ejemplo de Phi-3-mini en AI PC potenciado por procesadores Intel® Core™ Ultra.

![DemoPhiIntelAIPC](../../../../../imgs/01/03/AIPC/aipcphi3-mini.gif)

Instala la biblioteca de Python con pip

```bash

   pip install intel-npu-acceleration-library

```

***Nota*** El proyecto aún está en desarrollo, pero el modelo de referencia ya está bastante completo.

### **Ejecutando Phi-3 con Intel NPU Acceleration Library**

Usando la aceleración Intel NPU, esta biblioteca no afecta el proceso tradicional de codificación. Solo necesitas usar esta biblioteca para cuantificar el modelo original Phi-3, como FP16, INT8, INT4, por ejemplo:

```python
from transformers import AutoTokenizer, pipeline,TextStreamer
from intel_npu_acceleration_library import NPUModelForCausalLM, int4
from intel_npu_acceleration_library.compiler import CompilerConfig
import warnings

model_id = "microsoft/Phi-3-mini-4k-instruct"

compiler_conf = CompilerConfig(dtype=int4)
model = NPUModelForCausalLM.from_pretrained(
    model_id, use_cache=True, config=compiler_conf, attn_implementation="sdpa"
).eval()

tokenizer = AutoTokenizer.from_pretrained(model_id)

text_streamer = TextStreamer(tokenizer, skip_prompt=True)
```

Después de que la cuantificación sea exitosa, continúa la ejecución para llamar a la NPU y correr el modelo Phi-3.

```python
generation_args = {
   "max_new_tokens": 1024,
   "return_full_text": False,
   "temperature": 0.3,
   "do_sample": False,
   "streamer": text_streamer,
}

pipe = pipeline(
   "text-generation",
   model=model,
   tokenizer=tokenizer,
)

query = "<|system|>You are a helpful AI assistant.<|end|><|user|>Can you introduce yourself?<|end|><|assistant|>"

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    pipe(query, **generation_args)
```

Al ejecutar el código, podemos ver el estado de ejecución de la NPU a través del Administrador de tareas.

![NPU](../../../../../translated_images/es/aipc_NPU.7a3cb6db47b377e1.png)

***Ejemplos*** : [AIPC_NPU_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_NPU_DEMO.ipynb)

## **2. Usar DirectML + ONNX Runtime para ejecutar el modelo Phi-3**

### **Qué es DirectML**

[DirectML](https://github.com/microsoft/DirectML) es una biblioteca de alto rendimiento acelerada por hardware basada en DirectX 12 para aprendizaje automático. DirectML proporciona aceleración por GPU para tareas comunes de machine learning en una amplia gama de hardware y controladores compatibles, incluyendo todas las GPUs compatibles con DirectX 12 de fabricantes como AMD, Intel, NVIDIA y Qualcomm.

Cuando se usa de forma independiente, la API de DirectML es una biblioteca de bajo nivel de DirectX 12, adecuada para aplicaciones de alto rendimiento y baja latencia como frameworks, juegos y otras aplicaciones en tiempo real. La interoperabilidad fluida de DirectML con Direct3D 12, así como su bajo overhead y conformidad en diferentes hardware, hacen que DirectML sea ideal para acelerar el aprendizaje automático cuando se desea alto rendimiento y la confiabilidad y predictibilidad de resultados en distintos dispositivos es crítica.

***Nota*** : La última versión de DirectML ya soporta NPU (https://devblogs.microsoft.com/directx/introducing-neural-processor-unit-npu-support-in-directml-developer-preview/)

### DirectML y CUDA en cuanto a sus capacidades y rendimiento:

**DirectML** es una biblioteca de machine learning desarrollada por Microsoft. Está diseñada para acelerar cargas de trabajo de aprendizaje automático en dispositivos Windows, incluyendo desktops, laptops y dispositivos edge.  
- Basado en DX12: DirectML está construido sobre DirectX 12 (DX12), que ofrece un amplio soporte de hardware en GPUs, incluyendo NVIDIA y AMD.  
- Soporte más amplio: Al aprovechar DX12, DirectML puede funcionar con cualquier GPU que soporte DX12, incluso GPUs integradas.  
- Procesamiento de imágenes: DirectML procesa imágenes y otros datos usando redes neuronales, siendo adecuado para tareas como reconocimiento de imágenes, detección de objetos y más.  
- Facilidad de configuración: Configurar DirectML es sencillo y no requiere SDKs o bibliotecas específicas de fabricantes de GPU.  
- Rendimiento: En algunos casos, DirectML tiene buen rendimiento y puede ser más rápido que CUDA, especialmente en ciertas cargas de trabajo.  
- Limitaciones: Sin embargo, hay casos donde DirectML puede ser más lento, particularmente con grandes lotes en float16.

**CUDA** es la plataforma de computación paralela y modelo de programación de NVIDIA. Permite a los desarrolladores aprovechar la potencia de las GPUs NVIDIA para computación general, incluyendo machine learning y simulaciones científicas.  
- Específico de NVIDIA: CUDA está estrechamente integrado con GPUs NVIDIA y está diseñado específicamente para ellas.  
- Altamente optimizado: Proporciona un rendimiento excelente para tareas aceleradas por GPU, especialmente con GPUs NVIDIA.  
- Ampliamente usado: Muchos frameworks y bibliotecas de machine learning (como TensorFlow y PyTorch) soportan CUDA.  
- Personalización: Los desarrolladores pueden ajustar configuraciones de CUDA para tareas específicas, lo que puede llevar a un rendimiento óptimo.  
- Limitaciones: Sin embargo, la dependencia de CUDA en hardware NVIDIA puede ser limitante si se busca compatibilidad más amplia con diferentes GPUs.

### Elegir entre DirectML y CUDA

La elección entre DirectML y CUDA depende de tu caso de uso específico, disponibilidad de hardware y preferencias.  
Si buscas mayor compatibilidad y facilidad de configuración, DirectML puede ser una buena opción. Sin embargo, si cuentas con GPUs NVIDIA y necesitas un rendimiento altamente optimizado, CUDA sigue siendo una opción fuerte. En resumen, ambos tienen sus fortalezas y debilidades, así que considera tus requerimientos y hardware disponible al tomar una decisión.

### **IA generativa con ONNX Runtime**

En la era de la IA, la portabilidad de los modelos de IA es muy importante. ONNX Runtime permite desplegar fácilmente modelos entrenados en diferentes dispositivos. Los desarrolladores no necesitan preocuparse por el framework de inferencia y pueden usar una API unificada para completar la inferencia del modelo. En la era de la IA generativa, ONNX Runtime también ha realizado optimizaciones de código (https://onnxruntime.ai/docs/genai/). A través de ONNX Runtime optimizado, el modelo generativo cuantificado puede inferirse en diferentes terminales. En Generative AI con ONNX Runtime, puedes inferir modelos de IA mediante APIs en Python, C#, C/C++. Por supuesto, el despliegue en iPhone puede aprovechar la API de Generative AI con ONNX Runtime en C++.

[Código de ejemplo](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx)

***Compilar la biblioteca de Generative AI con ONNX Runtime***

```bash

winget install --id=Kitware.CMake  -e

git clone https://github.com/microsoft/onnxruntime.git

cd .\onnxruntime\

./build.bat --build_shared_lib --skip_tests --parallel --use_dml --config Release

cd ../

git clone https://github.com/microsoft/onnxruntime-genai.git

cd .\onnxruntime-genai\

mkdir ort

cd ort

mkdir include

mkdir lib

copy ..\onnxruntime\include\onnxruntime\core\providers\dml\dml_provider_factory.h ort\include

copy ..\onnxruntime\include\onnxruntime\core\session\onnxruntime_c_api.h ort\include

copy ..\onnxruntime\build\Windows\Release\Release\*.dll ort\lib

copy ..\onnxruntime\build\Windows\Release\Release\onnxruntime.lib ort\lib

python build.py --use_dml


```

**Instalar la biblioteca**

```bash

pip install .\onnxruntime_genai_directml-0.3.0.dev0-cp310-cp310-win_amd64.whl

```

Este es el resultado de la ejecución

![DML](../../../../../translated_images/es/aipc_DML.52a44180393ab491.png)

***Ejemplos*** : [AIPC_DirectML_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_DirectML_DEMO.ipynb)

## **3. Usar Intel OpenVino para ejecutar el modelo Phi-3**

### **Qué es OpenVINO**

[OpenVINO](https://github.com/openvinotoolkit/openvino) es un kit de herramientas de código abierto para optimizar y desplegar modelos de deep learning. Proporciona un rendimiento mejorado para modelos de visión, audio y lenguaje de frameworks populares como TensorFlow, PyTorch y más. Comienza con OpenVINO. OpenVINO también puede usarse en combinación con CPU y GPU para ejecutar el modelo Phi-3.

***Nota***: Actualmente, OpenVINO no soporta NPU.

### **Instalar la biblioteca OpenVINO**

```bash

 pip install git+https://github.com/huggingface/optimum-intel.git

 pip install git+https://github.com/openvinotoolkit/nncf.git

 pip install openvino-nightly

```

### **Ejecutando Phi-3 con OpenVINO**

Al igual que con la NPU, OpenVINO completa la llamada a modelos generativos ejecutando modelos cuantificados. Primero necesitamos cuantificar el modelo Phi-3 y completar la cuantificación del modelo desde la línea de comandos usando optimum-cli.

**INT4**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code ./openvinomodel/phi3/int4

```

**FP16**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format fp16 --trust-remote-code ./openvinomodel/phi3/fp16

```

El formato convertido, así:

![openvino_convert](../../../../../translated_images/es/aipc_OpenVINO_convert.9e6360b65331ffca.png)

Carga las rutas del modelo (model_dir), configuraciones relacionadas (ov_config = {"PERFORMANCE_HINT": "LATENCY", "NUM_STREAMS": "1", "CACHE_DIR": ""}) y dispositivos acelerados por hardware (GPU.0) a través de OVModelForCausalLM

```python

ov_model = OVModelForCausalLM.from_pretrained(
     model_dir,
     device='GPU.0',
     ov_config=ov_config,
     config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
     trust_remote_code=True,
)

```

Al ejecutar el código, podemos ver el estado de ejecución de la GPU a través del Administrador de tareas.

![openvino_gpu](../../../../../translated_images/es/aipc_OpenVINO_GPU.20180edfffd91e55.png)

***Ejemplos*** : [AIPC_OpenVino_Demo.ipynb](../../../../../code/03.Inference/AIPC/AIPC_OpenVino_Demo.ipynb)

### ***Nota*** : Los tres métodos anteriores tienen sus propias ventajas, pero se recomienda usar la aceleración NPU para la inferencia en AI PC.

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.