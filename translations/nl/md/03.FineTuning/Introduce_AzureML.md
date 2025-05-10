<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7fe541373802e33568e94e13226d463c",
  "translation_date": "2025-05-09T22:21:35+00:00",
  "source_file": "md/03.FineTuning/Introduce_AzureML.md",
  "language_code": "nl"
}
-->
# **Introductie van Azure Machine Learning Service**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo) is een cloudservice die het machine learning (ML) projectlevenscyclus versnelt en beheert.

ML-professionals, datawetenschappers en engineers kunnen het in hun dagelijkse workflows gebruiken om:

- Modellen te trainen en te implementeren.
- Machine learning operaties (MLOps) te beheren.
- Je kunt een model maken in Azure Machine Learning of een model gebruiken dat is gebouwd met een open-source platform zoals PyTorch, TensorFlow of scikit-learn.
- MLOps-tools helpen je bij het monitoren, opnieuw trainen en opnieuw implementeren van modellen.

## Voor wie is Azure Machine Learning bedoeld?

**Datawetenschappers en ML-engineers**

Zij kunnen tools gebruiken om hun dagelijkse workflows te versnellen en te automatiseren.  
Azure ML biedt functies voor eerlijkheid, verklaarbaarheid, tracking en auditbaarheid.

**Applicatieontwikkelaars**

Zij kunnen modellen naadloos integreren in applicaties of diensten.

**Platformontwikkelaars**

Zij hebben toegang tot een robuuste set tools die worden ondersteund door duurzame Azure Resource Manager API's.  
Deze tools maken het mogelijk geavanceerde ML-tools te bouwen.

**Ondernemingen**

Werkend in de Microsoft Azure-cloud profiteren ondernemingen van bekende beveiliging en rolgebaseerde toegangscontrole.  
Stel projecten in om toegang tot beschermde data en specifieke handelingen te regelen.

## Productiviteit voor iedereen in het team

ML-projecten vereisen vaak een team met diverse vaardigheden om te bouwen en te onderhouden.

Azure ML biedt tools waarmee je kunt:  
- Samenwerken met je team via gedeelde notebooks, rekenkracht, serverloze compute, data en omgevingen.  
- Modellen ontwikkelen met eerlijkheid, verklaarbaarheid, tracking en auditbaarheid om aan eisen voor herkomst en compliance te voldoen.  
- ML-modellen snel en eenvoudig op schaal implementeren, beheren en besturen met MLOps.  
- Machine learning workloads overal uitvoeren met ingebouwde governance, beveiliging en compliance.

## Cross-compatibele platformtools

Iedereen in een ML-team kan zijn favoriete tools gebruiken om het werk gedaan te krijgen.  
Of je nu snelle experimenten uitvoert, hyperparameter tuning doet, pijplijnen bouwt of inferenties beheert, je kunt vertrouwde interfaces gebruiken zoals:  
- Azure Machine Learning Studio  
- Python SDK (v2)  
- Azure CLI (v2)  
- Azure Resource Manager REST API's

Terwijl je modellen verfijnt en samenwerkt gedurende de ontwikkelingscyclus, kun je binnen de Azure Machine Learning studio UI assets, resources en metrics delen en terugvinden.

## **LLM/SLM in Azure ML**

Azure ML heeft veel functies toegevoegd die te maken hebben met LLM/SLM, waarbij LLMOps en SLMOps worden gecombineerd om een generatief AI-technologieplatform op ondernemingsniveau te creëren.

### **Model Catalogus**

Enterprisegebruikers kunnen verschillende modellen inzetten afhankelijk van de business scenario's via de Model Catalogus, en bieden diensten aan als Model as Service zodat enterpriseontwikkelaars of gebruikers hier toegang toe hebben.

![models](../../../../translated_images/models.2450411eac222e539ffb55785a8f550d01be1030bd8eb67c9c4f9ae4ca5d64be.nl.png)

