# **Inference Phi-3 na Androidu**

Pojďme se podívat, jak můžete provádět inference s Phi-3-mini na zařízeních s Androidem. Phi-3-mini je nová řada modelů od Microsoftu, která umožňuje nasazení velkých jazykových modelů (LLM) na edge zařízeních a IoT zařízeních.

## Semantic Kernel a inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) je aplikační framework, který vám umožní vytvářet aplikace kompatibilní s Azure OpenAI Service, OpenAI modely a dokonce i s lokálními modely. Pokud jste se Semantic Kernelem teprve začínáte, doporučujeme se podívat na [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Jak přistupovat k Phi-3-mini pomocí Semantic Kernel

Můžete ho zkombinovat s Hugging Face Connector v Semantic Kernel. Podívejte se na tento [ukázkový kód](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Ve výchozím nastavení odpovídá model ID na Hugging Face. Nicméně se můžete také připojit k lokálně postavenému serveru modelu Phi-3-mini.

### Volání kvantovaných modelů pomocí Ollama nebo LlamaEdge

Mnoho uživatelů dává přednost používání kvantovaných modelů pro lokální běh modelů. [Ollama](https://ollama.com/) a [LlamaEdge](https://llamaedge.com) umožňují jednotlivým uživatelům volat různé kvantované modely:

#### Ollama

Můžete přímo spustit `ollama run Phi-3` nebo jej nakonfigurovat offline vytvořením `Modelfile` s cestou k vašemu `.gguf` souboru.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Ukázkový kód](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Pokud chcete používat `.gguf` soubory současně v cloudu i na edge zařízeních, LlamaEdge je skvělá volba. Pro začátek se můžete podívat na tento [ukázkový kód](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo).

### Instalace a spuštění na telefonech s Androidem

1. **Stáhněte si aplikaci MLC Chat** (zdarma) pro Android telefony.  
2. Stáhněte APK soubor (148MB) a nainstalujte jej do svého zařízení.  
3. Spusťte aplikaci MLC Chat. Uvidíte seznam AI modelů, včetně Phi-3-mini.

Shrnuto, Phi-3-mini otevírá vzrušující možnosti pro generativní AI na edge zařízeních a můžete začít objevovat jeho schopnosti na Androidu.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.