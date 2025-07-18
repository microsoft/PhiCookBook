<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-07-16T21:54:12+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "ne"
}
-->
# **Apple MLX Framework प्रयोग गरी Phi-3.5 को क्वान्टाइजेशन**

MLX भनेको Apple सिलिकनमा मेसिन लर्निङ अनुसन्धानका लागि बनाइएको एरे फ्रेमवर्क हो, जुन Apple मेसिन लर्निङ अनुसन्धान टोलीले ल्याएको हो।

MLX मेसिन लर्निङ अनुसन्धानकर्ताहरूका लागि मेसिन लर्निङ अनुसन्धानकर्ताहरूले डिजाइन गरेको हो। यो फ्रेमवर्क प्रयोगकर्तामैत्री हुन डिजाइन गरिएको छ, तर मोडेलहरू छिटो प्रशिक्षण र डिप्लोय गर्न सक्षम पनि छ। फ्रेमवर्कको डिजाइन पनि अवधारणात्मक रूपमा सरल छ। हामी अनुसन्धानकर्ताहरूलाई MLX लाई सजिलै विस्तार र सुधार गर्न सकून् भनेर बनाउने लक्ष्य राख्छौं, जसले नयाँ विचारहरू छिटो अन्वेषण गर्न मद्दत गर्छ।

Apple सिलिकन उपकरणहरूमा MLX मार्फत LLMs लाई छिटो चलाउन सकिन्छ, र मोडेलहरू स्थानीय रूपमा सजिलै चलाउन सकिन्छ।

अब Apple MLX Framework ले Phi-3.5-Instruct(**Apple MLX Framework support**), Phi-3.5-Vision(**MLX-VLM Framework support**), र Phi-3.5-MoE(**Apple MLX Framework support**) को क्वान्टाइजेशन रूपान्तरणलाई समर्थन गर्दछ। अब यसलाई प्रयास गरौं:

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

### **🤖 Apple MLX सँग Phi-3.5 का नमूनाहरू**

| ल्याबहरू    | परिचय | जानुहोस् |
| -------- | ------- |  ------- |
| 🚀 ल्याब-परिचय Phi-3.5 Instruct  | Apple MLX फ्रेमवर्कसँग Phi-3.5 Instruct कसरी प्रयोग गर्ने सिक्नुहोस्   |  [जानुहोस्](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 ल्याब-परिचय Phi-3.5 Vision (छवि) | Apple MLX फ्रेमवर्कसँग Phi-3.5 Vision प्रयोग गरी छवि विश्लेषण कसरी गर्ने सिक्नुहोस्     |  [जानुहोस्](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 ल्याब-परिचय Phi-3.5 Vision (moE)   | Apple MLX फ्रेमवर्कसँग Phi-3.5 MoE कसरी प्रयोग गर्ने सिक्नुहोस्  |  [जानुहोस्](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **स्रोतहरू**

1. Apple MLX Framework को बारेमा जान्नुहोस् [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub रिपोजिटरी [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub रिपोजिटरी [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।