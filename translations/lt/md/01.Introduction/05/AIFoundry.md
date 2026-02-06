# **Naudojant Azure AI Foundry vertinimui**

![aistudo](../../../../../imgs/01/05/AIFoundry/AIFoundry.png)

Kaip įvertinti savo generatyviosios AI programą naudojant [Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Nesvarbu, ar vertinate vieno žingsnio, ar daugiapakopius pokalbius, Azure AI Foundry siūlo įrankius modelio našumo ir saugumo vertinimui.

![aistudo](../../../../../imgs/01/05/AIFoundry/AIPortfolio.png)

## Kaip vertinti generatyviosios AI programas su Azure AI Foundry
Daugiau informacijos rasite [Azure AI Foundry dokumentacijoje](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo).

Štai žingsniai, kaip pradėti:

## Generatyviųjų AI modelių vertinimas Azure AI Foundry

**Būtinos sąlygos**

- Testavimo duomenų rinkinys CSV arba JSON formatu.
- Įdiegtas generatyviosios AI modelis (pvz., Phi-3, GPT 3.5, GPT 4 arba Davinci modeliai).
- Veikimo aplinka su skaičiavimo instancija vertinimui vykdyti.

## Integruoti vertinimo rodikliai

Azure AI Foundry leidžia vertinti tiek vieno žingsnio, tiek sudėtingus daugiapakopius pokalbius. 
RAG (Retrieval Augmented Generation) scenarijams, kur modelis remiasi konkrečiais duomenimis, galite vertinti našumą naudodami integruotus vertinimo rodiklius. 
Be to, galite vertinti bendrus vieno žingsnio klausimų ir atsakymų scenarijus (ne RAG).

## Vertinimo vykdymo sukūrimas

Azure AI Foundry sąsajoje eikite į Vertinimo puslapį arba Prompt Flow puslapį. 
Sekite vertinimo kūrimo vedlį, kad nustatytumėte vertinimo vykdymą. Suteikite savo vertinimui pasirenkamą pavadinimą. 
Pasirinkite scenarijų, kuris atitinka jūsų programos tikslus. 
Pasirinkite vieną ar daugiau vertinimo rodiklių modelio rezultatų vertinimui.

## Individualizuotas vertinimo procesas (pasirinktinai)

Norėdami didesnio lankstumo, galite sukurti individualizuotą vertinimo procesą. Pritaikykite vertinimo eigą pagal savo specifinius poreikius.

## Rezultatų peržiūra

Po vertinimo vykdymo peržiūrėkite, analizuokite ir registruokite detalius vertinimo rodiklius Azure AI Foundry. Sužinokite savo programos galimybes ir apribojimus.

**Pastaba** Azure AI Foundry šiuo metu yra viešojoje peržiūroje, todėl naudokite ją eksperimentavimui ir kūrimui. Produkcijos darbo krūviams apsvarstykite kitas galimybes. Daugiau informacijos ir žingsnis po žingsnio instrukcijas rasite oficialioje [AI Foundry dokumentacijoje](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.