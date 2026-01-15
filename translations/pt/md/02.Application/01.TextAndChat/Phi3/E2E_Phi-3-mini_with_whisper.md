<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f72d7981ed3640865700f51ae407da4",
  "translation_date": "2026-01-14T15:30:47+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "pt"
}
-->
# Chatbot Interativo Phi 3 Mini 4K Instruct com Whisper

## Visão Geral

O Chatbot Interativo Phi 3 Mini 4K Instruct é uma ferramenta que permite aos utilizadores interagir com a demo Microsoft Phi 3 Mini 4K instruct utilizando entrada de texto ou áudio. O chatbot pode ser usado para várias tarefas, como tradução, atualizações meteorológicas e recolha geral de informação.

### Começar

Para usar este chatbot, basta seguir estas instruções:

1. Abra um novo [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Na janela principal do notebook, verá uma interface de chat com uma caixa de entrada de texto e um botão "Send".
3. Para usar o chatbot baseado em texto, digite a sua mensagem na caixa de entrada de texto e clique no botão "Send". O chatbot irá responder com um ficheiro de áudio que pode ser reproduzido diretamente dentro do notebook.

**Nota**: Esta ferramenta requer uma GPU e acesso aos modelos Microsoft Phi-3 e OpenAI Whisper, que são usados para reconhecimento e tradução de fala.

### Requisitos de GPU

Para executar esta demo necessita de 12GB de memória na GPU.

Os requisitos de memória para executar a demo **Microsoft-Phi-3-Mini-4K instruct** numa GPU dependem de vários fatores, como o tamanho dos dados de entrada (áudio ou texto), a língua usada para tradução, a velocidade do modelo e a memória disponível na GPU.

Em geral, o modelo Whisper foi criado para correr em GPUs. A quantidade mínima recomendada de memória na GPU para executar o modelo Whisper é de 8 GB, mas pode lidar com quantidades maiores de memória se necessário.

É importante notar que processar grandes volumes de dados ou um elevado número de pedidos ao modelo pode exigir mais memória na GPU e/ou causar problemas de desempenho. Recomenda-se testar o seu caso de uso com diferentes configurações e monitorizar a utilização da memória para determinar as definições ótimas para as suas necessidades específicas.

## Exemplo E2E para Chatbot Interativo Phi 3 Mini 4K Instruct com Whisper

O notebook jupyter intitulado [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstra como usar a Demo Microsoft Phi 3 Mini 4K instruct para gerar texto a partir de áudio ou texto escrito. O notebook define várias funções:

1. `tts_file_name(text)`: Esta função gera um nome de ficheiro com base no texto de entrada para guardar o ficheiro de áudio gerado.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Esta função usa a API Edge TTS para gerar um ficheiro de áudio a partir de uma lista de blocos de texto de entrada. Os parâmetros de entrada são a lista de blocos, a velocidade da fala, o nome da voz e o caminho de saída para guardar o ficheiro de áudio gerado.
1. `talk(input_text)`: Esta função gera um ficheiro de áudio usando a API Edge TTS e guardando-o com um nome de ficheiro aleatório no diretório /content/audio. O parâmetro de entrada é o texto a converter em fala.
1. `run_text_prompt(message, chat_history)`: Esta função usa a demo Microsoft Phi 3 Mini 4K instruct para gerar um ficheiro de áudio a partir de uma mensagem de entrada e adiciona-o ao histórico de chat.
1. `run_audio_prompt(audio, chat_history)`: Esta função converte um ficheiro de áudio em texto usando a API do modelo Whisper e passa-o para a função `run_text_prompt()`.
1. O código lança uma aplicação Gradio que permite aos utilizadores interagir com a demo Phi 3 Mini 4K instruct ao escreverem mensagens ou carregarem ficheiros de áudio. A saída é exibida como mensagem de texto dentro da aplicação.

## Resolução de Problemas

Instalação de drivers de GPU Cuda

1. Certifique-se de que as aplicações Linux estão atualizadas

    ```bash
    sudo apt update
    ```

1. Instalar drivers Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registar a localização do driver cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Verificar o tamanho da memória da GPU Nvidia (Requer 12GB de memória GPU)

    ```bash
    nvidia-smi
    ```

1. Limpar Cache: Se estiver a usar PyTorch, pode chamar torch.cuda.empty_cache() para libertar toda a memória em cache não utilizada para que possa ser usada por outras aplicações GPU

    ```python
    torch.cuda.empty_cache() 
    ```

1. Verificar Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Execute as seguintes tarefas para criar um token Hugging Face.

    - Navegue para a [página de Configurações de Token do Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Selecione **New token**.
    - Introduza o **Nome** do projeto que pretende usar.
    - Selecione o **Tipo** para **Write**.

> [!NOTE]
>
> Se encontrar o seguinte erro:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Para resolver isto, escreva o seguinte comando no seu terminal.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->