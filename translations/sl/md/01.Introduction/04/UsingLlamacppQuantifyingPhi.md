<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-07-16T22:12:50+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "sl"
}
-->
# **Kvantizacija družine Phi z uporabo llama.cpp**

## **Kaj je llama.cpp**

llama.cpp je odprtokodna programska knjižnica, večinoma napisana v C++, ki izvaja sklepanje na različnih velikih jezikovnih modelih (LLM), kot je Llama. Glavni cilj je zagotoviti vrhunsko zmogljivost pri sklepanju LLM na širokem naboru strojne opreme z minimalno nastavitvijo. Poleg tega so na voljo tudi Python vezave za to knjižnico, ki ponujajo visokonivojski API za dokončanje besedila in spletni strežnik združljiv z OpenAI.

Glavni namen llama.cpp je omogočiti sklepanje LLM z minimalno nastavitvijo in vrhunsko zmogljivostjo na različnih vrstah strojne opreme – lokalno in v oblaku.

- Preprosta implementacija v C/C++ brez odvisnosti
- Apple silicon je podprt kot prvorazredna platforma – optimizirano preko ARM NEON, Accelerate in Metal ogrodij
- Podpora za AVX, AVX2 in AVX512 na arhitekturah x86
- Kvantizacija z 1,5-bitnim, 2-bitnim, 3-bitnim, 4-bitnim, 5-bitnim, 6-bitnim in 8-bitnim celim številom za hitrejše sklepanje in manjšo porabo pomnilnika
- Prilagojeni CUDA jedra za izvajanje LLM na NVIDIA GPU-jih (podpora za AMD GPU-je preko HIP)
- Podpora za Vulkan in SYCL zaledje
- Hibridno sklepanje CPU+GPU za delno pospeševanje modelov, večjih od skupne kapacitete VRAM

## **Kvantizacija Phi-3.5 z llama.cpp**

Model Phi-3.5-Instruct je mogoče kvantizirati z llama.cpp, medtem ko Phi-3.5-Vision in Phi-3.5-MoE še nista podprta. Format, ki ga pretvori llama.cpp, je gguf, ki je tudi najbolj razširjen format kvantizacije.

Na Hugging Face je na voljo veliko modelov v kvantiziranem formatu GGUF. AI Foundry, Ollama in LlamaEdge temeljijo na llama.cpp, zato se modeli GGUF pogosto uporabljajo.

### **Kaj je GGUF**

GGUF je binarni format, optimiziran za hitro nalaganje in shranjevanje modelov, kar ga naredi zelo učinkovitega za sklepanje. GGUF je zasnovan za uporabo z GGML in drugimi izvrševalci. GGUF je razvil @ggerganov, ki je tudi razvijalec llama.cpp, priljubljenega C/C++ ogrodja za sklepanje LLM. Modeli, sprva razviti v ogrodjih, kot je PyTorch, se lahko pretvorijo v format GGUF za uporabo s temi motorji.

### **ONNX proti GGUF**

ONNX je tradicionalen format za strojno učenje/globoko učenje, ki je dobro podprt v različnih AI ogrodjih in ima dobre primere uporabe na robnih napravah. GGUF pa temelji na llama.cpp in ga lahko označimo kot produkt dobe GenAI. Oba imata podobne namene. Če želite boljšo zmogljivost na vgrajeni strojni opremi in aplikacijskih plasteh, je ONNX morda prava izbira. Če uporabljate izpeljano ogrodje in tehnologijo llama.cpp, je GGUF lahko boljša izbira.

### **Kvantizacija Phi-3.5-Instruct z uporabo llama.cpp**

**1. Nastavitev okolja**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantizacija**

S pomočjo llama.cpp pretvorite Phi-3.5-Instruct v FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Kvantizacija Phi-3.5 v INT4


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
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.