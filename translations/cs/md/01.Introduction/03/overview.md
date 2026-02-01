V kontextu Phi-3-mini se inference týká procesu využití modelu k vytváření predikcí nebo generování výstupů na základě vstupních dat. Dovolte mi poskytnout více informací o Phi-3-mini a jeho schopnostech inference.

Phi-3-mini je součástí série modelů Phi-3 vydaných společností Microsoft. Tyto modely jsou navrženy tak, aby předefinovaly možnosti malých jazykových modelů (SLM).

Zde jsou některé klíčové body o Phi-3-mini a jeho schopnostech inference:

## **Přehled Phi-3-mini:**
- Phi-3-mini má velikost parametrů 3,8 miliardy.
- Může běžet nejen na tradičních výpočetních zařízeních, ale také na edge zařízeních, jako jsou mobilní telefony a IoT zařízení.
- Vydání Phi-3-mini umožňuje jednotlivcům i firmám nasazovat SLM na různých hardwarových zařízeních, zejména v prostředích s omezenými zdroji.
- Podporuje různé formáty modelů, včetně tradičního formátu PyTorch, kvantované verze formátu gguf a kvantované verze založené na ONNX.

## **Přístup k Phi-3-mini:**
K přístupu k Phi-3-mini můžete použít [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) v aplikaci Copilot. Semantic Kernel je obecně kompatibilní se službou Azure OpenAI, open-source modely na Hugging Face a lokálními modely.  
Můžete také využít [Ollama](https://ollama.com) nebo [LlamaEdge](https://llamaedge.com) pro volání kvantovaných modelů. Ollama umožňuje jednotlivým uživatelům volat různé kvantované modely, zatímco LlamaEdge poskytuje multiplatformní dostupnost pro modely GGUF.

## **Kvantované modely:**
Mnoho uživatelů preferuje používat kvantované modely pro lokální inference. Například můžete přímo spustit Ollama run Phi-3 nebo jej nakonfigurovat offline pomocí Modelfile. Modelfile specifikuje cestu k souboru GGUF a formát promptu.

## **Možnosti generativní AI:**
Kombinace SLM jako Phi-3-mini otevírá nové možnosti pro generativní AI. Inference je jen prvním krokem; tyto modely lze využít pro různé úkoly v prostředích s omezenými zdroji, nízkou latencí a omezenými náklady.

## **Odemknutí generativní AI s Phi-3-mini: Průvodce inference a nasazením**  
Naučte se, jak používat Semantic Kernel, Ollama/LlamaEdge a ONNX Runtime pro přístup a inference modelů Phi-3-mini a objevte možnosti generativní AI v různých aplikačních scénářích.

**Funkce**  
Inference modelu phi3-mini v:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

Shrnuto, Phi-3-mini umožňuje vývojářům zkoumat různé formáty modelů a využívat generativní AI v různých aplikačních scénářích.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.