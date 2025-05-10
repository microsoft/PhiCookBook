<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-05-09T22:33:39+00:00",
  "source_file": "md/03.FineTuning/03.Inference/MLX_Inference.md",
  "language_code": "ro"
}
-->
# **Inferență Phi-3 cu Apple MLX Framework**

## **Ce este MLX Framework**

MLX este un framework pentru array-uri destinat cercetării în machine learning pe siliciul Apple, dezvoltat de echipa de cercetare în machine learning de la Apple.

MLX este creat de cercetători în machine learning pentru cercetători în machine learning. Framework-ul este conceput să fie ușor de folosit, dar în același timp eficient pentru antrenarea și implementarea modelelor. Designul framework-ului este, de asemenea, simplu din punct de vedere conceptual. Ne propunem să facilităm extinderea și îmbunătățirea MLX pentru a putea explora rapid idei noi.

Modelele LLM pot fi accelerate pe dispozitivele Apple Silicon prin MLX, iar modelele pot fi rulate local foarte comod.

## **Folosirea MLX pentru inferența Phi-3-mini**

### **1. Configurarea mediului MLX**

1. Python 3.11.x  
2. Instalarea librăriei MLX


```bash

pip install mlx-lm

```

### **2. Rularea Phi-3-mini în Terminal cu MLX**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Rezultatul (mediul meu este Apple M1 Max, 64GB) este

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.ro.png)

### **3. Cuantizarea Phi-3-mini cu MLX în Terminal**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note:*** Modelul poate fi cuantizat prin mlx_lm.convert, iar cuantizarea implicită este INT4. Acest exemplu cuantizează Phi-3-mini în INT4.

Modelul poate fi cuantizat prin mlx_lm.convert, iar cuantizarea implicită este INT4. În acest exemplu, Phi-3-mini este cuantizat în INT4. După cuantizare, modelul va fi salvat în directorul implicit ./mlx_model

Putem testa modelul cuantizat cu MLX din terminal


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Rezultatul este

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.ro.png)


### **4. Rularea Phi-3-mini cu MLX în Jupyter Notebook**


![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.ro.png)

***Note:*** Vă rugăm să consultați acest exemplu [click aici](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **Resurse**

1. Aflați mai multe despre Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Repozitoriu GitHub Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore)

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere automată AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un traducător uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.