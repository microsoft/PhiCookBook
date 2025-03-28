<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-03-27T15:05:53+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Qlora.md",
  "language_code": "fr"
}
-->
**Affiner Phi-3 avec QLoRA**

Affiner le modèle de langage Phi-3 Mini de Microsoft en utilisant [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA permettra d'améliorer la compréhension conversationnelle et la génération de réponses.

Pour charger des modèles en 4 bits avec transformers et bitsandbytes, vous devez installer accelerate et transformers depuis la source et vous assurer d'avoir la dernière version de la bibliothèque bitsandbytes.

**Exemples**
- [En savoir plus avec cet exemple de notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Exemple de script Python pour l'affinage](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Exemple d'affinage avec LORA sur Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Exemple d'affinage avec QLORA sur Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.