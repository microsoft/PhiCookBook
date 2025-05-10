<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-05-09T12:14:27+00:00",
  "source_file": "md/01.Introduction/03/MLX_Inference.md",
  "language_code": "sv"
}
-->
# **Inferens Phi-3 med Apple MLX Framework**

## **Vad är MLX Framework**

MLX är ett array-ramverk för maskininlärningsforskning på Apple silicon, utvecklat av Apple maskininlärningsforskning.

MLX är designat av maskininlärningsforskare för maskininlärningsforskare. Ramverket är tänkt att vara användarvänligt, men ändå effektivt för att träna och distribuera modeller. Själva designen av ramverket är också konceptuellt enkel. Vi vill göra det enkelt för forskare att bygga ut och förbättra MLX med målet att snabbt utforska nya idéer.

LLM:er kan accelereras på Apple Silicon-enheter via MLX, och modeller kan köras lokalt på ett mycket smidigt sätt.

## **Använda MLX för att inferera Phi-3-mini**

### **1. Sätt upp din MLX-miljö**

1. Python 3.11.x  
2. Installera MLX Library  


```bash

pip install mlx-lm

```

### **2. Köra Phi-3-mini i Terminal med MLX**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Resultatet (min miljö är Apple M1 Max, 64GB) är

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.sv.png)

### **3. Kvantisera Phi-3-mini med MLX i Terminal**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** Modellen kan kvantiseras via mlx_lm.convert, och standardkvantiseringen är INT4. Detta exempel kvantiserar Phi-3-mini till INT4

Modellen kan kvantiseras via mlx_lm.convert, och standardkvantiseringen är INT4. Detta exempel visar hur Phi-3-mini kvantiseras till INT4. Efter kvantiseringen sparas den i standardmappen ./mlx_model

Vi kan testa den kvantiserade modellen med MLX från terminalen


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Resultatet är

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.sv.png)


### **4. Köra Phi-3-mini med MLX i Jupyter Notebook**


![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.sv.png)

***Note:*** Läs gärna detta exempel [click this link](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **Resurser**

1. Läs mer om Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För viktig information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.