<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-09T14:16:50+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "hu"
}
-->
# **Phi család kvantálása llama.cpp segítségével**

## **Mi az a llama.cpp**

A llama.cpp egy nyílt forráskódú szoftárkönyvtár, amely elsősorban C++ nyelven íródott, és különböző nagy nyelvi modelleken (LLM-ek), például a Llamán végez inferenciát. Fő célja, hogy minimális beállítással biztosítson csúcsteljesítményt LLM inferencia terén széles hardverpalettán. Ezen felül elérhetők Python kötései is, amelyek magas szintű API-t kínálnak szövegkiegészítéshez, valamint egy OpenAI kompatibilis webszervert.

A llama.cpp fő célja, hogy lehetővé tegye az LLM inferenciát minimális beállítással és csúcsteljesítménnyel különféle hardvereken – helyben és felhőben egyaránt.

- Egyszerű C/C++ megvalósítás függőségek nélkül
- Apple silicon elsőrangú támogatása – optimalizálva ARM NEON, Accelerate és Metal keretrendszereken keresztül
- AVX, AVX2 és AVX512 támogatás x86 architektúrákhoz
- 1.5-bites, 2-bites, 3-bites, 4-bites, 5-bites, 6-bites és 8-bites egész szám kvantálás a gyorsabb inferencia és kisebb memóriahasználat érdekében
- Egyedi CUDA kernel-ek NVIDIA GPU-kon való LLM futtatáshoz (AMD GPU támogatás HIP-en keresztül)
- Vulkan és SYCL háttértámogatás
- CPU+GPU hibrid inferencia a VRAM kapacitást meghaladó modellek részleges gyorsításához

## **Phi-3.5 kvantálása llama.cpp-vel**

A Phi-3.5-Instruct modell kvantálható llama.cpp-vel, azonban a Phi-3.5-Vision és Phi-3.5-MoE még nem támogatott. A llama.cpp által konvertált formátum a gguf, amely a legelterjedtebb kvantálási formátum is egyben.

A Hugging Face-en rengeteg kvantált GGUF formátumú modell található. Az AI Foundry, Ollama és LlamaEdge is a llama.cpp-re épít, így a GGUF modellek gyakoriak.

### **Mi az a GGUF**

A GGUF egy bináris formátum, amelyet a modellek gyors betöltésére és mentésére optimalizáltak, így nagyon hatékony inferenciához. A GGUF a GGML és más futtatók használatára készült. A GGUF-t @ggerganov fejlesztette, aki a llama.cpp megalkotója is, egy népszerű C/C++ LLM inferencia keretrendszer. A PyTorch-hoz hasonló keretrendszerekben fejlesztett modelleket is át lehet konvertálni GGUF formátumba a kompatibilis futtatók használatához.

### **ONNX vs GGUF**

Az ONNX egy hagyományos gépi tanulási/mélytanulási formátum, amelyet széles körben támogatnak különböző AI keretrendszerek, és jól használható élő eszközökön. A GGUF ezzel szemben a llama.cpp-re épül, és mondhatjuk, hogy a GenAI korszak terméke. Mindkettő hasonló felhasználási területtel bír. Ha beágyazott hardvereken és alkalmazási rétegekben jobb teljesítményt szeretnél, az ONNX lehet a jobb választás. Ha pedig a llama.cpp származtatott keretrendszereit és technológiáit használod, akkor a GGUF lehet előnyösebb.

### **Phi-3.5-Instruct kvantálása llama.cpp-vel**

**1. Környezet beállítása**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantálás**

Phi-3.5-Instruct konvertálása FP16 GGUF formátumba llama.cpp segítségével


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5 kvantálása INT4-re


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Tesztelés**

llama-cpp-python telepítése


```bash

pip install llama-cpp-python -U

```

***Megjegyzés***

Ha Apple Silicon-t használsz, a llama-cpp-python telepítése így történjen


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Tesztelés


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Források**

1. Tudj meg többet a llama.cpp-ről [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. Tudj meg többet az onnxruntime-ról [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. Tudj meg többet a GGUF-ről [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Nyilatkozat:**  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hivatalos forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy helytelen értelmezésekért.