<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-07-16T22:10:02+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "no"
}
-->
# **Kvantifisering av Phi-familien med llama.cpp**

## **Hva er llama.cpp**

llama.cpp er et åpen kildekode-bibliotek hovedsakelig skrevet i C++ som utfører inferens på ulike store språkmodeller (LLMs), som Llama. Hovedmålet er å tilby topp ytelse for LLM-inferens på et bredt spekter av maskinvare med minimal oppsett. I tillegg finnes det Python-bindings for dette biblioteket, som gir et høynivå-API for tekstfullføring og en OpenAI-kompatibel webserver.

Hovedmålet med llama.cpp er å muliggjøre LLM-inferens med minimal oppsett og topp ytelse på mange forskjellige maskinvareplattformer – både lokalt og i skyen.

- Ren C/C++-implementering uten avhengigheter
- Apple silicon er fullt støttet – optimalisert via ARM NEON, Accelerate og Metal-rammeverkene
- Støtte for AVX, AVX2 og AVX512 på x86-arkitekturer
- 1,5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit og 8-bit heltallskvantifisering for raskere inferens og redusert minnebruk
- Egendefinerte CUDA-kjerner for kjøring av LLM på NVIDIA GPUer (støtte for AMD GPUer via HIP)
- Vulkan- og SYCL-backend-støtte
- CPU+GPU hybrid inferens for delvis akselerasjon av modeller som er større enn total VRAM-kapasitet

## **Kvantifisering av Phi-3.5 med llama.cpp**

Phi-3.5-Instruct-modellen kan kvantifiseres med llama.cpp, men Phi-3.5-Vision og Phi-3.5-MoE støttes ikke ennå. Formatet som konverteres av llama.cpp er gguf, som også er det mest brukte kvantiseringsformatet.

Det finnes et stort antall kvantiserte GGUF-modeller på Hugging Face. AI Foundry, Ollama og LlamaEdge baserer seg på llama.cpp, så GGUF-modeller brukes ofte.

### **Hva er GGUF**

GGUF er et binært format som er optimalisert for rask lasting og lagring av modeller, noe som gjør det svært effektivt for inferens. GGUF er designet for bruk med GGML og andre kjøringsmotorer. GGUF ble utviklet av @ggerganov, som også er utvikleren av llama.cpp, et populært C/C++-rammeverk for LLM-inferens. Modeller som opprinnelig er utviklet i rammeverk som PyTorch kan konverteres til GGUF-format for bruk med disse motorene.

### **ONNX vs GGUF**

ONNX er et tradisjonelt maskinlærings-/dyp læringsformat som har god støtte i ulike AI-rammeverk og gode bruksområder på edge-enheter. Når det gjelder GGUF, er det basert på llama.cpp og kan sies å være utviklet i GenAI-æraen. Begge har lignende bruksområder. Hvis du ønsker bedre ytelse på innebygd maskinvare og applikasjonsnivå, kan ONNX være valget ditt. Hvis du bruker avledede rammeverk og teknologi fra llama.cpp, kan GGUF være bedre.

### **Kvantifisering av Phi-3.5-Instruct med llama.cpp**

**1. Miljøkonfigurasjon**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantifisering**

Bruk llama.cpp for å konvertere Phi-3.5-Instruct til FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Kvantifisering av Phi-3.5 til INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testing**

Installer llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Merk***

Hvis du bruker Apple Silicon, installer llama-cpp-python slik


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testing


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Ressurser**

1. Lær mer om llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)  
2. Lær mer om onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  
3. Lær mer om GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.