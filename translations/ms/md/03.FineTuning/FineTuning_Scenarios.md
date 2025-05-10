<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cb5648935f63edc17e95ce38f23adc32",
  "translation_date": "2025-05-09T21:56:54+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Scenarios.md",
  "language_code": "ms"
}
-->
## سيناريوهات التخصيص الدقيق

![FineTuning with MS Services](../../../../translated_images/FinetuningwithMS.25759a0154a97ad90e43a6cace37d6bea87f0ac0236ada3ad5d4a1fbacc3bdf7.ms.png)

**المنصة** تشمل تقنيات مختلفة مثل Azure AI Foundry وAzure Machine Learning وأدوات الذكاء الاصطناعي وKaito وONNX Runtime.

**البنية التحتية** تشمل المعالج المركزي (CPU) وFPGA، وهما ضروريان لعملية التخصيص الدقيق. دعني أريك الرموز الخاصة بكل من هذه التقنيات.

**الأدوات والأُطُر** تشمل ONNX Runtime وONNX Runtime. دعني أريك الرموز الخاصة بكل من هذه التقنيات.  
[Insert icons for ONNX Runtime and ONNX Runtime]

تتضمن عملية التخصيص الدقيق باستخدام تقنيات Microsoft مكونات وأدوات مختلفة. من خلال فهم هذه التقنيات واستخدامها، يمكننا تخصيص تطبيقاتنا بشكل فعال وابتكار حلول أفضل.

## النموذج كخدمة

قم بتخصيص النموذج باستخدام التخصيص المستضاف، دون الحاجة إلى إنشاء وإدارة الحوسبة.

![MaaS Fine Tuning](../../../../translated_images/MaaSfinetune.6184d80a336ea9d7bb67a581e9e5d0b021cafdffff7ba257c2012e2123e0d77e.ms.png)

التخصيص بدون خادم متاح لنماذج Phi-3-mini وPhi-3-medium، مما يمكّن المطورين من تخصيص النماذج بسرعة وسهولة لسيناريوهات السحابة والحافة دون الحاجة لترتيب الحوسبة. كما أعلنا أن Phi-3-small متوفر الآن من خلال عرض Models-as-a-Service لدينا، مما يتيح للمطورين البدء بسرعة وسهولة في تطوير الذكاء الاصطناعي دون الحاجة لإدارة البنية التحتية الأساسية.

## النموذج كمنصة

يقوم المستخدمون بإدارة الحوسبة الخاصة بهم من أجل تخصيص نماذجهم.

![Maap Fine Tuning](../../../../translated_images/MaaPFinetune.cf8b08ef05bf57f362da90834be87562502f4370de4a7325a9fb03b8c008e5e7.ms.png)

[Fine Tuning Sample](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## سيناريوهات التخصيص الدقيق

| | | | | | | |
|-|-|-|-|-|-|-|
|السيناريو|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|تكييف نماذج LLM المدربة مسبقًا لمهام أو مجالات محددة|نعم|نعم|نعم|نعم|نعم|نعم|
|التخصيص لمهام معالجة اللغة الطبيعية مثل تصنيف النص، التعرف على الكيانات المسماة، والترجمة الآلية|نعم|نعم|نعم|نعم|نعم|نعم|
|التخصيص لمهام الأسئلة والأجوبة|نعم|نعم|نعم|نعم|نعم|نعم|
|التخصيص لتوليد ردود شبيهة بالبشر في الدردشة الآلية|نعم|نعم|نعم|نعم|نعم|نعم|
|التخصيص لتوليد الموسيقى، الفن، أو أشكال أخرى من الإبداع|نعم|نعم|نعم|نعم|نعم|نعم|
|تقليل التكاليف الحسابية والمالية|نعم|نعم|لا|نعم|نعم|لا|
|تقليل استخدام الذاكرة|لا|نعم|لا|نعم|نعم|نعم|
|استخدام عدد أقل من المعاملات لتخصيص فعال|لا|نعم|نعم|لا|لا|نعم|
|شكل فعال من حيث الذاكرة لتوازي البيانات يسمح بالوصول إلى الذاكرة المجمعة لجميع أجهزة GPU المتاحة|لا|لا|لا|نعم|نعم|نعم|

## أمثلة على أداء التخصيص الدقيق

![Finetuning Performance](../../../../translated_images/Finetuningexamples.9dbf84557eef43e011eb7cadf51f51686f9245f7953e2712a27095ab7d18a6d1.ms.png)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat kritikal, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.