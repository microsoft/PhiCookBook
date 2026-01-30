# **Quantiseren van Phi-3.5 met Apple MLX Framework**

MLX is een array-framework voor machine learning onderzoek op Apple silicon, ontwikkeld door Apple machine learning onderzoek.

MLX is ontworpen door machine learning onderzoekers voor machine learning onderzoekers. Het framework is bedoeld om gebruiksvriendelijk te zijn, maar toch efficiënt voor het trainen en inzetten van modellen. Het ontwerp van het framework zelf is ook conceptueel eenvoudig. We willen het onderzoekers gemakkelijk maken om MLX uit te breiden en te verbeteren, met als doel snel nieuwe ideeën te verkennen.

LLM's kunnen worden versneld op Apple Silicon apparaten via MLX, en modellen kunnen heel eenvoudig lokaal worden uitgevoerd.

Nu ondersteunt het Apple MLX Framework quantisatieconversie van Phi-3.5-Instruct (**Apple MLX Framework support**), Phi-3.5-Vision (**MLX-VLM Framework support**), en Phi-3.5-MoE (**Apple MLX Framework support**). Laten we het eens proberen:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 Voorbeelden voor Phi-3.5 met Apple MLX**

| Labs    | Introductie | Ga naar |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Leer hoe je Phi-3.5 Instruct gebruikt met het Apple MLX framework   |  [Ga naar](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Leer hoe je Phi-3.5 Vision gebruikt om afbeeldingen te analyseren met het Apple MLX framework     |  [Ga naar](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Leer hoe je Phi-3.5 MoE gebruikt met het Apple MLX framework  |  [Ga naar](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Resources**

1. Leer meer over Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Rep [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.