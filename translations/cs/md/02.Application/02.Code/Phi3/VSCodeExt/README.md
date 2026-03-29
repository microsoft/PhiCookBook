# **Vytvořte si vlastní Visual Studio Code GitHub Copilot Chat s Microsoft Phi-3 Family**

Použili jste pracovní agent v GitHub Copilot Chat? Chcete si vytvořit vlastního agenta pro kódování pro váš tým? Tento praktický kurz si klade za cíl zkombinovat open source model pro vytvoření podnikové úrovně kódovacího obchodního agenta.

## **Základy**

### **Proč zvolit Microsoft Phi-3**

Phi-3 je rodinná řada, zahrnující phi-3-mini, phi-3-small a phi-3-medium založené na různých tréninkových parametrech pro generování textu, dokončení dialogu a generování kódu. Existuje také phi-3-vision založená na Vision. Je vhodná pro podniky nebo různé týmy k vytváření offline generativních AI řešení.

Doporučujeme prostudovat tento odkaz [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Rozšíření GitHub Copilot Chat vám poskytuje chatovací rozhraní, které vám umožňuje komunikovat s GitHub Copilot a získávat odpovědi na otázky související s kódováním přímo ve VS Code, aniž byste museli procházet dokumentaci nebo hledat na online fórech.

Copilot Chat může používat zvýraznění syntaxe, odsazení a další formátovací prvky, aby bylo odpovědi lépe rozumět. V závislosti na typu otázky uživatele může výsledek obsahovat odkazy na kontext, který Copilot použil k generování odpovědi, jako jsou zdrojové soubory nebo dokumentace, nebo tlačítka pro přístup k funkcím VS Code.

- Copilot Chat se integruje do vašeho vývojářského pracovního postupu a poskytuje asistenci tam, kde ji potřebujete:

- Zahajte inline chatovou konverzaci přímo z editoru nebo terminálu, abyste získali pomoc během kódování

- Použijte zobrazení Chat, abyste měli AI asistenta po ruce kdykoli

- Spusťte Quick Chat, abyste položili rychlou otázku a mohli se rychle vrátit k práci

GitHub Copilot Chat můžete používat v různých situacích, například:

- Odpovídání na otázky týkající se kódování a nejlepšího řešení problému

- Vysvětlování cizího kódu a navrhování vylepšení

- Navrhování oprav kódu

- Generování jednotkových testů

- Generování dokumentace kódu

Doporučujeme prostudovat tento odkaz [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

### **Microsoft GitHub Copilot Chat @workspace**

Použití **@workspace** v Copilot Chat vám umožňuje klást otázky o celém vašem kódovém základu. Na základě otázky Copilot inteligentně vyhledá relevantní soubory a symboly, které následně uvádí ve své odpovědi jako odkazy a příklady kódu.

Pro odpověď na vaši otázku **@workspace** prochází stejné zdroje, které by vývojář použil při prohlížení kódové základny ve VS Code:

- Všechny soubory v pracovním prostoru kromě těch, které jsou ignorovány souborem .gitignore

- Struktura adresářů se zanořenými složkami a názvy souborů

- GitHubův index vyhledávání kódu, pokud je pracovní prostor repozitářem GitHubu a je indexován pomocí vyhledávání kódu

- Symboly a definice v pracovním prostoru

- Aktuálně vybraný text nebo viditelný text v aktivním editoru

Poznámka: .gitignore je obejit, pokud máte otevřený soubor nebo je vybraný text v ignorovaném souboru.

Doporučujeme prostudovat tento odkaz [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **Více o tomto kurzu**

GitHub Copilot výrazně zlepšil efektivitu programování v podnicích a každý podnik chce přizpůsobit relevantní funkce GitHub Copilot. Mnoho podniků si přizpůsobilo rozšíření podobná GitHub Copilotu na základě svých obchodních scénářů a open source modelů. Pro podniky jsou přizpůsobená rozšíření snazší na kontrolu, ale ovlivňuje to i uživatelský zážitek. GitHub Copilot má totiž silnější funkce pro obecné scénáře a profesionálnost. Pokud by bylo možné zachovat konzistentní zkušenost, bylo by lepší přizpůsobit vlastní podnikovou rozšíření. GitHub Copilot Chat poskytuje příslušné API pro rozšíření chatu v podnicích. Zachování konzistentního zážitku a přitom mít přizpůsobené funkce je lepší uživatelský zážitek.

Tento kurz hlavně využívá model Phi-3 v kombinaci s lokálním NPU a hybridním Azurem pro vytvoření vlastního agenta v GitHub Copilot Chat ***@PHI3*** k asistenci podnikovým vývojářům při dokončování generování kódu ***(@PHI3 /gen)*** a generování kódu na základě obrázků ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/cs/cover.1017ebc9a7c46d09.webp)

### ***Poznámka:*** 

Tento kurz je nyní implementován na AIPC Intel CPU a Apple Silicon. Budeme pokračovat v aktualizacích verze NPU od Qualcommu.


## **Kurz**

| Název | Popis | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Instalace(✅) | Konfigurace a instalace souvisejících prostředí a instalačních nástrojů | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Spuštění Prompt flow s Phi-3-mini (✅) | V kombinaci s AIPC / Apple Silicon, použití lokálního NPU pro vytvoření generování kódu prostřednictvím Phi-3-mini | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Nasazení Phi-3-vision na Azure Machine Learning Service(✅) | Generování kódu nasazením modelu Phi-3-vision z katalogu Azure Machine Learning Service | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Vytvoření @phi-3 agenta v GitHub Copilot Chat(✅)  | Vytvoření vlastního Phi-3 agenta v GitHub Copilot Chat pro dokončení generování kódu, generování kódu pro grafy, RAG atd. | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Vzorový kód (✅)  | Stažení vzorového kódu | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## **Zdroje**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Více informací o GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Více informací o GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Více informací o GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Více informací o Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Více informací o katalogu modelů Microsoft Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo špatné výklady vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->