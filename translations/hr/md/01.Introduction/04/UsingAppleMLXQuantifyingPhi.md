# **Kvantizacija Phi-3.5 pomoću Apple MLX Frameworka**

MLX je okvir za nizove namijenjen istraživanju strojnog učenja na Apple siliciju, razvijen od strane Apple istraživača strojnog učenja.

MLX su osmislili istraživači strojnog učenja za istraživače strojnog učenja. Okvir je dizajniran da bude jednostavan za korištenje, ali i učinkovit za treniranje i implementaciju modela. Sam dizajn okvira je također konceptualno jednostavan. Cilj nam je olakšati istraživačima proširivanje i poboljšavanje MLX-a kako bi brzo mogli isprobavati nove ideje.

LLM-ovi se mogu ubrzati na Apple Silicon uređajima putem MLX-a, a modeli se mogu vrlo jednostavno pokretati lokalno.

Sada Apple MLX Framework podržava konverziju kvantizacije za Phi-3.5-Instruct (**Apple MLX Framework podrška**), Phi-3.5-Vision (**MLX-VLM Framework podrška**) i Phi-3.5-MoE (**Apple MLX Framework podrška**). Isprobajmo to sljedeće:

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

### **🤖 Primjeri za Phi-3.5 s Apple MLX**

| Laboratorij | Uvod | Idi |
| -------- | ------- |  ------- |
| 🚀 Lab-Uvod u Phi-3.5 Instruct  | Nauči kako koristiti Phi-3.5 Instruct s Apple MLX frameworkom   |  [Idi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Uvod u Phi-3.5 Vision (slika) | Nauči kako koristiti Phi-3.5 Vision za analizu slika s Apple MLX frameworkom     |  [Idi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Uvod u Phi-3.5 Vision (moE)   | Nauči kako koristiti Phi-3.5 MoE s Apple MLX frameworkom  |  [Idi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Resursi**

1. Saznaj više o Apple MLX Frameworku [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub repozitorij [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub repozitorij [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.