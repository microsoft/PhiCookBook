<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-09T14:19:32+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "sr"
}
-->
# **Kvantizacija Phi porodice koristeći llama.cpp**

## **Šta je llama.cpp**

llama.cpp je open-source softverska biblioteka uglavnom napisana u C++ koja vrši inferencu na različitim velikim jezičkim modelima (LLM), kao što je Llama. Glavni cilj joj je da obezbedi vrhunske performanse za inferencu LLM na širokom spektru hardvera uz minimalnu konfiguraciju. Takođe, dostupni su Python bindingi za ovu biblioteku, koji nude visok nivo API-ja za dopunu teksta i OpenAI kompatibilan web server.

Glavni cilj llama.cpp je da omogući inferencu LLM sa minimalnom konfiguracijom i vrhunskim performansama na različitim hardverskim platformama - lokalno i u oblaku.

- Čista C/C++ implementacija bez ikakvih zavisnosti
- Apple silicon je prvi rang - optimizovan preko ARM NEON, Accelerate i Metal framework-a
- Podrška za AVX, AVX2 i AVX512 na x86 arhitekturama
- Kvantizacija u 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit i 8-bit celobrojne vrednosti za bržu inferencu i smanjenu potrošnju memorije
- Prilagođeni CUDA kerneli za pokretanje LLM na NVIDIA GPU-ima (podrška za AMD GPU preko HIP)
- Podrška za Vulkan i SYCL backend
- Hibridna inferenca CPU+GPU za delimično ubrzanje modela većih od ukupnog kapaciteta VRAM-a

## **Kvantizacija Phi-3.5 koristeći llama.cpp**

Model Phi-3.5-Instruct može se kvantizovati koristeći llama.cpp, dok Phi-3.5-Vision i Phi-3.5-MoE još nisu podržani. Format u koji llama.cpp konvertuje je gguf, koji je takođe najrašireniji format kvantizacije.

Na Hugging face postoji veliki broj modela u kvantizovanom GGUF formatu. AI Foundry, Ollama i LlamaEdge se oslanjaju na llama.cpp, pa se GGUF modeli često koriste.

### **Šta je GGUF**

GGUF je binarni format optimizovan za brzo učitavanje i čuvanje modela, što ga čini veoma efikasnim za inferencu. GGUF je dizajniran za upotrebu sa GGML i drugim izvršiocima. GGUF je razvio @ggerganov, koji je takođe developer llama.cpp, popularnog C/C++ framework-a za inferencu LLM. Modeli koji su prvobitno razvijeni u framework-ovima poput PyTorch mogu se konvertovati u GGUF format za upotrebu sa tim okruženjima.

### **ONNX vs GGUF**

ONNX je tradicionalni format za mašinsko učenje/duboko učenje, koji je dobro podržan u različitim AI framework-ovima i ima dobre primene na edge uređajima. GGUF, s druge strane, baziran je na llama.cpp i može se reći da je nastao u eri GenAI. Oboje imaju slične primene. Ako vam je potrebna bolja performansa na ugrađenom hardveru i u aplikacionim slojevima, ONNX može biti bolji izbor. Ako koristite izvedeni framework i tehnologiju llama.cpp, GGUF može biti prikladniji.

### **Kvantizacija Phi-3.5-Instruct koristeći llama.cpp**

**1. Konfiguracija okruženja**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantizacija**

Konvertovanje Phi-3.5-Instruct u FP16 GGUF koristeći llama.cpp


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Kvantizacija Phi-3.5 u INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testiranje**

Instalirajte llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Napomena*** 

Ako koristite Apple Silicon, instalirajte llama-cpp-python na sledeći način


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testiranje 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Resursi**

1. Više o llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)  
2. Više o onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  
3. Više o GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Изворни документ на његовом оригиналном језику треба сматрати ауторитетом. За критичне информације препоручује се професионални превод од стране људског преводиоца. Нисмо одговорни за било каква неспоразума или погрешне тумачења настала коришћењем овог превода.