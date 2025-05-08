<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-05-08T06:42:32+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "hi"
}
-->
## RAG with PromptFlow and AISearch

इस उदाहरण में, हम Retrieval Augmented Generation (RAG) एप्लिकेशन को Phi3 को SLM के रूप में, AI Search को vectorDB के रूप में और Prompt Flow को low-code ऑर्केस्ट्रेटर के रूप में उपयोग करके लागू करेंगे।

## Features

- Docker का उपयोग करके आसान डिप्लॉयमेंट।
- AI वर्कफ़्लोज़ को संभालने के लिए स्केलेबल आर्किटेक्चर।
- Prompt Flow का उपयोग करते हुए लो कोड अप्रोच।

## Prerequisites

शुरू करने से पहले, सुनिश्चित करें कि आपने निम्नलिखित आवश्यकताएँ पूरी कर ली हैं:

- आपके लोकल मशीन पर Docker इंस्टॉल हो।
- कंटेनर संसाधन बनाने और प्रबंधित करने के लिए अनुमति के साथ Azure अकाउंट।
- Azure AI Studio और Azure AI Search इंस्टेंस।
- अपना इंडेक्स बनाने के लिए एक एम्बेडिंग मॉडल (यह Azure OpenAI एम्बेडिंग या कैटलॉग से कोई OS मॉडल हो सकता है)।
- आपके लोकल मशीन पर Python 3.8 या उससे ऊपर इंस्टॉल हो।
- Azure Container Registry (या आपकी पसंद का कोई भी रजिस्ट्री)।

## Installation

1. अपने Azure AI Studio प्रोजेक्ट में flow.yaml फ़ाइल का उपयोग करके नया फ्लो बनाएं।
2. अपने Azure AI मॉडल कैटलॉग से एक Phi3 मॉडल डिप्लॉय करें और अपने प्रोजेक्ट से कनेक्शन बनाएं। [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. अपनी पसंद के किसी भी दस्तावेज़ का उपयोग करके Azure AI Search पर वेक्टर इंडेक्स बनाएं। [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. मैनेज्ड एंडपॉइंट पर फ्लो डिप्लॉय करें और prompt-flow-frontend.py फ़ाइल में इसका उपयोग करें। [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. रिपॉजिटरी क्लोन करें:

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

## Usage

1. Docker कंटेनर चलाएं:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. अपने ब्राउज़र में `http://localhost:8501` पर एप्लिकेशन एक्सेस करें।

## Contact

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

पूर्ण लेख: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या असंगतियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।