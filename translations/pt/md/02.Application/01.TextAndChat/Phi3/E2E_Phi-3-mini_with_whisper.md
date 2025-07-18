<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:17:33+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "pt"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot com Whisper

## Visão Geral

O Interactive Phi 3 Mini 4K Instruct Chatbot é uma ferramenta que permite aos utilizadores interagir com a demo Microsoft Phi 3 Mini 4K instruct através de entrada de texto ou áudio. O chatbot pode ser usado para várias tarefas, como tradução, atualizações meteorológicas e obtenção de informações gerais.

### Começar

Para usar este chatbot, basta seguir estas instruções:

1. Abra um novo [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Na janela principal do notebook, verá uma interface de chat com uma caixa de texto para entrada e um botão "Send".
3. Para usar o chatbot baseado em texto, basta escrever a sua mensagem na caixa de texto e clicar no botão "Send". O chatbot responderá com um ficheiro de áudio que pode ser reproduzido diretamente dentro do notebook.

**Note**: Esta ferramenta requer uma GPU e acesso aos modelos Microsoft Phi-3 e OpenAI Whisper, que são usados para reconhecimento de voz e tradução.

### Requisitos de GPU

Para executar esta demo, precisa de 12GB de memória GPU.

Os requisitos de memória para executar a demo **Microsoft-Phi-3-Mini-4K instruct** numa GPU dependem de vários fatores, como o tamanho dos dados de entrada (áudio ou texto), a língua usada para tradução, a velocidade do modelo e a memória disponível na GPU.

De modo geral, o modelo Whisper foi concebido para correr em GPUs. A quantidade mínima recomendada de memória GPU para executar o modelo Whisper é 8 GB, mas pode lidar com quantidades maiores de memória, se necessário.

É importante notar que processar uma grande quantidade de dados ou um elevado volume de pedidos no modelo pode exigir mais memória GPU e/ou causar problemas de desempenho. Recomenda-se testar o seu caso de uso com diferentes configurações e monitorizar o uso de memória para determinar as definições ideais para as suas necessidades específicas.

## Exemplo E2E para Interactive Phi 3 Mini 4K Instruct Chatbot com Whisper

O notebook Jupyter intitulado [Interactive Phi 3 Mini 4K Instruct Chatbot com Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstra como usar a demo Microsoft Phi 3 Mini 4K instruct para gerar texto a partir de áudio ou texto escrito. O notebook define várias funções:

1. `tts_file_name(text)`: Esta função gera um nome de ficheiro baseado no texto de entrada para guardar o ficheiro de áudio gerado.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Esta função usa a API Edge TTS para gerar um ficheiro de áudio a partir de uma lista de fragmentos de texto de entrada. Os parâmetros de entrada são a lista de fragmentos, a velocidade da fala, o nome da voz e o caminho de saída para guardar o ficheiro de áudio gerado.
1. `talk(input_text)`: Esta função gera um ficheiro de áudio usando a API Edge TTS e guarda-o com um nome de ficheiro aleatório na diretoria /content/audio. O parâmetro de entrada é o texto a converter em fala.
1. `run_text_prompt(message, chat_history)`: Esta função usa a demo Microsoft Phi 3 Mini 4K instruct para gerar um ficheiro de áudio a partir de uma mensagem de entrada e adiciona-o ao histórico de chat.
1. `run_audio_prompt(audio, chat_history)`: Esta função converte um ficheiro de áudio em texto usando a API do modelo Whisper e passa-o para a função `run_text_prompt()`.
1. O código lança uma aplicação Gradio que permite aos utilizadores interagir com a demo Phi 3 Mini 4K instruct, quer escrevendo mensagens, quer carregando ficheiros de áudio. A saída é apresentada como uma mensagem de texto dentro da aplicação.

## Resolução de Problemas

Instalar drivers Cuda para GPU

1. Certifique-se de que as suas aplicações Linux estão atualizadas

    ```bash
    sudo apt update
    ```

1. Instale os drivers Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registe a localização do driver cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Verificar o tamanho da memória da GPU Nvidia (Requer 12GB de memória GPU)

    ```bash
    nvidia-smi
    ```

1. Esvaziar Cache: Se estiver a usar PyTorch, pode chamar torch.cuda.empty_cache() para libertar toda a memória cache não utilizada, para que possa ser usada por outras aplicações GPU

    ```python
    torch.cuda.empty_cache() 
    ```

1. Verificar Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Execute as seguintes tarefas para criar um token Hugging Face.

    - Navegue até à [página de definições de tokens Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Selecione **New token**.
    - Introduza o **Nome** do projeto que pretende usar.
    - Selecione o **Tipo** para **Write**.

> **Note**
>
> Se encontrar o seguinte erro:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Para resolver, escreva o seguinte comando no seu terminal.
>
> ```bash
> sudo ldconfig
> ```

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.