### Cenário de Exemplo

Imagine que tem uma imagem (`demo.png`) e quer gerar código Python que processe esta imagem e guarde uma nova versão dela (`phi-3-vision.jpg`).

O código acima automatiza este processo ao:

1. Configurar o ambiente e as configurações necessárias.
2. Criar um prompt que instrui o modelo a gerar o código Python necessário.
3. Enviar o prompt para o modelo e recolher o código gerado.
4. Extrair e executar o código gerado.
5. Mostrar as imagens original e processada.

Esta abordagem aproveita o poder da IA para automatizar tarefas de processamento de imagens, tornando mais fácil e rápido alcançar os seus objetivos.

[Exemplo de Código](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Vamos analisar passo a passo o que o código faz:

1. **Instalar o Pacote Necessário**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Este comando instala o pacote `langchain_nvidia_ai_endpoints`, garantindo que está na versão mais recente.

2. **Importar os Módulos Necessários**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Estas importações trazem os módulos necessários para interagir com os endpoints NVIDIA AI, gerir passwords de forma segura, interagir com o sistema operativo e codificar/decodificar dados em base64.

3. **Configurar a Chave API**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Este código verifica se a variável de ambiente `NVIDIA_API_KEY` está definida. Caso contrário, pede ao utilizador para inserir a sua chave API de forma segura.

4. **Definir Modelo e Caminho da Imagem**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Isto define o modelo a usar, cria uma instância de `ChatNVIDIA` com o modelo especificado e define o caminho para o ficheiro de imagem.

5. **Criar Prompt de Texto**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Isto define um prompt de texto que instrui o modelo a gerar código Python para processar uma imagem.

6. **Codificar a Imagem em Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Este código lê o ficheiro de imagem, codifica-o em base64 e cria uma tag HTML de imagem com os dados codificados.

7. **Combinar Texto e Imagem no Prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    Isto combina o prompt de texto e a tag HTML da imagem numa única string.

8. **Gerar Código Usando ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Este código envia o prompt para o modelo `ChatNVIDIA` e recolhe o código gerado em partes, imprimindo e adicionando cada parte à string `code`.

9. **Extrair Código Python do Conteúdo Gerado**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Isto extrai o código Python real do conteúdo gerado, removendo a formatação markdown.

10. **Executar o Código Gerado**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Isto executa o código Python extraído como um subprocesso e captura a sua saída.

11. **Mostrar as Imagens**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Estas linhas mostram as imagens usando o módulo `IPython.display`.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.