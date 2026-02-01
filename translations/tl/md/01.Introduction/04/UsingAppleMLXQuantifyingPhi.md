# **Pag-quantize ng Phi-3.5 gamit ang Apple MLX Framework**

Ang MLX ay isang array framework para sa pananaliksik sa machine learning sa Apple silicon, na dala sa iyo ng Apple machine learning research.

Ang MLX ay dinisenyo ng mga mananaliksik sa machine learning para sa mga mananaliksik sa machine learning. Ang framework ay nilikha upang maging madaling gamitin, ngunit epektibo pa rin sa pagsasanay at pag-deploy ng mga modelo. Ang disenyo ng framework mismo ay simple rin sa konsepto. Layunin naming gawing madali para sa mga mananaliksik na palawakin at pagbutihin ang MLX upang mabilis na makapag-eksperimento ng mga bagong ideya.

Maaaring pabilisin ang LLMs sa mga Apple Silicon device gamit ang MLX, at ang mga modelo ay maaaring patakbuhin nang lokal nang napakadali.

Ngayon, sinusuportahan ng Apple MLX Framework ang quantization conversion ng Phi-3.5-Instruct (**Apple MLX Framework support**), Phi-3.5-Vision (**MLX-VLM Framework support**), at Phi-3.5-MoE (**Apple MLX Framework support**). Subukan natin ito ngayon:

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

### **🤖 Mga Halimbawa para sa Phi-3.5 gamit ang Apple MLX**

| Labs    | Introduksyon | Puntahan |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Alamin kung paano gamitin ang Phi-3.5 Instruct gamit ang Apple MLX framework   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Alamin kung paano gamitin ang Phi-3.5 Vision para suriin ang larawan gamit ang Apple MLX framework     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Alamin kung paano gamitin ang Phi-3.5 MoE gamit ang Apple MLX framework  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Mga Sanggunian**

1. Alamin ang tungkol sa Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Rep [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.