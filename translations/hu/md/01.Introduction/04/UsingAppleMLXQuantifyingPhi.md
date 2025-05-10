<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-09T13:49:09+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "hu"
}
-->
# **Phi-3.5 kvantálása az Apple MLX keretrendszerrel**

Az MLX egy tömbalapú keretrendszer gépi tanulási kutatásokhoz Apple szilíciumon, az Apple gépi tanulási kutatócsapatától.

Az MLX-et gépi tanulási kutatók tervezték gépi tanulási kutatók számára. A keretrendszer felhasználóbarátnak készült, ugyanakkor hatékony a modellek tanításához és futtatásához. Maga a keretrendszer felépítése is koncepcionálisan egyszerű. Célunk, hogy a kutatók könnyen bővíthessék és fejleszthessék az MLX-et, hogy gyorsan kísérletezhessenek új ötletekkel.

A nagy nyelvi modellek (LLM-ek) Apple Silicon eszközökön az MLX segítségével gyorsíthatók, és a modellek kényelmesen futtathatók helyben.

Most az Apple MLX keretrendszer támogatja a Phi-3.5-Instruct (**Apple MLX Framework support**), Phi-3.5-Vision (**MLX-VLM Framework support**) és Phi-3.5-MoE (**Apple MLX Framework support**) kvantálásának átalakítását. Próbáljuk ki a következőket:

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

### **🤖 Minta példák Phi-3.5-höz az Apple MLX keretrendszerrel**

| Laborok | Bemutatás | Megnyitás |
| -------- | ------- | ------- |
| 🚀 Lab-Bemutató Phi-3.5 Instruct  | Ismerd meg, hogyan használható a Phi-3.5 Instruct az Apple MLX keretrendszerrel  |  [Megnyitás](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Bemutató Phi-3.5 Vision (kép) | Tanuld meg, hogyan elemezheted képeket a Phi-3.5 Vision segítségével az Apple MLX keretrendszerrel  |  [Megnyitás](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Bemutató Phi-3.5 Vision (moE)   | Ismerd meg a Phi-3.5 MoE használatát az Apple MLX keretrendszerrel  |  [Megnyitás](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Források**

1. Tudj meg többet az Apple MLX keretrendszerről [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub tároló [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub tároló [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum anyanyelvű változata tekintendő hiteles forrásnak. Fontos információk esetén javasolt szakmai, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.