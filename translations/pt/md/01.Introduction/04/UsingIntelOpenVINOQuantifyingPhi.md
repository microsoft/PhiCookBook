<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-05-09T13:54:11+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "pt"
}
-->
# **Quantizando Phi-3.5 usando Intel OpenVINO**

A Intel é o fabricante de CPU mais tradicional, com muitos usuários. Com o crescimento do machine learning e deep learning, a Intel também entrou na corrida pela aceleração de IA. Para inferência de modelos, a Intel não utiliza apenas GPUs e CPUs, mas também NPUs.

Queremos implantar a Família Phi-3.x na ponta, visando torná-la a parte mais importante do PC de IA e do PC Copilot. O carregamento do modelo na ponta depende da colaboração entre diferentes fabricantes de hardware. Este capítulo foca principalmente no cenário de aplicação do Intel OpenVINO como modelo quantitativo.

## **O que é o OpenVINO**

OpenVINO é um kit de ferramentas open-source para otimizar e implantar modelos de deep learning do cloud até a edge. Ele acelera a inferência de deep learning em vários casos de uso, como IA generativa, vídeo, áudio e linguagem, com modelos de frameworks populares como PyTorch, TensorFlow, ONNX e outros. Converta e otimize modelos e faça deploy em uma variedade de hardwares e ambientes Intel®, localmente ou em dispositivos, no navegador ou na nuvem.

Com o OpenVINO, você pode rapidamente quantizar modelos GenAI em hardware Intel e acelerar a referência do modelo.

Atualmente, o OpenVINO suporta conversão de quantização para Phi-3.5-Vision e Phi-3.5 Instruct.

### **Configuração do Ambiente**

Por favor, certifique-se de que as seguintes dependências do ambiente estão instaladas, este é o requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Quantizando Phi-3.5-Instruct usando OpenVINO**

No Terminal, execute este script

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Quantizando Phi-3.5-Vision usando OpenVINO**

Execute este script em Python ou Jupyter lab

```python

import requests
from pathlib import Path
from ov_phi3_vision import convert_phi3_model
import nncf

if not Path("ov_phi3_vision.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/ov_phi3_vision.py")
    open("ov_phi3_vision.py", "w").write(r.text)


if not Path("gradio_helper.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/gradio_helper.py")
    open("gradio_helper.py", "w").write(r.text)

if not Path("notebook_utils.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/utils/notebook_utils.py")
    open("notebook_utils.py", "w").write(r.text)



model_id = "microsoft/Phi-3.5-vision-instruct"
out_dir = Path("../model/phi-3.5-vision-128k-instruct-ov")
compression_configuration = {
    "mode": nncf.CompressWeightsMode.INT4_SYM,
    "group_size": 64,
    "ratio": 0.6,
}
if not out_dir.exists():
    convert_phi3_model(model_id, out_dir, compression_configuration)

```

### **🤖 Exemplos para Phi-3.5 com Intel OpenVINO**

| Labs    | Introdução | Acessar |
| -------- | ------- |  ------- |
| 🚀 Lab-Introdução Phi-3.5 Instruct  | Aprenda como usar Phi-3.5 Instruct no seu PC de IA    |  [Acessar](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introdução Phi-3.5 Vision (imagem) | Aprenda como usar Phi-3.5 Vision para analisar imagens no seu PC de IA      |  [Acessar](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introdução Phi-3.5 Vision (vídeo)   | Aprenda como usar Phi-3.5 Vision para analisar vídeos no seu PC de IA    |  [Acessar](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Recursos**

1. Saiba mais sobre Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Repositório Intel OpenVINO no GitHub [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.