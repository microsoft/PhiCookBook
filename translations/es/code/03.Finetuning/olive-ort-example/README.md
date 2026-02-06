# Ajustar finamente Phi3 usando Olive

En este ejemplo usarás Olive para:

1. Ajustar finamente un adaptador LoRA para clasificar frases en Tristeza, Alegría, Miedo, Sorpresa.  
1. Fusionar los pesos del adaptador en el modelo base.  
1. Optimizar y cuantizar el modelo a `int4`.  

También te mostraremos cómo hacer inferencias con el modelo ajustado usando la API Generate de ONNX Runtime (ORT).

> **⚠️ Para el ajuste fino, necesitarás tener una GPU adecuada disponible - por ejemplo, una A10, V100, A100.**

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

## 🧪 Ajustar finamente Phi3 usando Olive  
El [archivo de configuración de Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) contiene un *workflow* con las siguientes *etapas*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

A grandes rasgos, este flujo de trabajo hará lo siguiente:

1. Ajustar finamente Phi3 (durante 150 pasos, que puedes modificar) usando los datos de [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).  
1. Fusionar los pesos del adaptador LoRA en el modelo base. Esto te dará un único artefacto de modelo en formato ONNX.  
1. Model Builder optimizará el modelo para ONNX Runtime *y* cuantizará el modelo a `int4`.  

Para ejecutar el flujo de trabajo, corre:

```bash
olive run --config phrase-classification.json
```

Cuando Olive termine, tu modelo Phi3 ajustado y optimizado en `int4` estará disponible en: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integra el Phi3 ajustado en tu aplicación

Para ejecutar la app:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

La respuesta debe ser una clasificación de una sola palabra para la frase (Tristeza/Alegría/Miedo/Sorpresa).

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.