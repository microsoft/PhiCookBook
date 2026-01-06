<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-05T09:48:51+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "sk"
}
-->
# **Kvantifikácia rodiny Phi**

Kvantifikácia modelu znamená proces mapovania parametrov (ako sú váhy a hodnoty aktivácie) v modeli neurónovej siete z veľkého rozsahu hodnôt (zvyčajne z kontinuálneho rozsahu hodnôt) do menšieho konečného rozsahu hodnôt. Táto technológia môže zmenšiť veľkosť a výpočtovú zložitosť modelu a zlepšiť prevádzkovú efektívnosť modelu v prostrediach s obmedzenými zdrojmi, ako sú mobilné zariadenia alebo zabudované systémy. Kvantifikácia modelu dosahuje kompresiu znížením presnosti parametrov, ale zároveň prináša určitú stratu presnosti. Preto je pri procese kvantifikácie potrebné vyvážiť veľkosť modelu, výpočtovú zložitosť a presnosť. Bežné kvantifikačné metódy zahŕňajú kvantifikáciu na pevný bod, kvantifikáciu v plávajúcej desatinnej čiarke atď. Podľa špecifického scenára a potrieb môžete zvoliť vhodnú kvantifikačnú stratégiu.

Dúfame, že nasadíme modely GenAI na okrajové zariadenia a umožníme viacerým zariadeniam vstúpiť do scénarov GenAI, ako sú mobilné zariadenia, AI PC/Copilot+PC a tradičné IoT zariadenia. Prostredníctvom kvantifikovaného modelu ho môžeme nasadiť na rôzne okrajové zariadenia podľa rôznych typov zariadení. V spojení s rámcami na zrýchlenie modelov a kvantifikovanými modelmi poskytovanými výrobcami hardvéru môžeme vytvoriť lepšie aplikačné scenáre SLM.

V kvantifikačných scenároch máme rôzne presnosti (INT4, INT8, FP16, FP32). Nasleduje vysvetlenie často používaných presností kvantifikácie.

### **INT4**

Kvantifikácia INT4 je radikálna kvantifikačná metóda, ktorá kvantifikuje váhy a hodnoty aktivácie modelu na 4-bitové celé čísla. Kvantifikácia INT4 zvyčajne vedie k väčšej strate presnosti kvôli menšiemu rozsahu reprezentácie a nižšej presnosti. Avšak v porovnaní s kvantifikáciou INT8 môže INT4 kvantifikácia ďalej znížiť požiadavky na ukladanie a výpočtovú zložitosť modelu. Treba poznamenať, že kvantifikácia INT4 je v praktických aplikáciách relatívne zriedkavá, pretože príliš nízka presnosť môže spôsobovať výrazné zhoršenie výkonu modelu. Okrem toho nie všetok hardvér podporuje operácie INT4, preto je pri výbere kvantifikačnej metódy potrebné zvážiť kompatibilitu hardvéru.

### **INT8**

Kvantifikácia INT8 je proces prevodu váh a aktivácií modelu z plávajúcej desatinnej čiarky na 8-bitové celé čísla. Hoci numerický rozsah reprezentovaný INT8 celými číslami je menší a menej presný, môže výrazne znížiť požiadavky na ukladanie a výpočty. Pri kvantifikácii INT8 prechádzajú váhy a hodnoty aktivácie modelu kvantifikačným procesom, vrátane škálovania a posunu, aby sa čo najviac zachovali pôvodné informácie vo formáte plávajúcej desatinnej čiarky. Počas inferencie sa tieto kvantifikované hodnoty dekvantifikujú späť na čísla s plávajúcou desatinnou čiarkou na výpočty a potom opäť kvantifikujú do INT8 pre ďalší krok. Táto metóda môže poskytnúť dostatočnú presnosť vo väčšine aplikácií pri zachovaní vysokej výpočtovej efektívnosti.

### **FP16**

Formát FP16, teda 16-bitové čísla s plávajúcou desatinnou čiarkou (float16), znižuje pamäťovú náročnosť na polovicu v porovnaní s 32-bitovými číslami s plávajúcou desatinnou čiarkou (float32), čo má výrazné výhody pri veľkoplošných aplikáciách hlbokého učenia. Formát FP16 umožňuje načítať väčšie modely alebo spracovať viac dát v rámci rovnakých pamäťových limitov GPU. Moderný hardvér GPU naďalej podporuje operácie vo formáte FP16, preto používanie tohto formátu môže tiež priniesť zlepšenie rýchlosti výpočtu. Na druhej strane formát FP16 má svoje inherentné nevýhody, konkrétne nižšiu presnosť, čo môže v niektorých prípadoch viesť k numerickej nestabilite alebo strate presnosti.

### **FP32**

Formát FP32 poskytuje vyššiu presnosť a dokáže presne reprezentovať široký rozsah hodnôt. V scenároch, kde sa vykonávajú zložité matematické operácie alebo je potrebný výsledok s vysokou presnosťou, je preferovaný formát FP32. Vysoká presnosť ale tiež znamená vyššiu spotrebu pamäte a dlhší čas výpočtu. Pri veľkoplošných modeloch hlbokého učenia, najmä keď je veľa parametrov modelu a veľké množstvo dát, môže formát FP32 spôsobiť nedostatok pamäte GPU alebo zníženie rýchlosti inferencie.

Na mobilných zariadeniach alebo IoT zariadeniach môžeme modely Phi-3.x konvertovať na INT4, zatiaľ čo AI PC / Copilot PC môžu používať vyššiu presnosť ako INT8, FP16, FP32.

V súčasnosti rôzni výrobcovia hardvéru majú rôzne rámce na podporu generatívnych modelov, ako sú Intel OpenVINO, Qualcomm QNN, Apple MLX a Nvidia CUDA, ktoré sa kombinujú s kvantifikáciou modelov na dokončenie lokálneho nasadenia.

Z technologického hľadiska máme rôznu podporu formátov po kvantifikácii, ako sú formáty PyTorch / TensorFlow, GGUF a ONNX. Vykonal som porovnanie formátov a aplikačných scenárov medzi GGUF a ONNX. Tu odporúčam ONNX kvantifikačný formát, ktorý má dobrú podporu od rámcov modelov až po hardvér. V tejto kapitole sa zameriame na ONNX Runtime pre GenAI, OpenVINO a Apple MLX na vykonanie kvantifikácie modelov (ak máte lepší spôsob, môžete nám ho tiež poslať prostredníctvom PR).

**Táto kapitola obsahuje**

1. [Kvantifikácia Phi-3.5 / 4 pomocou llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantifikácia Phi-3.5 / 4 pomocou rozšírení generatívnej AI pre onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantifikácia Phi-3.5 / 4 pomocou Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantifikácia Phi-3.5 / 4 pomocou Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornenie**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, berte prosím na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nepochopenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->