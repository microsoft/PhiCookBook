<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:18:48+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "tr"
}
-->
**QLoRA ile Phi-3 Modelini İnce Ayarlama**

Microsoft’un Phi-3 Mini dil modelini [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) kullanarak ince ayarlama.

QLoRA, sohbet anlayışını ve yanıt üretimini geliştirmeye yardımcı olacak.

transformers ve bitsandbytes ile modelleri 4 bit olarak yüklemek için accelerate ve transformers kütüphanelerini kaynaktan kurmanız ve bitsandbytes kütüphanesinin en güncel sürümüne sahip olmanız gerekiyor.

**Örnekler**
- [Bu örnek not defteri ile Daha Fazla Bilgi Edinin](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python İnce Ayar Örneği](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub ile LORA İnce Ayar Örneği](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Hub ile QLORA İnce Ayar Örneği](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.