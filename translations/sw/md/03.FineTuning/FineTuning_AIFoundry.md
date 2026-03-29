# Kurekebisha Phi-3 kwa Microsoft Foundry

 Hebu chunguza jinsi ya kurekebisha modeli ya lugha ya Phi-3 Mini ya Microsoft kwa kutumia Microsoft Foundry. Kurekebisha kunakuwezesha kuendana na Phi-3 Mini kwa kazi maalum, na kuiifanya iwe hata yenye nguvu zaidi na inayofahamu muktadha.

## Vizingiti

- **Uwezo:** Ni modeli gani zinaweza kurekebishwa? Modeli ya msingi inaweza kurekebishwa kufanya nini?
- **Gharama:** Mfano wa bei ya kurekebisha ni upi?
**Uwezo wa Kubadilika:** Ninaweza kubadilisha kiasi gani modeli ya msingi – na kwa njia gani?
- **Urahisi:** Kurekebisha hufanyika vipi kweli – je, nahitaji kuandika msimbo maalum? Je, nahitaji kuleta kompyuta yangu?
- **Usalama:** Modeli zilizorekebishwa zinajulikana kuwa na hatari za usalama – kuna mipaka yoyote ya ulinzi dhidi ya madhara yasiyotakiwa?

![AIFoundry Models](../../../../translated_images/sw/AIFoundryModels.0e1b16f7d0b09b73.webp)

## Maandalizi ya kurekebisha

### Vigezo vinavyohitajika

> [!NOTE]
> Kwa modeli za familia ya Phi-3, ofa ya kurekebisha kwa malipo kama unavyotumia inapatikana tu kwa vituo vilivyoundwa katika mikoa ya **East US 2**.

- Akaunti ya Azure. Ikiwa huna akaunti ya Azure, tengeneza [akaunti ya Azure yenye malipo](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) kuanza.

