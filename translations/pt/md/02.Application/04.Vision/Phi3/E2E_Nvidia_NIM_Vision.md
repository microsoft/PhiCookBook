<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-09T19:55:11+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "pt"
}
-->
### Cenário Exemplo

Imagine que você tem uma imagem (`demo.png`) e quer gerar um código Python que processe essa imagem e salve uma nova versão dela (`phi-3-vision.jpg`).

O código acima automatiza esse processo ao:

1. Configurar o ambiente e as configurações necessárias.
2. Criar um prompt que instrui o modelo a gerar o código Python solicitado.
3. Enviar o prompt para o modelo e coletar o código gerado.
4. Extrair e executar o código gerado.
5. Exibir as imagens original e processada.

Essa abordagem aproveita o poder da IA para automatizar tarefas de processamento de imagens, tornando mais fácil e rápido alcançar seus objetivos.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Vamos detalhar o que o código inteiro faz, passo a passo:

1. **Instalar o Pacote Necessário**:  
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```  
    Esse comando instala o pacote `langchain_nvidia_ai_endpoints`, garantindo que seja a versão mais recente.

2. **Importar Módulos Necessários**:  
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```  
    Essas importações trazem os módulos necessários para interagir com os endpoints NVIDIA AI, lidar com senhas de forma segura, interagir com o sistema operacional e codificar/decodificar dados em base64.

3. **Configurar a Chave da API**:  
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```  
    Esse código verifica se a variável de ambiente `NVIDIA_API_KEY` está definida. Caso não esteja, solicita que o usuário insira sua chave da API de forma segura.

4. **Definir Modelo e Caminho da Imagem**:  
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```  
    Isso define o modelo a ser usado, cria uma instância de `ChatNVIDIA` com o modelo especificado e define o caminho para o arquivo da imagem.

5. **Criar Prompt de Texto**:  
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```  
    Define um prompt de texto que instrui o modelo a gerar código Python para processar uma imagem.

6. **Codificar Imagem em Base64**:  
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```  
    Esse código lê o arquivo da imagem, codifica-o em base64 e cria uma tag HTML de imagem com os dados codificados.

7. **Combinar Texto e Imagem no Prompt**:  
    ```python
    prompt = f"{text} {image}"
    ```  
    Combina o prompt de texto e a tag HTML da imagem em uma única string.

8. **Gerar Código Usando ChatNVIDIA**:  
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```  
    Esse código envia o prompt para o `ChatNVIDIA` e obtém a string de código gerada.

9. **Extrair Código Python do Conteúdo Gerado**:  
    ```python
    begin = code.index('```python') + 9  
    code = code[begin:]  
    end = code.index('```')
    code = code[:end]
    ```  
    Extrai o código Python real do conteúdo gerado, removendo a formatação markdown.

10. **Executar o Código Gerado**:  
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```  
    Executa o código Python extraído como um subprocesso e captura sua saída.

11. **Exibir Imagens**:  
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```  
    Essas linhas exibem as imagens usando o módulo `IPython.display`.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.