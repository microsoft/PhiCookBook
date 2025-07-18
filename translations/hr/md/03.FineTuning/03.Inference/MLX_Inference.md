<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-07-17T10:09:45+00:00",
  "source_file": "md/03.FineTuning/03.Inference/MLX_Inference.md",
  "language_code": "hr"
}
-->
# **Inferencija Phi-3 s Apple MLX Frameworkom**

## **Što je MLX Framework**

MLX je framework za rad s nizovima podataka namijenjen istraživanju strojnog učenja na Apple siliciju, razvijen od strane Apple istraživača strojnog učenja.

MLX su osmislili istraživači strojnog učenja za istraživače strojnog učenja. Framework je dizajniran da bude jednostavan za korištenje, ali i učinkovit za treniranje i implementaciju modela. Sam dizajn frameworka je također konceptualno jednostavan. Cilj nam je omogućiti istraživačima da lako proširuju i unapređuju MLX kako bi brzo mogli isprobavati nove ideje.

LLM modeli mogu se ubrzati na Apple Silicon uređajima pomoću MLX-a, a modeli se mogu vrlo jednostavno pokretati lokalno.

## **Korištenje MLX-a za inferenciju Phi-3-mini**

### **1. Postavljanje MLX okruženja**

1. Python 3.11.x  
2. Instalirajte MLX biblioteku

```bash

pip install mlx-lm

```

### **2. Pokretanje Phi-3-mini u Terminalu s MLX-om**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Rezultat (moje okruženje je Apple M1 Max, 64GB) je

![Terminal](../../../../../translated_images/01.5cf57df8f7407cf9281c0237f4e69c3728b8817253aad0835d14108b07c83c88.hr.png)

### **3. Kvantizacija Phi-3-mini s MLX-om u Terminalu**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Napomena:*** Model se može kvantizirati pomoću mlx_lm.convert, a zadana kvantizacija je INT4. Ovaj primjer kvantizira Phi-3-mini u INT4.

Model se može kvantizirati pomoću mlx_lm.convert, a zadana kvantizacija je INT4. Ovaj primjer služi za kvantizaciju Phi-3-mini u INT4. Nakon kvantizacije, model će biti spremljen u zadani direktorij ./mlx_model

Model kvantiziran s MLX-om možemo testirati iz terminala

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Rezultat je

![INT4](../../../../../translated_images/02.7b188681a8eadbc111aba8d8006e4b3671788947a99a46329261e169dd2ec29f.hr.png)

### **4. Pokretanje Phi-3-mini s MLX-om u Jupyter Notebooku**

![Notebook](../../../../../translated_images/03.b9705a3a5aaa89f9eb0ca04c1a4565dfe4a5e8cc68604227d2eab149fef1d3c7.hr.png)

***Napomena:*** Molimo pročitajte ovaj primjer [kliknite na ovaj link](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **Resursi**

1. Saznajte više o Apple MLX Frameworku [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub repozitorij [https://github.com/ml-explore](https://github.com/ml-explore)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.