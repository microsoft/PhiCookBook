<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-05-07T10:34:53+00:00",
  "source_file": "md/03.FineTuning/olive-lab/readme.md",
  "language_code": "es"
}
-->
# Lab. Optimiza modelos de IA para inferencia en el dispositivo

## Introducción 

> [!IMPORTANT]
> Este laboratorio requiere una **GPU Nvidia A10 o A100** con los controladores asociados y el toolkit CUDA (versión 12+) instalados.

> [!NOTE]
> Este es un laboratorio de **35 minutos** que te dará una introducción práctica a los conceptos clave para optimizar modelos para inferencia en el dispositivo usando OLIVE.

## Objetivos de aprendizaje

Al finalizar este laboratorio, podrás usar OLIVE para:

- Cuantizar un modelo de IA usando el método de cuantización AWQ.
- Ajustar un modelo de IA para una tarea específica.
- Generar adaptadores LoRA (modelo ajustado) para una inferencia eficiente en el dispositivo con ONNX Runtime.

### Qué es Olive

Olive (*O*NNX *live*) es un conjunto de herramientas de optimización de modelos con una CLI que te permite distribuir modelos para ONNX runtime +++https://onnxruntime.ai+++ con calidad y rendimiento.

![Olive Flow](../../../../../translated_images/olive-flow.5daf97340275f8b61397e91430ff02724a2547937b352e7fdfc2f669c56dcd35.es.png)

La entrada para Olive suele ser un modelo de PyTorch o Hugging Face y la salida es un modelo ONNX optimizado que se ejecuta en un dispositivo (objetivo de despliegue) con ONNX runtime. Olive optimizará el modelo para el acelerador AI del objetivo de despliegue (NPU, GPU, CPU) proporcionado por un fabricante de hardware como Qualcomm, AMD, Nvidia o Intel.

Olive ejecuta un *workflow*, que es una secuencia ordenada de tareas individuales de optimización de modelos llamadas *passes* — algunos ejemplos de passes incluyen: compresión del modelo, captura del grafo, cuantización, optimización del grafo. Cada pass tiene un conjunto de parámetros que pueden ajustarse para lograr las mejores métricas, como precisión y latencia, evaluadas por el evaluador correspondiente. Olive emplea una estrategia de búsqueda que usa un algoritmo para ajustar automáticamente cada pass uno por uno o un conjunto de passes juntos.

#### Beneficios de Olive

- **Reduce la frustración y el tiempo** de experimentación manual por prueba y error con diferentes técnicas para optimización de grafos, compresión y cuantización. Define tus restricciones de calidad y rendimiento y deja que Olive encuentre automáticamente el mejor modelo para ti.
- **Más de 40 componentes integrados** para optimización de modelos que cubren técnicas avanzadas en cuantización, compresión, optimización de grafos y ajuste fino.
- **CLI fácil de usar** para tareas comunes de optimización de modelos. Por ejemplo, olive quantize, olive auto-opt, olive finetune.
- Empaquetado y despliegue de modelos incorporados.
- Soporta generación de modelos para **Multi LoRA serving**.
- Construye workflows usando YAML/JSON para orquestar tareas de optimización y despliegue de modelos.
- Integración con **Hugging Face** y **Azure AI**.
- Mecanismo de **caché** incorporado para **ahorrar costos**.

## Instrucciones del laboratorio
> [!NOTE]
> Asegúrate de haber provisionado tu Azure AI Hub y Proyecto y configurado tu cómputo A100 según el Laboratorio 1.

### Paso 0: Conéctate a tu Azure AI Compute

Te conectarás al cómputo Azure AI usando la función remota en **VS Code.** 

1. Abre tu aplicación de escritorio **VS Code**:
1. Abre la **paleta de comandos** con **Shift+Ctrl+P**
1. En la paleta de comandos busca **AzureML - remote: Connect to compute instance in New Window**.
1. Sigue las instrucciones en pantalla para conectarte al Compute. Esto implicará seleccionar tu Suscripción de Azure, Grupo de Recursos, Proyecto y el nombre del Cómputo que configuraste en el Laboratorio 1.
1. Una vez conectado a tu nodo Azure ML Compute, esto se mostrará en la **parte inferior izquierda de Visual Code** `><Azure ML: Compute Name`

