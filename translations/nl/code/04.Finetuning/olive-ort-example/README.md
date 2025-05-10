<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:45:57+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "nl"
}
-->
# Fijn afstemmen van Phi3 met Olive

In dit voorbeeld gebruik je Olive om:

1. Een LoRA-adapter fijn af te stemmen om zinnen te classificeren als Sad, Joy, Fear, Surprise.
1. De adaptergewichten samen te voegen met het basismodel.
1. Het model te optimaliseren en te kwantiseren naar `int4`.

We laten je ook zien hoe je het fijn afgestemde model kunt gebruiken met de ONNX Runtime (ORT) Generate API.

> **⚠️ Voor het fijn afstemmen heb je een geschikte GPU nodig - bijvoorbeeld een A10, V100, A100.**

## 💾 Installeren

Maak een nieuwe Python virtuele omgeving aan (bijvoorbeeld met `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Installeer daarna Olive en de benodigde afhankelijkheden voor een fijn-afstemmingsworkflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fijn afstemmen van Phi3 met Olive
Het [Olive configuratiebestand](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) bevat een *workflow* met de volgende *stappen*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

In grote lijnen doet deze workflow het volgende:

1. Fijn afstemmen van Phi3 (voor 150 stappen, aan te passen) met de data uit [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. De LoRA adaptergewichten samenvoegen met het basismodel. Dit levert één modelbestand op in ONNX-formaat.
1. ModelBuilder optimaliseert het model voor de ONNX runtime *en* kwantiseert het model naar `int4`.

Om de workflow uit te voeren, voer je het volgende uit:

```bash
olive run --config phrase-classification.json
```

Wanneer Olive klaar is, vind je je geoptimaliseerde `int4` fijn afgestemde Phi3 model in: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integreer het fijn afgestemde Phi3 in je applicatie

Om de app te draaien:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

De respons is een classificatie van één woord van de zin (Sad/Joy/Fear/Surprise).

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.