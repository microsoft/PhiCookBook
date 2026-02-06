## RAG with PromptFlow and AISearch

या उदाहरणात, आपण Retrieval Augmented Generation (RAG) अॅप्लिकेशन तयार करू ज्यामध्ये Phi3 SLM म्हणून, AI Search व्हेक्टरDB म्हणून आणि Prompt Flow लो-कोड ऑर्केस्ट्रेटर म्हणून वापरले जाईल.

## वैशिष्ट्ये

- Docker वापरून सोपी तैनाती.
- AI वर्कफ्लो हाताळण्यासाठी स्केलेबल आर्किटेक्चर.
- Prompt Flow वापरून लो-कोड पद्धत.

## पूर्वअट

सुरू करण्यापूर्वी, खालील अटी पूर्ण झाल्या आहेत याची खात्री करा:

- तुमच्या स्थानिक मशीनवर Docker स्थापित आहे.
- कंटेनर संसाधने तयार आणि व्यवस्थापित करण्यासाठी परवानग्या असलेले Azure खाते.
- Azure AI Studio आणि Azure AI Search इंस्टन्सेस.
- तुमचा निर्देशांक तयार करण्यासाठी एम्बेडिंग मॉडेल (हे Azure OpenAI एम्बेडिंग किंवा कॅटलॉगमधील OS मॉडेल असू शकते).
- तुमच्या स्थानिक मशीनवर Python 3.8 किंवा नंतरची आवृत्ती स्थापित आहे.
- Azure Container Registry (किंवा तुमच्या पसंतीचा कोणताही रजिस्ट्री).

## स्थापना

1. flow.yaml फाइल वापरून तुमच्या Azure AI Studio प्रोजेक्टवर नवीन फ्लो तयार करा.
2. Azure AI मॉडेल कॅटलॉगमधून Phi3 मॉडेल तैनात करा आणि तुमच्या प्रोजेक्टशी कनेक्शन तयार करा. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Azure AI Search वर तुमच्या पसंतीच्या कोणत्याही दस्तऐवजाचा वापर करून व्हेक्टर निर्देशांक तयार करा. [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. फ्लो मॅनेज्ड एन्डपॉइंटवर तैनात करा आणि prompt-flow-frontend.py फाइलमध्ये वापरा. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. रेपॉजिटरी क्लोन करा:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Docker इमेज तयार करा:

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

2. तुमच्या ब्राउझरमध्ये `http://localhost:8501` येथे अॅप्लिकेशन वापरा.

## संपर्क

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

पूर्ण लेख: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.