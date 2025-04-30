<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-03-27T03:40:25+00:00",
  "source_file": "code\\03.Finetuning\\olive-ort-example\\README.md",
  "language_code": "es"
}
-->
# Ajustar Phi3 utilizando Olive

En este ejemplo, usarás Olive para:

1. Ajustar un adaptador LoRA para clasificar frases en Sad, Joy, Fear, Surprise.
1. Combinar los pesos del adaptador con el modelo base.
1. Optimizar y cuantificar el modelo en `int4`.

También te mostraremos cómo realizar inferencias con el modelo ajustado utilizando la API Generate de ONNX Runtime (ORT).

> **⚠️ Para el ajuste, necesitarás tener disponible una GPU adecuada, por ejemplo, una A10, V100, A100.**

## 💾 Instalación

Crea un nuevo entorno virtual de Python (por ejemplo, usando `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

A continuación, instala Olive y las dependencias necesarias para el flujo de trabajo de ajuste:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Ajustar Phi3 utilizando Olive
El [archivo de configuración de Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) contiene un *flujo de trabajo* con los siguientes *pases*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

A un nivel alto, este flujo de trabajo realizará lo siguiente:

1. Ajustar Phi3 (durante 150 pasos, que puedes modificar) utilizando los datos de [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Combinar los pesos del adaptador LoRA con el modelo base. Esto te dará un único artefacto del modelo en formato ONNX.
1. Model Builder optimizará el modelo para ONNX runtime *y* cuantificará el modelo en `int4`.

Para ejecutar el flujo de trabajo, ejecuta:

```bash
olive run --config phrase-classification.json
```

Cuando Olive haya terminado, tu modelo Phi3 ajustado y optimizado en `int4` estará disponible en: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrar Phi3 ajustado en tu aplicación 

Para ejecutar la aplicación:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Esta respuesta debería ser una clasificación de una sola palabra de la frase (Sad/Joy/Fear/Surprise).

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.