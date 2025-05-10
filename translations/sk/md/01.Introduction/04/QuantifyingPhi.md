<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-05-09T13:36:48+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "sk"
}
-->
# **Kvantifikácia rodiny Phi**

Kvantifikácia modelu znamená proces mapovania parametrov (ako sú váhy a aktivačné hodnoty) v neurónovej sieti z veľkého rozsahu hodnôt (zvyčajne spojitého) na menší konečný rozsah hodnôt. Táto technológia dokáže zmenšiť veľkosť a výpočtovú náročnosť modelu a zároveň zlepšiť jeho efektivitu pri prevádzke v prostrediach s obmedzenými zdrojmi, ako sú mobilné zariadenia alebo zabudované systémy. Kvantifikácia modelu dosahuje kompresiu znížením presnosti parametrov, čo však prináša určitú stratu presnosti. Preto je pri kvantifikácii potrebné vyvážiť veľkosť modelu, výpočtovú náročnosť a presnosť. Bežné metódy kvantifikácie zahŕňajú kvantifikáciu na fixný počet bitov, kvantifikáciu s pohyblivou desatinnou čiarkou a podobne. Výber vhodnej kvantifikačnej stratégie závisí od konkrétneho scenára a potrieb.

Naším cieľom je nasadiť model GenAI na edge zariadenia a umožniť tak väčšiemu počtu zariadení vstup do GenAI scenárov, ako sú mobilné zariadenia, AI PC/Copilot+PC a tradičné IoT zariadenia. Vďaka kvantifikovanému modelu môžeme nasadiť model na rôzne edge zariadenia podľa ich špecifík. V kombinácii s frameworkom na zrýchlenie modelov a kvantifikovaným modelom poskytnutým výrobcami hardvéru môžeme vytvoriť lepšie aplikačné scenáre SLM.

V kvantifikačnom scenári rozlišujeme rôzne presnosti (INT4, INT8, FP16, FP32). Nižšie nájdete vysvetlenie najpoužívanejších kvantifikačných presností.

### **INT4**

Kvantifikácia INT4 je radikálna metóda, ktorá kvantifikuje váhy a aktivačné hodnoty modelu na 4-bitové celé čísla. INT4 kvantifikácia zvyčajne vedie k väčšej strate presnosti kvôli menšiemu rozsahu reprezentácie a nižšej presnosti. Napriek tomu v porovnaní s INT8 kvantifikáciou dokáže ďalej znížiť požiadavky na úložisko a výpočtovú náročnosť modelu. Treba však poznamenať, že INT4 kvantifikácia je v praxi pomerne zriedkavá, pretože príliš nízka presnosť môže výrazne zhoršiť výkon modelu. Okrem toho nie všetok hardvér podporuje operácie INT4, takže pri výbere kvantifikačnej metódy treba zvážiť kompatibilitu hardvéru.

### **INT8**

Kvantifikácia INT8 je proces prevodu váh a aktivačných hodnôt modelu z čísel s pohyblivou desatinnou čiarkou na 8-bitové celé čísla. Hoci je číselný rozsah INT8 menší a menej presný, výrazne znižuje požiadavky na ukladanie a výpočty. Pri INT8 kvantifikácii prechádzajú váhy a aktivačné hodnoty procesu kvantifikácie, ktorý zahŕňa škálovanie a posun, aby sa čo najviac zachovala pôvodná informácia z čísel s pohyblivou čiarkou. Počas inferencie sa tieto kvantifikované hodnoty dekvantifikujú späť na čísla s pohyblivou čiarkou pre výpočty a následne opäť kvantifikujú na INT8 pre ďalší krok. Táto metóda poskytuje dostatočnú presnosť vo väčšine aplikácií pri zachovaní vysokej výpočtovej efektivity.

### **FP16**

Formát FP16, teda 16-bitové čísla s pohyblivou desatinnou čiarkou (float16), znižuje pamäťovú náročnosť na polovicu v porovnaní so 32-bitovými číslami (float32), čo má významné výhody pri veľkých hlbokých modeloch. Formát FP16 umožňuje načítať väčšie modely alebo spracovať viac dát v rámci rovnakých pamäťových limitov GPU. Moderný GPU hardvér stále viac podporuje FP16 operácie, čo môže priniesť aj zlepšenie rýchlosti výpočtov. Na druhej strane FP16 formát má svoje nevýhody, najmä nižšiu presnosť, ktorá môže viesť k numerickej nestabilite alebo strate presnosti v niektorých prípadoch.

### **FP32**

Formát FP32 poskytuje vyššiu presnosť a dokáže presne reprezentovať široký rozsah hodnôt. V scenároch, kde sa vykonávajú zložité matematické operácie alebo je potrebný vysokopresný výsledok, je preferovaný formát FP32. Vyššia presnosť však znamená aj väčšiu pamäťovú náročnosť a dlhší čas výpočtu. Pri veľkých hlbokých modeloch, najmä s množstvom parametrov a veľkým objemom dát, môže FP32 formát spôsobiť nedostatok pamäte GPU alebo spomalenie inferencie.

Na mobilných alebo IoT zariadeniach môžeme konvertovať Phi-3.x modely na INT4, zatiaľ čo AI PC / Copilot PC môžu používať vyššie presnosti ako INT8, FP16, FP32.

V súčasnosti rôzni výrobcovia hardvéru ponúkajú rôzne frameworky na podporu generatívnych modelov, napríklad Intel OpenVINO, Qualcomm QNN, Apple MLX a Nvidia CUDA, ktoré v kombinácii s kvantifikáciou modelu umožňujú lokálne nasadenie.

Z technologického hľadiska máme po kvantifikácii podporu rôznych formátov, ako sú PyTorch / Tensorflow formáty, GGUF a ONNX. Vykonal som porovnanie formátov a aplikačných scenárov medzi GGUF a ONNX. Odporúčam ONNX kvantifikačný formát, ktorý má dobrú podporu od modelového frameworku až po hardvér. V tejto kapitole sa zameriame na ONNX Runtime pre GenAI, OpenVINO a Apple MLX na vykonanie kvantifikácie modelu (ak máte lepší spôsob, môžete nám ho poslať cez PR).

**Táto kapitola obsahuje**

1. [Quantizing Phi-3.5 / 4 using llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizing Phi-3.5 / 4 using Generative AI extensions for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizing Phi-3.5 / 4 using Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizing Phi-3.5 / 4 using Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, vezmite prosím na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.