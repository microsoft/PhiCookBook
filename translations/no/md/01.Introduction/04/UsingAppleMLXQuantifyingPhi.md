# **Kvantifisering av Phi-3.5 med Apple MLX Framework**

MLX er et rammeverk for maskinlæringsforskning på Apple-silikon, utviklet av Apple maskinlæringsforskning.

MLX er designet av maskinlæringsforskere for maskinlæringsforskere. Rammeverket er ment å være brukervennlig, men samtidig effektivt for trening og distribusjon av modeller. Designet av rammeverket er også konseptuelt enkelt. Vi ønsker å gjøre det lett for forskere å utvide og forbedre MLX med mål om raskt å utforske nye ideer.

LLMer kan akselereres på Apple Silicon-enheter gjennom MLX, og modeller kan kjøres lokalt på en veldig praktisk måte.

Nå støtter Apple MLX Framework kvantiseringskonvertering av Phi-3.5-Instruct (**Apple MLX Framework support**), Phi-3.5-Vision (**MLX-VLM Framework support**), og Phi-3.5-MoE (**Apple MLX Framework support**). La oss prøve det neste:

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

### **🤖 Eksempler for Phi-3.5 med Apple MLX**

| Labs    | Introduksjon | Gå til |
| -------- | ----------- | ------- |
| 🚀 Lab-Introduksjon Phi-3.5 Instruct  | Lær hvordan du bruker Phi-3.5 Instruct med Apple MLX framework   |  [Gå til](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduksjon Phi-3.5 Vision (bilde) | Lær hvordan du bruker Phi-3.5 Vision for å analysere bilder med Apple MLX framework     |  [Gå til](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduksjon Phi-3.5 Vision (moE)   | Lær hvordan du bruker Phi-3.5 MoE med Apple MLX framework  |  [Gå til](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Ressurser**

1. Lær om Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.