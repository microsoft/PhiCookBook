# **Inference Phi-3 Android įrenginiuose**

Pažvelkime, kaip galite atlikti spėjimą naudodami Phi-3-mini Android įrenginiuose. Phi-3-mini yra nauja Microsoft modelių serija, leidžianti diegti didelius kalbos modelius (LLM) krašto įrenginiuose ir IoT įrenginiuose.

## Semantic Kernel ir spėjimas

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) yra programų karkasas, leidžiantis kurti programas suderinamas su Azure OpenAI paslauga, OpenAI modeliais ir netgi vietiniais modeliais. Jei esate naujokas Semantic Kernel, siūlome pažvelgti į [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Kaip pasiekti Phi-3-mini naudojant Semantic Kernel

Jį galite derinti su Hugging Face jungtimi Semantic Kernel. Pažvelkite į šį [pavyzdinį kodą](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Pagal numatytuosius nustatymus jis atitinka modelio ID Hugging Face platformoje. Tačiau taip pat galite prisijungti prie vietoje sukurto Phi-3-mini modelio serverio.

### Kvantizuotų modelių kvietimas su Ollama arba LlamaEdge

Daugelis naudotojų renkasi kvantizuotus modelius, kad galėtų paleisti modelius vietoje. [Ollama](https://ollama.com/) ir [LlamaEdge](https://llamaedge.com) leidžia individualiems naudotojams kviesti skirtingus kvantizuotus modelius:

#### Ollama

Galite tiesiogiai paleisti `ollama run Phi-3` arba konfigūruoti ją neprisijungus sukurdami `Modelfile` su kelio adresu į jūsų `.gguf` failą.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Pavyzdinis kodas](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Jei norite naudoti `.gguf` failus tiek debesyje, tiek krašto įrenginiuose vienu metu, LlamaEdge yra puikus pasirinkimas. Galite pasinaudoti šiuo [pavyzdiniu kodu](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) pradėti.

### Įdiekite ir paleiskite Android telefonuose

1. **Atsisiųskite MLC Chat programėlę** (nemokama) Android telefonams.
2. Atsisiųskite APK failą (148MB) ir įdiekite jį savo įrenginyje.
3. Paleiskite MLC Chat programėlę. Matysite AI modelių sąrašą, įskaitant Phi-3-mini.

### Paleiskite Phi-4-mini-reasoning su LiteRT-LM

[Phi-4-mini-reasoning](https://huggingface.co/litert-community/Phi-4-mini-reasoning) yra prieinamas kaip bendruomenės konvertuota int4 `.litertlm` pakuotė Google [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) įrenginio veikimo aplinkai. Android įrenginyje jis veikia CPU arba GPU per [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) programėlę (importuojant pakuotę iš Hugging Face programėlės viduje) arba per LiteRT-LM Kotlin API; ta pati pakuotė taip pat veikia iOS, macOS, Linux ir Windows. Modelio kortelėje pateikiami matuoti greičiai ir paleidimo komandos.

Apibendrinant, Phi-3-mini atveria įdomias galimybes generatyviai dirbtiniam intelektui krašto įrenginiuose, ir galite pradėti tyrinėti jo galimybes Android įrenginiuose.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->