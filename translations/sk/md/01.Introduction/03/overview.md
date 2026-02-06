V kontexte Phi-3-mini sa inferencia vzťahuje na proces použitia modelu na tvorbu predpovedí alebo generovanie výstupov na základe vstupných dát. Dovoľte mi poskytnúť vám viac informácií o Phi-3-mini a jeho schopnostiach inferencie.

Phi-3-mini je súčasťou série modelov Phi-3, ktoré vydala spoločnosť Microsoft. Tieto modely sú navrhnuté tak, aby predefinovali možnosti malých jazykových modelov (SLM).

Tu sú niektoré kľúčové body o Phi-3-mini a jeho schopnostiach inferencie:

## **Prehľad Phi-3-mini:**
- Phi-3-mini má veľkosť parametrov 3,8 miliardy.
- Môže bežať nielen na tradičných výpočtových zariadeniach, ale aj na edge zariadeniach, ako sú mobilné zariadenia a IoT zariadenia.
- Vydanie Phi-3-mini umožňuje jednotlivcom a firmám nasadiť SLM na rôznych hardvérových zariadeniach, najmä v prostrediach s obmedzenými zdrojmi.
- Podporuje rôzne formáty modelov, vrátane tradičného formátu PyTorch, kvantizovanej verzie formátu gguf a kvantizovanej verzie založenej na ONNX.

## **Prístup k Phi-3-mini:**
Na prístup k Phi-3-mini môžete použiť [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) v aplikácii Copilot. Semantic Kernel je všeobecne kompatibilný so službou Azure OpenAI, open-source modelmi na Hugging Face a lokálnymi modelmi.  
Môžete tiež použiť [Ollama](https://ollama.com) alebo [LlamaEdge](https://llamaedge.com) na volanie kvantizovaných modelov. Ollama umožňuje jednotlivým používateľom volať rôzne kvantizované modely, zatiaľ čo LlamaEdge poskytuje multiplatformovú dostupnosť pre modely GGUF.

## **Kvantizované modely:**
Mnohí používatelia uprednostňujú používanie kvantizovaných modelov pre lokálnu inferenciu. Napríklad môžete priamo spustiť Ollama run Phi-3 alebo ho nakonfigurovať offline pomocou Modelfile. Modelfile špecifikuje cestu k súboru GGUF a formát promptu.

## **Možnosti generatívnej AI:**
Kombinácia SLM ako Phi-3-mini otvára nové možnosti pre generatívnu AI. Inferencia je len prvým krokom; tieto modely je možné využiť na rôzne úlohy v prostrediach s obmedzenými zdrojmi, nízkou latenciou a obmedzeným rozpočtom.

## **Odomknutie generatívnej AI s Phi-3-mini: Sprievodca inferenciou a nasadením**  
Naučte sa, ako používať Semantic Kernel, Ollama/LlamaEdge a ONNX Runtime na prístup a inferenciu modelov Phi-3-mini a preskúmajte možnosti generatívnej AI v rôznych aplikačných scenároch.

**Funkcie**  
Inferenciu modelu phi3-mini v:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

Na záver, Phi-3-mini umožňuje vývojárom skúmať rôzne formáty modelov a využiť generatívnu AI v rôznych aplikačných scenároch.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.