Deze demo laat zien hoe je een pretrained model kunt gebruiken om Python-code te genereren op basis van een afbeelding en een tekstprompt.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Hier is een stapsgewijze uitleg:

1. **Imports en Setup**:
   - De benodigde libraries en modules worden geïmporteerd, waaronder `requests`, `PIL` voor beeldverwerking, en `transformers` voor het afhandelen van het model en de verwerking.

2. **Afbeelding Laden en Weergeven**:
   - Een afbeeldingsbestand (`demo.png`) wordt geopend met de `PIL`-bibliotheek en weergegeven.

3. **De Prompt Definiëren**:
   - Er wordt een bericht gemaakt dat de afbeelding bevat en een verzoek om Python-code te genereren die de afbeelding verwerkt en opslaat met `plt` (matplotlib).

4. **De Processor Laden**:
   - De `AutoProcessor` wordt geladen vanuit een pretrained model dat is gespecificeerd door de `out_dir` map. Deze processor verwerkt de tekst- en afbeeldingsinput.

5. **De Prompt Maken**:
   - De `apply_chat_template` methode wordt gebruikt om het bericht te formatteren tot een prompt die geschikt is voor het model.

6. **De Inputs Verwerken**:
   - De prompt en afbeelding worden omgezet in tensors die het model kan begrijpen.

7. **Generatie-argumenten Instellen**:
   - Argumenten voor het generatieproces van het model worden gedefinieerd, waaronder het maximale aantal nieuwe tokens dat gegenereerd mag worden en of de output gesampled moet worden.

8. **De Code Genereren**:
   - Het model genereert de Python-code op basis van de inputs en generatie-argumenten. De `TextStreamer` wordt gebruikt om de output te verwerken, waarbij de prompt en speciale tokens worden overgeslagen.

9. **Output**:
   - De gegenereerde code wordt afgedrukt, die Python-code zou moeten bevatten om de afbeelding te verwerken en op te slaan zoals gespecificeerd in de prompt.

Deze demo laat zien hoe je een pretrained model kunt inzetten met OpenVino om dynamisch code te genereren op basis van gebruikersinput en afbeeldingen.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.