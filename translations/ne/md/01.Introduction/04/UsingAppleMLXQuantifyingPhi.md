<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-09T13:42:05+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "ne"
}
-->
# **Apple MLX Framework प्रयोग गरेर Phi-3.5 क्वान्टाइजेशन**

MLX एप्पल सिलिकनमा मेशिन लर्निङ अनुसन्धानका लागि बनाइएको एरे फ्रेमवर्क हो, जुन एप्पल मेशिन लर्निङ अनुसन्धान टोलीले प्रस्तुत गरेको हो।

MLX मेशिन लर्निङ अनुसन्धानकर्ताहरूका लागि मेशिन लर्निङ अनुसन्धानकर्ताहरूले डिजाइन गरेको हो। यो फ्रेमवर्क प्रयोग गर्न सजिलो बनाउन लक्षित छ, तर मोडेलहरू प्रशिक्षण र डिप्लोय गर्न अझै पनि प्रभावकारी छ। फ्रेमवर्कको डिजाइन पनि अवधारणात्मक रूपमा सरल छ। हामी अनुसन्धानकर्ताहरूलाई नयाँ विचारहरू छिटो अन्वेषण गर्न MLX लाई विस्तार र सुधार गर्न सजिलो बनाउने उद्देश्य राख्छौं।

एप्पल सिलिकन उपकरणहरूमा LLMs MLX मार्फत छिटो चलाउन सकिन्छ, र मोडेलहरू स्थानीय रूपमा सहजै चलाउन सकिन्छ।

अब Apple MLX Framework ले Phi-3.5-Instruct(**Apple MLX Framework support**), Phi-3.5-Vision(**MLX-VLM Framework support**), र Phi-3.5-MoE(**Apple MLX Framework support**) को क्वान्टाइजेसन रूपान्तरण समर्थन गर्दछ। अब यसलाई प्रयास गरौं:

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



### **🤖 Apple MLX सँग Phi-3.5 का नमूना**

| Labs    | परिचय | जानुहोस् |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Apple MLX फ्रेमवर्कसहित Phi-3.5 Instruct कसरी प्रयोग गर्ने सिक्नुहोस्   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Apple MLX फ्रेमवर्कसहित Phi-3.5 Vision प्रयोग गरी छवि विश्लेषण कसरी गर्ने सिक्नुहोस्     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Apple MLX फ्रेमवर्कसहित Phi-3.5 MoE कसरी प्रयोग गर्ने सिक्नुहोस्  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |


## **स्रोतहरू**

1. Apple MLX Framework बारे जान्नुहोस् [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub रिपो [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub रिपो [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया जान्नुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज़लाई यसको मूल भाषामा अधिकारिक स्रोतको रूपमा मान्नुपर्छ। महत्वपूर्ण जानकारीका लागि पेशेवर मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा व्याख्यामा हामी जिम्मेवार छैनौं।