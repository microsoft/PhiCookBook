<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-07-16T21:02:09+00:00",
  "source_file": "md/01.Introduction/03/MLX_Inference.md",
  "language_code": "mr"
}
-->
# **Apple MLX Framework सह Inference Phi-3**

## **MLX Framework म्हणजे काय**

MLX हा Apple सिलिकॉनवर मशीन लर्निंग संशोधनासाठी तयार केलेला एक array framework आहे, जो Apple मशीन लर्निंग संशोधनाद्वारे सादर केला आहे.

MLX मशीन लर्निंग संशोधकांसाठी मशीन लर्निंग संशोधकांनी डिझाइन केलेला आहे. हा framework वापरण्यास सोपा असला तरी मॉडेल्स ट्रेन आणि डिप्लॉय करण्यासाठी कार्यक्षम आहे. framework ची रचना संकल्पनात्मकदृष्ट्या सोपी आहे. आम्हाला संशोधकांसाठी MLX सहजपणे विस्तारण्यास आणि सुधारण्यास मदत करायची आहे, ज्यामुळे नवीन कल्पना लवकर तपासता येतील.

Apple सिलिकॉन डिव्हाइसेसवर MLX द्वारे LLMs जलद चालवता येतात आणि मॉडेल्स स्थानिक पातळीवर सहजपणे रन करता येतात.

## **Phi-3-mini चे MLX वापरून Inference करणे**

### **1. तुमचे MLX पर्यावरण सेट करा**

1. Python 3.11.x
2. MLX लायब्ररी इन्स्टॉल करा


```bash

pip install mlx-lm

```

### **2. MLX सह Terminal मध्ये Phi-3-mini चालवा**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

परिणाम (माझे पर्यावरण Apple M1 Max, 64GB आहे) असा आहे

![Terminal](../../../../../translated_images/mr/01.5cf57df8f7407cf9.png)

### **3. Terminal मध्ये MLX वापरून Phi-3-mini चे Quantization करा**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** मॉडेल mlx_lm.convert द्वारे quantize करता येते, आणि डीफॉल्ट quantization INT4 आहे. या उदाहरणात Phi-3-mini ला INT4 मध्ये quantize केले आहे.

मॉडेल mlx_lm.convert द्वारे quantize करता येते, आणि डीफॉल्ट quantization INT4 आहे. या उदाहरणात Phi-3-mini ला INT4 मध्ये quantize केले आहे. Quantization नंतर, ते डीफॉल्ट डायरेक्टरी ./mlx_model मध्ये साठवले जाईल.

आम्ही टर्मिनलमधून MLX वापरून quantized मॉडेलची चाचणी करू शकतो


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

परिणाम असा आहे

![INT4](../../../../../translated_images/mr/02.7b188681a8eadbc1.png)


### **4. Jupyter Notebook मध्ये MLX सह Phi-3-mini चालवा**


![Notebook](../../../../../translated_images/mr/03.b9705a3a5aaa89f9.png)

***Note:*** कृपया हा sample वाचा [click this link](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **संसाधने**

1. Apple MLX Framework बद्दल जाणून घ्या [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.