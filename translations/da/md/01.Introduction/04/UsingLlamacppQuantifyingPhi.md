<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-07-16T22:09:52+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "da"
}
-->
# **Kvantisering af Phi-familien ved brug af llama.cpp**

## **Hvad er llama.cpp**

llama.cpp er et open source softwarebibliotek, primært skrevet i C++, som udfører inferens på forskellige Large Language Models (LLMs), såsom Llama. Det primære mål er at levere state-of-the-art ydeevne til LLM-inferens på en bred vifte af hardware med minimal opsætning. Derudover findes der Python-bindings til dette bibliotek, som tilbyder et højniveau-API til tekstkomplettering samt en OpenAI-kompatibel webserver.

Hovedformålet med llama.cpp er at muliggøre LLM-inferens med minimal opsætning og toppræstation på mange forskellige hardwareplatforme – både lokalt og i skyen.

- Ren C/C++-implementering uden afhængigheder  
- Apple silicon understøttes fuldt ud – optimeret via ARM NEON, Accelerate og Metal frameworks  
- AVX, AVX2 og AVX512 support til x86-arkitekturer  
- 1,5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit og 8-bit heltalskvantisering for hurtigere inferens og reduceret hukommelsesforbrug  
- Specialbyggede CUDA-kernels til kørsel af LLMs på NVIDIA GPU’er (understøttelse af AMD GPU’er via HIP)  
- Vulkan- og SYCL-backend support  
- CPU+GPU hybrid inferens for delvist at accelerere modeller, der er større end den samlede VRAM-kapacitet  

## **Kvantisering af Phi-3.5 med llama.cpp**

Phi-3.5-Instruct modellen kan kvantiseres ved hjælp af llama.cpp, men Phi-3.5-Vision og Phi-3.5-MoE understøttes endnu ikke. Det format, som llama.cpp konverterer til, er gguf, som også er det mest udbredte kvantiseringsformat.

Der findes et stort antal kvantiserede GGUF-formatmodeller på Hugging Face. AI Foundry, Ollama og LlamaEdge benytter llama.cpp, så GGUF-modeller anvendes også ofte.

### **Hvad er GGUF**

GGUF er et binært format, optimeret til hurtig indlæsning og lagring af modeller, hvilket gør det meget effektivt til inferens. GGUF er designet til brug med GGML og andre eksekveringsmotorer. GGUF blev udviklet af @ggerganov, som også er udvikleren af llama.cpp, et populært C/C++ LLM-inferensframework. Modeller, der oprindeligt er udviklet i frameworks som PyTorch, kan konverteres til GGUF-format til brug med disse motorer.

### **ONNX vs GGUF**

ONNX er et traditionelt maskinlærings-/dybdelæringsformat, som er godt understøttet i forskellige AI-frameworks og har gode anvendelsesscenarier på edge-enheder. GGUF er derimod baseret på llama.cpp og kan siges at være skabt i GenAI-æraen. De to har lignende anvendelser. Hvis du ønsker bedre ydeevne på indlejret hardware og applikationslag, kan ONNX være dit valg. Hvis du bruger afledte frameworks og teknologier fra llama.cpp, kan GGUF være bedre.

### **Kvantisering af Phi-3.5-Instruct med llama.cpp**

**1. Miljøopsætning**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantisering**

Konverter Phi-3.5-Instruct til FP16 GGUF med llama.cpp


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Kvantisering af Phi-3.5 til INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Test**

Installer llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Note*** 

Hvis du bruger Apple Silicon, skal du installere llama-cpp-python på denne måde


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testning 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Ressourcer**

1. Lær mere om llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)  
2. Lær mere om onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  
3. Lær mere om GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.