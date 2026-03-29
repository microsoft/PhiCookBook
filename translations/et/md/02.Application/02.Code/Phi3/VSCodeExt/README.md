# **Ehita oma Visual Studio Code GitHub Copilot Chat Microsoft Phi-3 perekonnaga**

Kas oled kasutanud tööruumi agenti GitHub Copilot Chat'is? Kas soovid luua oma meeskonna koodiagentuuri? See praktiline labor üritab ühendada avatud lähtekoodiga mudeli, et luua ettevõtte tasemel koodibusinessi agent.

## **Alus**

### **Miks valida Microsoft Phi-3**

Phi-3 on perekonnavalik, mis sisaldab phi-3-mini, phi-3-small ja phi-3-medium erinevate treeningparameetritega teksti genereerimiseks, vestluste täiendamiseks ja koodi genereerimiseks. Samuti on olemas phi-3-vision, mis põhineb Vision'il. See sobib ettevõtetele või erinevatele meeskondadele offline generatiivsete tehisintellekti lahenduste loomiseks.

Soovitatav lugeda seda linki [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat laiendus annab sulle vestluskeskkonna, mis võimaldab suhelda GitHub Copilotiga ja saada programmeerimisega seotud küsimustele vastuseid otse VS Code'is, ilma et peaksid dokumentatsiooni sirvima või veebifoorumeid otsima.

Copilot Chat võib kasutada süntaksi esiletõstmist, taanet ja muid vormindamise funktsioone, et lisada genereeritud vastusele selgust. Sõltuvalt kasutaja küsimuse tüübist võib tulemus sisaldada linke kontekstile, mida Copilot vastuse genereerimisel kasutas, nagu lähtekoodifailid või dokumentatsioon, või nuppe VS Code'i funktsioonide kasutamiseks.

- Copilot Chat integreerub sinu arendaja töövoogu ja pakub abi seal, kus seda vajad:

- Alusta tekstisiseset vestlust otse redaktorist või terminalist, et saada abi programmeerimise ajal

- Kasuta Chat vaadet, et omada AI assistenti kõrval, kes aitab igal ajal

- Käivita Kiirvestlus, esita kiire küsimus ja naase oma töö juurde

Saad kasutada GitHub Copilot Chat erinevates stsenaariumites, näiteks:

- Vastamine programmeerimisküsimustele, kuidas probleemi kõige paremini lahendada

- Kellegi teise koodi selgitamine ja täiustuste soovitamine

- Koodiparanduste pakkumine

- Ühiktestide genereerimine

- Koodidokumentatsiooni loomine

Soovitatav lugeda seda linki [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Viidates **@workspace** Copilot Chat'is, saad esitada küsimusi kogu oma koodibaasi kohta. Küsimuse põhjal otsib Copilot nutikalt asjakohased failid ja sümbolid, mida ta seejärel vastuses viitab linkide ja koodi näidetena.

Sinu küsimusele vastamiseks otsib **@workspace** samu allikaid, mida arendaja kasutab koodibaasis VS Code'is navigeerides:

- Kõik tööruumi failid, välja arvatud failid, mida ignoreerib .gitignore fail

- Kataloogistruktuur koos alamkaustade ja failinimedega

- GitHubi koodotsingu indeks, kui tööruum on GitHubi hoidla ja on indekseeritud koodotsingu poolt

- Sümbolid ja definitsioonid tööruumis

- Praegune valitud tekst või nähtav tekst aktiivses redaktoris

Märkus: .gitignore jäetakse kasutusele, kui sul on avatud fail või valitud tekst ignoreeritud failis.

Soovitatav lugeda seda linki [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Lisateave selle labori kohta**

GitHub Copilot on oluliselt parandanud ettevõtete programmeerimise efektiivsust ning iga ettevõte soovib kohandada GitHub Copiloti asjakohaseid funktsioone. Paljud ettevõtted on kohandanud laiendusi, mis sarnanevad GitHub Copilotiga, tuginedes oma äristsenaariumitele ja avatud lähtekoodiga mudelitele. Ettevõtete jaoks on kohandatud laiendused kergemini hallatavad, kuid see mõjutab ka kasutajakogemust. GitHub Copilotil on tugevamad võimed üldstsenaariumite ja professionaalsuse käsitlemisel. Kui kogemused on võimalikult järjepidevad, oleks parem kohandada ettevõtte enda laiendus. GitHub Copilot Chat pakub ettevõtetele asjakohaseid API-sid, et laiendada Chat kogemust. Järjepideva kogemuse säilitamine ja kohandatud funktsioonide olemasolu annab parema kasutajakogemuse.

See labor kasutab peamiselt Phi-3 mudelit, mis on kombineeritud kohaliku NPU ja Azure hübriidiga, et luua kohandatud agent GitHub Copilot Chat'is ***@PHI3***, kes aitab ettevõtte arendajatel lõpetada koodi genereerimine***(@PHI3 /gen)*** ja piltide põhine koodigeneratsioon ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/et/cover.1017ebc9a7c46d09.webp)

### ***Märkus:***

See labor on praegu läbi viidud Intel CPU ja Apple Siliconi AIPC peal. Jätkame Qualcomm NPU versiooni uuendamist.


## **Labor**


| Nimi | Kirjeldus | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Paigaldused(✅) | Konfigureeri ja paigalda seotud keskkonnad ja paigaldustööriistad | [Mine](./HOL/AIPC/01.Installations.md) |[Mine](./HOL/Apple/01.Installations.md) |
| Lab1 - Käivita Prompt flow Phi-3-mini-ga (✅) | Koos AIPC / Apple Siliconiga kasutades kohalikku NPU-d koodigeneratsiooni loomiseks Phi-3-mini kaudu | [Mine](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Mine](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Paigalda Phi-3-vision Azure Machine Learning teenusele(✅) | Genereeri kood, paigaldades Azure Machine Learning teenuse Model Catalog - Phi-3-vision pildi | [Mine](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Mine](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Loo @phi-3 agent GitHub Copilot Chat'is(✅)  | Loo kohandatud Phi-3 agent GitHub Copilot Chat'is, et lõpetada koodi genereerimine, graafiku genereerimise kood, RAG jne | [Mine](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Mine](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Näidiskood (✅)  | Laadi alla näidiskood | [Mine](../../../../../../../code/07.Lab/01/AIPC) | [Mine](../../../../../../../code/07.Lab/01/Apple) |


## **Ressursid**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Õpi rohkem GitHub Copiloti kohta [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Õpi rohkem GitHub Copilot Chat'i kohta [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Õpi rohkem GitHub Copilot Chat API kohta [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Õpi rohkem Microsoft Foundry kohta [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Õpi rohkem Microsoft Foundry Model Catalog'i kohta [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutuse välistamine**:
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi me püüame täpsust, tuleb arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle emakeeles tuleks pidada usaldusväärseks allikaks. Kriitilise teabe puhul soovitatakse professionaalset inimtõlget. Me ei vastuta tõlgendustest ega valesti mõistmistest, mis võivad sellest tõlkest tuleneda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->