- Mradi wa [AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Udhibiti wa upatikanaji kwa asilimia za kutumia Azure (Azure RBAC) unatumika kutoa ruhusa kwa operesheni katika Microsoft Foundry. Ili kutekeleza hatua katika makala hii, akaunti yako ya mtumiaji lazima ipewe __Jukumu la Azure AI Developer__ kwenye kundi la rasilimali.

### Usajili wa mtoa huduma wa usajili

Thibitisha kuwa usajili umejisajili kwa mtoa huduma wa rasilimali `Microsoft.Network`.

1. Ingia kwenye [Azure portal](https://portal.azure.com).
1. Chagua **Subscriptions** kutoka kwenye menyu ya upande wa kushoto.
1. Chagua usajili unaotaka kutumia.
1. Chagua **AI project settings** > **Resource providers** kutoka kwenye menyu ya upande wa kushoto.
1. Thibitisha kuwa **Microsoft.Network** ipo kwenye orodha ya watoa huduma za rasilimali. Vinginevyo ongeza.

### Maandalizi ya data

Tayarisha data zako za mafunzo na uthibitishaji kurekebisha modeli yako. Seti za data zako za mafunzo na uthibitishaji zinajumuisha mifano ya ingizo na matokeo kwa jinsi unavyotaka modeli ifanye kazi.

Hakikisha mifano yako yote ya mafunzo inafuata muundo unaotarajiwa kwa utabiri. Ili kurekebisha modeli kwa ufanisi, hakikisha seti ya data ni yenye usawa na anuwai.

Hii inahusisha kudumisha usawa wa data, kujumuisha hali mbalimbali, na kurekebisha data ya mafunzo mara kwa mara ili kuendana na matarajio ya dunia halisi, hatimaye kuleta majibu sahihi na yenye usawa zaidi kutoka kwa modeli.

Aina tofauti za modeli zinahitaji muundo tofauti wa data ya mafunzo.

### Kukamilisha mazungumzo

Data ya mafunzo na uthibitishaji unayotumia **inabidi** kuwa imepangwa kama hati ya JSON Lines (JSONL). Kwa `Phi-3-mini-128k-instruct` seti ya data ya kurekebisha inapaswa kuwa na muundo wa mazungumzo unaotumiwa na API ya Kukamilisha mazungumzo.

### Mfano wa muundo wa faili

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Aina ya faili inayoungwa mkono ni JSON Lines. Faili huwasilishwa kwenye hifadhi ya chaguo-msingi na kupatikana katika mradi wako.

## Kurekebisha Phi-3 kwa Microsoft Foundry

Microsoft Foundry inakuwezesha kuunda modeli kubwa za lugha kulingana na seti zako za data kwa kutumia mchakato unaojulikana kama kurekebisha. Kurekebisha kunatoa thamani kubwa kwa kuwezesha ubinafsishaji na uboreshaji kwa kazi na programu maalum. Hii huleta utendaji bora, ufanisi wa gharama, kupunguza kuchelewa, na matokeo yaliyo ya mkono.

![Finetune AI Foundry](../../../../translated_images/sw/AIFoundryfinetune.193aaddce48d553c.webp)

### Tengeneza Mradi Mpya

1. Ingia kwenye [Microsoft Foundry](https://ai.azure.com).

1. Chagua **+New project** kuunda mradi mpya katika Microsoft Foundry.

    ![FineTuneSelect](../../../../translated_images/sw/select-new-project.cd31c0404088d7a3.webp)

1. Fanya kazi zifuatazo:

    - Jina la **Hub** la mradi. Lazima liwe thamani tofauti kabisa.
    - Chagua **Hub** ya kutumia (unda mpya ikiwa inahitajika).

    ![FineTuneSelect](../../../../translated_images/sw/create-project.ca3b71298b90e420.webp)

1. Fanya kazi zifuatazo kuunda hub mpya:

    - Weka **Jina la Hub**. Lazima liwe thamani tofauti kabisa.
    - Chagua **Usajili wa Azure**.
    - Chagua **Kundi la Rasilimali** la kutumia (unda mpya ikiwa inahitajika).
    - Chagua **Eneo** unalotaka kutumia.
    - Chagua **Unganisha Huduma za Azure AI** za kutumia (unda mpya ikiwa inahitajika).
    - Chagua **Unganisha Azure AI Search** kisha **Ruka kuunganisha**.

    ![FineTuneSelect](../../../../translated_images/sw/create-hub.49e53d235e80779e.webp)

1. Chagua **Next**.
1. Chagua **Create a project**.

### Maandalizi ya Data

Kabla ya kurekebisha, kusanya au unda seti ya data inayohusiana na kazi yako, kama vile maelekezo ya mazungumzo, jozi za maswali-jawabu, au data nyingine muhimu ya maandishi. Safisha na andaa data hii kwa kutoa kelele, kushughulikia thamani zilizokosekana, na kugawanya maandishi.

### Rekebisha modeli za Phi-3 katika Microsoft Foundry

> [!NOTE]
> Kurekebisha modeli za Phi-3 kwa sasa kunasaidiwa tu katika miradi iliyoko East US 2.

1. Chagua **Model catalog** kutoka kwenye kichupo cha upande wa kushoto.

1. Andika *phi-3* kwenye **kisanduku cha utafutaji** na chagua modeli ya phi-3 unayotaka kutumia.

    ![FineTuneSelect](../../../../translated_images/sw/select-model.60ef2d4a6a3cec57.webp)

1. Chagua **Fine-tune**.

    ![FineTuneSelect](../../../../translated_images/sw/select-finetune.a976213b543dd9d8.webp)

1. Weka jina la **Modeli iliyorekebishwa**.

    ![FineTuneSelect](../../../../translated_images/sw/finetune1.c2b39463f0d34148.webp)

1. Chagua **Next**.

1. Fanya kazi zifuatazo:

    - Chagua aina ya kazi **task type** kuwa **Chat completion**.
    - Chagua **Data ya Mafunzo** unayotaka kutumia. Unaweza kuipakia kupitia data ya Microsoft Foundry au kutoka mazingira yako ya ndani.

    ![FineTuneSelect](../../../../translated_images/sw/finetune2.43cb099b1a94442d.webp)

1. Chagua **Next**.

1. Pakia **Data ya Uthibitishaji** unayotaka kutumia. au unaweza kuchagua **mgawanyo wa kiotomatiki wa data ya mafunzo**.

    ![FineTuneSelect](../../../../translated_images/sw/finetune3.fd96121b67dcdd92.webp)

1. Chagua **Next**.

1. Fanya kazi zifuatazo:

    - Chagua **Kiwango cha ukubwa wa kundi** unayotaka kutumia.
    - Chagua **Kiwango cha kujifunza** unayotaka kutumia.
    - Chagua **Idadi ya vipindi (Epochs)** unayotaka kutumia.

    ![FineTuneSelect](../../../../translated_images/sw/finetune4.e18b80ffccb5834a.webp)

1. Chagua **Submit** kuanza mchakato wa kurekebisha.

    ![FineTuneSelect](../../../../translated_images/sw/select-submit.0a3802d581bac271.webp)


1. Mara moja modeli yako itakaporekebishwa, hali yake itaonyeshwa kama **Imefanikiwa**, kama inavyoonyeshwa kwenye picha chini. Sasa unaweza kusambaza modeli na kuitumia kwenye programu yako mwenyewe, katika uwanja wa michezo, au katika mtiririko wa maelekezo. Kwa habari zaidi, ona [Jinsi ya kusambaza modeli za familia ya Phi-3 ndogo kwa Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/sw/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Kwa taarifa za kina zaidi kuhusu kurekebisha Phi-3, tafadhali tembelea [Rekebisha modeli za Phi-3 katika Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Kusafisha modeli zako zilizorekebishwa

Unaweza kufuta modeli yaliyorekebishwa kutoka kwenye orodha ya modeli zilizorekebishwa katika [Microsoft Foundry](https://ai.azure.com) au kutoka kwenye ukurasa wa maelezo ya modeli. Chagua modeli iliyorekebishwa kuifuta kutoka kwenye ukurasa wa Fine-tuning, kisha chagua kitufe cha Futa ili kufuta modeli hiyo.

> [!NOTE]
> Huwezi kufuta modeli maalum ikiwa ina uenezi uliopo. Lazima uanze kwa kufuta uenezaji wa modeli yako kabla hujafuta modeli maalum.

## Gharama na vikwazo

### Vizingiti vya gharama na vikwazo kwa modeli za Phi-3 zilizorekebishwa kama huduma

Modeli za Phi zilizorekebishwa kama huduma hutolewa na Microsoft na kuunganishwa na Microsoft Foundry kwa matumizi. Unaweza kupata bei wakati wa [kusambaza](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) au kurekebisha modeli chini ya kichupo cha Bei na masharti kwenye mtaalamu wa usambazaji.

## Kuchuja maudhui

Modeli zinazotumika kama huduma kwa malipo kulingana na matumizi zinalindwa na Azure AI Content Safety. Unapotumika kwa sehemu za wakati halisi, unaweza kujiuzulu uwezo huu. Ukiwa na Azure AI content safety imewezeshwa, prompt na matokeo hupitia seti ya modeli za uainishaji zinazolenga kugundua na kuzuia utoaji wa maudhui hatari. Mfumo wa kuchuja maudhui huchunguza na kuchukua hatua kwa makundi maalum ya maudhui yanayoweza kusababisha madhara katika prompt za ingizo na majibu ya matokeo. Jifunze zaidi kuhusu [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Mpangilio wa Kurekebisha**

Hyperparameters: Bainisha hyperparameters kama kiwango cha kujifunza, ukubwa wa kundi, na idadi ya vipindi vya mafunzo.

**Kazi ya Hasara**

Chagua kazi ya hasara inayofaa kwa kazi yako (mfano, cross-entropy).

**Mrekebishaji**

Chagua mrekebishaji (mfano, Adam) kwa masasisho ya mwelekeo wa gradient wakati wa mafunzo.

**Mchakato wa Kurekebisha**

- Pakia Modeli Iliyojiandaa: Pakia rekodi ya Phi-3 Mini.
- Ongeza Tabaka Maalum: Ongeza tabaka maalum kwa kazi (mfano, kichwa cha uainishaji kwa maelekezo ya mazungumzo).

**Fanya Mafunzo ya Modeli**
Rekebisha modeli kwa kutumia seti ya data uliyoandaa. Fuatilia maendeleo ya mafunzo na badilisha hyperparameters kama inavyotakiwa.

**Tathmini na Uthibitishaji**

Seti ya Uthibitishaji: Gawanya data yako katika seti za mafunzo na uthibitishaji.

**Tathmini Utendaji**

Tumia vipimo kama usahihi, alama ya F1, au ugumu kuelewa kutathmini utendaji wa modeli.

## Hifadhi Modeli Iliyorekebishwa

**Rekodi**
Hifadhi rekodi ya modeli iliyorekebishwa kwa matumizi ya baadaye.

## Usambazaji

- Sambaza kama Huduma ya Wavuti: Sambaza modeli yako iliyorekebishwa kama huduma ya wavuti katika Microsoft Foundry.
- Jaribu Sehemu ya Muktadha: Tuma majaribio kwenye sehemu iliyosambazwa kuthibitisha utendaji wake.

## Rudia na Boresha

Rudia: Ikiwa utendaji haujitoshi, rudia kwa kubadilisha hyperparameters, kuongeza data zaidi, au kurekebisha kwa vipindi zaidi.

## Fuatilia na Boresha

Endelea kufuatilia tabia ya modeli na boresha inapohitajika.

## Binafsisha na Panua

Kazi Maalum: Phi-3 Mini inaweza kurekebishwa kwa kazi mbalimbali zaidi ya maelekezo ya mazungumzo. Chunguza matumizi mengine!
Jaribu: Jaribu usanifu tofauti, mchanganyiko wa tabaka, na mbinu kuboresha utendaji.

> [!NOTE]
> Kurekebisha ni mchakato wa kurudia. Jaribu, jifunze, na buni modeli yako kufikia matokeo bora kwa kazi yako maalum!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kiasi cha Majaribio**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Wakati tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri zinazofanywa kwa mashine zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa habari muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatuhusiki na kutoelewana au tafsiri mbaya zitokanazo na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->