<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-10-11T12:20:08+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "ta"
}
-->
# **Android-ல் Phi-3 inference**

Android சாதனங்களில் Phi-3-mini-யுடன் inference செய்ய எப்படி செயல்படுவது என்பதை பார்ப்போம். Phi-3-mini என்பது Microsoft-இன் புதிய மாடல் தொடர், இது பெரிய மொழி மாடல்களை (LLMs) edge சாதனங்கள் மற்றும் IoT சாதனங்களில் பயன்படுத்த அனுமதிக்கிறது.

## Semantic Kernel மற்றும் Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) என்பது Azure OpenAI Service, OpenAI மாடல்கள் மற்றும் உள்ளூர் மாடல்களுடன் இணக்கமான பயன்பாடுகளை உருவாக்க அனுமதிக்கும் ஒரு application framework ஆகும். Semantic Kernel-க்கு புதியவராக இருந்தால், [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) ஐப் பார்க்க பரிந்துரைக்கிறோம்.

### Semantic Kernel-ஐப் பயன்படுத்தி Phi-3-mini-யை அணுக

Semantic Kernel-இல் Hugging Face Connector-ஐ இணைக்கலாம். இந்த [மாதிரி குறியீட்டை](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) பார்க்கவும்.

இயல்பாக, இது Hugging Face-ல் உள்ள மாடல் ID-க்கு இணக்கமானது. இருப்பினும், உள்ளூர் கட்டப்பட்ட Phi-3-mini மாடல் சர்வருடன் இணைக்கவும் முடியும்.

### Ollama அல்லது LlamaEdge மூலம் Quantized மாடல்களை அழைக்க

பயனர்கள் பெரும்பாலும் உள்ளூர் மாடல்களை இயக்க Quantized மாடல்களை பயன்படுத்த விரும்புகிறார்கள். [Ollama](https://ollama.com/) மற்றும் [LlamaEdge](https://llamaedge.com) தனிப்பட்ட பயனர்களுக்கு பல Quantized மாடல்களை அழைக்க அனுமதிக்கின்றன:

#### Ollama

நீங்கள் நேரடியாக `ollama run Phi-3` ஐ இயக்கலாம் அல்லது உங்கள் `.gguf` கோப்பின் பாதையை உள்ளடக்கிய `Modelfile` உருவாக்கி அதை offline-ல் அமைக்கலாம்.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[மாதிரி குறியீடு](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

`.gguf` கோப்புகளை மேகத்தில் மற்றும் edge சாதனங்களில் ஒரே நேரத்தில் பயன்படுத்த விரும்பினால், LlamaEdge ஒரு சிறந்த தேர்வாகும். ஆரம்பிக்க இந்த [மாதிரி குறியீட்டை](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) பார்க்கவும்.

### Android போன்களில் நிறுவி இயக்க

1. **MLC Chat app-ஐ** (இலவசம்) Android போன்களுக்கு பதிவிறக்கவும்.
2. APK கோப்பை (148MB) பதிவிறக்கி உங்கள் சாதனத்தில் நிறுவவும்.
3. MLC Chat app-ஐ தொடங்கவும். Phi-3-mini உட்பட AI மாடல்களின் பட்டியலை நீங்கள் காணலாம்.

சுருக்கமாக, Phi-3-mini edge சாதனங்களில் generative AI-க்கு புதிய சாத்தியங்களைத் திறக்கிறது, மேலும் Android-ல் அதன் திறன்களை ஆராய துவங்கலாம்.

---

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.