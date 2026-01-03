<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a1e48b628022485aac989c9f733e792",
  "translation_date": "2025-07-17T05:26:51+00:00",
  "source_file": "md/02.QuickStart/AzureAIFoundry_QuickStart.md",
  "language_code": "sw"
}
-->
# **Kutumia Phi-3 katika Azure AI Foundry**

Kwa maendeleo ya AI ya Kizazi, tunatarajia kutumia jukwaa moja la kuendesha mifano tofauti ya LLM na SLM, ushirikiano wa data za biashara, urekebishaji/mchakato wa RAG, na tathmini ya biashara mbalimbali baada ya kuunganisha LLM na SLM, n.k., ili AI ya kizazi iweze kutekelezwa vyema katika programu za Smart. [Azure AI Foundry](https://ai.azure.com) ni jukwaa la programu za AI za kizazi kwa kiwango cha biashara.

![aistudo](../../../../translated_images/aifoundry_home.f28a8127c96c7d93.sw.png)

Kwa Azure AI Foundry, unaweza kutathmini majibu ya mifano mikubwa ya lugha (LLM) na kupanga vipengele vya programu za prompt kwa kutumia prompt flow kwa utendaji bora. Jukwaa hili linawezesha upanuzi kwa kubadilisha majaribio kuwa uzalishaji kamili kwa urahisi. Ufuatiliaji endelevu na maboresho husaidia mafanikio ya muda mrefu.

Tunaweza kupeleka haraka mfano wa Phi-3 kwenye Azure AI Foundry kwa hatua rahisi, kisha tumia Azure AI Foundry kukamilisha kazi zinazohusiana na Phi-3 kama Playground/Chat, urekebishaji, tathmini na kazi nyinginezo.

## **1. Maandalizi**

Kama tayari una [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) imewekwa kwenye kompyuta yako, kutumia templeti hii ni rahisi kama kuendesha amri hii kwenye saraka mpya.

## Uundaji wa Mikono

Kuunda mradi na kituo cha Microsoft Azure AI Foundry ni njia nzuri ya kupanga na kusimamia kazi zako za AI. Hapa kuna mwongozo wa hatua kwa hatua kuanza:

### Kuunda Mradi katika Azure AI Foundry

1. **Nenda Azure AI Foundry**: Ingia kwenye lango la Azure AI Foundry.
2. **Unda Mradi**:
   - Ikiwa uko ndani ya mradi, chagua "Azure AI Foundry" juu kushoto wa ukurasa kurudi kwenye ukurasa wa Nyumbani.
   - Chagua "+ Create project".
   - Weka jina la mradi.
   - Ikiwa una kituo, kitachaguliwa kwa chaguo-msingi. Ikiwa una ufikiaji wa vituo zaidi ya kimoja, unaweza kuchagua tofauti kutoka kwenye menyu ya kushuka. Ikiwa unataka kuunda kituo kipya, chagua "Create new hub" na toa jina.
   - Chagua "Create".

### Kuunda Kituo katika Azure AI Foundry

1. **Nenda Azure AI Foundry**: Ingia kwa akaunti yako ya Azure.
2. **Unda Kituo**:
   - Chagua Kituo cha Usimamizi kutoka kwenye menyu ya kushoto.
   - Chagua "All resources", kisha mshale wa kushuka karibu na "+ New project" na chagua "+ New hub".
   - Katika dirisha la "Create a new hub", weka jina la kituo chako (mfano, contoso-hub) na badilisha sehemu nyingine kama unavyotaka.
   - Chagua "Next", hakiki taarifa, kisha chagua "Create".

Kwa maelezo zaidi, unaweza rejelea [nyaraka rasmi za Microsoft](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Baada ya kuunda kwa mafanikio, unaweza kufikia studio uliyounda kupitia [ai.azure.com](https://ai.azure.com/)

Kunaweza kuwa na miradi mingi kwenye AI Foundry moja. Unda mradi katika AI Foundry kujiandaa.

Unda Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. Kuweka Mfano wa Phi katika Azure AI Foundry**

Bofya chaguo la Explore la mradi kuingia kwenye Katalogi ya Mfano na chagua Phi-3

Chagua Phi-3-mini-4k-instruct

Bofya 'Deploy' kuweka mfano wa Phi-3-mini-4k-instruct

> [!NOTE]
>
> Unaweza kuchagua nguvu ya kompyuta wakati wa kuweka

## **3. Playground Chat Phi katika Azure AI Foundry**

Nenda kwenye ukurasa wa kuweka, chagua Playground, na zungumza na Phi-3 wa Azure AI Foundry

## **4. Kuweka Mfano kutoka Azure AI Foundry**

Ili kuweka mfano kutoka Katalogi ya Mifano ya Azure, fuata hatua hizi:

- Ingia kwenye Azure AI Foundry.
- Chagua mfano unayotaka kuweka kutoka katalogi ya mifano ya Azure AI Foundry.
- Kwenye ukurasa wa Maelezo ya mfano, chagua Deploy kisha chagua Serverless API na Azure AI Content Safety.
- Chagua mradi ambao unataka kuweka mifano yako ndani yake. Ili kutumia huduma ya Serverless API, eneo lako la kazi lazima liwe katika East US 2 au Sweden Central. Unaweza kubadilisha jina la Deployment.
- Kwenye mtaalamu wa kuweka, chagua Bei na masharti ili kujifunza kuhusu bei na masharti ya matumizi.
- Chagua Deploy. Subiri mpaka kuweka kumalizike na utapelekwa kwenye ukurasa wa Deployments.
- Chagua Open in playground kuanza kuingiliana na mfano.
- Unaweza kurudi kwenye ukurasa wa Deployments, chagua deployment, na kumbuka URL ya Target ya endpoint na Secret Key, ambazo unaweza kutumia kuita deployment na kuzalisha majibu.
- Daima unaweza kupata maelezo ya endpoint, URL, na funguo za kufikia kwa kwenda kwenye kichupo cha Build na kuchagua Deployments kutoka sehemu ya Components.

> [!NOTE]
> Tafadhali kumbuka kuwa akaunti yako lazima iwe na ruhusa za Azure AI Developer kwenye Resource Group ili kufanya hatua hizi.

## **5. Kutumia Phi API katika Azure AI Foundry**

Unaweza kufikia https://{Your project name}.region.inference.ml.azure.com/swagger.json kupitia Postman GET na kuunganisha na Key kujifunza kuhusu interfaces zinazotolewa

Unaweza kupata vigezo vya ombi kwa urahisi sana, pamoja na vigezo vya majibu.

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.