# **Microsoft Foundry kasutamine hindamiseks**

![aistudo](../../../../../translated_images/et/AIFoundry.9e0b513e999a1c5a.webp)

Kuidas hinnata oma generatiivset tehisintellekti rakendust, kasutades [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Kas hindate ühekordseid vestlusi või mitmekordseid vestlusi, Microsoft Foundry pakub tööriistu mudeli jõudluse ja turvalisuse hindamiseks.

![aistudo](../../../../../translated_images/et/AIPortfolio.69da59a8e1eaa70f.webp)

## Kuidas hinnata generatiivseid AI-rakendusi Microsoft Foundry abil
Üksikasjalike juhiste saamiseks vaadake [Microsoft Foundry dokumentatsiooni](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Siin on sammud alustamiseks:

## Generatiivsete AI-mudelite hindamine Microsoft Foundrys

**Eeltingimused**

- Testandmekogu CSV- või JSON-vormingus.
- Käivitatud generatiivne AI mudel (näiteks Phi-3, GPT 3.5, GPT 4 või Davinci mudelid).
- Käituskeskkond koos arvutusinstantsiga hindamise läbiviimiseks.

## Sisseehitatud hindamismeetrikad

Microsoft Foundry võimaldab teil hinnata nii ühekordseid kui ka keerukaid mitmekordseid vestlusi.  
Hindamise jaoks paremaks teabepõhiseks loomise (RAG) stsenaariumites, kus mudel põhineb spetsiifilistel andmetel, saate hinnata jõudlust sisseehitatud hindamismeetodite abil.  
Lisaks saate hinnata üldisi ühekordse küsimuste-vastuste stsenaariume (mitte-RAG).

## Hindamise jooksu loomine

Microsoft Foundry kasutajaliidesest minge kas Evaluate lehele või Prompt Flow lehele.  
Järgige hindamise loomise viisardit hindamise jooksu seadistamiseks. Andke hindamisele vabatahtlik nimi.  
Valige stsenaarium, mis ühtib teie rakenduse eesmärkidega.  
Valige üks või mitu hindamismeetrit mudeli väljundi hindamiseks.

## Kohandatud hindamisvoog (valikuline)

Suurenda paindlikkust, luues kohandatud hindamisvoo. Kohanda hindamisprotsessi vastavalt oma konkreetsetele nõuetele.

## Tulemuste vaatamine

Pärast hindamise läbiviimist logige, vaadake ja analüüsige üksikasjalikke hindamismeetrikaid Microsoft Foundrys. Saage ülevaade oma rakenduse võimetest ja piirangutest.

**Note** Microsoft Foundry on hetkel avalikus beetaversioonis, seega kasutage seda katsetamiseks ja arendustöödeks. Tootmiskeskkondade jaoks kaaluge teisi võimalusi. Tutvuge ametliku [AI Foundry dokumentatsiooniga](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) üksikasjade ja samm-sammuliste juhiste saamiseks.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:  
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüame täpsust, palun arvestage, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument oma algkeeles tuleks pidada autoriteetseks allikaks. Kriitilise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->