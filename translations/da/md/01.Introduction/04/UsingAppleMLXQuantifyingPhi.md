<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-07-16T21:55:32+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "da"
}
-->
# **Kvantisering af Phi-3.5 med Apple MLX Framework**

MLX er et array-framework til maskinlæringsforskning på Apple silicon, udviklet af Apple maskinlæringsforskere.

MLX er designet af maskinlæringsforskere til maskinlæringsforskere. Frameworket er lavet til at være brugervenligt, men stadig effektivt til træning og implementering af modeller. Selve designet af frameworket er også konceptuelt enkelt. Vi ønsker at gøre det nemt for forskere at udvide og forbedre MLX med det formål hurtigt at kunne afprøve nye idéer.

LLM’er kan accelereres på Apple Silicon-enheder via MLX, og modeller kan køres lokalt på en meget bekvem måde.

Nu understøtter Apple MLX Framework kvantiseringskonvertering af Phi-3.5-Instruct (**Apple MLX Framework support**), Phi-3.5-Vision (**MLX-VLM Framework support**), og Phi-3.5-MoE (**Apple MLX Framework support**). Lad os prøve det næste:

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

### **🤖 Eksempler på Phi-3.5 med Apple MLX**

| Labs    | Introduktion | Gå til |
| -------- | ----------- | ------ |
| 🚀 Lab-Introduktion Phi-3.5 Instruct  | Lær hvordan du bruger Phi-3.5 Instruct med Apple MLX framework   |  [Gå til](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduktion Phi-3.5 Vision (billede) | Lær hvordan du bruger Phi-3.5 Vision til billedanalyse med Apple MLX framework     |  [Gå til](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduktion Phi-3.5 Vision (moE)   | Lær hvordan du bruger Phi-3.5 MoE med Apple MLX framework  |  [Gå til](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Ressourcer**

1. Lær om Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.