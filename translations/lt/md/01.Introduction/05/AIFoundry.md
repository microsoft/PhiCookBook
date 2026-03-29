# **Kaip naudotis Microsoft Foundry vertinimui**

![aistudo](../../../../../translated_images/lt/AIFoundry.9e0b513e999a1c5a.webp)

Kaip įvertinti savo generatyvios dirbtinio intelekto (DI) programą naudojant [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Nesvarbu, ar vertinate vieno apsisukimo, ar daugiaprasmius pokalbius, Microsoft Foundry suteikia įrankius modeliui vertinti pagal našumą ir saugumą.

![aistudo](../../../../../translated_images/lt/AIPortfolio.69da59a8e1eaa70f.webp)

## Kaip vertinti generatyvios DI programas su Microsoft Foundry  
Išsamesnę instrukciją rasite [Microsoft Foundry dokumentacijoje](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Štai žingsniai, kaip pradėti:

## Generatyvių DI modelių vertinimas Microsoft Foundry

**Išankstiniai reikalavimai**

- Testavimo duomenų rinkinys CSV arba JSON formatu.  
- Įdiegta generatyvi DI modelis (pvz., Phi-3, GPT 3.5, GPT 4 arba Davinci modeliai).  
- Veikimo laikas su skaičiavimo įrenginiu vertinimo vykdymui.

## Įmontuoti vertinimo rodikliai

Microsoft Foundry leidžia vertinti tiek vieno apsisukimo, tiek sudėtingus daugiaprasmius pokalbius.  
Retrieval Augmented Generation (RAG) scenarijuose, kai modelis grindžiamas specifiniais duomenimis, veiklumą galite vertinti naudodami įmontuotus vertinimo rodiklius.  
Taip pat galima vertinti ir bendrus vieno apsisukimo klausimų-atsakymų scenarijus (ne RAG).

## Vertinimo paleidimo kūrimas

Iš Microsoft Foundry vartotojo sąsajos eikite į Evaluate puslapį arba Prompt Flow puslapį.  
Priteikite vertinimo kūrimo vedlį, kad nustatytumėte vertinimą. Pateikite pasirenkamą vertinimo pavadinimą.  
Pasirinkite scenarijų, atitinkantį jūsų programos tikslus.  
Pasirinkite vieną ar kelis vertinimo rodiklius modeliui įvertinti.

## Pasirinktinis vertinimo srautas (neprivaloma)

Didesniam lankstumui galite sukurti pasirinktą vertinimo srautą. Pritaikykite vertinimo procesą pagal savo konkrečius reikalavimus.

## Rezultatų peržiūra

Po vertinimo paleidimo registruokite, peržiūrėkite ir analizuokite išsamius vertinimo rodiklius Microsoft Foundry. Gaukite įžvalgų apie savo programos galimybes ir ribotumus.

**Pastaba** Microsoft Foundry šiuo metu yra viešas peržiūros režimas, todėl naudokite jį eksperimentams ir kūrimui. Produkciniam darbui apsvarstykite kitus sprendimus. Išsamiau žiūrėkite oficialioje [AI Foundry dokumentacijoje](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmonių vertimas. Mes neatsakome už bet kokius nesusipratimus ar klaidingus aiškinimus, kilusius naudojant šį vertimą.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->