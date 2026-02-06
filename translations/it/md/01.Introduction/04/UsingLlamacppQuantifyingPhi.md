# **Quantizzazione della famiglia Phi usando llama.cpp**

## **Cos'è llama.cpp**

llama.cpp è una libreria software open-source scritta principalmente in C++ che esegue l'inferenza su vari Large Language Models (LLM), come Llama. Il suo obiettivo principale è fornire prestazioni all'avanguardia per l'inferenza di LLM su una vasta gamma di hardware con una configurazione minima. Inoltre, sono disponibili binding Python per questa libreria, che offrono un'API di alto livello per il completamento del testo e un server web compatibile con OpenAI.

L'obiettivo principale di llama.cpp è permettere l'inferenza di LLM con configurazione minima e prestazioni di alto livello su una grande varietà di hardware - sia in locale che nel cloud.

- Implementazione pura in C/C++ senza dipendenze
- Apple silicon è supportato come prima scelta - ottimizzato tramite ARM NEON, Accelerate e Metal frameworks
- Supporto AVX, AVX2 e AVX512 per architetture x86
- Quantizzazione intera a 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit e 8-bit per inferenze più veloci e minor uso di memoria
- Kernel CUDA personalizzati per eseguire LLM su GPU NVIDIA (supporto per GPU AMD tramite HIP)
- Supporto backend Vulkan e SYCL
- Inferenza ibrida CPU+GPU per accelerare parzialmente modelli più grandi della capacità totale di VRAM

## **Quantizzazione di Phi-3.5 con llama.cpp**

Il modello Phi-3.5-Instruct può essere quantizzato usando llama.cpp, mentre Phi-3.5-Vision e Phi-3.5-MoE non sono ancora supportati. Il formato convertito da llama.cpp è gguf, che è anche il formato di quantizzazione più diffuso.

Su Hugging Face esistono molti modelli quantizzati in formato GGUF. AI Foundry, Ollama e LlamaEdge si basano su llama.cpp, quindi i modelli GGUF sono spesso utilizzati.

### **Cos’è GGUF**

GGUF è un formato binario ottimizzato per il caricamento e il salvataggio rapido dei modelli, rendendolo molto efficiente per l’inferenza. GGUF è progettato per l’uso con GGML e altri executor. GGUF è stato sviluppato da @ggerganov, che è anche lo sviluppatore di llama.cpp, un popolare framework C/C++ per l’inferenza di LLM. I modelli inizialmente sviluppati in framework come PyTorch possono essere convertiti in formato GGUF per l’uso con questi motori.

### **ONNX vs GGUF**

ONNX è un formato tradizionale per machine learning/deep learning, ben supportato in diversi framework AI e con buoni scenari d’uso su dispositivi edge. GGUF, invece, si basa su llama.cpp e può essere considerato un prodotto dell’era GenAI. I due hanno usi simili. Se cerchi migliori prestazioni su hardware embedded e a livello applicativo, ONNX potrebbe essere la scelta giusta. Se usi framework e tecnologie derivate da llama.cpp, allora GGUF potrebbe essere preferibile.

### **Quantizzazione di Phi-3.5-Instruct usando llama.cpp**

**1. Configurazione dell’ambiente**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Quantizzazione**

Convertire Phi-3.5-Instruct in FP16 GGUF usando llama.cpp


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Quantizzazione di Phi-3.5 a INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Test**

Installare llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Nota*** 

Se usi Apple Silicon, installa llama-cpp-python in questo modo


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Test


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Risorse**

1. Per saperne di più su llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)  
2. Per saperne di più su onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  
3. Per saperne di più su GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.