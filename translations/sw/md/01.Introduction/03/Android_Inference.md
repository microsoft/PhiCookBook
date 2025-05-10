<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-05-09T10:50:07+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "sw"
}
-->
# **Kutafsiri Phi-3 kwenye Android**

Tuchunguze jinsi unavyoweza kufanya utambuzi kwa kutumia Phi-3-mini kwenye vifaa vya Android. Phi-3-mini ni mfululizo mpya wa mifano kutoka Microsoft inayoruhusu kuweka Large Language Models (LLMs) kwenye vifaa vya edge na vifaa vya IoT.

## Semantic Kernel na Utambuzi

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) ni mfumo wa programu unaokuwezesha kuunda programu zinazofanya kazi na Azure OpenAI Service, mifano ya OpenAI, na hata mifano ya ndani. Ikiwa wewe ni mpya kwa Semantic Kernel, tunapendekeza uangalie [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Kufikia Phi-3-mini Ukitumia Semantic Kernel

Unaweza kuichanganya na Hugging Face Connector katika Semantic Kernel. Rejelea [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Kwa kawaida, inahusiana na model ID kwenye Hugging Face. Hata hivyo, unaweza pia kuunganishwa na seva ya modeli ya Phi-3-mini uliyoijenga ndani.

### Kupiga Miito kwa Mifano Iliyo Quantized kwa Ollama au LlamaEdge

Watumiaji wengi wanapendelea kutumia mifano iliyopunguzwa ukubwa (quantized) ili kuendesha mifano kwa ndani. [Ollama](https://ollama.com/) na [LlamaEdge](https://llamaedge.com) huruhusu watumiaji binafsi kupiga miito kwa mifano tofauti iliyopunguzwa:

#### Ollama

Unaweza kuendesha moja kwa moja `ollama run Phi-3` au kuipanga bila mtandao kwa kuunda `Modelfile` yenye njia ya faili yako ya `.gguf`.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Ikiwa unataka kutumia faili za `.gguf` kwa wingu na vifaa vya edge kwa wakati mmoja, LlamaEdge ni chaguo zuri. Unaweza kuangalia [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) kuanzia hapo.

### Sakinisha na Endesha kwenye Simu za Android

1. **Pakua programu ya MLC Chat** (Bure) kwa simu za Android.  
2. Pakua faili la APK (148MB) na liweke kwenye kifaa chako.  
3. Fungua programu ya MLC Chat. Utaona orodha ya mifano ya AI, ikiwa ni pamoja na Phi-3-mini.

Kwa muhtasari, Phi-3-mini inaleta fursa mpya za AI za kizazi kwenye vifaa vya edge, na unaweza kuanza kuchunguza uwezo wake kwenye Android.

**Kasi**:  
Hati hii imetafsiriwa kwa kutumia huduma ya utafsiri wa AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuwa sahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu na ya binadamu inashauriwa. Hatubebwi mzigo wowote wa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.