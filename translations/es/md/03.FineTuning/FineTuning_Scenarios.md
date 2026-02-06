## Escenarios de Fine Tuning

![FineTuning con Servicios MS](../../../../translated_images/es/FinetuningwithMS.3d0cec8ae693e094.webp)

**Plataforma** Esto incluye diversas tecnologías como Azure AI Foundry, Azure Machine Learning, AI Tools, Kaito y ONNX Runtime.

**Infraestructura** Esto incluye la CPU y FPGA, que son esenciales para el proceso de fine-tuning. Permíteme mostrarte los íconos de cada una de estas tecnologías.

**Herramientas y Framework** Esto incluye ONNX Runtime y ONNX Runtime. Permíteme mostrarte los íconos de cada una de estas tecnologías.  
[Insertar íconos para ONNX Runtime y ONNX Runtime]

El proceso de fine-tuning con tecnologías de Microsoft involucra varios componentes y herramientas. Al comprender y utilizar estas tecnologías, podemos ajustar eficazmente nuestras aplicaciones y crear mejores soluciones.

## Modelo como Servicio

Ajusta el modelo usando fine-tuning alojado, sin necesidad de crear y administrar cómputo.

![MaaS Fine Tuning](../../../../translated_images/es/MaaSfinetune.3eee4630607aff0d.webp)

El fine-tuning serverless está disponible para los modelos Phi-3-mini y Phi-3-medium, permitiendo a los desarrolladores personalizar rápida y fácilmente los modelos para escenarios en la nube y en el edge sin tener que gestionar cómputo. También hemos anunciado que Phi-3-small ya está disponible a través de nuestra oferta Models-as-a-Service, para que los desarrolladores puedan comenzar rápidamente con el desarrollo de IA sin tener que administrar la infraestructura subyacente.

## Modelo como Plataforma

Los usuarios gestionan su propio cómputo para poder ajustar sus modelos.

![Maap Fine Tuning](../../../../translated_images/es/MaaPFinetune.fd3829c1122f5d1c.webp)

[Ejemplo de Fine Tuning](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Escenarios de Fine Tuning

| | | | | | | |
|-|-|-|-|-|-|-|
|Escenario|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|Adaptar LLMs preentrenados a tareas o dominios específicos|Sí|Sí|Sí|Sí|Sí|Sí|
|Fine-tuning para tareas de PLN como clasificación de texto, reconocimiento de entidades nombradas y traducción automática|Sí|Sí|Sí|Sí|Sí|Sí|
|Fine-tuning para tareas de QA|Sí|Sí|Sí|Sí|Sí|Sí|
|Fine-tuning para generar respuestas humanas en chatbots|Sí|Sí|Sí|Sí|Sí|Sí|
|Fine-tuning para generar música, arte u otras formas de creatividad|Sí|Sí|Sí|Sí|Sí|Sí|
|Reducir costos computacionales y financieros|Sí|Sí|No|Sí|Sí|No|
|Reducir uso de memoria|No|Sí|No|Sí|Sí|Sí|
|Usar menos parámetros para un fine-tuning eficiente|No|Sí|Sí|No|No|Sí|
|Forma eficiente en memoria de paralelismo de datos que da acceso a la memoria GPU agregada de todos los dispositivos GPU disponibles|No|No|No|Sí|Sí|Sí|

## Ejemplos de Rendimiento en Fine Tuning

![Rendimiento de Fine Tuning](../../../../translated_images/es/Finetuningexamples.a9a41214f8f5afc1.webp)

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.