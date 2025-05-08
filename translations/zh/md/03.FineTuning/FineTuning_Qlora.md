<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-07T13:15:11+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "zh"
}
-->
**使用 QLoRA 微调 Phi-3**

使用 [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) 对微软的 Phi-3 Mini 语言模型进行微调。

QLoRA 有助于提升对话理解和响应生成能力。

要使用 transformers 和 bitsandbytes 以 4bits 加载模型，需从源码安装 accelerate 和 transformers，并确保 bitsandbytes 库是最新版本。

**示例**
- [通过此示例笔记本了解更多](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 微调示例](../../../../code/03.Finetuning/FineTrainingScript.py)
- [使用 LORA 进行 Hugging Face Hub 微调示例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [使用 QLORA 进行 Hugging Face Hub 微调示例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免责声明**：  
本文件使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的原文版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们不承担任何责任。