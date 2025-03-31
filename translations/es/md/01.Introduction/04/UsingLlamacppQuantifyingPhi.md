<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e5bb9190ef9d149d28037a768c6b62b2",
  "translation_date": "2025-03-27T08:36:10+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingLlamacppQuantifyingPhi.md",
  "language_code": "es"
}
-->
# **Cuantificación de la familia Phi usando llama.cpp**

## **¿Qué es llama.cpp?**

llama.cpp es una biblioteca de software de código abierto escrita principalmente en C++ que realiza inferencias en varios Modelos de Lenguaje Extenso (LLMs), como Llama. Su objetivo principal es ofrecer un rendimiento de última generación para la inferencia de LLM en una amplia gama de hardware con una configuración mínima. Además, hay enlaces disponibles para Python que proporcionan una API de alto nivel para la generación de texto y un servidor web compatible con OpenAI.

El objetivo principal de llama.cpp es habilitar la inferencia de LLM con una configuración mínima y un rendimiento de última generación en una amplia variedad de hardware, tanto local como en la nube.

- Implementación sencilla en C/C++ sin dependencias
- Apple silicon como ciudadano de primera clase - optimizado mediante ARM NEON, Accelerate y Metal frameworks
- Soporte para AVX, AVX2 y AVX512 en arquitecturas x86
- Cuantización entera de 1.5 bits, 2 bits, 3 bits, 4 bits, 5 bits, 6 bits y 8 bits para una inferencia más rápida y menor uso de memoria
- Kernels personalizados CUDA para ejecutar LLMs en GPUs NVIDIA (soporte para GPUs AMD mediante HIP)
- Soporte para backend Vulkan y SYCL
- Inferencia híbrida CPU+GPU para acelerar parcialmente modelos más grandes que la capacidad total de VRAM

## **Cuantificación de Phi-3.5 con llama.cpp**

El modelo Phi-3.5-Instruct puede ser cuantificado usando llama.cpp, pero Phi-3.5-Vision y Phi-3.5-MoE aún no son compatibles. El formato convertido por llama.cpp es gguf, que también es el formato de cuantización más utilizado.

Hay una gran cantidad de modelos en formato GGUF cuantificados en Hugging Face. AI Foundry, Ollama y LlamaEdge dependen de llama.cpp, por lo que los modelos GGUF también se utilizan con frecuencia.

### **¿Qué es GGUF?**

GGUF es un formato binario optimizado para la carga y el guardado rápido de modelos, lo que lo hace altamente eficiente para fines de inferencia. GGUF está diseñado para su uso con GGML y otros ejecutores. GGUF fue desarrollado por @ggerganov, quien también es el creador de llama.cpp, un marco popular para la inferencia de LLM en C/C++. Los modelos desarrollados inicialmente en frameworks como PyTorch pueden convertirse al formato GGUF para ser utilizados con estos motores.

### **ONNX vs GGUF**

ONNX es un formato tradicional de aprendizaje automático/profundo que cuenta con buen soporte en diferentes frameworks de IA y tiene buenos casos de uso en dispositivos de borde. En cuanto a GGUF, está basado en llama.cpp y puede considerarse como producto de la era GenAI. Ambos tienen usos similares. Si buscas un mejor rendimiento en hardware integrado y capas de aplicación, ONNX puede ser tu elección. Si utilizas el framework derivado y la tecnología de llama.cpp, entonces GGUF puede ser más adecuado.

### **Cuantificación de Phi-3.5-Instruct usando llama.cpp**

**1. Configuración del entorno**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Cuantificación**

Usando llama.cpp para convertir Phi-3.5-Instruct a FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Cuantificación de Phi-3.5 a INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Pruebas**

Instalar llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Nota*** 

Si utilizas Apple Silicon, instala llama-cpp-python de esta manera


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Pruebas 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Recursos**

1. Aprende más sobre llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Aprende más sobre GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.