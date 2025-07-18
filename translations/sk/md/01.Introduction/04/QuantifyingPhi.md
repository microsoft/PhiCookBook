<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-07-16T21:50:03+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "sk"
}
-->
# **Kvantifikácia rodiny Phi**

Kvantifikácia modelu označuje proces mapovania parametrov (ako sú váhy a aktivačné hodnoty) v neurónovej sieti z veľkého rozsahu hodnôt (zvyčajne spojitého) na menší konečný rozsah hodnôt. Táto technológia dokáže zmenšiť veľkosť a výpočtovú náročnosť modelu a zlepšiť jeho prevádzkovú efektivitu v prostrediach s obmedzenými zdrojmi, ako sú mobilné zariadenia alebo zabudované systémy. Kvantifikácia modelu dosahuje kompresiu znížením presnosti parametrov, čo však prináša určitú stratu presnosti. Preto je pri kvantifikácii potrebné nájsť rovnováhu medzi veľkosťou modelu, výpočtovou náročnosťou a presnosťou. Bežné metódy kvantifikácie zahŕňajú kvantifikáciu na pevný bod, kvantifikáciu s pohyblivou rádovou čiarkou a podobne. Výber vhodnej kvantifikačnej stratégie závisí od konkrétneho scenára a potrieb.

Chceme nasadiť GenAI modely na edge zariadenia a umožniť tak viac zariadeniam vstúpiť do GenAI scenárov, ako sú mobilné zariadenia, AI PC/Copilot+PC a tradičné IoT zariadenia. Vďaka kvantifikovanému modelu ich môžeme nasadiť na rôzne edge zariadenia podľa ich špecifík. V kombinácii s frameworkom na zrýchlenie modelov a kvantifikovanými modelmi poskytovanými výrobcami hardvéru môžeme vytvoriť lepšie aplikačné scenáre SLM.

V kvantifikačnom prostredí používame rôzne presnosti (INT4, INT8, FP16, FP32). Nižšie nájdete vysvetlenie najčastejšie používaných kvantifikačných presností.

### **INT4**

Kvantifikácia INT4 je radikálna metóda, ktorá kvantifikuje váhy a aktivačné hodnoty modelu na 4-bitové celé čísla. INT4 kvantifikácia zvyčajne vedie k väčšej strate presnosti kvôli menšiemu rozsahu reprezentácie a nižšej presnosti. Na druhej strane, v porovnaní s INT8 kvantifikáciou dokáže INT4 ešte viac znížiť požiadavky na ukladací priestor a výpočtovú náročnosť modelu. Treba však poznamenať, že INT4 kvantifikácia je v praxi pomerne zriedkavá, pretože príliš nízka presnosť môže výrazne zhoršiť výkon modelu. Okrem toho nie všetok hardvér podporuje INT4 operácie, takže pri výbere kvantifikačnej metódy je potrebné zvážiť kompatibilitu hardvéru.

### **INT8**

Kvantifikácia INT8 znamená prevod váh a aktivačných hodnôt modelu z čísel s pohyblivou rádovou čiarkou na 8-bitové celé čísla. Hoci číselný rozsah reprezentovaný INT8 je menší a menej presný, výrazne znižuje požiadavky na ukladanie a výpočty. Pri INT8 kvantifikácii prechádzajú váhy a aktivačné hodnoty procesu kvantifikácie, ktorý zahŕňa škálovanie a posun, aby sa čo najviac zachovali pôvodné informácie z čísel s pohyblivou rádovou čiarkou. Počas inferencie sa tieto kvantifikované hodnoty dekvantifikujú späť na čísla s pohyblivou rádovou čiarkou pre výpočty a následne opäť kvantifikujú na INT8 pre ďalší krok. Táto metóda poskytuje dostatočnú presnosť vo väčšine aplikácií pri zachovaní vysokej výpočtovej efektivity.

### **FP16**

Formát FP16, teda 16-bitové čísla s pohyblivou rádovou čiarkou (float16), znižuje pamäťovú náročnosť na polovicu v porovnaní s 32-bitovými číslami (float32), čo je veľkou výhodou pri rozsiahlych hlbokých učiacich sa aplikáciách. Formát FP16 umožňuje načítať väčšie modely alebo spracovať viac dát v rámci rovnakých limitov GPU pamäte. Keďže moderný GPU hardvér stále viac podporuje FP16 operácie, použitie FP16 formátu môže priniesť aj zrýchlenie výpočtov. Na druhej strane, FP16 formát má svoje nevýhody, najmä nižšiu presnosť, ktorá môže v niektorých prípadoch viesť k numerickej nestabilite alebo strate presnosti.

### **FP32**

Formát FP32 poskytuje vyššiu presnosť a dokáže presne reprezentovať široký rozsah hodnôt. V situáciách, kde sa vykonávajú zložité matematické operácie alebo je potrebný vysokopresný výsledok, je preferovaný formát FP32. Vyššia presnosť však znamená aj väčšiu spotrebu pamäte a dlhší čas výpočtu. Pri rozsiahlych hlbokých modeloch, najmä ak obsahujú veľa parametrov a obrovské množstvo dát, môže FP32 formát spôsobiť nedostatok GPU pamäte alebo zníženie rýchlosti inferencie.

Na mobilných zariadeniach alebo IoT zariadeniach môžeme konvertovať Phi-3.x modely na INT4, zatiaľ čo AI PC / Copilot PC môžu používať vyššie presnosti ako INT8, FP16 alebo FP32.

V súčasnosti rôzni výrobcovia hardvéru ponúkajú rôzne frameworky na podporu generatívnych modelov, ako sú Intel OpenVINO, Qualcomm QNN, Apple MLX a Nvidia CUDA, ktoré v kombinácii s kvantifikáciou modelov umožňujú lokálne nasadenie.

Z technologického hľadiska podporujeme po kvantifikácii rôzne formáty, ako PyTorch / Tensorflow, GGUF a ONNX. Vykonal som porovnanie formátov a aplikačných scenárov medzi GGUF a ONNX. Odporúčam ONNX kvantifikačný formát, ktorý má dobrú podporu od modelových frameworkov až po hardvér. V tejto kapitole sa zameriame na ONNX Runtime pre GenAI, OpenVINO a Apple MLX na vykonanie kvantifikácie modelov (ak máte lepší spôsob, môžete nám ho poslať cez PR).

**Táto kapitola obsahuje**

1. [Kvantifikácia Phi-3.5 / 4 pomocou llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantifikácia Phi-3.5 / 4 pomocou rozšírení Generative AI pre onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantifikácia Phi-3.5 / 4 pomocou Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantifikácia Phi-3.5 / 4 pomocou Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.