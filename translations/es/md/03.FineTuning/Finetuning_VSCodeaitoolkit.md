<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2bc0950f44919ac75a88c1a871680c2",
  "translation_date": "2025-07-17T08:59:46+00:00",
  "source_file": "md/03.FineTuning/Finetuning_VSCodeaitoolkit.md",
  "language_code": "es"
}
-->
## Bienvenido a AI Toolkit para VS Code

[AI Toolkit para VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) reúne varios modelos del Catálogo de Azure AI Studio y otros catálogos como Hugging Face. El toolkit facilita las tareas comunes de desarrollo para crear aplicaciones de IA con herramientas y modelos de IA generativa mediante:
- Comenzar con el descubrimiento de modelos y el playground.
- Ajuste fino e inferencia de modelos usando recursos locales.
- Ajuste fino e inferencia remotos usando recursos de Azure.

[Instalar AI Toolkit para VSCode](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/es/Aitoolkit.7157953df04812dc.png)


**[Private Preview]** Provisionamiento con un clic para Azure Container Apps para ejecutar ajuste fino e inferencia de modelos en la nube.

Ahora, vamos a comenzar con el desarrollo de tu aplicación de IA:

- [Bienvenido a AI Toolkit para VS Code](../../../../md/03.FineTuning)
- [Desarrollo Local](../../../../md/03.FineTuning)
  - [Preparativos](../../../../md/03.FineTuning)
  - [Activar Conda](../../../../md/03.FineTuning)
  - [Solo ajuste fino del modelo base](../../../../md/03.FineTuning)
  - [Ajuste fino e inferencia del modelo](../../../../md/03.FineTuning)
  - [Ajuste fino del modelo](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [Ejemplos y recursos de ajuste fino](../../../../md/03.FineTuning)
- [**\[Private Preview\]** Desarrollo Remoto](../../../../md/03.FineTuning)
  - [Requisitos previos](../../../../md/03.FineTuning)
  - [Configurar un proyecto de desarrollo remoto](../../../../md/03.FineTuning)
  - [Provisionar recursos de Azure](../../../../md/03.FineTuning)
  - [\[Opcional\] Añadir token de Huggingface al secreto de Azure Container App](../../../../md/03.FineTuning)
  - [Ejecutar ajuste fino](../../../../md/03.FineTuning)
  - [Provisionar endpoint de inferencia](../../../../md/03.FineTuning)
  - [Desplegar el endpoint de inferencia](../../../../md/03.FineTuning)
  - [Uso avanzado](../../../../md/03.FineTuning)

## Desarrollo Local
### Preparativos

1. Asegúrate de que el driver NVIDIA esté instalado en el host.
2. Ejecuta `huggingface-cli login` si vas a usar HF para la utilización de datasets.
3. Explicaciones de las configuraciones clave de `Olive` para cualquier ajuste que modifique el uso de memoria.

### Activar Conda
Dado que usamos un entorno WSL compartido, necesitas activar manualmente el entorno conda. Después de este paso, podrás ejecutar ajuste fino o inferencia.

```bash
conda activate [conda-env-name] 
```

### Solo ajuste fino del modelo base
Para probar solo el modelo base sin ajuste fino, puedes ejecutar este comando después de activar conda.

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### Ajuste fino e inferencia del modelo

Una vez que el espacio de trabajo esté abierto en un contenedor de desarrollo, abre una terminal (la ruta predeterminada es la raíz del proyecto) y ejecuta el siguiente comando para ajustar un LLM con el dataset seleccionado.

```bash
python finetuning/invoke_olive.py 
```

Los puntos de control y el modelo final se guardarán en la carpeta `models`.

Luego, ejecuta la inferencia con el modelo ajustado a través de chats en una `consola`, `navegador web` o `prompt flow`.

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

Para usar `prompt flow` en VS Code, consulta este [Inicio Rápido](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html).

### Ajuste fino del modelo

A continuación, descarga el modelo correspondiente según la disponibilidad de GPU en tu dispositivo.

Para iniciar la sesión de ajuste fino local usando QLoRA, selecciona un modelo del catálogo que quieras ajustar.
| Plataforma(s) | GPU disponible | Nombre del modelo | Tamaño (GB) |
|---------|---------|--------|--------|
| Windows | Sí | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | Sí | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | No | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_Nota_** No necesitas una cuenta de Azure para descargar los modelos.

El modelo Phi3-mini (int4) tiene un tamaño aproximado de 2GB-3GB. Dependiendo de la velocidad de tu red, la descarga puede tardar unos minutos.

Comienza seleccionando un nombre y ubicación para el proyecto.
Luego, elige un modelo del catálogo. Se te pedirá descargar la plantilla del proyecto. Después, puedes hacer clic en "Configurar Proyecto" para ajustar varias configuraciones.

### Microsoft Olive

Usamos [Olive](https://microsoft.github.io/Olive/why-olive.html) para ejecutar el ajuste fino QLoRA en un modelo PyTorch de nuestro catálogo. Todas las configuraciones están preestablecidas con valores por defecto para optimizar el proceso de ajuste fino local con un uso eficiente de memoria, pero pueden ajustarse según tu escenario.

### Ejemplos y recursos de ajuste fino

- [Guía de inicio para ajuste fino](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [Ajuste fino con un dataset de HuggingFace](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-hf-dataset.md)
- [Ajuste fino con un dataset simple](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-simple-dataset.md)

## **[Private Preview]** Desarrollo Remoto

### Requisitos previos

1. Para ejecutar el ajuste fino del modelo en tu entorno remoto de Azure Container App, asegúrate de que tu suscripción tenga suficiente capacidad de GPU. Envía un [ticket de soporte](https://azure.microsoft.com/support/create-ticket/) para solicitar la capacidad necesaria para tu aplicación. [Más información sobre capacidad de GPU](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)
2. Si usas un dataset privado en HuggingFace, asegúrate de tener una [cuenta de HuggingFace](https://huggingface.co/?WT.mc_id=aiml-137032-kinfeylo) y [generar un token de acceso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=aiml-137032-kinfeylo)
3. Habilita la función de ajuste fino e inferencia remotos en AI Toolkit para VS Code
   1. Abre la configuración de VS Code seleccionando *Archivo -> Preferencias -> Configuración*.
   2. Navega a *Extensiones* y selecciona *AI Toolkit*.
   3. Activa la opción *"Enable Remote Fine-tuning And Inference"*.
   4. Recarga VS Code para que los cambios tengan efecto.

- [Ajuste fino remoto](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-finetuning.md)

### Configurar un proyecto de desarrollo remoto
1. Ejecuta la paleta de comandos `AI Toolkit: Focus on Resource View`.
2. Navega a *Model Fine-tuning* para acceder al catálogo de modelos. Asigna un nombre a tu proyecto y selecciona su ubicación en tu máquina. Luego, haz clic en el botón *"Configure Project"*.
3. Configuración del proyecto
    1. Evita activar la opción *"Fine-tune locally"*.
    2. Aparecerán las configuraciones de Olive con valores predeterminados preestablecidos. Ajusta y completa estas configuraciones según sea necesario.
    3. Continúa con *Generate Project*. Esta etapa usa WSL e implica configurar un nuevo entorno Conda, preparándose para futuras actualizaciones que incluirán Dev Containers.
4. Haz clic en *"Relaunch Window In Workspace"* para abrir tu proyecto de desarrollo remoto.

> **Nota:** El proyecto actualmente funciona solo localmente o remotamente dentro de AI Toolkit para VS Code. Si eliges *"Fine-tune locally"* durante la creación del proyecto, funcionará exclusivamente en WSL sin capacidades de desarrollo remoto. Por otro lado, si no activas *"Fine-tune locally"*, el proyecto estará limitado al entorno remoto de Azure Container App.

### Provisionar recursos de Azure
Para comenzar, necesitas provisionar el recurso de Azure para ajuste fino remoto. Hazlo ejecutando el comando `AI Toolkit: Provision Azure Container Apps job for fine-tuning` desde la paleta de comandos.

Monitorea el progreso del provisionamiento a través del enlace que aparece en el canal de salida.

### [Opcional] Añadir token de Huggingface al secreto de Azure Container App
Si usas un dataset privado de HuggingFace, configura tu token de HuggingFace como variable de entorno para evitar iniciar sesión manualmente en Hugging Face Hub.
Puedes hacerlo con el comando `AI Toolkit: Add Azure Container Apps Job secret for fine-tuning`. Con este comando, puedes establecer el nombre del secreto como [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) y usar tu token de Hugging Face como valor del secreto.

### Ejecutar ajuste fino
Para iniciar el trabajo de ajuste fino remoto, ejecuta el comando `AI Toolkit: Run fine-tuning`.

Para ver los registros del sistema y consola, puedes visitar el portal de Azure usando el enlace en el panel de salida (más pasos en [Ver y consultar registros en Azure](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)). O bien, puedes ver los registros de consola directamente en el panel de salida de VSCode ejecutando el comando `AI Toolkit: Show the running fine-tuning job streaming logs`.
> **Nota:** El trabajo puede estar en cola debido a recursos insuficientes. Si no se muestran los registros, ejecuta el comando `AI Toolkit: Show the running fine-tuning job streaming logs`, espera un momento y vuelve a ejecutarlo para reconectar con el streaming de logs.

Durante este proceso, se usará QLoRA para el ajuste fino, creando adaptadores LoRA para que el modelo los use durante la inferencia.
Los resultados del ajuste fino se almacenarán en Azure Files.

### Provisionar endpoint de inferencia
Después de entrenar los adaptadores en el entorno remoto, usa una aplicación simple de Gradio para interactuar con el modelo.
Al igual que con el ajuste fino, necesitas configurar los recursos de Azure para la inferencia remota ejecutando el comando `AI Toolkit: Provision Azure Container Apps for inference` desde la paleta de comandos.

Por defecto, la suscripción y el grupo de recursos para inferencia deben coincidir con los usados para el ajuste fino. La inferencia usará el mismo entorno de Azure Container App y accederá al modelo y adaptador almacenados en Azure Files, generados durante el paso de ajuste fino.

### Desplegar el endpoint de inferencia
Si deseas modificar el código de inferencia o recargar el modelo de inferencia, ejecuta el comando `AI Toolkit: Deploy for inference`. Esto sincronizará tu código más reciente con Azure Container App y reiniciará la réplica.

Una vez que el despliegue se complete con éxito, podrás acceder a la API de inferencia haciendo clic en el botón "*Go to Inference Endpoint*" que aparece en la notificación de VSCode. También puedes encontrar el endpoint web API bajo `ACA_APP_ENDPOINT` en `./infra/inference.config.json` y en el panel de salida. Ya estás listo para evaluar el modelo usando este endpoint.

### Uso avanzado
Para más información sobre desarrollo remoto con AI Toolkit, consulta la documentación de [Ajuste fino de modelos remotamente](https://aka.ms/ai-toolkit/remote-provision) y [Inferencia con el modelo ajustado](https://aka.ms/ai-toolkit/remote-inference).

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.