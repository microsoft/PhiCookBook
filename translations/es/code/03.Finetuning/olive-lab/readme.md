<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-03-27T03:29:09+00:00",
  "source_file": "code\\03.Finetuning\\olive-lab\\readme.md",
  "language_code": "es"
}
-->
# Laboratorio. Optimizar modelos de IA para inferencia en dispositivos

## Introducción 

> [!IMPORTANT]
> Este laboratorio requiere una **GPU Nvidia A10 o A100** con los controladores asociados y el kit de herramientas CUDA (versión 12+) instalados.

> [!NOTE]
> Este es un laboratorio de **35 minutos** que te brindará una introducción práctica a los conceptos clave de la optimización de modelos para inferencia en dispositivos utilizando OLIVE.

## Objetivos de aprendizaje

Al finalizar este laboratorio, podrás usar OLIVE para:

- Cuantificar un modelo de IA utilizando el método de cuantificación AWQ.
- Ajustar un modelo de IA para una tarea específica.
- Generar adaptadores LoRA (modelo ajustado) para inferencia eficiente en dispositivos utilizando ONNX Runtime.

### ¿Qué es Olive?

Olive (*O*NNX *live*) es una herramienta de optimización de modelos con una interfaz CLI que te permite implementar modelos para ONNX runtime +++https://onnxruntime.ai+++ con calidad y rendimiento.

![Flujo de Olive](../../../../../translated_images/olive-flow.5beac74493fb2216eb8578519cfb1c4a1e752a3536bc755c4545bd0959634684.es.png)

El input para Olive suele ser un modelo de PyTorch o Hugging Face y el output es un modelo ONNX optimizado que se ejecuta en un dispositivo (objetivo de despliegue) con ONNX runtime. Olive optimiza el modelo para el acelerador de IA del objetivo de despliegue (NPU, GPU, CPU) proporcionado por un proveedor de hardware como Qualcomm, AMD, Nvidia o Intel.

Olive ejecuta un *workflow*, que es una secuencia ordenada de tareas individuales de optimización de modelos llamadas *passes* - algunos ejemplos de passes incluyen: compresión de modelos, captura de gráficos, cuantificación, optimización de gráficos. Cada pass tiene un conjunto de parámetros que se pueden ajustar para lograr las mejores métricas, como precisión y latencia, que son evaluadas por el evaluador correspondiente. Olive utiliza una estrategia de búsqueda con un algoritmo para ajustar automáticamente cada pass, ya sea uno por uno o en conjunto.

#### Beneficios de Olive

- **Reduce la frustración y el tiempo** de la experimentación manual con técnicas de optimización de gráficos, compresión y cuantificación. Define tus restricciones de calidad y rendimiento y deja que Olive encuentre automáticamente el mejor modelo para ti.
- **Más de 40 componentes integrados de optimización de modelos** que cubren técnicas de vanguardia en cuantificación, compresión, optimización de gráficos y ajuste fino.
- **CLI fácil de usar** para tareas comunes de optimización de modelos. Por ejemplo, olive quantize, olive auto-opt, olive finetune.
- Empaquetado y despliegue de modelos integrado.
- Compatible con la generación de modelos para **Multi LoRA serving**.
- Construye workflows usando YAML/JSON para orquestar tareas de optimización y despliegue de modelos.
- Integración con **Hugging Face** y **Azure AI**.
- Mecanismo de **caching** integrado para **reducir costos**.

## Instrucciones del laboratorio
> [!NOTE]
> Asegúrate de haber configurado tu Azure AI Hub y Proyecto y de haber preparado tu recurso A100 como se indica en el Laboratorio 1.

### Paso 0: Conéctate a tu Azure AI Compute

Te conectarás al recurso de Azure AI Compute usando la función remota en **VS Code.** 

1. Abre tu aplicación de escritorio **VS Code**:
1. Abre la **paleta de comandos** usando **Shift+Ctrl+P**
1. En la paleta de comandos busca **AzureML - remote: Connect to compute instance in New Window**.
1. Sigue las instrucciones en pantalla para conectarte al Compute. Esto implicará seleccionar tu Suscripción de Azure, Grupo de Recursos, Proyecto y nombre del Compute que configuraste en el Laboratorio 1.
1. Una vez conectado al nodo de Azure ML Compute, esto se mostrará en la **parte inferior izquierda de Visual Code** `><Azure ML: Compute Name`

