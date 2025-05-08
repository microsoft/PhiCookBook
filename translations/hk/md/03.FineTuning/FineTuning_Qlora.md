<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-08T05:05:26+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "hk"
}
-->
**使用 QLoRA 微調 Phi-3**

使用 [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) 微調 Microsoft 的 Phi-3 Mini 語言模型。

QLoRA 有助提升對話理解及回應生成能力。

要用 transformers 和 bitsandbytes 以 4bits 載入模型，需從原始碼安裝 accelerate 和 transformers，並確保 bitsandbytes 庫是最新版本。

**範例**
- [透過此範例筆記本了解更多](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 微調範例示例](../../../../code/03.Finetuning/FineTrainingScript.py)
- [使用 LORA 在 Hugging Face Hub 進行微調的範例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [使用 QLORA 在 Hugging Face Hub 進行微調的範例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋努力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件嘅母語版本應視為權威來源。對於重要資訊，建議採用專業人手翻譯。我哋對因使用此翻譯而引致嘅任何誤解或誤釋概不負責。