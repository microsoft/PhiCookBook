<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-08T06:10:45+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "hi"
}
-->
# **Apple MLX Framework का उपयोग करके Phi-3.5 का क्वांटाइजेशन**


MLX एक एरे फ्रेमवर्क है जो Apple सिलिकॉन पर मशीन लर्निंग रिसर्च के लिए बनाया गया है, और यह Apple मशीन लर्निंग रिसर्च द्वारा प्रस्तुत किया गया है।

MLX मशीन लर्निंग शोधकर्ताओं द्वारा मशीन लर्निंग शोधकर्ताओं के लिए डिजाइन किया गया है। यह फ्रेमवर्क उपयोग में आसान होने के साथ-साथ मॉडल को ट्रेन और डिप्लॉय करने में प्रभावी भी है। फ्रेमवर्क की डिज़ाइन भी अवधारणात्मक रूप से सरल है। हमारा उद्देश्य शोधकर्ताओं के लिए MLX को आसानी से एक्सटेंड और बेहतर बनाना है ताकि वे जल्दी से नए आइडियाज का पता लगा सकें।

Apple सिलिकॉन डिवाइसों में MLX के माध्यम से LLMs को तेज़ किया जा सकता है, और मॉडल को लोकल स्तर पर बहुत सुविधाजनक रूप से चलाया जा सकता है।

अब Apple MLX Framework Phi-3.5-Instruct (**Apple MLX Framework support**), Phi-3.5-Vision (**MLX-VLM Framework support**), और Phi-3.5-MoE (**Apple MLX Framework support**) के क्वांटाइजेशन कन्वर्ज़न को सपोर्ट करता है। आइए इसे अगली बार आज़माएं:

### **Phi-3.5-Instruct**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```


### **Phi-3.5-Vision**


```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```



### **🤖 Apple MLX के साथ Phi-3.5 के लिए सैंपल्स**

| Labs    | परिचय | जाएं |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Apple MLX फ्रेमवर्क के साथ Phi-3.5 Instruct का उपयोग कैसे करें सीखें   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Apple MLX फ्रेमवर्क के साथ Phi-3.5 Vision का उपयोग करके इमेज का विश्लेषण कैसे करें सीखें     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Apple MLX फ्रेमवर्क के साथ Phi-3.5 MoE का उपयोग कैसे करें सीखें  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |


## **संसाधन**

1. Apple MLX Framework के बारे में जानें [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub रिपॉजिटरी [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub रिपॉजिटरी [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।