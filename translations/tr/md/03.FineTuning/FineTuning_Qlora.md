<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-09T21:52:07+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "tr"
}
-->
**QLoRA ile Phi-3 İnce Ayarı**

Microsoft’un Phi-3 Mini dil modelini [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) kullanarak ince ayar yapma.

QLoRA, sohbet anlayışını ve yanıt üretimini geliştirmeye yardımcı olacak.

Transformers ve bitsandbytes ile modelleri 4 bit olarak yüklemek için accelerate ve transformers kütüphanelerini kaynaktan kurmanız ve bitsandbytes kütüphanesinin en güncel sürümüne sahip olmanız gerekiyor.

**Örnekler**
- [Bu örnek defteri ile Daha Fazla Bilgi Edinin](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python İnce Ayar Örneği](../../../../code/03.Finetuning/FineTrainingScript.py)
- [LORA ile Hugging Face Hub İnce Ayar Örneği](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [QLORA ile Hugging Face Hub İnce Ayar Örneği](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.