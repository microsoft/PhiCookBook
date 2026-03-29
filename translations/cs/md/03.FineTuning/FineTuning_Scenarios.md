## Scénáře ladění modelů (Fine Tuning)

![FineTuning with MS Services](../../../../translated_images/cs/FinetuningwithMS.3d0cec8ae693e094.webp)

Tato sekce poskytuje přehled scénářů ladění modelů v prostředí Microsoft Foundry a Azure, včetně modelů nasazení, vrstev infrastruktury a běžně používaných optimalizačních technik.

**Platforma**  
To zahrnuje spravované služby, jako jsou Microsoft Foundry (dříve Microsoft Foundry) a Azure Machine Learning, které poskytují správu modelů, orchestraci, sledování experimentů a pracovní postupy nasazení.

**Infrastruktura**  
Ladění modelu vyžaduje škálovatelné výpočetní zdroje. V prostředí Azure obvykle zahrnuje virtuální stroje založené na GPU a CPU zdroje pro lehké zátěže spolu se škálovatelným úložištěm pro datové sady a kontrolní body.

**Nástroje a rámce**  
Pracovní postupy ladění modelů běžně spoléhají na rámce a optimalizační knihovny, jako jsou Hugging Face Transformers, DeepSpeed a PEFT (Parameter-Efficient Fine-Tuning).

Proces ladění modelů s technologiemi Microsoft zahrnuje platformní služby, výpočetní infrastrukturu a školicí rámce. Pochopením, jak tyto komponenty spolupracují, mohou vývojáři efektivně přizpůsobit základní modely konkrétním úkolům a produkčním scénářům.

## Model jako služba

Ladění modelu pomocí hostovaného ladění bez nutnosti vytvářet a spravovat výpočetní prostředky.

![MaaS Fine Tuning](../../../../translated_images/cs/MaaSfinetune.3eee4630607aff0d.webp)

Serverless ladění je nyní dostupné pro rodiny modelů Phi-3, Phi-3.5 a Phi-4, což umožňuje vývojářům rychle a snadno přizpůsobit modely pro cloudové a edge scénáře bez nutnosti zajišťovat výpočetní výkon.

## Model jako platforma

Uživatelé spravují vlastní výpočetní prostředky za účelem ladění svých modelů.

![Maap Fine Tuning](../../../../translated_images/cs/MaaPFinetune.fd3829c1122f5d1c.webp)

[Ukázka ladění](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Porovnání technik ladění modelů

|Scénář|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Přizpůsobení předtrénovaných LLM konkrétním úkolům nebo oblastem|Ano|Ano|Ano|Ano|Ano|Ano|
|Ladění pro NLP úlohy, jako je klasifikace textu, rozpoznávání pojmenovaných entit a strojový překlad|Ano|Ano|Ano|Ano|Ano|Ano|
|Ladění pro úlohy QA|Ano|Ano|Ano|Ano|Ano|Ano|
|Ladění pro generování lidsky znějících odpovědí v chatbotech|Ano|Ano|Ano|Ano|Ano|Ano|
|Ladění pro generování hudby, umění nebo jiných forem kreativity|Ano|Ano|Ano|Ano|Ano|Ano|
|Snižování výpočetních a finančních nákladů|Ano|Ano|Ano|Ano|Ano|Ano|
|Snižování využití paměti|Ano|Ano|Ano|Ano|Ano|Ano|
|Používání menšího počtu parametrů pro efektivní ladění|Ano|Ano|Ano|Ne|Ne|Ano|
|Paměťově efektivní forma datové paralelizace, která umožňuje přístup ke kombinované GPU paměti všech dostupných GPU zařízení|Ne|Ne|Ne|Ano|Ano|Ne|

> [!NOTE]
> LoRA, QLoRA, PEFT a DoRA jsou metody efektivního ladění pomocí parametrů, zatímco DeepSpeed a ZeRO se zaměřují na distribuované školení a optimalizaci paměti.

## Příklady výkonu ladění modelů

![Finetuning Performance](../../../../translated_images/cs/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, berte prosím na vědomí, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo chybné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->