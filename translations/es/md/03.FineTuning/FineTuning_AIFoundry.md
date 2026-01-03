<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c1559c5af6caccf6f623fd43a6b3a9a3",
  "translation_date": "2025-07-17T05:54:28+00:00",
  "source_file": "md/03.FineTuning/FineTuning_AIFoundry.md",
  "language_code": "es"
}
-->
# Ajuste fino de Phi-3 con Azure AI Foundry

Exploremos cómo ajustar finamente el modelo de lenguaje Phi-3 Mini de Microsoft usando Azure AI Foundry. El ajuste fino te permite adaptar Phi-3 Mini a tareas específicas, haciéndolo aún más potente y consciente del contexto.

## Consideraciones

- **Capacidades:** ¿Qué modelos se pueden ajustar finamente? ¿Para qué se puede ajustar el modelo base?
- **Costo:** ¿Cuál es el modelo de precios para el ajuste fino?
- **Personalización:** ¿Cuánto puedo modificar el modelo base y de qué maneras?
- **Comodidad:** ¿Cómo se realiza el ajuste fino? ¿Necesito escribir código personalizado? ¿Debo aportar mi propia capacidad de cómputo?
- **Seguridad:** Los modelos ajustados finamente pueden presentar riesgos de seguridad. ¿Existen mecanismos para proteger contra daños no intencionados?

![AIFoundry Models](../../../../translated_images/AIFoundryModels.0e1b16f7d0b09b73.es.png)

## Preparación para el ajuste fino

### Requisitos previos

> [!NOTE]
> Para los modelos de la familia Phi-3, la oferta de ajuste fino bajo el modelo de pago por uso solo está disponible con hubs creados en la región **East US 2**.

- Una suscripción de Azure. Si no tienes una, crea una [cuenta de Azure de pago](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) para comenzar.

