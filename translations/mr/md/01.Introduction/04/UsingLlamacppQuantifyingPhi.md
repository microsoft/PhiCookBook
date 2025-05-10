<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-09T14:06:00+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "mr"
}
-->
# **llama.cpp वापरून Phi कुटुंबाचे क्वांटायझेशन**

## **llama.cpp म्हणजे काय**

llama.cpp ही मुख्यतः C++ मध्ये लिहिलेली एक मुक्त स्रोत सॉफ्टवेअर लायब्ररी आहे जी Llama सारख्या विविध Large Language Models (LLMs) वर inference करते. याचा मुख्य उद्देश विविध हार्डवेअरवर कमी सेटअपसह अत्याधुनिक LLM inference प्रदान करणे आहे. याशिवाय, या लायब्ररीसाठी Python बाइंडिंग्स उपलब्ध आहेत, जे टेक्स्ट पूर्ण करण्यासाठी उच्चस्तरीय API आणि OpenAI सुसंगत वेब सर्व्हर ऑफर करतात.

llama.cpp चा मुख्य उद्देश म्हणजे कमी सेटअपमध्ये आणि विविध हार्डवेअरवर - स्थानिक तसेच क्लाउडमध्ये - अत्याधुनिक कामगिरीसह LLM inference सक्षम करणे.

- कोणत्याही अवलंबित्वांशिवाय साधा C/C++ अंमलबजावणी
- Apple silicon साठी विशेष अनुकूलन - ARM NEON, Accelerate आणि Metal फ्रेमवर्कद्वारे ऑप्टिमाइझ केलेले
- x86 आर्किटेक्चर्ससाठी AVX, AVX2 आणि AVX512 समर्थन
- जलद inference आणि कमी मेमरी वापरासाठी 1.5-बिट, 2-बिट, 3-बिट, 4-बिट, 5-बिट, 6-बिट आणि 8-बिट पूर्णांक क्वांटायझेशन
- NVIDIA GPUs वर LLM चालवण्यासाठी कस्टम CUDA कर्नल्स (AMD GPUs साठी HIP द्वारे समर्थन)
- Vulkan आणि SYCL बॅकएंड समर्थन
- एकूण VRAM क्षमतेपेक्षा मोठ्या मॉडेलसाठी CPU+GPU हायब्रिड inference ज्यामुळे काहीशी गती वाढते

## **llama.cpp वापरून Phi-3.5 चे क्वांटायझेशन**

Phi-3.5-Instruct मॉडेलला llama.cpp वापरून क्वांटाइज करता येते, पण Phi-3.5-Vision आणि Phi-3.5-MoE अजून समर्थित नाहीत. llama.cpp द्वारे रूपांतरित केलेला फॉरमॅट gguf आहे, जो सर्वाधिक वापरला जाणारा क्वांटायझेशन फॉरमॅट देखील आहे.

Hugging Face वर क्वांटाइज केलेल्या GGUF फॉरमॅटमधील मॉडेल्स खूप आहेत. AI Foundry, Ollama, आणि LlamaEdge हे llama.cpp वर आधारित असल्यामुळे GGUF मॉडेल्स देखील बऱ्याचदा वापरले जातात.

### **GGUF म्हणजे काय**

GGUF हा एक बायनरी फॉरमॅट आहे जो मॉडेल्स जलद लोड आणि सेव्ह करण्यासाठी ऑप्टिमाइझ केलेला आहे, ज्यामुळे inference साठी तो अत्यंत कार्यक्षम ठरतो. GGUF GGML आणि इतर एग्झिक्युटर्ससाठी डिझाइन केलेला आहे. GGUF ची निर्मिती @ggerganov यांनी केली आहे, जे llama.cpp चेही डेव्हलपर आहेत, जो एक लोकप्रिय C/C++ LLM inference फ्रेमवर्क आहे. PyTorch सारख्या फ्रेमवर्कमध्ये तयार केलेले मॉडेल्स GGUF फॉरमॅटमध्ये रूपांतरित करून त्या इंजिन्ससाठी वापरता येतात.

### **ONNX vs GGUF**

ONNX हा पारंपरिक मशीन लर्निंग/डीप लर्निंग फॉरमॅट आहे, जो विविध AI फ्रेमवर्कमध्ये चांगला समर्थित आहे आणि एज डिव्हाइसेसमध्ये वापरासाठी उपयुक्त आहे. तर GGUF हा llama.cpp वर आधारित असून GenAI युगात तयार झालेला म्हणता येईल. दोन्हीचे वापर समान आहेत. जर तुम्हाला एम्बेडेड हार्डवेअर आणि अ‍ॅप्लिकेशन स्तरावर चांगली कामगिरी हवी असेल तर ONNX तुमचा पर्याय असू शकतो. तर llama.cpp च्या डेरिव्हेटिव्ह फ्रेमवर्क आणि तंत्रज्ञानाचा वापर करत असल्यास GGUF चांगला पर्याय ठरू शकतो.

### **llama.cpp वापरून Phi-3.5-Instruct चे क्वांटायझेशन**

**1. पर्यावरण सेटअप**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. क्वांटायझेशन**

llama.cpp वापरून Phi-3.5-Instruct चे FP16 GGUF मध्ये रूपांतरण


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5 चे INT4 मध्ये क्वांटायझेशन


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. चाचणी**

llama-cpp-python इन्स्टॉल करा


```bash

pip install llama-cpp-python -U

```

***टीप*** 

जर तुम्ही Apple Silicon वापरत असाल, तर llama-cpp-python असे इन्स्टॉल करा


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

चाचणी 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **संसाधने**

1. llama.cpp बद्दल अधिक जाणून घ्या [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. onnxruntime बद्दल अधिक जाणून घ्या [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. GGUF बद्दल अधिक माहिती [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये चुका किंवा अचूकतेत त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाच्या माहितीकरिता व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थांबद्दल आम्ही जबाबदार नाही.