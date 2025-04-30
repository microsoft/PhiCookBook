<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f0858a9f2cc1889ab0e90cb9c63c044",
  "translation_date": "2025-04-03T08:20:12+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Qlora.md",
  "language_code": "zh"
}
-->
**微调 Phi-3 使用 QLoRA**

使用 [QLoRA (量子低秩适应)](https://github.com/artidoro/qlora) 微调微软的 Phi-3 Mini 语言模型。

QLoRA 将帮助提升对话理解能力和响应生成质量。

要使用 transformers 和 bitsandbytes 以 4bits 加载模型，你需要从源代码安装 accelerate 和 transformers，并确保安装最新版本的 bitsandbytes 库。

**示例**
- [通过这个示例笔记本了解更多](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 微调示例](../../../../code/03.Finetuning/FineTrainingScript.py)
- [使用 LORA 微调 Hugging Face Hub 示例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [使用 QLORA 微调 Hugging Face Hub 示例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免责声明**：  
本文档使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们尽力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原文档的原始语言版本视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而引发的任何误解或误读承担责任。