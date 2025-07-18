<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-07-17T05:02:57+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "br"
}
-->
Esta demonstração mostra como usar um modelo pré-treinado para gerar código Python com base em uma imagem e um texto de entrada.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Aqui está uma explicação passo a passo:

1. **Imports e Configuração**:
   - As bibliotecas e módulos necessários são importados, incluindo `requests`, `PIL` para processamento de imagens, e `transformers` para manipulação do modelo e do processamento.

2. **Carregando e Exibindo a Imagem**:
   - Um arquivo de imagem (`demo.png`) é aberto usando a biblioteca `PIL` e exibido.

3. **Definindo o Prompt**:
   - Uma mensagem é criada que inclui a imagem e uma solicitação para gerar código Python para processar a imagem e salvá-la usando `plt` (matplotlib).

4. **Carregando o Processor**:
   - O `AutoProcessor` é carregado a partir de um modelo pré-treinado especificado pelo diretório `out_dir`. Esse processor vai lidar com as entradas de texto e imagem.

5. **Criando o Prompt**:
   - O método `apply_chat_template` é usado para formatar a mensagem em um prompt adequado para o modelo.

6. **Processando as Entradas**:
   - O prompt e a imagem são processados em tensores que o modelo consegue interpretar.

7. **Definindo os Argumentos de Geração**:
   - São definidos os argumentos para o processo de geração do modelo, incluindo o número máximo de novos tokens a serem gerados e se a saída deve ser amostrada.

8. **Gerando o Código**:
   - O modelo gera o código Python com base nas entradas e nos argumentos de geração. O `TextStreamer` é usado para lidar com a saída, pulando o prompt e os tokens especiais.

9. **Saída**:
   - O código gerado é impresso, e deve incluir o código Python para processar a imagem e salvá-la conforme especificado no prompt.

Esta demonstração ilustra como aproveitar um modelo pré-treinado usando OpenVino para gerar código dinamicamente com base na entrada do usuário e em imagens.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.