# **Kwantyzacja rodziny Phi za pomocą rozszerzeń Generative AI dla onnxruntime**

## **Czym są rozszerzenia Generative AI dla onnxruntime**

Te rozszerzenia pomagają uruchamiać generatywną AI z ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Zapewniają pętlę generatywnej AI dla modeli ONNX, w tym inferencję z ONNX Runtime, przetwarzanie logitów, wyszukiwanie i próbkowanie oraz zarządzanie pamięcią podręczną KV. Programiści mogą wywołać wysokopoziomową metodę generate() lub uruchamiać każdą iterację modelu w pętli, generując po jednym tokenie na raz i opcjonalnie aktualizując parametry generowania wewnątrz pętli. Obsługuje wyszukiwanie zachłanne/beam search oraz próbkowanie TopP, TopK do generowania sekwencji tokenów oraz wbudowane przetwarzanie logitów, takie jak kary za powtórzenia. Można także łatwo dodać własne metody oceny.

Na poziomie aplikacji można używać rozszerzeń Generative AI dla onnxruntime do tworzenia aplikacji w C++/ C# / Python. Na poziomie modelu można je wykorzystać do łączenia wytrenowanych modeli i wykonywania związanych z tym ilościowych zadań wdrożeniowych.


## **Kwantyzacja Phi-3.5 za pomocą rozszerzeń Generative AI dla onnxruntime**

### **Obsługiwane modele**

Rozszerzenia Generative AI dla onnxruntime obsługują konwersję kwantyzacji modeli Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Model Builder w rozszerzeniach Generative AI dla onnxruntime**

Model Builder znacznie przyspiesza tworzenie zoptymalizowanych i skwantyzowanych modeli ONNX, które działają z API generate() ONNX Runtime.

Za pomocą Model Builder możesz skwantyzować model do INT4, INT8, FP16, FP32 oraz łączyć różne metody przyspieszenia sprzętowego, takie jak CPU, CUDA, DirectML, Mobile itd.

Aby korzystać z Model Builder, musisz zainstalować

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Po instalacji możesz uruchomić skrypt Model Builder z terminala, aby przeprowadzić konwersję formatu modelu i kwantyzację.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Zrozum odpowiednie parametry

1. **model_name** To jest model na Hugging Face, taki jak microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct itp. Może to być także ścieżka, gdzie przechowujesz model

2. **path_to_output_folder** Ścieżka do zapisu skonwertowanego modelu skwantyzowanego

3. **execution_provider** Wsparcie różnych przyspieszeń sprzętowych, takich jak cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Pobieramy model z Hugging Face i buforujemy lokalnie




***Uwaga：*** <ul>Chociaż rozszerzenia Generative AI dla onnxruntime są w wersji zapoznawczej, zostały włączone do Microsoft Olive i możesz też wywoływać funkcje Model Builder rozszerzeń Generative AI dla onnxruntime przez Microsoft Olive.</ul>

## **Jak używać Model Builder do kwantyzacji Phi-3.5**

Model Builder obecnie wspiera kwantyzację modelu ONNX dla Phi-3.5 Instruct i Phi-3.5-Vision

### **Phi-3.5-Instruct**


**Konwersja przyspieszona na CPU w kwantyzacji INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Konwersja przyspieszona CUDA w kwantyzacji INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Ustaw środowisko w terminalu

```bash

mkdir models

cd models 

```

2. Pobierz microsoft/Phi-3.5-vision-instruct do folderu models
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Proszę pobrać te pliki do swojego folderu Phi-3.5-vision-instruct

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Pobierz ten plik do folderu models
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Przejdź do terminala

    Konwersja wsparcia ONNX z FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Uwaga：**

1. Model Builder obecnie wspiera konwersję Phi-3.5-Instruct oraz Phi-3.5-Vision, ale nie Phi-3.5-MoE

2. Aby korzystać z kwantyzowanego modelu ONNX, możesz używać go poprzez SDK rozszerzeń Generative AI dla onnxruntime

3. Powinniśmy brać pod uwagę bardziej odpowiedzialną AI, więc po konwersji kwantyzacji modelu zalecane jest przeprowadzenie skuteczniejszych testów wyników

4. Kwantyzując model CPU INT4, możemy go wdrożyć na urządzeniu brzegowym (Edge Device), które ma lepsze scenariusze zastosowań, dlatego zakończyliśmy proces dla Phi-3.5-Instruct wokół INT 4


## **Zasoby**

1. Dowiedz się więcej o rozszerzeniach Generative AI dla onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Repozytorium GitHub rozszerzeń Generative AI dla onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->