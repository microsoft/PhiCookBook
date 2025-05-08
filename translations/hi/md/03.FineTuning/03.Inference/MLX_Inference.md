<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-05-08T05:25:16+00:00",
  "source_file": "md/03.FineTuning/03.Inference/MLX_Inference.md",
  "language_code": "hi"
}
-->
# **Inference Phi-3 with Apple MLX Framework**

## **MLX Framework क्या है**

MLX Apple सिलिकॉन पर मशीन लर्निंग रिसर्च के लिए एक array framework है, जिसे Apple मशीन लर्निंग रिसर्च द्वारा बनाया गया है।

MLX मशीन लर्निंग शोधकर्ताओं के लिए मशीन लर्निंग शोधकर्ताओं द्वारा डिजाइन किया गया है। यह framework यूजर-फ्रेंडली होने के साथ-साथ मॉडल को ट्रेन और डिप्लॉय करने में भी प्रभावी है। framework का डिज़ाइन भी कॉन्सेप्चुअली सरल है। हमारा उद्देश्य शोधकर्ताओं के लिए MLX को आसानी से एक्सटेंड और सुधारना है ताकि वे नए आइडियाज को जल्दी से एक्सप्लोर कर सकें।

Apple सिलिकॉन डिवाइसेस में LLMs को MLX के माध्यम से तेज़ किया जा सकता है, और मॉडल्स को लोकली बहुत ही आसानी से चलाया जा सकता है।

## **Phi-3-mini को MLX से इन्फरेंस करना**

### **1. अपना MLX एन्वायरनमेंट सेट करें**

1. Python 3.11.x
2. MLX लाइब्रेरी इंस्टॉल करें

```bash

pip install mlx-lm

```

### **2. MLX के साथ टर्मिनल में Phi-3-mini चलाना**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

परिणाम (मेरा एन्वायरनमेंट Apple M1 Max, 64GB है)

![Terminal](../../../../../translated_images/01.5cf57df8f7407cf9281c0237f4e69c3728b8817253aad0835d14108b07c83c88.hi.png)

### **3. टर्मिनल में MLX के साथ Phi-3-mini का क्वांटाइजेशन करना**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** मॉडल को mlx_lm.convert के माध्यम से क्वांटाइज़ किया जा सकता है, और डिफ़ॉल्ट क्वांटाइजेशन INT4 होता है। इस उदाहरण में Phi-3-mini को INT4 में क्वांटाइज़ किया गया है।

मॉडल mlx_lm.convert के जरिए क्वांटाइज़ किया जा सकता है, और डिफ़ॉल्ट क्वांटाइजेशन INT4 है। इस उदाहरण में Phi-3-mini को INT4 में क्वांटाइज़ किया गया है। क्वांटाइजेशन के बाद, यह डिफ़ॉल्ट डायरेक्टरी ./mlx_model में स्टोर होगा।

हम टर्मिनल से MLX के साथ क्वांटाइज़्ड मॉडल को टेस्ट कर सकते हैं

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
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान रखें कि स्वचालित अनुवादों में त्रुटियाँ या असंगतियाँ हो सकती हैं। मूल दस्तावेज़ उसकी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।