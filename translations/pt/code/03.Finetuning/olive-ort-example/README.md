<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:31:35+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "pt"
}
-->
# Ajuste fino do Phi3 usando Olive

Neste exemplo, você usará o Olive para:

1. Ajustar fino um adaptador LoRA para classificar frases em Triste, Alegria, Medo, Surpresa.  
1. Mesclar os pesos do adaptador ao modelo base.  
1. Otimizar e quantizar o modelo em `int4`.

Também mostraremos como realizar inferência com o modelo ajustado usando a API Generate do ONNX Runtime (ORT).

> **⚠️ Para o ajuste fino, é necessário ter uma GPU adequada disponível - por exemplo, A10, V100, A100.**

## 💾 Instalação

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

## 🧪 Ajuste fino do Phi3 usando Olive  
O [arquivo de configuração do Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) contém um *workflow* com as seguintes *etapas*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

De forma geral, esse fluxo irá:

1. Ajustar fino o Phi3 (por 150 passos, que você pode modificar) usando os dados de [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).  
1. Mesclar os pesos do adaptador LoRA ao modelo base. Isso resultará em um único artefato de modelo no formato ONNX.  
1. O Model Builder otimizará o modelo para o runtime ONNX *e* quantizará o modelo em `int4`.

Para executar o workflow, rode:

```bash
olive run --config phrase-classification.json
```

Quando o Olive finalizar, seu modelo Phi3 ajustado e otimizado em `int4` estará disponível em: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integre o Phi3 ajustado à sua aplicação

Para rodar o app:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

A resposta deverá ser uma classificação única da frase (Sad/Joy/Fear/Surprise).

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.