- Un [proyecto AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Se utilizan controles de acceso basados en roles de Azure (Azure RBAC) para otorgar permisos en Azure AI Foundry. Para realizar los pasos de este artículo, tu cuenta debe tener asignado el __rol de Azure AI Developer__ en el grupo de recursos.

### Registro del proveedor de suscripción

Verifica que la suscripción esté registrada con el proveedor de recursos `Microsoft.Network`.

1. Inicia sesión en el [portal de Azure](https://portal.azure.com).
1. Selecciona **Suscripciones** en el menú lateral.
1. Selecciona la suscripción que deseas usar.
1. Selecciona **Configuración del proyecto AI** > **Proveedores de recursos** en el menú lateral.
1. Confirma que **Microsoft.Network** esté en la lista de proveedores. Si no, agrégalo.

### Preparación de datos

Prepara tus datos de entrenamiento y validación para ajustar el modelo. Tus conjuntos de datos deben contener ejemplos de entrada y salida que reflejen cómo quieres que el modelo se desempeñe.

Asegúrate de que todos los ejemplos de entrenamiento sigan el formato esperado para inferencia. Para un ajuste fino efectivo, garantiza un conjunto de datos equilibrado y diverso.

Esto implica mantener el balance de datos, incluir diversos escenarios y refinar periódicamente los datos de entrenamiento para alinearlos con expectativas del mundo real, lo que conduce a respuestas más precisas y equilibradas del modelo.

Diferentes tipos de modelos requieren formatos distintos para los datos de entrenamiento.

### Chat Completion

Los datos de entrenamiento y validación que uses **deben** estar formateados como un documento JSON Lines (JSONL). Para `Phi-3-mini-128k-instruct`, el conjunto de datos para ajuste fino debe estar en el formato conversacional que usa la API de Chat completions.

### Ejemplo de formato de archivo

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

El tipo de archivo soportado es JSON Lines. Los archivos se suben al datastore predeterminado y se ponen disponibles en tu proyecto.

## Ajuste fino de Phi-3 con Azure AI Foundry

Azure AI Foundry te permite personalizar grandes modelos de lenguaje con tus propios conjuntos de datos mediante un proceso llamado ajuste fino. El ajuste fino aporta un gran valor al permitir la personalización y optimización para tareas y aplicaciones específicas. Esto mejora el rendimiento, la eficiencia en costos, reduce la latencia y genera resultados adaptados.

![Finetune AI Foundry](../../../../translated_images/AIFoundryfinetune.193aaddce48d553c.es.png)

### Crear un nuevo proyecto

1. Inicia sesión en [Azure AI Foundry](https://ai.azure.com).

1. Selecciona **+Nuevo proyecto** para crear un nuevo proyecto en Azure AI Foundry.

    ![FineTuneSelect](../../../../translated_images/select-new-project.cd31c0404088d7a3.es.png)

1. Realiza las siguientes tareas:

    - Nombre del **Hub** del proyecto. Debe ser un valor único.
    - Selecciona el **Hub** a usar (crea uno nuevo si es necesario).

    ![FineTuneSelect](../../../../translated_images/create-project.ca3b71298b90e420.es.png)

1. Realiza las siguientes tareas para crear un nuevo hub:

    - Ingresa el **Nombre del Hub**. Debe ser un valor único.
    - Selecciona tu **Suscripción** de Azure.
    - Selecciona el **Grupo de recursos** a usar (crea uno nuevo si es necesario).
    - Selecciona la **Ubicación** que deseas usar.
    - Selecciona **Conectar servicios Azure AI** a usar (crea uno nuevo si es necesario).
    - Selecciona **Conectar Azure AI Search** para **Omitir conexión**.

    ![FineTuneSelect](../../../../translated_images/create-hub.49e53d235e80779e.es.png)

1. Selecciona **Siguiente**.
1. Selecciona **Crear un proyecto**.

### Preparación de datos

Antes del ajuste fino, recopila o crea un conjunto de datos relevante para tu tarea, como instrucciones de chat, pares de preguntas y respuestas, u otro texto pertinente. Limpia y preprocesa estos datos eliminando ruido, manejando valores faltantes y tokenizando el texto.

### Ajustar finamente modelos Phi-3 en Azure AI Foundry

> [!NOTE]
> El ajuste fino de modelos Phi-3 actualmente está soportado solo en proyectos ubicados en East US 2.

1. Selecciona **Catálogo de modelos** en la pestaña lateral izquierda.

1. Escribe *phi-3* en la **barra de búsqueda** y selecciona el modelo phi-3 que deseas usar.

    ![FineTuneSelect](../../../../translated_images/select-model.60ef2d4a6a3cec57.es.png)

1. Selecciona **Ajustar fino**.

    ![FineTuneSelect](../../../../translated_images/select-finetune.a976213b543dd9d8.es.png)

1. Ingresa el **Nombre del modelo ajustado**.

    ![FineTuneSelect](../../../../translated_images/finetune1.c2b39463f0d34148.es.png)

1. Selecciona **Siguiente**.

1. Realiza las siguientes tareas:

    - Selecciona el **tipo de tarea** como **Chat completion**.
    - Selecciona los **datos de entrenamiento** que deseas usar. Puedes subirlos a través de los datos de Azure AI Foundry o desde tu entorno local.

    ![FineTuneSelect](../../../../translated_images/finetune2.43cb099b1a94442d.es.png)

1. Selecciona **Siguiente**.

1. Sube los **datos de validación** que deseas usar o selecciona **División automática de datos de entrenamiento**.

    ![FineTuneSelect](../../../../translated_images/finetune3.fd96121b67dcdd92.es.png)

1. Selecciona **Siguiente**.

1. Realiza las siguientes tareas:

    - Selecciona el **multiplicador de tamaño de lote** que deseas usar.
    - Selecciona la **tasa de aprendizaje** que deseas usar.
    - Selecciona las **épocas** que deseas usar.

    ![FineTuneSelect](../../../../translated_images/finetune4.e18b80ffccb5834a.es.png)

1. Selecciona **Enviar** para iniciar el proceso de ajuste fino.

    ![FineTuneSelect](../../../../translated_images/select-submit.0a3802d581bac271.es.png)

1. Una vez que tu modelo esté ajustado, el estado aparecerá como **Completado**, como se muestra en la imagen a continuación. Ahora puedes desplegar el modelo y usarlo en tu propia aplicación, en el playground o en prompt flow. Para más información, consulta [Cómo desplegar la familia de modelos pequeños Phi-3 con Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/completed.4dc8d2357144cdef.es.png)

> [!NOTE]
> Para información más detallada sobre el ajuste fino de Phi-3, visita [Ajustar finamente modelos Phi-3 en Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Limpieza de tus modelos ajustados

Puedes eliminar un modelo ajustado desde la lista de modelos de ajuste fino en [Azure AI Foundry](https://ai.azure.com) o desde la página de detalles del modelo. Selecciona el modelo ajustado que deseas eliminar en la página de Ajuste fino y luego selecciona el botón Eliminar para borrarlo.

> [!NOTE]
> No puedes eliminar un modelo personalizado si tiene un despliegue activo. Primero debes eliminar el despliegue del modelo antes de poder eliminar el modelo personalizado.

## Costos y cuotas

### Consideraciones de costos y cuotas para modelos Phi-3 ajustados como servicio

Los modelos Phi ajustados como servicio son ofrecidos por Microsoft e integrados con Azure AI Foundry para su uso. Puedes consultar los precios al [desplegar](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) o ajustar los modelos en la pestaña de Precios y términos del asistente de despliegue.

## Filtrado de contenido

Los modelos desplegados como servicio bajo pago por uso están protegidos por Azure AI Content Safety. Cuando se despliegan en endpoints en tiempo real, puedes optar por desactivar esta capacidad. Con Azure AI Content Safety activado, tanto el prompt como la respuesta pasan por un conjunto de modelos de clasificación diseñados para detectar y prevenir la salida de contenido dañino. El sistema de filtrado detecta y actúa sobre categorías específicas de contenido potencialmente dañino tanto en las entradas como en las salidas. Aprende más sobre [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Configuración del ajuste fino**

Hiperparámetros: Define hiperparámetros como tasa de aprendizaje, tamaño de lote y número de épocas de entrenamiento.

**Función de pérdida**

Elige una función de pérdida adecuada para tu tarea (por ejemplo, entropía cruzada).

**Optimizador**

Selecciona un optimizador (por ejemplo, Adam) para las actualizaciones de gradiente durante el entrenamiento.

**Proceso de ajuste fino**

- Cargar modelo preentrenado: Carga el checkpoint de Phi-3 Mini.
- Añadir capas personalizadas: Agrega capas específicas para la tarea (por ejemplo, cabeza de clasificación para instrucciones de chat).

**Entrenar el modelo**  
Ajusta el modelo usando tu conjunto de datos preparado. Monitorea el progreso y ajusta los hiperparámetros según sea necesario.

**Evaluación y validación**

Conjunto de validación: Divide tus datos en conjuntos de entrenamiento y validación.

**Evaluar desempeño**

Usa métricas como precisión, F1-score o perplexidad para evaluar el rendimiento del modelo.

## Guardar modelo ajustado

**Checkpoint**  
Guarda el checkpoint del modelo ajustado para uso futuro.

## Despliegue

- Despliega como servicio web: Despliega tu modelo ajustado como un servicio web en Azure AI Foundry.
- Prueba el endpoint: Envía consultas de prueba al endpoint desplegado para verificar su funcionamiento.

## Iterar y mejorar

Itera: Si el rendimiento no es satisfactorio, ajusta hiperparámetros, añade más datos o realiza más épocas de ajuste fino.

## Monitorear y refinar

Monitorea continuamente el comportamiento del modelo y refínalo según sea necesario.

## Personalizar y extender

Tareas personalizadas: Phi-3 Mini puede ajustarse para diversas tareas más allá de instrucciones de chat. ¡Explora otros casos de uso!  
Experimenta: Prueba diferentes arquitecturas, combinaciones de capas y técnicas para mejorar el rendimiento.

> [!NOTE]
> El ajuste fino es un proceso iterativo. ¡Experimenta, aprende y adapta tu modelo para lograr los mejores resultados en tu tarea específica!

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.