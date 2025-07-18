<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-07-16T22:10:23+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "nl"
}
-->
# **Quantizen van Phi Family met llama.cpp**

## **Wat is llama.cpp**

llama.cpp is een open-source softwarebibliotheek, voornamelijk geschreven in C++, die inferentie uitvoert op verschillende Large Language Models (LLM's), zoals Llama. Het hoofddoel is om state-of-the-art prestaties te leveren voor LLM-inferentie op een breed scala aan hardware met minimale configuratie. Daarnaast zijn er Python-bindings beschikbaar voor deze bibliotheek, die een high-level API bieden voor tekstafwerking en een OpenAI-compatibele webserver.

Het belangrijkste doel van llama.cpp is om LLM-inferentie mogelijk te maken met minimale setup en state-of-the-art prestaties op diverse hardware - zowel lokaal als in de cloud.

- Eenvoudige C/C++ implementatie zonder afhankelijkheden
- Apple silicon wordt volledig ondersteund - geoptimaliseerd via ARM NEON, Accelerate en Metal frameworks
- AVX, AVX2 en AVX512 ondersteuning voor x86-architecturen
- 1,5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit en 8-bit integer quantisatie voor snellere inferentie en minder geheugengebruik
- Aangepaste CUDA-kernels voor het draaien van LLM's op NVIDIA GPU's (ondersteuning voor AMD GPU's via HIP)
- Vulkan- en SYCL-backend ondersteuning
- CPU+GPU hybride inferentie om modellen die groter zijn dan de totale VRAM-capaciteit gedeeltelijk te versnellen

## **Quantizen van Phi-3.5 met llama.cpp**

Het Phi-3.5-Instruct model kan worden gequantized met llama.cpp, maar Phi-3.5-Vision en Phi-3.5-MoE worden nog niet ondersteund. Het formaat dat door llama.cpp wordt geconverteerd is gguf, wat ook het meest gebruikte quantisatieformaat is.

Er zijn veel gequantizeerde GGUF-formaat modellen beschikbaar op Hugging Face. AI Foundry, Ollama en LlamaEdge vertrouwen op llama.cpp, dus GGUF-modellen worden ook vaak gebruikt.

### **Wat is GGUF**

GGUF is een binair formaat dat geoptimaliseerd is voor snelle laad- en opslagtijden van modellen, waardoor het zeer efficiënt is voor inferentie. GGUF is ontworpen voor gebruik met GGML en andere executors. GGUF is ontwikkeld door @ggerganov, die ook de ontwikkelaar is van llama.cpp, een populair C/C++ LLM-inferentiekader. Modellen die oorspronkelijk in frameworks zoals PyTorch zijn ontwikkeld, kunnen worden geconverteerd naar het GGUF-formaat voor gebruik met deze engines.

### **ONNX vs GGUF**

ONNX is een traditioneel machine learning/deep learning formaat, dat goed wordt ondersteund in verschillende AI-frameworks en goede toepassingsmogelijkheden heeft op edge-apparaten. GGUF daarentegen is gebaseerd op llama.cpp en kan worden gezien als een product uit het GenAI-tijdperk. Beide hebben vergelijkbare toepassingen. Wil je betere prestaties op embedded hardware en applicatielagen, dan is ONNX wellicht de beste keuze. Gebruik je het afgeleide framework en de technologie van llama.cpp, dan is GGUF waarschijnlijk beter.

### **Quantizen van Phi-3.5-Instruct met llama.cpp**

**1. Omgevingsconfiguratie**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Quantisatie**

Gebruik llama.cpp om Phi-3.5-Instruct te converteren naar FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Quantizen van Phi-3.5 naar INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testen**

Installeer llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Opmerking*** 

Als je Apple Silicon gebruikt, installeer dan llama-cpp-python op deze manier


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testen 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Bronnen**

1. Meer informatie over llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. Meer informatie over onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. Meer informatie over GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.