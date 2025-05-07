<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-07T10:43:19+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "es"
}
-->
En el contexto de Phi-3-mini, la inferencia se refiere al proceso de usar el modelo para hacer predicciones o generar resultados basados en datos de entrada. Permíteme darte más detalles sobre Phi-3-mini y sus capacidades de inferencia.

Phi-3-mini es parte de la serie Phi-3 de modelos lanzados por Microsoft. Estos modelos están diseñados para redefinir lo que es posible con los Small Language Models (SLMs).

Aquí algunos puntos clave sobre Phi-3-mini y sus capacidades de inferencia:

## **Resumen de Phi-3-mini:**
- Phi-3-mini tiene un tamaño de parámetro de 3.8 mil millones.
- Puede ejecutarse no solo en dispositivos informáticos tradicionales, sino también en dispositivos edge como móviles y dispositivos IoT.
- El lanzamiento de Phi-3-mini permite a individuos y empresas desplegar SLMs en diferentes dispositivos de hardware, especialmente en entornos con recursos limitados.
- Cubre varios formatos de modelo, incluyendo el formato tradicional PyTorch, la versión cuantificada del formato gguf y la versión cuantificada basada en ONNX.

## **Acceso a Phi-3-mini:**
Para acceder a Phi-3-mini, puedes usar [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) en una aplicación Copilot. Semantic Kernel es generalmente compatible con Azure OpenAI Service, modelos open-source en Hugging Face y modelos locales.  
También puedes usar [Ollama](https://ollama.com) o [LlamaEdge](https://llamaedge.com) para llamar a modelos cuantificados. Ollama permite a usuarios individuales llamar a diferentes modelos cuantificados, mientras que LlamaEdge ofrece disponibilidad multiplataforma para modelos GGUF.

## **Modelos Cuantificados:**
Muchos usuarios prefieren usar modelos cuantificados para inferencia local. Por ejemplo, puedes ejecutar Ollama directamente con Phi-3 o configurarlo sin conexión usando un Modelfile. El Modelfile especifica la ruta del archivo GGUF y el formato del prompt.

## **Posibilidades de IA Generativa:**
Combinar SLMs como Phi-3-mini abre nuevas posibilidades para la IA generativa. La inferencia es solo el primer paso; estos modelos pueden usarse para diversas tareas en escenarios con recursos limitados, restricciones de latencia y costos ajustados.

## **Desbloqueando la IA Generativa con Phi-3-mini: Guía para Inferencia y Despliegue**  
Aprende cómo usar Semantic Kernel, Ollama/LlamaEdge y ONNX Runtime para acceder e inferir modelos Phi-3-mini, y explora las posibilidades de la IA generativa en varios escenarios de aplicación.

**Características**  
Inferencia del modelo phi3-mini en:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

En resumen, Phi-3-mini permite a los desarrolladores explorar diferentes formatos de modelo y aprovechar la IA generativa en diversos escenarios de aplicación.

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.