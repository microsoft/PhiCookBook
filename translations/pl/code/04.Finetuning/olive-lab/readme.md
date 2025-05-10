<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-05-09T04:37:21+00:00",
  "source_file": "code/04.Finetuning/olive-lab/readme.md",
  "language_code": "pl"
}
-->
# Lab. Optymalizacja modeli AI do inferencji na urządzeniu

## Wprowadzenie

> [!IMPORTANT]
> To laboratorium wymaga **karty graficznej Nvidia A10 lub A100** z odpowiednimi sterownikami i zainstalowanym zestawem narzędzi CUDA (wersja 12+).

> [!NOTE]
> To jest **35-minutowe** laboratorium, które pozwoli Ci praktycznie poznać podstawowe koncepcje optymalizacji modeli do inferencji na urządzeniu za pomocą OLIVE.

## Cele nauki

Pod koniec tego laboratorium będziesz potrafił używać OLIVE do:

- Kwantyzacji modelu AI za pomocą metody kwantyzacji AWQ.
- Dostosowania modelu AI do konkretnego zadania.
- Generowania adapterów LoRA (modeli dostrojonych) dla efektywnej inferencji na urządzeniu przy użyciu ONNX Runtime.

### Czym jest Olive

Olive (*O*NNX *live*) to zestaw narzędzi do optymalizacji modeli wraz z towarzyszącym CLI, który pozwala na dystrybucję modeli dla ONNX runtime +++https://onnxruntime.ai+++ z zachowaniem jakości i wydajności.

![Olive Flow](../../../../../translated_images/olive-flow.e4682fa65f77777f49e884482fa8dd83eadcb90904fcb41a54093af85c330060.pl.png)

Wejściem do Olive jest zazwyczaj model PyTorch lub Hugging Face, a wyjściem zoptymalizowany model ONNX, który jest wykonywany na urządzeniu (docelowym środowisku wdrożeniowym) uruchamiającym ONNX runtime. Olive optymalizuje model pod kątem akceleratora AI (NPU, GPU, CPU) dostarczonego przez producenta sprzętu takiego jak Qualcomm, AMD, Nvidia czy Intel.

Olive wykonuje *workflow*, czyli uporządkowaną sekwencję poszczególnych zadań optymalizacji modelu zwanych *passes* – przykładowe passes to: kompresja modelu, przechwytywanie grafu, kwantyzacja, optymalizacja grafu. Każdy pass ma zestaw parametrów, które można dostroić, aby osiągnąć najlepsze metryki, np. dokładność i opóźnienie, oceniane przez odpowiedniego ewaluatora. Olive stosuje strategię przeszukiwania, która wykorzystuje algorytm do automatycznego dostrajania kolejno każdego pass lub zestawu passów.

#### Zalety Olive

- **Zmniejsza frustrację i czas** związany z ręcznym eksperymentowaniem metodami optymalizacji grafu, kompresji i kwantyzacji. Określ swoje wymagania dotyczące jakości i wydajności, a Olive automatycznie znajdzie najlepszy model dla Ciebie.
- **Ponad 40 wbudowanych komponentów do optymalizacji modeli**, obejmujących najnowsze techniki w kwantyzacji, kompresji, optymalizacji grafu i dostrajaniu.
- **Łatwe w użyciu CLI** do typowych zadań optymalizacji modeli. Na przykład: olive quantize, olive auto-opt, olive finetune.
- Wbudowane pakowanie i wdrażanie modeli.
- Obsługa generowania modeli dla **Multi LoRA serving**.
- Tworzenie workflow za pomocą YAML/JSON do koordynacji zadań optymalizacji i wdrażania modeli.
- Integracja z **Hugging Face** i **Azure AI**.
- Wbudowany mechanizm **cache’owania** pozwalający **oszczędzać koszty**.

## Instrukcje do laboratorium

> [!NOTE]
> Upewnij się, że masz skonfigurowany Azure AI Hub i Projekt oraz przygotowany obliczeniowy węzeł A100 zgodnie z Lab 1.

### Krok 0: Połącz się ze swoim Azure AI Compute

Połączysz się z Azure AI compute korzystając z funkcji zdalnej w **VS Code**.

