## RAG ជាមួយ PromptFlow និង AISearch

ក្នុងឧទាហរណ៍នេះ យើងនឹងអនុវត្តកម្មវិធីបង្កើតបន្ថែមដោយការទាញយក (Retrieval Augmented Generation - RAG) ដែលប្រើ Phi3 ជា SLM, AI Search ជា vectorDB និង Prompt Flow ជាកម្មវិធីបញ្ជាដោយកូដទាប។

## លក្ខណៈពិសេស

- តំឡើងបានងាយប្រើប្រាស់ដោយការប្រើ Docker។
- ស្ថាបត្យកម្មអាចបង្កើនបានសម្រាប់ដោះស្រាយដំណើរការព័ត៌មាន AI។
- វិធីសាស្រ្តកូដទាបដោយប្រើ Prompt Flow

## លក្ខខ័ណ្ឌមុនចាប់ផ្ដើម

មុនចាប់ផ្ដើម សូមប្រាកដថាអ្នកបានបំពេញតំរូវការដូចខាងក្រោម៖

- តំឡើង Docker នៅលើកុំព្យូទ័រផ្ទាល់ខ្លួនរបស់អ្នក។
- មានគណនី Azure ដែលមានសិទ្ធិបង្កើត និងគ្រប់គ្រងធនធាន container។
- មាន Azure AI Studio និងឧបករណ៍ Azure AI Search
- មានម៉ូដែល embedding សម្រាប់បង្កើតសន្ទស្សន៍ (អាចជា embedding របស់ Azure OpenAI ឬម៉ូដែល OS ពីបញ្ជីម៉ូដែល)
- តំឡើង Python 3.8 ឬថ្មីជាងនេះនៅលើកុំព្យូទ័រផ្ទាល់ខ្លួនរបស់អ្នក។
- មាន Azure Container Registry (ឬ registry ផ្សេងៗតាមចំណង់ចំណូលចិត្ត)

## ការតំឡើង

1. បង្កើត flow ថ្មីនៅលើគម្រោង Azure AI Studio របស់អ្នកដោយប្រើឯកសារ flow.yaml។
2. ធ្វើការតំឡើងម៉ូដែល Phi3 ពីបញ្ជីម៉ូដែល Azure AI របស់អ្នកហើយបង្កើតការតភ្ជាប់ទៅគម្រោងរបស់អ្នក។ [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. បង្កើតសន្ទស្សន៍ vector នៅលើ Azure AI Search ដោយប្រើឯកសារណាមួយដែលអ្នកចូលចិត្ត [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. តំឡើង flow នៅលើ managed endpoint ហើយប្រើវា​ក្នុងឯកសារ prompt-flow-frontend.py។ [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. ក្លូន repository ៖

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. បង្កើតរូបភាព Docker ៖

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. ផ្ញើរូបភាព Docker ទៅ Azure Container Registry ៖

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## ការប្រើប្រាស់

1. រត់ container Docker ៖

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. ចូលប្រើកម្មវិធីនៅក្នុងកម្មវិធីអ៊ិនធឺរណេតរបស់អ្នកតាមរយៈ `http://localhost:8501`។

## ទំនាក់ទំនង

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

អត្ថបទ​ពេញលេញ ៖ [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបញ្ចាក់**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំប្រឹងប្រែងសម្រាប់ភាពត្រឹមត្រូវ សូមយកចិត្តទុកដាក់ថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុសឬការមិនត្រឹមត្រូវណាមួយ។ ឯកសារដើមជាភាសាមាតុភូមិគួរត្រូវបានគិតថាជាមូលដ្ឋានសញ្ញាប្រឹងប្រាជ្ញា។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើការបកប្រែមនុស្សវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសពីការប្រើប្រាស់ការបកប្រែនេះនោះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->