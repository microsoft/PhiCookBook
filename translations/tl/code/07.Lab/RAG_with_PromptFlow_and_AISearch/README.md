<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-05-09T05:14:06+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "tl"
}
-->
## RAG gamit ang PromptFlow at AISearch

Sa halimbawang ito, ipapatupad natin ang Retrieval Augmented Generation (RAG) na aplikasyon gamit ang Phi3 bilang SLM, AI Search bilang vectorDB, at Prompt Flow bilang low-code orchestrator.

## Mga Tampok

- Madaling i-deploy gamit ang Docker.
- Scalable na arkitektura para sa paghawak ng AI workflows.
- Low code na pamamaraan gamit ang Prompt Flow

## Mga Kinakailangan

Bago ka magsimula, siguraduhing natugunan mo ang mga sumusunod na pangangailangan:

- Nakainstall ang Docker sa iyong lokal na makina.
- May Azure account na may pahintulot na gumawa at mag-manage ng container resources.
- May Azure AI Studio at Azure AI Search na mga instance
- Isang embedding model para gumawa ng iyong index (maaari itong Azure OpenAI embedding o isang OS model mula sa katalogo)
- Nakainstall ang Python 3.8 o mas bago sa iyong lokal na makina.
- Isang Azure Container Registry (o anumang registry na gusto mo)

## Pag-install

1. Gumawa ng bagong flow sa iyong Azure AI Studio Project gamit ang flow.yaml file.
2. I-deploy ang Phi3 Model mula sa iyong Azure AI model catalog at gawin ang koneksyon sa iyong proyekto. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Gumawa ng vector index sa Azure AI Search gamit ang anumang dokumento na gusto mo [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. I-deploy ang flow sa isang managed endpoint at gamitin ito sa prompt-flow-frontend.py file. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. I-clone ang repositoryo:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. I-build ang Docker image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. I-push ang Docker image sa Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Paggamit

1. Patakbuhin ang Docker container:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Buksan ang aplikasyon sa iyong browser sa `http://localhost:8501`.

## Kontakin

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Buong Artikulo: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang likas na wika ang dapat ituring na pinagmumulan ng tama at opisyal na impormasyon. Para sa mga mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.