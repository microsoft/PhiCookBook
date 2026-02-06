Phi-3-mini தொடர்பான சூழலில், inference என்பது மாடலை பயன்படுத்தி உள்ளீட்டு தரவின் அடிப்படையில் கணிப்புகள் செய்ய அல்லது வெளியீடுகளை உருவாக்கும் செயல்முறையை குறிக்கிறது. Phi-3-mini மற்றும் அதன் inference திறன்களைப் பற்றிய மேலும் விவரங்களை உங்களுக்கு வழங்குகிறேன்.

Phi-3-mini என்பது மைக்ரோசாஃப்ட் வெளியிட்ட Phi-3 மாடல் தொடரின் ஒரு பகுதியாகும். இந்த மாடல்கள் Small Language Models (SLMs) மூலம் சாத்தியமானவற்றை மறுபரிசீலனை செய்ய வடிவமைக்கப்பட்டுள்ளன.

Phi-3-mini மற்றும் அதன் inference திறன்களைப் பற்றிய முக்கிய அம்சங்கள்:

## **Phi-3-mini கண்ணோட்டம்:**
- Phi-3-mini 3.8 பில்லியன் அளவிலான பராமீட்டர்களைக் கொண்டுள்ளது.
- இது பாரம்பரிய கணினி சாதனங்களில் மட்டுமல்லாமல், மொபைல் சாதனங்கள் மற்றும் IoT சாதனங்கள் போன்ற edge சாதனங்களில் இயங்க முடியும்.
- Phi-3-mini வெளியீடு தனிநபர்கள் மற்றும் நிறுவனங்களுக்கு resource-constrained சூழல்களில் SLMகளை வெவ்வேறு hardware சாதனங்களில் பயன்படுத்த அனுமதிக்கிறது.
- இது பாரம்பரிய PyTorch வடிவம், gguf வடிவத்தின் quantized பதிப்பு மற்றும் ONNX அடிப்படையிலான quantized பதிப்பு போன்ற பல மாடல் வடிவங்களை உள்ளடக்கியது.

## **Phi-3-mini ஐ அணுகுதல்:**
Phi-3-mini ஐ அணுக, [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) ஐ Copilot பயன்பாட்டில் பயன்படுத்தலாம். Semantic Kernel பொதுவாக Azure OpenAI Service, Hugging Face-ல் உள்ள open-source மாடல்கள் மற்றும் local மாடல்களுடன் இணக்கமாக உள்ளது.  
நீங்கள் [Ollama](https://ollama.com) அல்லது [LlamaEdge](https://llamaedge.com) ஐ quantized மாடல்களை அழைக்க பயன்படுத்தலாம். Ollama தனிநபர் பயனர்களுக்கு பல quantized மாடல்களை அழைக்க அனுமதிக்கிறது, LlamaEdge GGUF மாடல்களுக்கு cross-platform கிடைக்கும் வசதியை வழங்குகிறது.

## **Quantized மாடல்கள்:**
பல பயனர்கள் local inference க்காக quantized மாடல்களை பயன்படுத்த விரும்புகிறார்கள். உதாரணமாக, நீங்கள் நேரடியாக Ollama run Phi-3 ஐ இயக்கலாம் அல்லது Modelfile ஐ offline முறையில் அமைக்கலாம். Modelfile GGUF கோப்பு பாதை மற்றும் prompt வடிவத்தை குறிப்பிடுகிறது.

## **Generative AI சாத்தியங்கள்:**
Phi-3-mini போன்ற SLMகளை இணைப்பது Generative AI க்கான புதிய சாத்தியங்களைத் திறக்கிறது. Inference என்பது முதல் படி மட்டுமே; இந்த மாடல்கள் resource-constrained, latency-bound மற்றும் cost-constrained சூழல்களில் பல்வேறு பணிகளுக்கு பயன்படுத்தப்படலாம்.

## **Generative AI திறக்க Phi-3-mini: Inference மற்றும் Deployment க்கான வழிகாட்டி**
Semantic Kernel, Ollama/LlamaEdge மற்றும் ONNX Runtime ஐ பயன்படுத்தி Phi-3-mini மாடல்களை அணுகவும், inference செய்யவும், மற்றும் பல்வேறு பயன்பாட்டு சூழல்களில் Generative AI சாத்தியங்களை ஆராயவும்.

**அம்சங்கள்**
Phi-3-mini மாடலை கீழ்க்காணும் இடங்களில் inference செய்ய:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

சுருக்கமாக, Phi-3-mini டெவலப்பர்களுக்கு மாடல் வடிவங்களை ஆராயவும், Generative AI ஐ பல்வேறு பயன்பாட்டு சூழல்களில் பயன்படுத்தவும் அனுமதிக்கிறது.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.