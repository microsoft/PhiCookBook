<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:17:43+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "hi"
}
-->
**QLoRA के साथ Phi-3 का फाइन-ट्यूनिंग**

Microsoft के Phi-3 Mini भाषा मॉडल को [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) का उपयोग करके फाइन-ट्यून करना।

QLoRA संवाद की समझ और प्रतिक्रिया उत्पन्न करने में सुधार करने में मदद करेगा।

transformers और bitsandbytes के साथ 4bits में मॉडल लोड करने के लिए, आपको accelerate और transformers को स्रोत से इंस्टॉल करना होगा और यह सुनिश्चित करना होगा कि आपके पास bitsandbytes लाइब्रेरी का नवीनतम संस्करण हो।

**नमूने**
- [इस सैंपल नोटबुक के साथ और जानें](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python फाइनट्यूनिंग सैंपल का उदाहरण](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub पर LORA के साथ फाइन ट्यूनिंग का उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Hub पर QLORA के साथ फाइन ट्यूनिंग का उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।