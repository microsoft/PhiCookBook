<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-07-16T22:12:07+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "ro"
}
-->
# **Cuantificarea familiei Phi folosind llama.cpp**

## **Ce este llama.cpp**

llama.cpp este o bibliotecă software open-source scrisă în principal în C++ care realizează inferență pe diverse modele mari de limbaj (LLM-uri), cum ar fi Llama. Scopul său principal este să ofere performanțe de ultimă generație pentru inferența LLM pe o gamă largă de hardware, cu o configurare minimă. În plus, există legături Python disponibile pentru această bibliotecă, care oferă o API de nivel înalt pentru completarea textului și un server web compatibil cu OpenAI.

Obiectivul principal al llama.cpp este să permită inferența LLM cu o configurare minimă și performanțe de top pe o varietate largă de hardware - local și în cloud.

- Implementare simplă în C/C++ fără dependențe
- Apple silicon este tratat ca o prioritate - optimizat prin ARM NEON, Accelerate și framework-urile Metal
- Suport AVX, AVX2 și AVX512 pentru arhitecturi x86
- Cuantificare pe 1.5-biți, 2-biți, 3-biți, 4-biți, 5-biți, 6-biți și 8-biți pentru inferență mai rapidă și consum redus de memorie
- Kernel-uri CUDA personalizate pentru rularea LLM pe GPU-uri NVIDIA (suport pentru GPU-uri AMD prin HIP)
- Suport backend Vulkan și SYCL
- Inferență hibrid CPU+GPU pentru accelerarea parțială a modelelor mai mari decât capacitatea totală de VRAM

## **Cuantificarea Phi-3.5 cu llama.cpp**

Modelul Phi-3.5-Instruct poate fi cuantificat folosind llama.cpp, însă Phi-3.5-Vision și Phi-3.5-MoE nu sunt încă suportate. Formatul convertit de llama.cpp este gguf, care este și cel mai utilizat format de cuantificare.

Există un număr mare de modele cuantificate în format GGUF pe Hugging Face. AI Foundry, Ollama și LlamaEdge se bazează pe llama.cpp, astfel că modelele GGUF sunt folosite frecvent.

### **Ce este GGUF**

GGUF este un format binar optimizat pentru încărcarea și salvarea rapidă a modelelor, făcându-l foarte eficient pentru inferență. GGUF este conceput pentru a fi folosit cu GGML și alți executanți. GGUF a fost dezvoltat de @ggerganov, care este și dezvoltatorul llama.cpp, un framework popular de inferență LLM în C/C++. Modelele dezvoltate inițial în framework-uri precum PyTorch pot fi convertite în format GGUF pentru a fi folosite cu aceste motoare.

### **ONNX vs GGUF**

ONNX este un format tradițional pentru machine learning/deep learning, bine suportat în diverse framework-uri AI și cu scenarii bune de utilizare pe dispozitive edge. În schimb, GGUF este bazat pe llama.cpp și poate fi considerat produs în era GenAI. Ambele au utilizări similare. Dacă dorești performanțe mai bune pe hardware încorporat și în straturile aplicațiilor, ONNX poate fi alegerea potrivită. Dacă folosești framework-ul derivat și tehnologia llama.cpp, atunci GGUF poate fi mai potrivit.

### **Cuantificarea Phi-3.5-Instruct folosind llama.cpp**

**1. Configurarea mediului**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Cuantificarea**

Folosind llama.cpp convertește Phi-3.5-Instruct în FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Cuantificarea Phi-3.5 în INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testare**

Instalează llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Notă*** 

Dacă folosești Apple Silicon, te rugăm să instalezi llama-cpp-python astfel


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testare 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Resurse**

1. Află mai multe despre llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. Află mai multe despre onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. Află mai multe despre GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.