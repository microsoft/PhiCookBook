<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-07-16T21:01:52+00:00",
  "source_file": "md/01.Introduction/03/MLX_Inference.md",
  "language_code": "hi"
}
-->
# **Apple MLX Framework के साथ Inference Phi-3**

## **MLX Framework क्या है**

MLX Apple सिलिकॉन पर मशीन लर्निंग रिसर्च के लिए एक एरे फ्रेमवर्क है, जिसे Apple मशीन लर्निंग रिसर्च द्वारा विकसित किया गया है।

MLX मशीन लर्निंग शोधकर्ताओं द्वारा मशीन लर्निंग शोधकर्ताओं के लिए डिज़ाइन किया गया है। यह फ्रेमवर्क उपयोगकर्ता के अनुकूल होने के साथ-साथ मॉडल को ट्रेन और डिप्लॉय करने में प्रभावी भी है। फ्रेमवर्क का डिज़ाइन भी अवधारणात्मक रूप से सरल है। हमारा उद्देश्य शोधकर्ताओं के लिए MLX को आसानी से बढ़ाने और सुधारने योग्य बनाना है ताकि वे नए विचारों का तेजी से अन्वेषण कर सकें।

Apple सिलिकॉन डिवाइसेज में MLX के माध्यम से LLMs को तेज़ किया जा सकता है, और मॉडल को स्थानीय रूप से बहुत आसानी से चलाया जा सकता है।

## **MLX का उपयोग करके Phi-3-mini का Inference करना**

### **1. अपना MLX पर्यावरण सेट करें**

1. Python 3.11.x
2. MLX लाइब्रेरी इंस्टॉल करें

```bash

pip install mlx-lm

```

### **2. टर्मिनल में MLX के साथ Phi-3-mini चलाना**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

परिणाम (मेरा पर्यावरण Apple M1 Max, 64GB है)

![Terminal](../../../../../translated_images/01.5cf57df8f7407cf9281c0237f4e69c3728b8817253aad0835d14108b07c83c88.hi.png)

### **3. टर्मिनल में MLX के साथ Phi-3-mini को Quantize करना**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** मॉडल को mlx_lm.convert के माध्यम से क्वांटाइज़ किया जा सकता है, और डिफ़ॉल्ट क्वांटाइज़ेशन INT4 है। इस उदाहरण में Phi-3-mini को INT4 में क्वांटाइज़ किया गया है।

मॉडल को mlx_lm.convert के जरिए क्वांटाइज़ किया जा सकता है, और डिफ़ॉल्ट क्वांटाइज़ेशन INT4 है। इस उदाहरण में Phi-3-mini को INT4 में क्वांटाइज़ किया गया है। क्वांटाइज़ेशन के बाद, यह डिफ़ॉल्ट डायरेक्टरी ./mlx_model में स्टोर होगा।

हम टर्मिनल से MLX के साथ क्वांटाइज़ किए गए मॉडल का परीक्षण कर सकते हैं।

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

परिणाम है

![INT4](../../../../../translated_images/02.7b188681a8eadbc111aba8d8006e4b3671788947a99a46329261e169dd2ec29f.hi.png)

### **4. Jupyter Notebook में MLX के साथ Phi-3-mini चलाना**

![Notebook](../../../../../translated_images/03.b9705a3a5aaa89f9eb0ca04c1a4565dfe4a5e8cc68604227d2eab149fef1d3c7.hi.png)

***Note:*** कृपया इस सैंपल को पढ़ें [click this link](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **संसाधन**

1. Apple MLX Framework के बारे में जानें [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।