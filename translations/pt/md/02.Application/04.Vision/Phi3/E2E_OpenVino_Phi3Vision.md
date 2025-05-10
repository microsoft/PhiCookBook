<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-05-09T19:59:46+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "pt"
}
-->
Esta demonstração mostra como usar um modelo pré-treinado para gerar código Python com base em uma imagem e um texto de comando.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Aqui está uma explicação passo a passo:

1. **Importações e Configuração**:
   - As bibliotecas e módulos necessários são importados, incluindo `requests`, `PIL` para processamento de imagens, e `transformers` para manipulação do modelo e processamento.

2. **Carregando e Exibindo a Imagem**:
   - Um arquivo de imagem (`demo.png`) é aberto usando a biblioteca `PIL` e exibido.

3. **Definindo o Prompt**:
   - Uma mensagem é criada que inclui a imagem e uma solicitação para gerar código Python para processar a imagem e salvá-la usando `plt` (matplotlib).

4. **Carregando o Processador**:
   - O `AutoProcessor` é carregado a partir de um modelo pré-treinado especificado pelo diretório `out_dir`. Este processador irá lidar com as entradas de texto e imagem.

5. **Criando o Prompt**:
   - O método `apply_chat_template` é usado para formatar a mensagem em um prompt adequado para o modelo.

6. **Processando as Entradas**:
   - O prompt e a imagem são processados em tensores que o modelo consegue interpretar.

7. **Definindo os Argumentos de Geração**:
   - São definidos os argumentos para o processo de geração do modelo, incluindo o número máximo de novos tokens a serem gerados e se a saída deve ser amostrada.

8. **Gerando o Código**:
   - O modelo gera o código Python com base nas entradas e nos argumentos de geração. O `TextStreamer` é usado para manipular a saída, pulando o prompt e os tokens especiais.

9. **Saída**:
   - O código gerado é impresso, o qual deve incluir código Python para processar a imagem e salvá-la conforme especificado no prompt.

Esta demonstração ilustra como aproveitar um modelo pré-treinado usando OpenVino para gerar código dinamicamente com base na entrada do usuário e imagens.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.