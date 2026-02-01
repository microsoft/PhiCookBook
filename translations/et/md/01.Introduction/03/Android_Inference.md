# **Inference Phi-3 Androidis**

Vaatame, kuidas saab Android-seadmetes teha järeldusi Phi-3-mini abil. Phi-3-mini on Microsofti uus mudeliseeria, mis võimaldab suurtel keelemudelitel (LLM) töötada servaseadmetes ja IoT-seadmetes.

## Semantic Kernel ja järeldused

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) on rakendusraamistik, mis võimaldab luua rakendusi, mis ühilduvad Azure OpenAI Service'i, OpenAI mudelite ja isegi kohalike mudelitega. Kui oled Semantic Kerneliga uus, soovitame tutvuda [Semantic Kernel Cookbookiga](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Phi-3-mini kasutamine Semantic Kerneliga

Seda saab kombineerida Semantic Kernelis Hugging Face Connectoriga. Vaata [näidiskoodi](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Vaikimisi vastab see Hugging Face'i mudeli ID-le. Kuid võimalik on ühendada ka lokaalselt ehitatud Phi-3-mini mudeliserveriga.

### Kvantiseeritud mudelite kasutamine Ollama või LlamaEdge'iga

Paljud kasutajad eelistavad kvantiseeritud mudeleid, et mudeleid lokaalselt käivitada. [Ollama](https://ollama.com/) ja [LlamaEdge](https://llamaedge.com) võimaldavad individuaalsetel kasutajatel kasutada erinevaid kvantiseeritud mudeleid:

#### Ollama

Saad otse käivitada `ollama run Phi-3` või seadistada selle võrguühenduseta, luues `Modelfile` koos viitega oma `.gguf` failile.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Näidiskood](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Kui soovid kasutada `.gguf` faile nii pilves kui servaseadmetes, on LlamaEdge suurepärane valik. Alustamiseks vaata [näidiskoodi](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo).

### Installimine ja käivitamine Android-telefonides

1. **Laadi alla MLC Chat rakendus** (tasuta) Android-telefonidele.
2. Laadi alla APK-fail (148MB) ja installi see oma seadmesse.
3. Käivita MLC Chat rakendus. Näed AI mudelite loendit, sealhulgas Phi-3-mini.

Kokkuvõttes avab Phi-3-mini põnevaid võimalusi generatiivse AI jaoks servaseadmetes, ja saad alustada selle võimaluste uurimist Androidis.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.