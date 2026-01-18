<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-07-16T21:05:46+00:00",
  "source_file": "md/01.Introduction/03/MLX_Inference.md",
  "language_code": "sl"
}
-->
# **Inferenca Phi-3 z Apple MLX Framework**

## **Kaj je MLX Framework**

MLX je ogrodje za strojno učenje na Apple silikonskih napravah, ki ga je razvila Apple raziskovalna skupina za strojno učenje.

MLX je zasnovan s strani raziskovalcev strojnega učenja za raziskovalce strojnega učenja. Ogrodje je namenjeno enostavni uporabi, hkrati pa učinkovito za treniranje in izvajanje modelov. Samo zasnovo ogrodja je tudi konceptualno preprosta. Želimo omogočiti raziskovalcem, da enostavno razširjajo in izboljšujejo MLX z namenom hitrega preizkušanja novih idej.

LLM-je je mogoče pospešiti na napravah Apple Silicon z uporabo MLX, modeli pa se lahko zelo priročno izvajajo lokalno.

## **Uporaba MLX za inferenco Phi-3-mini**

### **1. Nastavite svoje MLX okolje**

1. Python 3.11.x  
2. Namestite MLX knjižnico

```bash

pip install mlx-lm

```

### **2. Zagon Phi-3-mini v terminalu z MLX**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Rezultat (moje okolje je Apple M1 Max, 64GB) je

![Terminal](../../../../../translated_images/sl/01.5cf57df8f7407cf9.webp)

### **3. Kvantizacija Phi-3-mini z MLX v terminalu**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** Model je mogoče kvantizirati preko mlx_lm.convert, privzeta kvantizacija je INT4. Ta primer kvantizira Phi-3-mini v INT4.

Model je mogoče kvantizirati preko mlx_lm.convert, privzeta kvantizacija je INT4. Ta primer kvantizira Phi-3-mini v INT4. Po kvantizaciji bo shranjen v privzeti imenik ./mlx_model

Model kvantiziran z MLX lahko preizkusimo iz terminala

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Rezultat je

![INT4](../../../../../translated_images/sl/02.7b188681a8eadbc1.webp)

### **4. Zagon Phi-3-mini z MLX v Jupyter Notebooku**

![Notebook](../../../../../translated_images/sl/03.b9705a3a5aaa89f9.webp)

***Note:*** Prosimo, preberite ta primer [kliknite na to povezavo](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **Viri**

1. Spoznajte Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub repozitorij [https://github.com/ml-explore](https://github.com/ml-explore)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.