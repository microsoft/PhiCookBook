# **Phi కుటుంబాన్ని llama.cpp ఉపయోగించి క్వాంటైజ్ చేయడం**

## **llama.cpp అంటే ఏమిటి**

llama.cpp ప్రధానంగా C++ లో రాయబడిన ఓ ఓపెన్-సోర్స్ సాఫ్ట్‌వేర్ లైబ్రరీ, ఇది Llama వంటి వివిధ పెద్ద భాషా మోడళ్ల (LLMs) పై ఇన్ఫరెన్స్ నిర్వహిస్తుంది. దీని ప్రధాన లక్ష్యం తక్కువ సెటప్‌తో విస్తృతమైన హార్డ్‌వేర్‌లో LLM ఇన్ఫరెన్స్‌కు అత్యాధునిక పనితీరును అందించడం. అదనంగా, ఈ లైబ్రరీకి కోసం Python బైండింగ్స్ అందుబాటులో ఉన్నాయి, ఇవి టెక్స్ట్ కంప్లీషన్ కోసం హై-లెవల్ API మరియు OpenAI అనుకూల వెబ్ సర్వర్ అందిస్తాయి.

llama.cpp యొక్క ప్రధాన లక్ష్యం తక్కువ సెటప్‌తో మరియు విస్తృత రకాల హార్డ్‌వేర్‌పై — లోకల్ మరియు క్లౌడ్ రెండింటిలో — అత్యాధునిక పనితీరుతో LLM ఇన్ఫరెన్స్ చేయగలగడం.

- Dependencies లేకుండా సాధారణ C/C++ అమలు
- Apple silicon ఒక ప్రాధాన్యత ఉన్న ప్లాట్‌ఫార్మ్ - ARM NEON, Accelerate మరియు Metal frameworks ద్వారా ఆప్టిమైజ్ చేయబడింది
- x86 ఆర్కిటెక్చర్ల కోసం AVX, AVX2 మరియు AVX512 వెర్షన్‌లు
- వేగవంతమైన ఇన్ఫరెన్స్ మరియు మెమరీ ఉపయోగాన్ని తగ్గించడానికి 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, మరియు 8-bit మొత్తం సంఖ్య క్వాంటైజేషన్
- NVIDIA GPUs పై LLMs నడపడానికి అనుకూలమైన కస్టమ్ CUDA కర్నెల్స్ (AMD GPUs కోసం HIP ద్వారా సపోర్ట్)
- Vulkan మరియు SYCL బ్యాక్‌ఎండ్ సపోర్ట్
- మొత్తం VRAM సామర్థ్యం కన్నా పెద్ద మోడళ్లను భాగంగా వేగవంతం చేయడానికి CPU+GPU హైబ్రిడ్ ఇన్ఫరెన్స్

## **llama.cpp ఉపయోగించి Phi-3.5 ని క్వాంటైజ్ చేయడం**

Phi-3.5-Instruct మోడల్‌ను llama.cpp ఉపయోగించి క్వాంటైజ్ చేయవచ్చు, కానీ Phi-3.5-Vision మరియు Phi-3.5-MoE ఇంకా సపోర్ట్ అయ్యే పరిస్థితిలో లేవు. llama.cpp మార్చే ఫార్మాట్ gguf, ఇది కూడా అత్యంత విస్తృతంగా ఉపయోగించే క్వాంటైజేషన్ ఫార్మాట్.

Hugging Faceపై చాలా సంఖ్యలో క్వాంటైజ్డ్ GGUF ఫార్మాట్ మోడళ్లు ఉన్నాయి. AI Foundry, Ollama, మరియు LlamaEdge llama.cpp పై ఆధారపడి ఉన్నవారు, కాబట్టి GGUF మోడళ్లు కూడా తరచుగా ఉపయోగించబడతాయి.

### **GGUF అంటే ఏమిటి**

GGUF ఒక బైనరీ ఫార్మాట్, ఇది మోడళ్లను వేగంగా లోడ్ చేయడం మరియు సేవ్ చేయడం కోసం ఆప్టిమైజ్ చేయబడింది, ఇది ఇన్ఫరెన్స్ అవసరాల కోసం చాలా సమర్ధవంతంగా ఉంటుంది. GGUF ను GGML మరియు ఇతర ఎగ్జిక్యూటర్లతో ఉపయోగించడానికి డిజైన్ చేశారు. GGUF ని llama.cpp ను అభివృద్ధి చేసిన @ggerganov అభివృద్ధి చేశారు, అతడే llama.cpp యొక్క డెవలపర్ కూడా, ఇది ఒక ప్రముఖ C/C++ LLM ఇన్ఫరెన్స్ ఫ్రేమ్‌వర్క్. PyTorch వంటి ఫ్రేమ్‌వర్క్‌లలో ప్రారంభంలో అభివృద్ధి చేసిన మోడళ్లు వాటి ఇంజిన్లలో ఉపయోగం కోసం GGUF ఫార్మాట్‌కు మార్చవచ్చు.

### **ONNX vs GGUF**

ONNX ఒక సంప్రదాయ మెషీన్ లెర్నింగ్/డీప్ లెర్నింగ్ ఫార్మాట్, ఇది వివిధ AI ఫ్రేమ్‌వర్క్‌లలో బాగా సపోర్ట్ చేస్తుంది మరియు ఎజ్ పరికరాల్లో ఉపయోగించడానికి మంచి సందర్భాలు కలిగి ఉంటుంది. GGUF విషయానికి వస్తే, అది llama.cpp ఆధారంగా ఉంది మరియు GenAI యుగంలో ఉత్పత్తి కాలింది అని చెప్పవచ్చు. రెండింటి వినియోగం సమానమైనది. ఎంబెడెడ్ హార్డ్‌వేర్ మరియు అప్లికేషన్ లేయర్లలో మెరుగైన పనితీరును కోరుకుంటే ONNX మీ ఎంపిక కావచ్చు. మీరు llama.cpp యొక్క డెరివేటివ్ ఫ్రేమ్‌వర్క్ మరియు టెక్నాలజీని ఉపయోగిస్తే, তাহলে GGUF బెటర్ అయి ఉండొచ్చు.

### **llama.cpp ఉపయోగించి Phi-3.5-Instruct క్వாண்டైజేషన్**

**1. Environment Configuration**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Quantization**

llama.cpp ఉపయోగించి Phi-3.5-Instruct ను FP16 GGUF గా మార్చడం


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5 ను INT4గా క్వాంటైజ్ చేయడం


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testing**

llama-cpp-python ను ఇన్‌స్టాల్ చేయండి


```bash

pip install llama-cpp-python -U

```

***గమనిక*** 

మీరు Apple Silicon ఉపయోగిస్తే , దయచేసి ఇలా llama-cpp-python ను ఇన్‌స్టాల్ చేయండి


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

పరిశీలన/testing 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **వనరులు**

1. llama.cpp గురించి మరింత తెలుసుకోండి [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. onnxruntime గురించి మరింత తెలుసుకోండి [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. GGUF గురించి మరింత తెలుసుకోండి [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
డిస్క్లైమర్:
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా లోపాలు ఉండవచ్చని దయచేసి గమనించండి. స్థానిక భాషలోని అసలు పత్రాన్ని అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి వృత్తిపరమైన మానవ అనువాదాన్ని సూచిస్తున్నాము. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదిట్టుల కోసం మేము బాధ్యులు కాదని స్పష్టం చేయబడును.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->