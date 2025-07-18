<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-07-16T22:09:41+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "sv"
}
-->
# **Kvantisering av Phi-familjen med llama.cpp**

## **Vad är llama.cpp**

llama.cpp är ett open-source mjukvarubibliotek främst skrivet i C++ som utför inferens på olika stora språkmodeller (LLMs), såsom Llama. Dess huvudsakliga mål är att erbjuda toppmodern prestanda för LLM-inferens på en mängd olika hårdvaror med minimal konfiguration. Dessutom finns Python-bindningar för detta bibliotek, som erbjuder ett högre API för textkomplettering och en OpenAI-kompatibel webbserver.

Huvudsyftet med llama.cpp är att möjliggöra LLM-inferens med minimal setup och toppmodern prestanda på en mängd olika hårdvaror – både lokalt och i molnet.

- Ren C/C++-implementation utan några beroenden  
- Apple silicon är prioriterat – optimerat via ARM NEON, Accelerate och Metal-ramverk  
- Stöd för AVX, AVX2 och AVX512 på x86-arkitekturer  
- 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit och 8-bit heltalskvantisering för snabbare inferens och minskad minnesanvändning  
- Anpassade CUDA-kärnor för att köra LLMs på NVIDIA GPU:er (stöd för AMD GPU:er via HIP)  
- Vulkan- och SYCL-backendstöd  
- CPU+GPU hybridinferens för att delvis accelerera modeller som är större än den totala VRAM-kapaciteten  

## **Kvantisering av Phi-3.5 med llama.cpp**

Phi-3.5-Instruct-modellen kan kvantiseras med llama.cpp, men Phi-3.5-Vision och Phi-3.5-MoE stöds ännu inte. Formatet som konverteras av llama.cpp är gguf, vilket också är det mest använda kvantiseringsformatet.

Det finns ett stort antal kvantiserade GGUF-formatmodeller på Hugging Face. AI Foundry, Ollama och LlamaEdge förlitar sig på llama.cpp, så GGUF-modeller används ofta.

### **Vad är GGUF**

GGUF är ett binärt format som är optimerat för snabb inläsning och sparande av modeller, vilket gör det mycket effektivt för inferensändamål. GGUF är designat för användning med GGML och andra exekverare. GGUF utvecklades av @ggerganov som också är utvecklaren av llama.cpp, ett populärt C/C++-ramverk för LLM-inferens. Modeller som ursprungligen utvecklats i ramverk som PyTorch kan konverteras till GGUF-format för användning med dessa motorer.

### **ONNX vs GGUF**

ONNX är ett traditionellt maskininlärnings-/djupinlärningsformat som har bra stöd i olika AI-ramverk och används ofta i edge-enheter. GGUF, å andra sidan, baseras på llama.cpp och kan sägas vara utvecklat i GenAI-eran. De två har liknande användningsområden. Om du vill ha bättre prestanda i inbäddad hårdvara och applikationslager kan ONNX vara rätt val. Om du använder derivatramverket och teknologin från llama.cpp kan GGUF vara bättre.

### **Kvantisering av Phi-3.5-Instruct med llama.cpp**

**1. Miljökonfiguration**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantisering**

Konvertera Phi-3.5-Instruct till FP16 GGUF med llama.cpp


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Kvantisering av Phi-3.5 till INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testning**

Installera llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Notera*** 

Om du använder Apple Silicon, installera llama-cpp-python på detta sätt


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testning 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Resurser**

1. Läs mer om llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)  
2. Läs mer om onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  
3. Läs mer om GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.