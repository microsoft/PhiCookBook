<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-09-12T14:52:51+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "lt"
}
-->
# **Inference Phi-3 Android įrenginiuose**

Pažvelkime, kaip galite atlikti išvestį su Phi-3-mini Android įrenginiuose. Phi-3-mini yra nauja Microsoft modelių serija, leidžianti diegti didelius kalbos modelius (LLMs) kraštiniuose įrenginiuose ir IoT įrenginiuose.

## Semantic Kernel ir išvestis

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) yra aplikacijų kūrimo sistema, leidžianti kurti programas, suderinamas su Azure OpenAI Service, OpenAI modeliais ir netgi vietiniais modeliais. Jei esate naujokas Semantic Kernel, rekomenduojame peržiūrėti [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Kaip pasiekti Phi-3-mini naudojant Semantic Kernel

Jį galite sujungti su Hugging Face Connector Semantic Kernel sistemoje. Žr. šį [Pavyzdinį kodą](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Pagal numatymą jis atitinka modelio ID Hugging Face platformoje. Tačiau taip pat galite prisijungti prie vietinio Phi-3-mini modelio serverio.

### Kvantizuotų modelių naudojimas su Ollama arba LlamaEdge

Daugelis vartotojų renkasi kvantizuotus modelius, kad galėtų juos paleisti vietoje. [Ollama](https://ollama.com/) ir [LlamaEdge](https://llamaedge.com) leidžia individualiems vartotojams naudoti įvairius kvantizuotus modelius:

#### Ollama

Galite tiesiogiai paleisti `ollama run Phi-3` arba konfigūruoti jį neprisijungus, sukurdami `Modelfile` su keliu į jūsų `.gguf` failą.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Pavyzdinis kodas](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Jei norite naudoti `.gguf` failus debesyje ir kraštiniuose įrenginiuose vienu metu, LlamaEdge yra puikus pasirinkimas. Pradėti galite peržiūrėję šį [pavyzdinį kodą](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo).

### Diegimas ir paleidimas Android telefonuose

1. **Atsisiųskite MLC Chat programėlę** (nemokamai) Android telefonams.
2. Atsisiųskite APK failą (148MB) ir įdiekite jį savo įrenginyje.
3. Paleiskite MLC Chat programėlę. Joje matysite AI modelių sąrašą, įskaitant Phi-3-mini.

Apibendrinant, Phi-3-mini suteikia įdomių galimybių generatyvinei AI kraštiniuose įrenginiuose, ir jūs galite pradėti tyrinėti jo galimybes Android platformoje.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.