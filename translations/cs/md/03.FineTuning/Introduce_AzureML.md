<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7fe541373802e33568e94e13226d463c",
  "translation_date": "2025-07-17T09:47:17+00:00",
  "source_file": "md/03.FineTuning/Introduce_AzureML.md",
  "language_code": "cs"
}
-->
# **Představení služby Azure Machine Learning**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo) je cloudová služba pro urychlení a správu životního cyklu projektů strojového učení (ML).

Odborníci na ML, datoví vědci a inženýři ji mohou využívat ve svých každodenních pracovních postupech k:

- Trénování a nasazení modelů.
- Správě operací strojového učení (MLOps).
- Můžete vytvořit model v Azure Machine Learning nebo použít model vytvořený na open-source platformě, jako jsou PyTorch, TensorFlow nebo scikit-learn.
- Nástroje MLOps vám pomáhají sledovat, znovu trénovat a znovu nasazovat modely.

## Pro koho je Azure Machine Learning určeno?

**Datoví vědci a ML inženýři**

Mohou využívat nástroje k urychlení a automatizaci svých každodenních pracovních postupů.  
Azure ML nabízí funkce pro spravedlnost, vysvětlitelnost, sledování a auditovatelnost.

**Vývojáři aplikací**  
Mohou bezproblémově integrovat modely do aplikací nebo služeb.

**Vývojáři platformy**

Mají přístup k robustní sadě nástrojů podporovaných spolehlivými Azure Resource Manager API.  
Tyto nástroje umožňují vytvářet pokročilé ML nástroje.

**Podniky**

Pracující v cloudu Microsoft Azure těží z dobře známé bezpečnosti a řízení přístupu na základě rolí.  
Nastavte projekty pro kontrolu přístupu k chráněným datům a specifickým operacím.

## Produktivita pro celý tým  
Projekty ML často vyžadují tým s různorodými dovednostmi pro jejich tvorbu a údržbu.

Azure ML poskytuje nástroje, které vám umožní:  
- Spolupracovat s týmem prostřednictvím sdílených poznámkových bloků, výpočetních zdrojů, serverless výpočetních prostředí, dat a prostředí.  
- Vyvíjet modely se zaměřením na spravedlnost, vysvětlitelnost, sledování a auditovatelnost, aby splňovaly požadavky na sledovatelnost a audit.  
- Rychle a snadno nasazovat ML modely ve velkém měřítku a efektivně je spravovat a řídit pomocí MLOps.  
- Spouštět úlohy strojového učení kdekoli s vestavěnou správou, bezpečností a dodržováním předpisů.

## Nástroje platformy kompatibilní napříč prostředími

Kdokoli v ML týmu může používat své oblíbené nástroje k dokončení práce.  
Ať už provádíte rychlé experimenty, ladění hyperparametrů, vytváření pipeline nebo správu inferencí, můžete využít známá rozhraní, včetně:  
- Azure Machine Learning Studio  
- Python SDK (v2)  
- Azure CLI (v2)  
- Azure Resource Manager REST API

Během ladění modelů a spolupráce v průběhu vývojového cyklu můžete sdílet a vyhledávat zdroje, aktiva a metriky přímo v uživatelském rozhraní Azure Machine Learning studia.

## **LLM/SLM v Azure ML**

Azure ML přidalo mnoho funkcí souvisejících s LLM/SLM, které kombinují LLMOps a SLMOps a vytvářejí tak podnikovou platformu pro generativní umělou inteligenci.

### **Katalog modelů**

Podnikové uživatele mohou nasazovat různé modely podle různých obchodních scénářů prostřednictvím Katalogu modelů a poskytovat služby jako Model jako služba (Model as Service) pro přístup podnikových vývojářů nebo uživatelů.

![models](../../../../translated_images/models.e6c7ff50a51806fd0bfd398477e3db3d5c3dc545cd7308344e448e0b8d8295a1.cs.png)

Katalog modelů v Azure Machine Learning studiu je centrem pro objevování a využívání široké škály modelů, které umožňují vytvářet aplikace generativní AI. Katalog obsahuje stovky modelů od poskytovatelů jako Azure OpenAI service, Mistral, Meta, Cohere, Nvidia, Hugging Face, včetně modelů trénovaných Microsoftem. Modely od jiných než Microsoft poskytovatelů jsou označovány jako Non-Microsoft Products podle podmínek Microsoft Product Terms a podléhají podmínkám přiloženým k modelu.

### **Job Pipeline**

Jádrem pipeline strojového učení je rozdělení kompletního úkolu strojového učení do vícestupňového pracovního postupu. Každý krok je zvládnutelná komponenta, kterou lze samostatně vyvíjet, optimalizovat, konfigurovat a automatizovat. Kroky jsou propojeny přes dobře definovaná rozhraní. Služba pipeline Azure Machine Learning automaticky koordinuje všechny závislosti mezi kroky pipeline.

Při doladění SLM / LLM můžeme spravovat data, trénink a generování prostřednictvím Pipeline.

![finetuning](../../../../translated_images/finetuning.6559da198851fa523d94d6f0b9f271fa6e1bbac13db0024ebda43cb5348a4633.cs.png)

### **Prompt flow**

Výhody používání Azure Machine Learning prompt flow  
Azure Machine Learning prompt flow nabízí řadu výhod, které pomáhají uživatelům přejít od nápadu k experimentování a nakonec k produkčně připraveným aplikacím založeným na LLM:

**Agilita prompt engineeringu**

Interaktivní prostředí pro tvorbu: Azure Machine Learning prompt flow poskytuje vizuální zobrazení struktury toku, které uživatelům umožňuje snadno pochopit a orientovat se ve svých projektech. Nabízí také prostředí podobné poznámkovému bloku pro efektivní vývoj a ladění toku.  
Varianty pro ladění promptů: Uživatelé mohou vytvářet a porovnávat více variant promptů, což usnadňuje iterativní proces zdokonalování.

Hodnocení: Vestavěné hodnotící toky umožňují uživatelům posoudit kvalitu a efektivitu jejich promptů a toků.

Komplexní zdroje: Azure Machine Learning prompt flow obsahuje knihovnu vestavěných nástrojů, ukázek a šablon, které slouží jako výchozí bod pro vývoj, inspirují kreativitu a urychlují proces.

**Podniková připravenost pro aplikace založené na LLM**

Spolupráce: Azure Machine Learning prompt flow podporuje týmovou spolupráci, umožňuje více uživatelům pracovat společně na projektech prompt engineeringu, sdílet znalosti a udržovat správu verzí.

Vše v jednom: Azure Machine Learning prompt flow zjednodušuje celý proces prompt engineeringu od vývoje a hodnocení až po nasazení a monitorování. Uživatelé mohou snadno nasadit své toky jako Azure Machine Learning endpointy a sledovat jejich výkon v reálném čase, což zajišťuje optimální provoz a kontinuální zlepšování.

Řešení Azure Machine Learning pro podnikovou připravenost: Prompt flow využívá robustní podniková řešení Azure Machine Learning, která poskytují bezpečný, škálovatelný a spolehlivý základ pro vývoj, experimentování a nasazení toků.

S Azure Machine Learning prompt flow mohou uživatelé uvolnit svou agilitu v prompt engineeringu, efektivně spolupracovat a využívat podniková řešení pro úspěšný vývoj a nasazení aplikací založených na LLM.

Kombinací výpočetního výkonu, dat a různých komponent Azure ML mohou podnikoví vývojáři snadno vytvářet vlastní aplikace umělé inteligence.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.