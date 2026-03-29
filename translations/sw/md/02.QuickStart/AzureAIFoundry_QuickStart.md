# **Kutumia Phi-3 katika Microsoft Foundry**

Pamoja na maendeleo ya AI Inayozalisha, tunatarajia kutumia jukwaa linalounganisha kusimamia LLM na SLM tofauti, muunganisho wa data za kampuni, urekebishaji/mfumo wa RAG, na tathmini ya biashara mbalimbali za kampuni baada ya kuunganisha LLM na SLM, nk, ili programu za AI inayozalisha ziweze kutekelezwa kwa njia bora zaidi. [Microsoft Foundry](https://ai.azure.com) ni jukwaa la programu la AI inayozalisha kwa kiwango cha kampuni.

![aistudo](../../../../translated_images/sw/aifoundry_home.f28a8127c96c7d93.webp)

Kwa Microsoft Foundry, unaweza kutathmini majibu ya modeli kubwa za lugha (LLM) na kuendesha vipengele vya programu ya prompt kwa kutumia mtiririko wa prompt kwa utendaji bora zaidi. Jukwaa hili linawezesha upanuzi kwa kubadilisha uthibitisho wa dhana kuwa uzalishaji kamili kwa urahisi. Ufuatiliaji endelevu na uboreshaji husaidia mafanikio ya muda mrefu.

Tunaweza kupeleka modeli ya Phi-3 haraka kwenye Microsoft Foundry kupitia hatua rahisi, kisha tumia Microsoft Foundry kukamilisha Playground/Chat, Urekebishaji, tathmini na kazi nyingine zinazohusiana na Phi-3.

## **1. Maandalizi**

Ikiwa tayari una [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) imewekwa kwenye mashine yako, kutumia templeti hii ni rahisi kama kuendesha amri hii kwenye saraka mpya.

## Uundaji wa Kawaida

Kuunda mradi na kitovu cha Microsoft Foundry ni njia nzuri ya kupanga na kusimamia kazi yako ya AI. Hapa kuna mwongozo wa hatua kwa hatua kukusaidia kuanza:

### Kuunda Mradi katika Microsoft Foundry

1. **Nenda Microsoft Foundry**: Ingia kwenye lango la Microsoft Foundry.
2. **Unda Mradi**:
   - Ukipo ndani ya mradi, chagua "Microsoft Foundry" upande wa juu kushoto wa ukurasa kwenda ukurasa wa Mwanzo.
   - Chagua "+ Create project".
   - Ingiza jina la mradi.
   - Ikiwa una kitovu, kitakuwa kimechaguliwa kwa chaguo-msingi. Ikiwa una ufikiaji wa vituo zaidi ya kimoja, unaweza kuchagua tofauti kutoka kwenye menyu kunjuzi. Ikiwa unataka kuunda kitovu kipya, chagua "Create new hub" na toa jina.
   - Chagua "Create".

### Kuunda Kituo katika Microsoft Foundry

1. **Nenda Microsoft Foundry**: Ingia na akaunti yako ya Azure.
2. **Unda Kituo**:
   - Chagua kituo cha Usimamizi kutoka kwenye menyu ya kushoto.
   - Chagua "All resources", kisha mshale wa chini karibu na "+ New project" na chagua "+ New hub".
   - Katika mazungumzo ya "Create a new hub", ingiza jina la kitovu chako (mfano, contoso-hub) na badilisha sehemu nyingine kama unavyotaka.
   - Chagua "Next", hakiki taarifa, kisha chagua "Create".

Kwa maelezo zaidi, unaweza rejelea [nyaraka rasmi za Microsoft](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Baada ya kuunda kwa mafanikio, unaweza kufikia studio ulioiunda kupitia [ai.azure.com](https://ai.azure.com/)

Kunaweza kuwa na miradi mingi kwenye AI Foundry moja. Unda mradi katika AI Foundry kwa maandalizi.

Tengeneza Microsoft Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. Kuweka Phi modeli katika Microsoft Foundry**

Bonyeza chaguo la Explore la mradi kuingia katika Katalogi ya Modeli na chagua Phi-3

Chagua Phi-3-mini-4k-instruct

Bonyeza 'Deploy' kuweka modeli ya Phi-3-mini-4k-instruct

> [!NOTE]
>
> Unaweza kuchagua nguvu ya kompyuta wakati wa kuweka

## **3. Mchezo wa Chat Phi katika Microsoft Foundry**

Nenda kwenye ukurasa wa kuweka, chagua Playground, na ongea na Phi-3 wa Microsoft Foundry

## **4. Kuweka Modeli kutoka Microsoft Foundry**

Ili kuweka modeli kutoka kwenye Katalogi ya Modeli ya Azure, unaweza kufuata hatua hizi:

- Ingia Microsoft Foundry.
- Chagua modeli unayotaka kuweka kutoka katalogi ya modeli za Microsoft Foundry.
- Kwenye ukurasa wa Maelezo ya modeli, chagua Deploy kisha chagua Serverless API na Azure AI Content Safety.
- Chagua mradi unaotaka kuweka modeli zako ndani yake. Ili kutumia toleo la Serverless API, kazi yako lazima iwe katika mkoa wa East US 2 au Sweden Central. Unaweza kubinafsisha Jina la Kuweka.
- Kwenye mchawi wa kuweka, chagua Bei na masharti kujifunza kuhusu bei na masharti ya matumizi.
- Chagua Deploy. Subiri mpaka kuweka kumalizike na utapelekwa kwenye ukurasa wa Deployments.
- Chagua Fungua katika playground kuanza kuingiliana na modeli.
- Unaweza kurudi kwenye ukurasa wa Deployments, chagua kuweka, na kumbuka URL ya Target ya kiunganishi na Funguo ya Siri, ambazo unaweza kutumia kuita kuweka na kuzalisha majibu.
- Daima unaweza kupata maelezo ya kiunganishi, URL, na funguo za kufikia kwa kwenda kwenye kichupo cha Build na kuchagua Deployments kutoka sehemu ya Vipengele.

> [!NOTE]
> Tafadhali kumbuka kuwa akaunti yako lazima iwe na ruhusa za Azure AI Developer kwenye Kikundi cha Rasilimali ili kufanya hatua hizi.

## **5. Kutumia Phi API katika Microsoft Foundry**

Unaweza kufikia https://{Your project name}.region.inference.ml.azure.com/swagger.json kupitia Postman GET na kuziunganisha na Funguo kujifunza kuhusu kiolesura kinachotolewa

Unaweza kupata vigezo vya ombi kwa urahisi sana, pamoja na vigezo vya majibu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kielezeaji**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Wakati tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za otomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya kiasili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya mtaalamu wa binadamu inapendekezwa. Hatujui majukumu yoyote kwa maelewano au tafsiri potofu zitokanazo na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->