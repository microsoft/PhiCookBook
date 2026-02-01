# **Quantizando Phi-3.5 usando o Apple MLX Framework**

MLX é um framework de arrays para pesquisa em aprendizado de máquina no Apple silicon, desenvolvido pela equipe de pesquisa em aprendizado de máquina da Apple.

O MLX foi criado por pesquisadores de aprendizado de máquina para pesquisadores de aprendizado de máquina. O framework foi pensado para ser fácil de usar, mas ainda assim eficiente para treinar e implantar modelos. O design do próprio framework também é conceitualmente simples. Nosso objetivo é facilitar para os pesquisadores a extensão e melhoria do MLX, permitindo explorar novas ideias rapidamente.

LLMs podem ser acelerados em dispositivos Apple Silicon através do MLX, e os modelos podem ser executados localmente de forma muito prática.

Agora o Apple MLX Framework suporta a conversão de quantização do Phi-3.5-Instruct (**suporte do Apple MLX Framework**), Phi-3.5-Vision (**suporte do MLX-VLM Framework**) e Phi-3.5-MoE (**suporte do Apple MLX Framework**). Vamos experimentar a seguir:

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

| Laboratórios    | Introdução | Acessar |
| -------- | ------- |  ------- |
| 🚀 Lab-Introdução Phi-3.5 Instruct  | Aprenda como usar o Phi-3.5 Instruct com o Apple MLX framework   |  [Acessar](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introdução Phi-3.5 Vision (imagem) | Aprenda como usar o Phi-3.5 Vision para analisar imagens com o Apple MLX framework     |  [Acessar](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introdução Phi-3.5 Vision (moE)   | Aprenda como usar o Phi-3.5 MoE com o Apple MLX framework  |  [Acessar](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Recursos**

1. Saiba mais sobre o Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Repositório Apple MLX no GitHub [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Repositório MLX-VLM no GitHub [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.