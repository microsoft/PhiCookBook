<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-03-27T11:10:11+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\UsingPromptFlowWithONNX.md",
  "language_code": "es"
}
-->
# Usar GPU de Windows para crear una solución Prompt flow con Phi-3.5-Instruct ONNX

El siguiente documento es un ejemplo de cómo usar PromptFlow con ONNX (Open Neural Network Exchange) para desarrollar aplicaciones de IA basadas en modelos Phi-3.

PromptFlow es un conjunto de herramientas de desarrollo diseñadas para simplificar el ciclo completo de desarrollo de aplicaciones de IA basadas en LLM (Modelos de Lenguaje Grande), desde la idea y el prototipo hasta las pruebas y la evaluación.

Al integrar PromptFlow con ONNX, los desarrolladores pueden:

- **Optimizar el rendimiento del modelo**: Aprovechar ONNX para una inferencia y despliegue eficientes del modelo.
- **Simplificar el desarrollo**: Utilizar PromptFlow para gestionar el flujo de trabajo y automatizar tareas repetitivas.
- **Mejorar la colaboración**: Facilitar una mejor colaboración entre los miembros del equipo al proporcionar un entorno de desarrollo unificado.

**Prompt flow** es un conjunto de herramientas de desarrollo diseñadas para simplificar el ciclo completo de desarrollo de aplicaciones de IA basadas en LLM, desde la ideación, el prototipado, las pruebas, la evaluación, hasta el despliegue en producción y el monitoreo. Hace que la ingeniería de prompts sea mucho más sencilla y permite construir aplicaciones de LLM con calidad de producción.

Prompt flow puede conectarse a OpenAI, Azure OpenAI Service y modelos personalizables (Huggingface, LLM/SLM locales). Esperamos implementar el modelo ONNX cuantificado de Phi-3.5 en aplicaciones locales. Prompt flow puede ayudarnos a planificar mejor nuestro negocio y completar soluciones locales basadas en Phi-3.5. En este ejemplo, combinaremos la biblioteca GenAI de ONNX Runtime para completar la solución Prompt flow basada en GPU de Windows.

## **Instalación**

### **ONNX Runtime GenAI para GPU de Windows**

Lee esta guía para configurar ONNX Runtime GenAI para GPU de Windows [haz clic aquí](./ORTWindowGPUGuideline.md)

### **Configurar Prompt flow en VSCode**

1. Instalar la extensión de Prompt flow para VS Code

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.es.png)

2. Después de instalar la extensión de Prompt flow para VS Code, haz clic en la extensión y selecciona **Installation dependencies**. Sigue esta guía para instalar el SDK de Prompt flow en tu entorno.

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.es.png)

3. Descarga [Código de ejemplo](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) y usa VS Code para abrir este ejemplo.

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.es.png)

4. Abre **flow.dag.yaml** para seleccionar tu entorno de Python.

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.es.png)

   Abre **chat_phi3_ort.py** para cambiar la ubicación de tu modelo Phi-3.5-instruct ONNX.

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.es.png)

5. Ejecuta tu Prompt flow para realizar pruebas.

Abre **flow.dag.yaml** y haz clic en el editor visual.

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.es.png)

Después de hacer clic en esto, ejecútalo para probar.

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.es.png)

1. Puedes ejecutar un lote en el terminal para verificar más resultados.

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Puedes verificar los resultados en tu navegador predeterminado.

![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.es.png)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables por malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.