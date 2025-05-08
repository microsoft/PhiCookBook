<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-08T05:05:31+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "ja"
}
-->
**QLoRAによるPhi-3のファインチューニング**

MicrosoftのPhi-3 Mini言語モデルを[QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora)を使ってファインチューニングします。

QLoRAは会話の理解力と応答生成の向上に役立ちます。

transformersとbitsandbytesで4ビットモデルを読み込むには、accelerateとtransformersをソースからインストールし、bitsandbytesライブラリの最新バージョンを使用していることを確認してください。

**サンプル**
- [このサンプルノートブックで詳しく学ぶ](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Pythonファインチューニングサンプルの例](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face HubでのLORAを使ったファインチューニング例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face HubでのQLORAを使ったファインチューニング例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源として扱われるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、一切の責任を負いかねますのでご了承ください。