# **Apple MLX Framework सँग Phi-3 को इन्फरेन्स**

## **MLX Framework के हो**

MLX Apple सिलिकनमा मेशिन लर्निङ अनुसन्धानका लागि बनेको एक एरे फ्रेमवर्क हो, जुन Apple मेशिन लर्निङ अनुसन्धान टोलीले विकास गरेको हो।

MLX मेशिन लर्निङ अनुसन्धानकर्ताहरूका लागि डिजाइन गरिएको हो। यो फ्रेमवर्क प्रयोगकर्तामैत्री छ, तर मोडेलहरूलाई छिटो प्रशिक्षण र डिप्लोय गर्न सक्षम छ। फ्रेमवर्कको डिजाइन पनि अवधारणात्मक रूपमा सरल छ। हामी अनुसन्धानकर्ताहरूलाई MLX लाई सजिलै विस्तार र सुधार गर्न सकून् भनेर बनाउने लक्ष्य राख्छौं, जसले नयाँ विचारहरू छिटो अन्वेषण गर्न मद्दत गर्छ।

Apple सिलिकन उपकरणहरूमा MLX मार्फत LLMs लाई छिटो चलाउन सकिन्छ, र मोडेलहरू स्थानीय रूपमा सजिलै चलाउन सकिन्छ।

## **MLX प्रयोग गरेर Phi-3-mini को इन्फरेन्स गर्ने तरिका**

### **1. आफ्नो MLX वातावरण सेटअप गर्नुहोस्**

1. Python 3.11.x
2. MLX लाइब्रेरी इन्स्टल गर्नुहोस्

```bash

pip install mlx-lm

```

### **2. MLX सँग टर्मिनलमा Phi-3-mini चलाउने**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

परिणाम (मेरो वातावरण Apple M1 Max, 64GB छ) यस्तो छ

![Terminal](../../../../../translated_images/ne/01.5cf57df8f7407cf9.webp)

### **3. MLX सँग टर्मिनलमा Phi-3-mini को क्वान्टाइजेसन गर्ने**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** मोडेल mlx_lm.convert मार्फत क्वान्टाइज गर्न सकिन्छ, र डिफल्ट क्वान्टाइजेसन INT4 हो। यो उदाहरणमा Phi-3-mini लाई INT4 मा क्वान्टाइज गरिएको छ।

मोडेल mlx_lm.convert मार्फत क्वान्टाइज गर्न सकिन्छ, र डिफल्ट क्वान्टाइजेसन INT4 हो। यो उदाहरण Phi-3-mini लाई INT4 मा क्वान्टाइज गर्ने हो। क्वान्टाइज गरेपछि, यो डिफल्ट डाइरेक्टरी ./mlx_model मा सुरक्षित हुन्छ।

हामी टर्मिनलबाट MLX सँग क्वान्टाइज गरिएको मोडेल परीक्षण गर्न सक्छौं।

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

परिणाम यस्तो छ

![INT4](../../../../../translated_images/ne/02.7b188681a8eadbc1.webp)

### **4. MLX सँग Jupyter Notebook मा Phi-3-mini चलाउने**

![Notebook](../../../../../translated_images/ne/03.b9705a3a5aaa89f9.webp)

***Note:*** कृपया यो नमुना पढ्नुहोस् [click this link](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **स्रोतहरू**

1. Apple MLX Framework को बारेमा जान्न [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा आधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।