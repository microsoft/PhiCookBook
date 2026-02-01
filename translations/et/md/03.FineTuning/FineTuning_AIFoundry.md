# Phi-3 Mini mudeli peenhäälestamine Azure AI Foundry abil

Uurime, kuidas peenhäälestada Microsofti Phi-3 Mini keelemudelit Azure AI Foundry abil. Peenhäälestamine võimaldab kohandada Phi-3 Mini konkreetsete ülesannete jaoks, muutes selle veelgi võimsamaks ja kontekstitundlikumaks.

## Olulised kaalutlused

- **Võimekus:** Milliseid mudeleid saab peenhäälestada? Milleks saab algmudelit peenhäälestada?
- **Maksumus:** Milline on peenhäälestamise hinnamudel?
- **Kohandatavus:** Kui palju saab algmudelit muuta – ja millisel viisil?
- **Mugavus:** Kuidas peenhäälestamine tegelikult toimub – kas pean kirjutama kohandatud koodi? Kas pean ise arvutusressursid hankima?
- **Turvalisus:** Peenhäälestatud mudelitel on teadaolevalt turvariske – kas on olemas kaitsemeetmeid soovimatu kahju vältimiseks?

![AIFoundry Models](../../../../imgs/03/AIFoundry/AIFoundryModels.png)

## Ettevalmistused peenhäälestamiseks

### Eeltingimused

> [!NOTE]
> Phi-3 mudelite puhul on tasulise peenhäälestamise pakkumine saadaval ainult **East US 2** piirkonnas loodud keskustes.

- Azure'i tellimus. Kui sul pole Azure'i tellimust, loo [tasuline Azure'i konto](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go), et alustada.

- [AI Foundry projekt](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Azure'i rollipõhised juurdepääsukontrollid (Azure RBAC) võimaldavad anda juurdepääsu Azure AI Foundry toimingutele. Selle artikli samme täitmiseks peab sinu kasutajakontole olema määratud __Azure AI Developer roll__ ressursigrupis.

### Tellimuse pakkuja registreerimine

Kontrolli, kas tellimus on registreeritud `Microsoft.Network` ressursipakkuja juures.

1. Logi sisse [Azure'i portaalis](https://portal.azure.com).
1. Vali vasakult menüüst **Subscriptions**.
1. Vali tellimus, mida soovid kasutada.
1. Vali vasakult menüüst **AI project settings** > **Resource providers**.
1. Kinnita, et **Microsoft.Network** on ressursipakkujate loendis. Kui ei ole, lisa see.

### Andmete ettevalmistamine

Valmista ette oma treening- ja valideerimisandmed mudeli peenhäälestamiseks. Treening- ja valideerimisandmed koosnevad sisendi ja väljundi näidetest, mis näitavad, kuidas soovid, et mudel toimiks.

Veendu, et kõik treeningnäited järgiksid oodatud vormingut järelduste tegemiseks. Mudelite tõhusaks peenhäälestamiseks tagage tasakaalustatud ja mitmekesine andmestik.

See hõlmab andmete tasakaalu säilitamist, erinevate stsenaariumide kaasamist ja treeningandmete perioodilist täiendamist, et need vastaksid reaalse maailma ootustele, mis viib täpsemate ja tasakaalustatumate mudelivastusteni.

Erinevat tüüpi mudelid nõuavad erinevat treeningandmete vormingut.

### Vestluse lõpetamine

Treening- ja valideerimisandmed **peavad** olema vormindatud JSON Lines (JSONL) dokumendina. `Phi-3-mini-128k-instruct` mudeli peenhäälestamise andmestik peab olema vormindatud vestlusvormingus, mida kasutab Chat completions API.

### Näidisfaili vorming

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Toetatud failitüüp on JSON Lines. Failid laaditakse üles vaikimisi andmesalvestusse ja tehakse projektis kättesaadavaks.

## Phi-3 peenhäälestamine Azure AI Foundry abil

Azure AI Foundry võimaldab kohandada suuri keelemudeleid isiklike andmestike järgi, kasutades protsessi, mida nimetatakse peenhäälestamiseks. Peenhäälestamine pakub märkimisväärset väärtust, võimaldades kohandamist ja optimeerimist konkreetsete ülesannete ja rakenduste jaoks. See toob kaasa parema jõudluse, kulutõhususe, väiksema latentsuse ja kohandatud väljundid.

![Finetune AI Foundry](../../../../imgs/03/AIFoundry/AIFoundryfinetune.png)

### Uue projekti loomine

1. Logi sisse [Azure AI Foundry](https://ai.azure.com).

1. Vali **+New project**, et luua uus projekt Azure AI Foundry's.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/select-new-project.png)

1. Täida järgmised ülesanded:

    - Projekti **Hub name**. See peab olema unikaalne väärtus.
    - Vali **Hub**, mida kasutada (loo uus, kui vaja).

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/create-project.png)

1. Täida järgmised ülesanded uue keskuse loomiseks:

    - Sisesta **Hub name**. See peab olema unikaalne väärtus.
    - Vali oma Azure'i **Subscription**.
    - Vali **Resource group**, mida kasutada (loo uus, kui vaja).
    - Vali **Location**, mida soovid kasutada.
    - Vali **Connect Azure AI Services**, mida kasutada (loo uus, kui vaja).
    - Vali **Connect Azure AI Search**, et **Skip connecting**.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/create-hub.png)

1. Vali **Next**.
1. Vali **Create a project**.

### Andmete ettevalmistamine

Enne peenhäälestamist kogu või loo ülesandega seotud andmestik, näiteks vestlusjuhised, küsimuste ja vastuste paarid või muu asjakohane tekst. Puhasta ja eeltöötlusta andmed, eemaldades müra, käsitledes puuduvad väärtused ja tehes tekstist tokeniseerimise.

### Phi-3 mudelite peenhäälestamine Azure AI Foundry abil

> [!NOTE]
> Phi-3 mudelite peenhäälestamine on praegu toetatud projektides, mis asuvad East US 2 piirkonnas.

1. Vali vasakult menüüst **Model catalog**.

1. Sisesta otsinguribale *phi-3* ja vali phi-3 mudel, mida soovid kasutada.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/select-model.png)

1. Vali **Fine-tune**.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/select-finetune.png)

