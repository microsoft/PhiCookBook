<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-03-27T07:40:57+00:00",
  "source_file": "md\\01.Introduction\\03\\Local_Server_Inference.md",
  "language_code": "es"
}
-->
# **Inferencia de Phi-3 en Servidor Local**

Podemos desplegar Phi-3 en un servidor local. Los usuarios pueden optar por las soluciones de [Ollama](https://ollama.com) o [LM Studio](https://llamaedge.com), o escribir su propio código. Puedes conectar los servicios locales de Phi-3 a través de [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) o [Langchain](https://www.langchain.com/) para construir aplicaciones tipo Copilot.

## **Usar Semantic Kernel para acceder a Phi-3-mini**

En la aplicación Copilot, creamos aplicaciones utilizando Semantic Kernel / LangChain. Este tipo de marco de aplicaciones es generalmente compatible con Azure OpenAI Service / modelos de OpenAI, y también puede admitir modelos de código abierto en Hugging Face y modelos locales. ¿Qué debemos hacer si queremos usar Semantic Kernel para acceder a Phi-3-mini? Usando .NET como ejemplo, podemos combinarlo con el Conector de Hugging Face en Semantic Kernel. Por defecto, puede corresponder al id del modelo en Hugging Face (la primera vez que lo uses, el modelo se descargará desde Hugging Face, lo que toma bastante tiempo). También puedes conectarte al servicio local configurado. Comparando ambas opciones, recomendamos usar esta última porque ofrece un mayor grado de autonomía, especialmente en aplicaciones empresariales.

![sk](../../../../../translated_images/sk.c244b32f4811c6f0938b9e95b0b2f4b28105bff6495bdc3b24cd42b3e3e89bb9.es.png)

En la imagen se muestra cómo acceder a servicios locales mediante Semantic Kernel, lo que permite conectar fácilmente al servidor del modelo Phi-3-mini configurado por el usuario. Aquí está el resultado de ejecución:

![skrun](../../../../../translated_images/skrun.fb7a635a22ae8b7919d6e15c0eb27262526ed69728c5a1d2773a97d4562657c7.es.png)

***Código de ejemplo*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr la mayor precisión posible, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autoritaria. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.