<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-05T09:20:41+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "sw"
}
-->
# **Kupima Familia ya Phi**

Kupima mfano kunahusu mchakato wa kupanga vigezo (kama uzito na thamani za uanzishaji) katika mfano wa mtandao wa neva kutoka kwa kiwango kikubwa cha thamani (kwa kawaida kiwango cha thamani kinachoendelea) hadi kiwango kidogo cha thamani kilicho na kikomo. Teknolojia hii inaweza kupunguza ukubwa na ugumu wa kihesabu wa mfano na kuboresha ufanisi wa uendeshaji wa mfano katika mazingira yenye rasilimali chache kama vile vifaa vya mkononi au mifumo iliyojengwa ndani. Kupima mfano hufanikisha ukandishaji kwa kupunguza usahihi wa vigezo, lakini pia huleta upotevu fulani wa usahihi. Kwa hiyo, katika mchakato wa kupima, ni muhimu kusawazisha ukubwa wa mfano, ugumu wa kihesabu, na usahihi. Mbinu za kawaida za kupima ni pamoja na kupima kwa nukta imara, kupima kwa nukta inayoelea, n.k. Unaweza kuchagua mkakati unaofaa wa kupima kulingana na hali na mahitaji maalum.

Tunatarajia kuweka mfano wa GenAI kwenye vifaa vya ukingo na kuruhusu vifaa zaidi kuingia katika matukio ya GenAI, kama vile vifaa vya mkononi, AI PC/Copilot+PC, na vifaa vya kawaida vya IoT. Kupitia mfano wa kupima, tunaweza kuuweka kwenye vifaa tofauti vya ukingo kulingana na vifaa tofauti. Tukiunganisha na mfumo wa kuharakisha mfano na mfano wa kupima unaotolewa na wazalishaji wa vifaa, tunaweza kujenga matukio bora ya programu za SLM.

Katika hali ya kupima, tunayo usahihi tofauti (INT4, INT8, FP16, FP32). Ifuatayo ni maelezo ya usahihi wa kawaida wa kupima

### **INT4**

Kupima kwa INT4 ni mbinu kali ya kupima inayopima uzito na thamani za uanzishaji za mfano kuwa nambari kamili za bits 4. Kupima kwa INT4 kwa kawaida husababisha upotevu mkubwa wa usahihi kutokana na eneo dogo la uwakilishi na usahihi mdogo. Hata hivyo, ikilinganishwa na kupima kwa INT8, kupima kwa INT4 kunaweza kupunguza zaidi mahitaji ya uhifadhi na ugumu wa kihesabu wa mfano. Inapaswa kuzingatiwa kuwa kupima kwa INT4 ni nadra katika matumizi halisi, kwa sababu usahihi mdogo sana unaweza kusababisha kupungua kwa utendaji wa mfano. Zaidi ya hayo, si vifaa vyote vinaunga mkono operesheni za INT4, hivyo ulinganifu wa vifaa unapaswa kuzingatiwa wakati wa kuchagua mbinu ya kupima.

### **INT8**

Kupima kwa INT8 ni mchakato wa kubadilisha uzito na uanzishaji wa mfano kutoka nambari za nukta inayoelea hadi nambari kamili za bits 8. Ingawa eneo la nambari linalowakilishwa na nambari kamili za INT8 ni dogo na lisilo sahihi sana, linaweza kupunguza kwa kiasi kikubwa mahitaji ya uhifadhi na hesabu. Katika kupima kwa INT8, uzito na thamani za uanzishaji za mfano hupitia mchakato wa kupima, ikiwa ni pamoja na upimaji na kizuizi, ili kuhifadhi taarifa za asili za nambari zinazoelea kadri inavyowezekana. Wakati wa makadirio, thamani hizi zilizopimwa zitatolewa upya kama nambari za nukta inayoelea kwa ajili ya hesabu, kisha kupimwa tena kuwa INT8 kwa hatua inayofuata. Njia hii inaweza kutoa usahihi wa kutosha katika matumizi mengi huku ikidumisha ufanisi mkubwa wa kihesabu.

### **FP16**

Muundo wa FP16, yaani nambari za nukta inayoelea za bits 16 (float16), hupunguza matumizi ya kumbukumbu kwa nusu ikilinganishwa na nambari za nukta inayoelea za bits 32 (float32), jambo lenye faida kubwa katika matumizi makubwa ya ujifunzaji wa kina. Muundo wa FP16 unaruhusu kupakia mifano mikubwa zaidi au kushughulikia data nyingi zaidi ndani ya vizingiti vya kumbukumbu za GPU sawa. Kadiri vifaa vya kisasa vya GPU vinavyoendelea kuunga mkono operesheni za FP16, kutumia muundo wa FP16 pia kunaweza kuleta maboresho katika kasi ya hesabu. Hata hivyo, muundo wa FP16 pia una hasara zake za asili, yaani usahihi mdogo, ambao unaweza kusababisha ukosefu wa utulivu wa nambari au upotevu wa usahihi katika baadhi ya kesi.

### **FP32**

Muundo wa FP32 hutoa usahihi mkubwa zaidi na unaweza kuwakilisha kwa usahihi aina nyingi za thamani. Katika hali ambapo operesheni za kihesabu ngumu zinafanywa au matokeo yenye usahihi wa juu yanahitajika, muundo wa FP32 hupendekezwa. Hata hivyo, usahihi mkubwa pia unamaanisha matumizi makubwa ya kumbukumbu na muda mrefu wa hesabu. Kwa mifano mikubwa ya ujifunzaji wa kina, hasa wakati kuna vigezo vingi vya mfano na kiasi kikubwa cha data, muundo wa FP32 unaweza kusababisha ukosefu wa kumbukumbu ya GPU au kupungua kwa kasi ya makadirio.

Kwa vifaa vya mkononi au vifaa vya IoT, tunaweza kubadilisha mifano ya Phi-3.x kuwa INT4, wakati AI PC / Copilot PC inaweza kutumia usahihi wa juu zaidi kama INT8, FP16, FP32.

Kwa sasa, wazalishaji tofauti wa vifaa wana mifumo tofauti ya kuunga mkono mifano ya kizazi, kama vile OpenVINO ya Intel, QNN ya Qualcomm, MLX ya Apple, na CUDA ya Nvidia, n.k., ikijumuishwa na kupima mfano kukamilisha uanzishaji wa ndani.

Kielektroniki, tunaunga mkono miundo tofauti baada ya kupima, kama vile miundo ya PyTorch / TensorFlow, GGUF, na ONNX. Nimefanya kulinganisha kwa muundo na matukio ya matumizi kati ya GGUF na ONNX. Hapa ninapendekeza muundo wa kupima wa ONNX, unaounga mkono vizuri kutoka mfumo wa mfano hadi vifaa. Katika sura hii, tutazingatia ONNX Runtime kwa GenAI, OpenVINO, na Apple MLX kufanya kupima mfano (ikiwa una njia bora zaidi, unaweza pia kutoa kwa kutuma PR)

**Sura hii inajumuisha**

1. [Kupima Phi-3.5 / 4 kwa kutumia llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kupima Phi-3.5 / 4 kwa kutumia nyongeza za AI za kizazi kwa onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kupima Phi-3.5 / 4 kwa kutumia Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kupima Phi-3.5 / 4 kwa kutumia Mfumo wa Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kikwazo cha Dhima**:
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri kwa AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za moja kwa moja zinaweza kuwa na makosa au kasoro. Hati asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu na ya mtu inaanzishwa. Hatuhusiki kwa mawazo potofu au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->