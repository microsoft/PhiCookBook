<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-07-17T03:44:25+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "sk"
}
-->
# **Vytvorte si vlastný Visual Studio Code GitHub Copilot Chat s Microsoft Phi-3 Family**

Použili ste už workspace agenta v GitHub Copilot Chat? Chcete si vytvoriť vlastného agenta pre tímový kód? Tento praktický workshop sa snaží spojiť open source model na vytvorenie podnikovej úrovne kódovacieho agenta.

## **Základy**

### **Prečo si vybrať Microsoft Phi-3**

Phi-3 je séria modelov, ktorá zahŕňa phi-3-mini, phi-3-small a phi-3-medium, založené na rôznych parametroch tréningu pre generovanie textu, dokončovanie dialógov a generovanie kódu. Existuje aj phi-3-vision založený na Vision. Je vhodný pre podniky alebo rôzne tímy na vytváranie offline generatívnych AI riešení.

Odporúčame prečítať tento odkaz [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Rozšírenie GitHub Copilot Chat vám poskytuje chatové rozhranie, ktoré vám umožňuje komunikovať s GitHub Copilot a získavať odpovede na otázky týkajúce sa kódovania priamo vo VS Code, bez potreby prehľadávať dokumentáciu alebo online fóra.

Copilot Chat môže používať zvýrazňovanie syntaxe, odsadenie a ďalšie formátovacie prvky na lepšiu prehľadnosť generovanej odpovede. V závislosti od typu otázky od používateľa môže výsledok obsahovať odkazy na kontext, ktorý Copilot použil pri generovaní odpovede, ako sú zdrojové súbory alebo dokumentácia, alebo tlačidlá na prístup k funkciám VS Code.

- Copilot Chat sa integruje do vášho vývojárskeho toku a poskytuje pomoc tam, kde ju potrebujete:

- Začnite inline chat priamo z editora alebo terminálu, keď potrebujete pomoc počas kódovania

- Použite zobrazenie Chat, aby ste mali AI asistenta po ruke kedykoľvek

- Spustite Quick Chat na rýchlu otázku a pokračujte v práci

GitHub Copilot Chat môžete využiť v rôznych situáciách, napríklad:

- Odpovedanie na otázky o tom, ako najlepšie vyriešiť problém

- Vysvetľovanie cudzieho kódu a navrhovanie vylepšení

- Navrhovanie opráv kódu

- Generovanie jednotkových testov

- Generovanie dokumentácie kódu

Odporúčame prečítať tento odkaz [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

### **Microsoft GitHub Copilot Chat @workspace**

Použitie **@workspace** v Copilot Chat vám umožňuje klásť otázky o celom vašom kódovom základe. Na základe otázky Copilot inteligentne vyhľadá relevantné súbory a symboly, ktoré potom v odpovedi uvádza ako odkazy a príklady kódu.

Na zodpovedanie vašej otázky **@workspace** prehľadáva rovnaké zdroje, aké by vývojár použil pri navigácii v kódovej základni vo VS Code:

- Všetky súbory v pracovnom priestore, okrem súborov ignorovaných súborom .gitignore

- Štruktúru adresárov s vnorenými priečinkami a názvami súborov

- Index vyhľadávania kódu GitHub, ak je pracovný priestor GitHub repozitár a je indexovaný vyhľadávaním kódu

- Symboly a definície v pracovnom priestore

- Aktuálne vybraný text alebo viditeľný text v aktívnom editore

Poznámka: .gitignore sa obchádza, ak máte otvorený súbor alebo máte vybraný text v ignorovanom súbore.

Odporúčame prečítať tento odkaz [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **Viac o tomto workshope**

GitHub Copilot výrazne zlepšil efektivitu programovania v podnikoch a každý podnik chce prispôsobiť relevantné funkcie GitHub Copilot. Mnohé podniky si prispôsobili rozšírenia podobné GitHub Copilot na základe svojich obchodných scenárov a open source modelov. Pre podniky sú prispôsobené rozšírenia ľahšie na kontrolu, no zároveň to ovplyvňuje používateľský zážitok. GitHub Copilot má totiž silnejšie funkcie pri riešení všeobecných scenárov a profesionality. Ak je možné zachovať konzistentný zážitok, je lepšie prispôsobiť vlastné podnikové rozšírenie. GitHub Copilot Chat poskytuje relevantné API pre podniky na rozšírenie chatového zážitku. Zachovanie konzistentného zážitku a zároveň prispôsobené funkcie prinášajú lepší používateľský zážitok.

Tento workshop využíva model Phi-3 v kombinácii s lokálnym NPU a hybridom Azure na vytvorenie vlastného agenta v GitHub Copilot Chat ***@PHI3***, ktorý pomáha podnikovým vývojárom dokončiť generovanie kódu ***(@PHI3 /gen)*** a generovanie kódu na základe obrázkov ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/cover.1017ebc9a7c46d09.sk.png)

### ***Poznámka:***

Tento workshop je momentálne implementovaný na AIPC Intel CPU a Apple Silicon. Pokračujeme v aktualizácii verzie NPU pre Qualcomm.

## **Workshop**

| Názov | Popis | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Inštalácie(✅) | Konfigurácia a inštalácia súvisiacich prostredí a inštalačných nástrojov | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Spustenie Prompt flow s Phi-3-mini (✅) | V kombinácii s AIPC / Apple Silicon, využitie lokálneho NPU na vytvorenie generovania kódu cez Phi-3-mini | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Nasadenie Phi-3-vision na Azure Machine Learning Service(✅) | Generovanie kódu nasadením modelu Phi-3-vision z katalógu Azure Machine Learning Service | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Vytvorenie @phi-3 agenta v GitHub Copilot Chat(✅)  | Vytvorenie vlastného Phi-3 agenta v GitHub Copilot Chat na dokončenie generovania kódu, generovanie grafov, RAG a ďalšie | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Ukážkový kód (✅)  | Stiahnutie ukážkového kódu | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |

## **Zdroje**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Viac o GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Viac o GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Viac o GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Viac o Azure AI Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Viac o katalógu modelov Azure AI Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.