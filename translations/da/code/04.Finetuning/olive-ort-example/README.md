<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:45:35+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "da"
}
-->
# Finjuster Phi3 med Olive

I dette eksempel bruger du Olive til:

1. At finjustere en LoRA-adapter til at klassificere sætninger som Sad, Joy, Fear, Surprise.
1. At slå adaptervægtningerne sammen med basismodellen.
1. At optimere og kvantisere modellen til `int4`.

Vi viser dig også, hvordan du kan køre inference på den finjusterede model ved hjælp af ONNX Runtime (ORT) Generate API.

> **⚠️ Til finjustering skal du have en passende GPU tilgængelig - for eksempel en A10, V100, A100.**

## 💾 Installation

Opret et nyt Python virtuelt miljø (for eksempel med `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Installer derefter Olive og afhængighederne til en finjusteringsworkflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Finjuster Phi3 med Olive
[Olive konfigurationsfilen](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) indeholder et *workflow* med følgende *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Overordnet vil dette workflow:

1. Finjustere Phi3 (i 150 trin, som du kan ændre) ved hjælp af dataene fra [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Flette LoRA-adaptervægtningerne ind i basismodellen. Det giver dig en enkelt modelartefakt i ONNX-format.
1. Model Builder optimerer modellen til ONNX runtime *og* kvantiserer modellen til `int4`.

For at køre workflowet, kør:

```bash
olive run --config phrase-classification.json
```

Når Olive er færdig, finder du din optimerede `int4` finjusterede Phi3-model i: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrer den finjusterede Phi3 i din applikation

For at køre appen:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Svaret skal være en enkeltordsklassifikation af sætningen (Sad/Joy/Fear/Surprise).

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.