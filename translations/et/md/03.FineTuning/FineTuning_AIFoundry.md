# Phi-3 peenhäälestamine Microsoft Foundryga

Uurime, kuidas peenhäälestada Microsofti Phi-3 Mini keelemudelit, kasutades Microsoft Foundryt. Peenhäälestamine võimaldab kohandada Phi-3 Mini spetsiifiliste ülesannete jaoks, muutes selle veelgi võimsamaks ja kontekstiteadlikumaks.

## Arvestatavad kaalutlused

- **Võimekus:** Millised mudelid on peenhäälestatavad? Mida baasmudeliga saab peenhäälestamisega teha?
- **Kulu:** Milline on peenhäälestamise hinnamudel?
- **Kohandatavus:** Kui palju saan baasmudelit muuta – ja millisel viisil?
- **Mugavus:** Kuidas peenhäälestamine tegelikult toimub – kas pean kirjutama kohandatud koodi? Kas pean ise arvutusressursse juurde tooma?
- **Ohutus:** Peenhäälestatud mudelid võivad omada ohutusriske – kas on olemas kaitsemehhanismid tahtmatu kahju vältimiseks?

![AIFoundry Models](../../../../translated_images/et/AIFoundryModels.0e1b16f7d0b09b73.webp)

## Valmistumine peenhäälestamiseks

### Eeldused

> [!NOTE]
> Phi-3 perekonna mudelite puhul on maksa vastavalt kasutusele põhinev peenhäälestamistarjandus saadaval ainult **East US 2** piirkonnas loodud keskustes.

- Azure tellimus. Kui sul pole Azure tellimust, loo [tasuline Azure konto](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go), et alustada.

