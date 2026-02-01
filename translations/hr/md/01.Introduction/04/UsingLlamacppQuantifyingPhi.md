# **Kvantizacija Phi obitelji koristeći llama.cpp**

## **Što je llama.cpp**

llama.cpp je open-source softverska biblioteka uglavnom napisana u C++ koja vrši inferenciju na raznim velikim jezičnim modelima (LLM), poput Llama. Glavni cilj joj je pružiti vrhunske performanse za LLM inferenciju na širokom spektru hardvera uz minimalnu konfiguraciju. Također, dostupne su Python veze za ovu biblioteku koje nude visokorazinski API za dovršavanje teksta i OpenAI kompatibilan web server.

Glavni cilj llama.cpp je omogućiti LLM inferenciju s minimalnom konfiguracijom i vrhunskim performansama na raznovrsnom hardveru – lokalno i u oblaku.

- Čista C/C++ implementacija bez ikakvih ovisnosti
- Apple silicon je prioritet – optimiziran putem ARM NEON, Accelerate i Metal frameworka
- Podrška za AVX, AVX2 i AVX512 na x86 arhitekturama
- Kvantizacija na 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit i 8-bit cijele brojeve za bržu inferenciju i smanjenu potrošnju memorije
- Prilagođeni CUDA kerneli za pokretanje LLM-ova na NVIDIA GPU-ima (podrška za AMD GPU-e putem HIP-a)
- Podrška za Vulkan i SYCL backend
- Hibridna inferencija CPU+GPU za djelomično ubrzanje modela većih od ukupnog kapaciteta VRAM-a

## **Kvantizacija Phi-3.5 s llama.cpp**

Model Phi-3.5-Instruct može se kvantizirati koristeći llama.cpp, no Phi-3.5-Vision i Phi-3.5-MoE još nisu podržani. Format koji llama.cpp konvertira je gguf, koji je također najrašireniji format kvantizacije.

Na Hugging faceu postoji veliki broj modela u kvantiziranom GGUF formatu. AI Foundry, Ollama i LlamaEdge se oslanjaju na llama.cpp, pa se GGUF modeli često koriste.

### **Što je GGUF**

GGUF je binarni format optimiziran za brzo učitavanje i spremanje modela, što ga čini vrlo učinkovitim za inferenciju. GGUF je dizajniran za korištenje s GGML-om i drugim izvršiteljima. GGUF je razvio @ggerganov, koji je također developer llama.cpp, popularnog C/C++ okvira za LLM inferenciju. Modeli izvorno razvijeni u frameworkima poput PyTorcha mogu se konvertirati u GGUF format za korištenje s tim motorima.

### **ONNX vs GGUF**

ONNX je tradicionalni format za strojno učenje/duboko učenje, koji je dobro podržan u različitim AI frameworkima i ima dobre primjene na edge uređajima. Što se tiče GGUF-a, on je baziran na llama.cpp i može se reći da je nastao u eri GenAI. Oba imaju slične primjene. Ako želite bolje performanse na ugrađenom hardveru i aplikacijskim slojevima, ONNX može biti vaš izbor. Ako koristite izvedeni framework i tehnologiju llama.cpp, GGUF može biti bolji.

### **Kvantizacija Phi-3.5-Instruct koristeći llama.cpp**

**1. Konfiguracija okruženja**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantizacija**

Korištenjem llama.cpp konvertirajte Phi-3.5-Instruct u FP16 GGUF


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

Ako koristite Apple Silicon, instalirajte llama-cpp-python na ovaj način


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testiranje 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Resursi**

1. Saznajte više o llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. Saznajte više o onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. Saznajte više o GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.