### Paso 1: Clona este repositorio

En VS Code, puedes abrir una terminal nueva con **Ctrl+J** y clonar este repositorio:

En la terminal deberías ver el prompt

```
azureuser@computername:~/cloudfiles/code$ 
```
Clona la solución

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Paso 2: Abre la carpeta en VS Code

Para abrir VS Code en la carpeta correspondiente ejecuta el siguiente comando en la terminal, que abrirá una ventana nueva:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Alternativamente, puedes abrir la carpeta seleccionando **Archivo** > **Abrir carpeta**. 

### Paso 3: Dependencias

Abre una terminal en VS Code en tu instancia Azure AI Compute (atajo: **Ctrl+J**) y ejecuta los siguientes comandos para instalar las dependencias:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> La instalación de todas las dependencias tomará alrededor de 5 minutos.

En este laboratorio descargarás y subirás modelos al catálogo de modelos Azure AI. Para acceder al catálogo de modelos, necesitas iniciar sesión en Azure con:

```bash
az login
```

> [!NOTE]
> Al iniciar sesión se te pedirá seleccionar tu suscripción. Asegúrate de seleccionar la suscripción proporcionada para este laboratorio.

### Paso 4: Ejecuta comandos de Olive

Abre una terminal en VS Code en tu instancia Azure AI Compute (atajo: **Ctrl+J**) y asegúrate de que el entorno conda `olive-ai` esté activado:

```bash
conda activate olive-ai
```

Luego, ejecuta los siguientes comandos de Olive en la línea de comandos.

1. **Inspecciona los datos:** En este ejemplo, vas a ajustar el modelo Phi-3.5-Mini para que esté especializado en responder preguntas relacionadas con viajes. El código a continuación muestra los primeros registros del conjunto de datos, que están en formato JSON lines:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **Cuantiza el modelo:** Antes de entrenar el modelo, primero lo cuantizas con el siguiente comando que usa una técnica llamada Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ cuantiza los pesos de un modelo considerando las activaciones producidas durante la inferencia. Esto significa que el proceso de cuantización toma en cuenta la distribución real de datos en las activaciones, lo que permite preservar mejor la precisión del modelo en comparación con métodos tradicionales de cuantización de pesos.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    Toma **~8 minutos** completar la cuantización AWQ, lo que **reduce el tamaño del modelo de ~7.5GB a ~2.5GB**.
   
   En este laboratorio te mostramos cómo ingresar modelos desde Hugging Face (por ejemplo: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` ajusta el modelo cuantizado. Cuantizar el modelo *antes* del ajuste fino en lugar de después ofrece mejor precisión ya que el ajuste fino recupera parte de la pérdida causada por la cuantización.
    
    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```
    
    Toma **~6 minutos** completar el ajuste fino (con 100 pasos).

1. **Optimiza:** Con el modelo entrenado, ahora optimízalo usando los argumentos `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` de Olive - pero para este laboratorio usaremos CPU.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```
    
    Toma **~5 minutos** completar la optimización.

### Paso 5: Prueba rápida de inferencia del modelo

Para probar la inferencia del modelo, crea un archivo Python en tu carpeta llamado **app.py** y copia y pega el siguiente código:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

Ejecuta el código usando:

```bash
python app.py
```

### Paso 6: Sube el modelo a Azure AI

Subir el modelo a un repositorio de modelos Azure AI hace que el modelo sea compartible con otros miembros de tu equipo de desarrollo y también gestiona el control de versiones del modelo. Para subir el modelo ejecuta el siguiente comando:

> [!NOTE]
> Actualiza los valores `{}`` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group ` para "resourceGroup" y el nombre del Proyecto Azure AI, luego ejecuta el siguiente comando

```
az ml workspace show
```

O bien, accede a +++ai.azure.com+++ y selecciona **centro de administración** **proyecto** **visión general**

Actualiza los marcadores de posición `{}` con el nombre de tu grupo de recursos y el nombre del Proyecto Azure AI.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

Luego podrás ver tu modelo subido y desplegarlo en https://ml.azure.com/model/list

**Aviso Legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables por malentendidos o interpretaciones erróneas que puedan derivarse del uso de esta traducción.