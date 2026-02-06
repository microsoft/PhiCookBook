# **Quantização do Phi-3.5 usando o Apple MLX Framework**

MLX é um framework para arrays dedicado à investigação em machine learning em dispositivos Apple Silicon, desenvolvido pela equipa de investigação em machine learning da Apple.

O MLX foi criado por investigadores de machine learning para investigadores de machine learning. O framework foi pensado para ser fácil de usar, mas ao mesmo tempo eficiente para treinar e implementar modelos. O design do próprio framework é também conceptualmente simples. Pretendemos facilitar a extensão e melhoria do MLX por parte dos investigadores, com o objetivo de explorar rapidamente novas ideias.

Os LLMs podem ser acelerados em dispositivos Apple Silicon através do MLX, e os modelos podem ser executados localmente de forma muito conveniente.

Agora, o Apple MLX Framework suporta a conversão de quantização do Phi-3.5-Instruct (**suporte do Apple MLX Framework**), Phi-3.5-Vision (**suporte do MLX-VLM Framework**) e Phi-3.5-MoE (**suporte do Apple MLX Framework**). Vamos experimentar a seguir:

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

### **🤖 Exemplos para Phi-3.5 com Apple MLX**

| Laboratórios    | Introdução | Ir |
| -------- | ------- |  ------- |
| 🚀 Lab-Introdução Phi-3.5 Instruct  | Aprenda a usar o Phi-3.5 Instruct com o Apple MLX framework   |  [Ir](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introdução Phi-3.5 Vision (imagem) | Aprenda a usar o Phi-3.5 Vision para analisar imagens com o Apple MLX framework     |  [Ir](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introdução Phi-3.5 Vision (moE)   | Aprenda a usar o Phi-3.5 MoE com o Apple MLX framework  |  [Ir](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Recursos**

1. Saiba mais sobre o Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Repositório Apple MLX no GitHub [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Repositório MLX-VLM no GitHub [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.