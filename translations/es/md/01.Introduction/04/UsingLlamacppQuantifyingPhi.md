# **Cuantificación de la familia Phi usando llama.cpp**

## **Qué es llama.cpp**

llama.cpp es una biblioteca de software de código abierto escrita principalmente en C++ que realiza inferencias en varios Modelos de Lenguaje Grande (LLMs), como Llama. Su objetivo principal es ofrecer un rendimiento de última generación para la inferencia de LLM en una amplia variedad de hardware con una configuración mínima. Además, existen enlaces en Python para esta biblioteca, que proporcionan una API de alto nivel para la finalización de texto y un servidor web compatible con OpenAI.

El objetivo principal de llama.cpp es permitir la inferencia de LLM con una configuración mínima y un rendimiento de vanguardia en una gran variedad de hardware, tanto localmente como en la nube.

- Implementación pura en C/C++ sin dependencias
- Apple silicon es una prioridad - optimizado mediante ARM NEON, Accelerate y frameworks Metal
- Soporte para AVX, AVX2 y AVX512 en arquitecturas x86
- Cuantificación entera de 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit y 8-bit para inferencias más rápidas y menor uso de memoria
- Kernels CUDA personalizados para ejecutar LLMs en GPUs NVIDIA (soporte para GPUs AMD vía HIP)
- Soporte para backend Vulkan y SYCL
- Inferencia híbrida CPU+GPU para acelerar parcialmente modelos más grandes que la capacidad total de VRAM

## **Cuantificación de Phi-3.5 con llama.cpp**

El modelo Phi-3.5-Instruct puede ser cuantificado usando llama.cpp, pero Phi-3.5-Vision y Phi-3.5-MoE aún no son compatibles. El formato convertido por llama.cpp es gguf, que también es el formato de cuantificación más utilizado.

Hay una gran cantidad de modelos cuantificados en formato GGUF en Hugging Face. AI Foundry, Ollama y LlamaEdge dependen de llama.cpp, por lo que los modelos GGUF también se usan con frecuencia.

### **Qué es GGUF**

GGUF es un formato binario optimizado para la carga y guardado rápido de modelos, lo que lo hace muy eficiente para propósitos de inferencia. GGUF está diseñado para usarse con GGML y otros ejecutores. GGUF fue desarrollado por @ggerganov, quien también es el desarrollador de llama.cpp, un popular framework de inferencia LLM en C/C++. Los modelos inicialmente desarrollados en frameworks como PyTorch pueden convertirse al formato GGUF para usarse con esos motores.

### **ONNX vs GGUF**

ONNX es un formato tradicional de machine learning/deep learning, bien soportado en diferentes frameworks de IA y con buenos casos de uso en dispositivos edge. En cuanto a GGUF, está basado en llama.cpp y puede considerarse un formato surgido en la era GenAI. Ambos tienen usos similares. Si buscas mejor rendimiento en hardware embebido y capas de aplicación, ONNX puede ser tu elección. Si usas el framework derivado y la tecnología de llama.cpp, entonces GGUF puede ser mejor.

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

Cuantificando Phi-3.5 a INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Pruebas**

Instalar llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Nota*** 

Si usas Apple Silicon, por favor instala llama-cpp-python de esta forma


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Pruebas


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Recursos**

1. Aprende más sobre llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)  
2. Aprende más sobre onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  
3. Aprende más sobre GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.