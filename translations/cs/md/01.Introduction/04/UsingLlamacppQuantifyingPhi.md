<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-09T14:17:25+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "cs"
}
-->
# **Quantizando la familia Phi usando llama.cpp**

## **Qué es llama.cpp**

llama.cpp es una biblioteca de software de código abierto escrita principalmente en C++ que realiza inferencia en varios Modelos de Lenguaje Grande (LLMs), como Llama. Su objetivo principal es ofrecer un rendimiento de última generación para la inferencia de LLM en una amplia variedad de hardware con una configuración mínima. Además, existen enlaces en Python para esta biblioteca, que proporcionan una API de alto nivel para la finalización de texto y un servidor web compatible con OpenAI.

El objetivo principal de llama.cpp es permitir la inferencia de LLM con una configuración mínima y un rendimiento de vanguardia en una gran variedad de hardware, tanto localmente como en la nube.

- Implementación pura en C/C++ sin dependencias
- Apple silicon es un ciudadano de primera clase: optimizado mediante ARM NEON, Accelerate y frameworks Metal
- Soporte AVX, AVX2 y AVX512 para arquitecturas x86
- Cuantización entera de 1.5, 2, 3, 4, 5, 6 y 8 bits para acelerar la inferencia y reducir el uso de memoria
- Kernels CUDA personalizados para ejecutar LLMs en GPUs NVIDIA (soporte para GPUs AMD mediante HIP)
- Soporte para backends Vulkan y SYCL
- Inferencia híbrida CPU+GPU para acelerar parcialmente modelos más grandes que la capacidad total de VRAM

## **Cuantizando Phi-3.5 con llama.cpp**

El modelo Phi-3.5-Instruct puede ser cuantizado usando llama.cpp, pero Phi-3.5-Vision y Phi-3.5-MoE aún no están soportados. El formato convertido por llama.cpp es gguf, que también es el formato de cuantización más utilizado.

Existen muchos modelos cuantizados en formato GGUF en Hugging Face. AI Foundry, Ollama y LlamaEdge dependen de llama.cpp, por lo que los modelos GGUF también son frecuentemente usados.

### **Qué es GGUF**

GGUF es un formato binario optimizado para la carga y guardado rápidos de modelos, haciéndolo muy eficiente para propósitos de inferencia. GGUF está diseñado para usarse con GGML y otros ejecutores. GGUF fue desarrollado por @ggerganov, quien también es el desarrollador de llama.cpp, un popular framework de inferencia LLM en C/C++. Los modelos inicialmente desarrollados en frameworks como PyTorch pueden convertirse al formato GGUF para usarse con estos motores.

### **ONNX vs GGUF**

ONNX es un formato tradicional de machine learning/deep learning, bien soportado en diferentes frameworks de IA y con buenos casos de uso en dispositivos edge. En cuanto a GGUF, está basado en llama.cpp y se puede decir que fue creado en la era GenAI. Ambos tienen usos similares. Si buscas mejor rendimiento en hardware embebido y capas de aplicación, ONNX puede ser tu elección. Si usas el framework derivado y tecnología de llama.cpp, entonces GGUF puede ser mejor.

### **Cuantización de Phi-3.5-Instruct usando llama.cpp**

**1. Configuración del entorno**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Cuantización**

Usando llama.cpp convierte Phi-3.5-Instruct a FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Cuantizando Phi-3.5 a INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Pruebas**

Instala llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Nota*** 

Si usas Apple Silicon, instala llama-cpp-python así


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

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo chybné výklady vzniklé použitím tohoto překladu.