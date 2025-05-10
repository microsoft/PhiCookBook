<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-05-09T21:48:42+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "nl"
}
-->
# Phi-3-Vision-128K-Instruct Projectoverzicht

## Het Model

De Phi-3-Vision-128K-Instruct, een lichtgewicht, geavanceerd multimodaal model, vormt de kern van dit project. Het maakt deel uit van de Phi-3 modelreeks en ondersteunt een contextlengte tot 128.000 tokens. Het model is getraind op een diverse dataset die synthetische data en zorgvuldig gefilterde, openbaar beschikbare websites bevat, met de nadruk op hoogwaardige, redeneerintensieve inhoud. Het trainingsproces omvatte gesuperviseerde fine-tuning en directe voorkeuroptimalisatie om nauwkeurige naleving van instructies te waarborgen, evenals robuuste veiligheidsmaatregelen.

## Het maken van voorbeelddata is om verschillende redenen cruciaal:

1. **Testen**: Voorbeelddata stelt je in staat je applicatie onder verschillende scenario’s te testen zonder echte data te beïnvloeden. Dit is vooral belangrijk in de ontwikkel- en testfasen.

2. **Prestatieoptimalisatie**: Met voorbeelddata die de schaal en complexiteit van echte data nabootst, kun je prestatieknelpunten identificeren en je applicatie optimaliseren.

3. **Prototyping**: Voorbeelddata kan gebruikt worden om prototypes en mockups te maken, wat helpt bij het begrijpen van gebruikersbehoeften en het verkrijgen van feedback.

4. **Data-analyse**: In data science wordt voorbeelddata vaak gebruikt voor verkennende data-analyse, modeltraining en het testen van algoritmes.

5. **Beveiliging**: Het gebruik van voorbeelddata in ontwikkel- en testomgevingen helpt het per ongeluk lekken van gevoelige echte data te voorkomen.

6. **Leren**: Als je een nieuwe technologie of tool leert, biedt werken met voorbeelddata een praktische manier om het geleerde toe te passen.

Onthoud dat de kwaliteit van je voorbeelddata een grote invloed kan hebben op deze activiteiten. Het moet zo dicht mogelijk bij de echte data liggen qua structuur en variatie.

### Voorbeelddata aanmaken
[Generate DataSet Script](./CreatingSampleData.md)

## Dataset

Een goed voorbeeld van een voorbeelddataset is de [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (beschikbaar op Huggingface).  
De voorbeelddataset van Burberry-producten bevat metadata over productcategorie, prijs en titel met in totaal 3.040 rijen, elk representatief voor een uniek product. Deze dataset stelt ons in staat het vermogen van het model te testen om visuele data te begrijpen en te interpreteren, en beschrijvende teksten te genereren die gedetailleerde visuele kenmerken en merkgebonden eigenschappen vastleggen.

**Note:** Je kunt elke dataset gebruiken die afbeeldingen bevat.

## Complex Redeneren

Het model moet redeneren over prijzen en namen op basis van alleen de afbeelding. Dit vereist dat het model niet alleen visuele kenmerken herkent, maar ook begrijpt wat deze betekenen in termen van productwaarde en branding. Door nauwkeurige tekstuele beschrijvingen uit afbeeldingen te synthetiseren, laat het project zien hoe visuele data geïntegreerd kan worden om de prestaties en veelzijdigheid van modellen in praktische toepassingen te verbeteren.

## Phi-3 Vision Architectuur

De modelarchitectuur is een multimodale versie van Phi-3. Het verwerkt zowel tekst- als afbeeldingsdata en integreert deze inputs in een eenduidige sequentie voor een volledig begrip en generatietaken. Het model gebruikt aparte embeddinglagen voor tekst en afbeeldingen. Teksttokens worden omgezet in dichte vectoren, terwijl afbeeldingen worden verwerkt via een CLIP vision-model om feature embeddings te extraheren. Deze image embeddings worden vervolgens geprojecteerd zodat ze overeenkomen met de dimensies van de tekst embeddings, zodat ze naadloos geïntegreerd kunnen worden.

## Integratie van Tekst- en Afbeeldingsembeddings

Speciale tokens binnen de tekstsequentie geven aan waar de image embeddings moeten worden ingevoegd. Tijdens het verwerken worden deze speciale tokens vervangen door de bijbehorende image embeddings, waardoor het model tekst en afbeeldingen als één sequentie kan behandelen. De prompt voor onze dataset is geformatteerd met de speciale <|image|> token als volgt:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Voorbeeldcode
- [Phi-3-Vision Trainingsscript](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias voorbeeld walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal dient als de gezaghebbende bron te worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.