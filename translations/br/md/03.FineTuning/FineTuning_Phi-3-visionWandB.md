<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-07-17T08:09:11+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "br"
}
-->
# Visão Geral do Projeto Phi-3-Vision-128K-Instruct

## O Modelo

O Phi-3-Vision-128K-Instruct, um modelo multimodal leve e de última geração, está no centro deste projeto. Ele faz parte da família de modelos Phi-3 e suporta um comprimento de contexto de até 128.000 tokens. O modelo foi treinado em um conjunto de dados diversificado que inclui dados sintéticos e sites públicos cuidadosamente filtrados, com ênfase em conteúdo de alta qualidade e que exige raciocínio. O processo de treinamento incluiu fine-tuning supervisionado e otimização direta de preferências para garantir aderência precisa às instruções, além de medidas robustas de segurança.

## Criar dados de exemplo é crucial por vários motivos:

1. **Testes**: Dados de exemplo permitem testar sua aplicação em vários cenários sem afetar dados reais. Isso é especialmente importante nas fases de desenvolvimento e homologação.

2. **Ajuste de Performance**: Com dados de exemplo que imitam a escala e complexidade dos dados reais, você pode identificar gargalos de desempenho e otimizar sua aplicação adequadamente.

3. **Prototipagem**: Dados de exemplo podem ser usados para criar protótipos e mockups, ajudando a entender os requisitos dos usuários e obter feedback.

4. **Análise de Dados**: Em ciência de dados, dados de exemplo são frequentemente usados para análise exploratória, treinamento de modelos e testes de algoritmos.

5. **Segurança**: Usar dados de exemplo em ambientes de desenvolvimento e teste ajuda a evitar vazamentos acidentais de dados sensíveis reais.

6. **Aprendizado**: Se você está aprendendo uma nova tecnologia ou ferramenta, trabalhar com dados de exemplo oferece uma forma prática de aplicar o que aprendeu.

Lembre-se, a qualidade dos seus dados de exemplo pode impactar significativamente essas atividades. Eles devem ser o mais próximo possível dos dados reais em termos de estrutura e variabilidade.

### Criação de Dados de Exemplo
[Generate DataSet Script](./CreatingSampleData.md)

## Conjunto de Dados

Um bom exemplo de conjunto de dados de exemplo é o [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (disponível no Huggingface).  
O conjunto de dados de exemplo dos produtos Burberry, junto com metadados sobre a categoria, preço e título dos produtos, possui um total de 3.040 linhas, cada uma representando um produto único. Esse conjunto nos permite testar a capacidade do modelo de entender e interpretar dados visuais, gerando textos descritivos que capturam detalhes visuais intrincados e características específicas da marca.

**Note:** Você pode usar qualquer conjunto de dados que inclua imagens.

## Raciocínio Complexo

O modelo precisa raciocinar sobre preços e nomes apenas a partir da imagem. Isso exige que o modelo não apenas reconheça características visuais, mas também compreenda suas implicações em termos de valor do produto e branding. Ao sintetizar descrições textuais precisas a partir das imagens, o projeto destaca o potencial de integrar dados visuais para melhorar o desempenho e a versatilidade dos modelos em aplicações do mundo real.

## Arquitetura Phi-3 Vision

A arquitetura do modelo é uma versão multimodal do Phi-3. Ele processa dados de texto e imagem, integrando essas entradas em uma sequência unificada para tarefas de compreensão e geração abrangentes. O modelo usa camadas de embedding separadas para texto e imagens. Tokens de texto são convertidos em vetores densos, enquanto as imagens são processadas por um modelo de visão CLIP para extrair embeddings de características. Esses embeddings de imagem são então projetados para corresponder às dimensões dos embeddings de texto, garantindo que possam ser integrados perfeitamente.

## Integração dos Embeddings de Texto e Imagem

Tokens especiais dentro da sequência de texto indicam onde os embeddings de imagem devem ser inseridos. Durante o processamento, esses tokens especiais são substituídos pelos embeddings de imagem correspondentes, permitindo que o modelo trate texto e imagens como uma única sequência. O prompt para nosso conjunto de dados é formatado usando o token especial <|image|> da seguinte forma:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Código de Exemplo
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Exemplo passo a passo do Weights and Bias](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.