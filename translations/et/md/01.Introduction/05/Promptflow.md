<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cbe7629d254f1043193b7fe22524d55",
  "translation_date": "2025-10-11T12:17:33+00:00",
  "source_file": "md/01.Introduction/05/Promptflow.md",
  "language_code": "et"
}
-->
# **Tutvustus: Promptflow**

[Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) on visuaalne töövoo automatiseerimise tööriist, mis võimaldab kasutajatel luua automatiseeritud töövooge, kasutades eelnevalt loodud malle ja kohandatud ühendusi. See on loodud selleks, et arendajad ja ärianalüütikud saaksid kiiresti luua automatiseeritud protsesse, mis hõlmavad näiteks andmehaldust, koostööd ja protsesside optimeerimist. Prompt Flow abil saavad kasutajad hõlpsasti ühendada erinevaid teenuseid, rakendusi ja süsteeme ning automatiseerida keerukaid äriprotsesse.

Microsoft Prompt Flow on loodud selleks, et lihtsustada suurte keelemudelite (LLM-ide) toel töötavate tehisintellekti rakenduste arendamise tsüklit algusest lõpuni. Olgu tegemist ideede genereerimise, prototüüpimise, testimise, hindamise või juurutamisega, Prompt Flow muudab protsessi lihtsamaks ja võimaldab luua tootmiskvaliteediga LLM-rakendusi.

## Siin on Microsoft Prompt Flow kasutamise peamised omadused ja eelised:

**Interaktiivne autorikogemus**

Prompt Flow pakub visuaalset esitust teie töövoo struktuurist, muutes projektide mõistmise ja navigeerimise lihtsaks.  
See pakub märkmikulaadset kodeerimiskogemust, mis võimaldab tõhusat töövoo arendamist ja silumist.

**Küsimuste variandid ja häälestamine**

Looge ja võrrelge mitmeid küsimuste variante, et hõlbustada iteratiivset täiustamisprotsessi.  
Hinnake erinevate küsimuste jõudlust ja valige kõige tõhusamad.

**Sisseehitatud hindamistöövood**  
Hinnake oma küsimuste ja töövoogude kvaliteeti ja tõhusust sisseehitatud hindamisvahendite abil.  
Mõistke, kui hästi teie LLM-põhised rakendused toimivad.

**Ulatuslikud ressursid**

Prompt Flow sisaldab sisseehitatud tööriistade, näidete ja mallide kogu. Need ressursid on arenduse lähtepunktiks, inspireerivad loovust ja kiirendavad protsessi.

**Koostöö ja ettevõttevalmidus**

Toetage meeskonnatööd, võimaldades mitmel kasutajal koos töötada küsimuste inseneerimise projektide kallal.  
Hoidke versioonikontrolli ja jagage teadmisi tõhusalt. Lihtsustage kogu küsimuste inseneerimise protsessi alates arendamisest ja hindamisest kuni juurutamise ja jälgimiseni.

## Hindamine Prompt Flow's

Microsoft Prompt Flow's mängib hindamine olulist rolli tehisintellekti mudelite jõudluse hindamisel. Vaatame, kuidas saate kohandada hindamistöövooge ja mõõdikuid Prompt Flow's:

![PFVizualise](../../../../../imgs/01/05/PromptFlow/pfvisualize.png)

**Hindamise mõistmine Prompt Flow's**

Prompt Flow's esindab töövoog sõlmede järjestust, mis töötlevad sisendit ja genereerivad väljundit. Hindamistöövood on spetsiaalsed töövood, mis on loodud jooksu jõudluse hindamiseks kindlate kriteeriumide ja eesmärkide alusel.

**Hindamistöövoogude peamised omadused**

Need käivitatakse tavaliselt pärast testitavat töövoogu, kasutades selle väljundeid.  
Need arvutavad hindeid või mõõdikuid, et mõõta testitava töövoo jõudlust.  
Mõõdikud võivad hõlmata täpsust, asjakohasuse hindeid või muid olulisi näitajaid.

### Hindamistöövoogude kohandamine

**Sisendite määratlemine**

Hindamistöövood peavad vastu võtma testitava jooksu väljundeid. Määratlege sisendid sarnaselt tavaliste töövoogudega.  
Näiteks, kui hindate küsimuste-vastuste töövoogu, nimetage sisend "vastus". Kui hindate klassifitseerimise töövoogu, nimetage sisend "kategooria". Võib olla vaja ka tõeseid sisendeid (nt tegelikud sildid).

**Väljundid ja mõõdikud**

Hindamistöövood toodavad tulemusi, mis mõõdavad testitava töövoo jõudlust.  
Mõõdikuid saab arvutada Pythoniga või suurte keelemudelite (LLM) abil. Kasutage funktsiooni log_metric(), et logida asjakohaseid mõõdikuid.

**Kohandatud hindamistöövoogude kasutamine**

Arendage oma hindamistöövoog, mis on kohandatud teie konkreetsete ülesannete ja eesmärkide jaoks.  
Kohandage mõõdikuid vastavalt oma hindamise eesmärkidele.  
Rakendage seda kohandatud hindamistöövoogu partiijooksudele suuremahulise testimise jaoks.

## Sisseehitatud hindamismeetodid

Prompt Flow pakub ka sisseehitatud hindamismeetodeid.  
Saate esitada partiijookse ja kasutada neid meetodeid, et hinnata, kui hästi teie töövoog suurte andmekogumitega toimib.  
Vaadake hindamistulemusi, võrrelge mõõdikuid ja tehke vajadusel muudatusi.  
Pidage meeles, et hindamine on oluline, et tagada teie tehisintellekti mudelite vastavus soovitud kriteeriumidele ja eesmärkidele. Vaadake ametlikku dokumentatsiooni, et saada üksikasjalikke juhiseid hindamistöövoogude arendamise ja kasutamise kohta Microsoft Prompt Flow's.

Kokkuvõtteks võib öelda, et Microsoft Prompt Flow annab arendajatele võimaluse luua kõrgekvaliteedilisi LLM-rakendusi, lihtsustades küsimuste inseneerimist ja pakkudes tugevat arenduskeskkonda. Kui töötate LLM-idega, on Prompt Flow väärtuslik tööriist, mida uurida. Tutvuge [Prompt Flow hindamise dokumentatsiooniga](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo), et saada üksikasjalikke juhiseid hindamistöövoogude arendamise ja kasutamise kohta Microsoft Prompt Flow's.

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.