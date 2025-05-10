<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-09T14:16:23+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "sw"
}
-->
# **Kukokotoa Familia ya Phi kwa kutumia llama.cpp**

## **Nini llama.cpp**

llama.cpp ni maktaba ya programu chanzo huria iliyotungwa hasa kwa C++ ambayo hufanya utambuzi wa lugha kwa kutumia Miundo Mikubwa ya Lugha (LLMs) mbalimbali, kama Llama. Lengo lake kuu ni kutoa utendaji bora wa kisasa kwa utambuzi wa LLM kwenye vifaa mbalimbali kwa usanidi mdogo. Zaidi ya hayo, kuna vifungo vya Python vinavyopatikana kwa maktaba hii, vinavyotoa API ya hali ya juu kwa ukamilishaji wa maandishi na seva ya wavuti inayolingana na OpenAI.

Lengo kuu la llama.cpp ni kuwezesha utambuzi wa LLM kwa usanidi mdogo na utendaji wa kisasa kwenye aina nyingi za vifaa - mahali pa kazi na wingu.

- Utekelezaji wa C/C++ usio na utegemezi wowote
- Apple silicon inazingatiwa sana - imeboreshwa kwa kutumia ARM NEON, Accelerate na Metal frameworks
- Msaada wa AVX, AVX2 na AVX512 kwa miundo ya x86
- Uwekaji wa nambari kwa 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, na 8-bit kwa utambuzi wa haraka na matumizi ya chini ya kumbukumbu
- Kernels maalum za CUDA kwa kuendesha LLM kwenye GPUs za NVIDIA (msaada kwa GPUs za AMD kupitia HIP)
- Msaada wa backend wa Vulkan na SYCL
- Utambuzi mchanganyiko wa CPU+GPU kuharakisha sehemu ya mifano mikubwa kuliko uwezo wa jumla wa VRAM

## **Kukokotoa Phi-3.5 kwa kutumia llama.cpp**

Mfano wa Phi-3.5-Instruct unaweza kukokotolewa kwa kutumia llama.cpp, lakini Phi-3.5-Vision na Phi-3.5-MoE bado hazijatambuliwa. Muundo unaobadilishwa na llama.cpp ni gguf, ambao pia ni muundo unaotumika zaidi kwa kukokotoa.

Kuna idadi kubwa ya mifano iliyokokotolewa kwa muundo wa GGUF kwenye Hugging face. AI Foundry, Ollama, na LlamaEdge hutegemea llama.cpp, hivyo mifano ya GGUF pia hutumika mara nyingi.

### **Nini GGUF**

GGUF ni muundo wa binary ulioboreshwa kwa upakiaji na uhifadhi wa haraka wa mifano, na hivyo kufanya kazi kwa ufanisi mkubwa kwa madhumuni ya utambuzi. GGUF imeundwa kwa matumizi na GGML na watendaji wengine. GGUF ilitengenezwa na @ggerganov ambaye pia ni mtengenezaji wa llama.cpp, mfumo maarufu wa utambuzi wa LLM wa C/C++. Mifano iliyoandaliwa awali katika mifumo kama PyTorch inaweza kubadilishwa kuwa muundo wa GGUF kwa matumizi na injini hizo.

### **ONNX vs GGUF**

ONNX ni muundo wa jadi wa mashine ya kujifunza/mfumo wa kujifunza kwa kina, unaoungwa mkono vizuri katika mifumo mbalimbali ya AI na una matumizi mazuri kwenye vifaa vya edge. Kuhusu GGUF, inategemea llama.cpp na inaweza kusemwa kuwa imezaliwa katika enzi ya GenAI. Zote mbili zina matumizi yanayofanana. Ikiwa unahitaji utendaji bora kwenye vifaa vilivyojengwa ndani na tabaka za programu, ONNX inaweza kuwa chaguo lako. Ikiwa unatumia mfumo wa lezo na teknolojia ya llama.cpp, basi GGUF inaweza kuwa bora zaidi.

### **Kukokotoa Phi-3.5-Instruct kwa kutumia llama.cpp**

**1. Usanidi wa Mazingira**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kukokotoa**

Kutumia llama.cpp kubadilisha Phi-3.5-Instruct kuwa FP16 GGUF


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

Kama unatumia Apple Silicon, tafadhali sakinisha llama-cpp-python kwa njia hii


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

**Kiarushi**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upotovu wa maana. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatubeba dhima kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.