<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-05-09T05:13:16+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "fi"
}
-->
## RAG with PromptFlow and AISearch

Tässä esimerkissä toteutamme Retrieval Augmented Generation (RAG) -sovelluksen hyödyntäen Phi3:ta SLM:nä, AI Searchia vectorDB:nä ja Prompt Flow'ta low-code orkestroijana.

## Ominaisuudet

- Helppo käyttöönotto Dockerin avulla.
- Skaalautuva arkkitehtuuri AI-työnkulkujen hallintaan.
- Low-code-lähestymistapa Prompt Flown avulla.

## Vaatimukset

Ennen aloittamista varmista, että seuraavat vaatimukset täyttyvät:

- Docker asennettuna paikalliselle koneellesi.
- Azure-tili, jolla on oikeudet luoda ja hallita konttiresursseja.
- Azure AI Studio- ja Azure AI Search -instanssit.
- Upotusmalli indeksin luomiseen (voi olla Azure OpenAI -upotus tai OS-malli katalogista).
- Python 3.8 tai uudempi asennettuna paikalliselle koneellesi.
- Azure Container Registry (tai mikä tahansa haluamasi rekisteri).

## Asennus

1. Luo uusi flow Azure AI Studio -projektissasi käyttäen flow.yaml-tiedostoa.
2. Ota käyttöön Phi3-malli Azure AI -mallikatalogistasi ja luo yhteys projektiisi. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Luo vektori-indeksi Azure AI Searchissa käyttämällä haluamaasi dokumenttia. [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Ota flow käyttöön hallitussa päätepisteessä ja käytä sitä prompt-flow-frontend.py-tiedostossa. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Kloonaa repositorio:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Rakenna Docker-kuva:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Työnnä Docker-kuva Azure Container Registryyn:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Käyttö

1. Käynnistä Docker-kontti:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Käytä sovellusta selaimessasi osoitteessa `http://localhost:8501`.

## Yhteystiedot

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Koko artikkeli: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää auktoritatiivisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaisen ihmiskääntäjän käyttöä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virhetulkinnoista.