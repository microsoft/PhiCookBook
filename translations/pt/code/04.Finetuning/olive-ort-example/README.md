<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-16T16:25:44+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "pt"
}
-->
# Ajustar finamente o Phi3 usando Olive

Neste exemplo, vais usar o Olive para:

1. Ajustar finamente um adaptador LoRA para classificar frases em Triste, Alegria, Medo, Surpresa.  
1. Fundir os pesos do adaptador no modelo base.  
1. Otimizar e quantizar o modelo para `int4`.  

Também te mostramos como fazer inferência com o modelo ajustado usando a API ONNX Runtime (ORT) Generate.

> **⚠️ Para o ajuste fino, precisas de ter uma GPU adequada disponível - por exemplo, uma A10, V100, A100.**

## 💾 Instalar

Cria um novo ambiente virtual Python (por exemplo, usando `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

De seguida, instala o Olive e as dependências para o fluxo de trabalho de ajuste fino:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Ajustar finamente o Phi3 usando Olive  
O [ficheiro de configuração do Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) contém um *workflow* com as seguintes *etapas*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

De forma geral, este workflow irá:

1. Ajustar finamente o Phi3 (durante 150 passos, que podes modificar) usando os dados de [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).  
1. Fundir os pesos do adaptador LoRA no modelo base. Isto vai gerar um único artefacto de modelo no formato ONNX.  
1. O Model Builder vai otimizar o modelo para o runtime ONNX *e* quantizar o modelo para `int4`.  

Para executar o workflow, corre:

```bash
olive run --config phrase-classification.json
```

Quando o Olive terminar, o teu modelo Phi3 ajustado e otimizado em `int4` estará disponível em: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrar o Phi3 ajustado na tua aplicação

Para correr a aplicação:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

A resposta deverá ser uma classificação de uma única palavra da frase (Triste/Alegria/Medo/Surpresa).

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.