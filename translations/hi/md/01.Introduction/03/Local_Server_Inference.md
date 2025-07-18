<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-07-16T20:56:10+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "hi"
}
-->
# **लोकल सर्वर में Inference Phi-3**

हम Phi-3 को लोकल सर्वर पर डिप्लॉय कर सकते हैं। उपयोगकर्ता [Ollama](https://ollama.com) या [LM Studio](https://llamaedge.com) समाधान चुन सकते हैं, या वे अपना खुद का कोड लिख सकते हैं। आप Phi-3 की लोकल सेवाओं को [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) या [Langchain](https://www.langchain.com/) के माध्यम से कनेक्ट कर सकते हैं ताकि Copilot एप्लिकेशन बनाए जा सकें।

## **Phi-3-mini तक पहुँचने के लिए Semantic Kernel का उपयोग करें**

Copilot एप्लिकेशन में, हम Semantic Kernel / LangChain के माध्यम से एप्लिकेशन बनाते हैं। इस प्रकार का एप्लिकेशन फ्रेमवर्क आमतौर पर Azure OpenAI Service / OpenAI मॉडल्स के साथ संगत होता है, और यह Hugging Face पर उपलब्ध ओपन सोर्स मॉडल्स और लोकल मॉडल्स को भी सपोर्ट कर सकता है। अगर हम Semantic Kernel का उपयोग करके Phi-3-mini तक पहुँचना चाहते हैं तो हमें क्या करना चाहिए? .NET को उदाहरण के तौर पर लेते हुए, हम इसे Semantic Kernel में Hugging Face Connector के साथ जोड़ सकते हैं। डिफ़ॉल्ट रूप से, यह Hugging Face पर मॉडल आईडी के अनुरूप होता है (पहली बार उपयोग करने पर, मॉडल Hugging Face से डाउनलोड होगा, जिसमें काफी समय लग सकता है)। आप लोकल सर्विस से भी कनेक्ट कर सकते हैं जो आपने खुद बनाई है। इन दोनों में से, हम बाद वाले का उपयोग करने की सलाह देते हैं क्योंकि इसमें स्वायत्तता का स्तर अधिक होता है, खासकर एंटरप्राइज एप्लिकेशन में।

![sk](../../../../../translated_images/sk.d03785c25edc6d445a2e9ae037979e544e0b0c482f43c7617b0324e717b9af62.hi.png)

चित्र से पता चलता है कि Semantic Kernel के माध्यम से लोकल सेवाओं तक पहुँचना आसानी से स्वनिर्मित Phi-3-mini मॉडल सर्वर से कनेक्ट हो सकता है। यहाँ इसका रनिंग परिणाम है।

![skrun](../../../../../translated_images/skrun.5aafc1e7197dca2020eefcaeaaee184d29bb0cf1c37b00fd9c79acc23a6dc8d2.hi.png)

***Sample Code*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।