<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-09T13:51:03+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "sr"
}
-->
# **Kvantizacija Phi-3.5 korišćenjem Apple MLX Framework-a**

MLX je framework za mašinsko učenje na Apple silicijum uređajima, razvijen od strane Apple istraživača mašinskog učenja.

MLX je napravljen od strane istraživača mašinskog učenja za istraživače mašinskog učenja. Framework je osmišljen da bude jednostavan za korišćenje, a istovremeno efikasan za treniranje i primenu modela. Dizajn samog framework-a je takođe konceptualno jednostavan. Cilj nam je da olakšamo istraživačima da proširuju i unapređuju MLX kako bi brzo mogli da istražuju nove ideje.

LLM modeli mogu biti ubrzani na Apple Silicon uređajima pomoću MLX-a, a modeli se mogu vrlo lako pokretati lokalno.

Sada Apple MLX Framework podržava kvantizacionu konverziju Phi-3.5-Instruct (**Apple MLX Framework support**), Phi-3.5-Vision (**MLX-VLM Framework support**), i Phi-3.5-MoE (**Apple MLX Framework support**). Hajde da probate:

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

### **🤖 Primeri za Phi-3.5 sa Apple MLX**

| Laboratorije    | Uvod | Kreni |
| -------- | ------- |  ------- |
| 🚀 Lab-Uvod Phi-3.5 Instruct  | Naučite kako da koristite Phi-3.5 Instruct sa Apple MLX framework-om   |  [Kreni](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Uvod Phi-3.5 Vision (slika) | Naučite kako da koristite Phi-3.5 Vision za analizu slika sa Apple MLX framework-om     |  [Kreni](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Uvod Phi-3.5 Vision (moE)   | Naučite kako da koristite Phi-3.5 MoE sa Apple MLX framework-om  |  [Kreni](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Resursi**

1. Saznajte više o Apple MLX Framework-u [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub repozitorijum [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub repozitorijum [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, молимо имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Изворни документ на оригиналном језику треба сматрати ауторитетом. За критичне информације препоручује се професионални људски превод. Не сносимо одговорност за било каква неспоразума или погрешна тумачења настала коришћењем овог превода.