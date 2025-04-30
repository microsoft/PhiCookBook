<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-03-27T07:05:09+00:00",
  "source_file": "md\\01.Introduction\\03\\Android_Inference.md",
  "language_code": "es"
}
-->
# **Inferencia Phi-3 en Android**

Exploremos cómo puedes realizar inferencias con Phi-3-mini en dispositivos Android. Phi-3-mini es una nueva serie de modelos de Microsoft que permite el despliegue de Modelos de Lenguaje Extensos (LLMs) en dispositivos edge y dispositivos IoT.

## Semantic Kernel e Inferencia

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) es un marco de aplicación que te permite crear aplicaciones compatibles con Azure OpenAI Service, modelos de OpenAI e incluso modelos locales. Si eres nuevo en Semantic Kernel, te sugerimos que consultes el [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Acceder a Phi-3-mini Usando Semantic Kernel

Puedes combinarlo con el conector de Hugging Face en Semantic Kernel. Consulta este [Código de Ejemplo](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Por defecto, corresponde al ID del modelo en Hugging Face. Sin embargo, también puedes conectarte a un servidor de modelo Phi-3-mini construido localmente.

### Llamar a Modelos Cuantizados con Ollama o LlamaEdge

Muchos usuarios prefieren usar modelos cuantizados para ejecutar modelos de forma local. [Ollama](https://ollama.com/) y [LlamaEdge](https://llamaedge.com) permiten a los usuarios individuales llamar a diferentes modelos cuantizados:

#### Ollama

Puedes ejecutar directamente `ollama run Phi-3` o configurarlo offline creando un `Modelfile` con la ruta a tu archivo `.gguf`.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Código de Ejemplo](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Si deseas usar archivos `.gguf` en la nube y en dispositivos edge simultáneamente, LlamaEdge es una excelente opción. Puedes consultar este [código de ejemplo](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) para comenzar.

### Instalar y Ejecutar en Teléfonos Android

1. **Descarga la aplicación MLC Chat** (gratuita) para teléfonos Android.
2. Descarga el archivo APK (148MB) e instálalo en tu dispositivo.
3. Abre la aplicación MLC Chat. Verás una lista de modelos de IA, incluyendo Phi-3-mini.

En resumen, Phi-3-mini abre emocionantes posibilidades para la IA generativa en dispositivos edge, y puedes comenzar a explorar sus capacidades en Android.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.