## PromptFlow మరియు AISearch తో RAG

ఈ ఉదాహరణలో, మేము Retrieval Augmented Generation (RAG) అప్లికేషన్‌ను అమలు చేస్తాము, ఇందులో Phi3 ను SLM గా, AI Search ను vectorDB గా మరియు Prompt Flow ను low-code ఆర్కెస్ట్రేటర్ గా ఉపయోగిస్తాము.

## లక్షణాలు

- Docker ఉపయోగించి సులభంగా డిప్లాయ్ చేయగలదు.
- AI వర్క్‌ఫ్లోలను నిర్వహించడానికి స్కేలబుల్ ఆర్కిటెక్చర్.
- Prompt Flow ఉపయోగించే తక్కువ కోడ్ దృష్టికోణం

## ముందు అవసరాలు

ప్రారంభించే ముందు, మీరు క్రింది అవసరాలను తీర్చినట్లునో చూసుకోండి:

- మీ స్థానిక యంత్రంలో Docker ఇన్‌స్టాల్ చేయబడాలి.
- కంటైనర్ వనరులను సృష్టించడానికి మరియు నిర్వహించడానికి అనుమతులతో కూడిన Azure ఖాతా.
- ఒక Azure AI Studio మరియు Azure AI Search ఉదాహరణలు
- మీ సూచికను సృష్టించడానికి ఒక embedding మోడల్ (ఇది Azure OpenAI embedding లేదా కాటలాగ్ నుండి ఒక OS మోడల్ కావచ్చు)
- మీ స్థానిక యంత్రంలో Python 3.8 లేదా అంతకంటే వచ్చే వెర్షన్ ఇన్‌స్టాల్ చేయబడాలి.
- ఒక Azure Container Registry (లేదా మీ ఇష్టమైన ఏదైనా రిజిస్ట్రీ)

## ఇన్‌స్టాలేషన్

1. మీ Azure AI Studio Projectలో flow.yaml ఫైల్ ఉపయోగించి కొత్త flow సృష్టించండి.
2. Azure AI మోడల్ కాటలాగ్ నుండి Phi3 మోడల్‌ను డిప్లాయ్ చేసి మీ ప్రాజెక్టుకు కనెక్షన్‌ను సృష్టించండి. [Phi-3 ను Model as a Service గా డిప్లాయ్ చేయండి](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. మీకు ఇష్టమైన ఏదైనా డాక్యుమెంట్ ఉపయోగించి Azure AI Search పై వెక్టర్ సూచికను రూపొందించండి [Azure AI Search పై వెక్టర్ సూచికను oluşturించండి](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. మేనేజ్ చేయబడే endpoint పై flow ను డిప్లాయ్ చేసి దాన్ని prompt-flow-frontend.py ఫైల్‌లో ఉపయోగించండి. [ఆన్లైన్ endpoint పై flow ను డిప్లాయ్ చేయండి](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. రిపాజిటరీని క్లోన్ చేయండి:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Docker ఇమేజ్‌ను బిల్డ్ చేయండి:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Docker ఇమేజ్‌ను Azure Container Registry కు పుష్ చేయండి:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## ఉపయోగం

1. Docker కంటైనర్‌ను రన్ చేయండి:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. మీ బ్రౌజర్‌లో అప్లికేషన్‌ను ఈ అడ్రస్‌లో యాక్సెస్ చేయండి `http://localhost:8501`.

## సంప్రదింపు

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

పూర్తి ఆర్టికల్: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
బాధ్యతా నిరాకరణ:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator)ను ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలలో పొరపాట్లు లేదా తప్పులు ఉండవచ్చు అని దయచేసి గమనించండి. అసలు భాషలో ఉన్న మూల పత్రాన్ని అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి వృత్తిపరమైన మానవ అనువాదాన్ని సూచించబడుతుంది. ఈ అనువాదాన్ని ఉపయోగించటం వల్ల ఏర్పడే ఏవైనా అపార్థాలు లేదా తప్పుగా అర్ధమయ్యే విషయాలకు మేము బాధ్యులం కాదాం.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->