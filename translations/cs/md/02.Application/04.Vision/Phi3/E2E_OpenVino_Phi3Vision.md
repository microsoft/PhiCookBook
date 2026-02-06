Tato ukázka demonstruje, jak použít předtrénovaný model k vygenerování Python kódu na základě obrázku a textového zadání.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Zde je krok za krokem vysvětlení:

1. **Importy a nastavení**:
   - Načtou se potřebné knihovny a moduly, včetně `requests`, `PIL` pro zpracování obrázků a `transformers` pro práci s modelem a zpracování.

2. **Načtení a zobrazení obrázku**:
   - Obrázek (`demo.png`) je otevřen pomocí knihovny `PIL` a zobrazen.

3. **Definování zadání**:
   - Vytvoří se zpráva, která obsahuje obrázek a požadavek na vygenerování Python kódu pro zpracování obrázku a jeho uložení pomocí `plt` (matplotlib).

4. **Načtení procesoru**:
   - `AutoProcessor` je načten z předtrénovaného modelu určeného adresářem `out_dir`. Tento procesor zpracuje textové i obrazové vstupy.

5. **Vytvoření promptu**:
   - Metoda `apply_chat_template` se použije k formátování zprávy do promptu vhodného pro model.

6. **Zpracování vstupů**:
   - Prompt a obrázek jsou převedeny na tensory, které model dokáže zpracovat.

7. **Nastavení parametrů generování**:
   - Definují se parametry pro generování modelu, včetně maximálního počtu nových tokenů a zda se má výstup náhodně vzorkovat.

8. **Generování kódu**:
   - Model vygeneruje Python kód na základě vstupů a nastavených parametrů. `TextStreamer` se použije k zpracování výstupu, přičemž se přeskočí prompt a speciální tokeny.

9. **Výstup**:
   - Vygenerovaný kód je vytištěn, měl by obsahovat Python kód pro zpracování obrázku a jeho uložení podle zadání.

Tato ukázka ukazuje, jak využít předtrénovaný model s OpenVino k dynamickému generování kódu na základě uživatelského vstupu a obrázků.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.