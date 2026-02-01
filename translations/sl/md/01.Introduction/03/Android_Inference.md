# **Inferenca Phi-3 na Androidu**

Poglejmo, kako lahko izvedete inferenco s Phi-3-mini na napravah z Androidom. Phi-3-mini je nova serija modelov iz Microsofta, ki omogoča uporabo velikih jezikovnih modelov (LLM) na robnih napravah in IoT napravah.

## Semantic Kernel in inferenca

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) je aplikacijski okvir, ki omogoča ustvarjanje aplikacij, združljivih z Azure OpenAI Service, OpenAI modeli in celo lokalnimi modeli. Če ste novi pri Semantic Kernel, priporočamo, da si ogledate [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Dostop do Phi-3-mini prek Semantic Kernel

Lahko ga združite s Hugging Face Connectorjem v Semantic Kernel. Oglejte si ta [primer kode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Privzeto ustreza ID-ju modela na Hugging Face. Vendar se lahko povežete tudi z lokalno postavljenim strežnikom modela Phi-3-mini.

### Klicanje kvantiziranih modelov z Ollama ali LlamaEdge

Veliko uporabnikov raje uporablja kvantizirane modele za lokalno izvajanje modelov. [Ollama](https://ollama.com/) in [LlamaEdge](https://llamaedge.com) omogočata posameznim uporabnikom klic različnih kvantiziranih modelov:

#### Ollama

Model lahko zaženete neposredno z ukazom `ollama run Phi-3` ali pa ga konfigurirate brez povezave tako, da ustvarite `Modelfile` s potjo do vaše `.gguf` datoteke.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Primer kode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Če želite hkrati uporabljati `.gguf` datoteke v oblaku in na robnih napravah, je LlamaEdge odlična izbira. Za začetek si lahko ogledate ta [primer kode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo).

### Namestitev in zagon na Android telefonih

1. **Prenesite aplikacijo MLC Chat** (brezplačno) za Android telefone.  
2. Prenesite APK datoteko (148 MB) in jo namestite na svojo napravo.  
3. Zaženite aplikacijo MLC Chat. Videli boste seznam AI modelov, vključno s Phi-3-mini.

Za povzetek, Phi-3-mini odpira zanimive možnosti za generativno AI na robnih napravah, zato lahko začnete raziskovati njegove zmogljivosti na Androidu.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.