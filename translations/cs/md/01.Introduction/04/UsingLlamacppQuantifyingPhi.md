<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-07-16T22:11:46+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "cs"
}
-->
# **Kvantilace rodiny Phi pomocí llama.cpp**

## **Co je llama.cpp**

llama.cpp je open-source softwarová knihovna primárně napsaná v C++, která provádí inferenci na různých velkých jazykových modelech (LLM), jako je Llama. Jejím hlavním cílem je poskytovat špičkový výkon při inferenci LLM na široké škále hardwaru s minimální konfigurací. K dispozici jsou také Python bindingy, které nabízejí vysoce úrovňové API pro doplňování textu a webový server kompatibilní s OpenAI.

Hlavním cílem llama.cpp je umožnit inferenci LLM s minimální konfigurací a špičkovým výkonem na různorodém hardwaru – lokálně i v cloudu.

- Čistá implementace v C/C++ bez závislostí
- Apple silicon je plnohodnotně podporován – optimalizace pomocí ARM NEON, Accelerate a Metal frameworků
- Podpora AVX, AVX2 a AVX512 pro architektury x86
- Kvantizace na 1,5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit a 8-bit celá čísla pro rychlejší inferenci a snížení paměťové náročnosti
- Vlastní CUDA kernely pro běh LLM na NVIDIA GPU (podpora AMD GPU přes HIP)
- Podpora backendů Vulkan a SYCL
- Hybridní inference CPU+GPU pro částečné zrychlení modelů větších než celková kapacita VRAM

## **Kvantilace Phi-3.5 pomocí llama.cpp**

Model Phi-3.5-Instruct lze kvantizovat pomocí llama.cpp, ale Phi-3.5-Vision a Phi-3.5-MoE zatím nejsou podporovány. Formát, do kterého llama.cpp převádí, je gguf, což je také nejrozšířenější formát kvantizace.

Na Hugging Face je k dispozici velké množství kvantizovaných modelů ve formátu GGUF. AI Foundry, Ollama a LlamaEdge spoléhají na llama.cpp, takže modely GGUF jsou často využívány.

### **Co je GGUF**

GGUF je binární formát optimalizovaný pro rychlé načítání a ukládání modelů, což ho činí velmi efektivním pro inferenci. GGUF je navržen pro použití s GGML a dalšími vykonavateli. GGUF vyvinul @ggerganov, který je také autorem llama.cpp, populárního C/C++ frameworku pro inferenci LLM. Modely původně vyvinuté v rámci jako PyTorch lze převést do formátu GGUF pro použití s těmito enginy.

### **ONNX vs GGUF**

ONNX je tradiční formát pro strojové učení a hluboké učení, který je dobře podporován v různých AI frameworcích a má dobré využití v edge zařízeních. GGUF je založen na llama.cpp a dá se říct, že vznikl v éře GenAI. Oba mají podobné využití. Pokud chcete lepší výkon na embedded hardwaru a aplikačních vrstvách, může být ONNX vaší volbou. Pokud používáte odvozený framework a technologie llama.cpp, pak může být lepší GGUF.

### **Kvantilace Phi-3.5-Instruct pomocí llama.cpp**

**1. Konfigurace prostředí**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantizace**

Pomocí llama.cpp převést Phi-3.5-Instruct do FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Kvantilace Phi-3.5 na INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testování**

Nainstalujte llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Poznámka*** 

Pokud používáte Apple Silicon, nainstalujte llama-cpp-python takto


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testování 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Zdroje**

1. Více o llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. Více o onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. Více o GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.