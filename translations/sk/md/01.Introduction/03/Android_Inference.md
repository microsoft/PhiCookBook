# **Inference Phi-3 na Android**

Pozrime sa, ako môžete vykonávať inferenciu s Phi-3-mini na zariadeniach s Androidom. Phi-3-mini je nová séria modelov od Microsoftu, ktorá umožňuje nasadenie veľkých jazykových modelov (LLM) na edge zariadeniach a IoT zariadeniach.

## Semantic Kernel a inferencia

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) je aplikačný framework, ktorý vám umožňuje vytvárať aplikácie kompatibilné so službou Azure OpenAI, OpenAI modelmi, ale aj s lokálnymi modelmi. Ak ste v Semantic Kernel nováčik, odporúčame pozrieť si [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Ako pristupovať k Phi-3-mini pomocou Semantic Kernel

Môžete ho skombinovať s Hugging Face Connectorom v Semantic Kernel. Pozrite si tento [ukážkový kód](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Štandardne zodpovedá modelovému ID na Hugging Face, no môžete sa tiež pripojiť k lokálne vytvorenému serveru modelu Phi-3-mini.

### Volanie kvantizovaných modelov cez Ollama alebo LlamaEdge

Mnohí používatelia uprednostňujú používanie kvantizovaných modelov na lokálne spúšťanie modelov. [Ollama](https://ollama.com/) a [LlamaEdge](https://llamaedge.com) umožňujú jednotlivým používateľom volať rôzne kvantizované modely:

#### Ollama

Môžete priamo spustiť `ollama run Phi-3` alebo ho nakonfigurovať offline vytvorením `Modelfile` so cestou k vášmu `.gguf` súboru.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Ukážkový kód](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Ak chcete používať `.gguf` súbory súčasne v cloude aj na edge zariadeniach, LlamaEdge je skvelá voľba. Naštartovať sa môžete podľa tohto [ukážkového kódu](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo).

### Inštalácia a spustenie na Android telefónoch

1. **Stiahnite si aplikáciu MLC Chat** (zadarmo) pre Android telefóny.  
2. Stiahnite si APK súbor (148MB) a nainštalujte ho do svojho zariadenia.  
3. Spustite aplikáciu MLC Chat. Uvidíte zoznam AI modelov vrátane Phi-3-mini.

Na záver, Phi-3-mini otvára vzrušujúce možnosti pre generatívnu AI na edge zariadeniach a môžete začať objavovať jeho schopnosti na Androide.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.