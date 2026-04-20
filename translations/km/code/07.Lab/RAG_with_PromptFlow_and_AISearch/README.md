## RAG ជាមួយ PromptFlow និង AISearch

ក្នុងឧទាហរណ៍នេះ យើងនឹងអនុវត្តកម្មវិធីបង្កើតនេះដោយប្រើការទាញយកបន្ថែម (Retrieval Augmented Generation - RAG) ដោយប្រើ Phi3 ជា SLM, AI Search ជា vectorDB និង Prompt Flow ជា low-code orchestrator។

## លក្ខណៈពិសេស

- ការតំឡើងរហ័សតាមរយៈ Docker។
- ស្ថាបត្យកម្មអាចពង្រីកសម្រាប់គ្រប់គ្រងការងារ AI។
- វិធីសាស្រ្តកូដទាបដោយប្រើ Prompt Flow

## លក្ខខណ្ឌដំបូង

មុននឹងចាប់ផ្ដើម សូមប្រាកដថាអ្នកបានបំពេញលក្ខខណ្ឌដូចខាងក្រោម៖

- មាន Docker តំឡើងលើម៉ាស៊ីនក្នុងដៃ។
- មានគណនី Azure ដែលមានសិទ្ធិបង្កើត និងគ្រប់គ្រងធនធាន container។
- មាន Azure AI Studio និង Azure AI Search instances
- មានម៉ូដែល embedding ដើម្បីបង្កើត index (អាចជាដូចជា embedding Azure OpenAI ឬម៉ូដែល OS ពីបញ្ជី)
- មាន Python 3.8 ឬក្រោយបំផុតតំឡើងលើម៉ាស៊ីនក្នុងដៃ។
- មាន Azure Container Registry (ឬ registry មួយណាមួយដែលអ្នកចង់បាន)

## ការតំឡើង

1. បង្កើត flow ថ្មីមួយលើគម្រោង Azure AI Studio របស់អ្នក ដោយប្រើ flow.yaml។  
2. ដាក់ឲ្យដំណើរការ ម៉ូដែល Phi3 ពីបញ្ជីម៉ូដែល Azure AI របស់អ្នក ហើយបង្កើតការតភ្ជាប់ទៅគម្រោងរបស់អ្នក។ [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)  
3. បង្កើតវ៉ិចទ័រ index លើ Azure AI Search ដោយប្រើឯកសារណាមួយដែលអ្នកចង់បាន [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)  
4. ដាក់ឲ្យដំណើរការហើយប្រើ flow លើ managed endpoint ហើយប្រើក្នុងไฟล์ prompt-flow-frontend.py។ [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)  
5. ចម្លងមើលរក្សាទុក repository៖

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```
  
6. សាងសង់រូបភាព Docker៖

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```
  
7. បញ្ចូនរូបភាព Docker ទៅ Azure Container Registry៖

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```
  
## ការប្រើប្រាស់

1. រត់ container Docker៖

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```
  
2. ចូលប្រើកម្មវិធីក្នុងកម្មវិបព័រ នៅ `http://localhost:8501`។

## ទំនាក់ទំនង

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

អត្ថបទពេញលេញ៖ [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំរកភាពត្រឹមត្រូវ សូមយល់ព្រមថាការបកប្រែក្នុងរបៀបស្វ័យប្រវត្តិអាចមានមោទនភាពខុសឬការមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសារបស់វាគួរត្រូវបានគិតថាជា ឯកសារដែលមានអំណាចសុពលភាព។ សម្រាប់ព័ត៌មានដ៏សំខាន់ សូមណែនាំឱ្យបកប្រែដោយអ្នកជំនាញមនុស្សវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់មិនត្រឹមត្រូវ ឬការបកប្រែខុសក្នុងការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->