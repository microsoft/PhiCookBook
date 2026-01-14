<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e08ce816e23ad813244a09ca34ebb8ac",
  "translation_date": "2025-07-16T20:00:37+00:00",
  "source_file": "md/01.Introduction/03/AIPC_Inference.md",
  "language_code": "pl"
}
-->
# **Inference Phi-3 na AI PC**

Wraz z rozwojem generatywnej sztucznej inteligencji oraz poprawą możliwości sprzętowych urządzeń brzegowych, coraz więcej modeli generatywnej AI może być integrowanych z urządzeniami użytkowników w modelu Bring Your Own Device (BYOD). AI PC to jedne z takich urządzeń. Od 2024 roku Intel, AMD i Qualcomm współpracują z producentami komputerów, aby wprowadzić AI PC, które ułatwiają wdrażanie lokalnych modeli generatywnej AI poprzez modyfikacje sprzętowe. W tej dyskusji skupimy się na AI PC Intela i omówimy, jak wdrożyć Phi-3 na AI PC Intela.

### Czym jest NPU

NPU (Neural Processing Unit) to dedykowany procesor lub jednostka przetwarzająca w większym SoC, zaprojektowana specjalnie do przyspieszania operacji sieci neuronowych i zadań AI. W przeciwieństwie do ogólnego przeznaczenia CPU i GPU, NPU są zoptymalizowane pod kątem równoległego przetwarzania danych, co czyni je bardzo wydajnymi w obróbce ogromnych ilości multimediów, takich jak wideo i obrazy, oraz w przetwarzaniu danych dla sieci neuronowych. Szczególnie dobrze radzą sobie z zadaniami związanymi z AI, takimi jak rozpoznawanie mowy, rozmycie tła podczas rozmów wideo czy edycja zdjęć i filmów, np. wykrywanie obiektów.

## NPU a GPU

Chociaż wiele zadań AI i uczenia maszynowego jest wykonywanych na GPU, istnieje istotna różnica między GPU a NPU.  
GPU są znane ze swoich możliwości obliczeń równoległych, ale nie wszystkie GPU są równie efektywne poza przetwarzaniem grafiki. NPU natomiast są specjalnie zaprojektowane do złożonych obliczeń związanych z operacjami sieci neuronowych, co czyni je bardzo skutecznymi w zadaniach AI.

Podsumowując, NPU to matematyczne „mózgi”, które przyspieszają obliczenia AI i odgrywają kluczową rolę w nadchodzącej erze AI PC!

***Ten przykład oparty jest na najnowszym procesorze Intel Core Ultra***

## **1. Użycie NPU do uruchomienia modelu Phi-3**

Urządzenie Intel® NPU to akcelerator inferencji AI zintegrowany z procesorami Intel klienta, począwszy od generacji Intel® Core™ Ultra (dawniej znanej jako Meteor Lake). Umożliwia energooszczędne wykonywanie zadań sztucznych sieci neuronowych.

![Latency](../../../../../translated_images/pl/aipcphitokenlatency.2be14f04f30a3bf7.png)

![Latency770](../../../../../translated_images/pl/aipcphitokenlatency770.e923609a57c5d394.png)

**Intel NPU Acceleration Library**

