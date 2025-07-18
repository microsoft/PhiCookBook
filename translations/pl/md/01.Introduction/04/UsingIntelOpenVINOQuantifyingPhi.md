<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-07-16T22:01:24+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "pl"
}
-->
# **Kwotowanie Phi-3.5 za pomocą Intel OpenVINO**

Intel to najbardziej tradycyjny producent procesorów CPU z wieloma użytkownikami. Wraz z rozwojem uczenia maszynowego i głębokiego uczenia, Intel dołączył również do rywalizacji o przyspieszenie AI. Do inferencji modeli Intel wykorzystuje nie tylko GPU i CPU, ale także NPU.

Mamy nadzieję wdrożyć rodzinę Phi-3.x na urządzeniach końcowych, licząc na to, że stanie się ona najważniejszą częścią AI PC i Copilot PC. Ładowanie modelu na urządzeniu końcowym zależy od współpracy różnych producentów sprzętu. Ten rozdział koncentruje się głównie na scenariuszu zastosowania Intel OpenVINO jako modelu kwantowego.

## **Czym jest OpenVINO**

OpenVINO to otwartoźródłowy zestaw narzędzi do optymalizacji i wdrażania modeli głębokiego uczenia od chmury po urządzenia brzegowe. Przyspiesza inferencję głębokiego uczenia w różnych zastosowaniach, takich jak generatywna AI, wideo, audio i język, z modelami z popularnych frameworków, takich jak PyTorch, TensorFlow, ONNX i innych. Konwertuj i optymalizuj modele oraz wdrażaj je na różnych urządzeniach i środowiskach Intel®, lokalnie i na urządzeniach, w przeglądarce lub w chmurze.

Dzięki OpenVINO możesz szybko skwantować model GenAI na sprzęcie Intela i przyspieszyć referencyjny model.

Obecnie OpenVINO obsługuje konwersję kwantyzacji Phi-3.5-Vision oraz Phi-3.5 Instruct.

### **Konfiguracja środowiska**

Upewnij się, że zainstalowane są następujące zależności środowiskowe, to jest requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Kwotowanie Phi-3.5-Instruct za pomocą OpenVINO**

W terminalu uruchom ten skrypt

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Kwotowanie Phi-3.5-Vision za pomocą OpenVINO**

Uruchom ten skrypt w Pythonie lub Jupyter lab

```python

import requests
from pathlib import Path
from ov_phi3_vision import convert_phi3_model
import nncf

if not Path("ov_phi3_vision.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/ov_phi3_vision.py")
    open("ov_phi3_vision.py", "w").write(r.text)


if not Path("gradio_helper.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/gradio_helper.py")
    open("gradio_helper.py", "w").write(r.text)

if not Path("notebook_utils.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/utils/notebook_utils.py")
    open("notebook_utils.py", "w").write(r.text)



model_id = "microsoft/Phi-3.5-vision-instruct"
out_dir = Path("../model/phi-3.5-vision-128k-instruct-ov")
compression_configuration = {
    "mode": nncf.CompressWeightsMode.INT4_SYM,
    "group_size": 64,
    "ratio": 0.6,
}
if not out_dir.exists():
    convert_phi3_model(model_id, out_dir, compression_configuration)

```

### **🤖 Przykłady dla Phi-3.5 z Intel OpenVINO**

| Laboratoria    | Opis | Przejdź |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Naucz się, jak używać Phi-3.5 Instruct na swoim AI PC    |  [Przejdź](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (obraz) | Naucz się, jak używać Phi-3.5 Vision do analizy obrazów na swoim AI PC      |  [Przejdź](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (wideo)   | Naucz się, jak używać Phi-3.5 Vision do analizy wideo na swoim AI PC    |  [Przejdź](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Zasoby**

1. Dowiedz się więcej o Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Repozytorium Intel OpenVINO na GitHub [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.