<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "340bd4c009524ef84102b78d06eea735",
  "translation_date": "2025-04-04T12:12:36+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingAppleMLXQuantifyingPhi.md",
  "language_code": "mo"
}
-->
# **Quantizing Phi-3.5 using Apple MLX Framework**

MLX ye framework ke array ho jo Apple silicon par machine learning research ke liye banaya gaya hai, Apple machine learning research ke dwara prastut.

MLX ko machine learning researchers ke liye design kiya gaya hai, aur iska maksad hai ki yeh framework user-friendly ho, saath hi models ko efficiently train aur deploy karne mein madad kare. Framework ka design bhi conceptually simple hai. Hum yeh asha karte hain ki researchers MLX ko aasani se expand aur sudhar sakein, taaki naye vicharon par jaldi kaam kiya ja sake.

Apple Silicon devices par MLX ke madhyam se LLMs ko accelerate kiya ja sakta hai, aur models ko local taur par chalana kaafi convenient hai.

Ab Apple MLX Framework Phi-3.5-Instruct(**Apple MLX Framework support**), Phi-3.5-Vision(**MLX-VLM Framework support**) aur Phi-3.5-MoE(**Apple MLX Framework support**) ke quantization conversion ko support karta hai. Aaiye ise aage explore karte hain:

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

### **🤖 Samples for Phi-3.5 with Apple MLX**

| Labs    | Parichay | Jaayein |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Seekhein kaise Phi-3.5 Instruct ko Apple MLX framework ke saath istemal karte hain   |  [Jaayein](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Seekhein kaise Phi-3.5 Vision ko Apple MLX framework ke saath image analyze karne ke liye istemal karte hain     |  [Jaayein](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Seekhein kaise Phi-3.5 MoE ko Apple MLX framework ke saath istemal karte hain  |  [Jaayein](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Resources**

1. Apple MLX Framework ke baare mein seekhein [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

It seems like you want the text translated into "mo," but could you clarify what "mo" refers to? Are you referring to a specific language or dialect? For example, it could be shorthand for Maori, Mongolian, or something else entirely. Let me know, and I'd be happy to assist!