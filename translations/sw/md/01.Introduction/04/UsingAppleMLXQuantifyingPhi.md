<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-09T13:48:49+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "sw"
}
-->
# **Kukokotoa Phi-3.5 kwa kutumia Apple MLX Framework**

MLX ni mfumo wa array kwa utafiti wa mashine ya kujifunza kwenye Apple silicon, uliotengenezwa na utafiti wa mashine ya kujifunza wa Apple.

MLX imetengenezwa na watafiti wa mashine ya kujifunza kwa ajili ya watafiti wa mashine ya kujifunza. Mfumo huu umebuniwa kuwa rafiki kwa mtumiaji, lakini bado wenye ufanisi wa kufundisha na kuendesha modeli. Ubunifu wa mfumo huu pia ni rahisi kifikra. Lengo letu ni kufanya iwe rahisi kwa watafiti kuongeza na kuboresha MLX ili kuchunguza haraka mawazo mapya.

LLMs zinaweza kuharakishwa kwenye vifaa vya Apple Silicon kupitia MLX, na modeli zinaweza kuendeshwa kwa urahisi kiasili.

Sasa Apple MLX Framework inaunga mkono mabadiliko ya quantization ya Phi-3.5-Instruct (**Apple MLX Framework support**), Phi-3.5-Vision (**MLX-VLM Framework support**), na Phi-3.5-MoE (**Apple MLX Framework support**). Hebu tujaribu ifuatayo:

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

### **🤖 Sampuli za Phi-3.5 na Apple MLX**

| Maabara | Utangulizi | Nenda |
| -------- | ------- | ------- |
| 🚀 Maabara-Utangulizi Phi-3.5 Instruct | Jifunze jinsi ya kutumia Phi-3.5 Instruct na Apple MLX framework | [Nenda](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb) |
| 🚀 Maabara-Utangulizi Phi-3.5 Vision (picha) | Jifunze jinsi ya kutumia Phi-3.5 Vision kuchambua picha kwa Apple MLX framework | [Nenda](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb) |
| 🚀 Maabara-Utangulizi Phi-3.5 Vision (moE) | Jifunze jinsi ya kutumia Phi-3.5 MoE na Apple MLX framework | [Nenda](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb) |

## **Rasilimali**

1. Jifunze kuhusu Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Repoti ya Apple MLX GitHub [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Repo ya MLX-VLM GitHub [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Kasi ya Kutojibu**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha kuaminika. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.