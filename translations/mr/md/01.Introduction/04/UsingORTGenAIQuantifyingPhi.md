# **onnxruntime साठी Generative AI विस्तारांचा वापर करून Phi कुटुंबाचे क्वांटायझेशन**

## **onnxruntime साठी Generative AI विस्तार म्हणजे काय**

हे विस्तार तुम्हाला ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) सह Generative AI चालविण्यात मदत करतात. हे ONNX मॉडेल्ससाठी generative AI लूप प्रदान करते, ज्यामध्ये ONNX Runtime सह इन्फरन्स, logits प्रक्रिया, शोध व सैम्पलिंग, आणि KV कॅश व्यवस्थापन यांचा समावेश आहे. विकसक उच्च स्तराचा generate() मेथड कॉल करू शकतात, किंवा मॉडेलच्या प्रत्येक पुनरावृत्तीमध्ये वेगवेगळ्या टोकनसाठी एक एक करून टोकन तयार करू शकतात, आणि पर्यायीपणे लूपमध्ये जनरेशन पॅरामीटर्स अपडेट करू शकतात. यात greedy/beam शोध व TopP, TopK सैम्पलिंगचा समर्थन आहे ज्या टोकन साखळ्या तयार करतात आणि पुनरावृत्ती दंडासारख्या अंतर्निर्मित logits प्रक्रियेचे समर्थन आहे. तुम्ही सहजपणे सानुकूल स्कोरिंग देखील जोडू शकता.

अनुप्रयोगस्तरावर, तुम्ही C++ / C# / Python वापरून onnxruntime साठी Generative AI विस्तार वापरून अनुप्रयोग तयार करू शकता. मॉडेल स्तरावर, तुम्ही हे वापरून फाईन-ट्यून केलेल्या मॉडेल्स मर्ज करू शकता आणि संबंधित मात्रात्मक वितरणाचे काम करू शकता.


## **onnxruntime साठी Generative AI विस्तार वापरून Phi-3.5 चे क्वांटायझेशन**

### **समर्थित मॉडेल्स**

onnxruntime साठी Generative AI विस्तार Microsoft Phi, Google Gemma, Mistral, Meta LLaMA यांच्या क्वांटायझेशन रूपांतरणाचे समर्थन करतात.


### **onnxruntime साठी Generative AI विस्तारमधील मॉडेल बिल्डर**

मॉडेल बिल्डर OPTIMIZED आणि QUANTIZED ONNX मॉडेल्स तयार करण्याची प्रक्रिया मोठ्या प्रमाणावर वेगवान करते ज्यांचा वापर ONNX Runtime generate() API सोबत होऊ शकतो.

मॉडेल बिल्डरच्या माध्यमातून, तुम्ही मॉडेलचे INT4, INT8, FP16, FP32 मध्ये क्वांटायझेशन करू शकता, आणि CPU, CUDA, DirectML, Mobile इत्यादी हॅर्डवेअर वेगवेगळ्या प्रमाणीकरण पद्धती एकत्र करू शकता.

मॉडेल बिल्डर वापरण्यासाठी तुम्हाला खालील प्रमाणे स्थापित करावे लागेल

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

प्रतिष्ठापनानंतर, तुम्ही टर्मिनलवरून मॉडेल बिल्डर स्क्रिप्ट चालवून मॉडेल फॉरमॅट आणि क्वांटायझेशन रूपांतरण करू शकता.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

संबंधित पॅरामीटर्स समजून घ्या

1. **model_name** हे Hugging Face वरील मॉडेल आहे, जसे microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct इत्यादी. हे तुम्ही जतन केलेल्या मॉडेलचा मार्ग देखील असू शकतो

2. **path_to_output_folder** क्वांटायझेशन रूपांतरण जतन करण्याचा मार्ग

3. **execution_provider** वेगवेगळ्या हॅर्डवेअर वेगासाठी समर्थन, जसे cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** आम्ही Hugging Face वरून मॉडेल डाउनलोड करतो आणि ते स्थानिकरीत्या कॅश करतो




***टीप：*** <ul>जरी onnxruntime साठी Generative AI विस्तार प्रिव्ह्यूमध्ये आहेत, तरी ते Microsoft Olive मध्ये समाविष्ट केले गेले आहेत, आणि तुम्ही Microsoft Olive द्वारे onnxruntime साठी Generative AI विस्तार मॉडेल बिल्डर फंक्शन्स कॉल करू शकता.</ul>

## **Phi-3.5 चे क्वांटायझेशन करण्यासाठी मॉडेल बिल्डर कसा वापरावा**

मॉडेल बिल्डर आता Phi-3.5 Instruct आणि Phi-3.5-Vision साठी ONNX मॉडेल क्वांटायझेशन समर्थन करतो

### **Phi-3.5-Instruct**


**CPU-द्वारे जलद केलेले क्वांटाइझ्ड INT 4 रूपांतरण**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA-ने जलद केलेले क्वांटाइझ्ड INT 4 रूपांतरण**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. टर्मिनलमध्ये पर्यावरण सेट करा

```bash

mkdir models

cd models 

```

2. models फोल्डरमध्ये microsoft/Phi-3.5-vision-instruct डाउनलोड करा
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. कृपया ही फाइल्स आपल्या Phi-3.5-vision-instruct फोल्डरमध्ये डाउनलोड करा

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. ही फाइल models फोल्डरमध्ये डाउनलोड करा
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. टर्मिनलवर जा

    FP32 सह ONNX समर्थन रूपांतरण करा


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **टीप：**

1. मॉडेल बिल्डर सध्या Phi-3.5-Instruct आणि Phi-3.5-Vision चे रूपांतरण समर्थन करतो, परंतु Phi-3.5-MoE चे नाही

2. ONNX च्या क्वांटाइज्ड मॉडेलचा वापर Generative AI विस्तारांसह onnxruntime SDK द्वारे केला जाऊ शकतो

3. आम्हाला अधिक जबाबदार AI विचारात घ्यावा लागतो, म्हणून मॉडेल क्वांटायझेशन रूपांतरणानंतर अधिक प्रभावी परिणाम चाचणी करणे शिफारसीय आहे

4. CPU INT4 मॉडेल क्वांटायझेशन करून ते एज डिव्हाइसवर तैनात करू शकतो, ज्याचे अनुप्रयोग दृश्य चांगले आहेत. त्यामुळे Phi-3.5-Instruct जवळजवळ INT4 पर्यंत पूर्ण केले आहे


## **स्रोत**

1. onnxruntime साठी Generative AI विस्तारांविषयी अधिक जाणून घ्या [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. onnxruntime साठी Generative AI विस्तार GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->