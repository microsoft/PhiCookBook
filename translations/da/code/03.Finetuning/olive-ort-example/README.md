<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:32:36+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "da"
}
-->
# Finjuster Phi3 ved hjælp af Olive

I dette eksempel vil du bruge Olive til at:

1. Finjustere en LoRA-adapter til at klassificere sætninger som Sad, Joy, Fear, Surprise.  
1. Flette adaptervægtene ind i basismodellen.  
1. Optimere og kvantisere modellen til `int4`.

Vi vil også vise dig, hvordan du kan inferere den finjusterede model ved hjælp af ONNX Runtime (ORT) Generate API.

> **⚠️ For finjustering skal du have en egnet GPU til rådighed - for eksempel en A10, V100, A100.**

## 💾 Installation

Opret et nyt Python-virtuel miljø (for eksempel ved brug af `conda`):

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

## 🧪 Finjuster Phi3 ved hjælp af Olive
[Olive konfigurationsfilen](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) indeholder en *workflow* med følgende *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

På et overordnet niveau vil denne workflow:

1. Finjustere Phi3 (i 150 trin, som du kan ændre) ved brug af data fra [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).  
1. Flette LoRA adaptervægtene ind i basismodellen. Dette giver dig et enkelt modelartefakt i ONNX-formatet.  
1. Model Builder vil optimere modellen til ONNX runtime *og* kvantisere modellen til `int4`.

For at køre workflowen, kør:

```bash
olive run --config phrase-classification.json
```

Når Olive er færdig, vil din optimerede `int4` finjusterede Phi3-model være tilgængelig i: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrer den finjusterede Phi3 i din applikation

For at køre appen:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Dette svar skal være en enkeltordsklassificering af sætningen (Sad/Joy/Fear/Surprise).

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.