<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-03-27T03:58:49+00:00",
  "source_file": "code\\04.Finetuning\\olive-ort-example\\README.md",
  "language_code": "es"
}
-->
# Ajustar Phi3 utilizando Olive

En este ejemplo usarás Olive para:

1. Ajustar un adaptador LoRA para clasificar frases en Sad, Joy, Fear, Surprise.
1. Combinar los pesos del adaptador en el modelo base.
1. Optimizar y cuantizar el modelo en `int4`.

También te mostraremos cómo realizar inferencias con el modelo ajustado utilizando la API Generate de ONNX Runtime (ORT).

> **⚠️ Para el ajuste, necesitarás tener disponible una GPU adecuada, como por ejemplo, una A10, V100, A100.**

## 💾 Instalar

Crea un nuevo entorno virtual de Python (por ejemplo, usando `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

A continuación, instala Olive y las dependencias para un flujo de trabajo de ajuste:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Ajustar Phi3 utilizando Olive
El [archivo de configuración de Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) contiene un *workflow* con los siguientes *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

A grandes rasgos, este flujo de trabajo hará lo siguiente:

1. Ajustar Phi3 (por 150 pasos, que puedes modificar) utilizando los datos de [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Combinar los pesos del adaptador LoRA en el modelo base. Esto te dará un único artefacto del modelo en formato ONNX.
1. Model Builder optimizará el modelo para ONNX runtime *y* cuantizará el modelo en `int4`.

Para ejecutar el flujo de trabajo, ejecuta:

```bash
olive run --config phrase-classification.json
```

Cuando Olive haya finalizado, tu modelo ajustado y optimizado `int4` Phi3 estará disponible en: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrar el modelo ajustado Phi3 en tu aplicación 

Para ejecutar la aplicación:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Esta respuesta debería ser una clasificación de una sola palabra de la frase (Sad/Joy/Fear/Surprise).

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.