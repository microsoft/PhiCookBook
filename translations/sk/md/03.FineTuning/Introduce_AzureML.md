<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7fe541373802e33568e94e13226d463c",
  "translation_date": "2025-07-17T09:47:38+00:00",
  "source_file": "md/03.FineTuning/Introduce_AzureML.md",
  "language_code": "sk"
}
-->
# **Predstavenie služby Azure Machine Learning**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo) je cloudová služba na zrýchlenie a správu životného cyklu projektov strojového učenia (ML).

Odborníci na ML, dátoví vedci a inžinieri ju môžu používať vo svojich každodenných pracovných postupoch na:

- Trénovanie a nasadzovanie modelov.
- Správu operácií strojového učenia (MLOps).
- Môžete vytvoriť model v Azure Machine Learning alebo použiť model vytvorený na open-source platforme, ako sú PyTorch, TensorFlow alebo scikit-learn.
- Nástroje MLOps vám pomáhajú monitorovať, znovu trénovať a znovu nasadzovať modely.

## Pre koho je Azure Machine Learning určený?

**Dátoví vedci a ML inžinieri**

Môžu využívať nástroje na zrýchlenie a automatizáciu svojich každodenných pracovných postupov.  
Azure ML poskytuje funkcie pre spravodlivosť, vysvetliteľnosť, sledovanie a auditovateľnosť.

**Vývojári aplikácií:**  
Môžu bezproblémovo integrovať modely do aplikácií alebo služieb.

**Vývojári platforiem**

Majú prístup k robustnej sade nástrojov podporovaných trvácnymi Azure Resource Manager API.  
Tieto nástroje umožňujú vytvárať pokročilé ML nástroje.

**Podniky**

Pracujúce v cloude Microsoft Azure využívajú známe zabezpečenie a riadenie prístupu na základe rolí.  
Nastavte projekty na kontrolu prístupu k chráneným údajom a konkrétnym operáciám.

## Produktivita pre celý tím  
Projekty ML často vyžadujú tím s rôznorodými zručnosťami na ich vytváranie a údržbu.

Azure ML poskytuje nástroje, ktoré vám umožnia:  
- Spolupracovať s tímom prostredníctvom zdieľaných poznámkových blokov, výpočtových zdrojov, serverless výpočtov, dát a prostredí.  
- Vyvíjať modely so zameraním na spravodlivosť, vysvetliteľnosť, sledovanie a auditovateľnosť, aby ste splnili požiadavky na pôvodnosť a súlad s auditom.  
- Rýchlo a jednoducho nasadzovať ML modely vo veľkom meradle a efektívne ich spravovať a riadiť pomocou MLOps.  
- Spúšťať úlohy strojového učenia kdekoľvek s integrovanou správou, zabezpečením a súladom.

## Nástroje platformy kompatibilné naprieč prostrediami

Každý člen ML tímu môže používať svoje obľúbené nástroje na splnenie úloh.  
Či už vykonávate rýchle experimenty, ladenie hyperparametrov, tvorbu pipeline alebo správu inferencií, môžete používať známe rozhrania vrátane:  
- Azure Machine Learning Studio  
- Python SDK (v2)  
- Azure CLI (v2)  
- Azure Resource Manager REST API

Počas dolaďovania modelov a spolupráce v priebehu vývojového cyklu môžete zdieľať a vyhľadávať aktíva, zdroje a metriky v používateľskom rozhraní Azure Machine Learning studia.

## **LLM/SLM v Azure ML**

Azure ML pridalo množstvo funkcií súvisiacich s LLM/SLM, ktoré kombinujú LLMOps a SLMOps na vytvorenie podnikového generatívneho AI technologického platformy.

### **Katalóg modelov**

Podnikový používatelia môžu nasadzovať rôzne modely podľa rôznych obchodných scenárov cez Katalóg modelov a poskytovať služby ako Model ako službu pre podnikových vývojárov alebo používateľov.

