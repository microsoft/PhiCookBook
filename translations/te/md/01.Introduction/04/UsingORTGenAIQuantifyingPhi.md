<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-12-22T02:08:29+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "te"
}
-->
# **Generative AI extensions for onnxruntime ఉపయోగించి Phi కుటుంబాన్ని క్వాంటైజ్ చేయడం**

## **Generative AI extensions for onnxruntime అంటే ఏమిటి**

ఈ ఎక్స్‌టెన్షన్‌లు ONNX Runtime ( [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) తో జనరేటివ్ AI నడపడానికి మీకు సహాయపడతాయి. ఇవి ONNX మోడళ్ల కోసం జనరేటివ్ AI లూప్‌ను అందిస్తాయి, దీనిలో ONNX Runtime ద్వారా ఇన్ఫరెన్స్, లాజిట్స్ ప్రాసెసింగ్, శోధన మరియు శాంప్లింగ్, మరియు KV క్యాష్ నిర్వహణ ఉంటాయి. డెవలపర్లు ఒక ఉన్నత స్థాయి generate() మెethoden ను పిలవవచ్చు, లేదా మోడల్ యొక్క ప్రతి ఇటరేషన్‌ను లూప్‌లో నడిపించి ఒక్కొక్క టోకెన్‌ను ఉత్పత్తి చేయవచ్చు మరియు ఆప్షనల్‌గా లూప్‌లో జనరేషన్ పారామీటర్లను నవీకరించవచ్చు. ఇది greedy/beam search మరియు TopP, TopK శాంప్లింగ్‌కు మద్దతు కలిగి ఉంది టోకెన్ సీక్వెన్స్‌లను ఉత్పత్తి చేయడానికి అలాగే పునరావృత్తి శిక్షల వంటి బిల్ట్-ఇన్ లాజిట్స్ ప్రాసెసింగ్‌ను కూడా కలిగి ఉంది. మీరు సులభంగా కస్టమ్ స్కోరింగ్ కూడా జోడించవచ్చు.

అప్లికేషన్ స్థాయిలో, మీరు Generative AI extensions for onnxruntime ను ఉపయోగించి C++/ C# / Python ఉపయోగించి అప్లికేషన్లను నిర్మించవచ్చు. మోడల్ స్థాయిలో, మీరు దీన్ని ఫైన్-ట్యూన్ చేసిన మోడళ్లను విలీనం చేయడానికి మరియు సంబంధిత పరిమాణాత్మక డిప్లాయ్‌మెంట్ పనులను చేయడానికి ఉపయోగించవచ్చు.


## **Generative AI extensions for onnxruntime తో Phi-3.5 ను క్వాంటైజ్ చేయడం**

### **మద్దతు పొందిన మోడళ్లు**

Generative AI extensions for onnxruntime Microsoft Phi , Google Gemma, Mistral, Meta LLaMA。 

### **Generative AI extensions for onnxruntime లో Model Builder**

Model Builder ONNX Runtime generate() API తో నడిచే ఆప్టిమైజ్డ్ మరియు క్వాంటైజ్డ్ ONNX మోడళ్లను త్వరగా సృష్టించడాన్ని పెద్దగా ускорిస్తుంది.

Model Builder ద్వారా, మీరు మోడల్‌ను INT4, INT8, FP16, FP32 కు క్వాంటైజ్ చేయవచ్చు, మరియు CPU, CUDA, DirectML, Mobile వంటి వివిధ హార్డ్‌వేర్ ఆక్సలరేషన్ విధానాలను కలిపి ఉపయోగించవచ్చు.

Model Builder ఉపయోగించడానికి మీరు ఇనిస్టాల్ చేయాలి

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

ఇన్‌స్టలేషన్ అనంతరం, మీరు టెర్మినల్ నుండి Model Builder స్క్రిప్ట్ ను రన్ చేసి మోడల్ ఫార్మాట్ మరియు క్వాంటైజేషన్ మార్పుల్ని చేయవచ్చు。


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

సంబంధిత పారామీటర్లను అర్థం చేసుకోండి

1. **model_name** ఇది Hugging Faceపై ఉన్న మోడల్, ఉదాహరణకు microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, మొదలైనవి. ఇది మీరు మోడల్ నిల్వ చేసిన పాథ్ కూడా కావచ్చు

2. **path_to_output_folder** క్వాంటైజ్డ్ మార్పు సేవ్ చేయాల్సిన మార్గం

3. **execution_provider** వెరైన హార్డ్‌వేర్ ఆక్సలరేషన్ మద్దతు, ఉదాహరణకు cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** మేము Hugging Face నుండి మోడల్‌ను డౌన్లోడ్ చేసి స్థానికంగా క్యాష్ చేయడానికి ఉపయోగించే డైరెక్టరీ




***గమనిక：*** <ul>Generative AI extensions for onnxruntime ప్రివ్యూ లో ఉన్నప్పటికీ, అవి Microsoft Oliveలో చేర్చబడ్డాయి, మరియు మీరు Generative AI extensions for onnxruntime Model Builder ఫంక్షన్లను Microsoft Olive ద్వారా కూడా పిలవవచ్చు.</ul>

## **Model Builder ఉపయోగించి Phi-3.5 ను ఎలా క్వాంటైజ్ చేయాలి**

Model Builder ఇప్పుడు Phi-3.5 Instruct మరియు Phi-3.5-Vision కోసం ONNX మోడల్ క్వాంటైజేషన్ ను మద్దతు చేస్తుంది

### **Phi-3.5-Instruct**


**క్వాంటైజ్ చేయబడిన INT 4 కోసం CPU ఆక్సలరేటెడ్ మార్పిడి**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**క్వాంటైజ్ చేయబడిన INT 4 కోసం CUDA ఆక్సలరేటెడ్ మార్పిడి**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. టెర్మినల్‌లో వాతావరణాన్ని సెటప్ చేయండి

```bash

mkdir models

cd models 

```

2. models ఫోల్డర్‌లో microsoft/Phi-3.5-vision-instruct ను డౌన్లోడ్ చేయండి
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. దయచేసి ఈ ఫైల్స్‌ను మీ Phi-3.5-vision-instruct ఫోల్డర్‌కు డౌన్లోడ్ చేయండి

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. ఈ ఫైల్‌ను models ఫోల్డర్‌కు డౌన్లోడ్ చేయండి
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. టెర్మినల్‌కు వెళ్ళండి

    FP32 తో ONNX మద్దతు మార్చండి


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **గమనిక：**

1. Model Builder ప్రస్తుతానికి Phi-3.5-Instruct మరియు Phi-3.5-Vision యొక్క మార్చాల్ని మద్దతు చేస్తుంది, కానీ Phi-3.5-MoE ను కాదు

2. ONNX యొక్క క్వాంటైజ్డ్ మోడల్‌ను ఉపయోగించుకోవడానికి, మీరు దాన్ని Generative AI extensions for onnxruntime SDK ద్వారా ఉపయోగించవచ్చు

3. మేము మరింత బాధ్యతా ప్రమాణాలను పరిగణనలోకి తీసుకోవాలి, కాబట్టి మోడల్ క్వాంటైజేషన్ మార్చిన తర్వాత, ఇంపురత ఫలితాలను పరిశీలించడం మరియు విస్తృత పరీక్షలు చేయడం సిఫార్సు చేయబడుతుంది

4. CPU INT4 మోడల్‌ను క్వాంటైజ్ చేయడం ద్వారా, దాన్ని Edge Device పై డిప్లాయ్ చేయవచ్చు, ఇది బెటర్ అప్లికేషన్ సన్నివేశాలు కలిగి ఉంటుంది, కాబట్టి మేము Phi-3.5-Instruct ను ప్రధానంగా INT4 చుట్టూ పూర్తి చేశాము


## **వనరులు**

1. Generative AI extensions for onnxruntime గురించి మరింత తెలుసుకోండి [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub రిపో [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
నిరాకరణ:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటిక్ అనువాదాల్లో పొరపాట్లు లేదా తప్పులు ఉండవచ్చని కుడా దయచేసి గమనించండి. మూల పత్రాన్ని దాని స్వదేశీ భాషలోని ప్రామాణిక మూలంగా పరిగణించాలి. అత్యంత ముఖ్యమైన సమాచారం కోసం వృత్తిపరమైన మానవ అనువాదం ఇతరాయించబడుతుంది. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏమైనా అపార్థాలు లేదా తప్పుగా అర్థం చేసుకోవడంపై మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->