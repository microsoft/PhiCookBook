<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-09T14:20:03+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "hr"
}
-->
# **Kvantizacija Phi obitelji koristeći llama.cpp**

## **Što je llama.cpp**

llama.cpp je open-source softverska biblioteka prvenstveno napisana u C++ koja vrši inferenciju na raznim velikim jezičnim modelima (LLM), poput Llama. Glavni cilj joj je pružiti vrhunske performanse za inferenciju LLM-a na širokom spektru hardvera uz minimalnu konfiguraciju. Osim toga, dostupne su Python bindings za ovu biblioteku, koje nude visoko-nivo API za dovršavanje teksta i web server kompatibilan s OpenAI.

Glavni cilj llama.cpp je omogućiti inferenciju LLM-a s minimalnom konfiguracijom i vrhunskim performansama na raznolikom hardveru – lokalno i u oblaku.

- Čista C/C++ implementacija bez ikakvih ovisnosti
- Apple silicon je tretiran kao prvi razred – optimizirano putem ARM NEON, Accelerate i Metal frameworka
- Podrška za AVX, AVX2 i AVX512 na x86 arhitekturama
- Kvantizacija s 1.5-bitnim, 2-bitnim, 3-bitnim, 4-bitnim, 5-bitnim, 6-bitnim i 8-bitnim cijelim brojevima za bržu inferenciju i manju potrošnju memorije
- Prilagođeni CUDA kernel-i za pokretanje LLM-a na NVIDIA GPU-ima (podrška za AMD GPU-e putem HIP-a)
- Podrška za Vulkan i SYCL backend
- Hibridna inferencija CPU+GPU za djelomično ubrzanje modela većih od ukupnog kapaciteta VRAM-a

## **Kvantizacija Phi-3.5 s llama.cpp**

Model Phi-3.5-Instruct može se kvantizirati koristeći llama.cpp, dok Phi-3.5-Vision i Phi-3.5-MoE još nisu podržani. Format koji llama.cpp koristi za konverziju je gguf, koji je ujedno i najrašireniji format kvantizacije.

Postoji velik broj kvantiziranih modela u GGUF formatu na Hugging Faceu. AI Foundry, Ollama i LlamaEdge se oslanjaju na llama.cpp, stoga se GGUF modeli često koriste.

### **Što je GGUF**

GGUF je binarni format optimiziran za brzo učitavanje i spremanje modela, što ga čini vrlo učinkovitim za inferenciju. GGUF je dizajniran za korištenje s GGML i drugim izvršiteljima. GGUF je razvio @ggerganov, koji je također developer llama.cpp, popularnog C/C++ frameworka za inferenciju LLM-a. Modeli razvijeni u frameworkima poput PyTorcha mogu se konvertirati u GGUF format za korištenje s tim alatima.

### **ONNX vs GGUF**

ONNX je tradicionalni format za strojno i duboko učenje, koji je dobro podržan u različitim AI frameworkima i ima dobru primjenu na edge uređajima. GGUF, s druge strane, baziran je na llama.cpp i može se reći da je nastao u eri GenAI. Oba imaju slične primjene. Ako želite bolje performanse na ugrađenom hardveru i u aplikacijskim slojevima, ONNX bi mogao biti vaš izbor. Ako koristite izvedeni framework i tehnologiju llama.cpp, GGUF može biti bolji.

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

***Note*** 

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
Ovaj dokument preveden je pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.