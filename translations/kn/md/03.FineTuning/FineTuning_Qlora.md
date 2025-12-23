<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-12-21T17:20:32+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "kn"
}
-->
**Phi-3 ಅನ್ನು QLoRA ಬಳಸಿ ಫೈನ್-ಟ್ಯೂನಿಂಗ್**

Microsoft ನ Phi-3 Mini ಭಾಷಾ ಮಾದರಿಯನ್ನು [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) ಬಳಸಿ ಫೈನ್-ಟ್ಯೂನಿಂಗ್ ಮಾಡುವುದು. 

QLoRA ಸಂಭಾಷಣಾತ್ಮಕ ಅರ್ಥಗ್ರಹಣ ಮತ್ತು ಪ್ರತಿಕ್ರಿಯಾ ಉತ್ಪಾದನೆಯನ್ನು ಸುಧಾರಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ. 

transformers ಮತ್ತು bitsandbytes ಬಳಸಿ ಮಾದರಿಗಳನ್ನು 4bits ನಲ್ಲಿ ಲೋಡ್ ಮಾಡಲು, ನೀವು accelerate ಮತ್ತು transformers ಅನ್ನು ಮೂಲದಿಂದ ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಬೇಕು ಮತ್ತು bitsandbytes ಲೈಬ್ರರಿಯ ಇತ್ತೀಚಿನ ಆವೃತ್ತಿಯಿರುವುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

**ಉದಾಹರಣೆಗಳು**
- [ಈ ಮಾದರಿ ನೋಟ್‌ಬುಕ್ ಮೂಲಕ ಇನ್ನಷ್ಟು ತಿಳಿಯಿರಿ](../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python ಫೈನ್-ಟ್ಯೂನಿಂಗ್ ಉದಾಹರಣೆ](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub ನಲ್ಲಿ LORA ಬಳಸಿ ಫೈನ್-ಟ್ಯೂನಿಂಗ್ ಉದಾಹರಣೆ](../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Hub ನಲ್ಲಿ QLORA ಬಳಸಿ ಫೈನ್-ಟ್ಯೂನಿಂಗ್ ಉದಾಹರಣೆ](../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಜವಾಬ್ದಾರಿ ನಿರಾಕರಣೆ:
ಈ ದಾಖಲೆಯನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಗೆ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ ಸಹ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅನಿಖರತೆಗಳು ಇರಬಹುದು ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನದಲ್ಲಿಡಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಾಖಲೆ ಅನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಗ್ರಹಿಕೆಗಳು ಅಥವಾ ತಪ್ಪಾಗಿ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆಗಳಿಗೆ ನಾವು ಜವಾಬ್ದಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->