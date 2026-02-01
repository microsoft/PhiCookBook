# **Phi-3.5 kvantálása Apple MLX keretrendszerrel**

Az MLX egy tömbalapú keretrendszer gépi tanulási kutatásokhoz Apple szilíciumon, amelyet az Apple gépi tanulási kutatócsoportja fejlesztett.

Az MLX-et gépi tanulási kutatók tervezték gépi tanulási kutatók számára. A keretrendszer célja, hogy felhasználóbarát legyen, ugyanakkor hatékonyan lehessen vele modelleket tanítani és telepíteni. Maga a keretrendszer koncepciója is egyszerű. Az a célunk, hogy a kutatók könnyen bővíthessék és fejleszthessék az MLX-et, hogy gyorsan tudjanak új ötleteket kipróbálni.

Az LLM-ek Apple Silicon eszközökön az MLX segítségével gyorsíthatók, és a modellek helyben, kényelmesen futtathatók.

Most az Apple MLX keretrendszer támogatja a Phi-3.5-Instruct (**Apple MLX Framework support**), Phi-3.5-Vision (**MLX-VLM Framework support**) és Phi-3.5-MoE (**Apple MLX Framework support**) kvantálásra való átalakítását. Próbáljuk ki most:

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

### **🤖 Phi-3.5 minták Apple MLX keretrendszerrel**

| Laborok    | Bemutató | Indítás |
| -------- | ------- |  ------- |
| 🚀 Lab-Bemutató Phi-3.5 Instruct  | Ismerd meg, hogyan használd a Phi-3.5 Instruct modellt az Apple MLX keretrendszerrel   |  [Indítás](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Bemutató Phi-3.5 Vision (kép) | Tanuld meg, hogyan elemezd a képeket Phi-3.5 Vision modellel az Apple MLX keretrendszer segítségével     |  [Indítás](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Bemutató Phi-3.5 Vision (moE)   | Ismerd meg, hogyan használd a Phi-3.5 MoE modellt az Apple MLX keretrendszerrel  |  [Indítás](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Források**

1. Ismerd meg az Apple MLX keretrendszert [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub tárhely [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub tárhely [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.