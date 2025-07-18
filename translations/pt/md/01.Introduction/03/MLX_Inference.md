<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-07-16T21:02:33+00:00",
  "source_file": "md/01.Introduction/03/MLX_Inference.md",
  "language_code": "pt"
}
-->
# **Inferência Phi-3 com o Framework Apple MLX**

## **O que é o Framework MLX**

MLX é um framework de arrays para investigação em machine learning em Apple silicon, desenvolvido pela equipa de investigação em machine learning da Apple.

O MLX foi criado por investigadores de machine learning para investigadores de machine learning. O framework pretende ser fácil de usar, mas ao mesmo tempo eficiente para treinar e implementar modelos. O design do próprio framework é também conceptualmente simples. Queremos facilitar que os investigadores possam estender e melhorar o MLX com o objetivo de explorar rapidamente novas ideias.

LLMs podem ser acelerados em dispositivos Apple Silicon através do MLX, e os modelos podem ser executados localmente de forma muito conveniente.

## **Usar o MLX para inferir Phi-3-mini**

### **1. Configurar o seu ambiente MLX**

1. Python 3.11.x  
2. Instalar a biblioteca MLX

```bash

pip install mlx-lm

```

### **2. Executar Phi-3-mini no Terminal com MLX**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

O resultado (o meu ambiente é Apple M1 Max, 64GB) é

![Terminal](../../../../../translated_images/01.5cf57df8f7407cf9281c0237f4e69c3728b8817253aad0835d14108b07c83c88.pt.png)

### **3. Quantizar Phi-3-mini com MLX no Terminal**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Nota:*** O modelo pode ser quantizado através do mlx_lm.convert, e a quantização padrão é INT4. Este exemplo quantiza o Phi-3-mini para INT4.

O modelo pode ser quantizado através do mlx_lm.convert, e a quantização padrão é INT4. Este exemplo mostra como quantizar o Phi-3-mini para INT4. Após a quantização, o modelo será guardado na diretoria padrão ./mlx_model

Podemos testar o modelo quantizado com MLX a partir do terminal

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

O resultado é

![INT4](../../../../../translated_images/02.7b188681a8eadbc111aba8d8006e4b3671788947a99a46329261e169dd2ec29f.pt.png)

### **4. Executar Phi-3-mini com MLX no Jupyter Notebook**

![Notebook](../../../../../translated_images/03.b9705a3a5aaa89f9eb0ca04c1a4565dfe4a5e8cc68604227d2eab149fef1d3c7.pt.png)

***Nota:*** Por favor, consulte este exemplo [clique neste link](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **Recursos**

1. Saiba mais sobre o Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Repositório Apple MLX no GitHub [https://github.com/ml-explore](https://github.com/ml-explore)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.