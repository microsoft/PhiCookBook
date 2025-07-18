<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:16:19+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "fr"
}
-->
**Affinage de Phi-3 avec QLoRA**

Affinage du modèle de langage Phi-3 Mini de Microsoft en utilisant [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA permet d’améliorer la compréhension des conversations et la génération de réponses.

Pour charger des modèles en 4 bits avec transformers et bitsandbytes, vous devez installer accelerate et transformers depuis la source et vous assurer d’avoir la dernière version de la bibliothèque bitsandbytes.

**Exemples**
- [En savoir plus avec ce notebook d’exemple](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Exemple de script Python pour l’affinage](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Exemple d’affinage sur Hugging Face Hub avec LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Exemple d’affinage sur Hugging Face Hub avec QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.