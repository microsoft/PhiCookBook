<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e010400c2918557b36bb932a14004c",
  "translation_date": "2025-05-09T22:17:11+00:00",
  "source_file": "md/03.FineTuning/FineTuning_vs_RAG.md",
  "language_code": "sk"
}
-->
## Doladenie vs RAG

## Retrieval Augmented Generation

RAG je kombinácia vyhľadávania dát a generovania textu. Štruktúrované aj neštruktúrované dáta v podniku sú uložené vo vektorovej databáze. Pri hľadaní relevantného obsahu sa nájde zodpovedajúce zhrnutie a obsah, ktoré tvoria kontext, a potom sa spojí schopnosť dokončenia textu modelom LLM/SLM na generovanie výsledného obsahu.

## Proces RAG
![FinetuningvsRAG](../../../../translated_images/rag.36e7cb856f120334d577fde60c6a5d7c5eecae255dac387669303d30b4b3efa4.sk.png)

## Doladenie
Doladenie je založené na zlepšení konkrétneho modelu. Nemusí sa začínať od algoritmu modelu, ale je potrebné neustále zbierať dáta. Ak potrebujete presnejšiu terminológiu a jazykový prejav v priemyselných aplikáciách, doladenie je lepšia voľba. Ak sa však vaše dáta často menia, doladenie môže byť komplikované.

## Ako vybrať
Ak naša odpoveď vyžaduje zapojenie externých dát, RAG je najlepšia voľba.

Ak potrebujete stabilný a presný výstup odborných znalostí, doladenie bude vhodnejšie. RAG uprednostňuje vyťahovanie relevantného obsahu, ale nemusí vždy dokonale zachytiť špecializované nuansy.

Doladenie vyžaduje kvalitný dátový súbor a ak ide len o malý rozsah dát, veľký rozdiel to neurobí. RAG je flexibilnejšie.  
Doladenie je čierna skrinka, metafyzika, a je ťažké pochopiť jeho vnútorný mechanizmus. RAG však umožňuje jednoduchšie nájsť zdroj dát, čím efektívne koriguje halucinácie alebo chyby v obsahu a poskytuje lepšiu transparentnosť.

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.