1. Sisesta **Fine-tuned model name**.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/finetune1.png)

1. Vali **Next**.

1. Täida järgmised ülesanded:

    - Vali **task type** väärtuseks **Chat completion**.
    - Vali **Training data**, mida soovid kasutada. Sa saad selle üles laadida Azure AI Foundry kaudu või oma kohalikust keskkonnast.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/finetune2.png)

1. Vali **Next**.

1. Laadi üles **Validation data**, mida soovid kasutada, või vali **Automatic split of training data**.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/finetune3.png)

1. Vali **Next**.

1. Täida järgmised ülesanded:

    - Vali **Batch size multiplier**, mida soovid kasutada.
    - Vali **Learning rate**, mida soovid kasutada.
    - Vali **Epochs**, mida soovid kasutada.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/finetune4.png)

1. Vali **Submit**, et alustada peenhäälestamise protsessi.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/select-submit.png)

1. Kui mudel on peenhäälestatud, kuvatakse selle olek **Completed**, nagu näidatud alloleval pildil. Nüüd saad mudeli juurutada ja kasutada seda oma rakenduses, mänguväljakul või prompt flow's. Lisateabe saamiseks vaata [Kuidas juurutada Phi-3 väikese keelemudelite perekonda Azure AI Foundry abil](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/completed.png)

