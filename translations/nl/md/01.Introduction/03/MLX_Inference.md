<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-05-09T12:15:49+00:00",
  "source_file": "md/01.Introduction/03/MLX_Inference.md",
  "language_code": "nl"
}
-->
# **Inference Phi-3 met Apple MLX Framework**

## **Wat is MLX Framework**

MLX is een array-framework voor machine learning onderzoek op Apple silicon, ontwikkeld door Apple machine learning onderzoek.

MLX is ontworpen door machine learning onderzoekers voor machine learning onderzoekers. Het framework is bedoeld om gebruiksvriendelijk te zijn, maar toch efficiënt om modellen te trainen en te implementeren. Het ontwerp van het framework zelf is ook conceptueel eenvoudig. We willen het onderzoekers gemakkelijk maken om MLX uit te breiden en te verbeteren, met als doel snel nieuwe ideeën te verkennen.

LLM’s kunnen worden versneld op Apple Silicon apparaten via MLX, en modellen kunnen heel gemakkelijk lokaal worden uitgevoerd.

## **MLX gebruiken om Phi-3-mini te infereren**

### **1. Stel je MLX-omgeving in**

1. Python 3.11.x  
2. Installeer MLX Library

```bash

pip install mlx-lm

```

### **2. Phi-3-mini draaien in Terminal met MLX**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Het resultaat (mijn omgeving is Apple M1 Max, 64GB) is

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.nl.png)

### **3. Phi-3-mini kwantiseren met MLX in Terminal**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** Het model kan worden gekwantiseerd via mlx_lm.convert, waarbij de standaard kwantisatie INT4 is. Dit voorbeeld kwantiseert Phi-3-mini naar INT4.

Het model kan worden gekwantiseerd via mlx_lm.convert, waarbij de standaard kwantisatie INT4 is. Dit voorbeeld kwantiseert Phi-3-mini naar INT4. Na kwantisatie wordt het opgeslagen in de standaardmap ./mlx_model

We kunnen het gekwantiseerde model met MLX vanuit de terminal testen

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Het resultaat is

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.nl.png)

### **4. Phi-3-mini draaien met MLX in Jupyter Notebook**

![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.nl.png)

***Note:*** Lees deze voorbeeld [klik op deze link](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **Resources**

1. Leer meer over Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.