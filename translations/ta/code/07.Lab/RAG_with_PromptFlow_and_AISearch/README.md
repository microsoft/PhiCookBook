## PromptFlow மற்றும் AISearch உடன் RAG

இந்த உதாரணத்தில், Phi3 ஐ SLM ஆகவும், AI Search ஐ vectorDB ஆகவும், Prompt Flow ஐ குறைந்த குறியீட்டு ஒருங்கிணைப்பாளராகவும் பயன்படுத்தி Retrieval Augmented Generation (RAG) பயன்பாட்டை செயல்படுத்துவோம்.

## அம்சங்கள்

- Docker பயன்படுத்தி எளிதான நிறுவல்.
- AI வேலைப்பாடுகளை கையாளுவதற்கான அளவளாவிய கட்டமைப்பு.
- Prompt Flow மூலம் குறைந்த குறியீட்டு அணுகுமுறை.

## முன்பதிவுகள்

தொடங்குவதற்கு முன், நீங்கள் பின்வரும் தேவைகளை பூர்த்தி செய்துள்ளீர்கள் என்பதை உறுதிப்படுத்தவும்:

- உங்கள் உள்ளூர் கணினியில் Docker நிறுவப்பட்டிருக்க வேண்டும்.
- Azure கணக்கு மற்றும் கொண்டெய்னர் வளங்களை உருவாக்க மற்றும் நிர்வகிக்க அனுமதிகள்.
- Azure AI Studio மற்றும் Azure AI Search நிகழ்வுகள்.
- உங்கள் குறியீட்டைப் உருவாக்க ஒரு embedding மாடல் (Azure OpenAI embedding அல்லது பட்டியலிலிருந்து OS மாடல் ஆகியவற்றில் ஏதேனும் ஒன்று இருக்கலாம்).
- Python 3.8 அல்லது அதற்கு மேல் உங்கள் உள்ளூர் கணினியில் நிறுவப்பட்டிருக்க வேண்டும்.
- Azure Container Registry (அல்லது உங்கள் விருப்பமான எந்தவொரு registry).

## நிறுவல்

1. உங்கள் Azure AI Studio Project இல் flow.yaml கோப்பைப் பயன்படுத்தி புதிய ஒரு flow உருவாக்கவும்.
2. Azure AI மாடல் பட்டியலிலிருந்து Phi3 மாடலை நிறுவி உங்கள் திட்டத்துடன் இணைக்கவும். [Phi-3 ஐ Model as a Service ஆக நிறுவவும்](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. உங்கள் விருப்பமான எந்தவொரு ஆவணத்தைப் பயன்படுத்தி Azure AI Search இல் vector index ஐ உருவாக்கவும். [Azure AI Search இல் vector index ஐ உருவாக்கவும்](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. flow ஐ ஒரு நிர்வகிக்கப்பட்ட endpoint இல் நிறுவி அதை prompt-flow-frontend.py கோப்பில் பயன்படுத்தவும். [ஒரு online endpoint இல் flow ஐ நிறுவவும்](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. repository ஐ clone செய்யவும்:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Docker image ஐ உருவாக்கவும்:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Docker image ஐ Azure Container Registry இல் push செய்யவும்:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## பயன்பாடு

1. Docker container ஐ இயக்கவும்:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. உங்கள் உலாவியில் `http://localhost:8501` இல் பயன்பாட்டை அணுகவும்.

## தொடர்பு

வாலென்டினா ஆல்டோ - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

முழு கட்டுரை: [Azure Model Catalog இல் Phi-3-Medium ஐ Model as a Service ஆக RAG](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.