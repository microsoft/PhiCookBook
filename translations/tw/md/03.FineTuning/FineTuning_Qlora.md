<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-08T05:05:36+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "tw"
}
-->
**使用 QLoRA 微調 Phi-3**

使用 [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) 來微調 Microsoft 的 Phi-3 Mini 語言模型。

QLoRA 有助於提升對話理解和回應生成的表現。

要用 transformers 和 bitsandbytes 以 4bits 載入模型，你需要從原始碼安裝 accelerate 和 transformers，並確認你安裝的是最新版本的 bitsandbytes 函式庫。

**範例**
- [透過此範例筆記本了解更多](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 微調範例示範](../../../../code/03.Finetuning/FineTrainingScript.py)
- [使用 LORA 在 Hugging Face Hub 微調範例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [使用 QLORA 在 Hugging Face Hub 微調範例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不精確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生之任何誤解或誤譯負責。