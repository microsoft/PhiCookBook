# **Vytvorte si vlastný Visual Studio Code GitHub Copilot Chat s rodinou Microsoft Phi-3**

Použili ste už workspace agenta v GitHub Copilot Chat? Chcete si vytvoriť vlastného agenta kódu pre svoj tím? Tento praktický lab sa snaží skombinovať open source model na vytvorenie podnikateľského agenta pre kód na úrovni podniku.

## **Základy**

### **Prečo si vybrať Microsoft Phi-3**

Phi-3 je rodinná séria, zahŕňajúca phi-3-mini, phi-3-small a phi-3-medium založené na rôznych trénovacích parametroch pre generovanie textu, dokončovanie dialógov a generovanie kódu. Existuje aj phi-3-vision založený na Vision. Je vhodný pre podniky alebo rôzne tímy na vytváranie offline generatívnych AI riešení.

Odporúčame prečítať si tento odkaz [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Rozšírenie GitHub Copilot Chat vám poskytuje chatovacie rozhranie, ktoré vám umožní komunikovať s GitHub Copilot a dostávať odpovede na otázky súvisiace s kódovaním priamo vo VS Code, bez potreby prehliadať dokumentáciu alebo vyhľadávať na online fórach.

Copilot Chat môže používať zvýrazňovanie syntaxe, odsadenie a ďalšie funkcie formátovania na zvýraznenie generovanej odpovede. V závislosti od typu otázky od používateľa môže výsledok obsahovať odkazy na kontext, ktorý Copilot použil na generovanie odpovede, ako sú súbory zdrojového kódu alebo dokumentácia, alebo tlačidlá na prístup k funkciám VS Code.

- Copilot Chat sa integruje do vášho vývojárskeho toku a poskytuje vám pomoc tam, kde ju potrebujete:

- Začnite inline chat konverzáciu priamo z editora alebo terminálu pre pomoc počas kódovania

- Použite pohľad Chat na bočnej strane ako AI asistenta, ktorý vám pomôže kedykoľvek

- Spustite Rýchly chat na rýchlu otázku a rýchle pokračovanie v práci

GitHub Copilot Chat môžete použiť v rôznych scenároch, ako sú:

- Odpovedanie na otázky o tom, ako najlepšie vyriešiť problém

- Vysvetľovanie kódu niekoho iného a navrhovanie vylepšení

- Navrhovanie opráv kódu

- Generovanie jednotkových testovacích prípadov

- Generovanie dokumentácie kódu

Odporúčame prečítať si tento odkaz [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Referencia na **@workspace** v Copilot Chat vám umožňuje klásť otázky o celej vašej kódovej základni. Na základe otázky Copilot inteligentne načíta relevantné súbory a symboly, ktoré potom odkazuje vo svojej odpovedi ako odkazy a príklady kódu.

Na zodpovedanie vašej otázky **@workspace** prehľadáva rovnaké zdroje, aké používa vývojár pri navigácii v kódovej základni vo VS Code:

- Všetky súbory v pracovnom priestore, okrem súborov ignorovaných v .gitignore súbore

- Štruktúra adresárov s vnorenými názvami zložiek a súborov

- Kódový vyhľadávací index GitHubu, ak je pracovný priestor GitHub repozitárom a je indexovaný vyhľadávaním kódu

- Symboly a definície v pracovnom priestore

- Práve vybraný text alebo viditeľný text v aktívnom editore

Poznámka: .gitignore je obchádzaný, ak máte otvorený súbor alebo máte vybraný text v ignorovanom súbore.

Odporúčame prečítať si tento odkaz [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Viac o tomto Labe**

GitHub Copilot výrazne zlepšil efektivitu programovania v podnikoch a každý podnik túži prispôsobiť relevantné funkcie GitHub Copilot. Mnohé podniky si prispôsobili rozšírenia podobné GitHub Copilot na základe svojich vlastných obchodných scénarov a open source modelov. Pre podniky sú prispôsobené rozšírenia jednoduchšie na kontrolu, ale ovplyvňuje to aj používateľskú skúsenosť. Napokon, GitHub Copilot má silnejšie funkcie v riešení všeobecných scenárov a profesionality. Ak by sa skúsenosť mohla udržať konzistentná, bolo by lepšie prispôsobiť si vlastné rozšírenie podniku. GitHub Copilot Chat poskytuje relevantné API pre podniky na rozšírenie chatovej skúsenosti. Udržiavať konzistentnú skúsenosť a mať prispôsobené funkcie je lepšia používateľská skúsenosť.

Tento lab hlavne používa model Phi-3 v kombinácii s lokálnym NPU a Azure hybridom na vytvorenie vlastného Agenta v GitHub Copilot Chat ***@PHI3*** na pomoc podnikových vývojárov pri dokončení generovania kódu ***(@PHI3 /gen)*** a generovania kódu na základe obrázkov ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/sk/cover.1017ebc9a7c46d09.webp)

### ***Poznámka:*** 

Tento lab je momentálne implementovaný v AIPC na Intel CPU a Apple Silicon. Budeme pokračovať v aktualizácii verzie Qualcomm NPU.


## **Lab**


| Názov | Popis | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Inštalácie(✅) | Konfigurácia a inštalácia súvisiacich prostredí a inštalačných nástrojov | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Spustenie Prompt flow s Phi-3-mini (✅) | V kombinácii s AIPC / Apple Silicon použitie lokálneho NPU na vytvorenie generovania kódu cez Phi-3-mini | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Nasadenie Phi-3-vision na Azure Machine Learning Service(✅) | Generovanie kódu nasadením modelového katalógu Azure Machine Learning Service - Phi-3-vision obraz | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Vytvorte agenta @phi-3 v GitHub Copilot Chat(✅)  | Vytvorte vlastného Phi-3 agenta v GitHub Copilot Chat na dokončenie generovania kódu, generovania kódu grafov, RAG atď. | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Ukážkový kód (✅)  | Stiahnutie ukážkového kódu | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## **Zdroje**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Viac o GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Viac o GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Viac o GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Viac o Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Viac o modelovom katalógu Microsoft Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o vylúčení zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->