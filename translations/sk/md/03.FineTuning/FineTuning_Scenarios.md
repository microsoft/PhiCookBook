## Scenáre doladenia

![Doladenie s MS službami](../../../../translated_images/sk/FinetuningwithMS.3d0cec8ae693e094.webp)

Táto časť poskytuje prehľad scenárov doladenia v prostrediach Microsoft Foundry a Azure, vrátane modelov nasadenia, vrstiev infraštruktúry a bežne používaných optimalizačných techník.

**Platforma**  
Toto zahŕňa spravované služby ako Microsoft Foundry (predtým Microsoft Foundry) a Azure Machine Learning, ktoré poskytujú správu modelov, orchestráciu, sledovanie experimentov a pracovné postupy nasadenia.

**Infraštruktúra**  
Doladenie vyžaduje škálovateľné výpočtové zdroje. V prostrediach Azure to zvyčajne zahŕňa GPU založené virtuálne stroje a CPU zdroje pre ľahké pracovné záťaže spolu so škálovateľným úložiskom pre dátové súbory a kontrolné body.

**Nástroje a rámce**  
Pracovné postupy doladenia bežne spoliehajú na rámce a knižnice optimalizácie ako Hugging Face Transformers, DeepSpeed a PEFT (Parameter-Efficient Fine-Tuning).

Proces doladenia s technológiami Microsoft zahŕňa platformové služby, výpočtovú infraštruktúru a tréningové rámce. Pochopením, ako tieto komponenty spolupracujú, môžu vývojári efektívne prispôsobiť základné modely špecifickým úlohám a produkčným scenárom.

## Model ako služba

Doladte model pomocou hostovaného doladenia bez potreby vytvárať a spravovať výpočtové zdroje.

![MaaS Doladenie](../../../../translated_images/sk/MaaSfinetune.3eee4630607aff0d.webp)

Serverless doladenie je momentálne dostupné pre modelové rodiny Phi-3, Phi-3.5 a Phi-4, čo umožňuje vývojárom rýchlo a jednoducho prispôsobiť modely pre cloudové a edge scenáre bez starostí o zabezpečenie výpočtovej kapacity.

## Model ako platforma

Používatelia spravujú vlastné výpočtové zdroje, aby mohli doladiť svoje modely.

![Maap Doladenie](../../../../translated_images/sk/MaaPFinetune.fd3829c1122f5d1c.webp)

[Príklad doladenia](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Porovnanie techník doladenia

|Scenár|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Prispôsobenie predtrénovaných LLM špecifickým úlohám alebo doménam|Áno|Áno|Áno|Áno|Áno|Áno|
|Doladenie pre NLP úlohy ako klasifikácia textu, rozpoznávanie pomenovaných entít a strojový preklad|Áno|Áno|Áno|Áno|Áno|Áno|
|Doladenie pre úlohy QA|Áno|Áno|Áno|Áno|Áno|Áno|
|Doladenie na generovanie ľudsky znejúcich odpovedí v chatbotov|Áno|Áno|Áno|Áno|Áno|Áno|
|Doladenie na generovanie hudby, umenia alebo iných foriem kreativity|Áno|Áno|Áno|Áno|Áno|Áno|
|Znižovanie výpočtových a finančných nákladov|Áno|Áno|Áno|Áno|Áno|Áno|
|Znižovanie použitia pamäte|Áno|Áno|Áno|Áno|Áno|Áno|
|Použitie menšieho počtu parametrov pre efektívne doladenie|Áno|Áno|Áno|Nie|Nie|Áno|
|Pamäťovo efektívna forma dátovej paralelizácie, ktorá umožňuje prístup k celkovej GPU pamäti všetkých dostupných GPU zariadení|Nie|Nie|Nie|Áno|Áno|Nie|

> [!NOTE]
> LoRA, QLoRA, PEFT a DoRA sú metódy parametricky efektívneho doladenia, zatiaľ čo DeepSpeed a ZeRO sa zameriavajú na distribuované trénovanie a optimalizáciu pamäte.

## Príklady výkonu doladenia

![Výkon doladenia](../../../../translated_images/sk/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->