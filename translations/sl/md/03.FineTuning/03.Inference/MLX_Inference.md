<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-05-09T22:34:07+00:00",
  "source_file": "md/03.FineTuning/03.Inference/MLX_Inference.md",
  "language_code": "sl"
}
-->
# **Inference Phi-3 s Apple MLX Framework**

## **Kaj je MLX Framework**

MLX je ogrodje za delo z matrikami za raziskave strojnega učenja na Apple siliciju, ki ga je razvila Apple raziskovalna skupina za strojno učenje.

MLX so zasnovali raziskovalci strojnega učenja za raziskovalce strojnega učenja. Ogrodje je namenjeno enostavni uporabi, hkrati pa učinkovito za treniranje in uporabo modelov. Njegova zasnova je tudi konceptualno preprosta. Želimo omogočiti raziskovalcem, da enostavno razširjajo in izboljšujejo MLX z namenom hitrega preizkušanja novih idej.

LLM-je je mogoče pospešiti na napravah Apple Silicon z MLX, modele pa lahko zelo priročno poganjate lokalno.

## **Uporaba MLX za inferenco Phi-3-mini**

### **1. Nastavitev MLX okolja**

1. Python 3.11.x  
2. Namestitev MLX knjižnice


```bash

pip install mlx-lm

```

### **2. Zagon Phi-3-mini v terminalu z MLX**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Rezultat (moje okolje je Apple M1 Max, 64GB) je

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.sl.png)

### **3. Kvantizacija Phi-3-mini z MLX v terminalu**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** Model je mogoče kvantizirati preko mlx_lm.convert, privzeta kvantizacija je INT4. Ta primer kvantizira Phi-3-mini v INT4.

Model je mogoče kvantizirati preko mlx_lm.convert, privzeta kvantizacija je INT4. Ta primer kvantizira Phi-3-mini v INT4. Po kvantizaciji se shrani v privzeto mapo ./mlx_model

Model kvantiziran z MLX lahko testiramo iz terminala


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Rezultat je

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.sl.png)


### **4. Zagon Phi-3-mini z MLX v Jupyter Notebooku**


![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.sl.png)

***Note:*** Prosim, preberite ta primer [kliknite tukaj](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **Viri**

1. Več o Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub repozitorij [https://github.com/ml-explore](https://github.com/ml-explore)

**Opozorilo**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.