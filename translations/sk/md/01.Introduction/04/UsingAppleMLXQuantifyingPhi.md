<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-09T13:49:53+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "sk"
}
-->
# **Kvantizácia Phi-3.5 pomocou Apple MLX Frameworku**

MLX je framework pre strojové učenie na Apple silicii, vytvorený výskumníkmi Apple v oblasti strojového učenia.

MLX je navrhnutý výskumníkmi strojového učenia pre výskumníkov strojového učenia. Framework je užívateľsky prívetivý, no zároveň efektívny na trénovanie a nasadzovanie modelov. Jeho dizajn je konceptuálne jednoduchý. Cieľom je umožniť výskumníkom ľahko rozširovať a vylepšovať MLX, aby mohli rýchlo skúmať nové nápady.

LLM modely je možné zrýchliť na zariadeniach Apple Silicon pomocou MLX a modely je možné pohodlne spúšťať lokálne.

Teraz Apple MLX Framework podporuje konverziu kvantizácie pre Phi-3.5-Instruct (**podpora Apple MLX Frameworku**), Phi-3.5-Vision (**podpora MLX-VLM Frameworku**) a Phi-3.5-MoE (**podpora Apple MLX Frameworku**). Poďme to vyskúšať:

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

### **🤖 Príklady pre Phi-3.5 s Apple MLX**

| Laboratóriá    | Úvod | Spustiť |
| -------- | ------- |  ------- |
| 🚀 Lab-Úvod Phi-3.5 Instruct  | Naučte sa, ako používať Phi-3.5 Instruct s Apple MLX frameworkom   |  [Spustiť](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Úvod Phi-3.5 Vision (obrázok) | Naučte sa, ako používať Phi-3.5 Vision na analýzu obrázkov s Apple MLX frameworkom     |  [Spustiť](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Úvod Phi-3.5 Vision (moE)   | Naučte sa, ako používať Phi-3.5 MoE s Apple MLX frameworkom  |  [Spustiť](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Zdroje**

1. Viac o Apple MLX Frameworku [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub repozitár [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub repozitár [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.