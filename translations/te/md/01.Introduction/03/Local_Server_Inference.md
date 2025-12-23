<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-12-22T01:02:39+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "te"
}
-->
# **లోకల్ సర్వర్‌లో Phi-3 ఇన్ఫెరెన్స్**

మేము Phi-3 ను లోకల్ సర్వర్‌లో నియమించవచ్చు. వినియోగదారులు [Ollama](https://ollama.com) లేదా [LM Studio](https://llamaedge.com) పరిష్కారాలను ఎంచుకోవచ్చు, లేదా వారు తమ స్వంత కోడ్ రాయవచ్చు. మీరు Phi-3 యొక్క లోకల్ సర్వీసులను [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) లేదా [Langchain](https://www.langchain.com/) ద్వారా కనెక్ట్ చేసి Copilot అప్లికేషన్లను నిర్మించవచ్చు


## **Phi-3-mini ను యాక్సెస్ చేయడానికి Semantic Kernel ఉపయోగించండి**

Copilot అప్లికేషన్‌లో, మనం Semantic Kernel / LangChain ద్వారా అప్లికేషన్లు సృష్టిస్తాము. ఈ రకమైన అప్లికేషన్ ఫ్రేమ్‌వర్క్ సాధారణంగా Azure OpenAI Service / OpenAI మోడల్స్‌తో అనుకూలంగా ఉంటుంది, మరియు Hugging Face పై ఉన్న ఓపెన్ సోర్స్ మోడల్స్ మరియు లోకల్ మోడల్స్‌ను కూడా మద్దతు చేయగలదు. Semantic Kernel ఉపయోగించి Phi-3-mini ను యాక్సెస్ చేయాలనుకుంటే మనం ఏమి చేయాలి? .NETని ఉదాహరణగా ఉపయోగిస్తూ, దీన్ని Semantic Kernel లోని Hugging Face Connector తో కలపవచ్చు. డిఫాల్ట్‌గా, ఇది Hugging Face上的 మోడల్ id కు అనుగుణంగా ఉంటుంది (మొదటి సారి ఉపయోగిస్తున్నప్పుడు, మోడల్ Hugging Face నుండి డౌన్‌లోడ్ అవుతుంది, ఇది ఎక్కువ సమయం తీసుకుంటుంది). మీరు కూడా స్వతంత్రంగా నిర్మించిన లోకల్ సర్వీస్‌కు కనెక్ట్ చేయవచ్చు. ఇరువరిటితో పోలిస్తే, చివరినిది ఉపయోగించడం మేము సిఫార్సు చేస్తాము, ఎందుకంటే అది అధిక స్వాయాంశ్రయాన్ని కలిగి ఉంటుంది, ముఖ్యంగా సంస్థ అప్లికేషన్లలో.

![sk](../../../../../translated_images/sk.d03785c25edc6d445a2e9ae037979e544e0b0c482f43c7617b0324e717b9af62.te.png)


చిత్రం ద్వారా, Semantic Kernel ఉపయోగించి లోకల్ సర్వీసులకు యాక్సెస్ చేయడం ద్వారా స్వయంగా నిర్మించిన Phi-3-mini మోడల్ సర్వర్‌కి సులభంగా కనెక్ట్ చేయవచ్చునని చూడవచ్చు. ఇక్కడ రన్ అయిన ఫలితం ఉంది

![skrun](../../../../../translated_images/skrun.5aafc1e7197dca2020eefcaeaaee184d29bb0cf1c37b00fd9c79acc23a6dc8d2.te.png)

***నమూనా కోడ్*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
డిస్క్లైమర్:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ద్వారా అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా అసంపూర్తులు ఉండవచ్చు. మూల భాషలోని అసలు పత్రాన్ని అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి వృత్తిపరమైన మానవ అనువాదం చేయించడం మేలకు సూచనీయమే. ఈ అనువాదాన్ని ఉపయోగించడం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుగా అర్థం చేసుకోవడాలకు మేము బాధ్యులు కాదని గమనించండి.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->