Biblioteka Intel NPU Acceleration Library [https://github.com/intel/intel-npu-acceleration-library](https://github.com/intel/intel-npu-acceleration-library) to biblioteka Pythona zaprojektowana, aby zwiększyć wydajność Twoich aplikacji, wykorzystując moc Intel Neural Processing Unit (NPU) do wykonywania szybkich obliczeń na kompatybilnym sprzęcie.

Przykład Phi-3-mini na AI PC z procesorami Intel® Core™ Ultra.

![DemoPhiIntelAIPC](../../../../../imgs/01/03/AIPC/aipcphi3-mini.gif)

Zainstaluj bibliotekę Pythona za pomocą pip

```bash

   pip install intel-npu-acceleration-library

```

***Uwaga*** Projekt jest nadal w fazie rozwoju, ale model referencyjny jest już bardzo kompletny.

### **Uruchamianie Phi-3 z Intel NPU Acceleration Library**

Korzystając z akceleracji Intel NPU, ta biblioteka nie wpływa na tradycyjny proces kodowania. Wystarczy użyć tej biblioteki do kwantyzacji oryginalnego modelu Phi-3, np. FP16, INT8, INT4, na przykład:

```python
from transformers import AutoTokenizer, pipeline,TextStreamer
from intel_npu_acceleration_library import NPUModelForCausalLM, int4
from intel_npu_acceleration_library.compiler import CompilerConfig
import warnings

model_id = "microsoft/Phi-3-mini-4k-instruct"

compiler_conf = CompilerConfig(dtype=int4)
model = NPUModelForCausalLM.from_pretrained(
    model_id, use_cache=True, config=compiler_conf, attn_implementation="sdpa"
).eval()

tokenizer = AutoTokenizer.from_pretrained(model_id)

text_streamer = TextStreamer(tokenizer, skip_prompt=True)
```

Po pomyślnej kwantyzacji kontynuujemy wykonanie, aby wywołać NPU do uruchomienia modelu Phi-3.

```python
generation_args = {
   "max_new_tokens": 1024,
   "return_full_text": False,
   "temperature": 0.3,
   "do_sample": False,
   "streamer": text_streamer,
}

pipe = pipeline(
   "text-generation",
   model=model,
   tokenizer=tokenizer,
)

query = "<|system|>You are a helpful AI assistant.<|end|><|user|>Can you introduce yourself?<|end|><|assistant|>"

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    pipe(query, **generation_args)
```

Podczas wykonywania kodu możemy obserwować status pracy NPU w Menedżerze zadań

![NPU](../../../../../translated_images/pl/aipc_NPU.7a3cb6db47b377e1.png)

***Przykłady*** : [AIPC_NPU_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_NPU_DEMO.ipynb)

## **2. Użycie DirectML + ONNX Runtime do uruchomienia modelu Phi-3**

### **Czym jest DirectML**

[DirectML](https://github.com/microsoft/DirectML) to wysokowydajna, sprzętowo przyspieszona biblioteka DirectX 12 do uczenia maszynowego. DirectML zapewnia akcelerację GPU dla powszechnych zadań uczenia maszynowego na szerokim zakresie obsługiwanego sprzętu i sterowników, w tym wszystkich GPU obsługujących DirectX 12 od producentów takich jak AMD, Intel, NVIDIA i Qualcomm.

Używany samodzielnie, DirectML API to niskopoziomowa biblioteka DirectX 12, odpowiednia dla aplikacji wymagających wysokiej wydajności i niskich opóźnień, takich jak frameworki, gry i inne aplikacje czasu rzeczywistego. Bezproblemowa współpraca DirectML z Direct3D 12, niskie narzuty oraz zgodność sprzętowa czynią DirectML idealnym do przyspieszania uczenia maszynowego, gdy potrzebna jest zarówno wysoka wydajność, jak i niezawodność oraz przewidywalność wyników na różnych urządzeniach.

***Uwaga***: Najnowsza wersja DirectML obsługuje już NPU (https://devblogs.microsoft.com/directx/introducing-neural-processor-unit-npu-support-in-directml-developer-preview/)

### DirectML i CUDA pod względem możliwości i wydajności:

**DirectML** to biblioteka uczenia maszynowego opracowana przez Microsoft. Została stworzona, aby przyspieszyć zadania uczenia maszynowego na urządzeniach z Windows, w tym na komputerach stacjonarnych, laptopach i urządzeniach brzegowych.  
- Oparta na DX12: DirectML bazuje na DirectX 12 (DX12), co zapewnia szerokie wsparcie sprzętowe dla GPU, w tym NVIDIA i AMD.  
- Szersze wsparcie: Dzięki wykorzystaniu DX12, DirectML działa na każdym GPU obsługującym DX12, także na zintegrowanych GPU.  
- Przetwarzanie obrazów: DirectML przetwarza obrazy i inne dane za pomocą sieci neuronowych, co czyni go odpowiednim do zadań takich jak rozpoznawanie obrazów, wykrywanie obiektów i inne.  
- Łatwość konfiguracji: Konfiguracja DirectML jest prosta i nie wymaga specyficznych SDK czy bibliotek od producentów GPU.  
- Wydajność: W niektórych przypadkach DirectML działa bardzo dobrze i może być szybszy niż CUDA, zwłaszcza dla określonych zadań.  
- Ograniczenia: Jednak zdarzają się sytuacje, gdy DirectML jest wolniejszy, szczególnie przy dużych partiach float16.

**CUDA** to platforma obliczeniowa i model programowania równoległego firmy NVIDIA. Pozwala programistom wykorzystać moc GPU NVIDIA do obliczeń ogólnego przeznaczenia, w tym uczenia maszynowego i symulacji naukowych.  
- Specyficzne dla NVIDIA: CUDA jest ściśle zintegrowane z GPU NVIDIA i zaprojektowane specjalnie dla nich.  
- Wysoka optymalizacja: Zapewnia doskonałą wydajność dla zadań przyspieszanych przez GPU, zwłaszcza na sprzęcie NVIDIA.  
- Szerokie zastosowanie: Wiele frameworków i bibliotek uczenia maszynowego (np. TensorFlow, PyTorch) obsługuje CUDA.  
- Możliwość dostosowania: Programiści mogą precyzyjnie dostosować ustawienia CUDA do konkretnych zadań, co pozwala osiągnąć optymalną wydajność.  
- Ograniczenia: Jednak zależność od sprzętu NVIDIA może ograniczać kompatybilność z innymi GPU.

### Wybór między DirectML a CUDA

Wybór między DirectML a CUDA zależy od konkretnego zastosowania, dostępnego sprzętu i preferencji.  
Jeśli zależy Ci na szerszej kompatybilności i łatwości konfiguracji, DirectML może być dobrym wyborem. Natomiast jeśli posiadasz GPU NVIDIA i potrzebujesz maksymalnej wydajności, CUDA pozostaje silnym kandydatem. Podsumowując, oba rozwiązania mają swoje zalety i wady, dlatego warto rozważyć swoje potrzeby i dostępny sprzęt przed podjęciem decyzji.

### **Generatywna AI z ONNX Runtime**

W erze AI przenośność modeli AI jest bardzo ważna. ONNX Runtime umożliwia łatwe wdrażanie wytrenowanych modeli na różnych urządzeniach. Programiści nie muszą martwić się o framework inferencji i mogą korzystać z jednolitego API do wykonywania inferencji modeli. W erze generatywnej AI ONNX Runtime również przeprowadza optymalizację kodu (https://onnxruntime.ai/docs/genai/). Dzięki zoptymalizowanemu ONNX Runtime, skwantyzowany model generatywnej AI może być inferowany na różnych terminalach. W Generative AI z ONNX Runtime można korzystać z API modelu AI przez Python, C#, C/C++. Oczywiście wdrożenie na iPhone może wykorzystać API Generative AI z ONNX Runtime w C++.

[Przykładowy kod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx)

***kompilacja biblioteki generatywnej AI z ONNX Runtime***

```bash

winget install --id=Kitware.CMake  -e

git clone https://github.com/microsoft/onnxruntime.git

cd .\onnxruntime\

./build.bat --build_shared_lib --skip_tests --parallel --use_dml --config Release

cd ../

git clone https://github.com/microsoft/onnxruntime-genai.git

cd .\onnxruntime-genai\

mkdir ort

cd ort

mkdir include

mkdir lib

copy ..\onnxruntime\include\onnxruntime\core\providers\dml\dml_provider_factory.h ort\include

copy ..\onnxruntime\include\onnxruntime\core\session\onnxruntime_c_api.h ort\include

copy ..\onnxruntime\build\Windows\Release\Release\*.dll ort\lib

copy ..\onnxruntime\build\Windows\Release\Release\onnxruntime.lib ort\lib

python build.py --use_dml


```

**Instalacja biblioteki**

```bash

pip install .\onnxruntime_genai_directml-0.3.0.dev0-cp310-cp310-win_amd64.whl

```

Oto wynik działania

![DML](../../../../../translated_images/pl/aipc_DML.52a44180393ab491.png)

***Przykłady*** : [AIPC_DirectML_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_DirectML_DEMO.ipynb)

## **3. Użycie Intel OpenVino do uruchomienia modelu Phi-3**

### **Czym jest OpenVINO**

[OpenVINO](https://github.com/openvinotoolkit/openvino) to otwartoźródłowy zestaw narzędzi do optymalizacji i wdrażania modeli głębokiego uczenia. Zapewnia przyspieszenie wydajności modeli wizji komputerowej, audio i językowych z popularnych frameworków, takich jak TensorFlow, PyTorch i innych. Zacznij pracę z OpenVINO. OpenVINO może być również używane w połączeniu z CPU i GPU do uruchamiania modelu Phi-3.

***Uwaga***: Obecnie OpenVINO nie obsługuje NPU.

### **Instalacja biblioteki OpenVINO**

```bash

 pip install git+https://github.com/huggingface/optimum-intel.git

 pip install git+https://github.com/openvinotoolkit/nncf.git

 pip install openvino-nightly

```

### **Uruchamianie Phi-3 z OpenVINO**

Podobnie jak NPU, OpenVINO realizuje wywołanie modeli generatywnej AI poprzez uruchamianie modeli kwantyzowanych. Najpierw musimy skwantyzować model Phi-3 i wykonać kwantyzację modelu z poziomu wiersza poleceń za pomocą optimum-cli.

**INT4**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code ./openvinomodel/phi3/int4

```

**FP16**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format fp16 --trust-remote-code ./openvinomodel/phi3/fp16

```

konwertowany format wygląda tak

![openvino_convert](../../../../../translated_images/pl/aipc_OpenVINO_convert.9e6360b65331ffca.png)

Wczytujemy ścieżki modelu (model_dir), powiązane konfiguracje (ov_config = {"PERFORMANCE_HINT": "LATENCY", "NUM_STREAMS": "1", "CACHE_DIR": ""}) oraz sprzętowo przyspieszone urządzenia (GPU.0) za pomocą OVModelForCausalLM

```python

ov_model = OVModelForCausalLM.from_pretrained(
     model_dir,
     device='GPU.0',
     ov_config=ov_config,
     config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
     trust_remote_code=True,
)

```

Podczas wykonywania kodu możemy obserwować status pracy GPU w Menedżerze zadań

![openvino_gpu](../../../../../translated_images/pl/aipc_OpenVINO_GPU.20180edfffd91e55.png)

***Przykłady*** : [AIPC_OpenVino_Demo.ipynb](../../../../../code/03.Inference/AIPC/AIPC_OpenVino_Demo.ipynb)

### ***Uwaga*** : Powyższe trzy metody mają swoje zalety, ale zaleca się korzystanie z akceleracji NPU do inferencji na AI PC.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.