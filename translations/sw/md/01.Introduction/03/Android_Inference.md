# **Inference Phi-3 kwenye Android**

Tuchunguze jinsi unavyoweza kufanya inference kwa kutumia Phi-3-mini kwenye vifaa vya Android. Phi-3-mini ni mfululizo mpya wa modeli kutoka Microsoft unaowezesha kuanzisha Large Language Models (LLMs) kwenye vifaa vya edge na vifaa vya IoT.

## Semantic Kernel na Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) ni mfumo wa programu unaokuwezesha kuunda programu zinazofanana na Azure OpenAI Service, modeli za OpenAI, na hata modeli za ndani. Ikiwa wewe ni mpya kwa Semantic Kernel, tunapendekeza utazame [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Kufikia Phi-3-mini Ukitumia Semantic Kernel

Unaweza kuunganisha na Hugging Face Connector katika Semantic Kernel. Rejelea [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Kwa kawaida, inahusiana na model ID kwenye Hugging Face. Hata hivyo, pia unaweza kuunganishwa na seva ya modeli ya Phi-3-mini iliyojengwa kwa ndani.

### Kupiga Simu kwa Modeli Zilizopunguzwa Ukitumia Ollama au LlamaEdge

Watumiaji wengi wanapendelea kutumia modeli zilizopunguzwa (quantized) ili kuendesha modeli kwa ndani. [Ollama](https://ollama.com/) na [LlamaEdge](https://llamaedge.com) huwapa watumiaji binafsi uwezo wa kupiga simu kwa modeli mbalimbali zilizopunguzwa:

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

Ikiwa unataka kutumia faili za `.gguf` kwenye wingu na vifaa vya edge kwa wakati mmoja, LlamaEdge ni chaguo zuri. Unaweza kurejelea [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) kuanza.

### Sakinisha na Endesha kwenye Simu za Android

1. **Pakua app ya MLC Chat** (Bure) kwa simu za Android.  
2. Pakua faili la APK (148MB) na liweke kwenye kifaa chako.  
3. Fungua app ya MLC Chat. Utaona orodha ya modeli za AI, ikiwa ni pamoja na Phi-3-mini.

Kwa muhtasari, Phi-3-mini hutoa fursa za kusisimua kwa AI ya kizazi kwenye vifaa vya edge, na unaweza kuanza kuchunguza uwezo wake kwenye Android.

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatuna dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.