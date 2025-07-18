<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:52:22+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "pl"
}
-->
# **Używanie Microsoft Phi-3.5 tflite do tworzenia aplikacji na Androida**

To jest przykładowa aplikacja na Androida wykorzystująca modele Microsoft Phi-3.5 tflite.

## **📚 Wiedza**

Android LLM Inference API pozwala na uruchamianie dużych modeli językowych (LLM) całkowicie na urządzeniu w aplikacjach na Androida, co umożliwia wykonywanie szerokiego zakresu zadań, takich jak generowanie tekstu, wyszukiwanie informacji w formie naturalnego języka oraz streszczanie dokumentów. Zadanie to oferuje wbudowane wsparcie dla wielu modeli tekst-do-tekstu, dzięki czemu możesz zastosować najnowsze generatywne modele AI działające lokalnie w swoich aplikacjach na Androida.

Google AI Edge Torch to biblioteka Pythona, która wspiera konwersję modeli PyTorch do formatu .tflite, który następnie można uruchomić za pomocą TensorFlow Lite i MediaPipe. Umożliwia to tworzenie aplikacji na Androida, iOS oraz IoT, które mogą działać całkowicie lokalnie na urządzeniu. AI Edge Torch oferuje szerokie wsparcie dla CPU, a także początkowe wsparcie dla GPU i NPU. AI Edge Torch dąży do ścisłej integracji z PyTorch, opierając się na torch.export() i zapewniając dobre wsparcie dla operatorów Core ATen.

## **🪬 Wskazówki**

### **🔥 Konwersja Microsoft Phi-3.5 do formatu tflite**

0. Ten przykład jest przeznaczony dla Androida 14+

1. Zainstaluj Python 3.10.12

***Sugestia:*** użyj conda do stworzenia środowiska Pythona

2. Ubuntu 20.04 / 22.04 (skup się na [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Sugestia:*** użyj Azure Linux VM lub innej chmury do stworzenia środowiska

3. Przejdź do swojego terminala Linux i zainstaluj bibliotekę Pythona

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Pobierz Microsoft-3.5-Instruct z Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Konwertuj Microsoft Phi-3.5 do tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Konwersja Microsoft Phi-3.5 do pakietu Android Mediapipe**

najpierw zainstaluj mediapipe

```bash

pip install mediapipe

```

uruchom ten kod w [twoim notatniku](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

```python

import mediapipe as mp
from mediapipe.tasks.python.genai import bundler

config = bundler.BundleConfig(
    tflite_model='Your Phi-3.5 tflite model path',
    tokenizer_model='Your Phi-3.5 tokenizer model path',
    start_token='start_token',
    stop_tokens=[STOP_TOKENS],
    output_filename='Your Phi-3.5 task model path',
    enable_bytes_to_unicode_mapping=True or Flase,
)
bundler.create_bundle(config)

```

### **🔥 Wysyłanie modelu zadania na urządzenia Android za pomocą adb push**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Uruchamianie kodu na Androidzie**

![demo](../../../../../../translated_images/demo.06d5a4246f057d1be99ffad0cbf22f4ac0c41530774d51ff903cfaa1d3cd3c8e.pl.png)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.