<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-07-16T21:49:21+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "sw"
}
-->
# **Kupima Familia ya Phi**

Kukokotoa mfano kunahusu mchakato wa kubadilisha vigezo (kama vile uzito na thamani za uamsho) katika mfano wa mtandao wa neva kutoka kwenye anuwai kubwa ya thamani (kawaida anuwai ya thamani zinazoendelea) kwenda kwenye anuwai ndogo ya thamani zilizopimwa. Teknolojia hii inaweza kupunguza ukubwa na ugumu wa hesabu wa mfano na kuboresha ufanisi wa kufanya kazi wa mfano katika mazingira yenye rasilimali chache kama vile vifaa vya mkononi au mifumo iliyojengwa ndani. Kukokotoa mfano hufanikisha usimbuaji kwa kupunguza usahihi wa vigezo, lakini pia huleta upotevu fulani wa usahihi. Kwa hiyo, katika mchakato wa kukokotoa, ni muhimu kusawazisha ukubwa wa mfano, ugumu wa hesabu, na usahihi. Mbinu za kawaida za kukokotoa ni pamoja na kukokotoa kwa pointi imara, kukokotoa kwa pointi inayoelea, n.k. Unaweza kuchagua mkakati unaofaa wa kukokotoa kulingana na hali na mahitaji maalum.

Tunatarajia kuweka mfano wa GenAI kwenye vifaa vya edge na kuruhusu vifaa zaidi kuingia katika mazingira ya GenAI, kama vile vifaa vya mkononi, AI PC/Copilot+PC, na vifaa vya jadi vya IoT. Kupitia mfano wa kukokotoa, tunaweza kuuweka kwenye vifaa tofauti vya edge kulingana na vifaa tofauti. Tukichanganya na mfumo wa kuharakisha mfano na mfano wa kukokotoa unaotolewa na watengenezaji wa vifaa, tunaweza kujenga mazingira bora ya matumizi ya SLM.

Katika mazingira ya kukokotoa, tunayo usahihi tofauti (INT4, INT8, FP16, FP32). Ifuatayo ni maelezo ya usahihi wa kukokotoa unaotumika mara kwa mara

### **INT4**

Kukokotoa kwa INT4 ni mbinu kali ya kukokotoa inayobadilisha uzito na thamani za uamsho za mfano kuwa nambari za bit 4. Kukokotoa kwa INT4 kawaida husababisha upotevu mkubwa wa usahihi kutokana na anuwai ndogo ya uwakilishi na usahihi mdogo. Hata hivyo, ikilinganishwa na kukokotoa kwa INT8, INT4 inaweza kupunguza zaidi mahitaji ya kuhifadhi na ugumu wa hesabu wa mfano. Inapaswa kuzingatiwa kuwa kukokotoa kwa INT4 ni nadra katika matumizi halisi, kwa sababu usahihi mdogo sana unaweza kusababisha kushuka kwa utendaji wa mfano. Zaidi ya hayo, si vifaa vyote vinavyounga mkono utendakazi wa INT4, hivyo ulinganifu wa vifaa unapaswa kuzingatiwa wakati wa kuchagua mbinu ya kukokotoa.

### **INT8**

Kukokotoa kwa INT8 ni mchakato wa kubadilisha uzito na thamani za uamsho za mfano kutoka nambari za pointi inayoelea kuwa nambari za bit 8. Ingawa anuwai ya nambari inayowakilishwa na INT8 ni ndogo na isiyo sahihi sana, inaweza kupunguza kwa kiasi kikubwa mahitaji ya kuhifadhi na hesabu. Katika kukokotoa kwa INT8, uzito na thamani za uamsho za mfano hupitia mchakato wa kukokotoa, ikiwa ni pamoja na kupanua na kuondoa mwelekeo, ili kuhifadhi taarifa za asili za pointi inayoelea kadri inavyowezekana. Wakati wa utambuzi, thamani hizi zilizokokotolewa zitabadilishwa tena kuwa nambari za pointi inayoelea kwa ajili ya hesabu, kisha zikokotoe tena kuwa INT8 kwa hatua inayofuata. Njia hii inaweza kutoa usahihi wa kutosha katika matumizi mengi huku ikidumisha ufanisi mkubwa wa hesabu.

### **FP16**

Muundo wa FP16, yaani nambari za pointi inayoelea za bit 16 (float16), hupunguza matumizi ya kumbukumbu kwa nusu ikilinganishwa na nambari za bit 32 (float32), jambo lenye faida kubwa katika matumizi makubwa ya kujifunza kwa kina. Muundo wa FP16 unaruhusu kupakia mifano mikubwa zaidi au kushughulikia data zaidi ndani ya mipaka ile ile ya kumbukumbu ya GPU. Kadiri vifaa vya kisasa vya GPU vinavyoendelea kuunga mkono utendakazi wa FP16, matumizi ya muundo wa FP16 yanaweza pia kuleta maboresho ya kasi ya kompyuta. Hata hivyo, muundo wa FP16 pia una hasara zake za asili, yaani usahihi mdogo, ambao unaweza kusababisha kutokuwa imara kwa nambari au upotevu wa usahihi katika baadhi ya matukio.

### **FP32**

Muundo wa FP32 hutoa usahihi wa juu na unaweza kuwakilisha anuwai kubwa ya thamani kwa usahihi. Katika mazingira ambapo operesheni ngumu za kihisabati zinafanyika au matokeo yenye usahihi wa juu yanahitajika, muundo wa FP32 hupendekezwa. Hata hivyo, usahihi wa juu pia unamaanisha matumizi makubwa ya kumbukumbu na muda mrefu wa hesabu. Kwa mifano mikubwa ya kujifunza kwa kina, hasa pale ambapo kuna vigezo vingi vya mfano na kiasi kikubwa cha data, muundo wa FP32 unaweza kusababisha ukosefu wa kumbukumbu ya GPU au kupungua kwa kasi ya utambuzi.

Kwenye vifaa vya mkononi au vifaa vya IoT, tunaweza kubadilisha mifano ya Phi-3.x kuwa INT4, wakati AI PC / Copilot PC inaweza kutumia usahihi wa juu zaidi kama INT8, FP16, FP32.

Kwa sasa, watengenezaji tofauti wa vifaa wana mifumo tofauti ya kuunga mkono mifano ya kizazi, kama OpenVINO ya Intel, QNN ya Qualcomm, MLX ya Apple, na CUDA ya Nvidia, n.k., ikichanganywa na kukokotoa mfano kwa ajili ya kuweka kwa ndani.

Kuhusu teknolojia, tunao msaada wa miundo tofauti baada ya kukokotoa, kama muundo wa PyTorch / Tensorflow, GGUF, na ONNX. Nimefanya kulinganisha kwa miundo na mazingira ya matumizi kati ya GGUF na ONNX. Hapa ninapendekeza muundo wa kukokotoa wa ONNX, ambao una msaada mzuri kutoka mfumo wa mfano hadi vifaa. Katika sura hii, tutazingatia ONNX Runtime kwa GenAI, OpenVINO, na Apple MLX kufanya kukokotoa mfano (kama una njia bora zaidi, unaweza pia kutupatia kwa kuwasilisha PR)

**Sura hii inajumuisha**

1. [Kukokotoa Phi-3.5 / 4 kwa kutumia llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kukokotoa Phi-3.5 / 4 kwa kutumia nyongeza za AI za kizazi kwa onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kukokotoa Phi-3.5 / 4 kwa kutumia Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kukokotoa Phi-3.5 / 4 kwa kutumia Mfumo wa Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.