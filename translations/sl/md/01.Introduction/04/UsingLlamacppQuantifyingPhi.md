<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-09T14:20:33+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "sl"
}
-->
# **Quantiziranje Phi Family z uporabo llama.cpp**

## **Kaj je llama.cpp**

llama.cpp je odprtokodna programska knjižnica, večinoma napisana v C++, ki izvaja inferenco na različnih velikih jezikovnih modelih (LLM), kot je Llama. Glavni cilj je zagotoviti vrhunsko zmogljivost za inferenco LLM na širokem spektru strojne opreme z minimalno nastavitev. Poleg tega so na voljo tudi Python vezave, ki nudijo visokonivojski API za dokončanje besedila in OpenAI združljiv spletni strežnik.

Glavni namen llama.cpp je omogočiti inferenco LLM z minimalno nastavitev in vrhunsko zmogljivostjo na različnih napravah – lokalno in v oblaku.

- Čista C/C++ implementacija brez odvisnosti  
- Apple silicon je enakovredno podprt – optimiziran preko ARM NEON, Accelerate in Metal ogrodij  
- Podpora za AVX, AVX2 in AVX512 na x86 arhitekturah  
- Kvantizacija z 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit in 8-bit celimi števili za hitrejšo inferenco in manjšo porabo pomnilnika  
- Prilagojeni CUDA jedri za poganjanje LLM na NVIDIA GPU-jih (podpora za AMD GPU preko HIP)  
- Podpora za Vulkan in SYCL backend  
- Hibridna inferenca CPU+GPU za delno pospeševanje modelov, ki so večji od skupne kapacitete VRAM  

## **Kvantiacija Phi-3.5 z llama.cpp**

Model Phi-3.5-Instruct je mogoče kvantizirati z llama.cpp, vendar Phi-3.5-Vision in Phi-3.5-MoE še nista podprta. Format, ki ga pretvori llama.cpp, je gguf, kar je tudi najbolj razširjen format kvantizacije.

Na Hugging Face je veliko modelov v kvantiziranem GGUF formatu. AI Foundry, Ollama in LlamaEdge uporabljajo llama.cpp, zato so GGUF modeli pogosto v uporabi.

### **Kaj je GGUF**

GGUF je binarni format, optimiziran za hitro nalaganje in shranjevanje modelov, kar ga naredi zelo učinkovitega za inferenco. GGUF je zasnovan za uporabo z GGML in drugimi izvrševalci. GGUF je razvil @ggerganov, ki je tudi razvijalec llama.cpp, priljubljenega C/C++ ogrodja za inferenco LLM. Modeli, ki so sprva razviti v ogrodjih, kot je PyTorch, se lahko pretvorijo v GGUF format za uporabo z omenjenimi motorji.

### **ONNX proti GGUF**

ONNX je tradicionalen format za strojno učenje/globoko učenje, ki je dobro podprt v različnih AI ogrodjih in ima dobre primere uporabe na robnih napravah. GGUF pa temelji na llama.cpp in ga lahko štejemo za produkt dobe GenAI. Oba imata podobne uporabe. Če želite boljšo zmogljivost na vgrajeni strojni opremi in aplikacijskih slojih, je ONNX lahko vaša izbira. Če uporabljate derivatna ogrodja in tehnologije llama.cpp, je GGUF morda boljši.

### **Kvantiacija Phi-3.5-Instruct z uporabo llama.cpp**

**1. Nastavitev okolja**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantizacija**

Pretvorba Phi-3.5-Instruct v FP16 GGUF z uporabo llama.cpp


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Kvantiacija Phi-3.5 v INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testiranje**

Namestite llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Opomba*** 

Če uporabljate Apple Silicon, namestite llama-cpp-python na ta način


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testiranje 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Viri**

1. Več o llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)  
2. Več o onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  
3. Več o GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.