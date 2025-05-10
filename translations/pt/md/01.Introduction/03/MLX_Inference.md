<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-05-09T12:11:45+00:00",
  "source_file": "md/01.Introduction/03/MLX_Inference.md",
  "language_code": "pt"
}
-->
# **Inferência Phi-3 com o Apple MLX Framework**

## **O que é o MLX Framework**

MLX é um framework de arrays para pesquisa em machine learning em dispositivos Apple Silicon, desenvolvido pela equipe de pesquisa em machine learning da Apple.

O MLX foi criado por pesquisadores de machine learning para pesquisadores de machine learning. O framework foi pensado para ser fácil de usar, mas ainda assim eficiente para treinar e implementar modelos. O design do próprio framework também é conceitualmente simples. Nosso objetivo é facilitar para os pesquisadores a extensão e melhoria do MLX, permitindo a rápida exploração de novas ideias.

LLMs podem ser acelerados em dispositivos Apple Silicon por meio do MLX, e os modelos podem ser executados localmente de forma muito conveniente.

## **Usando MLX para inferir Phi-3-mini**

### **1. Configure seu ambiente MLX**

1. Python 3.11.x  
2. Instale a biblioteca MLX  


```bash

pip install mlx-lm

```

### **2. Executando Phi-3-mini no Terminal com MLX**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

O resultado (meu ambiente é Apple M1 Max, 64GB) é

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.pt.png)

### **3. Quantizando Phi-3-mini com MLX no Terminal**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note:*** O modelo pode ser quantizado através do mlx_lm.convert, e a quantização padrão é INT4. Este exemplo quantiza o Phi-3-mini para INT4.

O modelo pode ser quantizado usando mlx_lm.convert, e a quantização padrão é INT4. Neste exemplo, o Phi-3-mini é quantizado para INT4. Após a quantização, ele será armazenado no diretório padrão ./mlx_model

Podemos testar o modelo quantizado com MLX diretamente do terminal

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

O resultado é

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.pt.png)

### **4. Executando Phi-3-mini com MLX no Jupyter Notebook**

![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.pt.png)

***Note:*** Por favor, leia este exemplo [clique neste link](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **Recursos**

1. Saiba mais sobre o Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Repositório Apple MLX no GitHub [https://github.com/ml-explore](https://github.com/ml-explore)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.