<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-05-09T12:10:30+00:00",
  "source_file": "md/01.Introduction/03/MLX_Inference.md",
  "language_code": "mr"
}
-->
# **Inference Phi-3 with Apple MLX Framework**

## **MLX Framework काय आहे**

MLX हा Apple सिलिकॉनवर मशीन लर्निंग संशोधनासाठी तयार केलेला एक array framework आहे, जो Apple मशीन लर्निंग संशोधनाकडून आणला आहे.

MLX मशीन लर्निंग संशोधकांसाठी मशीन लर्निंग संशोधकांनी डिझाइन केलेला आहे. हा framework वापरायला सोपा असूनही मॉडेल्स ट्रेन आणि deploy करण्यासाठी कार्यक्षम आहे. framework चा डिझाइन सुद्धा संकल्पनात्मकदृष्ट्या सोपा आहे. आम्ही संशोधकांना MLX सहजपणे विस्तारण्यास आणि सुधारण्यास प्रोत्साहित करतो, ज्यामुळे नवीन कल्पना लवकर तपासता येतील.

LLMs Apple Silicon उपकरणांवर MLX च्या माध्यमातून जलद चालवता येतात आणि मॉडेल्स स्थानिकपणे सहज चालवता येतात.

## **MLX वापरून Phi-3-mini चे inference कसे करायचे**

### **1. तुमचे MLX पर्यावरण सेट करा**

1. Python 3.11.x
2. MLX Library इंस्टॉल करा

```bash

pip install mlx-lm

```

### **2. MLX सह Terminal मध्ये Phi-3-mini चालवा**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

परिणाम (माझे पर्यावरण Apple M1 Max, 64GB आहे) असा आहे

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.mr.png)

### **3. Terminal मध्ये MLX वापरून Phi-3-mini चे Quantize करा**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** मॉडेल mlx_lm.convert द्वारे quantize करू शकतो, आणि default quantization INT4 आहे. या उदाहरणात Phi-3-mini ला INT4 मध्ये quantize केले आहे.

मॉडेल mlx_lm.convert द्वारे quantize करता येतो, आणि default quantization INT4 आहे. या उदाहरणात Phi-3-mini ला INT4 मध्ये quantize केले आहे. Quantization नंतर, ते default directory ./mlx_model मध्ये साठवले जाईल.

आम्ही terminal मधून MLX वापरून quantized मॉडेल चाचणी करू शकतो

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

परिणाम असा आहे

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.mr.png)

### **4. Jupyter Notebook मध्ये MLX सह Phi-3-mini चालवा**

![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.mr.png)

***Note:*** कृपया हा sample वाचा [click this link](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **स्रोत**

1. Apple MLX Framework बद्दल जाणून घ्या [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अपूर्णता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करणे शिफारसीय आहे. या अनुवादाचा वापर केल्यामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीसाठी आम्ही जबाबदार नाही.