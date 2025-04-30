<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cbe7629d254f1043193b7fe22524d55",
  "translation_date": "2025-03-27T08:57:46+00:00",
  "source_file": "md\\01.Introduction\\05\\Promptflow.md",
  "language_code": "es"
}
-->
# **Introduce Promptflow**

[Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) es una herramienta visual de automatización de flujos de trabajo que permite a los usuarios crear flujos de trabajo automatizados utilizando plantillas predefinidas y conectores personalizados. Está diseñada para que desarrolladores y analistas de negocios puedan construir rápidamente procesos automatizados para tareas como gestión de datos, colaboración y optimización de procesos. Con Prompt Flow, los usuarios pueden conectar fácilmente diferentes servicios, aplicaciones y sistemas, y automatizar procesos empresariales complejos.

Microsoft Prompt Flow está diseñado para simplificar el ciclo de desarrollo completo de aplicaciones de IA impulsadas por Modelos de Lenguaje Extensos (LLMs). Ya sea que estés ideando, creando prototipos, probando, evaluando o implementando aplicaciones basadas en LLM, Prompt Flow facilita el proceso y te permite construir aplicaciones LLM con calidad de producción.

## Estas son las características clave y los beneficios de usar Microsoft Prompt Flow:

**Experiencia de Autoría Interactiva**

Prompt Flow proporciona una representación visual de la estructura de tu flujo, lo que facilita la comprensión y navegación de tus proyectos.  
Ofrece una experiencia de codificación similar a un cuaderno para un desarrollo y depuración de flujos más eficiente.

**Variantes de Prompts y Ajustes**

Crea y compara múltiples variantes de prompts para facilitar un proceso iterativo de refinamiento. Evalúa el desempeño de diferentes prompts y elige los más efectivos.

**Flujos de Evaluación Integrados**

Evalúa la calidad y efectividad de tus prompts y flujos utilizando herramientas de evaluación integradas.  
Comprende qué tan bien están funcionando tus aplicaciones basadas en LLM.

**Recursos Integrales**

Prompt Flow incluye una biblioteca de herramientas, ejemplos y plantillas integradas. Estos recursos sirven como punto de partida para el desarrollo, inspiran creatividad y aceleran el proceso.

**Colaboración y Preparación Empresarial**

Facilita la colaboración en equipo permitiendo que múltiples usuarios trabajen juntos en proyectos de ingeniería de prompts.  
Mantén el control de versiones y comparte conocimientos de manera efectiva. Optimiza todo el proceso de ingeniería de prompts, desde el desarrollo y evaluación hasta la implementación y el monitoreo.

## Evaluación en Prompt Flow

En Microsoft Prompt Flow, la evaluación juega un papel crucial en la valoración del desempeño de tus modelos de IA. Exploremos cómo puedes personalizar flujos y métricas de evaluación dentro de Prompt Flow:

![PFVizualise](../../../../../translated_images/pfvisualize.93c453890f4088830217fa7308b1a589058ed499bbfff160c85676066b5cbf2d.es.png)

**Entendiendo la Evaluación en Prompt Flow**

En Prompt Flow, un flujo representa una secuencia de nodos que procesan entradas y generan salidas. Los flujos de evaluación son tipos especiales de flujos diseñados para evaluar el desempeño de una ejecución basada en criterios y objetivos específicos.

**Características clave de los flujos de evaluación**

Generalmente se ejecutan después del flujo que está siendo probado, utilizando sus salidas.  
Calculan puntuaciones o métricas para medir el desempeño del flujo probado. Las métricas pueden incluir precisión, puntuaciones de relevancia u otras medidas relevantes.

### Personalización de Flujos de Evaluación

**Definición de Entradas**

Los flujos de evaluación necesitan tomar las salidas de la ejecución que se está probando. Define las entradas de manera similar a los flujos estándar.  
Por ejemplo, si estás evaluando un flujo de preguntas y respuestas, nombra una entrada como "respuesta". Si estás evaluando un flujo de clasificación, nombra una entrada como "categoría". También podrían ser necesarias entradas de referencia (por ejemplo, etiquetas reales).

**Salidas y Métricas**

Los flujos de evaluación producen resultados que miden el desempeño del flujo probado. Las métricas pueden calcularse usando Python o LLM (Modelos de Lenguaje Extensos). Utiliza la función log_metric() para registrar métricas relevantes.

**Uso de Flujos de Evaluación Personalizados**

Desarrolla tu propio flujo de evaluación adaptado a tus tareas y objetivos específicos. Personaliza las métricas según tus metas de evaluación.  
Aplica este flujo de evaluación personalizado a ejecuciones por lotes para pruebas a gran escala.

## Métodos de Evaluación Integrados

Prompt Flow también ofrece métodos de evaluación integrados.  
Puedes enviar ejecuciones por lotes y usar estos métodos para evaluar qué tan bien funciona tu flujo con grandes conjuntos de datos.  
Visualiza los resultados de la evaluación, compara métricas e itera según sea necesario.  
Recuerda, la evaluación es esencial para garantizar que tus modelos de IA cumplan con los criterios y objetivos deseados. Consulta la documentación oficial para obtener instrucciones detalladas sobre cómo desarrollar y usar flujos de evaluación en Microsoft Prompt Flow.

En resumen, Microsoft Prompt Flow permite a los desarrolladores crear aplicaciones LLM de alta calidad al simplificar la ingeniería de prompts y proporcionar un entorno de desarrollo robusto. Si trabajas con LLMs, Prompt Flow es una herramienta valiosa que deberías explorar. Consulta los [Documentos de Evaluación de Prompt Flow](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo) para obtener instrucciones detalladas sobre cómo desarrollar y usar flujos de evaluación en Microsoft Prompt Flow.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.