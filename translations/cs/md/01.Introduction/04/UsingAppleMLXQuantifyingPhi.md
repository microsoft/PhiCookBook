<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-07-16T21:56:58+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "cs"
}
-->
# **Kvantilace Phi-3.5 pomocí Apple MLX Frameworku**

MLX je framework pro pole určený pro výzkum strojového učení na Apple silicon, vyvinutý týmem Apple machine learning research.

MLX je navržený výzkumníky strojového učení pro výzkumníky strojového učení. Framework je zamýšlen jako uživatelsky přívětivý, ale zároveň efektivní pro trénink a nasazení modelů. Design samotného frameworku je také konceptuálně jednoduchý. Naším cílem je usnadnit výzkumníkům rozšiřování a vylepšování MLX, aby mohli rychle zkoumat nové nápady.

LLM lze na zařízeních Apple Silicon zrychlit pomocí MLX a modely lze velmi pohodlně spouštět lokálně.

Nyní Apple MLX Framework podporuje konverzi kvantizace Phi-3.5-Instruct (**podpora Apple MLX Frameworku**), Phi-3.5-Vision (**podpora MLX-VLM Frameworku**) a Phi-3.5-MoE (**podpora Apple MLX Frameworku**). Pojďme to vyzkoušet:

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

### **🤖 Ukázky pro Phi-3.5 s Apple MLX**

| Labs    | Úvod | Spustit |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Naučte se, jak používat Phi-3.5 Instruct s Apple MLX frameworkem   |  [Spustit](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Naučte se, jak používat Phi-3.5 Vision k analýze obrázků s Apple MLX frameworkem     |  [Spustit](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Naučte se, jak používat Phi-3.5 MoE s Apple MLX frameworkem  |  [Spustit](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Zdroje**

1. Seznamte se s Apple MLX Frameworkem [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub repozitář [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub repozitář [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.