<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f0858a9f2cc1889ab0e90cb9c63c044",
  "translation_date": "2025-04-04T19:02:38+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Qlora.md",
  "language_code": "hk"
}
-->
**微調 Phi-3 使用 QLoRA**

使用 [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) 微調 Microsoft 的 Phi-3 Mini 語言模型。

QLoRA 可以幫助提升對話理解能力以及生成回應的表現。

要使用 transformers 和 bitsandbytes 在 4bits 模式下載入模型，您需要從源代碼安裝 accelerate 和 transformers，並確保安裝最新版本的 bitsandbytes 庫。

**範例**
- [透過此範例筆記本了解更多](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 微調範例](../../../../code/03.Finetuning/FineTrainingScript.py)
- [使用 LORA 在 Hugging Face Hub 上微調範例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [使用 QLORA 在 Hugging Face Hub 上微調範例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免責聲明**:  
本文檔已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們不對因使用此翻譯而引起的任何誤解或誤釋承擔責任。