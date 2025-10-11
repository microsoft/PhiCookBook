<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-10-11T11:51:48+00:00",
  "source_file": "md/03.FineTuning/03.Inference/MLX_Inference.md",
  "language_code": "et"
}
-->
# **Inference Phi-3 Apple MLX raamistikuga**

## **Mis on MLX raamistik**

MLX on masinõppe uurimiseks mõeldud raamistik Apple Siliconi seadmetele, mille on loonud Apple'i masinõppe uurimisrühm.

MLX on loodud masinõppe teadlaste poolt masinõppe teadlastele. Raamistik on kasutajasõbralik, kuid samas tõhus mudelite treenimiseks ja rakendamiseks. Raamistiku disain on kontseptuaalselt lihtne, et teadlastel oleks lihtne MLX-i laiendada ja täiustada, eesmärgiga kiiresti uusi ideid uurida.

LLM-e saab Apple Siliconi seadmetes MLX-i abil kiirendada ning mudeleid saab mugavalt lokaalselt käivitada.

## **Phi-3-mini inferents MLX-i abil**

### **1. MLX keskkonna seadistamine**

1. Python 3.11.x
2. MLX-i teegi installimine

```bash

pip install mlx-lm

```

### **2. Phi-3-mini käivitamine terminalis MLX-i abil**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Tulemus (minu keskkond: Apple M1 Max, 64GB) on:

![Terminal](../../../../../imgs/01/03/MLX/01.png)

### **3. Phi-3-mini kvantiseerimine MLX-i abil terminalis**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Märkus:*** Mudelit saab kvantiseerida mlx_lm.convert abil, vaikimisi kvantiseerimine on INT4. Selles näites kvantiseeritakse Phi-3-mini INT4-ks.

Mudel kvantiseeritakse mlx_lm.convert abil, vaikimisi kvantiseerimine on INT4. Selles näites kvantiseeritakse Phi-3-mini INT4-ks. Pärast kvantiseerimist salvestatakse mudel vaikimisi kataloogi ./mlx_model.

Kvantiseeritud mudelit saab testida MLX-i abil terminalis.

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Tulemus on:

![INT4](../../../../../imgs/01/03/MLX/02.png)

### **4. Phi-3-mini käivitamine MLX-i abil Jupyter Notebookis**

![Notebook](../../../../../imgs/01/03/MLX/03.png)

***Märkus:*** Palun tutvu selle näitega [klõpsa siia lingile](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **Ressursid**

1. Tutvu Apple MLX raamistikuga [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHubi repo [https://github.com/ml-explore](https://github.com/ml-explore)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.