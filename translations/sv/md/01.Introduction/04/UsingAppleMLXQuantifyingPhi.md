# **Kvantisering av Phi-3.5 med Apple MLX Framework**

MLX är ett array-ramverk för maskininlärningsforskning på Apple silicon, utvecklat av Apple machine learning research.

MLX är designat av maskininlärningsforskare för maskininlärningsforskare. Ramverket är tänkt att vara användarvänligt, men ändå effektivt för att träna och distribuera modeller. Själva designen av ramverket är också konceptuellt enkel. Vi vill göra det lätt för forskare att utöka och förbättra MLX med målet att snabbt kunna utforska nya idéer.

LLM:er kan accelereras på Apple Silicon-enheter via MLX, och modeller kan köras lokalt på ett mycket smidigt sätt.

Nu stödjer Apple MLX Framework kvantiseringskonvertering av Phi-3.5-Instruct (**Apple MLX Framework support**), Phi-3.5-Vision (**MLX-VLM Framework support**), och Phi-3.5-MoE (**Apple MLX Framework support**). Låt oss prova det härnäst:

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

### **🤖 Exempel för Phi-3.5 med Apple MLX**

| Labs    | Introduktion | Gå till |
| -------- | ----------- | ------- |
| 🚀 Lab-Introduktion Phi-3.5 Instruct  | Lär dig hur du använder Phi-3.5 Instruct med Apple MLX framework   |  [Gå till](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduktion Phi-3.5 Vision (bild) | Lär dig hur du använder Phi-3.5 Vision för att analysera bilder med Apple MLX framework     |  [Gå till](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduktion Phi-3.5 Vision (moE)   | Lär dig hur du använder Phi-3.5 MoE med Apple MLX framework  |  [Gå till](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Resurser**

1. Läs om Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.