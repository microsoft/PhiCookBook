<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:44:58+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "pl"
}
-->
# Dostosuj Phi3 za pomocą Olive

W tym przykładzie użyjesz Olive, aby:

1. Dostosować adapter LoRA do klasyfikacji fraz na Sad, Joy, Fear, Surprise.  
1. Scalić wagi adaptera z modelem bazowym.  
1. Zoptymalizować i skwantyzować model do `int4`.

Pokażemy również, jak wykonać inferencję dostosowanego modelu za pomocą ONNX Runtime (ORT) Generate API.

> **⚠️ Do dostosowywania potrzebna będzie odpowiednia karta GPU – na przykład A10, V100, A100.**

## 💾 Instalacja

Utwórz nowe wirtualne środowisko Pythona (na przykład używając `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Następnie zainstaluj Olive oraz zależności potrzebne do procesu dostosowywania:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Dostosowanie Phi3 za pomocą Olive  
Plik konfiguracyjny [Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) zawiera *workflow* z następującymi *passami*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Na wysokim poziomie, ten workflow:

1. Dostosowuje Phi3 (przez 150 kroków, co możesz zmienić) na podstawie danych z [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).  
1. Scala wagi adaptera LoRA z modelem bazowym, tworząc pojedynczy artefakt modelu w formacie ONNX.  
1. Model Builder optymalizuje model pod ONNX runtime *i* kwantyzuje model do `int4`.

Aby uruchomić workflow, wykonaj:

```bash
olive run --config phrase-classification.json
```

Po zakończeniu Olive, zoptymalizowany i dostosowany model Phi3 w formacie `int4` będzie dostępny w: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integracja dostosowanego Phi3 z Twoją aplikacją

Aby uruchomić aplikację:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Odpowiedź powinna być pojedynczą klasyfikacją frazy (Sad/Joy/Fear/Surprise).

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najdokładniejsze, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiążące. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.