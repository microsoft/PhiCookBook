# **Phi perekonna kvantiseerimine kasutades llama.cpp**

## **Mis on llama.cpp**

llama.cpp on avatud lähtekoodiga tarkvararaamatukogu, mis on peamiselt kirjutatud C++ keeles ja võimaldab järeldusi erinevatel suurte keelemudelite (LLM) põhjal, nagu Llama. Selle peamine eesmärk on pakkuda tipptasemel jõudlust LLM-i järelduste tegemisel mitmesugustel riistvaradel minimaalse seadistusega. Lisaks on saadaval Pythoniga seotud liidesed, mis pakuvad kõrgetasemelist API-d tekstide täitmiseks ja OpenAI-ga ühilduvat veebiserverit.

llama.cpp peamine eesmärk on võimaldada LLM-i järeldusi minimaalse seadistusega ja tipptasemel jõudlust mitmesugustel riistvaradel - nii lokaalselt kui ka pilves.

- Lihtne C/C++ implementatsioon ilma sõltuvusteta
- Apple Silicon on esmaklassiline - optimeeritud ARM NEON-i, Accelerate'i ja Metal raamistikuga
- AVX, AVX2 ja AVX512 tugi x86 arhitektuuridele
- 1,5-bitine, 2-bitine, 3-bitine, 4-bitine, 5-bitine, 6-bitine ja 8-bitine täisarvude kvantiseerimine kiiremaks järelduseks ja väiksemaks mälukasutuseks
- Kohandatud CUDA tuumad LLM-ide käitamiseks NVIDIA GPU-del (tugi AMD GPU-dele HIP-i kaudu)
- Vulkan ja SYCL tagapõhja tugi
- CPU+GPU hübriidjäreldus mudelite osaliseks kiirendamiseks, mis on suuremad kui kogu VRAM-i maht

## **Phi-3.5 kvantiseerimine kasutades llama.cpp**

Phi-3.5-Instruct mudelit saab kvantiseerida kasutades llama.cpp, kuid Phi-3.5-Vision ja Phi-3.5-MoE ei ole veel toetatud. llama.cpp poolt konverteeritud formaat on gguf, mis on ka kõige laialdasemalt kasutatav kvantiseerimisformaat.

Hugging Face'is on saadaval suur hulk kvantiseeritud GGUF formaadis mudeleid. AI Foundry, Ollama ja LlamaEdge kasutavad llama.cpp-d, seega kasutatakse GGUF mudeleid sageli.

### **Mis on GGUF**

GGUF on binaarformaat, mis on optimeeritud mudelite kiireks laadimiseks ja salvestamiseks, muutes selle väga tõhusaks järelduste tegemiseks. GGUF on loodud kasutamiseks GGML-i ja teiste täituritega. GGUF-i arendas @ggerganov, kes on ka llama.cpp, populaarse C/C++ LLM-i järeldusraamistiku, arendaja. Algul PyTorchis arendatud mudeleid saab konverteerida GGUF formaati, et neid nendes mootorites kasutada.

### **ONNX vs GGUF**

ONNX on traditsiooniline masinõppe/sügavõppe formaat, mis on hästi toetatud erinevates AI raamistikudes ja millel on head kasutusstsenaariumid servaseadmetes. GGUF põhineb llama.cpp-l ja seda võib pidada GenAI ajastu produktiks. Mõlemal on sarnased kasutusalad. Kui soovite paremat jõudlust manustatud riistvaras ja rakenduse kihtides, võib ONNX olla teie valik. Kui kasutate llama.cpp-st tulenevat raamistikku ja tehnoloogiat, võib GGUF olla parem.

### **Phi-3.5-Instruct kvantiseerimine kasutades llama.cpp**

**1. Keskkonna seadistamine**

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantiseerimine**

Phi-3.5-Instruct konverteerimine FP16 GGUF formaati kasutades llama.cpp

```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5 kvantiseerimine INT4 formaati

```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testimine**

Paigaldage llama-cpp-python

```bash

pip install llama-cpp-python -U

```

***Märkus*** 

Kui kasutate Apple Siliconi, paigaldage llama-cpp-python järgmiselt

```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testimine 

```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```


## **Ressursid**

1. Lisateave llama.cpp kohta [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. Lisateave onnxruntime kohta [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. Lisateave GGUF kohta [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta arusaamatuste või valesti tõlgenduste eest, mis võivad tekkida selle tõlke kasutamise tõttu.