![models](../../../../translated_images/sk/models.e6c7ff50a51806fd.png)

Katalóg modelov v Azure Machine Learning studiu je centrum na objavovanie a používanie širokej škály modelov, ktoré vám umožňujú vytvárať generatívne AI aplikácie. Katalóg obsahuje stovky modelov od poskytovateľov ako Azure OpenAI service, Mistral, Meta, Cohere, Nvidia, Hugging Face, vrátane modelov trénovaných Microsoftom. Modely od iných poskytovateľov než Microsoft sú považované za Ne-Microsoft produkty podľa podmienok Microsoftu a podliehajú podmienkam dodaným s modelom.

### **Job Pipeline**

Jadro pipeline strojového učenia spočíva v rozdelení kompletného úlohy strojového učenia na viacstupňový pracovný tok. Každý krok je zvládnuteľná súčasť, ktorú možno samostatne vyvíjať, optimalizovať, konfigurovať a automatizovať. Kroky sú prepojené cez dobre definované rozhrania. Služba pipeline Azure Machine Learning automaticky koordinuje všetky závislosti medzi krokmi pipeline.

Pri dolaďovaní SLM / LLM môžeme spravovať naše dáta, trénovanie a generovanie prostredníctvom Pipeline.

![finetuning](../../../../translated_images/sk/finetuning.6559da198851fa52.png)

### **Prompt flow**

Výhody používania Azure Machine Learning prompt flow  
Azure Machine Learning prompt flow ponúka množstvo výhod, ktoré pomáhajú používateľom prejsť od nápadu cez experimentovanie až po produkčne pripravené aplikácie založené na LLM:

**Agilita prompt inžinierstva**

Interaktívne vytváranie: Azure Machine Learning prompt flow poskytuje vizuálne znázornenie štruktúry toku, čo umožňuje používateľom ľahko pochopiť a navigovať svoje projekty. Tiež ponúka skúsenosť podobnú poznámkovému bloku pre efektívny vývoj a ladenie toku.  
Varianty pre ladenie promptov: Používatelia môžu vytvárať a porovnávať viacero variantov promptov, čo uľahčuje iteratívne dolaďovanie.

Hodnotenie: Vstavané hodnotiace toky umožňujú používateľom posúdiť kvalitu a efektívnosť ich promptov a tokov.

Komplexné zdroje: Azure Machine Learning prompt flow obsahuje knižnicu vstavaných nástrojov, príkladov a šablón, ktoré slúžia ako východiskový bod pre vývoj, inšpirujú kreativitu a zrýchľujú proces.

**Podniková pripravenosť pre aplikácie založené na LLM**

Spolupráca: Azure Machine Learning prompt flow podporuje tímovú spoluprácu, umožňuje viacerým používateľom pracovať spoločne na projektoch prompt inžinierstva, zdieľať vedomosti a udržiavať verziovanie.

Všetko v jednom: Azure Machine Learning prompt flow zjednodušuje celý proces prompt inžinierstva od vývoja a hodnotenia až po nasadenie a monitorovanie. Používatelia môžu jednoducho nasadiť svoje toky ako Azure Machine Learning endpointy a sledovať ich výkon v reálnom čase, čím zabezpečujú optimálnu prevádzku a neustále zlepšovanie.

Enterprise Readiness riešenia Azure Machine Learning: Prompt flow využíva robustné podnikové riešenia Azure Machine Learning, ktoré poskytujú bezpečný, škálovateľný a spoľahlivý základ pre vývoj, experimentovanie a nasadenie tokov.

S Azure Machine Learning prompt flow môžu používatelia uvoľniť svoju agilitu v prompt inžinierstve, efektívne spolupracovať a využiť podnikové riešenia pre úspešný vývoj a nasadenie aplikácií založených na LLM.

Kombináciou výpočtovej sily, dát a rôznych komponentov Azure ML môžu podnikový vývojári jednoducho vytvárať vlastné aplikácie umelej inteligencie.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.