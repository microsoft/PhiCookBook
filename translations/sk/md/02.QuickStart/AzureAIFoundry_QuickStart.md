<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a1e48b628022485aac989c9f733e792",
  "translation_date": "2025-05-09T20:14:40+00:00",
  "source_file": "md/02.QuickStart/AzureAIFoundry_QuickStart.md",
  "language_code": "sk"
}
-->
# **Použitie Phi-3 v Azure AI Foundry**

S rozvojom generatívnej AI chceme využiť jednotnú platformu na správu rôznych LLM a SLM, integráciu podnikových dát, operácie doladenia/RAG a hodnotenie rôznych podnikových procesov po integrácii LLM a SLM, aby bolo možné lepšie implementovať inteligentné aplikácie založené na generatívnej AI. [Azure AI Foundry](https://ai.azure.com) je podniková platforma pre aplikácie generatívnej AI.

![aistudo](../../../../translated_images/aifoundry_home.ffa4fe13d11f26171097f8666a1db96ac0979ffa1adde80374c60d1136c7e1de.sk.png)

S Azure AI Foundry môžete hodnotiť odpovede veľkých jazykových modelov (LLM) a orchestrácie komponentov aplikácie promptov pomocou prompt flow pre lepší výkon. Platforma umožňuje škálovateľnosť a jednoduchý prechod od konceptov k plnohodnotnej produkcii. Neustále monitorovanie a vylepšovanie podporujú dlhodobý úspech.

Model Phi-3 môžeme rýchlo nasadiť na Azure AI Foundry jednoduchými krokmi a následne využiť Azure AI Foundry na dokončenie súvisiacich úloh ako Playground/Chat, doladenie, hodnotenie a ďalšie.

## **1. Príprava**

Ak už máte nainštalovaný [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) na vašom zariadení, použitie tejto šablóny je také jednoduché ako spustiť tento príkaz v novom adresári.

## Manuálne vytvorenie

Vytvorenie projektu a hubu v Microsoft Azure AI Foundry je skvelý spôsob, ako organizovať a spravovať vašu AI prácu. Tu je krok za krokom návod, ako začať:

### Vytvorenie projektu v Azure AI Foundry

1. **Prejdite do Azure AI Foundry**: Prihláste sa do portálu Azure AI Foundry.
2. **Vytvorte projekt**:
   - Ak ste v nejakom projekte, vyberte "Azure AI Foundry" v ľavom hornom rohu stránky pre návrat na domovskú stránku.
   - Kliknite na "+ Create project".
   - Zadajte názov projektu.
   - Ak máte hub, bude predvolený. Ak máte prístup k viacerým hubom, môžete vybrať iný zo zoznamu. Ak chcete vytvoriť nový hub, vyberte "Create new hub" a zadajte jeho názov.
   - Kliknite na "Create".

### Vytvorenie hubu v Azure AI Foundry

1. **Prejdite do Azure AI Foundry**: Prihláste sa pomocou svojho Azure účtu.
2. **Vytvorte hub**:
   - Vyberte Management center v ľavom menu.
   - Kliknite na "All resources", potom na šípku vedľa "+ New project" a vyberte "+ New hub".
   - V dialógu "Create a new hub" zadajte názov hubu (napr. contoso-hub) a upravte ostatné polia podľa potreby.
   - Kliknite na "Next", skontrolujte informácie a potom kliknite na "Create".

Pre podrobnejšie pokyny môžete navštíviť oficiálnu [Microsoft dokumentáciu](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Po úspešnom vytvorení máte prístup do štúdia cez [ai.azure.com](https://ai.azure.com/)

Na jednom AI Foundry môže byť viacero projektov. Vytvorte projekt v AI Foundry na prípravu.

Vytvorte Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. Nasadenie Phi modelu v Azure AI Foundry**

Kliknite na možnosť Explore v projekte, prejdite do Model Catalog a vyberte Phi-3

Vyberte Phi-3-mini-4k-instruct

Kliknite na 'Deploy' pre nasadenie modelu Phi-3-mini-4k-instruct

> [!NOTE]
>
> Pri nasadzovaní môžete vybrať výpočtový výkon

## **3. Playground Chat Phi v Azure AI Foundry**

Prejdite na stránku nasadenia, vyberte Playground a komunikujte s Phi-3 v Azure AI Foundry

## **4. Nasadenie modelu z Azure AI Foundry**

Ak chcete nasadiť model z Azure Model Catalog, postupujte podľa týchto krokov:

- Prihláste sa do Azure AI Foundry.
- Vyberte model, ktorý chcete nasadiť, z katalógu modelov Azure AI Foundry.
- Na stránke detailov modelu vyberte Deploy a potom Serverless API s Azure AI Content Safety.
- Vyberte projekt, v ktorom chcete model nasadiť. Pre použitie Serverless API musí byť vaše pracovné prostredie v regióne East US 2 alebo Sweden Central. Môžete si prispôsobiť názov nasadenia.
- V sprievodcovi nasadením vyberte Pricing and terms, kde sa dozviete o cenách a podmienkach používania.
- Kliknite na Deploy. Počkajte, kým bude nasadenie pripravené a budete presmerovaní na stránku Deployments.
- Kliknite na Open in playground, aby ste mohli začať interagovať s modelom.
- Môžete sa vrátiť na stránku Deployments, vybrať nasadenie a poznačiť si Target URL endpointu a Secret Key, ktoré použijete na volanie nasadenia a generovanie odpovedí.
- Detaily endpointu, URL a prístupové kľúče nájdete vždy v záložke Build v sekcii Components pod Deployments.

> [!NOTE]
> Upozorňujeme, že vaše konto musí mať oprávnenia Azure AI Developer role v Resource Group, aby ste mohli vykonať tieto kroky.

## **5. Použitie Phi API v Azure AI Foundry**

Môžete pristupovať na https://{Your project name}.region.inference.ml.azure.com/swagger.json cez Postman pomocou GET a spojiť to s Key, aby ste sa zoznámili s dostupnými rozhraniami.

Veľmi pohodlne získate parametre požiadaviek aj odpovedí.

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.