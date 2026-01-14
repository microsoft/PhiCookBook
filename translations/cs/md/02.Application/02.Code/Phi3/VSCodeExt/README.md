<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-07-17T03:44:04+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "cs"
}
-->
# **Vytvořte si vlastní Visual Studio Code GitHub Copilot Chat s Microsoft Phi-3 Family**

Použili jste už workspace agenta v GitHub Copilot Chat? Chcete si vytvořit vlastního agenta pro kódování pro váš tým? Tento praktický lab si klade za cíl spojit open source model a vytvořit podnikový agent pro kódování na úrovni firmy.

## **Základy**

### **Proč zvolit Microsoft Phi-3**

Phi-3 je rodina modelů, která zahrnuje phi-3-mini, phi-3-small a phi-3-medium, založené na různých tréninkových parametrech pro generování textu, dokončování dialogů a generování kódu. K dispozici je také phi-3-vision založený na Vision. Je vhodný pro firmy nebo různé týmy, které chtějí vytvářet offline generativní AI řešení.

Doporučujeme přečíst tento odkaz [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Rozšíření GitHub Copilot Chat vám poskytuje chatovací rozhraní, které vám umožní komunikovat s GitHub Copilot a získávat odpovědi na otázky týkající se kódování přímo ve VS Code, aniž byste museli procházet dokumentaci nebo hledat na online fórech.

Copilot Chat může využívat zvýraznění syntaxe, odsazení a další formátovací prvky, aby byla odpověď přehlednější. V závislosti na typu otázky může výsledek obsahovat odkazy na kontext, který Copilot použil při generování odpovědi, například zdrojové soubory nebo dokumentaci, nebo tlačítka pro přístup k funkcím VS Code.

- Copilot Chat se integruje do vašeho vývojářského toku a poskytuje pomoc tam, kde ji potřebujete:

- Zahajte inline chat přímo z editoru nebo terminálu, když potřebujete pomoc při kódování

- Použijte zobrazení Chat, abyste měli AI asistenta po ruce kdykoliv

- Spusťte Quick Chat pro rychlou otázku a rychlý návrat k práci

GitHub Copilot Chat můžete využít v různých situacích, například:

- Odpovídání na otázky ohledně kódování a nejlepších řešení problému

- Vysvětlování cizího kódu a navrhování vylepšení

- Navrhování oprav kódu

- Generování jednotkových testů

- Generování dokumentace kódu

Doporučujeme přečíst tento odkaz [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

### **Microsoft GitHub Copilot Chat @workspace**

Odkazování na **@workspace** v Copilot Chat vám umožňuje klást otázky týkající se celého vašeho kódového základu. Na základě otázky Copilot inteligentně vyhledá relevantní soubory a symboly, které pak ve své odpovědi uvádí jako odkazy a příklady kódu.

Pro odpověď na vaši otázku **@workspace** prohledává stejné zdroje, které by vývojář použil při procházení kódové základny ve VS Code:

- Všechny soubory ve workspace, kromě těch, které jsou ignorovány souborem .gitignore

- Strukturu adresářů včetně vnořených složek a názvů souborů

- Index vyhledávání kódu GitHubu, pokud je workspace repozitářem GitHubu a je indexován vyhledáváním kódu

- Symboly a definice ve workspace

- Aktuálně vybraný text nebo viditelný text v aktivním editoru

Poznámka: .gitignore je ignorován, pokud máte otevřený soubor nebo vybraný text v ignorovaném souboru.

Doporučujeme přečíst tento odkaz [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **Více o tomto labu**

GitHub Copilot výrazně zlepšil efektivitu programování ve firmách a každá firma si přeje přizpůsobit relevantní funkce GitHub Copilot. Mnoho firem si na základě svých obchodních scénářů a open source modelů přizpůsobilo rozšíření podobná GitHub Copilot. Pro firmy jsou přizpůsobená rozšíření snáze ovladatelná, ale to může ovlivnit uživatelský zážitek. GitHub Copilot má totiž silnější funkce pro obecné scénáře a profesionální použití. Pokud lze zachovat konzistentní zážitek, je lepší přizpůsobit si vlastní firemní rozšíření. GitHub Copilot Chat poskytuje relevantní API, která firmám umožňují rozšířit chatovací zážitek. Zachování konzistentního zážitku a zároveň přizpůsobení funkcí znamená lepší uživatelský zážitek.

Tento lab využívá model Phi-3 v kombinaci s lokálním NPU a hybridním Azure k vytvoření vlastního agenta v GitHub Copilot Chat ***@PHI3***, který pomáhá vývojářům ve firmě s generováním kódu***(@PHI3 /gen)*** a generováním kódu na základě obrázků ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/cs/cover.1017ebc9a7c46d09.png)

### ***Poznámka:***

Tento lab je momentálně implementován na AIPC Intel CPU a Apple Silicon. Budeme pokračovat v aktualizaci verze pro Qualcomm NPU.

## **Lab**

| Název | Popis | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Instalace(✅) | Konfigurace a instalace souvisejících prostředí a instalačních nástrojů | [Jít](./HOL/AIPC/01.Installations.md) |[Jít](./HOL/Apple/01.Installations.md) |
| Lab1 - Spuštění Prompt flow s Phi-3-mini (✅) | V kombinaci s AIPC / Apple Silicon, využití lokálního NPU pro generování kódu pomocí Phi-3-mini | [Jít](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Jít](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Nasazení Phi-3-vision na Azure Machine Learning Service(✅) | Generování kódu nasazením modelu Phi-3-vision z katalogu Azure Machine Learning Service | [Jít](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Jít](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Vytvoření @phi-3 agenta v GitHub Copilot Chat(✅)  | Vytvoření vlastního Phi-3 agenta v GitHub Copilot Chat pro dokončení generování kódu, generování grafů, RAG atd. | [Jít](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Jít](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Ukázkový kód (✅)  | Stažení ukázkového kódu | [Jít](../../../../../../../code/07.Lab/01/AIPC) | [Jít](../../../../../../../code/07.Lab/01/Apple) |

## **Zdroje**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Více o GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Více o GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Více o GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Více o Azure AI Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Více o katalogu modelů Azure AI Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.