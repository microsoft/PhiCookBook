<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-05-09T22:31:29+00:00",
  "source_file": "md/03.FineTuning/03.Inference/MLX_Inference.md",
  "language_code": "pl"
}
-->
# **Inferencja Phi-3 z wykorzystaniem Apple MLX Framework**

## **Czym jest MLX Framework**

MLX to framework tablicowy do badań nad uczeniem maszynowym na Apple silicon, stworzony przez zespół badawczy Apple zajmujący się uczeniem maszynowym.

MLX został zaprojektowany przez badaczy uczenia maszynowego dla badaczy uczenia maszynowego. Framework ma być przyjazny dla użytkownika, a jednocześnie efektywny w trenowaniu i wdrażaniu modeli. Sama koncepcja frameworku jest również prosta. Naszym celem jest ułatwienie badaczom rozszerzania i ulepszania MLX, aby szybko eksplorować nowe pomysły.

Modele LLM można przyspieszyć na urządzeniach Apple Silicon dzięki MLX, a modele można wygodnie uruchamiać lokalnie.

## **Użycie MLX do inferencji Phi-3-mini**

### **1. Konfiguracja środowiska MLX**

1. Python 3.11.x  
2. Instalacja biblioteki MLX  


```bash

pip install mlx-lm

```

### **2. Uruchomienie Phi-3-mini w terminalu z MLX**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Wynik (moje środowisko to Apple M1 Max, 64GB) to

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.pl.png)

### **3. Kwantyzacja Phi-3-mini z MLX w terminalu**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** Model można poddać kwantyzacji za pomocą mlx_lm.convert, a domyślną kwantyzacją jest INT4. Ten przykład kwantyzuje Phi-3-mini do INT4.

Model można poddać kwantyzacji za pomocą mlx_lm.convert, a domyślną kwantyzacją jest INT4. W tym przykładzie Phi-3-mini jest kwantyzowany do INT4. Po kwantyzacji model zostanie zapisany w domyślnym katalogu ./mlx_model

Możemy przetestować model poddany kwantyzacji z MLX z poziomu terminala

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Wynik to

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.pl.png)

### **4. Uruchomienie Phi-3-mini z MLX w Jupyter Notebook**

![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.pl.png)

***Note:*** Proszę zapoznać się z tym przykładem [klikając ten link](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **Zasoby**

1. Dowiedz się więcej o Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Repozytorium Apple MLX na GitHub [https://github.com/ml-explore](https://github.com/ml-explore)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiążące. W przypadku informacji o istotnym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.