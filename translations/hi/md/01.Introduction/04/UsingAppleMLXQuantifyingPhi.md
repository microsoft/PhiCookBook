<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "340bd4c009524ef84102b78d06eea735",
  "translation_date": "2025-04-04T17:57:25+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingAppleMLXQuantifyingPhi.md",
  "language_code": "hi"
}
-->
# **Apple MLX फ्रेमवर्क का उपयोग करके Phi-3.5 का क्वांटाइजेशन**

MLX Apple सिलिकॉन पर मशीन लर्निंग अनुसंधान के लिए एक एरे फ्रेमवर्क है, जिसे Apple मशीन लर्निंग अनुसंधान टीम द्वारा विकसित किया गया है।

MLX मशीन लर्निंग शोधकर्ताओं द्वारा मशीन लर्निंग शोधकर्ताओं के लिए डिज़ाइन किया गया है। यह फ्रेमवर्क उपयोगकर्ता के लिए आसान होने के साथ-साथ मॉडल को प्रशिक्षित और लागू करने में प्रभावी भी है। फ्रेमवर्क का डिज़ाइन भी अवधारणात्मक रूप से सरल है। हमारा उद्देश्य शोधकर्ताओं के लिए MLX को विस्तार और सुधारने में मदद करना है ताकि वे नई विचारों को जल्दी से खोज सकें।

Apple सिलिकॉन डिवाइसों में MLX के माध्यम से LLMs को तेज़ किया जा सकता है, और मॉडल को स्थानीय रूप से बहुत आसानी से चलाया जा सकता है।

अब Apple MLX फ्रेमवर्क Phi-3.5-Instruct (**Apple MLX फ्रेमवर्क सपोर्ट**), Phi-3.5-Vision (**MLX-VLM फ्रेमवर्क सपोर्ट**) और Phi-3.5-MoE (**Apple MLX फ्रेमवर्क सपोर्ट**) के क्वांटाइजेशन कन्वर्ज़न को सपोर्ट करता है। आइए इसे आज़माएं:

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

### **🤖 Apple MLX के साथ Phi-3.5 के सैंपल**

| लैब्स    | परिचय | जाएं |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Apple MLX फ्रेमवर्क के साथ Phi-3.5 Instruct का उपयोग करना सीखें   |  [जाएं](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Apple MLX फ्रेमवर्क के साथ इमेज का विश्लेषण करने के लिए Phi-3.5 Vision का उपयोग करना सीखें     |  [जाएं](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Apple MLX फ्रेमवर्क के साथ Phi-3.5 MoE का उपयोग करना सीखें  |  [जाएं](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **संसाधन**

1. Apple MLX फ्रेमवर्क के बारे में जानें [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub रिपॉजिटरी [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub रिपॉजिटरी [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में मौजूद मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।