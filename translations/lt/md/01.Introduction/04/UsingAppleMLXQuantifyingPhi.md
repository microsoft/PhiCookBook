<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-09-12T14:52:18+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "lt"
}
-->
# **Phi-3.5 kvantavimas naudojant Apple MLX Framework**

MLX yra masyvo pagrindu sukurtas sisteminis įrankis mašininio mokymosi tyrimams su Apple silicio lustais, sukurtas Apple mašininio mokymosi tyrimų komandos.

MLX sukurtas mašininio mokymosi tyrėjams, siekiant palengvinti jų darbą. Šis sisteminis įrankis yra draugiškas vartotojui, tačiau tuo pačiu efektyvus modelių mokymui ir diegimui. Framework'o dizainas yra konceptualiai paprastas, todėl tyrėjams lengva jį plėsti ir tobulinti, siekiant greitai išbandyti naujas idėjas.

LLM modeliai gali būti paspartinti Apple silicio įrenginiuose naudojant MLX, o modelius galima patogiai paleisti vietoje.

Dabar Apple MLX Framework palaiko Phi-3.5-Instruct kvantavimo konversiją (**Apple MLX Framework palaikymas**), Phi-3.5-Vision (**MLX-VLM Framework palaikymas**) ir Phi-3.5-MoE (**Apple MLX Framework palaikymas**). Išbandykime tai:

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

### **🤖 Pavyzdžiai Phi-3.5 su Apple MLX**

| Laboratorijos | Aprašymas | Eiti |
| ------------- | --------- | ---- |
| 🚀 Laboratorija - Phi-3.5 Instruct pristatymas | Sužinokite, kaip naudoti Phi-3.5 Instruct su Apple MLX framework'u | [Eiti](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb) |
| 🚀 Laboratorija - Phi-3.5 Vision (vaizdas) pristatymas | Sužinokite, kaip naudoti Phi-3.5 Vision analizuojant vaizdus su Apple MLX framework'u | [Eiti](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb) |
| 🚀 Laboratorija - Phi-3.5 Vision (MoE) pristatymas | Sužinokite, kaip naudoti Phi-3.5 MoE su Apple MLX framework'u | [Eiti](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb) |

## **Resursai**

1. Sužinokite apie Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub repozitorija [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub repozitorija [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.