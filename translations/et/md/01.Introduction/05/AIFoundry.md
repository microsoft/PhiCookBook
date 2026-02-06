# **Azure AI Foundry kasutamine hindamiseks**

![aistudo](../../../../../imgs/01/05/AIFoundry/AIFoundry.png)

Kuidas hinnata oma generatiivse tehisintellekti rakendust, kasutades [Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Olenemata sellest, kas hindate ühe pöörde või mitme pöörde vestlusi, pakub Azure AI Foundry tööriistu mudeli jõudluse ja turvalisuse hindamiseks.

![aistudo](../../../../../imgs/01/05/AIFoundry/AIPortfolio.png)

## Kuidas hinnata generatiivseid tehisintellekti rakendusi Azure AI Foundry abil
Lisateabe saamiseks vaadake [Azure AI Foundry dokumentatsiooni](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo).

Siin on sammud alustamiseks:

## Generatiivsete tehisintellekti mudelite hindamine Azure AI Foundry abil

**Eeltingimused**

- Testandmestik kas CSV- või JSON-vormingus.
- Juurutatud generatiivse tehisintellekti mudel (näiteks Phi-3, GPT 3.5, GPT 4 või Davinci mudelid).
- Käituskeskkond arvutusressursiga hindamise läbiviimiseks.

## Sisseehitatud hindamismõõdikud

Azure AI Foundry võimaldab hinnata nii ühe pöörde kui ka keerulisi, mitme pöörde vestlusi.  
Retrieval Augmented Generation (RAG) stsenaariumide puhul, kus mudel põhineb spetsiifilistel andmetel, saate jõudlust hinnata sisseehitatud hindamismõõdikute abil.  
Lisaks saate hinnata üldisi ühe pöörde küsimuste-vastuste stsenaariume (mitte-RAG).

## Hindamisprotsessi loomine

Azure AI Foundry kasutajaliideses navigeerige kas hindamise lehele või Prompt Flow lehele.  
Järgige hindamise loomise viisardit, et seadistada hindamisprotsess. Andke oma hindamisele valikuline nimi.  
Valige stsenaarium, mis vastab teie rakenduse eesmärkidele.  
Valige üks või mitu hindamismõõdikut mudeli väljundi hindamiseks.

## Kohandatud hindamisprotsess (valikuline)

Suurema paindlikkuse saavutamiseks saate luua kohandatud hindamisprotsessi. Kohandage hindamisprotsess vastavalt oma konkreetsetele vajadustele.

## Tulemuste vaatamine

Pärast hindamise läbiviimist logige, vaadake ja analüüsige üksikasjalikke hindamismõõdikuid Azure AI Foundry keskkonnas. Saage ülevaade oma rakenduse võimekusest ja piirangutest.

**Märkus** Azure AI Foundry on hetkel avalikus eelvaates, seega kasutage seda katsetamiseks ja arendamiseks. Tootmiskoormuste jaoks kaaluge muid võimalusi. Lisateabe ja samm-sammuliste juhiste saamiseks uurige ametlikku [AI Foundry dokumentatsiooni](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo).

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.