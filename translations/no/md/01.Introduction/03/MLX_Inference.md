<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-07-16T21:03:43+00:00",
  "source_file": "md/01.Introduction/03/MLX_Inference.md",
  "language_code": "no"
}
-->
# **Inferens Phi-3 med Apple MLX Framework**

## **Hva er MLX Framework**

MLX er et array-rammeverk for maskinlæringsforskning på Apple-silikon, utviklet av Apple maskinlæringsforskning.

MLX er designet av maskinlæringsforskere for maskinlæringsforskere. Rammeverket er ment å være brukervennlig, men samtidig effektivt for trening og distribusjon av modeller. Designet av rammeverket i seg selv er også konseptuelt enkelt. Vi ønsker å gjøre det lett for forskere å utvide og forbedre MLX med mål om raskt å utforske nye ideer.

LLMer kan akselereres på Apple Silicon-enheter gjennom MLX, og modeller kan kjøres lokalt på en veldig praktisk måte.

## **Bruke MLX til å inferere Phi-3-mini**

### **1. Sett opp ditt MLX-miljø**

1. Python 3.11.x  
2. Installer MLX-biblioteket


```bash

pip install mlx-lm

```

### **2. Kjøre Phi-3-mini i Terminal med MLX**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Resultatet (mitt miljø er Apple M1 Max, 64GB) er

![Terminal](../../../../../translated_images/no/01.5cf57df8f7407cf9.png)

### **3. Kvantisere Phi-3-mini med MLX i Terminal**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note:*** Modellen kan kvantiseres gjennom mlx_lm.convert, og standard kvantisering er INT4. Dette eksempelet kvantiserer Phi-3-mini til INT4.

Modellen kan kvantiseres gjennom mlx_lm.convert, og standard kvantisering er INT4. Dette eksempelet viser hvordan Phi-3-mini kvantiseres til INT4. Etter kvantisering lagres den i standardkatalogen ./mlx_model

Vi kan teste den kvantiserte modellen med MLX fra terminalen


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Resultatet er

![INT4](../../../../../translated_images/no/02.7b188681a8eadbc1.png)


### **4. Kjøre Phi-3-mini med MLX i Jupyter Notebook**


![Notebook](../../../../../translated_images/no/03.b9705a3a5aaa89f9.png)

***Note:*** Vennligst les dette eksempelet [klikk på denne lenken](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **Ressurser**

1. Lær om Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.