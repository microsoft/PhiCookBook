# Visão Geral do Projeto Phi-3-Vision-128K-Instruct

## O Modelo

O Phi-3-Vision-128K-Instruct, um modelo multimodal leve e de última geração, está no centro deste projeto. Faz parte da família de modelos Phi-3 e suporta um comprimento de contexto de até 128.000 tokens. O modelo foi treinado com um conjunto de dados diversificado que inclui dados sintéticos e websites públicos cuidadosamente filtrados, com ênfase em conteúdo de alta qualidade e que exige raciocínio. O processo de treino incluiu fine-tuning supervisionado e otimização direta de preferências para garantir uma adesão precisa às instruções, bem como medidas robustas de segurança.

## Criar dados de exemplo é crucial por várias razões:

1. **Testes**: Dados de exemplo permitem testar a sua aplicação em vários cenários sem afetar dados reais. Isto é especialmente importante nas fases de desenvolvimento e staging.

2. **Ajuste de Performance**: Com dados de exemplo que imitam a escala e complexidade dos dados reais, pode identificar gargalos de performance e otimizar a sua aplicação em conformidade.

3. **Prototipagem**: Dados de exemplo podem ser usados para criar protótipos e mockups, ajudando a compreender os requisitos dos utilizadores e a obter feedback.

4. **Análise de Dados**: Em ciência de dados, dados de exemplo são frequentemente usados para análise exploratória, treino de modelos e testes de algoritmos.

5. **Segurança**: Usar dados de exemplo em ambientes de desenvolvimento e teste pode ajudar a prevenir fugas acidentais de dados sensíveis reais.

6. **Aprendizagem**: Se está a aprender uma nova tecnologia ou ferramenta, trabalhar com dados de exemplo pode fornecer uma forma prática de aplicar o que aprendeu.

Lembre-se, a qualidade dos seus dados de exemplo pode impactar significativamente estas atividades. Devem ser o mais próximo possível dos dados reais em termos de estrutura e variabilidade.

### Criação de Dados de Exemplo
[Generate DataSet Script](./CreatingSampleData.md)

## Conjunto de Dados

Um bom exemplo de conjunto de dados de exemplo é o [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (disponível no Huggingface).  
O conjunto de dados de exemplo dos produtos Burberry inclui metadados sobre a categoria dos produtos, preço e título, com um total de 3.040 linhas, cada uma representando um produto único. Este conjunto de dados permite testar a capacidade do modelo de compreender e interpretar dados visuais, gerando texto descritivo que capta detalhes visuais complexos e características específicas da marca.

**Note:** Pode usar qualquer conjunto de dados que inclua imagens.

## Raciocínio Complexo

O modelo precisa de raciocinar sobre preços e nomes apenas a partir da imagem. Isto exige que o modelo não só reconheça características visuais, mas também compreenda as suas implicações em termos de valor do produto e branding. Ao sintetizar descrições textuais precisas a partir das imagens, o projeto destaca o potencial de integrar dados visuais para melhorar o desempenho e a versatilidade dos modelos em aplicações do mundo real.

## Arquitetura Phi-3 Vision

A arquitetura do modelo é uma versão multimodal do Phi-3. Processa dados de texto e imagem, integrando estas entradas numa sequência unificada para tarefas de compreensão e geração abrangentes. O modelo usa camadas de embedding separadas para texto e imagens. Os tokens de texto são convertidos em vetores densos, enquanto as imagens são processadas através de um modelo de visão CLIP para extrair embeddings de características. Estes embeddings de imagem são depois projetados para corresponder às dimensões dos embeddings de texto, garantindo que possam ser integrados sem problemas.

## Integração dos Embeddings de Texto e Imagem

Tokens especiais dentro da sequência de texto indicam onde os embeddings de imagem devem ser inseridos. Durante o processamento, estes tokens especiais são substituídos pelos embeddings de imagem correspondentes, permitindo que o modelo trate texto e imagens como uma única sequência. O prompt para o nosso conjunto de dados é formatado usando o token especial <|image|> da seguinte forma:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Código de Exemplo
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Exemplo passo a passo do Weights and Bias](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.