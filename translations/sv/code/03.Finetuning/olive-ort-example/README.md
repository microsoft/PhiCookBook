<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:32:29+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "sv"
}
-->
# Fine-tune Phi3 med Olive

I det här exemplet kommer du att använda Olive för att:

1. Finjustera en LoRA-adapter för att klassificera fraser i Sad, Joy, Fear, Surprise.
1. Slå samman adaptervikterna med basmodellen.
1. Optimera och kvantisera modellen till `int4`.

Vi visar också hur du kan inferera den finjusterade modellen med ONNX Runtime (ORT) Generate API.

> **⚠️ För finjustering behöver du en lämplig GPU tillgänglig – till exempel en A10, V100, A100.**

## 💾 Installera

Skapa en ny Python-virtuell miljö (till exempel med `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Installera sedan Olive och beroenden för ett finjusteringsflöde:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Finjustera Phi3 med Olive  
[Olive-konfigurationsfilen](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) innehåller ett *workflow* med följande *steg*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

På en övergripande nivå kommer detta workflow att:

1. Finjustera Phi3 (i 150 steg, vilket du kan ändra) med data från [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Slå samman LoRA-adaptervikterna med basmodellen. Det ger dig en enda modellartefakt i ONNX-format.
1. Model Builder optimerar modellen för ONNX runtime *och* kvantiserar modellen till `int4`.

För att köra workflow, kör:

```bash
olive run --config phrase-classification.json
```

När Olive är klar finns din optimerade och finjusterade `int4` Phi3-modell i: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrera finjusterad Phi3 i din applikation

För att köra appen:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Svaret ska vara en enkel ordklassificering av frasen (Sad/Joy/Fear/Surprise).

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För viktig information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.