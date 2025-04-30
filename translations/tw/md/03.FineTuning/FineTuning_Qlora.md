<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f0858a9f2cc1889ab0e90cb9c63c044",
  "translation_date": "2025-04-04T07:11:37+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Qlora.md",
  "language_code": "tw"
}
-->
**微調 Phi-3 使用 QLoRA**

使用 [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) 微調 Microsoft 的 Phi-3 Mini 語言模型。

QLoRA 能幫助提升對話理解能力以及生成回應的品質。

若要使用 transformers 和 bitsandbytes 以 4 位元模式載入模型，您需要從源碼安裝 accelerate 和 transformers，並確保 bitsandbytes 庫是最新版本。

**範例**
- [透過此範例筆記本了解更多](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 微調範例](../../../../code/03.Finetuning/FineTrainingScript.py)
- [使用 LORA 的 Hugging Face Hub 微調範例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [使用 QLORA 的 Hugging Face Hub 微調範例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免責聲明**:  
本文檔使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，機器翻譯可能會包含錯誤或不準確之處。原始語言的文件應被視為具有權威性的來源。對於關鍵信息，建議使用專業的人工翻譯。我們不對因使用此翻譯而引起的任何誤解或錯誤解釋承擔責任。