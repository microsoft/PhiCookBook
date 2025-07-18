<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:18:05+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "ne"
}
-->
**QLoRA सँग Phi-3 को फाइन-ट्यूनिङ**

Microsoft को Phi-3 Mini भाषा मोडेललाई [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) प्रयोग गरेर फाइन-ट्यून गर्ने।

QLoRA ले संवाद बुझाइ र प्रतिक्रिया उत्पादन सुधार गर्न मद्दत गर्नेछ।

transformers र bitsandbytes सँग 4bits मा मोडेलहरू लोड गर्न, तपाईंले accelerate र transformers लाई स्रोतबाट इन्स्टल गर्नुपर्छ र bitsandbytes लाइब्रेरीको सबैभन्दा नयाँ संस्करण भएको सुनिश्चित गर्नुपर्छ।

**नमूनाहरू**
- [यस नमूना नोटबुकसँग थप जान्नुहोस्](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python फाइनट्यूनिङ नमूनाको उदाहरण](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub मा LORA सँग फाइन ट्यूनिङको उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Hub मा QLORA सँग फाइन ट्यूनिङको उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।