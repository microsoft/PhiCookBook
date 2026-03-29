## Hali za Uboreshaji wa Hali ya Juu

![FineTuning with MS Services](../../../../translated_images/sw/FinetuningwithMS.3d0cec8ae693e094.webp)

Sehemu hii inatoa muhtasari wa hali za uboreshaji wa hali ya juu katika mazingira ya Microsoft Foundry na Azure, ikiwa ni pamoja na mifano ya uenezaji, tabaka za miundombinu, na mbinu zinazotumika mara kwa mara za uboreshaji.

**Jukwaa**  
Hii inajumuisha huduma zinazosimamiwa kama Microsoft Foundry (zamani Microsoft Foundry) na Azure Machine Learning, ambazo hutoa usimamizi wa modeli, upangaji, ufuatiliaji wa majaribio, na michakato ya uenezaji.

**Miundombinu**  
Uboreshaji wa hali ya juu unahitaji rasilimali za kompyuta zinazoweza kupanuka. Katika mazingira ya Azure, hii kawaida inajumuisha mashine pepe za GPU na rasilimali za CPU kwa kazi nyepesi, pamoja na hifadhi inayoweza kupanuka kwa seti za data na maeneo ya uhifadhi wa kumbukumbu.

**Zana & Mfumo**  
Mchakato wa uboreshaji wa hali ya juu kawaida hutegemea mifumo na maktaba za uboreshaji kama Hugging Face Transformers, DeepSpeed, na PEFT (Parameter-Efficient Fine-Tuning).

Mchakato wa uboreshaji wa hali ya juu ukitumia teknolojia za Microsoft unagusa huduma za jukwaa, miundombinu ya kompyuta, na mifumo ya mafunzo. Kwa kuelewa jinsi vipengele hivi vinavyofanya kazi pamoja, watengenezaji wanaweza kurekebisha kwa ufanisi modeli msingi kwa kazi maalum na hali za uzalishaji.

## Modeli kama Huduma

Boreshaji modeli kwa kutumia uboreshaji uliowekwa, bila hitaji la kuunda na kusimamia kompyuta.

![MaaS Fine Tuning](../../../../translated_images/sw/MaaSfinetune.3eee4630607aff0d.webp)

Uboreshaji usio na seva sasa unapatikana kwa familia za modeli za Phi-3, Phi-3.5, na Phi-4, kuwezesha watengenezaji kubadilisha modeli kwa haraka na kwa urahisi kwa hali za wingu na edge bila kuhitaji kupanga kompyuta.

## Modeli kama Jukwaa

Watumiaji husimamia kompyuta zao ili kuboresha modeli zao.

![Maap Fine Tuning](../../../../translated_images/sw/MaaPFinetune.fd3829c1122f5d1c.webp)

[Muhtasari wa Uboreshaji](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Ulinganisho wa Mbinu za Uboreshaji wa Hali ya Juu

|Hali|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Kurekebisha LLMs zilizo tayari kufundishwa kwa kazi au maeneo maalum|Ndiyo|Ndiyo|Ndiyo|Ndiyo|Ndiyo|Ndiyo|
|Uboreshaji kwa kazi za NLP kama uainishaji wa maandishi, utambuzi wa entiti zilizopewa jina, na tafsiri ya mashine|Ndiyo|Ndiyo|Ndiyo|Ndiyo|Ndiyo|Ndiyo|
|Uboreshaji kwa kazi za QA|Ndiyo|Ndiyo|Ndiyo|Ndiyo|Ndiyo|Ndiyo|
|Uboreshaji kwa kuzalisha majibu yanayofanana na ya binadamu katika chatbots|Ndiyo|Ndiyo|Ndiyo|Ndiyo|Ndiyo|Ndiyo|
|Uboreshaji kwa kuzalisha muziki, sanaa, au aina nyingine za ubunifu|Ndiyo|Ndiyo|Ndiyo|Ndiyo|Ndiyo|Ndiyo|
|Kupunguza gharama za kompyuta na kifedha|Ndiyo|Ndiyo|Ndiyo|Ndiyo|Ndiyo|Ndiyo|
|Kupunguza matumizi ya kumbukumbu|Ndiyo|Ndiyo|Ndiyo|Ndiyo|Ndiyo|Ndiyo|
|Kutumia vigezo vichache kwa uboreshaji wenye ufanisi|Ndiyo|Ndiyo|Ndiyo|Hapana|Hapana|Ndiyo|
|Aina ya matumizi ya kumbukumbu yenye ufanisi wa data parallelism inayotoa ufikivu wa kumbukumbu ya jumla ya GPU zote zilizopo|Hapana|Hapana|Hapana|Ndiyo|Ndiyo|Hapana|

> [!NOTE]
> LoRA, QLoRA, PEFT, na DoRA ni mbinu za uboreshaji wa hali ya juu zinazotumia vigezo kwa ufanisi, wakati DeepSpeed na ZeRO zinazingatia mafunzo yaliyoenea na uboreshaji wa kumbukumbu.

## Mifano ya Utendaji wa Uboreshaji wa Hali ya Juu

![Finetuning Performance](../../../../translated_images/sw/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Maelezo ya kisheria**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuwa sahihi, tafadhali fahamu kuwa tafsiri za moja kwa moja zinaweza kuwa na makosa au upotoshaji. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo halali. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inashauriwa. Hatuwezi kuwajibika kwa kutoelewana au upotoshaji unaotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->