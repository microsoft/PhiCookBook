## Escenarios de Ajuste Fino

![FineTuning with MS Services](../../../../translated_images/es/FinetuningwithMS.3d0cec8ae693e094.webp)

Esta sección ofrece una visión general de los escenarios de ajuste fino en los entornos Microsoft Foundry y Azure, incluidos los modelos de implementación, las capas de infraestructura y las técnicas de optimización comúnmente utilizadas.

**Plataforma**  
Esto incluye servicios gestionados como Microsoft Foundry (anteriormente Microsoft Foundry) y Azure Machine Learning, que proporcionan gestión de modelos, orquestación, seguimiento de experimentos y flujos de trabajo de implementación.

**Infraestructura**  
El ajuste fino requiere recursos de computación escalables. En entornos Azure, esto generalmente incluye máquinas virtuales basadas en GPU y recursos de CPU para cargas de trabajo ligeras, junto con almacenamiento escalable para conjuntos de datos y puntos de control.

**Herramientas y Framework**  
Los flujos de trabajo de ajuste fino comúnmente dependen de frameworks y bibliotecas de optimización como Hugging Face Transformers, DeepSpeed y PEFT (Fine-Tuning Eficiente en Parámetros).

El proceso de ajuste fino con tecnologías de Microsoft abarca servicios de plataforma, infraestructura de cómputo y frameworks de entrenamiento. Al comprender cómo estos componentes trabajan juntos, los desarrolladores pueden adaptar eficientemente modelos base a tareas específicas y escenarios de producción.

## Modelo como Servicio

Ajusta el modelo utilizando ajuste fino alojado, sin la necesidad de crear y gestionar cómputo.

![MaaS Fine Tuning](../../../../translated_images/es/MaaSfinetune.3eee4630607aff0d.webp)

El ajuste fino sin servidor ya está disponible para las familias de modelos Phi-3, Phi-3.5 y Phi-4, permitiendo a los desarrolladores personalizar rápida y fácilmente los modelos para escenarios en la nube y en el borde sin tener que gestionar cómputo.

## Modelo como Plataforma

Los usuarios gestionan su propio cómputo para ajustar fino sus modelos.

![Maap Fine Tuning](../../../../translated_images/es/MaaPFinetune.fd3829c1122f5d1c.webp)

[Ejemplo de Ajuste Fino](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Comparación de Técnicas de Ajuste Fino

|Escenario|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Adaptar LLMs preentrenados a tareas o dominios específicos|Sí|Sí|Sí|Sí|Sí|Sí|
|Ajuste fino para tareas de PLN como clasificación de texto, reconocimiento de entidades nombradas y traducción automática|Sí|Sí|Sí|Sí|Sí|Sí|
|Ajuste fino para tareas de preguntas y respuestas|Sí|Sí|Sí|Sí|Sí|Sí|
|Ajuste fino para generar respuestas humanas en chatbots|Sí|Sí|Sí|Sí|Sí|Sí|
|Ajuste fino para generar música, arte u otras formas de creatividad|Sí|Sí|Sí|Sí|Sí|Sí|
|Reducir costos computacionales y financieros|Sí|Sí|Sí|Sí|Sí|Sí|
|Reducir uso de memoria|Sí|Sí|Sí|Sí|Sí|Sí|
|Usar menos parámetros para un ajuste fino eficiente|Sí|Sí|Sí|No|No|Sí|
|Forma eficiente en memoria de paralelismo de datos que da acceso a la memoria GPU agregada de todos los dispositivos GPU disponibles|No|No|No|Sí|Sí|No|

> [!NOTE]
> LoRA, QLoRA, PEFT y DoRA son métodos de ajuste fino eficientes en parámetros, mientras que DeepSpeed y ZeRO se centran en entrenamiento distribuido y optimización de memoria.

## Ejemplos de Rendimiento de Ajuste Fino

![Finetuning Performance](../../../../translated_images/es/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por un humano. No nos hacemos responsables por malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->