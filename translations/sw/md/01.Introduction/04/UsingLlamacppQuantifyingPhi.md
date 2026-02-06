# **Kukokotoa Familia ya Phi kwa kutumia llama.cpp**

## **Nini llama.cpp**

llama.cpp ni maktaba ya programu ya chanzo wazi iliyotengenezwa hasa kwa C++ inayofanya utambuzi kwenye Mifano Mikubwa ya Lugha (LLMs) mbalimbali, kama Llama. Lengo lake kuu ni kutoa utendaji wa hali ya juu kwa utambuzi wa LLM kwenye aina mbalimbali za vifaa kwa usanidi mdogo. Zaidi ya hayo, kuna vifungo vya Python vinavyopatikana kwa maktaba hii, vinavyotoa API ya kiwango cha juu kwa ukamilishaji wa maandishi na seva ya wavuti inayolingana na OpenAI.

Lengo kuu la llama.cpp ni kuwezesha utambuzi wa LLM kwa usanidi mdogo na utendaji wa hali ya juu kwenye aina mbalimbali za vifaa - kwa ndani na kwenye wingu.

- Utekelezaji wa kawaida wa C/C++ bila utegemezi wowote
- Apple silicon ni kipaumbele - umeboreshwa kupitia ARM NEON, Accelerate na mifumo ya Metal
- Msaada wa AVX, AVX2 na AVX512 kwa usanifu wa x86
- Kukokotoa kwa nambari za 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, na 8-bit kwa utambuzi wa haraka na matumizi madogo ya kumbukumbu
- Kernels maalum za CUDA kwa kuendesha LLM kwenye GPUs za NVIDIA (msaada kwa GPUs za AMD kupitia HIP)
- Msaada wa backend wa Vulkan na SYCL
- Utambuzi mchanganyiko wa CPU+GPU kuharakisha sehemu ya mifano mikubwa zaidi ya uwezo wa jumla wa VRAM

## **Kukokotoa Phi-3.5 kwa kutumia llama.cpp**

Mfano wa Phi-3.5-Instruct unaweza kukokotolewa kwa kutumia llama.cpp, lakini Phi-3.5-Vision na Phi-3.5-MoE bado hazijaungwa mkono. Muundo unaobadilishwa na llama.cpp ni gguf, ambao pia ni muundo unaotumika sana wa kukokotoa.

Kuna idadi kubwa ya mifano iliyokokotolewa kwa muundo wa GGUF kwenye Hugging Face. AI Foundry, Ollama, na LlamaEdge hutegemea llama.cpp, hivyo mifano ya GGUF pia hutumika mara nyingi.

### **Nini GGUF**

GGUF ni muundo wa binary ulioboreshwa kwa upakiaji na uhifadhi wa haraka wa mifano, na hivyo kuwa na ufanisi mkubwa kwa madhumuni ya utambuzi. GGUF imetengenezwa kwa matumizi na GGML na watendaji wengine. GGUF ilitengenezwa na @ggerganov ambaye pia ni mtengenezaji wa llama.cpp, mfumo maarufu wa utambuzi wa LLM wa C/C++. Mifano iliyotengenezwa awali katika mifumo kama PyTorch inaweza kubadilishwa kuwa muundo wa GGUF kwa matumizi na injini hizo.

### **ONNX dhidi ya GGUF**

ONNX ni muundo wa kawaida wa mashine kujifunza/kufundisha kwa kina, unaounga mkono vizuri katika Mifumo mbalimbali ya AI na una matukio mazuri ya matumizi kwenye vifaa vya edge. Kuhusu GGUF, inategemea llama.cpp na inaweza kusemwa imetengenezwa katika enzi ya GenAI. Zina matumizi yanayofanana. Ikiwa unataka utendaji bora kwenye vifaa vilivyojumuishwa na tabaka za programu, ONNX inaweza kuwa chaguo lako. Ikiwa unatumia mfumo wa urithi na teknolojia ya llama.cpp, basi GGUF inaweza kuwa bora zaidi.

### **Kukokotoa Phi-3.5-Instruct kwa kutumia llama.cpp**

**1. Usanidi wa Mazingira**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kukokotoa**

Kutumia llama.cpp badilisha Phi-3.5-Instruct kuwa FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Kukokotoa Phi-3.5 kuwa INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Kupima**

Sakinisha llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Note*** 

Ikiwa unatumia Apple Silicon, tafadhali sakinisha llama-cpp-python kwa njia hii


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Kupima 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Rasilimali**

1. Jifunze zaidi kuhusu llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. Jifunze zaidi kuhusu onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. Jifunze zaidi kuhusu GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.