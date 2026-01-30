# **Kvantizácia Phi rodiny pomocou llama.cpp**

## **Čo je llama.cpp**

llama.cpp je open-source softvérová knižnica primárne napísaná v C++, ktorá vykonáva inferenciu na rôznych veľkých jazykových modeloch (LLM), ako je Llama. Jej hlavným cieľom je zabezpečiť špičkový výkon pri inferencii LLM na širokej škále hardvéru s minimálnou konfiguráciou. Okrem toho sú k dispozícii aj Python väzby pre túto knižnicu, ktoré ponúkajú vysokoúrovňové API pre dopĺňanie textu a OpenAI kompatibilný webový server.

Hlavným cieľom llama.cpp je umožniť inferenciu LLM s minimálnou konfiguráciou a špičkovým výkonom na rôznorodom hardvéri – lokálne aj v cloude.

- Čistá implementácia v C/C++ bez závislostí
- Apple silicon je plnohodnotne podporovaný – optimalizovaný cez ARM NEON, Accelerate a Metal frameworky
- Podpora AVX, AVX2 a AVX512 pre x86 architektúry
- Kvantizácia na 1,5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit a 8-bit celé čísla pre rýchlejšiu inferenciu a zníženú spotrebu pamäte
- Vlastné CUDA kernely pre spúšťanie LLM na NVIDIA GPU (podpora AMD GPU cez HIP)
- Podpora backendov Vulkan a SYCL
- Hybridná inferencia CPU+GPU na čiastočné zrýchlenie modelov väčších ako celková kapacita VRAM

## **Kvantizácia Phi-3.5 pomocou llama.cpp**

Model Phi-3.5-Instruct je možné kvantizovať pomocou llama.cpp, no Phi-3.5-Vision a Phi-3.5-MoE zatiaľ nie sú podporované. Formát, ktorý llama.cpp konvertuje, je gguf, čo je zároveň najpoužívanejší formát kvantizácie.

Na Hugging face je veľké množstvo kvantizovaných modelov vo formáte GGUF. AI Foundry, Ollama a LlamaEdge využívajú llama.cpp, preto sa GGUF modely často používajú aj tam.

### **Čo je GGUF**

GGUF je binárny formát optimalizovaný pre rýchle načítanie a ukladanie modelov, čo ho robí veľmi efektívnym pre inferenciu. GGUF je navrhnutý na použitie s GGML a ďalšími vykonávacími prostrediami. GGUF vyvinul @ggerganov, ktorý je zároveň vývojárom llama.cpp, populárneho C/C++ frameworku pre inferenciu LLM. Modely pôvodne vyvinuté vo frameworkoch ako PyTorch je možné konvertovať do formátu GGUF pre použitie s týmito enginmi.

### **ONNX vs GGUF**

ONNX je tradičný formát pre strojové učenie/hlboké učenie, ktorý je dobre podporovaný v rôznych AI frameworkoch a má dobré využitie na edge zariadeniach. GGUF je založený na llama.cpp a dá sa povedať, že vznikol v ére GenAI. Oba formáty majú podobné využitie. Ak chcete lepší výkon na zabudovanom hardvéri a aplikačných vrstvách, ONNX môže byť vaša voľba. Ak používate odvodený framework a technológie llama.cpp, potom môže byť lepší GGUF.

### **Kvantizácia Phi-3.5-Instruct pomocou llama.cpp**

**1. Konfigurácia prostredia**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantizácia**

Pomocou llama.cpp konvertujte Phi-3.5-Instruct do FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Kvantizácia Phi-3.5 na INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testovanie**

Nainštalujte llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Poznámka*** 

Ak používate Apple Silicon, nainštalujte llama-cpp-python takto


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testovanie 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Zdroje**

1. Viac o llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. Viac o onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. Viac o GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.