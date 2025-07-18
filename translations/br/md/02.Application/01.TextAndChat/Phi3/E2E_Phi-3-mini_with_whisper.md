<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:17:48+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "br"
}
-->
# Chatbot Interativo Phi 3 Mini 4K Instruct com Whisper

## Visão Geral

O Chatbot Interativo Phi 3 Mini 4K Instruct é uma ferramenta que permite aos usuários interagir com a demonstração Microsoft Phi 3 Mini 4K instruct usando entrada de texto ou áudio. O chatbot pode ser usado para diversas tarefas, como tradução, atualizações do tempo e obtenção de informações gerais.

### Começando

Para usar este chatbot, basta seguir estas instruções:

1. Abra um novo [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Na janela principal do notebook, você verá uma interface de chat com uma caixa de entrada de texto e um botão "Send".
3. Para usar o chatbot baseado em texto, digite sua mensagem na caixa de entrada de texto e clique no botão "Send". O chatbot responderá com um arquivo de áudio que pode ser reproduzido diretamente dentro do notebook.

**Note**: Esta ferramenta requer uma GPU e acesso aos modelos Microsoft Phi-3 e OpenAI Whisper, que são usados para reconhecimento de fala e tradução.

### Requisitos de GPU

Para executar esta demonstração, você precisa de 12GB de memória GPU.

Os requisitos de memória para rodar a demonstração **Microsoft-Phi-3-Mini-4K instruct** em uma GPU dependem de vários fatores, como o tamanho dos dados de entrada (áudio ou texto), o idioma usado para tradução, a velocidade do modelo e a memória disponível na GPU.

Em geral, o modelo Whisper foi projetado para rodar em GPUs. A quantidade mínima recomendada de memória GPU para executar o modelo Whisper é 8 GB, mas ele pode lidar com quantidades maiores de memória, se necessário.

É importante notar que processar uma grande quantidade de dados ou um volume alto de requisições no modelo pode exigir mais memória GPU e/ou causar problemas de desempenho. Recomenda-se testar seu caso de uso com diferentes configurações e monitorar o uso de memória para determinar as configurações ideais para suas necessidades específicas.

## Exemplo E2E para Chatbot Interativo Phi 3 Mini 4K Instruct com Whisper

O notebook Jupyter intitulado [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstra como usar a demonstração Microsoft Phi 3 Mini 4K instruct para gerar texto a partir de entrada de áudio ou texto escrito. O notebook define várias funções:

1. `tts_file_name(text)`: Esta função gera um nome de arquivo baseado no texto de entrada para salvar o arquivo de áudio gerado.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Esta função usa a API Edge TTS para gerar um arquivo de áudio a partir de uma lista de pedaços de texto de entrada. Os parâmetros de entrada são a lista de pedaços, a velocidade da fala, o nome da voz e o caminho de saída para salvar o arquivo de áudio gerado.
1. `talk(input_text)`: Esta função gera um arquivo de áudio usando a API Edge TTS e o salva com um nome de arquivo aleatório no diretório /content/audio. O parâmetro de entrada é o texto a ser convertido em fala.
1. `run_text_prompt(message, chat_history)`: Esta função usa a demonstração Microsoft Phi 3 Mini 4K instruct para gerar um arquivo de áudio a partir de uma mensagem de entrada e adiciona esse áudio ao histórico do chat.
1. `run_audio_prompt(audio, chat_history)`: Esta função converte um arquivo de áudio em texto usando a API do modelo Whisper e passa o texto para a função `run_text_prompt()`.
1. O código inicia um aplicativo Gradio que permite aos usuários interagir com a demonstração Phi 3 Mini 4K instruct, digitando mensagens ou enviando arquivos de áudio. A saída é exibida como uma mensagem de texto dentro do aplicativo.

## Solução de Problemas

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

1. Limpar Cache: Se você estiver usando PyTorch, pode chamar torch.cuda.empty_cache() para liberar toda a memória cache não utilizada, permitindo que outras aplicações GPU a utilizem

    ```python
    torch.cuda.empty_cache() 
    ```

1. Verificar Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Execute as seguintes tarefas para criar um token Hugging Face.

    - Acesse a [página de Configurações de Token do Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
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
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.