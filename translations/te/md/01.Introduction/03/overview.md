<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-12-22T00:40:14+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "te"
}
-->
Phi-3-mini సందర్భంలో, ఇన్ఫెరెన్స్ అనగా మోడల్‌ను ఉపయోగించి ఇన్పుట్ డేటా ఆధారంగా అంచనాలు చేయడం లేదా అవుట్‌పుట్‌లను ఉత్పత్తి చేయడం అనే ప్రక్రియను సూచిస్తుంది. నేను Phi-3-mini మరియు దీని ఇన్ఫెరెన్స్ సామర్థ్యాల గురించి మరిన్ని వివరాలు అందిస్తాను.

Phi-3-mini Microsoft విడుదల చేసిన Phi-3 సిరీస్‌లో భాగం. ఈ మోడల్‌లు చిన్న భాషా మోడళ్ల (Small Language Models, SLMs)తో సాధ్యమయ్యే విషయాలను పునర్వ్యాఖ్య చేయడానికి రూపొందించబడ్డాయి.

Here are some key points about Phi-3-mini and its inference capabilities:

## **Phi-3-mini Overview:**
- Phi-3-mini యొక్క పరామీటర్ పరిమాణం 3.8 బిలియన్.
- ఇది సంప్రదాయ కంప్యూటింగ్ పరికరాలపై మాత్రమే కాకుండా మొబైల్ పరికరాలు మరియు IoT పరికరాల వంటి ఎడ్జ్ పరికరాలపై కూడా నడపగలదు.
- Phi-3-mini విడుదల వలన వ్యక్తులు మరియు సంస్థలు వివిధ హార్డ్‌వేర్ పరికరాల్లో, ముఖ్యంగా పరిమిత వనరుల వాతావరణాల్లో SLMలను అమలులో పెట్టగలుగుతారు.
- ఇది వివిధ మోడల్ ఫార్మాట్లను కవర్ చేస్తుంది, అందులో సంప్రదాయ PyTorch ఫార్మాట్, gguf ఫార్మాట్ యొక్క క్వాంటైజ్డ్ వెర్షన్, మరియు ONNX ఆధారిత క్వాంటైజ్డ్ వెర్షన్ ఉన్నాయి.

## **Accessing Phi-3-mini:**
To access Phi-3-mini, you can use [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) in a Copilot application. Semantic Kernel is generally compatible with Azure OpenAI Service, open-source models on Hugging Face, and local models.
You can also use [Ollama](https://ollama.com) or [LlamaEdge](https://llamaedge.com) to call quantized models. Ollama allows individual users to call different quantized models, while LlamaEdge provides cross-platform availability for GGUF models.

## **Quantized Models:**
Many users prefer to use quantized models for local inference. For example, you can directly run Ollama run Phi-3 or configure it offline using a Modelfile. The Modelfile specifies the GGUF file path and the prompt format.

## **Generative AI Possibilities:**
Combining SLMs like Phi-3-mini opens up new possibilities for generative AI. Inference is just the first step; these models can be used for various tasks in resource-constrained, latency-bound, and cost-constrained scenarios.

## **Unlocking Generative AI with Phi-3-mini: A Guide to Inference and Deployment** 
Learn how to use Semantic Kernel, Ollama/LlamaEdge, and ONNX Runtime to access and infer Phi-3-mini models, and explore the possibilities of generative AI in various application scenarios.

**Features**
Inference phi3-mini model in:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

In summary, Phi-3-mini allows developers to explore different model formats and leverage generative AI in various application scenarios.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
బాధ్యత నిరాకరణ:
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. ఖచ్చితత్వానికి మేము ప్రయత్నించినప్పటికీ, స్వయంచాలక అనువాదాల్లో తప్పులు లేదా లోపాలు ఉండవచ్చునని దయచేసి గమనించండి. మూల పత్రాన్ని దాని మాతృభాషలో ఉన్నదాని ప్రకారం అధికారిక మూలంగా పరిగణించవలెను. కీలకమైన సమాచారం సంబంధించి వృత్తిపరులైన మానవ అనువాదాన్ని సూచిస్తాము. ఈ అనువాదం ఉపయోగించడంవల్ల ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుగా అర్థం చేసుకోవడాలకు మేము బాధ్యులు కాకపోవడం తెలియజేస్తున్నాము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->