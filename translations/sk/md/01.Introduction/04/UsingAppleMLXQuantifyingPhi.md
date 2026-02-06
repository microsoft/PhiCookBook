# **Kvantilizácia Phi-3.5 pomocou Apple MLX Frameworku**

MLX je framework pre strojové učenie na Apple silicium, vyvinutý výskumníkmi v oblasti strojového učenia v Apple.

MLX je navrhnutý výskumníkmi pre výskumníkov v oblasti strojového učenia. Framework je určený tak, aby bol používateľsky prívetivý, no zároveň efektívny pri trénovaní a nasadzovaní modelov. Koncepcia samotného frameworku je tiež jednoduchá. Naším cieľom je umožniť výskumníkom ľahko rozširovať a vylepšovať MLX, aby mohli rýchlo skúmať nové nápady.

LLM modely môžu byť zrýchlené na zariadeniach Apple Silicon pomocou MLX a modely je možné pohodlne spúšťať lokálne.

Teraz Apple MLX Framework podporuje konverziu kvantilizácie pre Phi-3.5-Instruct (**podpora Apple MLX Frameworku**), Phi-3.5-Vision (**podpora MLX-VLM Frameworku**) a Phi-3.5-MoE (**podpora Apple MLX Frameworku**). Poďme to vyskúšať:

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

### **🤖 Ukážky pre Phi-3.5 s Apple MLX**

| Laboratóriá    | Úvod | Spustiť |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Naučte sa, ako používať Phi-3.5 Instruct s Apple MLX frameworkom   |  [Spustiť](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (obrázok) | Naučte sa, ako používať Phi-3.5 Vision na analýzu obrázkov s Apple MLX frameworkom     |  [Spustiť](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Naučte sa, ako používať Phi-3.5 MoE s Apple MLX frameworkom  |  [Spustiť](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Zdroje**

1. Viac o Apple MLX Frameworku [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub repozitár [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub repozitár [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.