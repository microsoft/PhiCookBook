<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-09T13:43:10+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "br"
}
-->
# **Quantizando Phi-3.5 usando o Apple MLX Framework**

MLX é um framework de arrays para pesquisa em aprendizado de máquina em dispositivos Apple Silicon, desenvolvido pela equipe de pesquisa em machine learning da Apple.

O MLX foi criado por pesquisadores de machine learning para pesquisadores de machine learning. O framework é pensado para ser fácil de usar, mas ainda assim eficiente para treinar e implementar modelos. O design do próprio framework também é conceitualmente simples. Nosso objetivo é facilitar para que pesquisadores possam estender e melhorar o MLX, permitindo a rápida experimentação de novas ideias.

LLMs podem ser acelerados em dispositivos Apple Silicon por meio do MLX, e os modelos podem ser executados localmente de forma muito prática.

Agora, o Apple MLX Framework suporta a conversão de quantização do Phi-3.5-Instruct (**Apple MLX Framework support**), Phi-3.5-Vision (**MLX-VLM Framework support**), e Phi-3.5-MoE (**Apple MLX Framework support**). Vamos testar a seguir:

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

| Labs    | Introdução | Acessar |
| -------- | ------- |  ------- |
| 🚀 Lab-Introdução Phi-3.5 Instruct  | Aprenda a usar o Phi-3.5 Instruct com o Apple MLX framework   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introdução Phi-3.5 Vision (imagem) | Aprenda a usar o Phi-3.5 Vision para analisar imagens com o Apple MLX framework     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introdução Phi-3.5 Vision (moE)   | Aprenda a usar o Phi-3.5 MoE com o Apple MLX framework  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Recursos**

1. Saiba mais sobre o Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Repositório Apple MLX no GitHub [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Repositório MLX-VLM no GitHub [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.