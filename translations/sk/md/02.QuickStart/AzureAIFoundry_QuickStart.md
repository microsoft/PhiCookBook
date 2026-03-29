# **Používanie Phi-3 v Microsoft Foundry**

S rozvojom Generatívnej AI dúfame, že použijeme jednotnú platformu na správu rôznych LLM a SLM, integráciu podnikových dát, operácie ladania/fine-tuning/RAG a hodnotenie rôznych podnikov po integrácii LLM a SLM, atď., aby mohli byť inteligentné aplikácie generatívnej AI lepšie implementované. [Microsoft Foundry](https://ai.azure.com) je podniková platforma pre generatívne AI aplikácie.

![aistudo](../../../../translated_images/sk/aifoundry_home.f28a8127c96c7d93.webp)

S Microsoft Foundry môžete hodnotiť odpovede veľkého jazykového modelu (LLM) a orchestrovať komponenty aplikácie promptov pomocou prompt flow pre lepší výkon. Platforma uľahčuje škálovateľnosť pre transformáciu dôkazov konceptov do plnohodnotnej produkcie s ľahkosťou. Neustále monitorovanie a zdokonaľovanie podporujú dlhodobý úspech.

Model Phi-3 môžeme rýchlo nasadiť v Microsoft Foundry pomocou jednoduchých krokov a následne využiť Microsoft Foundry na dokončenie súvisiacich prác ako Playground/Chat, fine-tuning, hodnotenie a ďalšie.

## **1. Príprava**

Ak už máte na svojom počítači nainštalovaný [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo), použitie tejto šablóny je také jednoduché ako spustiť tento príkaz v novom adresári.

## Manuálne vytvorenie

Vytvorenie projektu a hubu v Microsoft Foundry je skvelý spôsob, ako organizovať a spravovať vašu prácu s AI. Tu je krok za krokom návod, ako začať:

### Vytvorenie projektu v Microsoft Foundry

1. **Choďte na Microsoft Foundry**: Prihláste sa do portálu Microsoft Foundry.
2. **Vytvorte projekt**:
   - Ak ste už v niektorom projekte, vyberte "Microsoft Foundry" v ľavom hornom rohu stránky, aby ste sa dostali na domovskú stránku.
   - Vyberte "+ Create project".
   - Zadajte názov projektu.
   - Ak máte hub, bude predvolene vybraný. Ak máte prístup k viacerým hubom, môžete z rozbaľovacieho zoznamu vybrať iný. Ak chcete vytvoriť nový hub, vyberte "Create new hub" a zadajte názov.
   - Vyberte "Create".

### Vytvorenie hubu v Microsoft Foundry

1. **Choďte na Microsoft Foundry**: Prihláste sa so svojím Azure účtom.
2. **Vytvorte hub**:
   - Vyberte Správu (Management center) z ľavého menu.
   - Vyberte "All resources", potom šípku dolu vedľa "+ New project" a zvoľte "+ New hub".
   - V dialógu "Create a new hub" zadajte názov pre váš hub (napr. contoso-hub) a upravte ďalšie polia podľa potreby.
   - Vyberte "Next", skontrolujte informácie a potom vyberte "Create".

Pre podrobnejšie inštrukcie sa môžete odvolať na oficiálnu [Microsoft dokumentáciu](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Po úspešnom vytvorení môžete pristupovať do štúdia, ktoré ste vytvorili cez [ai.azure.com](https://ai.azure.com/)

Na jednej platforme AI Foundry môže byť viacero projektov. Vytvorte projekt v AI Foundry ako prípravu.

Vytvorte Microsoft Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. Nasadenie Phi modelu v Microsoft Foundry**

Kliknite na možnosť Explore v projekte, aby ste vstúpili do Model Catalog a vyberte Phi-3

Vyberte Phi-3-mini-4k-instruct

Kliknite na 'Deploy' pre nasadenie modelu Phi-3-mini-4k-instruct

> [!NOTE]
>
> Pri nasadzovaní môžete vybrať výpočtový výkon

## **3. Playground Chat Phi v Microsoft Foundry**

Choďte na stránku nasadenia, vyberte Playground a chat s Phi-3 z Microsoft Foundry

## **4. Nasadenie modelu z Microsoft Foundry**

Ak chcete nasadiť model z Azure Model Catalog, postupujte podľa týchto krokov:

- Prihláste sa do Microsoft Foundry.
- Vyberte model, ktorý chcete nasadiť, z katalógu modelov Microsoft Foundry.
- Na stránke s detailmi modelu vyberte Deploy a potom Serverless API s Azure AI Content Safety.
- Vyberte projekt, v ktorom chcete model nasadiť. Na používanie Serverless API musí vaše pracovné prostredie patriť do regiónu East US 2 alebo Sweden Central. Môžete si prispôsobiť názov nasadenia.
- V sprievodcovi nasadením vyberte Pricing and terms pre informácie o cenách a podmienkach používania.
- Vyberte Deploy. Počkajte, kým je nasadenie hotové a budete presmerovaný na stránku Nasadení.
- Vyberte Open in playground, aby ste začali interagovať s modelom.
- Môžete sa vrátiť na stránku Nasadení, vybrať konkrétne nasadenie a zaznamenať si adresu cieľového URL a Tajný kľúč, ktoré môžete použiť na volanie nasadenia a generovanie výstupov.
- Vždy môžete získať detaily endpointu, URL a prístupové kľúče prechádzaním na záložku Build a výberom Nasadení v sekcii Components.

> [!NOTE]
> Prosím, všimnite si, že váš účet musí mať oprávnenia Azure AI Developer roly v Resource Groupe, aby ste mohli tieto kroky vykonať.

## **5. Používanie Phi API v Microsoft Foundry**

Môžete pristupovať na https://{Your project name}.region.inference.ml.azure.com/swagger.json cez Postman GET a spojiť to s kľúčom, aby ste sa dozvedeli o poskytovaných rozhraniach

Môžete veľmi pohodlne získať požadované parametre a taktiež parametre odpovedí.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vzniknuté použitím tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->