De Model Catalogus in Azure Machine Learning studio is het centrale punt om een breed scala aan modellen te ontdekken en te gebruiken waarmee je Generative AI-toepassingen kunt bouwen. De catalogus bevat honderden modellen van modelproviders zoals Azure OpenAI service, Mistral, Meta, Cohere, Nvidia, Hugging Face, inclusief modellen getraind door Microsoft. Modellen van andere providers dan Microsoft worden beschouwd als Non-Microsoft Products, zoals gedefinieerd in de Productvoorwaarden van Microsoft, en vallen onder de voorwaarden die bij het model horen.

### **Job Pipeline**

De kern van een machine learning pijplijn is het opdelen van een complete machine learning taak in een workflow met meerdere stappen. Elke stap is een beheersbaar onderdeel dat afzonderlijk ontwikkeld, geoptimaliseerd, geconfigureerd en geautomatiseerd kan worden. De stappen zijn verbonden via goed gedefinieerde interfaces. De Azure Machine Learning pipeline service orkestreert automatisch alle afhankelijkheden tussen de pijplijnstappen.

Bij het fijn afstemmen van SLM / LLM kunnen we onze data, training en generatieprocessen beheren via de Pipeline.

![finetuning](../../../../translated_images/finetuning.b52e4aa971dfd8d3c668db913a2b419380533bd3a920d227ec19c078b7b3f309.nl.png)

### **Prompt flow**

Voordelen van het gebruik van Azure Machine Learning prompt flow  
Azure Machine Learning prompt flow biedt diverse voordelen die gebruikers helpen bij de overgang van idee naar experiment en uiteindelijk naar productieklare LLM-gebaseerde applicaties:

**Prompt engineering flexibiliteit**

Interactieve authoring ervaring: Azure Machine Learning prompt flow geeft een visuele weergave van de structuur van de flow, waardoor gebruikers hun projecten makkelijk kunnen begrijpen en navigeren. Het biedt ook een notebook-achtige codeerervaring voor efficiënte flow-ontwikkeling en debugging.  
Varianten voor prompt tuning: gebruikers kunnen meerdere promptvarianten maken en vergelijken, wat een iteratief verfijningsproces mogelijk maakt.

Evaluatie: ingebouwde evaluatieflows stellen gebruikers in staat de kwaliteit en effectiviteit van hun prompts en flows te beoordelen.

Uitgebreide resources: Azure Machine Learning prompt flow bevat een bibliotheek met ingebouwde tools, voorbeelden en sjablonen die als startpunt dienen voor ontwikkeling, creativiteit stimuleren en het proces versnellen.

**Enterprise gereedheid voor LLM-gebaseerde applicaties**

Samenwerking: Azure Machine Learning prompt flow ondersteunt teamwerk, waardoor meerdere gebruikers samen kunnen werken aan prompt engineering projecten, kennis kunnen delen en versiebeheer kunnen toepassen.

Alles-in-één platform: Azure Machine Learning prompt flow stroomlijnt het volledige prompt engineering proces, van ontwikkeling en evaluatie tot implementatie en monitoring. Gebruikers kunnen hun flows moeiteloos implementeren als Azure Machine Learning endpoints en realtime de prestaties monitoren, voor optimale werking en continue verbetering.

Azure Machine Learning Enterprise Readiness Solutions: Prompt flow maakt gebruik van de robuuste enterprise readiness oplossingen van Azure Machine Learning, die een veilige, schaalbare en betrouwbare basis bieden voor de ontwikkeling, experimentatie en implementatie van flows.

Met Azure Machine Learning prompt flow kunnen gebruikers hun prompt engineering flexibiliteit volledig benutten, effectief samenwerken en gebruikmaken van enterprise-grade oplossingen voor succesvolle ontwikkeling en implementatie van LLM-gebaseerde applicaties.

Door de rekenkracht, data en verschillende componenten van Azure ML te combineren, kunnen enterpriseontwikkelaars eenvoudig hun eigen AI-toepassingen bouwen.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal geldt als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.