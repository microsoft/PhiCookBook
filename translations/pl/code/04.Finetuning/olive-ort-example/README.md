<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-16T16:26:04+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "pl"
}
-->
# Dostosuj Phi3 za pomocą Olive

W tym przykładzie użyjesz Olive, aby:

1. Dostosować adapter LoRA do klasyfikacji fraz na Smutek, Radość, Strach, Zaskoczenie.  
1. Połączyć wagi adaptera z modelem bazowym.  
1. Zoptymalizować i skwantyzować model do `int4`.  

Pokażemy Ci również, jak wykonać inferencję dostosowanego modelu za pomocą ONNX Runtime (ORT) Generate API.

> **⚠️ Do dostosowywania potrzebna będzie odpowiednia karta GPU - na przykład A10, V100, A100.**

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

## 🧪 Dostosuj Phi3 za pomocą Olive  
[Plik konfiguracyjny Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) zawiera *workflow* z następującymi *etapami*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Na wysokim poziomie ten workflow:

1. Dostosuje Phi3 (przez 150 kroków, co możesz zmienić) używając danych z [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).  
1. Połączy wagi adaptera LoRA z modelem bazowym, tworząc pojedynczy artefakt modelu w formacie ONNX.  
1. Model Builder zoptymalizuje model pod ONNX runtime *oraz* skwantyzuje go do `int4`.  

Aby uruchomić workflow, wykonaj:

```bash
olive run --config phrase-classification.json
```

Po zakończeniu Olive, zoptymalizowany i dostosowany model Phi3 w formacie `int4` znajdziesz w: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Zintegruj dostosowany Phi3 z Twoją aplikacją

Aby uruchomić aplikację:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Odpowiedź powinna być pojedynczą klasyfikacją frazy (Smutek/Radość/Strach/Zaskoczenie).

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło wiarygodne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.