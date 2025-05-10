<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-09T21:51:39+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "pa"
}
-->
**QLoRA ਨਾਲ Phi-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ**

Microsoft ਦੇ Phi-3 Mini ਭਾਸ਼ਾ ਮਾਡਲ ਨੂੰ [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) ਦੀ ਵਰਤੋਂ ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਕਰਨਾ।

QLoRA ਗੱਲਬਾਤ ਦੀ ਸਮਝ ਅਤੇ ਜਵਾਬ ਬਣਾਉਣ ਵਿੱਚ ਸੁਧਾਰ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰੇਗਾ।

transformers ਅਤੇ bitsandbytes ਨਾਲ 4bits ਵਿੱਚ ਮਾਡਲ ਲੋਡ ਕਰਨ ਲਈ, ਤੁਹਾਨੂੰ accelerate ਅਤੇ transformers ਨੂੰ ਸੋਰਸ ਤੋਂ ਇੰਸਟਾਲ ਕਰਨਾ ਪਵੇਗਾ ਅਤੇ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਪਵੇਗਾ ਕਿ ਤੁਹਾਡੇ ਕੋਲ bitsandbytes ਲਾਇਬ੍ਰੇਰੀ ਦਾ ਨਵਾਂ ਵਰਜਨ ਹੈ।

**ਨਮੂਨੇ**
- [ਇਸ ਸੈਂਪਲ ਨੋਟਬੁੱਕ ਨਾਲ ਹੋਰ ਸਿੱਖੋ](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python FineTuning ਸੈਂਪਲ ਦਾ ਉਦਾਹਰਨ](../../../../code/03.Finetuning/FineTrainingScript.py)
- [LORA ਨਾਲ Hugging Face Hub Fine Tuning ਦਾ ਉਦਾਹਰਨ](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [QLORA ਨਾਲ Hugging Face Hub Fine Tuning ਦਾ ਉਦਾਹਰਨ](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**ਅਸਵੀਕਾਰੋक्ति**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਅਧਿਕਾਰਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉੱਪਜਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਭ੍ਰਮਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।