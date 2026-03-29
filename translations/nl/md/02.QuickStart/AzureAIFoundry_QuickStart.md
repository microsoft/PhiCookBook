# **Phi-3 gebruiken in Microsoft Foundry**

Met de ontwikkeling van Generative AI hopen we een uniform platform te gebruiken om verschillende LLM- en SLM-modellen te beheren, enterprise data-integratie, fine-tuning/RAG-operaties en de evaluatie van verschillende enterprise-bedrijven na integratie van LLM en SLM uit te voeren, zodat generatieve AI beter in slimme applicaties kan worden geïmplementeerd. [Microsoft Foundry](https://ai.azure.com) is een generatief AI-applicatieplatform op ondernemingsniveau.

![aistudo](../../../../translated_images/nl/aifoundry_home.f28a8127c96c7d93.webp)

Met Microsoft Foundry kunt u de reacties van grote taalmodellen (LLM) evalueren en promptapplicatiecomponenten orkestreren met prompt flow voor betere prestaties. Het platform faciliteert schaalbaarheid voor het moeiteloos omzetten van proof of concepts naar volwaardige productie. Continue monitoring en verfijning ondersteunen langdurig succes.

We kunnen het Phi-3-model snel implementeren op Microsoft Foundry door eenvoudige stappen te volgen, en vervolgens Microsoft Foundry gebruiken om Phi-3 gerelateerde Playground/Chat, Fine-tuning, evaluatie en ander gerelateerd werk te voltooien.

## **1. Voorbereiding**

Als u de [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) al op uw machine hebt geïnstalleerd, is het gebruik van deze template zo eenvoudig als het uitvoeren van dit commando in een nieuwe directory.

## Handmatige Aanmaak

Een Microsoft Foundry-project en hub aanmaken is een geweldige manier om uw AI-werk te organiseren en beheren. Hier is een stapsgewijze handleiding om u op weg te helpen:

### Een project aanmaken in Microsoft Foundry

1. **Ga naar Microsoft Foundry**: Meld u aan bij het Microsoft Foundry-portaal.
2. **Maak een project aan**:
   - Als u zich in een project bevindt, selecteer dan "Microsoft Foundry" linksboven op de pagina om naar de startpagina te gaan.
   - Selecteer "+ Create project".
   - Voer een naam in voor het project.
   - Als u een hub hebt, wordt deze standaard geselecteerd. Als u toegang hebt tot meer dan één hub, kunt u er een andere selecteren in de vervolgkeuzelijst. Wilt u een nieuwe hub aanmaken, selecteer dan "Create new hub" en geef een naam op.
   - Selecteer "Create".

### Een hub aanmaken in Microsoft Foundry

1. **Ga naar Microsoft Foundry**: Meld u aan met uw Azure-account.
2. **Maak een hub aan**:
   - Selecteer het Management centrum in het linkermenu.
   - Selecteer "All resources", klik op het pijltje naast "+ New project" en selecteer "+ New hub".
   - Voer in het dialoogvenster "Create a new hub" een naam in voor uw hub (bijv. contoso-hub) en pas de andere velden aan indien gewenst.
   - Selecteer "Next", controleer de informatie en selecteer vervolgens "Create".

Voor meer gedetailleerde instructies kunt u de officiële [Microsoft documentatie](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects) raadplegen.

Na succesvolle aanmaak kunt u via [ai.azure.com](https://ai.azure.com/) toegang krijgen tot de door u gemaakte studio.

Er kunnen meerdere projecten zijn op één AI Foundry. Maak een project aan in AI Foundry ter voorbereiding.

Maak Microsoft Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. Een Phi-model implementeren in Microsoft Foundry**

Klik op de optie Explore van het project om de Model Catalog te openen en selecteer Phi-3.

Selecteer Phi-3-mini-4k-instruct.

Klik op 'Deploy' om het Phi-3-mini-4k-instruct model te implementeren.

> [!NOTE]
>
> U kunt de rekenkracht selecteren bij het implementeren.

## **3. Playground Chat Phi in Microsoft Foundry**

Ga naar de implementatiepagina, selecteer Playground en chat met Phi-3 van Microsoft Foundry.

## **4. Het Model implementeren vanuit Microsoft Foundry**

Om een model te implementeren vanuit de Azure Model Catalog, kunt u de volgende stappen volgen:

- Meld u aan bij Microsoft Foundry.
- Kies het model dat u wilt implementeren uit de Microsoft Foundry modelcatalogus.
- Selecteer op de detailpagina van het model Deploy en vervolgens Serverless API met Azure AI Content Safety.
- Selecteer het project waarin u uw modellen wilt implementeren. Om de Serverless API-aanbieding te gebruiken, moet uw werkruimte zich in de regio East US 2 of Sweden Central bevinden. U kunt de naam van de implementatie aanpassen.
- Selecteer in de implementatiewizard de Prijzen en voorwaarden om meer te weten te komen over de prijzen en gebruiksvoorwaarden.
- Selecteer Deploy. Wacht totdat de implementatie klaar is en u wordt doorgestuurd naar de pagina Implementaties.
- Selecteer Open in playground om te beginnen met interactie met het model.
- U kunt terugkeren naar de pagina Implementaties, de implementatie selecteren en de Target URL en Secret Key van het eindpunt noteren, die u kunt gebruiken om de implementatie aan te roepen en completions te genereren.
- U kunt altijd de details van het eindpunt, de URL en toegangssleutels vinden door naar het tabblad Build te navigeren en Deployments te selecteren in het onderdeel Components.

> [!NOTE]
> Houd er rekening mee dat uw account de Azure AI Developer-rolmachtigingen op de Resource Group moet hebben om deze stappen uit te voeren.

## **5. Phi API gebruiken in Microsoft Foundry**

U kunt https://{Uw projectnaam}.region.inference.ml.azure.com/swagger.json via Postman GET benaderen en dit combineren met uw sleutel om meer te leren over de beschikbare interfaces.

U kunt heel gemakkelijk de aanvraagparameters krijgen, evenals de responsparameters.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vrijwaring**:  
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professioneel menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->