<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:35:46+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "br"
}
-->
﻿## Bem-vindo aos laboratórios Phi usando C#

Há uma seleção de laboratórios que mostram como integrar as diferentes versões poderosas dos modelos Phi em um ambiente .NET.

## Pré-requisitos

Antes de executar o exemplo, certifique-se de que você tenha o seguinte instalado:

**.NET 9:** Garanta que você tenha a [versão mais recente do .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) instalada em sua máquina.

**(Opcional) Visual Studio ou Visual Studio Code:** Você precisará de uma IDE ou editor de código capaz de executar projetos .NET. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) ou [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) são recomendados.

**Usando git** clone localmente uma das versões disponíveis Phi-3, Phi3.5 ou Phi-4 a partir de [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Baixe os modelos Phi-4 ONNX** para sua máquina local:

### navegue até a pasta para armazenar os modelos

```bash
cd c:\phi\models
```

### adicione suporte para lfs

```bash
git lfs install 
```

### clone e baixe o modelo Phi-4 mini instruct e o modelo Phi-4 multimodal

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Baixe os modelos Phi-3 ONNX** para sua máquina local:

### clone e baixe o modelo Phi-3 mini 4K instruct e o modelo Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Importante:** As demos atuais foram projetadas para usar as versões ONNX do modelo. Os passos anteriores clonam os seguintes modelos.

## Sobre os Laboratórios

A solução principal possui vários laboratórios de exemplo que demonstram as capacidades dos modelos Phi usando C#.

| Projeto | Modelo | Descrição |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 ou Phi-3.5 | Chat de console de exemplo que permite ao usuário fazer perguntas. O projeto carrega um modelo local ONNX Phi-3 usando as bibliotecas `Microsoft.ML.OnnxRuntime`. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 ou Phi-3.5 | Chat de console de exemplo que permite ao usuário fazer perguntas. O projeto carrega um modelo local ONNX Phi-3 usando as bibliotecas `Microsoft.Semantic.Kernel`. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 ou Phi-3.5 | Este é um projeto de exemplo que usa um modelo local phi3 vision para analisar imagens. O projeto carrega um modelo local ONNX Phi-3 Vision usando as bibliotecas `Microsoft.ML.OnnxRuntime`. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 ou Phi-3.5 | Este é um projeto de exemplo que usa um modelo local phi3 vision para analisar imagens. O projeto carrega um modelo local ONNX Phi-3 Vision usando as bibliotecas `Microsoft.ML.OnnxRuntime`. O projeto também apresenta um menu com diferentes opções para interagir com o usuário. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Chat de console de exemplo que permite ao usuário fazer perguntas. O projeto carrega um modelo local ONNX Phi-4 usando as bibliotecas `Microsoft.ML.OnnxRuntime`. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Chat de console de exemplo que permite ao usuário fazer perguntas. O projeto carrega um modelo local ONNX Phi-4 usando as bibliotecas `Semantic Kernel`. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Chat de console de exemplo que permite ao usuário fazer perguntas. O projeto carrega um modelo local ONNX Phi-4 usando as bibliotecas `Microsoft.ML.OnnxRuntimeGenAI` e implementa o `IChatClient` do `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Chat de console de exemplo que permite ao usuário fazer perguntas. O chat implementa memória. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Este é um projeto de exemplo que usa um modelo local Phi-4 para analisar imagens mostrando o resultado no console. O projeto carrega um modelo local Phi-4-`multimodal-instruct-onnx` usando as bibliotecas `Microsoft.ML.OnnxRuntime`. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Este é um projeto de exemplo que usa um modelo local Phi-4 para analisar um arquivo de áudio, gerar a transcrição do arquivo e mostrar o resultado no console. O projeto carrega um modelo local Phi-4-`multimodal-instruct-onnx` usando as bibliotecas `Microsoft.ML.OnnxRuntime`. |

## Como Executar os Projetos

Para executar os projetos, siga os passos:

1. Clone o repositório para sua máquina local.

1. Abra um terminal e navegue até o projeto desejado. Por exemplo, vamos executar `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Execute o projeto com o comando

    ```bash
    dotnet run
    ```

1. O projeto de exemplo solicita uma entrada do usuário e responde usando o modelo local.

   A demo em execução é semelhante a esta:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.