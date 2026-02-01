# **Phi család kvantálása llama.cpp-vel**

## **Mi az a llama.cpp**

A llama.cpp egy nyílt forráskódú szoftárkönyvtár, amely elsősorban C++ nyelven íródott, és különböző nagy nyelvi modelleken (LLM-ek), például a Llamán végez következtetést. Fő célja, hogy minimális beállítással csúcsteljesítményt nyújtson LLM következtetéshez széles körű hardvereken. Emellett elérhetők Python kötései is, amelyek magas szintű API-t biztosítanak szövegkiegészítéshez, valamint OpenAI-kompatibilis webszervert.

A llama.cpp fő célja, hogy minimális beállítással és csúcsteljesítménnyel tegye lehetővé az LLM következtetést különféle hardvereken – helyileg és felhőben egyaránt.

- Egyszerű C/C++ megvalósítás, függőségek nélkül
- Apple Silicon elsőrangú támogatása – optimalizálva ARM NEON, Accelerate és Metal keretrendszerekkel
- AVX, AVX2 és AVX512 támogatás x86 architektúrákon
- 1,5-bites, 2-bites, 3-bites, 4-bites, 5-bites, 6-bites és 8-bites egész szám kvantálás a gyorsabb következtetés és kisebb memóriahasználat érdekében
- Egyedi CUDA kernel-ek NVIDIA GPU-kon futtatáshoz (AMD GPU támogatás HIP-en keresztül)
- Vulkan és SYCL backend támogatás
- CPU+GPU hibrid következtetés a VRAM kapacitásánál nagyobb modellek részleges gyorsításához

## **Phi-3.5 kvantálása llama.cpp-vel**

A Phi-3.5-Instruct modellt lehet kvantálni llama.cpp-vel, de a Phi-3.5-Vision és Phi-3.5-MoE még nem támogatott. A llama.cpp által konvertált formátum a gguf, amely a legelterjedtebb kvantálási formátum is egyben.

Számos kvantált GGUF formátumú modell található a Hugging Face-en. Az AI Foundry, Ollama és LlamaEdge is a llama.cpp-re épít, így a GGUF modellek gyakran használatosak.

### **Mi az a GGUF**

A GGUF egy bináris formátum, amely gyors betöltést és mentést tesz lehetővé, így nagyon hatékony a következtetés során. A GGUF-t a GGML és más futtatók használatára tervezték. A GGUF-t @ggerganov fejlesztette, aki a llama.cpp fejlesztője is, egy népszerű C/C++ LLM következtetési keretrendszer. A PyTorch-hoz hasonló keretrendszerekben fejlesztett modellek átkonvertálhatók GGUF formátumba, hogy azokat ezekkel a motorokkal használhassuk.

### **ONNX vs GGUF**

Az ONNX egy hagyományos gépi tanulási/mélytanulási formátum, amelyet széles körben támogatnak különböző AI keretrendszerek, és jól használható élő eszközökön. A GGUF ezzel szemben a llama.cpp-re épül, és mondhatjuk, hogy a GenAI korszak terméke. Mindkettő hasonló célokra használható. Ha beágyazott hardveren és alkalmazási rétegekben jobb teljesítményt szeretnél, az ONNX lehet a jobb választás. Ha pedig a llama.cpp származtatott keretrendszerét és technológiáját használod, akkor a GGUF lehet előnyösebb.

### **Phi-3.5-Instruct kvantálása llama.cpp-vel**

**1. Környezet beállítása**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantálás**

Phi-3.5-Instruct konvertálása FP16 GGUF formátumba llama.cpp-vel


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

Ha Apple Silicon-t használsz, akkor a llama-cpp-python telepítése így történjen


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

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.