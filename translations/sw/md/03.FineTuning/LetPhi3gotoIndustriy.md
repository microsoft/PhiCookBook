<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "743d7e9cb9c4e8ea642d77bee657a7fa",
  "translation_date": "2025-07-17T09:59:50+00:00",
  "source_file": "md/03.FineTuning/LetPhi3gotoIndustriy.md",
  "language_code": "sw"
}
-->
# **Acha Phi-3 awe mtaalamu wa sekta**

Ili kuweka mfano wa Phi-3 katika sekta fulani, unahitaji kuongeza data ya biashara ya sekta hiyo kwenye mfano wa Phi-3. Tuna chaguzi mbili tofauti, ya kwanza ni RAG (Retrieval Augmented Generation) na ya pili ni Fine Tuning.

## **RAG dhidi ya Fine-Tuning**

### **Retrieval Augmented Generation**

RAG ni mchakato wa kupata data + uzalishaji wa maandishi. Data iliyopangwa na isiyopangwa ya shirika huhifadhiwa katika hifadhidata ya vector. Wakati wa kutafuta maudhui yanayohusiana, muhtasari na maudhui yanayohusiana hupatikana kuunda muktadha, na uwezo wa kukamilisha maandishi wa LLM/SLM unachanganywa kuzalisha maudhui.

### **Fine-tuning**

Fine-tuning inategemea kuboresha mfano fulani. Hainahitaji kuanza na algorithm ya mfano, lakini data inapaswa kuendelea kukusanywa. Ikiwa unataka istilahi sahihi zaidi na uelezaji wa lugha katika matumizi ya sekta, fine-tuning ni chaguo bora kwako. Lakini ikiwa data yako hubadilika mara kwa mara, fine-tuning inaweza kuwa ngumu.

### **Jinsi ya kuchagua**

1. Ikiwa jibu letu linahitaji kuingiza data ya nje, RAG ni chaguo bora

2. Ikiwa unahitaji kutoa maarifa thabiti na sahihi ya sekta, fine-tuning itakuwa chaguo zuri. RAG inalenga kupata maudhui yanayohusiana lakini huenda isifikie kila mara undani maalum wa taaluma.

3. Fine-tuning inahitaji seti ya data yenye ubora wa juu, na ikiwa ni data ndogo tu, haitakuwa na tofauti kubwa. RAG ni rahisi kubadilika zaidi

4. Fine-tuning ni kama sanduku la giza, ni metaphysics, na ni vigumu kuelewa mfumo wa ndani. Lakini RAG inaweza kurahisisha kupata chanzo cha data, hivyo kurekebisha kwa ufanisi makosa ya maudhui au mawazo potofu na kutoa uwazi bora.

### **Mazingira**

1. Sekta za wima zinahitaji msamiati maalum wa kitaalamu na maelezo, ***Fine-tuning*** itakuwa chaguo bora

2. Mfumo wa QA, unaohusisha muundo wa pointi tofauti za maarifa, ***RAG*** itakuwa chaguo bora

3. Mchanganyiko wa mtiririko wa biashara wa kiotomatiki ***RAG + Fine-tuning*** ni chaguo bora

## **Jinsi ya kutumia RAG**

![rag](../../../../translated_images/sw/rag.2014adc59e6f6007.png)

Hifadhidata ya vector ni mkusanyiko wa data iliyohifadhiwa kwa njia ya kihisabati. Hifadhidata za vector hurahisisha mifano ya kujifunza mashine kukumbuka maingizo ya awali, na hivyo kuwezesha matumizi ya kujifunza mashine kusaidia matumizi kama utafutaji, mapendekezo, na uzalishaji wa maandishi. Data inaweza kutambuliwa kwa msingi wa vipimo vya ufananishi badala ya mechi kamili, kuruhusu mifano ya kompyuta kuelewa muktadha wa data.

Hifadhidata ya vector ni ufunguo wa kutekeleza RAG. Tunaweza kubadilisha data kuwa hifadhi ya vector kupitia mifano ya vector kama text-embedding-3, jina-ai-embedding, n.k.

Jifunze zaidi kuhusu kuunda programu ya RAG [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo) 

## **Jinsi ya kutumia Fine-tuning**

Algorithmi zinazotumika mara kwa mara katika Fine-tuning ni Lora na QLora. Jinsi ya kuchagua?
- [Jifunze Zaidi kwa kutumia daftari hili la mfano](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Mfano wa Python FineTuning Sample](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora na QLora**

![lora](../../../../translated_images/sw/qlora.e6446c988ee04ca0.png)

LoRA (Low-Rank Adaptation) na QLoRA (Quantized Low-Rank Adaptation) ni mbinu zinazotumika kurekebisha mifano mikubwa ya lugha (LLMs) kwa kutumia Parameter Efficient Fine Tuning (PEFT). Mbinu za PEFT zimetengenezwa kufundisha mifano kwa ufanisi zaidi kuliko njia za kawaida.  
LoRA ni mbinu ya kujitegemea ya fine-tuning inayopunguza matumizi ya kumbukumbu kwa kutumia takriban ya kiwango cha chini kwenye matrix ya masasisho ya uzito. Inatoa muda mfupi wa mafunzo na hifadhi utendaji karibu na mbinu za kawaida za fine-tuning.

QLoRA ni toleo lililopanuliwa la LoRA linalojumuisha mbinu za kuhesabu kwa kiasi (quantization) kupunguza matumizi ya kumbukumbu zaidi. QLoRA huhesabu kwa kiwango cha 4-bit usahihi wa vigezo vya uzito katika LLM iliyofunzwa awali, ambayo ni ya ufanisi zaidi kwa kumbukumbu kuliko LoRA. Hata hivyo, mafunzo ya QLoRA ni takriban asilimia 30 polepole zaidi kuliko mafunzo ya LoRA kutokana na hatua za ziada za kuhesabu na kuondoa hesabu.

QLoRA hutumia LoRA kama nyongeza kurekebisha makosa yanayotokea wakati wa kuhesabu kwa kiasi. QLoRA inaruhusu fine-tuning ya mifano mikubwa yenye mabilioni ya vigezo kwenye GPUs ndogo, zinazopatikana kwa urahisi. Kwa mfano, QLoRA inaweza kufanyia fine-tuning mfano wa 70B parameters unaohitaji GPUs 36 kwa kutumia tu 2...

**Kiarifu cha Msamaha**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatuna dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.