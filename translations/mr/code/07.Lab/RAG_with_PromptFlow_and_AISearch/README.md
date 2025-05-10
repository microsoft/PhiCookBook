<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-05-09T05:11:22+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "mr"
}
-->
## RAG with PromptFlow आणि AISearch

या उदाहरणात, आपण Retrieval Augmented Generation (RAG) ऍप्लिकेशन तयार करू ज्यामध्ये Phi3 SLM म्हणून, AI Search vectorDB म्हणून आणि Prompt Flow low-code ऑर्केस्ट्रेटर म्हणून वापरले जाईल.

## वैशिष्ट्ये

- Docker वापरून सोपी तैनाती.
- AI वर्कफ्लो हाताळण्यासाठी स्केलेबल आर्किटेक्चर.
- Prompt Flow वापरून कमी कोड दृष्टिकोन.

## पूर्वअट

सुरू करण्यापूर्वी, खालील आवश्यकतांची खात्री करा:

- तुमच्या स्थानिक मशीनवर Docker इन्स्टॉल केलेले आहे.
- कंटेनर संसाधने तयार करण्यासाठी आणि व्यवस्थापित करण्यासाठी परवानग्या असलेले Azure खाते.
- Azure AI Studio आणि Azure AI Search इंस्टन्सेस.
- तुमचा निर्देशांक तयार करण्यासाठी embedding मॉडेल (Azure OpenAI embedding किंवा कॅटलॉगमधील कोणताही OS मॉडेल असू शकतो).
- Python 3.8 किंवा नंतरची आवृत्ती तुमच्या स्थानिक मशीनवर इन्स्टॉल केलेली आहे.
- Azure Container Registry (किंवा तुमच्या पसंतीचा कोणताही रजिस्ट्री).

## इंस्टॉलेशन

1. flow.yaml फाइल वापरून तुमच्या Azure AI Studio प्रोजेक्टमध्ये नवीन flow तयार करा.
2. Azure AI मॉडेल कॅटलॉगमधून Phi3 मॉडेल डिप्लॉय करा आणि तुमच्या प्रोजेक्टशी कनेक्शन तयार करा. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. तुमच्या पसंतीच्या कोणत्याही दस्तऐवजाचा वापर करून Azure AI Search वर vector index तयार करा. [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. managed endpoint वर flow डिप्लॉय करा आणि prompt-flow-frontend.py फाइलमध्ये वापरा. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. रिपॉझिटरी क्लोन करा:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Docker इमेज बिल्ड करा:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Docker इमेज Azure Container Registry मध्ये पुश करा:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## वापर

1. Docker कंटेनर चालवा:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. तुमच्या ब्राउझरमध्ये `http://localhost:8501` या पत्त्यावर ऍप्लिकेशन वापरा.

## संपर्क

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

पूर्ण लेख: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाच्या माहितीकरिता व्यावसायिक मानवी अनुवाद शिफारसीय आहे. या अनुवादाचा वापर करून झालेल्या कोणत्याही गैरसमजुतीसाठी किंवा चुकीच्या अर्थ लावण्यासाठी आम्ही जबाबदार नाही.