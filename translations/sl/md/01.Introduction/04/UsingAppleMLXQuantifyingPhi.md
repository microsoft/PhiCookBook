<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-07-16T21:57:46+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "sl"
}
-->
# **Kvantilizacija Phi-3.5 z uporabo Apple MLX Frameworka**

MLX je ogrodje za strojno učenje na Apple silikonskih napravah, ki ga je razvila Apple raziskovalna skupina za strojno učenje.

MLX so zasnovali raziskovalci strojnega učenja za raziskovalce strojnega učenja. Ogrodje je namenjeno enostavni uporabi, hkrati pa učinkovito za treniranje in uvajanje modelov. Sam koncept ogrodja je prav tako preprost. Želimo omogočiti raziskovalcem, da zlahka razširjajo in izboljšujejo MLX, da bi hitro preizkušali nove ideje.

LLM-je je mogoče pospešiti na napravah Apple Silicon z MLX, modeli pa se lahko zelo priročno izvajajo lokalno.

Zdaj Apple MLX Framework podpira kvantilizacijo Phi-3.5-Instruct (**podpora Apple MLX Frameworka**), Phi-3.5-Vision (**podpora MLX-VLM Frameworka**) in Phi-3.5-MoE (**podpora Apple MLX Frameworka**). Poskusimo naslednje:

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

### **🤖 Primeri za Phi-3.5 z Apple MLX**

| Laboratorij    | Uvod | Pojdi |
| -------- | ------- |  ------- |
| 🚀 Lab-Uvod Phi-3.5 Instruct  | Naučite se, kako uporabljati Phi-3.5 Instruct z Apple MLX frameworkom   |  [Pojdi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Uvod Phi-3.5 Vision (slika) | Naučite se, kako uporabiti Phi-3.5 Vision za analizo slike z Apple MLX frameworkom     |  [Pojdi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Uvod Phi-3.5 Vision (moE)   | Naučite se, kako uporabljati Phi-3.5 MoE z Apple MLX frameworkom  |  [Pojdi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Viri**

1. Spoznajte Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub repozitorij [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub repozitorij [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.