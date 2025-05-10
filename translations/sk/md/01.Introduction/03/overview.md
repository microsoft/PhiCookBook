<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-09T12:32:22+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "sk"
}
-->
V kontexte Phi-3-mini znamená inference proces použitia modelu na vytváranie predikcií alebo generovanie výstupov na základe vstupných dát. Dovoľte mi poskytnúť vám viac informácií o Phi-3-mini a jeho možnostiach inference.

Phi-3-mini je súčasťou série modelov Phi-3, ktoré vydala spoločnosť Microsoft. Tieto modely sú navrhnuté tak, aby predefinovali možnosti malých jazykových modelov (SLM).

Tu sú niektoré kľúčové body o Phi-3-mini a jeho schopnostiach inference:

## **Prehľad Phi-3-mini:**
- Phi-3-mini má veľkosť parametrov 3,8 miliardy.
- Dokáže bežať nielen na tradičných výpočtových zariadeniach, ale aj na edge zariadeniach, ako sú mobilné telefóny a IoT zariadenia.
- Vydanie Phi-3-mini umožňuje jednotlivcom a firmám nasadiť SLM na rôzne hardvérové zariadenia, najmä v prostrediach s obmedzenými zdrojmi.
- Podporuje rôzne formáty modelov, vrátane tradičného PyTorch formátu, kvantizovanej verzie formátu gguf a kvantizovanej verzie založenej na ONNX.

## **Prístup k Phi-3-mini:**
Na prístup k Phi-3-mini môžete použiť Semantic Kernel v aplikácii Copilot. Semantic Kernel je všeobecne kompatibilný so službou Azure OpenAI, open-source modelmi na Hugging Face a lokálnymi modelmi.  
Môžete tiež využiť Ollama alebo LlamaEdge na volanie kvantizovaných modelov. Ollama umožňuje individuálnym používateľom volať rôzne kvantizované modely, zatiaľ čo LlamaEdge poskytuje multiplatformovú dostupnosť pre modely GGUF.

## **Kvantizované modely:**
Mnohí používatelia uprednostňujú kvantizované modely pre lokálnu inferenciu. Napríklad môžete priamo spustiť Ollama run Phi-3 alebo ho nakonfigurovať offline pomocou Modelfile, ktorý špecifikuje cestu k súboru GGUF a formát promptu.

## **Možnosti generatívnej AI:**
Kombinácia SLM ako Phi-3-mini otvára nové možnosti pre generatívnu AI. Inference je len prvý krok; tieto modely je možné využiť na rôzne úlohy v prostrediach s obmedzenými zdrojmi, nízkou latenciou a obmedzenými nákladmi.

## **Odomknutie generatívnej AI s Phi-3-mini: Sprievodca inference a nasadením**  
Naučte sa, ako používať Semantic Kernel, Ollama/LlamaEdge a ONNX Runtime na prístup a inferenciu modelov Phi-3-mini a preskúmajte možnosti generatívnej AI v rôznych aplikačných scenároch.

**Funkcie**  
Inference modelu phi3-mini v:

- Semantic Kernel  
- Ollama  
- LlamaEdge WASM  
- ONNX Runtime  
- iOS  

Na záver, Phi-3-mini umožňuje vývojárom skúmať rôzne formáty modelov a využiť generatívnu AI v rôznych aplikačných scenároch.

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.