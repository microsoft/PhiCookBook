<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-09T18:30:21+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "br"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## Overview

O Interactive Phi 3 Mini 4K Instruct Chatbot é uma ferramenta que permite aos usuários interagir com a demonstração Microsoft Phi 3 Mini 4K instruct usando entrada de texto ou áudio. O chatbot pode ser usado para diversas tarefas, como tradução, atualizações do tempo e coleta geral de informações.

### Getting Started

Para usar este chatbot, siga estas instruções:

1. Abra um novo [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Na janela principal do notebook, você verá uma interface de chat com uma caixa de entrada de texto e um botão "Send".
3. Para usar o chatbot baseado em texto, digite sua mensagem na caixa de entrada e clique no botão "Send". O chatbot responderá com um arquivo de áudio que pode ser reproduzido diretamente no notebook.

**Note**: Esta ferramenta requer uma GPU e acesso aos modelos Microsoft Phi-3 e OpenAI Whisper, usados para reconhecimento de fala e tradução.

### GPU Requirements

Para rodar esta demonstração, você precisa de 12Gb de memória GPU.

Os requisitos de memória para executar a demo **Microsoft-Phi-3-Mini-4K instruct** numa GPU dependem de vários fatores, como o tamanho dos dados de entrada (áudio ou texto), o idioma usado para tradução, a velocidade do modelo e a memória disponível na GPU.

Em geral, o modelo Whisper foi projetado para rodar em GPUs. A quantidade mínima recomendada de memória GPU para o Whisper é 8 GB, mas ele pode usar mais memória se necessário.

É importante notar que processar grandes volumes de dados ou muitas requisições pode exigir mais memória GPU e/ou causar problemas de desempenho. Recomenda-se testar seu caso de uso com diferentes configurações e monitorar o uso de memória para encontrar as melhores configurações para suas necessidades específicas.

## E2E Sample for Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

O notebook Jupyter intitulado [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstra como usar a demonstração Microsoft Phi 3 Mini 4K instruct para gerar texto a partir de áudio ou texto escrito. O notebook define várias funções:

1. `tts_file_name(text)`: Esta função gera um nome de arquivo baseado no texto de entrada para salvar o arquivo de áudio gerado.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Esta função usa a API Edge TTS para gerar um arquivo de áudio a partir de uma lista de pedaços de texto. Os parâmetros de entrada são a lista de pedaços, a velocidade da fala, o nome da voz e o caminho de saída para salvar o arquivo de áudio gerado.
1. `talk(input_text)`: Esta função gera um arquivo de áudio usando a API Edge TTS e salva com um nome aleatório na pasta /content/audio. O parâmetro de entrada é o texto a ser convertido em fala.
1. `run_text_prompt(message, chat_history)`: Esta função usa a demonstração Microsoft Phi 3 Mini 4K instruct para gerar um arquivo de áudio a partir de uma mensagem e adiciona ao histórico do chat.
1. `run_audio_prompt(audio, chat_history)`: Esta função converte um arquivo de áudio em texto usando a API do modelo Whisper e passa o resultado para a função `run_text_prompt()`.
1. O código inicia um app Gradio que permite aos usuários interagir com a demonstração Phi 3 Mini 4K instruct, digitando mensagens ou enviando arquivos de áudio. A saída é exibida como mensagem de texto dentro do app.

## Troubleshooting

Instalando drivers Cuda para GPU

1. Certifique-se de que seu sistema Linux está atualizado

    ```bash
    sudo apt update
    ```

1. Instale os drivers Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registre a localização do driver cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Verifique o tamanho da memória da GPU Nvidia (Requer 12GB de memória GPU)

    ```bash
    nvidia-smi
    ```

1. Limpar Cache: Se estiver usando PyTorch, você pode chamar torch.cuda.empty_cache() para liberar toda a memória cache não utilizada, permitindo que outras aplicações GPU possam usá-la

    ```python
    torch.cuda.empty_cache() 
    ```

1. Verifique o Cuda Nvidia

    ```bash
    nvcc --version
    ```

1. Realize as seguintes etapas para criar um token Hugging Face.

    - Acesse a [página de configurações de token do Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Selecione **New token**.
    - Insira o **Nome** do projeto que deseja usar.
    - Selecione o **Tipo** como **Write**.

> **Note**
>
> Se você encontrar o seguinte erro:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Para resolver, digite o seguinte comando no seu terminal.
>
> ```bash
> sudo ldconfig
> ```

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.