> [!NOTE]
> Täpsema teabe saamiseks Phi-3 peenhäälestamise kohta külastage [Phi-3 mudelite peenhäälestamine Azure AI Foundry abil](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Peenhäälestatud mudelite kustutamine

Sa saad kustutada peenhäälestatud mudeli peenhäälestamise mudelite loendist [Azure AI Foundry](https://ai.azure.com) või mudeli detailide lehelt. Vali peenhäälestatud mudel, mida soovid kustutada, ja seejärel vali kustutamise nupp, et mudel kustutada.

> [!NOTE]
> Kohandatud mudelit ei saa kustutada, kui sellel on olemasolev juurutus. Enne kohandatud mudeli kustutamist pead esmalt kustutama mudeli juurutuse.

## Maksumus ja kvoodid

### Phi-3 mudelite teenusena peenhäälestamise maksumus ja kvoodid

Phi mudelid, mida pakutakse teenusena, on Microsofti poolt integreeritud Azure AI Foundry'sse kasutamiseks. Hinnakujundust saab vaadata [juurutamise](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) või peenhäälestamise ajal juurutamise viisardi hinnakujunduse ja tingimuste vahekaardil.

## Sisufiltreerimine

Teenusena juurutatud mudelid tasulise kasutuse korral on kaitstud Azure AI Content Safety abil. Reaalajas lõpp-punktides juurutamisel saab sellest funktsioonist loobuda. Azure AI sisuturvalisuse lubamisel läbivad nii sisend kui ka väljund klassifikatsioonimudelite ansambli, mille eesmärk on tuvastada ja takistada kahjuliku sisu väljundit. Sisufiltreerimissüsteem tuvastab ja tegutseb potentsiaalselt kahjuliku sisu kategooriate osas nii sisendites kui ka väljundites. Lisateavet leiate [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Peenhäälestamise konfiguratsioon**

Hüperparameetrid: Määra hüperparameetrid, nagu õppemäär, partii suurus ja treeningtsüklite arv.

**Kaotuse funktsioon**

Vali ülesande jaoks sobiv kaotuse funktsioon (nt ristentropia).

**Optimeerija**

Vali optimeerija (nt Adam) gradientide uuendamiseks treeningu ajal.

**Peenhäälestamise protsess**

- Laadi eeltreenitud mudel: Laadi Phi-3 Mini kontrollpunkt.
- Lisa kohandatud kihid: Lisa ülesandespetsiifilised kihid (nt klassifikatsioonipea vestlusjuhiste jaoks).

**Treeni mudelit**
Peenhäälesta mudel, kasutades ettevalmistatud andmestikku. Jälgi treeningu edenemist ja kohanda hüperparameetreid vastavalt vajadusele.

**Hindamine ja valideerimine**

Valideerimiskomplekt: Jaga oma andmed treening- ja valideerimiskomplektideks.

**Hinda jõudlust**

Kasuta mõõdikuid, nagu täpsus, F1-skoor või hämmeldus, et hinnata mudeli jõudlust.

## Peenhäälestatud mudeli salvestamine

**Kontrollpunkt**
Salvesta peenhäälestatud mudeli kontrollpunkt tulevaseks kasutamiseks.

## Juurutamine

- Juuruta veebiteenusena: Juuruta oma peenhäälestatud mudel veebiteenusena Azure AI Foundry's.
- Testi lõpp-punkti: Saada testpäringuid juurutatud lõpp-punkti, et kontrollida selle funktsionaalsust.

## Iteratsioon ja täiustamine

Iteratsioon: Kui jõudlus pole rahuldav, iteratsiooni tehes kohanda hüperparameetreid, lisa rohkem andmeid või peenhäälesta täiendavate tsüklite jaoks.

## Jälgi ja täiusta

Jälgi pidevalt mudeli käitumist ja täiusta vastavalt vajadusele.

## Kohanda ja laienda

Kohandatud ülesanded: Phi-3 Mini saab peenhäälestada erinevateks ülesanneteks peale vestlusjuhiste. Uuri teisi kasutusvõimalusi!
Katseta: Proovi erinevaid arhitektuure, kihtide kombinatsioone ja tehnikaid, et jõudlust parandada.

> [!NOTE]
> Peenhäälestamine on iteratiivne protsess. Katseta, õpi ja kohanda oma mudelit, et saavutada parimad tulemused konkreetse ülesande jaoks!

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.