1. Otwórz aplikację **VS Code** na swoim komputerze.
2. Otwórz **paletę poleceń** używając **Shift+Ctrl+P**.
3. W palecie poleceń wyszukaj **AzureML - remote: Connect to compute instance in New Window**.
4. Postępuj zgodnie z instrukcjami wyświetlanymi na ekranie, aby połączyć się z Compute. Będzie to wymagało wybrania subskrypcji Azure, grupy zasobów, projektu oraz nazwy Compute skonfigurowanej w Lab 1.
5. Po połączeniu z węzłem Azure ML Compute, informacja ta pojawi się w **lewym dolnym rogu Visual Code** `><Azure ML: Compute Name`

### Krok 1: Sklonuj repozytorium

W VS Code możesz otworzyć nowy terminal za pomocą **Ctrl+J** i sklonować to repozytorium:

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

Aby otworzyć VS Code w odpowiednim folderze, wykonaj następujące polecenie w terminalu, które otworzy nowe okno:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Alternatywnie możesz otworzyć folder, wybierając **Plik** > **Otwórz folder**.

### Krok 3: Zależności

Otwórz okno terminala w VS Code na swoim Azure AI Compute Instance (wskazówka: **Ctrl+J**) i wykonaj poniższe polecenia, aby zainstalować zależności:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> Instalacja wszystkich zależności zajmie około 5 minut.

W tym laboratorium pobierzesz i załadujesz modele do katalogu modeli Azure AI. Aby mieć dostęp do katalogu modeli, musisz zalogować się do Azure używając:

```bash
az login
```

> [!NOTE]
> Podczas logowania zostaniesz poproszony o wybranie subskrypcji. Upewnij się, że wybierasz tę przypisaną do tego laboratorium.

### Krok 4: Wykonaj polecenia Olive

Otwórz terminal w VS Code na swoim Azure AI Compute Instance (wskazówka: **Ctrl+J**) i upewnij się, że środowisko conda `olive-ai` jest aktywowane:

```bash
conda activate olive-ai
```

Następnie wykonaj poniższe polecenia Olive w linii poleceń.

1. **Sprawdź dane:** W tym przykładzie dostroisz model Phi-3.5-Mini, aby specjalizował się w odpowiadaniu na pytania związane z podróżami. Poniższy kod wyświetla pierwsze rekordy zestawu danych w formacie JSON lines:

    ```bash
    head data/data_sample_travel.jsonl
    ```
2. **Kwantyzuj model:** Przed treningiem modelu najpierw wykonaj kwantyzację za pomocą polecenia korzystającego z techniki zwanej Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ kwantyzuje wagi modelu uwzględniając aktywacje generowane podczas inferencji. Oznacza to, że proces kwantyzacji bierze pod uwagę rzeczywisty rozkład danych w aktywacjach, co pozwala lepiej zachować dokładność modelu w porównaniu do tradycyjnych metod kwantyzacji wag.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    Kwantyzacja AWQ zajmuje około **8 minut** i pozwala **zmniejszyć rozmiar modelu z ~7,5GB do ~2,5GB**.

    W tym laboratorium pokazujemy, jak wprowadzić modele z Hugging Face (np. `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` to polecenie dostraja kwantyzowany model. Kwantyzacja modelu *przed* dostrajaniem zamiast po nim daje lepszą dokładność, ponieważ proces dostrajania odzyskuje część utraty spowodowanej kwantyzacją.

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

    Dostrajanie (z 100 krokami) zajmuje około **6 minut**.

3. **Optymalizacja:** Po wytrenowaniu modelu zoptymalizuj go używając polecenia Olive `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` - w tym laboratorium użyjemy CPU.

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

### Krok 6: Załaduj model do Azure AI

Przesłanie modelu do repozytorium modeli Azure AI umożliwia udostępnianie go innym członkom zespołu oraz zarządzanie wersjami modelu. Aby przesłać model, uruchom poniższe polecenie:

> [!NOTE]
> Zaktualizuj wartości `{}` dla `resourceGroup` oraz nazwy projektu Azure AI i uruchom polecenie

```
az ml workspace show
```

Alternatywnie możesz przejść na +++ai.azure.com+++ i wybrać **management center** > **project** > **overview**

Zastąp `{}` nazwą swojej grupy zasobów oraz nazwy projektu Azure AI.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

Model przesłany możesz zobaczyć i wdrożyć pod adresem https://ml.azure.com/model/list

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym powinien być uważany za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.