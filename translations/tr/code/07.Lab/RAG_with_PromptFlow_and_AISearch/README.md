<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-05-09T05:12:28+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "tr"
}
-->
## RAG with PromptFlow ve AISearch

Bu örnekte, Phi3'ü SLM olarak, AI Search'ü vectorDB olarak ve Prompt Flow'u düşük kodlu düzenleyici olarak kullanarak Retrieval Augmented Generation (RAG) uygulaması gerçekleştireceğiz.

## Özellikler

- Docker kullanarak kolay dağıtım.
- AI iş akışlarını yönetmek için ölçeklenebilir mimari.
- Prompt Flow ile düşük kod yaklaşımı.

## Gereksinimler

Başlamadan önce aşağıdaki gereksinimleri karşıladığınızdan emin olun:

- Yerel makinenizde Docker yüklü olmalı.
- Konteyner kaynakları oluşturma ve yönetme yetkilerine sahip bir Azure hesabı.
- Azure AI Studio ve Azure AI Search örnekleri.
- İndeks oluşturmak için bir embedding modeli (Azure OpenAI embedding veya katalogdan bir OS modeli olabilir).
- Yerel makinenizde Python 3.8 veya üzeri yüklü olmalı.
- Azure Container Registry (veya tercih ettiğiniz herhangi bir kayıt defteri).

## Kurulum

1. Azure AI Studio Projenizde flow.yaml dosyasını kullanarak yeni bir akış oluşturun.
2. Azure AI model kataloğunuzdan bir Phi3 Modeli dağıtın ve projenize bağlantısını kurun. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Seçtiğiniz herhangi bir belgeyi kullanarak Azure AI Search üzerinde vektör indeks oluşturun. [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Akışı yönetilen bir uç noktada dağıtın ve prompt-flow-frontend.py dosyasında kullanın. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Depoyu klonlayın:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Docker imajını oluşturun:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Docker imajını Azure Container Registry'ye gönderin:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Kullanım

1. Docker konteynerini çalıştırın:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Uygulamaya tarayıcınızda `http://localhost:8501` adresinden erişin.

## İletişim

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Tam Makale: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilindeki haliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek herhangi bir yanlış anlama veya yorum hatasından sorumlu değiliz.