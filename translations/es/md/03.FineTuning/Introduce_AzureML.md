<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7fe541373802e33568e94e13226d463c",
  "translation_date": "2025-07-17T09:33:12+00:00",
  "source_file": "md/03.FineTuning/Introduce_AzureML.md",
  "language_code": "es"
}
-->
# **Introducción al Servicio de Azure Machine Learning**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo) es un servicio en la nube para acelerar y gestionar el ciclo de vida de proyectos de aprendizaje automático (ML).

Los profesionales de ML, científicos de datos e ingenieros pueden usarlo en sus flujos de trabajo diarios para:

- Entrenar y desplegar modelos.  
Gestionar operaciones de aprendizaje automático (MLOps).  
- Puedes crear un modelo en Azure Machine Learning o usar un modelo desarrollado en una plataforma de código abierto, como PyTorch, TensorFlow o scikit-learn.  
- Las herramientas de MLOps te ayudan a monitorear, reentrenar y volver a desplegar modelos.

## ¿Para quién es Azure Machine Learning?

**Científicos de Datos e Ingenieros de ML**

Pueden usar herramientas para acelerar y automatizar sus flujos de trabajo diarios.  
Azure ML ofrece funcionalidades para equidad, explicabilidad, seguimiento y auditoría.

**Desarrolladores de Aplicaciones:**  
Pueden integrar modelos en aplicaciones o servicios de forma sencilla.

**Desarrolladores de Plataforma**

Tienen acceso a un conjunto robusto de herramientas respaldadas por APIs duraderas de Azure Resource Manager.  
Estas herramientas permiten construir soluciones avanzadas de ML.

**Empresas**

Al trabajar en la nube de Microsoft Azure, las empresas se benefician de la seguridad conocida y el control de acceso basado en roles.  
Configuran proyectos para controlar el acceso a datos protegidos y operaciones específicas.

## Productividad para Todo el Equipo  
Los proyectos de ML suelen requerir un equipo con habilidades variadas para construir y mantener.

Azure ML ofrece herramientas que te permiten:  
- Colaborar con tu equipo mediante notebooks compartidos, recursos de cómputo, cómputo sin servidor, datos y entornos.  
- Desarrollar modelos con equidad, explicabilidad, seguimiento y auditoría para cumplir con requisitos de trazabilidad y cumplimiento.  
- Desplegar modelos de ML rápida y fácilmente a escala, y gestionarlos eficientemente con MLOps.  
- Ejecutar cargas de trabajo de aprendizaje automático en cualquier lugar con gobernanza, seguridad y cumplimiento integrados.

## Herramientas de Plataforma Compatibles

Cualquier miembro del equipo de ML puede usar sus herramientas preferidas para realizar el trabajo.  
Ya sea que estés ejecutando experimentos rápidos, ajustando hiperparámetros, construyendo pipelines o gestionando inferencias, puedes usar interfaces familiares como:  
- Azure Machine Learning Studio  
- Python SDK (v2)  
- Azure CLI (v2)  
- Azure Resource Manager REST APIs

A medida que refinas modelos y colaboras durante el ciclo de desarrollo, puedes compartir y encontrar activos, recursos y métricas dentro de la interfaz de Azure Machine Learning studio.

## **LLM/SLM en Azure ML**

Azure ML ha incorporado muchas funciones relacionadas con LLM/SLM, combinando LLMOps y SLMOps para crear una plataforma tecnológica de inteligencia artificial generativa a nivel empresarial.

### **Catálogo de Modelos**

Los usuarios empresariales pueden desplegar diferentes modelos según distintos escenarios de negocio a través del Catálogo de Modelos, y ofrecer servicios como Modelo como Servicio para que desarrolladores o usuarios empresariales accedan.

![models](../../../../translated_images/es/models.e6c7ff50a51806fd.png)

El Catálogo de Modelos en Azure Machine Learning studio es el centro para descubrir y usar una amplia variedad de modelos que te permiten construir aplicaciones de IA Generativa. El catálogo incluye cientos de modelos de proveedores como Azure OpenAI service, Mistral, Meta, Cohere, Nvidia, Hugging Face, incluyendo modelos entrenados por Microsoft. Los modelos de proveedores distintos a Microsoft son Productos No Microsoft, según lo definido en los Términos de Producto de Microsoft, y están sujetos a los términos proporcionados con el modelo.

### **Pipeline de Trabajo**

El núcleo de un pipeline de aprendizaje automático es dividir una tarea completa de ML en un flujo de trabajo de múltiples pasos. Cada paso es un componente manejable que puede desarrollarse, optimizarse, configurarse y automatizarse individualmente. Los pasos están conectados mediante interfaces bien definidas. El servicio de pipelines de Azure Machine Learning orquesta automáticamente todas las dependencias entre los pasos.

En el ajuste fino de SLM / LLM, podemos gestionar nuestros datos, entrenamiento y procesos de generación a través del Pipeline.

![finetuning](../../../../translated_images/es/finetuning.6559da198851fa52.png)

### **Prompt flow**

Beneficios de usar Azure Machine Learning prompt flow  
Azure Machine Learning prompt flow ofrece una serie de beneficios que ayudan a los usuarios a pasar de la ideación a la experimentación y, finalmente, a aplicaciones basadas en LLM listas para producción:

**Agilidad en la ingeniería de prompts**

Experiencia interactiva de autoría: Azure Machine Learning prompt flow proporciona una representación visual de la estructura del flujo, permitiendo a los usuarios entender y navegar fácilmente sus proyectos. También ofrece una experiencia de codificación tipo notebook para un desarrollo y depuración eficientes.  
Variantes para ajuste de prompts: Los usuarios pueden crear y comparar múltiples variantes de prompts, facilitando un proceso iterativo de refinamiento.

Evaluación: Los flujos de evaluación integrados permiten a los usuarios valorar la calidad y efectividad de sus prompts y flujos.

Recursos completos: Azure Machine Learning prompt flow incluye una biblioteca de herramientas, ejemplos y plantillas integradas que sirven como punto de partida para el desarrollo, inspirando creatividad y acelerando el proceso.

**Preparación empresarial para aplicaciones basadas en LLM**

Colaboración: Azure Machine Learning prompt flow soporta la colaboración en equipo, permitiendo que varios usuarios trabajen juntos en proyectos de ingeniería de prompts, compartan conocimientos y mantengan control de versiones.

Plataforma todo en uno: Azure Machine Learning prompt flow simplifica todo el proceso de ingeniería de prompts, desde el desarrollo y evaluación hasta el despliegue y monitoreo. Los usuarios pueden desplegar fácilmente sus flujos como endpoints de Azure Machine Learning y monitorear su rendimiento en tiempo real, asegurando una operación óptima y mejora continua.

Soluciones de preparación empresarial de Azure Machine Learning: Prompt flow aprovecha las robustas soluciones de preparación empresarial de Azure Machine Learning, proporcionando una base segura, escalable y confiable para el desarrollo, experimentación y despliegue de flujos.

Con Azure Machine Learning prompt flow, los usuarios pueden liberar su agilidad en ingeniería de prompts, colaborar eficazmente y aprovechar soluciones de nivel empresarial para el desarrollo y despliegue exitoso de aplicaciones basadas en LLM.

Combinando la potencia de cómputo, datos y diferentes componentes de Azure ML, los desarrolladores empresariales pueden construir fácilmente sus propias aplicaciones de inteligencia artificial.

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.