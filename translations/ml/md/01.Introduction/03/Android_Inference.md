<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-12-22T01:22:31+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "ml"
}
-->
# **Android-ൽ Phi-3 ഇൻഫറൻസ്**

ഞങ്ങൾ Android ഉപകരണങ്ങളിൽ Phi-3-mini ഉപയോഗിച്ച് ഇൻഫറൻസ് എങ്ങനെ നടത്താമെന്ന് പരിശോധിക്കാം. Phi-3-mini Microsoft-ൽ നിന്നുള്ള പുതിയ മോഡൽ നിരയിലൊന്നാണ്, ഇത് എജ് ഡിവൈസുകളിലും IoT ഉപകരണങ്ങളിലുമായി Large Language Models (LLMs) വിന്യസിക്കാൻ സാധ്യമാക്കുന്നു.

## Semantic Kernel ഉം ഇൻഫറൻസ്

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) ഒരു അപ്ലിക്കേഷൻ ഫ്രെയിംവർക്കാണ്, ഇത് Azure OpenAI Service, OpenAI മോഡലുകൾ, കൂടാതെ ലൊക്കൽ മോഡലുകൾക്ക് შესაბამისമായ അപ്ലിക്കേഷനുകൾ നിങ്ങൾക്ക് നിർമ്മിക്കാൻ അനുവദിക്കുന്നു. നിങ്ങൾ Semantic Kernel-newആണെങ്കിൽ, [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) നോക്കാമെന്ന് ഞങ്ങൾ നിർദ്ദേശിക്കുന്നു.

### Semantic Kernel ഉപയോഗിച്ച് Phi-3-mini ആക്‌സസ് ചെയ്യാൻ

നീங்கள் അത് Semantic Kernel-ഇൽനിന്നുള്ള Hugging Face Connector-ഓടേക്കൊത്ത് കൂട്ടിച്ചേർക്കാൻ കഴിയും. ഇതിന് ഈ [സാമ്പിൾ കോഡ്](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) കാണുക.

ഡിഫോൾട്ട് ആയി, ഇത് Hugging Face-上的 മോഡൽ ID-നെ അനുഗമിക്കുന്നു. എന്നിരുന്നാലും, നിങ്ങൾക്ക് ലൊക്കലായി നിർമ്മിച്ച Phi-3-mini മോഡൽ സർവറിനൊപ്പം കണക്റ്റ് ചെയ്യാനും കഴിയും.

### Ollama അല്ലെങ്കിൽ LlamaEdge ഉപയോഗിച്ച് ക്വാണ്ടൈസുചെയ്ത മോഡലുകൾ വിളിക്കുക

മിക്കവരും മോഡലുകൾ ലൊക്കലായി റൺ ചെയ്യാൻ ക്വാണ്ടൈസുചയ്യപ്പെട്ട മോഡലുകൾ ഉപയോഗിക്കാനാണ് предпочക്കം. [Ollama](https://ollama.com/)യും [LlamaEdge](https://llamaedge.com)യും വ്യത്യസ്ത ക്വാണ്ടൈസുചെയ്ത മോഡലുകൾ വ്യക്തിഗത ഉപയോക്താക്കൾക്ക് വിളിക്കാൻ അനുവദിക്കുന്നു:

#### Ollama

നീങ്ങൾ നേരിട്ട് `ollama run Phi-3` റൺ ചെയ്യാമോ അല്ലെങ്കിൽ നിങ്ങളുടെ `.gguf` ഫയലിന്റെ പാത്ത് ഉപയോഗിച്ച് ഒരു `Modelfile` സ്രഷ്ടിച്ച് അത് ഓഫ്‌ലൈനിൽ കോൺഫിഗർ ചെയ്യാം.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[സാമ്പിൾ കോഡ്](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

നിങ്ങൾക്ക് ക്ലൗഡ്-ലും എജ് ഡിവൈസുകളിലും ഒരേ സമയം `.gguf` ഫയലുകൾ ഉപയോഗിക്കാൻ ആഗ്രഹിക്കുന്നുവെങ്കിൽ, LlamaEdge നല്ലൊരു തിരഞ്ഞെടുപ്പാണ്. തുടങ്ങി തുടങ്ങാൻ ഈ [സാമ്പിൾ കോഡ്](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) കാണാവുന്നതാണ്.

### Android ഫോണുകളിൽ ഇൻസ്റ്റാൾ ചെയ്ത് റൺ ചെയ്യൽ

1. **MLC Chat ആപ്പ് ഡൗൺലോഡ് ചെയ്യൂ** (സൗജന്യമാണ്) Android ഫോണുകൾക്കായി.
2. APK ഫയൽ (148MB) ഡൗൺലോഡ് ചെയ്ത് നിങ്ങളുടെ ഡിവൈസിൽ ഇൻസ്റ്റാൾ ചെയ്യുക.
3. MLC Chat ആപ്പ് പ്രാരഭമാക്കുക. Phi-3-mini ഉൾപ്പെടെ AI മോഡലുകളുടെ പട്ടിക നിങ്ങൾക്ക് കാണാം.

സംഗ്രഹത്തോടെ, Phi-3-mini എജ് ഡിവൈസുകളിലുണ്ടാകുന്ന ജനറേറ്റീവ് AI-ക്കായി രസകരമായ സാധ്യതകൾ തുറക്കുന്നു, കൂടാതെ Android-ൽ ഇതിന്റെ കഴിവുകൾ പരീക്ഷിക്കാൻ നിങ്ങൾ തുടക്കം കുറിക്കാം.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
അസ്വീകാരം:
ഈ രേഖ AI വിവർത്തന സേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങൾ കൃത്യതക്ക് ശ്രമിച്ചിട്ടും യന്ത്രവത്കൃത വിവർത്തനങ്ങളിൽ പിശകുകളും അസാധുതകളും ഉണ്ടാകാവുന്നതാണ് എന്ന് ദയവായി ശ്രദ്ധിക്കുക. മൂല ഭാഷയിലുള്ള ഒറിജിനൽ രേഖം അംഗീകരിച്ച പ്രാമാണിക ഉറവിടമായിരിക്കണം. നിർണ്ണായക വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മാനവ വിവർത്തനം ഉപയോഗിക്കേണ്ടതാണ്. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണങ്ങളോ തെറ്റായ വ്യാഖ്യാനങ്ങളോ വേണ്ടപ്പെട്ട് ഞങ്ങളെ ബാധിക്കില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->