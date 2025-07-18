<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-07-17T03:43:07+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "sw"
}
-->
# **Jenga Chat yako ya Visual Studio Code GitHub Copilot na Familia ya Microsoft Phi-3**

Je, umewahi kutumia wakala wa eneo la kazi katika GitHub Copilot Chat? Unataka kujenga wakala wa msimbo wa timu yako mwenyewe? Maabara hii ya vitendo inalenga kuunganisha mfano wa chanzo wazi kujenga wakala wa biashara wa kiwango cha shirika.

## **Msingi**

### **Kwa nini uchague Microsoft Phi-3**

Phi-3 ni mfululizo wa familia, ikiwa ni pamoja na phi-3-mini, phi-3-small, na phi-3-medium kulingana na vigezo tofauti vya mafunzo kwa ajili ya uzalishaji wa maandishi, kukamilisha mazungumzo, na uzalishaji wa msimbo. Pia kuna phi-3-vision inayotegemea Vision. Inafaa kwa mashirika au timu tofauti kuunda suluhisho za AI za kizazi zisizo mtandaoni.

Inapendekezwa kusoma kiungo hiki [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Kiendelezi cha GitHub Copilot Chat kinakupa kiolesura cha mazungumzo kinachokuwezesha kuwasiliana na GitHub Copilot na kupokea majibu kwa maswali yanayohusiana na uandishi wa msimbo moja kwa moja ndani ya VS Code, bila ya kuhitaji kutafuta nyaraka au kuvinjari majukwaa ya mtandaoni.

Copilot Chat inaweza kutumia muonekano wa msimbo, uingizaji wa mistari, na vipengele vingine vya muundo kuongeza uwazi kwa jibu lililotolewa. Kulingana na aina ya swali kutoka kwa mtumiaji, matokeo yanaweza kuwa na viungo vya muktadha ambavyo Copilot ilitumia kutengeneza jibu, kama vile faili za msimbo wa chanzo au nyaraka, au vifungo vya kufikia vipengele vya VS Code.

- Copilot Chat inaingizwa katika mtiririko wako wa maendeleo na inakupa msaada unapoihitaji:

- Anza mazungumzo ya moja kwa moja kutoka mhariri au terminal kwa msaada wakati unapoandika msimbo

- Tumia mtazamo wa Chat kuwa na msaidizi wa AI kando kusaidia wakati wowote

- Anzisha Quick Chat kuuliza swali la haraka na kurudi kwenye kazi yako

Unaweza kutumia GitHub Copilot Chat katika hali mbalimbali, kama vile:

- Kujibu maswali ya uandishi wa msimbo kuhusu jinsi ya kutatua tatizo kwa njia bora

- Kuelezea msimbo wa mtu mwingine na kupendekeza maboresho

- Kupendekeza marekebisho ya msimbo

- Kutengeneza kesi za majaribio ya vitengo

- Kutengeneza nyaraka za msimbo

Inapendekezwa kusoma kiungo hiki [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

### **Microsoft GitHub Copilot Chat @workspace**

Kurejelea **@workspace** katika Copilot Chat kunakuwezesha kuuliza maswali kuhusu msimbo wako mzima. Kulingana na swali, Copilot hutafuta kwa akili faili na alama zinazohusiana, ambazo hutaja katika jibu lake kama viungo na mifano ya msimbo.

Ili kujibu swali lako, **@workspace** hutafuta kupitia vyanzo sawa ambavyo mtaalamu wa maendeleo atatumia anapovinjari msimbo katika VS Code:

- Faili zote katika eneo la kazi, isipokuwa faili zinazopitwa na .gitignore

- Muundo wa saraka na majina ya folda na faili zilizomo ndani yake

- Kielezo cha utafutaji wa msimbo cha GitHub, ikiwa eneo la kazi ni hifadhidata ya GitHub na kimeorodheshwa na utafutaji wa msimbo

- Alama na ufafanuzi katika eneo la kazi

- Maandishi yaliyoteuliwa sasa au yaliyomo kwenye mhariri unaoonekana

Kumbuka: .gitignore haizingatiwi ikiwa una faili wazi au umechagua maandishi ndani ya faili iliyopitwa.

Inapendekezwa kusoma kiungo hiki [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **Jifunze Zaidi Kuhusu Maabara Hii**

GitHub Copilot imeboresha sana ufanisi wa programu katika mashirika, na kila shirika linatarajia kubinafsisha vipengele husika vya GitHub Copilot. Mashirika mengi yamebinafsisha Viendelezi vinavyofanana na GitHub Copilot kulingana na hali zao za biashara na mifano ya chanzo wazi. Kwa mashirika, Viendelezi vilivyobinafsishwa ni rahisi kudhibiti, lakini hii pia huathiri uzoefu wa mtumiaji. Baada ya yote, GitHub Copilot ina vipengele vyenye nguvu zaidi katika kushughulikia hali za jumla na taaluma. Ikiwa uzoefu unaweza kudumishwa kuwa thabiti, itakuwa bora kubinafsisha Kiendelezi cha shirika chako. GitHub Copilot Chat hutoa API zinazohusiana kwa mashirika kupanua uzoefu wa Chat. Kudumisha uzoefu thabiti na kuwa na vipengele vilivyobinafsishwa ni uzoefu bora kwa mtumiaji.

Maabara hii inatumia hasa mfano wa Phi-3 uliounganishwa na NPU ya eneo la karibu na Azure hybrid kujenga Wakala maalum katika GitHub Copilot Chat ***@PHI3*** kusaidia waendelezaji wa mashirika kukamilisha uzalishaji wa msimbo***(@PHI3 /gen)*** na kuzalisha msimbo kulingana na picha ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/cover.1017ebc9a7c46d095fe0b942687287803c03933d2d1d439d14e10fa1442a864d.sw.png)

### ***Kumbuka:***

Maabara hii kwa sasa inatekelezwa katika AIPC ya Intel CPU na Apple Silicon. Tutaendelea kusasisha toleo la Qualcomm la NPU.

## **Maabara**

| Jina | Maelezo | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Usanidi(✅) | Sanidi na sakinisha mazingira na zana zinazohusiana | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Endesha mtiririko wa Prompt na Phi-3-mini (✅) | Imeunganishwa na AIPC / Apple Silicon, kutumia NPU ya eneo la karibu kuunda uzalishaji wa msimbo kupitia Phi-3-mini | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Sambaza Phi-3-vision kwenye Azure Machine Learning Service(✅) | Tengeneza msimbo kwa kusambaza Katalogi ya Mfano wa Azure Machine Learning Service - picha ya Phi-3-vision | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Unda wakala wa @phi-3 katika GitHub Copilot Chat(✅)  | Unda wakala maalum wa Phi-3 katika GitHub Copilot Chat kukamilisha uzalishaji wa msimbo, msimbo wa uzalishaji wa grafu, RAG, n.k. | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Msimbo wa Mfano (✅)  | Pakua msimbo wa mfano | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |

## **Rasilimali**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Jifunze zaidi kuhusu GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Jifunze zaidi kuhusu GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Jifunze zaidi kuhusu API ya GitHub Copilot Chat [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Jifunze zaidi kuhusu Azure AI Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Jifunze zaidi kuhusu Katalogi ya Mfano wa Azure AI Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**Kiarifu cha Msamaha**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatuna dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.