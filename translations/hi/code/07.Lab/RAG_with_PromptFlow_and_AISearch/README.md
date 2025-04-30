<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "962051ba495487884232e77fda80027f",
  "translation_date": "2025-04-04T17:23:11+00:00",
  "source_file": "code\\07.Lab\\RAG_with_PromptFlow_and_AISearch\\README.md",
  "language_code": "hi"
}
-->
## PromptFlow और AISearch के साथ RAG

इस उदाहरण में, हम Retrieval Augmented Generation (RAG) एप्लिकेशन को लागू करेंगे, जिसमें Phi3 को SLM, AI Search को vectorDB और Prompt Flow को लो-कोड ऑर्केस्ट्रेटर के रूप में उपयोग किया जाएगा।

## विशेषताएं

- Docker का उपयोग करके आसान डिप्लॉयमेंट।
- AI वर्कफ्लो को संभालने के लिए स्केलेबल आर्किटेक्चर।
- Prompt Flow का उपयोग करते हुए लो-कोड दृष्टिकोण।

## पूर्व आवश्यकताएं

शुरू करने से पहले, सुनिश्चित करें कि आपने निम्नलिखित आवश्यकताओं को पूरा कर लिया है:

- आपके लोकल मशीन पर Docker इंस्टॉल हो।
- एक Azure खाता, जिसमें कंटेनर संसाधनों को बनाने और प्रबंधित करने की अनुमति हो।
- Azure AI Studio और Azure AI Search की इंस्टेंस।
- इंडेक्स बनाने के लिए एक एम्बेडिंग मॉडल (यह Azure OpenAI एम्बेडिंग या कैटलॉग से कोई भी ओपन-सोर्स मॉडल हो सकता है)।
- आपके लोकल मशीन पर Python 3.8 या उससे बाद का संस्करण इंस्टॉल हो।
- Azure Container Registry (या आपकी पसंद का कोई भी रजिस्ट्री)।

## इंस्टॉलेशन

1. अपने Azure AI Studio प्रोजेक्ट पर flow.yaml फ़ाइल का उपयोग करके एक नया फ्लो बनाएं।
2. Azure AI मॉडल कैटलॉग से Phi3 मॉडल को डिप्लॉय करें और अपने प्रोजेक्ट से कनेक्शन बनाएं। [Phi-3 को Model as a Service के रूप में डिप्लॉय करें](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. अपनी पसंद के किसी भी दस्तावेज़ का उपयोग करके Azure AI Search पर एक वेक्टर इंडेक्स बनाएं। [Azure AI Search पर वेक्टर इंडेक्स बनाएं](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. फ्लो को एक मैनेज्ड एंडपॉइंट पर डिप्लॉय करें और इसे prompt-flow-frontend.py फ़ाइल में उपयोग करें। [ऑनलाइन एंडपॉइंट पर फ्लो डिप्लॉय करें](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. रिपॉजिटरी को क्लोन करें:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Docker इमेज बनाएं:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Docker इमेज को Azure Container Registry में पुश करें:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## उपयोग

1. Docker कंटेनर चलाएं:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. अपने ब्राउज़र में एप्लिकेशन को `http://localhost:8501` पर एक्सेस करें।

## संपर्क

वेलेंटीना आल्टो - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

पूरा लेख: [Azure Model Catalog से Phi-3-Medium को Model as a Service के रूप में उपयोग करके RAG](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।