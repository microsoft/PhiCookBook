<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-05-07T14:31:58+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "mo"
}
-->
# **Inference Phi-3 en Android**

Exploremos cómo puedes realizar inferencias con Phi-3-mini en dispositivos Android. Phi-3-mini es una nueva serie de modelos de Microsoft que permite desplegar Modelos de Lenguaje Grande (LLMs) en dispositivos edge y dispositivos IoT.

## Semantic Kernel e Inferencia

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) es un marco de aplicaciones que te permite crear aplicaciones compatibles con Azure OpenAI Service, modelos OpenAI e incluso modelos locales. Si eres nuevo en Semantic Kernel, te recomendamos revisar el [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Para acceder a Phi-3-mini usando Semantic Kernel

Puedes combinarlo con el Hugging Face Connector en Semantic Kernel. Consulta este [Código de ejemplo](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Por defecto, corresponde al ID del modelo en Hugging Face. Sin embargo, también puedes conectarte a un servidor de modelo Phi-3-mini construido localmente.

### Llamando a modelos cuantificados con Ollama o LlamaEdge

Muchos usuarios prefieren usar modelos cuantificados para ejecutar modelos localmente. [Ollama](https://ollama.com/) y [LlamaEdge](https://llamaedge.com) permiten a usuarios individuales llamar a diferentes modelos cuantificados:

#### Ollama

Puedes ejecutarlo directamente con `ollama run Phi-3` o configurarlo sin conexión creando un `Modelfile` con la ruta a tu archivo `.gguf`.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Código de ejemplo](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Si deseas usar archivos `.gguf` en la nube y en dispositivos edge al mismo tiempo, LlamaEdge es una excelente opción. Puedes consultar este [código de ejemplo](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) para comenzar.

### Instalar y ejecutar en teléfonos Android

1. **Descarga la app MLC Chat** (Gratis) para teléfonos Android.  
2. Descarga el archivo APK (148MB) e instálalo en tu dispositivo.  
3. Abre la app MLC Chat. Verás una lista de modelos de IA, incluyendo Phi-3-mini.

En resumen, Phi-3-mini abre posibilidades emocionantes para la IA generativa en dispositivos edge, y puedes comenzar a explorar sus capacidades en Android.

**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.

---

(Note: "mo" is not a recognized language code or language name in common language databases. Could you please clarify what language "mo" refers to?)