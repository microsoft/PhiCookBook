<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:16:24+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "es"
}
-->
**Ajuste fino de Phi-3 con QLoRA**

Ajuste fino del modelo de lenguaje Phi-3 Mini de Microsoft usando [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA ayudará a mejorar la comprensión conversacional y la generación de respuestas.

Para cargar modelos en 4 bits con transformers y bitsandbytes, debes instalar accelerate y transformers desde la fuente y asegurarte de tener la versión más reciente de la biblioteca bitsandbytes.

**Ejemplos**
- [Aprende más con este cuaderno de ejemplo](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Ejemplo de ajuste fino en Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Ejemplo de ajuste fino en Hugging Face Hub con LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Ejemplo de ajuste fino en Hugging Face Hub con QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.