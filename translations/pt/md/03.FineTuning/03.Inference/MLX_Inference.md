<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-07-17T10:05:55+00:00",
  "source_file": "md/03.FineTuning/03.Inference/MLX_Inference.md",
  "language_code": "pt"
}
-->
# **Inferência Phi-3 com o Framework Apple MLX**

## **O que é o Framework MLX**

O MLX é um framework de arrays para investigação em machine learning em Apple silicon, desenvolvido pela equipa de investigação em machine learning da Apple.

O MLX foi criado por investigadores de machine learning para investigadores de machine learning. O framework pretende ser fácil de usar, mas ao mesmo tempo eficiente para treinar e implementar modelos. O design do próprio framework é também conceptualmente simples. Queremos facilitar que os investigadores possam estender e melhorar o MLX com o objetivo de explorar rapidamente novas ideias.

LLMs podem ser acelerados em dispositivos Apple Silicon através do MLX, e os modelos podem ser executados localmente de forma muito conveniente.

## **Usar o MLX para inferir Phi-3-mini**

### **1. Configurar o seu ambiente MLX**

1. Python 3.11.x  
2. Instalar a Biblioteca MLX

```bash

pip install mlx-lm

```

### **2. Executar Phi-3-mini no Terminal com MLX**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

O resultado (o meu ambiente é Apple M1 Max, 64GB) é

![Terminal](../../../../../translated_images/pt/01.5cf57df8f7407cf9.png)

### **3. Quantizar Phi-3-mini com MLX no Terminal**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note:*** O modelo pode ser quantizado através do mlx_lm.convert, e a quantização por defeito é INT4. Este exemplo quantiza o Phi-3-mini para INT4.

O modelo pode ser quantizado através do mlx_lm.convert, e a quantização por defeito é INT4. Este exemplo serve para quantizar o Phi-3-mini para INT4. Após a quantização, será guardado na diretoria por defeito ./mlx_model

Podemos testar o modelo quantizado com MLX a partir do terminal

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

O resultado é

![INT4](../../../../../translated_images/pt/02.7b188681a8eadbc1.png)

### **4. Executar Phi-3-mini com MLX no Jupyter Notebook**

![Notebook](../../../../../translated_images/pt/03.b9705a3a5aaa89f9.png)

***Note:*** Por favor, leia este exemplo [clique neste link](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **Recursos**

1. Saiba mais sobre o Framework Apple MLX [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Repositório Apple MLX no GitHub [https://github.com/ml-explore](https://github.com/ml-explore)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.