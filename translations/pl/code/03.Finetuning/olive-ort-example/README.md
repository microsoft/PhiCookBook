<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:31:57+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "pl"
}
-->
# Dostraja Phi3 za pomocą Olive

W tym przykładzie użyjesz Olive do:

1. Dostrajenia adaptera LoRA do klasyfikacji fraz na Sad, Joy, Fear, Surprise.  
1. Scalania wag adaptera z modelem bazowym.  
1. Optymalizacji i kwantyzacji modelu do `int4`.

Pokażemy też, jak wykonać inferencję dostrojonego modelu za pomocą ONNX Runtime (ORT) Generate API.

> **⚠️ Do dostrajania potrzebna będzie odpowiednia karta GPU – na przykład A10, V100, A100.**

## 💾 Instalacja

Utwórz nowe wirtualne środowisko Pythona (np. używając `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Następnie zainstaluj Olive oraz zależności potrzebne do workflow dostrajania:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Dostrajenie Phi3 za pomocą Olive
[Plik konfiguracyjny Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) zawiera *workflow* z następującymi *passami*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Na wysokim poziomie workflow:

1. Dostraja Phi3 (przez 150 kroków, które możesz zmienić) używając danych z [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).  
1. Scala wagi adaptera LoRA z modelem bazowym, tworząc pojedynczy artefakt modelu w formacie ONNX.  
1. Model Builder zoptymalizuje model pod ONNX Runtime *i* zakwantyzuje go do `int4`.

Aby uruchomić workflow, wykonaj:

```bash
olive run --config phrase-classification.json
```

Po zakończeniu przez Olive, zoptymalizowany i dostrojony model Phi3 w formacie `int4` będzie dostępny w: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integracja dostrojonego Phi3 z Twoją aplikacją

Aby uruchomić aplikację:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Odpowiedź powinna być pojedynczą klasyfikacją frazy (Sad/Joy/Fear/Surprise).

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy uważać za źródło autorytatywne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.