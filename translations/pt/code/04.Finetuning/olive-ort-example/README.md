<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:44:39+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "pt"
}
-->
# Ajustar Phi3 usando Olive

Neste exemplo, você usará o Olive para:

1. Ajustar um adaptador LoRA para classificar frases em Triste, Alegria, Medo, Surpresa.
1. Mesclar os pesos do adaptador no modelo base.
1. Otimizar e quantizar o modelo em `int4`.

Também mostraremos como fazer inferência com o modelo ajustado usando a API Generate do ONNX Runtime (ORT).

> **⚠️ Para o ajuste fino, você precisará de uma GPU adequada disponível - por exemplo, uma A10, V100, A100.**

## 💾 Instalar

Crie um novo ambiente virtual Python (por exemplo, usando `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Em seguida, instale o Olive e as dependências para o fluxo de trabalho de ajuste fino:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Ajustar Phi3 usando Olive  
O [arquivo de configuração do Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) contém um *workflow* com as seguintes *etapas*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

De forma geral, este workflow irá:

1. Ajustar o Phi3 (por 150 passos, que você pode modificar) usando os dados de [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Mesclar os pesos do adaptador LoRA no modelo base. Isso resultará em um único artefato de modelo no formato ONNX.
1. O Model Builder irá otimizar o modelo para o runtime ONNX *e* quantizar o modelo em `int4`.

Para executar o workflow, rode:

```bash
olive run --config phrase-classification.json
```

Quando o Olive terminar, seu modelo Phi3 ajustado e otimizado em `int4` estará disponível em: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrar o Phi3 ajustado na sua aplicação

Para executar o app:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

A resposta deve ser uma classificação de uma palavra para a frase (Triste/Alegria/Medo/Surpresa).

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.