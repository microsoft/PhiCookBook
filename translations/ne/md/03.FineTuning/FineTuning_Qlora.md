<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-09T21:51:34+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "ne"
}
-->
**Phi-3 लाई QLoRA सँग फाइन-ट्यून गर्ने**

Microsoft को Phi-3 Mini भाषा मोडललाई [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) प्रयोग गरेर फाइन-ट्यून गर्ने। 

QLoRA ले संवाद बुझ्न र प्रतिक्रिया सिर्जना गर्न सुधार गर्न मद्दत गर्नेछ। 

transformers र bitsandbytes प्रयोग गरेर 4bits मा मोडल लोड गर्न, तपाईंले accelerate र transformers लाई स्रोतबाट इन्स्टल गर्नुपर्नेछ र bitsandbytes पुस्तकालयको नयाँ संस्करण भएको सुनिश्चित गर्नुपर्नेछ।

**नमूनाहरू**
- [यस नमूना नोटबुकबाट थप जान्नुहोस्](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python फाइन-ट्यूनिङ नमूनाको उदाहरण](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub मा LORA सँग फाइन ट्यूनिङको उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Hub मा QLORA सँग फाइन ट्यूनिङको उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा गलतफहमी हुनसक्छ। मूल दस्तावेज यसको मूल भाषामा आधिकारिक स्रोतको रूपमा मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानवीय अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा व्याख्यामा हामी जिम्मेवार हुने छैनौं।