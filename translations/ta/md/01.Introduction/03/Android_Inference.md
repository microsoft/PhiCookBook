# **ஆண்ட்ராய்டில் Inference Phi-3**

ஆண்ட்ராய்டு சாதனங்களில் Phi-3-mini உடன் inference செய்ய எப்படி என்பதை விபரமாக ஆராய்ந்து கொள்வோம். Phi-3-mini என்பதாவது மைக்ரோசாஃப்ட் வழங்கும் புதிய தரம் கொண்ட மாடல் தொடர், இது எட்ஜ் சாதனங்களுக்கும் IoT சாதனங்களுக்குமான பெரிய மொழி மாதிரிகளை (LLMs) வழங்க உதவுகிறது.

## Semantic Kernel மற்றும் Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) என்பது Azure OpenAI சேவை, OpenAI மாதிரிகள் மற்றும் உள்ளூர் மாதிரிகளுடன் பொருந்தக்கூடிய பயன்பாடுகளை உருவாக்க உதவும் ஒரு பயன்பாட்டு கட்டமைப்பு ஆகும். Semantic Kernel இல் புதியவராக இருப்பின், [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) ஐ பார்வையிட பரிந்துரைக்கப்படுகின்றது.

### Semantic Kernel மூலம் Phi-3-mini ஐ அணுகுவது எப்படி

அதை Semantic Kernel இல் Hugging Face Connector உடன் இணைக்கலாம். இதற்கான [மாதிரி குறியீட்டை](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) பார்க்கவும்.

இயல்பாக இது Hugging Face இல் உள்ள மாதிரி ஐடியை சார்ந்ததாக இருக்கும். எனினும், உள்ளூரில் கட்டிய Phi-3-mini மாதிரி சேவையகத்துடன் கூட இணைக்க முடியும்.

### Ollama அல்லது LlamaEdge இலுள்ள Quantized மாடல்களை அழைப்பது

பல பயனாளர்கள் உள்ளூரிலேயே மாதிரிகளை இயக்க quantized மாடல்களைப் பயன்படுத்த விரும்புகிறார்கள். [Ollama](https://ollama.com/) மற்றும் [LlamaEdge](https://llamaedge.com) தனிப்பட்ட பயனாளர்களுக்கு வெவ்வேறு quantized மாதிரிகளை அழைக்க அனுமதிக்கின்றன:

#### Ollama

`ollama run Phi-3` ஐ நேரடியாக இயக்கலாம் அல்லது `.gguf` கோப்பின் பாதையை கொண்ட `Modelfile` உருவாக்கி அதை ஆஃப்லைனில் அமைக்க முடியும்.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[மாதிரி குறியீடு](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

உங்கள் `.gguf` கோப்புகளை மேகம் மற்றும் எட்ஜ் சாதனங்களில் ஒரே சமயத்தில் பயன்படுத்த LlamaEdge சிறந்த தேர்வாகும். தொடங்க இந்த [மாதிரி குறியீட்டை](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) பார்க்கவும்.

### ஆண்ட்ராய்டு போன்களில் நிறுவி இயக்குவது

1. **MLC Chat பயன்பாட்டை** (இலவசம்) ஆண்ட்ராய்டு போன்களுக்கு பதிவிறக்கவும்.
2. APK கோப்பை (148MB) பதிவிறக்கி உங்கள் சாதனத்தில் நிறுவவும்.
3. MLC Chat பயன்பாட்டை துவங்கவும். Phi-3-mini உட்பட பல AI மாதிரிகள் பட்டியலில் தோன்றும்.

### LiteRT-LM உடன் Phi-4-mini-reasoning ஐ இயக்குவது

[Phi-4-mini-reasoning](https://huggingface.co/litert-community/Phi-4-mini-reasoning) என்பது சமுதாயத்தால் மாற்றியமைக்கப்பட்ட int4 `.litertlm` தொகுப்பு ஆகும், இது கூகுளின் [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) சாதனத்தில் இயங்கும் நேர்த்திவாய்ப்பு முறைக்கானது. ஆண்ட்ராய்டில் CPU அல்லது GPU யில் [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) பயன்பாட்டின் மூலம் (பயன்பாட்டுக்குள் Hugging Face இல் இருந்து தொகுப்பை இறக்குமதி செய்யவும்) அல்லது LiteRT-LM Kotlin API மூலம் இயங்கும்; அதே தொகுப்பு iOS, macOS, Linux மற்றும் Windows-இல் கூட இயங்கும். மாதிரி அட்டை அளவிடப்பட்ட வேகங்களும் இயக்கக் கட்டளைகளும் பட்டியலிடப்பட்டுள்ளது.

சுருக்கமாக, Phi-3-mini எட்ஜ் சாதனங்களில் உருவாக்கும் AIக்கான அதிரடியான வாய்ப்புகளை திறக்கிறது, மற்றும் ஆண்ட்ராய்டில் அதன் திறன்களை நீங்கள் ஆராயத் தொடங்கலாம்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->