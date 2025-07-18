<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-07-16T21:56:42+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "sw"
}
-->
# **Kukokotoa Phi-3.5 kwa kutumia Apple MLX Framework**

MLX ni mfumo wa safu kwa ajili ya utafiti wa mashine kujifunza kwenye Apple silicon, uliotolewa na utafiti wa mashine kujifunza wa Apple.

MLX imeundwa na watafiti wa mashine kujifunza kwa ajili ya watafiti wa mashine kujifunza. Mfumo huu umebuniwa kuwa rahisi kwa mtumiaji, lakini bado wenye ufanisi wa kufundisha na kuendesha mifano. Muundo wa mfumo huu pia ni rahisi kimsingi. Tunakusudia kufanya iwe rahisi kwa watafiti kuongeza na kuboresha MLX kwa lengo la kuchunguza haraka mawazo mapya.

LLMs zinaweza kuharakishwa kwenye vifaa vya Apple Silicon kupitia MLX, na mifano inaweza kuendeshwa kwa urahisi mahali hapa.

Sasa Apple MLX Framework inaunga mkono mabadiliko ya kukokotoa ya Phi-3.5-Instruct (**Apple MLX Framework support**), Phi-3.5-Vision (**MLX-VLM Framework support**), na Phi-3.5-MoE (**Apple MLX Framework support**). Hebu tujaribu sasa:

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

| Maabara    | Utangulizi | Nenda |
| -------- | ------- |  ------- |
| 🚀 Maabara-Utangulizi Phi-3.5 Instruct  | Jifunze jinsi ya kutumia Phi-3.5 Instruct na mfumo wa Apple MLX   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Maabara-Utangulizi Phi-3.5 Vision (picha) | Jifunze jinsi ya kutumia Phi-3.5 Vision kuchambua picha kwa kutumia mfumo wa Apple MLX     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Maabara-Utangulizi Phi-3.5 Vision (moE)   | Jifunze jinsi ya kutumia Phi-3.5 MoE na mfumo wa Apple MLX  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Rasilimali**

1. Jifunze kuhusu Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Rep [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatuna wajibu wowote kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.