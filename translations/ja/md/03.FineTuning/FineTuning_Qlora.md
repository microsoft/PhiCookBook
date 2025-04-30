<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f0858a9f2cc1889ab0e90cb9c63c044",
  "translation_date": "2025-04-04T13:27:59+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Qlora.md",
  "language_code": "ja"
}
-->
**Phi-3のQLoRAによる微調整**

[QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) を使用して、MicrosoftのPhi-3 Mini言語モデルを微調整します。

QLoRAは、会話の理解と応答生成の向上に役立ちます。

transformersとbitsandbytesを使用してモデルを4bitで読み込むには、accelerateとtransformersをソースからインストールし、bitsandbytesライブラリの最新バージョンを確認する必要があります。

**サンプル**
- [このサンプルノートブックで詳細を学ぶ](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Pythonによる微調整サンプルの例](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face HubでのLORAを使用した微調整の例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face HubでのQLORAを使用した微調整の例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免責事項**:  
この文書はAI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の母国語での文書を公式な情報源としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の利用に起因する誤解や誤解釈について、当方は一切の責任を負いません。