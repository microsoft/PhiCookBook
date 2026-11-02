# **Inferents Phi-3 Androidis**

Uurime, kuidas saate Phi-3-mini abil teha inferentsi Androidi seadmetes. Phi-3-mini on Microsofti uus mudelite seeria, mis võimaldab suurte keelemudelite (LLM) juurutamist servaseadmetel ja IoT-seadmetel.

## Semantilise tuuma ja inferents

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) on rakendusraamistik, mis võimaldab teil luua rakendusi, mis on ühilduvad Azure OpenAI teenuse, OpenAI mudelite ja isegi kohalikult loodud mudelitega. Kui te pole Semantic Kerneliga tuttav, soovitame vaadata [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Phi-3-mini kasutamine Semantic Kerneliga

Võite seda kombineerida Hugging Face'i ühendajaga Semantic Kernelis. Viitamiseks vaadake seda [näidiskoodi](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Vaikimisi vastab see Hugging Face'i mudeli ID-le. Kuid saate ühendada ka kohaliselt loodud Phi-3-mini mudeliserveriga.

### Kvantiseeritud mudelite kutsumine Ollama või LlamaEdge kaudu

Paljud kasutajad eelistavad kvantiseeritud mudeleid mudelite kohalikuks käitamiseks. [Ollama](https://ollama.com/) ja [LlamaEdge](https://llamaedge.com) võimaldavad kasutajatel kutsuda erinevaid kvantiseeritud mudeleid:

#### Ollama

Võite otse käivitada `ollama run Phi-3` või seadistada selle võrguühenduseta, luues `Modelfile` koos oma `.gguf` faili teega.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Näidiskood](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Kui soovite kasutada `.gguf` faile pilves ja servaseadmetes samaaegselt, on LlamaEdge suurepärane valik. Alustamiseks võite vaadata seda [näidiskoodi](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo).

### Installimine ja käivitamine Androidi telefonides

1. **Laadige alla MLC Chati rakendus** (tasuta) Androidi telefonidele.
2. Laadige alla APK-fail (148 MB) ja installige see oma seadmesse.
3. Käivitage MLC Chati rakendus. Näete AI mudelite nimekirja, sealhulgas Phi-3-mini.

### Phi-4-mini-reasoning käivitamine LiteRT-LM-iga

[Phi-4-mini-reasoning](https://huggingface.co/litert-community/Phi-4-mini-reasoning) on saadaval kogukonna konverteeritud int4 `.litertlm` pakendina Google'i [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) seadmel töötava keskkonna jaoks. Androidis töötab see CPU või GPU kaudu [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) rakenduses (impordi pakend Hugging Face'ist rakenduse sees) või LiteRT-LM Kotlin API kaudu; sama pakend töötab ka iOS-il, macOS-il, Linuxil ja Windowsil. Mudelikaartil on loetletud mõõdetud kiirused ja käsklused.

Kokkuvõttes avab Phi-3-mini põnevad võimalused generatiivsele tehisintellektile servaseadmetes ning saate alustada selle võimekuse uurimist Androidis.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->