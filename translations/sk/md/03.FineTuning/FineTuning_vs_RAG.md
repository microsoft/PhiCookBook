<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e010400c2918557b36bb932a14004c",
  "translation_date": "2025-07-17T09:31:21+00:00",
  "source_file": "md/03.FineTuning/FineTuning_vs_RAG.md",
  "language_code": "sk"
}
-->
## Doladenie vs RAG

## Retrieval Augmented Generation

RAG je kombinácia vyhľadávania dát a generovania textu. Štruktúrované aj neštruktúrované dáta v podniku sú uložené vo vektorovej databáze. Pri hľadaní relevantného obsahu sa nájde zodpovedajúce zhrnutie a obsah, ktoré tvoria kontext, a schopnosť dopĺňania textu modelom LLM/SLM sa využije na generovanie výsledného textu.

## Proces RAG
![FinetuningvsRAG](../../../../translated_images/sk/rag.2014adc59e6f6007.png)

## Doladenie
Doladenie je založené na zlepšení konkrétneho modelu. Nie je potrebné začínať od algoritmu modelu, ale je potrebné neustále zhromažďovať dáta. Ak chcete presnejšiu terminológiu a jazykové vyjadrenie v priemyselných aplikáciách, doladenie je lepšia voľba. Ak sa však vaše dáta často menia, doladenie môže byť komplikované.

## Ako si vybrať
Ak naša odpoveď vyžaduje zapojenie externých dát, RAG je najlepšia voľba.

Ak potrebujete stabilné a presné priemyselné znalosti, doladenie bude dobrá voľba. RAG uprednostňuje vyhľadávanie relevantného obsahu, ale nemusí vždy dokonale zachytiť špecializované nuansy.

Doladenie vyžaduje kvalitný dátový súbor, a ak ide len o malý rozsah dát, nebude mať veľký efekt. RAG je flexibilnejší.  
Doladenie je čierna skrinka, metafyzika, a je ťažké pochopiť jeho vnútorný mechanizmus. RAG však umožňuje ľahšie nájsť zdroj dát, čím efektívne upravuje halucinácie alebo chyby v obsahu a poskytuje lepšiu transparentnosť.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.