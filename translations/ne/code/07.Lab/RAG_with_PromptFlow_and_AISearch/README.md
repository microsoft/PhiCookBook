## RAG with PromptFlow र AISearch

यस उदाहरणमा, हामी Retrieval Augmented Generation (RAG) एप्लिकेशन कार्यान्वयन गर्नेछौं जसमा Phi3 लाई SLM को रूपमा, AI Search लाई vectorDB को रूपमा र Prompt Flow लाई low-code orchestrator को रूपमा प्रयोग गरिनेछ।

## सुविधाहरू

- Docker प्रयोग गरेर सजिलो डिप्लोयमेन्ट।
- AI वर्कफ्लोहरू सम्हाल्न सक्ने स्केलेबल आर्किटेक्चर।
- Prompt Flow प्रयोग गरेर कम कोड विधि।

## पूर्वआवश्यकताहरू

सुरु गर्नु अघि, तलका आवश्यकताहरू पूरा भएको सुनिश्चित गर्नुहोस्:

- तपाईंको स्थानीय मेसिनमा Docker इन्स्टल गरिएको छ।
- कन्टेनर स्रोतहरू सिर्जना र व्यवस्थापन गर्न अनुमति भएको Azure खाता।
- Azure AI Studio र Azure AI Search इन्स्टेन्सहरू।
- तपाईंको इन्डेक्स बनाउनको लागि एक embedding मोडेल (Azure OpenAI embedding वा क्याटलगबाट OS मोडेल हुन सक्छ)।
- तपाईंको स्थानीय मेसिनमा Python 3.8 वा पछि संस्करण इन्स्टल गरिएको छ।
- Azure Container Registry (वा तपाईंको रोजाइको कुनै पनि रजिस्ट्री)।

## इन्स्टलेशन

1. तपाईंको Azure AI Studio प्रोजेक्टमा flow.yaml फाइल प्रयोग गरेर नयाँ फ्लो सिर्जना गर्नुहोस्।
2. Azure AI मोडेल क्याटलगबाट Phi3 मोडेल डिप्लोय गर्नुहोस् र तपाईंको प्रोजेक्टसँग कनेक्शन बनाउनुहोस्। [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Azure AI Search मा तपाईंको रोजाइको कुनै पनि डकुमेन्ट प्रयोग गरेर भेक्टर इन्डेक्स सिर्जना गर्नुहोस्। [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. फ्लोलाई म्यानेज्ड एन्डपोइन्टमा डिप्लोय गर्नुहोस् र prompt-flow-frontend.py फाइलमा प्रयोग गर्नुहोस्। [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. रिपोजिटोरी क्लोन गर्नुहोस्:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Docker इमेज बनाउनुहोस्:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Docker इमेज Azure Container Registry मा पुश गर्नुहोस्:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## प्रयोग

1. Docker कन्टेनर चलाउनुहोस्:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. तपाईंको ब्राउजरमा `http://localhost:8501` मा एप्लिकेशन पहुँच गर्नुहोस्।

## सम्पर्क

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

पूर्ण लेख: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं भने पनि, कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।