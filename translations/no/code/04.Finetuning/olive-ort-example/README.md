<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-16T16:26:52+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "no"
}
-->
# Finjuster Phi3 med Olive

I dette eksempelet skal du bruke Olive til å:

1. Finjustere en LoRA-adapter for å klassifisere setninger som Sad, Joy, Fear, Surprise.  
1. Slå sammen adaptervektene med basismodellen.  
1. Optimalisere og kvantisere modellen til `int4`.  

Vi viser deg også hvordan du kan kjøre inferens med den finjusterte modellen ved hjelp av ONNX Runtime (ORT) Generate API.

> **⚠️ For finjustering trenger du en egnet GPU tilgjengelig – for eksempel A10, V100, A100.**

## 💾 Installer

Opprett et nytt Python-virtuelt miljø (for eksempel med `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Deretter installerer du Olive og avhengighetene for en finjusteringsarbeidsflyt:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Finjuster Phi3 med Olive  
[Olive-konfigurasjonsfilen](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) inneholder en *workflow* med følgende *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

På et overordnet nivå vil denne arbeidsflyten:

1. Finjustere Phi3 (i 150 steg, som du kan endre) ved bruk av dataene i [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).  
1. Slå sammen LoRA-adaptervektene med basismodellen. Dette gir deg en enkelt modellfil i ONNX-format.  
1. Model Builder vil optimalisere modellen for ONNX runtime *og* kvantisere modellen til `int4`.  

For å kjøre arbeidsflyten, bruk:

```bash
olive run --config phrase-classification.json
```

Når Olive er ferdig, finner du den optimaliserte `int4` finjusterte Phi3-modellen her: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrer finjustert Phi3 i applikasjonen din

For å kjøre appen:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Svaret skal være en enkeltord-klassifisering av setningen (Sad/Joy/Fear/Surprise).

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.