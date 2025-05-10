<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:32:58+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "nl"
}
-->
# Fine-tune Phi3 met Olive

In dit voorbeeld gebruik je Olive om:

1. Een LoRA-adapter fijn af te stemmen om zinnen te classificeren als Sad, Joy, Fear, Surprise.
1. De adaptergewichten samen te voegen met het basismodel.
1. Het model te optimaliseren en te kwantiseren naar `int4`.

We laten je ook zien hoe je het fijn afgestemde model kunt infereren met de ONNX Runtime (ORT) Generate API.

> **⚠️ Voor het fijn afstemmen heb je een geschikte GPU nodig - bijvoorbeeld een A10, V100, A100.**

## 💾 Installeren

Maak een nieuwe Python virtuele omgeving aan (bijvoorbeeld met `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Installeer daarna Olive en de afhankelijkheden voor een fijn afstemmingsworkflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fijn afstemmen van Phi3 met Olive
Het [Olive configuratiebestand](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) bevat een *workflow* met de volgende *stappen*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

In grote lijnen doet deze workflow het volgende:

1. Fijn afstemmen van Phi3 (voor 150 stappen, aanpasbaar) met de data uit [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. De LoRA-adaptergewichten samenvoegen met het basismodel. Dit levert één modelbestand op in ONNX-formaat.
1. Model Builder optimaliseert het model voor de ONNX runtime *en* kwantiseert het model naar `int4`.

Om de workflow uit te voeren, run je:

```bash
olive run --config phrase-classification.json
```

Als Olive klaar is, vind je je geoptimaliseerde en fijn afgestemde `int4` Phi3-model in: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integreer het fijn afgestemde Phi3 in je applicatie

Om de app te draaien:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

De output moet een eenduidige classificatie van de zin zijn (Sad/Joy/Fear/Surprise).

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.