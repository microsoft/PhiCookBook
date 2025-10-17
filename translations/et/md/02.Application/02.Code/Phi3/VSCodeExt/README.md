<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-10-11T11:55:12+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "et"
}
-->
# **Ehita oma Visual Studio Code GitHub Copilot Chat Microsoft Phi-3 perekonnaga**

Kas olete kasutanud GitHub Copilot Chati tööruumi agenti? Kas soovite luua oma meeskonna koodiagendi? See praktiline labor ühendab avatud lähtekoodiga mudeli, et luua ettevõtte tasemel koodiga seotud ärilahendusi.

## **Alus**

### **Miks valida Microsoft Phi-3**

Phi-3 on perekonnaseeria, mis sisaldab phi-3-mini, phi-3-small ja phi-3-medium mudeleid, mis põhinevad erinevatel treeningparameetritel tekstigeneratsiooni, dialoogi lõpetamise ja koodigeneratsiooni jaoks. Lisaks on olemas phi-3-vision, mis põhineb Visionil. See sobib ettevõtetele või erinevatele meeskondadele, et luua võrguühenduseta generatiivse AI lahendusi.

Soovitatav lugemiseks: [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat laiendus pakub vestlusliidest, mis võimaldab teil suhelda GitHub Copilotiga ja saada vastuseid koodiga seotud küsimustele otse VS Code'is, ilma et peaksite sirvima dokumentatsiooni või otsima vastuseid veebifoorumitest.

Copilot Chat võib kasutada süntaksi esiletõstmist, taandamist ja muid vormindamisfunktsioone, et muuta genereeritud vastused selgemaks. Sõltuvalt kasutaja küsimuse tüübist võib tulemus sisaldada linke kontekstile, mida Copilot kasutas vastuse genereerimiseks, näiteks lähtekoodifailid või dokumentatsioon, või nuppe VS Code'i funktsioonide kasutamiseks.

- Copilot Chat integreerub teie arendaja töövoogu ja pakub abi seal, kus seda vajate:

- Alustage vestlust otse redaktorist või terminalist, et saada abi koodi kirjutamise ajal

- Kasutage vestlusvaadet, et AI assistent oleks alati käepärast

- Käivitage Quick Chat, et esitada kiire küsimus ja jätkata oma tööd

GitHub Copilot Chati saab kasutada mitmesugustes olukordades, näiteks:

- Vastamine koodiga seotud küsimustele, kuidas probleemi kõige paremini lahendada

- Kellegi teise koodi selgitamine ja parenduste soovitamine

- Koodiparanduste ettepanekud

- Üksustestide loomine

- Koodidokumentatsiooni genereerimine

Soovitatav lugemiseks: [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

### **Microsoft GitHub Copilot Chat @workspace**

Viidates **@workspace** Copilot Chatis, saate esitada küsimusi kogu oma koodibaasi kohta. Sõltuvalt küsimusest otsib Copilot intelligentselt asjakohaseid faile ja sümboleid, mida ta vastuses viitab linkide ja koodinäidetena.

Et vastata teie küsimusele, otsib **@workspace** samu allikaid, mida arendaja kasutaks koodibaasi sirvimisel VS Code'is:

- Kõik tööruumi failid, välja arvatud failid, mida .gitignore fail ignoreerib

- Kataloogistruktuur koos pesastatud kaustade ja failinimedega

- GitHubi koodiotsingu indeks, kui tööruum on GitHubi repositoorium ja indekseeritud koodiotsingu abil

- Sümbolid ja definitsioonid tööruumis

- Praegu valitud tekst või aktiivses redaktoris nähtav tekst

Märkus: .gitignore failist möödutakse, kui teil on fail avatud või tekst valitud ignoreeritud failis.

Soovitatav lugemiseks: [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)

## **Lisateave selle labori kohta**

GitHub Copilot on oluliselt parandanud ettevõtete programmeerimise efektiivsust ja iga ettevõte soovib kohandada GitHub Copiloti funktsioone vastavalt oma vajadustele. Paljud ettevõtted on kohandanud laiendusi, mis sarnanevad GitHub Copilotiga, tuginedes oma äristsenaariumidele ja avatud lähtekoodiga mudelitele. Ettevõtete jaoks on kohandatud laiendusi lihtsam hallata, kuid see võib mõjutada kasutajakogemust. Lõppude lõpuks on GitHub Copilot üldiste ja professionaalsete stsenaariumide käsitlemisel tugevam. Kui kogemus jääks samaks, oleks parem kohandada ettevõtte enda laiendust. GitHub Copilot Chat pakub vastavaid API-sid, et ettevõtted saaksid laiendada vestluskogemust. Ühtse kogemuse säilitamine ja kohandatud funktsioonide olemasolu pakub paremat kasutajakogemust.

See labor kasutab peamiselt Phi-3 mudelit koos kohaliku NPU ja Azure'i hübriidiga, et luua kohandatud agent GitHub Copilot Chatis ***@PHI3***, mis aitab ettevõtte arendajatel koodi genereerida ***(@PHI3 /gen)*** ja luua koodi piltide põhjal ***(@PHI3 /img)***.

![PHI3](../../../../../../../imgs/02/vscodeext/cover.png)

### ***Märkus:*** 

See labor on praegu rakendatud Intel CPU ja Apple Siliconi AIPC-s. Jätkame Qualcommi NPU versiooni uuendamist.

## **Labor**

| Nimi | Kirjeldus | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Installatsioonid(✅) | Seadistage ja installige seotud keskkonnad ja tööriistad | [Mine](./HOL/AIPC/01.Installations.md) |[Mine](./HOL/Apple/01.Installations.md) |
| Lab1 - Käivitage Prompt flow Phi-3-mini-ga (✅) | Kombineeritud AIPC / Apple Siliconiga, kasutades kohalikku NPU-d koodi genereerimiseks Phi-3-mini abil | [Mine](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Mine](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Deploy Phi-3-vision Azure Machine Learning Service'is (✅) | Looge koodi, kasutades Azure Machine Learning Service'i Model Catalog - Phi-3-vision pilti | [Mine](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Mine](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Looge @phi-3 agent GitHub Copilot Chatis (✅)  | Looge kohandatud Phi-3 agent GitHub Copilot Chatis, et täita koodi genereerimist, graafikute loomist, RAG-i jne | [Mine](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Mine](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Näidiskood (✅)  | Laadige alla näidiskood | [Mine](../../../../../../../code/07.Lab/01/AIPC) | [Mine](../../../../../../../code/07.Lab/01/Apple) |

## **Ressursid**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Lisateave GitHub Copiloti kohta [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Lisateave GitHub Copilot Chati kohta [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Lisateave GitHub Copilot Chati API kohta [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Lisateave Azure AI Foundry kohta [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Lisateave Azure AI Foundry Model Catalogi kohta [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.