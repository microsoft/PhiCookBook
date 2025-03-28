<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-03-27T07:53:10+00:00",
  "source_file": "md\\01.Introduction\\03\\overview.md",
  "language_code": "es"
}
-->
En el contexto de Phi-3-mini, la inferencia se refiere al proceso de utilizar el modelo para hacer predicciones o generar resultados basados en datos de entrada. Permíteme brindarte más detalles sobre Phi-3-mini y sus capacidades de inferencia.

Phi-3-mini forma parte de la serie de modelos Phi-3 lanzados por Microsoft. Estos modelos están diseñados para redefinir lo que es posible con Modelos de Lenguaje Pequeños (SLMs).

A continuación, algunos puntos clave sobre Phi-3-mini y sus capacidades de inferencia:

## **Descripción general de Phi-3-mini:**
- Phi-3-mini tiene un tamaño de parámetros de 3.8 mil millones.
- Puede ejecutarse no solo en dispositivos informáticos tradicionales, sino también en dispositivos de borde, como dispositivos móviles y dispositivos IoT.
- El lanzamiento de Phi-3-mini permite a individuos y empresas implementar SLMs en diferentes dispositivos de hardware, especialmente en entornos con recursos limitados.
- Admite varios formatos de modelo, incluyendo el formato tradicional de PyTorch, la versión cuantizada del formato gguf y la versión cuantizada basada en ONNX.

## **Acceso a Phi-3-mini:**
Para acceder a Phi-3-mini, puedes usar [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) en una aplicación Copilot. Semantic Kernel es generalmente compatible con Azure OpenAI Service, modelos de código abierto en Hugging Face y modelos locales.
También puedes usar [Ollama](https://ollama.com) o [LlamaEdge](https://llamaedge.com) para llamar a modelos cuantizados. Ollama permite a los usuarios individuales llamar a diferentes modelos cuantizados, mientras que LlamaEdge ofrece disponibilidad multiplataforma para modelos GGUF.

## **Modelos cuantizados:**
Muchos usuarios prefieren usar modelos cuantizados para inferencia local. Por ejemplo, puedes ejecutar directamente Ollama run Phi-3 o configurarlo sin conexión utilizando un Modelfile. El Modelfile especifica la ruta del archivo GGUF y el formato del prompt.

## **Posibilidades de la IA generativa:**
La combinación de SLMs como Phi-3-mini abre nuevas posibilidades para la IA generativa. La inferencia es solo el primer paso; estos modelos pueden usarse para diversas tareas en escenarios con limitaciones de recursos, latencia y costos.

## **Desbloqueando la IA generativa con Phi-3-mini: Una guía para la inferencia y el despliegue**  
Aprende a usar Semantic Kernel, Ollama/LlamaEdge y ONNX Runtime para acceder e inferir con los modelos Phi-3-mini, y explora las posibilidades de la IA generativa en diversos escenarios de aplicación.

**Características**
Inferencia del modelo phi3-mini en:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

En resumen, Phi-3-mini permite a los desarrolladores explorar diferentes formatos de modelos y aprovechar la IA generativa en diversos escenarios de aplicación.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables por malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.