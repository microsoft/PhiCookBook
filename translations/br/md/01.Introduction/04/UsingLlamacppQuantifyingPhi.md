<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-07-16T22:08:37+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "br"
}
-->
# **Quantizando a Família Phi usando llama.cpp**

## **O que é llama.cpp**

llama.cpp é uma biblioteca de software open-source escrita principalmente em C++ que realiza inferência em diversos Large Language Models (LLMs), como o Llama. Seu principal objetivo é oferecer desempenho de ponta para inferência de LLMs em uma ampla variedade de hardwares com configuração mínima. Além disso, existem bindings em Python disponíveis para essa biblioteca, que fornecem uma API de alto nível para completamento de texto e um servidor web compatível com OpenAI.

O objetivo principal do llama.cpp é permitir inferência de LLMs com configuração mínima e desempenho de ponta em diversos hardwares — localmente e na nuvem.

- Implementação pura em C/C++ sem dependências
- Apple silicon é tratado como prioridade — otimizado via ARM NEON, Accelerate e frameworks Metal
- Suporte a AVX, AVX2 e AVX512 para arquiteturas x86
- Quantização inteira de 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit e 8-bit para inferência mais rápida e menor uso de memória
- Kernels CUDA personalizados para rodar LLMs em GPUs NVIDIA (suporte a GPUs AMD via HIP)
- Suporte a backends Vulkan e SYCL
- Inferência híbrida CPU+GPU para acelerar parcialmente modelos maiores que a capacidade total de VRAM

## **Quantizando Phi-3.5 com llama.cpp**

O modelo Phi-3.5-Instruct pode ser quantizado usando llama.cpp, mas Phi-3.5-Vision e Phi-3.5-MoE ainda não são suportados. O formato convertido pelo llama.cpp é o gguf, que também é o formato de quantização mais amplamente utilizado.

Há uma grande quantidade de modelos quantizados no formato GGUF no Hugging Face. AI Foundry, Ollama e LlamaEdge dependem do llama.cpp, então modelos GGUF também são frequentemente usados.

### **O que é GGUF**

GGUF é um formato binário otimizado para carregamento e salvamento rápidos de modelos, tornando-o altamente eficiente para inferência. GGUF foi projetado para uso com GGML e outros executores. GGUF foi desenvolvido por @ggerganov, que também é o desenvolvedor do llama.cpp, um framework popular de inferência LLM em C/C++. Modelos inicialmente desenvolvidos em frameworks como PyTorch podem ser convertidos para o formato GGUF para uso nesses motores.

### **ONNX vs GGUF**

ONNX é um formato tradicional de machine learning/deep learning, bem suportado em diferentes frameworks de IA e com bons cenários de uso em dispositivos edge. Já o GGUF é baseado no llama.cpp e pode ser considerado um formato produzido na era GenAI. Ambos têm usos semelhantes. Se você busca melhor desempenho em hardware embarcado e camadas de aplicação, ONNX pode ser sua escolha. Se você utiliza o framework derivado e a tecnologia do llama.cpp, então GGUF pode ser mais adequado.

### **Quantização do Phi-3.5-Instruct usando llama.cpp**

**1. Configuração do Ambiente**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Quantização**

Usando llama.cpp para converter Phi-3.5-Instruct para FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Quantizando Phi-3.5 para INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testes**

Instale o llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Nota*** 

Se você usa Apple Silicon, por favor instale o llama-cpp-python assim


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testando 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Recursos**

1. Saiba mais sobre llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)  
2. Saiba mais sobre onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  
3. Saiba mais sobre GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.