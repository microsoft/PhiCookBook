<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-09-12T14:47:25+00:00",
  "source_file": "md/03.FineTuning/03.Inference/MLX_Inference.md",
  "language_code": "lt"
}
-->
# **Inference Phi-3 su Apple MLX Framework**

## **Kas yra MLX Framework**

MLX yra masyvo pagrindu sukurtas framework'as mašininio mokymosi tyrimams su Apple silicio technologija, sukurtas Apple mašininio mokymosi tyrimų komandos.

MLX sukurtas mašininio mokymosi tyrėjams, siekiant palengvinti jų darbą. Framework'as yra draugiškas vartotojui, tačiau tuo pačiu efektyvus modelių mokymui ir diegimui. Framework'o dizainas yra konceptualiai paprastas, todėl tyrėjams lengva jį plėsti ir tobulinti, siekiant greitai išbandyti naujas idėjas.

LLM modeliai gali būti paspartinti Apple silicio įrenginiuose naudojant MLX, o modelius galima patogiai paleisti vietoje.

## **Phi-3-mini inferencija naudojant MLX**

### **1. Paruoškite MLX aplinką**

1. Python 3.11.x
2. Įdiekite MLX biblioteką

```bash

pip install mlx-lm

```

### **2. Phi-3-mini paleidimas terminale su MLX**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Rezultatas (mano aplinka: Apple M1 Max, 64GB) yra:

![Terminal](../../../../../imgs/01/03/MLX/01.png)

### **3. Phi-3-mini kvantavimas su MLX terminale**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Pastaba:*** Modelis gali būti kvantuotas naudojant mlx_lm.convert, o numatytasis kvantavimas yra INT4. Šiame pavyzdyje Phi-3-mini kvantuojamas į INT4.

Modelis gali būti kvantuotas naudojant mlx_lm.convert, o numatytasis kvantavimas yra INT4. Šiame pavyzdyje Phi-3-mini kvantuojamas į INT4. Po kvantavimo modelis bus saugomas numatytame kataloge ./mlx_model.

Modelį, kvantuotą su MLX, galima išbandyti terminale.

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Rezultatas yra:

![INT4](../../../../../imgs/01/03/MLX/02.png)

### **4. Phi-3-mini paleidimas su MLX Jupyter Notebook'e**

![Notebook](../../../../../imgs/01/03/MLX/03.png)

***Pastaba:*** Prašome perskaityti šį pavyzdį [spustelėkite šią nuorodą](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **Resursai**

1. Sužinokite apie Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.