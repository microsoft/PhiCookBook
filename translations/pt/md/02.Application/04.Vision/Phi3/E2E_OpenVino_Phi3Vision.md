<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-07-17T05:02:50+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "pt"
}
-->
Esta demonstração mostra como usar um modelo pré-treinado para gerar código Python com base numa imagem e num prompt de texto.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Aqui está uma explicação passo a passo:

1. **Importações e Configuração**:
   - São importadas as bibliotecas e módulos necessários, incluindo `requests`, `PIL` para processamento de imagens, e `transformers` para lidar com o modelo e o processamento.

2. **Carregar e Exibir a Imagem**:
   - Um ficheiro de imagem (`demo.png`) é aberto usando a biblioteca `PIL` e exibido.

3. **Definir o Prompt**:
   - É criada uma mensagem que inclui a imagem e um pedido para gerar código Python que processe a imagem e a guarde usando `plt` (matplotlib).

4. **Carregar o Processor**:
   - O `AutoProcessor` é carregado a partir de um modelo pré-treinado especificado pelo diretório `out_dir`. Este processor irá tratar as entradas de texto e imagem.

5. **Criar o Prompt**:
   - O método `apply_chat_template` é usado para formatar a mensagem num prompt adequado para o modelo.

6. **Processar as Entradas**:
   - O prompt e a imagem são processados em tensores que o modelo consegue interpretar.

7. **Definir Argumentos de Geração**:
   - São definidos os argumentos para o processo de geração do modelo, incluindo o número máximo de novos tokens a gerar e se deve ser feita amostragem da saída.

8. **Gerar o Código**:
   - O modelo gera o código Python com base nas entradas e nos argumentos de geração. O `TextStreamer` é usado para gerir a saída, ignorando o prompt e os tokens especiais.

9. **Saída**:
   - O código gerado é impresso, devendo incluir código Python para processar a imagem e guardá-la conforme especificado no prompt.

Esta demonstração ilustra como aproveitar um modelo pré-treinado usando OpenVino para gerar código de forma dinâmica com base na entrada do utilizador e em imagens.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.