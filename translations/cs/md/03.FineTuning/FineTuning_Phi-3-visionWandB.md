# Phi-3-Vision-128K-Instruct Přehled projektu

## Model

Phi-3-Vision-128K-Instruct, lehký a špičkový multimodální model, je jádrem tohoto projektu. Patří do rodiny modelů Phi-3 a podporuje délku kontextu až 128 000 tokenů. Model byl trénován na různorodé sadě dat, která zahrnuje syntetická data a pečlivě filtrované veřejně dostupné webové stránky, s důrazem na vysoce kvalitní obsah vyžadující logické uvažování. Tréninkový proces zahrnoval řízené doladění a přímou optimalizaci preferencí, aby bylo zajištěno přesné dodržování instrukcí, stejně jako robustní bezpečnostní opatření.

## Vytváření vzorových dat je důležité z několika důvodů:

1. **Testování**: Vzorová data umožňují testovat vaši aplikaci v různých scénářích, aniž by došlo k ovlivnění skutečných dat. To je zvláště důležité ve fázi vývoje a testování.

2. **Ladění výkonu**: Díky vzorovým datům, která napodobují rozsah a složitost reálných dat, můžete identifikovat úzká místa ve výkonu a optimalizovat aplikaci.

3. **Prototypování**: Vzorová data lze použít k tvorbě prototypů a maket, které pomáhají lépe pochopit požadavky uživatelů a získat zpětnou vazbu.

4. **Analýza dat**: V datové vědě se vzorová data často používají pro průzkumnou analýzu, trénink modelů a testování algoritmů.

5. **Bezpečnost**: Používání vzorových dat ve vývojových a testovacích prostředích pomáhá zabránit nechtěnému úniku citlivých reálných dat.

6. **Učení**: Pokud se učíte novou technologii nebo nástroj, práce se vzorovými daty vám poskytne praktickou možnost aplikovat získané znalosti.

Pamatujte, že kvalita vašich vzorových dat může výrazně ovlivnit tyto aktivity. Měla by být co nejblíže reálným datům z hlediska struktury a variability.

### Vytváření vzorových dat
[Generate DataSet Script](./CreatingSampleData.md)

## Dataset

Dobrou ukázkou vzorové datové sady je [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (dostupná na Huggingface).  
Vzorová datová sada produktů Burberry spolu s metadaty o kategorii produktů, ceně a názvu obsahuje celkem 3 040 řádků, z nichž každý představuje jedinečný produkt. Tato datová sada nám umožňuje testovat schopnost modelu porozumět a interpretovat vizuální data a generovat popisný text, který zachycuje složité vizuální detaily a charakteristické znaky značky.

**Note:** Můžete použít jakoukoli datovou sadu, která obsahuje obrázky.

## Složitá dedukce

Model musí odvozovat ceny a názvy pouze na základě obrázku. To vyžaduje, aby model nejen rozpoznal vizuální prvky, ale také pochopil jejich význam z hlediska hodnoty produktu a značky. Tím, že model dokáže přesně syntetizovat textové popisy z obrázků, projekt ukazuje potenciál integrace vizuálních dat pro zlepšení výkonu a všestrannosti modelů v reálných aplikacích.

## Architektura Phi-3 Vision

Architektura modelu je multimodální verze Phi-3. Zpracovává jak textová, tak obrazová data a integruje tyto vstupy do jednotné sekvence pro komplexní porozumění a generování. Model používá samostatné vrstvy embeddingu pro text a obrázky. Textové tokeny jsou převedeny na husté vektory, zatímco obrázky jsou zpracovány pomocí CLIP vision modelu pro extrakci rysových embeddingů. Tyto obrazové embeddingy jsou následně projekčně upraveny tak, aby odpovídaly rozměrům textových embeddingů, což zajišťuje jejich bezproblémovou integraci.

## Integrace textových a obrazových embeddingů

Speciální tokeny v textové sekvenci označují místa, kde mají být vloženy obrazové embeddingy. Během zpracování jsou tyto speciální tokeny nahrazeny odpovídajícími obrazovými embeddingy, což umožňuje modelu pracovat s textem i obrázky jako s jednou sekvencí. Prompt pro naši datovou sadu je formátován pomocí speciálního tokenu <|image|> následovně:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Ukázkový kód
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.