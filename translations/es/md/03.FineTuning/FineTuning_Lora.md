<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:27:00+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "es"
}
-->
# **Ajuste fino de Phi-3 con Lora**

Ajuste fino del modelo de lenguaje Phi-3 Mini de Microsoft usando [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) en un conjunto de datos personalizado de instrucciones para chat.

LORA ayudará a mejorar la comprensión conversacional y la generación de respuestas.

## Guía paso a paso para ajustar fino Phi-3 Mini:

**Importaciones y Configuración**

Instalando loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Comienza importando las librerías necesarias como datasets, transformers, peft, trl y torch.  
Configura el registro para seguir el proceso de entrenamiento.

Puedes elegir adaptar algunas capas reemplazándolas por contrapartes implementadas en loralib. Por ahora solo soportamos nn.Linear, nn.Embedding y nn.Conv2d. También soportamos MergedLinear para casos donde un solo nn.Linear representa más de una capa, como en algunas implementaciones de la proyección qkv de atención (consulta Notas Adicionales para más detalles).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

Antes de que comience el ciclo de entrenamiento, marca solo los parámetros de LoRA como entrenables.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Al guardar un checkpoint, genera un state_dict que contenga únicamente los parámetros de LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Al cargar un checkpoint usando load_state_dict, asegúrate de establecer strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Ahora el entrenamiento puede continuar como de costumbre.

**Hiperparámetros**

Define dos diccionarios: training_config y peft_config. training_config incluye hiperparámetros para el entrenamiento, como tasa de aprendizaje, tamaño de lote y configuraciones de registro.

peft_config especifica parámetros relacionados con LoRA como rank, dropout y tipo de tarea.

**Carga del Modelo y Tokenizador**

Especifica la ruta al modelo preentrenado Phi-3 (por ejemplo, "microsoft/Phi-3-mini-4k-instruct"). Configura los ajustes del modelo, incluyendo uso de caché, tipo de dato (bfloat16 para precisión mixta) e implementación de atención.

**Entrenamiento**

Ajusta fino el modelo Phi-3 usando el conjunto de datos personalizado de instrucciones para chat. Utiliza las configuraciones de LoRA de peft_config para una adaptación eficiente. Monitorea el progreso del entrenamiento usando la estrategia de registro especificada.  
Evaluación y Guardado: Evalúa el modelo ajustado.  
Guarda checkpoints durante el entrenamiento para uso posterior.

**Ejemplos**  
- [Aprende más con este notebook de ejemplo](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Ejemplo de script de ajuste fino en Python](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Ejemplo de ajuste fino en Hugging Face Hub con LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Ejemplo de tarjeta de modelo en Hugging Face - Ejemplo de ajuste fino con LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Ejemplo de ajuste fino en Hugging Face Hub con QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.