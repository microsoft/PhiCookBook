<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:44:45+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "br"
}
-->
# Fine-tune Phi3 use Olive

En este ejemplo usarás Olive para:

1. Ajustar un adaptador LoRA para clasificar frases en Tristeza, Alegría, Miedo, Sorpresa.  
1. Fusionar los pesos del adaptador en el modelo base.  
1. Optimizar y cuantizar el modelo en `int4`.

También te mostraremos cómo inferir el modelo ajustado usando la API Generate de ONNX Runtime (ORT).

> **⚠️ Para el ajuste fino, necesitarás una GPU adecuada disponible, por ejemplo, una A10, V100, A100.**

## 💾 Instalación

Crea un nuevo entorno virtual de Python (por ejemplo, usando `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Luego, instala Olive y las dependencias para un flujo de trabajo de ajuste fino:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Ajustar Phi3 usando Olive
El [archivo de configuración de Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) contiene un *workflow* con las siguientes *pasadas*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

A grandes rasgos, este workflow hará:

1. Ajustar Phi3 (por 150 pasos, que puedes modificar) usando los datos de [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).  
1. Fusionar los pesos del adaptador LoRA en el modelo base. Esto te dará un único artefacto de modelo en formato ONNX.  
1. Model Builder optimizará el modelo para ONNX Runtime *y* cuantizará el modelo en `int4`.

Para ejecutar el workflow, corre:

```bash
olive run --config phrase-classification.json
```

Cuando Olive termine, tu modelo ajustado optimizado `int4` estará disponible en: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integra Phi3 ajustado en tu aplicación

Para ejecutar la app:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

La respuesta debe ser una clasificación de una sola palabra para la frase (Sad/Joy/Fear/Surprise).

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.