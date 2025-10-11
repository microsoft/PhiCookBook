<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-10-11T12:26:08+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "et"
}
-->
# **Phi-3.5 kvantiseerimine Apple MLX raamistikuga**

MLX on masinõppe uurimiseks mõeldud massiivraamistik Apple'i silikoonil, mille on loonud Apple'i masinõppe uurimisrühm.

MLX on loodud masinõppe teadlaste poolt masinõppe teadlastele. Raamistik on mõeldud kasutajasõbralikuks, kuid samas tõhusaks mudelite treenimiseks ja juurutamiseks. Raamistiku disain on kontseptuaalselt lihtne, et teadlastel oleks lihtne MLX-i laiendada ja täiustada, eesmärgiga kiiresti uusi ideid uurida.

LLM-e saab Apple'i silikoonseadmetes MLX-i abil kiirendada ning mudeleid saab mugavalt kohapeal käivitada.

Nüüd toetab Apple MLX raamistik Phi-3.5-Instruct kvantiseerimise konversiooni (**Apple MLX Framework tugi**), Phi-3.5-Vision (**MLX-VLM Framework tugi**) ja Phi-3.5-MoE (**Apple MLX Framework tugi**). Proovime seda järgmisena:

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


### **🤖 Näidised Phi-3.5 jaoks Apple MLX-iga**

| Laborid    | Tutvustus | Mine |
| -------- | ------- |  ------- |
| 🚀 Lab-Tutvustus Phi-3.5 Instruct  | Õpi, kuidas kasutada Phi-3.5 Instructi Apple MLX raamistikuga   |  [Mine](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Tutvustus Phi-3.5 Vision (pilt) | Õpi, kuidas kasutada Phi-3.5 Visioni piltide analüüsimiseks Apple MLX raamistikuga     |  [Mine](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Tutvustus Phi-3.5 Vision (moE)   | Õpi, kuidas kasutada Phi-3.5 MoE-d Apple MLX raamistikuga  |  [Mine](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Ressursid**

1. Tutvu Apple MLX raamistikuga [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHubi repo [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHubi repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

---

**Vastutusest loobumine**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.