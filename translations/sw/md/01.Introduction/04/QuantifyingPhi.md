<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-05-09T13:34:31+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "sw"
}
-->
# **Kupima Familia ya Phi**

Kupima mfano kunamaanisha mchakato wa kubadilisha vigezo (kama vile uzito na thamani za uanzishaji) katika mfano wa mtandao wa neva kutoka kwa safu kubwa ya thamani (kawaida ni safu endelevu) hadi safu ndogo ya thamani zilizopimwa. Teknolojia hii inaweza kupunguza ukubwa na ugumu wa mahesabu ya mfano na kuboresha ufanisi wa kufanya kazi wa mfano katika mazingira yenye rasilimali finyu kama vile vifaa vya simu au mifumo iliyojumuishwa. Kupima mfano hufanikisha usimbuaji kwa kupunguza usahihi wa vigezo, lakini pia huleta upotevu fulani wa usahihi. Kwa hiyo, katika mchakato wa kupima ni muhimu kusawazisha ukubwa wa mfano, ugumu wa mahesabu, na usahihi. Mbinu za kawaida za kupima ni pamoja na kupima kwa pointi thabiti, kupima kwa pointi zinazotembea, n.k. Unaweza kuchagua mkakati unaofaa wa kupima kulingana na hali maalum na mahitaji.

Tunatarajia kuweka mfano wa GenAI kwenye vifaa vya edge na kuruhusu vifaa zaidi kuingia katika mazingira ya GenAI, kama vile vifaa vya simu, AI PC/Copilot+PC, na vifaa vya jadi vya IoT. Kupitia mfano uliopimwa, tunaweza kuuweka kwenye vifaa tofauti vya edge kulingana na aina ya kifaa. Tukichanganya na mfumo wa kuharakisha mfano na mfano wa kupima unaotolewa na watengenezaji wa vifaa, tunaweza kujenga mazingira bora ya matumizi ya SLM.

Katika mazingira ya kupima, tunayo usahihi tofauti (INT4, INT8, FP16, FP32). Hapa chini kuna maelezo ya usahihi wa kawaida wa kupima.

### **INT4**

Kupima kwa INT4 ni mbinu kali ya kupima ambayo hupima uzito na thamani za uanzishaji za mfano kuwa nambari za nane za 4-bit. Kupima kwa INT4 kawaida husababisha upotevu mkubwa wa usahihi kutokana na safu ndogo ya uwakilishi na usahihi mdogo. Hata hivyo, ikilinganishwa na kupima kwa INT8, INT4 hupunguza mahitaji ya kuhifadhi na ugumu wa mahesabu ya mfano zaidi. Inapaswa kuzingatiwa kuwa kupima kwa INT4 ni nadra katika matumizi halisi, kwa sababu usahihi mdogo sana unaweza kusababisha kushuka kwa utendaji wa mfano. Zaidi ya hayo, si vifaa vyote vinaunga mkono operesheni za INT4, hivyo ulinganifu wa vifaa unapaswa kuzingatiwa wakati wa kuchagua mbinu ya kupima.

### **INT8**

Kupima kwa INT8 ni mchakato wa kubadilisha uzito na thamani za uanzishaji za mfano kutoka nambari za pointi zinazotembea kuwa nambari za 8-bit. Ingawa safu ya nambari inayowakilishwa na nambari za INT8 ni ndogo na isiyo sahihi sana, inaweza kupunguza kwa kiasi kikubwa mahitaji ya kuhifadhi na mahesabu. Katika kupima kwa INT8, uzito na thamani za uanzishaji za mfano hupitia mchakato wa kupima, ikiwa ni pamoja na kupanua na kuondoa mzigo, ili kuhifadhi taarifa za asili za pointi zinazotembea kadri inavyowezekana. Wakati wa kutabiri, thamani hizi zilizopimwa zitageuzwa tena kuwa nambari za pointi zinazotembea kwa ajili ya mahesabu, kisha zirejeshwe kwa INT8 kwa hatua inayofuata. Mbinu hii inaweza kutoa usahihi wa kutosha katika matumizi mengi huku ikidumisha ufanisi wa juu wa mahesabu.

### **FP16**

Muundo wa FP16, yaani nambari za pointi zinazotembea za 16-bit (float16), hupunguza matumizi ya kumbukumbu kwa nusu ikilinganishwa na nambari za 32-bit (float32), jambo lenye faida kubwa katika matumizi makubwa ya kujifunza kwa kina. Muundo wa FP16 unaruhusu kupakia mifano mikubwa zaidi au kushughulikia data zaidi ndani ya mipaka ile ile ya kumbukumbu ya GPU. Kadiri vifaa vya kisasa vya GPU vinavyoendelea kuunga mkono operesheni za FP16, matumizi ya muundo wa FP16 pia yanaweza kuleta uboreshaji wa kasi ya mahesabu. Hata hivyo, muundo wa FP16 pia una hasara zake za asili, yaani usahihi mdogo, ambao unaweza kusababisha kutokuwa thabiti kwa nambari au upotevu wa usahihi katika baadhi ya matukio.

### **FP32**

Muundo wa FP32 hutoa usahihi wa juu na unaweza kuwakilisha safu kubwa ya thamani kwa usahihi. Katika mazingira ambapo operesheni ngumu za kihisabati zinafanyika au matokeo yenye usahihi wa hali ya juu yanahitajika, muundo wa FP32 unapendekezwa. Hata hivyo, usahihi wa juu pia unamaanisha matumizi makubwa ya kumbukumbu na muda mrefu wa mahesabu. Kwa mifano mikubwa ya kujifunza kwa kina, hasa pale ambapo kuna vigezo vingi vya mfano na kiasi kikubwa cha data, muundo wa FP32 unaweza kusababisha ukosefu wa kumbukumbu ya GPU au kupungua kwa kasi ya kutabiri.

Katika vifaa vya simu au vifaa vya IoT, tunaweza kubadilisha mifano ya Phi-3.x kuwa INT4, wakati AI PC / Copilot PC inaweza kutumia usahihi wa juu kama INT8, FP16, FP32.

Kwa sasa, watengenezaji tofauti wa vifaa wana mifumo tofauti ya kuunga mkono mifano ya kizazi, kama OpenVINO ya Intel, QNN ya Qualcomm, MLX ya Apple, na CUDA ya Nvidia, nk, ikichanganywa na kupima mfano kwa ajili ya utekelezaji wa ndani.

Kuhusu teknolojia, tuna msaada wa miundo tofauti baada ya kupima, kama muundo wa PyTorch / Tensorflow, GGUF, na ONNX. Nimefanya kulinganisha kwa miundo na mazingira ya matumizi kati ya GGUF na ONNX. Hapa napendekeza muundo wa kupima wa ONNX, unaounga mkono vizuri kutoka mfumo wa mfano hadi vifaa. Katika sura hii, tutazingatia ONNX Runtime kwa GenAI, OpenVINO, na Apple MLX kwa ajili ya kupima mfano (ikiwa una njia bora zaidi, unaweza pia kutupatia kwa kuwasilisha PR)

**Sura hii inajumuisha**

1. [Kupima Phi-3.5 / 4 kwa kutumia llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kupima Phi-3.5 / 4 kwa kutumia nyongeza za AI ya kizazi kwa onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kupima Phi-3.5 / 4 kwa kutumia Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kupima Phi-3.5 / 4 kwa kutumia Mfumo wa Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

**Kufafanua**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuwa sahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatuna wajibu kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.