<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-05-09T12:17:59+00:00",
  "source_file": "md/01.Introduction/03/MLX_Inference.md",
  "language_code": "sw"
}
-->
# **Kutathmini Phi-3 na Mfumo wa Apple MLX**

## **Nini Mfumo wa MLX**

MLX ni mfumo wa safu kwa utafiti wa kujifunza mashine kwenye Apple silicon, unaotolewa na utafiti wa kujifunza mashine wa Apple.

MLX umeundwa na watafiti wa kujifunza mashine kwa ajili ya watafiti wa kujifunza mashine. Mfumo huu umebuniwa kuwa rahisi kwa mtumiaji, lakini bado wenye ufanisi wa kufundisha na kuendesha modeli. Muundo wa mfumo pia ni rahisi kifikra. Lengo letu ni kurahisisha watafiti kuongeza na kuboresha MLX kwa ajili ya kuchunguza haraka mawazo mapya.

LLMs zinaweza kuharakishwa kwenye vifaa vya Apple Silicon kupitia MLX, na modeli zinaweza kuendeshwa kwa urahisi kwa mtaa.

## **Kutumia MLX kutathmini Phi-3-mini**

### **1. Tengeneza mazingira yako ya MLX**

1. Python 3.11.x  
2. Sakinisha Maktaba ya MLX


```bash

pip install mlx-lm

```

### **2. Kuendesha Phi-3-mini kwenye Terminal kwa kutumia MLX**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Matokeo (mazingira yangu ni Apple M1 Max, 64GB) ni

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.sw.png)

### **3. Kupunguza ukubwa wa Phi-3-mini kwa MLX kwenye Terminal**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** Modeli inaweza kupunguzwa ukubwa kupitia mlx_lm.convert, na upunguzaji wa chaguo-msingi ni INT4. Mfano huu unapunguza Phi-3-mini hadi INT4

Modeli inaweza kupunguzwa ukubwa kupitia mlx_lm.convert, na upunguzaji wa chaguo-msingi ni INT4. Mfano huu ni kupunguza Phi-3-mini hadi INT4. Baada ya kupunguzwa, itahifadhiwa katika saraka ya chaguo-msingi ./mlx_model

Tunaweza kujaribu modeli iliyopunguzwa ukubwa kwa MLX kutoka terminal


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Matokeo ni

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.sw.png)


### **4. Kuendesha Phi-3-mini kwa MLX katika Jupyter Notebook**


![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.sw.png)

***Note:*** Tafadhali soma sampuli hii [click this link](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **Rasilimali**

1. Jifunze kuhusu Mfumo wa Apple MLX [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)

**Kionyesha**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuwa sahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu na ya binadamu inapendekezwa. Hatubeba dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.