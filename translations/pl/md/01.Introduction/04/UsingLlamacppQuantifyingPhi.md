<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-09T14:09:10+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "pl"
}
-->
# **Kwantyzacja rodziny Phi za pomocą llama.cpp**

## **Czym jest llama.cpp**

llama.cpp to otwartoźródłowa biblioteka oprogramowania napisana głównie w C++, która umożliwia inferencję na różnych dużych modelach językowych (LLM), takich jak Llama. Jej głównym celem jest zapewnienie najnowocześniejszej wydajności inferencji LLM na szerokim spektrum sprzętu przy minimalnej konfiguracji. Dodatkowo, dostępne są powiązania Pythona dla tej biblioteki, oferujące wysokopoziomowe API do uzupełniania tekstu oraz serwer webowy kompatybilny z OpenAI.

Głównym celem llama.cpp jest umożliwienie inferencji LLM przy minimalnej konfiguracji i zapewnienie najnowocześniejszej wydajności na różnorodnym sprzęcie — lokalnie i w chmurze.

- Prosta implementacja w C/C++ bez żadnych zależności
- Apple silicon jest traktowany priorytetowo — zoptymalizowany przez ARM NEON, Accelerate i Metal
- Obsługa AVX, AVX2 oraz AVX512 dla architektur x86
- Kwantyzacja całkowitoliczbowa 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit i 8-bit dla szybszej inferencji i mniejszego zużycia pamięci
- Własne jądra CUDA do uruchamiania LLM na GPU NVIDIA (obsługa GPU AMD przez HIP)
- Obsługa backendów Vulkan i SYCL
- Hybrydowa inferencja CPU+GPU do częściowego przyspieszenia modeli większych niż całkowita pojemność VRAM

## **Kwantyzacja Phi-3.5 za pomocą llama.cpp**

Model Phi-3.5-Instruct można skwantyzować za pomocą llama.cpp, jednak Phi-3.5-Vision i Phi-3.5-MoE nie są jeszcze obsługiwane. Format konwertowany przez llama.cpp to gguf, który jest również najpowszechniej stosowanym formatem kwantyzacji.

Na Hugging Face dostępna jest duża liczba modeli w skwantyzowanym formacie GGUF. AI Foundry, Ollama i LlamaEdge korzystają z llama.cpp, dlatego modele GGUF są tam często wykorzystywane.

### **Czym jest GGUF**

GGUF to format binarny zoptymalizowany pod kątem szybkiego ładowania i zapisywania modeli, co czyni go bardzo efektywnym do celów inferencji. GGUF jest przeznaczony do użycia z GGML i innymi executorami. GGUF został opracowany przez @ggerganov, który jest również twórcą llama.cpp, popularnego frameworka do inferencji LLM w C/C++. Modele pierwotnie stworzone w takich frameworkach jak PyTorch można przekonwertować do formatu GGUF, aby używać ich z tymi silnikami.

### **ONNX vs GGUF**

ONNX to tradycyjny format uczenia maszynowego/głębokiego uczenia, dobrze wspierany przez różne frameworki AI i wykorzystywany w urządzeniach brzegowych. GGUF natomiast opiera się na llama.cpp i można powiedzieć, że powstał w erze GenAI. Oba mają podobne zastosowania. Jeśli zależy Ci na lepszej wydajności w sprzęcie wbudowanym i warstwach aplikacji, ONNX może być lepszym wyborem. Jeśli natomiast korzystasz z pochodnych frameworków i technologii llama.cpp, GGUF może okazać się lepszy.

### **Kwantyzacja Phi-3.5-Instruct za pomocą llama.cpp**

**1. Konfiguracja środowiska**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kwantyzacja**

Konwersja Phi-3.5-Instruct do FP16 GGUF za pomocą llama.cpp


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Kwantyzacja Phi-3.5 do INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testowanie**

Zainstaluj llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Uwaga*** 

Jeśli używasz Apple Silicon, zainstaluj llama-cpp-python w ten sposób


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testowanie 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Zasoby**

1. Dowiedz się więcej o llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. Dowiedz się więcej o onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. Dowiedz się więcej o GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło wiarygodne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.