### Paso 1: Clonar este repositorio

En VS Code, puedes abrir un nuevo terminal con **Ctrl+J** y clonar este repositorio:

En el terminal deberías ver el prompt

```
azureuser@computername:~/cloudfiles/code$ 
```
Clona la solución 

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Paso 2: Abrir carpeta en VS Code

Para abrir VS Code en la carpeta relevante ejecuta el siguiente comando en el terminal, lo que abrirá una nueva ventana:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Alternativamente, puedes abrir la carpeta seleccionando **Archivo** > **Abrir carpeta**. 

### Paso 3: Dependencias

Abre una ventana de terminal en VS Code en tu instancia de Azure AI Compute (tip: **Ctrl+J**) y ejecuta los siguientes comandos para instalar las dependencias:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> Tomará aproximadamente ~5 minutos instalar todas las dependencias.

En este laboratorio descargarás y subirás modelos al catálogo de modelos de Azure AI. Para acceder al catálogo de modelos, necesitarás iniciar sesión en Azure utilizando:

```bash
az login
```

> [!NOTE]
> Durante el inicio de sesión se te pedirá seleccionar tu suscripción. Asegúrate de configurar la suscripción proporcionada para este laboratorio.

### Paso 4: Ejecutar comandos de Olive 

Abre una ventana de terminal en VS Code en tu instancia de Azure AI Compute (tip: **Ctrl+J**) y asegúrate de que el entorno conda `olive-ai` esté activado:

```bash
conda activate olive-ai
```

A continuación, ejecuta los siguientes comandos de Olive en la línea de comandos.

1. **Inspeccionar los datos:** En este ejemplo, ajustarás el modelo Phi-3.5-Mini para que se especialice en responder preguntas relacionadas con viajes. El siguiente código muestra los primeros registros del conjunto de datos, que están en formato JSON lines:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **Cuantificar el modelo:** Antes de entrenar el modelo, primero lo cuantificarás con el siguiente comando que utiliza una técnica llamada Cuantificación Activa Consciente (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ cuantifica los pesos de un modelo considerando las activaciones producidas durante la inferencia. Esto significa que el proceso de cuantificación toma en cuenta la distribución real de los datos en las activaciones, lo que conduce a una mejor preservación de la precisión del modelo en comparación con los métodos tradicionales de cuantificación de pesos.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    Este proceso toma **~8 minutos** y **reduce el tamaño del modelo de ~7.5GB a ~2.5GB**.
   
   En este laboratorio, te mostramos cómo ingresar modelos desde Hugging Face (por ejemplo: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` ajusta el modelo cuantificado. Cuantificar el modelo *antes* del ajuste en lugar de después proporciona mejor precisión, ya que el proceso de ajuste recupera parte de la pérdida ocasionada por la cuantificación.
    
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
    
    Este proceso toma **~6 minutos** y se realiza en 100 pasos.

1. **Optimizar:** Con el modelo entrenado, ahora lo optimizas utilizando los argumentos `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` de Olive - pero para los propósitos de este laboratorio utilizaremos CPU.

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
    
    Este proceso toma **~5 minutos**.

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

Ejecuta el código utilizando:

```bash
python app.py
```

### Paso 6: Subir modelo a Azure AI

Subir el modelo a un repositorio de modelos de Azure AI hace que el modelo sea compartible con otros miembros de tu equipo de desarrollo y también maneja el control de versiones del modelo. Para subir el modelo, ejecuta el siguiente comando:

> [!NOTE]
> Actualiza los campos `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"` y nombre del Proyecto de Azure AI, ejecuta el siguiente comando 

```
az ml workspace show
```

También puedes hacerlo accediendo a +++ai.azure.com+++ y seleccionando **centro de gestión**, **proyecto** y **vista general**.

Actualiza los campos `{}` con el nombre de tu grupo de recursos y nombre del Proyecto de Azure AI.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
Luego podrás ver tu modelo subido y desplegarlo en https://ml.azure.com/model/list

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.