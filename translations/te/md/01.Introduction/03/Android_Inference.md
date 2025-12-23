<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-12-22T01:20:58+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "te"
}
-->
# **Androidలో Phi-3 ఇన్ఫరెన్స్**

ఈ క్రింది భాగంలో Android పరికరాల్లో Phi-3-mini తో మీరు ఎలా ఇన్ఫరెన్స్ చేయగలరో చూద్దాం. Phi-3-mini Microsoft నుండి వచ్చిన ఒక కొత్త మోడళ్ల సిరీస్, ఇది ఎడ్జ్ పరికరాలు మరియు IoT పరికరాలపై Large Language Models (LLMs) ను డిప్లాయ్ చేయడానికి అనుమతిస్తుంది.

## Semantic Kernel మరియు ఇన్ఫరెన్స్

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) ఒక అప్లికేషన్ ఫ్రేమ్‌వర్క్, ఇది Azure OpenAI Service, OpenAI మోడల్స్, మరియు స్థానిక మోడల్స్ కు అనుగుణమైన అప్లికేషన్లను రూపొందించడానికి సహాయపడుతుంది. మీరు Semantic Kernelకి కొత్త అయితే, మేము మీరు [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) ను చూడాలని సూచిస్తున్నాము.

### Semantic Kernel ఉపయోగించి Phi-3-mini యాక్సెస్ చేయడానికి

దాన్ని Semantic Kernelలోని Hugging Face Connector తో కలిపి ఉపయోగించవచ్చు. దీనికి సంబంధించిన ఈ [నమూనా కోడ్](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) ను చూడండి.

డిఫాల్ట్‌గా, ఇది Hugging Face పై ఉన్న మోడల్ IDకి అనుగుణంగా ఉంటుంది. అయితే, మీరు స్థానికంగా రూపొందించిన Phi-3-mini మోడల్ సర్వర్‌కి కూడా కనెక్ట్ చేయవచ్చు.

### Ollama లేదా LlamaEdge తో క్వాంటైజ్డ్ మోడల్స్‌ను కాల్ చేయడం

చాలా వినియోగదారులు మోడల్స్‌ను స్థానికంగా నడవడానికి క్వాంటైజ్డ్ మోడల్స్ ఉపయోగించడాన్ని ఇష్టపడతారు. [Ollama](https://ollama.com/) మరియు [LlamaEdge](https://llamaedge.com) వ్యక్తిగత వినియోగదారులకు వేరే వేరే క్వాంటైజ్డ్ మోడల్స్‌ను కాల్ చేయడానికి అనుమతిస్తాయి:

#### Ollama

మీరు నేరుగా `ollama run Phi-3` నడిపించవచ్చు లేదా మీ `.gguf` ఫైల్ మార్గంతో `Modelfile` సృష్టించడం ద్వారా ఆఫ్‌లైన్‌లో కాన్ఫిగర్ చేయవచ్చు.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[నమూనా కోడ్](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

మీరు క్లౌడ్ మరియు ఎడ్జ్ పరికరాల్లో ఒకేసారి `.gguf` ఫైళ్లను ఉపయోగించాలని ఉంటే, LlamaEdge ఒక గొప్ప ఎంపిక. ప్రారంభించడానికి మీరు ఈ [నమూనా కోడ్](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) ను చూడవచ్చు.

### Android ఫోన్లలో ఇన్‌స్టాల్ చేయడం మరియు నడపడం

1. **MLC Chat యాప్‌ను డౌన్లోడ్ చేయండి** (ఉచితం) Android ఫోన్ల కోసం.
2. APK ఫైల్ (148MB) డౌన్లోడ్ చేసి, మీ డివైస్‌లో ఇన్‌స్టాల్ చేయండి.
3. MLC Chat యాప్‌ను ప్రారంభించండి. మీరు Phi-3-mini సహా AI మోడల్స్ యొక్క జాబితాను చూడగలుగుతారు.

సారాంశంగా, Phi-3-mini ఎడ్జ్ పరికరాలలో జనరేటివ్ AI కోసం ఆసక్తికరమైన అవకాశాలను తెరుస్తుంది, మరియు మీరు Androidపై దాని సామర్థ్యాలను అన్వేషించడం ప్రారంభించవచ్చు.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
నిరాకరణ:
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి శ్రమించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా అసంపూర్ణతలు ఉండవచ్చని దయచేసి గమనించండి. మూల పత్రాన్ని దాని స్థానిక భాషలో ఉన్న వెర్షన్‌ను అధికారిక మూలంగా పరిగణించాలి. కీలకమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫార్సు చేస్తున్నాము. ఈ అనువాదాన్ని ఉపయోగించడం వల్ల వచ్చిన ఏవైనా అపార్థాలు లేదా తప్పుగా అర్థం చేసుకోవడాలకు మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->