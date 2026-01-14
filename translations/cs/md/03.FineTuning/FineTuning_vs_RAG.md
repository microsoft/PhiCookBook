<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e010400c2918557b36bb932a14004c",
  "translation_date": "2025-07-17T09:31:12+00:00",
  "source_file": "md/03.FineTuning/FineTuning_vs_RAG.md",
  "language_code": "cs"
}
-->
## Doladění vs RAG

## Retrieval Augmented Generation

RAG je kombinace vyhledávání dat a generování textu. Strukturovaná i nestrukturovaná data firmy jsou uložena ve vektorové databázi. Při hledání relevantního obsahu se najde souhrn a obsah, které tvoří kontext, a ten se spojí s textovou generací LLM/SLM pro vytvoření výsledného textu.

## Proces RAG
![FinetuningvsRAG](../../../../translated_images/cs/rag.2014adc59e6f6007.png)

## Doladění
Doladění vychází ze zlepšení konkrétního modelu. Není potřeba začínat od algoritmu modelu, ale je nutné průběžně sbírat data. Pokud chcete přesnější terminologii a jazykové vyjádření v průmyslových aplikacích, doladění je lepší volba. Pokud se ale vaše data často mění, doladění může být složité.

## Jak vybrat
Pokud naše odpověď vyžaduje zapojení externích dat, RAG je nejlepší volba.

Pokud potřebujete stabilní a přesné průmyslové znalosti, doladění bude vhodnější. RAG upřednostňuje vytažení relevantního obsahu, ale nemusí vždy zachytit specializované nuance.

Doladění vyžaduje kvalitní datovou sadu, a pokud jde jen o malý rozsah dat, nebude mít velký efekt. RAG je flexibilnější.  
Doladění je černá skříňka, něco jako metafyzika, a je těžké pochopit jeho vnitřní mechanismus. RAG naopak usnadňuje dohledání zdroje dat, což pomáhá efektivně korigovat halucinace nebo chyby v obsahu a zajišťuje lepší průhlednost.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.