- [AI Foundry projekt](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Azure rollipõhine juurdepääsu kontroll (Azure RBAC) võimaldab anda õigusi Microsoft Foundrys operatsioonide tegemiseks. Selle artikli sammude tegemiseks peab sinu kasutajakontole olema antud __Azure AI Developer roll__ ressurmirühmas.

### Tellimuse pakkuja registreerimine

Kontrolli, et tellimus on registreeritud `Microsoft.Network` ressursipakkujana.

1. Logi sisse [Azure portaali](https://portal.azure.com).
1. Vali vasakult menüüst **Subscriptions**.
1. Vali oma kasutatav tellimus.
1. Vali vasakult menüüst **AI project settings** > **Resource providers**.
1. Veendu, et nimekirjas oleks **Microsoft.Network**. Kui mitte, lisa see.

### Andmete ettevalmistus

Valmista ette treening- ja valideerimisandmed, et mudelit peenhäälestada. Sinu treening- ja valideerimisandmestik sisaldab sisendi- ja väljundnäiteid, kuidas soovid, et mudel toimiks.

Veendu, et kõik treeningnäited järgiksid eeldatavat formaati inferentsiks. Mudelite tõhusaks peenhäälestamiseks kindlusta tasakaalustatud ja mitmekesine andmestik.

See hõlmab andmete tasakaalu hoidmist, erinevate stsenaariumite kaasamist ning treeningandmete perioodilist korrigeerimist reaalse maailma ootustega sobitamiseks, mis viib täpsemate ja tasakaalustatud mudelivastusteni.

Erinevad mudelitüübid vajavad erinevat treeningandmete formaati.

### Vestluse lõpetamine

Kasutatav treening- ja valideerimisandmestik **peab** olema vormindatud JSON Lines (JSONL) dokumendina. `Phi-3-mini-128k-instruct` mudeli peenhäälestamise andmestik peab olema vormindatud vestlusformaadis, mida kasutab Chat completions API.

### Näidiskomplekti formaat

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Toetatav faili tüüp on JSON Lines. Failid üles laaditakse vaikeandmehoidlasse ja tehakse projektis kättesaadavaks.

## Phi-3 peenhäälestamine Microsoft Foundryga

Microsoft Foundry võimaldab sul kohandada suuri keelemudeleid isiklike andmestike põhjal, kasutades protsessi, mida nimetatakse peenhäälestamiseks. Peenhäälestamine pakub olulist väärtust, võimaldades kohandamist ja optimeerimist spetsiifiliste ülesannete ja rakenduste jaoks. See parandab jõudlust, kulutõhusust, vähendab latentsust ja võimaldab kohandatud väljundit.

![Finetune AI Foundry](../../../../translated_images/et/AIFoundryfinetune.193aaddce48d553c.webp)

### Uue projekti loomine

1. Logi sisse [Microsoft Foundry](https://ai.azure.com).

1. Vali **+New project**, et luua Microsoft Foundrys uus projekt.

    ![FineTuneSelect](../../../../translated_images/et/select-new-project.cd31c0404088d7a3.webp)

1. Tee järgmised toimingud:

    - Projekti **Hub name**. See peab olema unikaalne väärtus.
    - Vali kasutatav **Hub** (loo vajadusel uus).

    ![FineTuneSelect](../../../../translated_images/et/create-project.ca3b71298b90e420.webp)

1. Uue hubi loomiseks tee järgmised toimingud:

    - Sisesta **Hub name**. See peab olema unikaalne väärtus.
    - Vali oma Azure **Subscription**.
    - Vali kasutatav **Resource group** (loo vajadusel uus).
    - Vali soovitud **Location**.
    - Vali kasutatav **Connect Azure AI Services** (loo vajadusel uus).
    - Vali **Connect Azure AI Search** juures valik **Skip connecting**.

    ![FineTuneSelect](../../../../translated_images/et/create-hub.49e53d235e80779e.webp)

1. Vali **Next**.
1. Vali **Create a project**.

### Andmete ettevalmistus

Enne peenhäälestamist koguge või looge ülesandega seotud andmestik, näiteks vestlusjuhised, küsimus-vastus paarid või muu asjakohane tekstimaterjal. Puhasta ja eeltööta andmed, eemaldades müra, käsitledes puuduvate väärtusi ja tehes teksti tokeniseerimist.

### Phi-3 mudelite peenhäälestamine Microsoft Foundrys

> [!NOTE]
> Phi-3 mudelite peenhäälestamine on hetkel toetatud ainult East US 2 piirkonnas asuvates projektides.

1. Vali vasakult menüüst **Model catalog**.

1. Otsi **otsinguribal** *phi-3* ja vali soovitud phi-3 mudel.

    ![FineTuneSelect](../../../../translated_images/et/select-model.60ef2d4a6a3cec57.webp)

1. Vali **Fine-tune**.

    ![FineTuneSelect](../../../../translated_images/et/select-finetune.a976213b543dd9d8.webp)

1. Sisesta **Fine-tuned model name**.

    ![FineTuneSelect](../../../../translated_images/et/finetune1.c2b39463f0d34148.webp)

1. Vali **Next**.

1. Tee järgmised valikud:

    - Vali **task type**: **Chat completion**.
    - Vali kasutatav **Training data**. Võid selle üles laadida Microsoft Foundry andmete kaudu või oma lokaalsest keskkonnast.

    ![FineTuneSelect](../../../../translated_images/et/finetune2.43cb099b1a94442d.webp)

1. Vali **Next**.

1. Laadi üles kasutatav **Validation data** või vali **Automatic split of training data**.

    ![FineTuneSelect](../../../../translated_images/et/finetune3.fd96121b67dcdd92.webp)

1. Vali **Next**.

1. Määra järgmised parameetrid:

    - Vali sobiv **Batch size multiplier**.
    - Vali **Learning rate**.
    - Vali soovitud **Epochs**.

    ![FineTuneSelect](../../../../translated_images/et/finetune4.e18b80ffccb5834a.webp)

1. Vali **Submit**, et alustada peenhäälestamist.

    ![FineTuneSelect](../../../../translated_images/et/select-submit.0a3802d581bac271.webp)


1. Kui mudel on peenhäälestatud, kuvatakse olek **Completed**, nagu alloleval pildil. Nüüd saad mudelit juurutada ja kasutada seda oma rakenduses, mänguväljakul või prompt flow's. Lisateabe saamiseks vaata [Kuidas juurutada Phi-3 väikeste keelemudelite perekonda Microsoft Foundryga](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/et/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Täpsema info saamiseks Phi-3 peenhäälestuse kohta külasta [Fine-tune Phi-3 models in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Peenhäälestatud mudelite puhastamine

Saad peenhäälestatud mudeli kustutada peenhäälestatud mudelite nimekirjast Microsoft Foundrys või mudeli detailide lehelt. Vali peenhäälestatud mudel kustutamiseks Fine-tuning lehel ja seejärel vali Kustuta nupp.

> [!NOTE]
> Kohandatud mudelit ei saa kustutada, kui sellel on olemasolev juurutus. Pead esmalt kustutama mudeli juurutuse, enne kui saad kustutada kohandatud mudeli.

## Kulu ja piirangud

### Phi-3 mudelite peenhäälestamisel teenusena kehtivad kulu- ja piiranguküsimused

Phi-3 mudelid, mis on peenhäälestatud teenusena, on Microsofti poolt pakutavad ja integreeritud Microsoft Foundryga kasutamiseks. Saad hinnainfot mudelite [juurutamisel](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) või peenhäälestamisel, kasutades juurutamise võluri "Pricing and terms" vahelehte.

## Sisufiltreerimine

Pay-as-you-go teenusena juurutatud mudelid on kaitstud Azure AI Content Safety kontrolliga. Reaalajas lõpp-punktides kasutuselevõtul võid selle võimaluse välja lülitada. Azure AI sisuturbe lubamise korral läbivad nii sisendkäsud kui ka mudeli väljundid hulga klassifitseerimismudeleid, mis püüavad tuvastada ja takistada kahjuliku sisu edastamist. Sisufiltreerimissüsteem tuvastab ja rakendab meetmeid teatud kategooriates potentsiaalselt kahjuliku sisu puhul nii sisendpäringutes kui väljundites. Loe rohkem [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering) kohta.

**Peenhäälestamise konfiguratsioon**

Hüperparameetrid: Määratle hüperparameetrid, näiteks õppimise kiirus, partiide suurus ja treeningepochide arv.

**Kahjufunktsioon**

Vali oma ülesande jaoks sobiv kahjufunktsioon (nt rist-entropia).

**Optimeerija**

Vali optimeerija (nt Adam) gradientide värskendamiseks treeningu ajal.

**Peenhäälestamise protsess**

- Laadi eelträenitud mudel: Laadi Phi-3 Mini kontrollpunkt.
- Lisa kohandatud kihid: Lisa ülesandespetsiifilised kihid (näiteks klassifikatsioonipea vestlusjuhiste jaoks).

**Treeni mudelit**
Peenhäälesta mudelit oma ettevalmistatud andmestiku põhjal. Jälgi treeningu edenemist ja reguleeri vajadusel hüperparameetreid.

**Hindamine ja valideerimine**

Valideerimiskomplekt: Jaota andmed treening- ja valideerimiskomplektideks.

**Soorituse hindamine**

Kasuta mõõdikuid nagu täpsus, F1-skoor või segadusmõõde mudeli soorituse hindamiseks.

## Peenhäälestatud mudeli salvestamine

**Kontrollpunkt**
Salvesta peenhäälestatud mudeli kontrollpunkt tulevikus kasutamiseks.

## Juurutamine

- Juuruta veebiteenusena: Juuruta peenhäälestatud mudel Microsoft Foundrys veebiteenusena.
- Testi lõpp-punkti: Saada testpäringud juurutatud lõpp-punktile, et kontrollida funktsionaalsust.

## Iteratsioon ja parandamine

Itereeri: Kui sooritus ei ole rahuldav, tee iteratsioone, muutes hüperparameetreid, lisades rohkem andmeid või peenhäälestades täiendavate epochide jooksul.

## Jälgimine ja täiendamine

Jälgi mudeli käitumist pidevalt ja täienda vastavalt vajadusele.

## Kohandamine ja laiendamine

Kohandatud ülesanded: Phi-3 Mini saab peenhäälestada mitmesugusteks ülesanneteks peale vestlusjuhiste. Uuri teisi kasutusjuhtumeid!
Katseta erinevaid arhitektuure, kihikombinatsioone ja tehnikaid parema soorituse saavutamiseks.

> [!NOTE]
> Peenhäälestamine on iteratiivne protsess. Katseta, õpi ja kohanda mudelit, et saavutada parim tulemus oma konkreetses ülesandes!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:  
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüame täpsust, palun olge teadlikud, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument oma emakeeles peaks olema autoriteetne allikas. Kriitilise info puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta ühegi arusaamatuse või valesti mõistmise eest, mis võib sellest tõlkest tingida.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->