<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-07-17T10:19:00+00:00",
  "source_file": "md/03.FineTuning/olive-lab/readme.md",
  "language_code": "pl"
}
-->
# Lab. Optymalizacja modeli AI do inferencji na urządzeniu

## Wprowadzenie

> [!IMPORTANT]
> To laboratorium wymaga **karty graficznej Nvidia A10 lub A100** z zainstalowanymi odpowiednimi sterownikami i zestawem narzędzi CUDA (wersja 12+).

> [!NOTE]
> To jest **35-minutowe** laboratorium, które pozwoli Ci praktycznie poznać podstawowe koncepcje optymalizacji modeli do inferencji na urządzeniu za pomocą OLIVE.

## Cele nauki

Po zakończeniu tego laboratorium będziesz potrafił używać OLIVE do:

- Kwantyzacji modelu AI metodą AWQ.
- Dostosowania modelu AI do konkretnego zadania.
- Generowania adapterów LoRA (modeli dostrojonych) do efektywnej inferencji na urządzeniu za pomocą ONNX Runtime.

### Czym jest Olive

Olive (*O*NNX *live*) to zestaw narzędzi do optymalizacji modeli wraz z towarzyszącym CLI, który umożliwia dostarczanie modeli dla środowiska ONNX runtime +++https://onnxruntime.ai+++ z zachowaniem jakości i wydajności.

![Olive Flow](../../../../../translated_images/olive-flow.5daf97340275f8b6.pl.png)

Wejściem do Olive jest zazwyczaj model PyTorch lub Hugging Face, a wyjściem jest zoptymalizowany model ONNX, który jest wykonywany na urządzeniu (docelowym środowisku wdrożeniowym) z uruchomionym ONNX runtime. Olive optymalizuje model pod kątem akceleratora AI (NPU, GPU, CPU) dostarczonego przez producenta sprzętu, takiego jak Qualcomm, AMD, Nvidia czy Intel.

Olive wykonuje *workflow*, czyli uporządkowaną sekwencję pojedynczych zadań optymalizacji modelu zwanych *passes* – przykładowe passes to: kompresja modelu, przechwytywanie grafu, kwantyzacja, optymalizacja grafu. Każdy pass ma zestaw parametrów, które można dostroić, aby osiągnąć najlepsze metryki, takie jak dokładność i opóźnienie, oceniane przez odpowiedni evaluator. Olive stosuje strategię wyszukiwania, która wykorzystuje algorytm do automatycznego dostrajania każdego passa pojedynczo lub zestawu passów razem.

#### Korzyści z Olive

- **Zmniejszenie frustracji i czasu** związanego z ręcznym eksperymentowaniem metodami optymalizacji grafu, kompresji i kwantyzacji. Określ swoje wymagania dotyczące jakości i wydajności, a Olive automatycznie znajdzie najlepszy model dla Ciebie.
- **Ponad 40 wbudowanych komponentów optymalizacji modeli** obejmujących najnowsze techniki kwantyzacji, kompresji, optymalizacji grafu i dostrajania.
- **Łatwe w użyciu CLI** do typowych zadań optymalizacji modeli, np. olive quantize, olive auto-opt, olive finetune.
- Wbudowane pakowanie i wdrażanie modeli.
- Obsługa generowania modeli do **Multi LoRA serving**.
- Tworzenie workflow za pomocą YAML/JSON do orkiestracji zadań optymalizacji i wdrażania modeli.
- Integracja z **Hugging Face** i **Azure AI**.
- Wbudowany mechanizm **cache’owania** pozwalający **oszczędzać koszty**.

## Instrukcje do laboratorium

> [!NOTE]
> Upewnij się, że masz skonfigurowany Azure AI Hub i projekt oraz ustawiony obliczeniowy węzeł A100 zgodnie z Lab 1.

### Krok 0: Połącz się z Azure AI Compute

Połączysz się z Azure AI compute za pomocą funkcji zdalnej w **VS Code**.

1. Otwórz aplikację **VS Code** na komputerze.
2. Otwórz **paletę poleceń** za pomocą **Shift+Ctrl+P**.
3. W palecie poleceń wyszukaj **AzureML - remote: Connect to compute instance in New Window**.
4. Postępuj zgodnie z instrukcjami na ekranie, aby połączyć się z Compute. Będzie to wymagało wybrania subskrypcji Azure, grupy zasobów, projektu i nazwy Compute, które ustawiłeś w Lab 1.
5. Po połączeniu z węzłem Azure ML Compute, jego nazwa pojawi się w **lewym dolnym rogu Visual Studio Code** jako `><Azure ML: Compute Name`.

### Krok 1: Sklonuj repozytorium

W VS Code otwórz nowy terminal za pomocą **Ctrl+J** i sklonuj to repozytorium:

W terminalu powinien pojawić się prompt

```
azureuser@computername:~/cloudfiles/code$ 
```  
Sklonuj rozwiązanie

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Krok 2: Otwórz folder w VS Code

Aby otworzyć VS Code w odpowiednim folderze, wykonaj poniższe polecenie w terminalu, co otworzy nowe okno:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Alternatywnie możesz otworzyć folder, wybierając **Plik** > **Otwórz folder**.

### Krok 3: Zależności

Otwórz terminal w VS Code na swoim Azure AI Compute Instance (skrót: **Ctrl+J**) i wykonaj poniższe polecenia, aby zainstalować zależności:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> Instalacja wszystkich zależności zajmie około 5 minut.

W tym laboratorium będziesz pobierać i przesyłać modele do katalogu modeli Azure AI. Aby uzyskać dostęp do katalogu modeli, musisz zalogować się do Azure za pomocą:

```bash
az login
```

> [!NOTE]
> Podczas logowania zostaniesz poproszony o wybranie subskrypcji. Upewnij się, że wybierasz subskrypcję przypisaną do tego laboratorium.

### Krok 4: Wykonaj polecenia Olive

Otwórz terminal w VS Code na swoim Azure AI Compute Instance (skrót: **Ctrl+J**) i upewnij się, że środowisko `olive-ai` jest aktywne:

```bash
conda activate olive-ai
```

Następnie wykonaj poniższe polecenia Olive w wierszu poleceń.

1. **Sprawdź dane:** W tym przykładzie dostroisz model Phi-3.5-Mini, aby specjalizował się w odpowiadaniu na pytania związane z podróżami. Poniższy kod wyświetla pierwsze rekordy zbioru danych w formacie JSON lines:

    ```bash
    head data/data_sample_travel.jsonl
    ```

2. **Kwantyzuj model:** Przed trenowaniem modelu najpierw wykonaj kwantyzację za pomocą polecenia wykorzystującego technikę Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ kwantyzuje wagi modelu, biorąc pod uwagę aktywacje generowane podczas inferencji. Oznacza to, że proces kwantyzacji uwzględnia rzeczywisty rozkład danych w aktywacjach, co pozwala lepiej zachować dokładność modelu w porównaniu do tradycyjnych metod kwantyzacji wag.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    Kwantyzacja AWQ zajmuje około **8 minut** i **zmniejsza rozmiar modelu z ~7,5GB do ~2,5GB**.

    W tym laboratorium pokazujemy, jak wprowadzać modele z Hugging Face (np. `microsoft/Phi-3.5-mini-instruct`). Olive pozwala również na wprowadzanie modeli z katalogu Azure AI, aktualizując argument `model_name_or_path` na identyfikator zasobu Azure AI (np. `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`).

3. **Trenuj model:** Następnie polecenie `olive finetune` dostraja skwantyzowany model. Kwantyzacja modelu *przed* dostrajaniem, a nie po nim, daje lepszą dokładność, ponieważ proces dostrajania odzyskuje część utraty spowodowanej kwantyzacją.

    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```

    Dostrajanie trwa około **6 minut** (100 kroków).

4. **Optymalizuj:** Po wytrenowaniu modelu zoptymalizuj go za pomocą polecenia `auto-opt` Olive, które przechwytuje graf ONNX i automatycznie wykonuje szereg optymalizacji poprawiających wydajność modelu na CPU poprzez kompresję i fuzje. Warto zauważyć, że możesz optymalizować również pod inne urządzenia, takie jak NPU czy GPU, zmieniając argumenty `--device` i `--provider` – jednak w tym laboratorium używamy CPU.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```

    Optymalizacja zajmuje około **5 minut**.

### Krok 5: Szybki test inferencji modelu

Aby przetestować inferencję modelu, utwórz w swoim folderze plik Python o nazwie **app.py** i wklej poniższy kod:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

Uruchom kod za pomocą:

```bash
python app.py
```

### Krok 6: Prześlij model do Azure AI

Przesłanie modelu do repozytorium modeli Azure AI umożliwia dzielenie się modelem z innymi członkami zespołu oraz zarządzanie wersjami modelu. Aby przesłać model, uruchom następujące polecenie:

> [!NOTE]
> Zaktualizuj miejsca `{}` nazwą swojej grupy zasobów i nazwą projektu Azure AI.

Aby znaleźć swoją grupę zasobów `"resourceGroup"` i nazwę projektu Azure AI, uruchom poniższe polecenie:

```
az ml workspace show
```

Lub przejdź na +++ai.azure.com+++ i wybierz **management center** > **project** > **overview**

Zaktualizuj miejsca `{}` nazwą swojej grupy zasobów i nazwą projektu Azure AI.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

Następnie możesz zobaczyć przesłany model i wdrożyć go pod adresem https://ml.azure.com/model/list

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.