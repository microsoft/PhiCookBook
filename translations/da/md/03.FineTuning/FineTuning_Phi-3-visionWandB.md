<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-07-17T08:11:00+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "da"
}
-->
# Phi-3-Vision-128K-Instruct Projektoversigt

## Modellen

Phi-3-Vision-128K-Instruct, en letvægts, avanceret multimodal model, er kernen i dette projekt. Den er en del af Phi-3 modelserien og understøtter en kontekstlængde på op til 128.000 tokens. Modellen er trænet på et varieret datasæt, der inkluderer syntetiske data og nøje filtrerede offentligt tilgængelige hjemmesider med fokus på indhold af høj kvalitet og komplekse ræsonnementer. Træningsprocessen omfattede superviseret finjustering og direkte præferenceoptimering for at sikre præcis overholdelse af instruktioner samt robuste sikkerhedsforanstaltninger.

## Oprettelse af sample data er vigtigt af flere grunde:

1. **Testning**: Sample data giver dig mulighed for at teste din applikation under forskellige scenarier uden at påvirke rigtige data. Dette er især vigtigt i udviklings- og stagingfaserne.

2. **Performanceoptimering**: Med sample data, der efterligner omfanget og kompleksiteten af rigtige data, kan du identificere flaskehalse og optimere din applikation derefter.

3. **Prototyping**: Sample data kan bruges til at lave prototyper og mockups, hvilket hjælper med at forstå brugerkrav og indhente feedback.

4. **Dataanalyse**: Inden for datalogi bruges sample data ofte til eksplorativ dataanalyse, modeltræning og algoritmetest.

5. **Sikkerhed**: Brug af sample data i udviklings- og testmiljøer kan hjælpe med at forhindre utilsigtede datalækager af følsomme rigtige data.

6. **Læring**: Hvis du lærer en ny teknologi eller et værktøj, kan arbejde med sample data give en praktisk måde at anvende det, du har lært.

Husk, at kvaliteten af dit sample data kan have stor betydning for disse aktiviteter. Det bør være så tæt på de rigtige data som muligt med hensyn til struktur og variation.

### Oprettelse af Sample Data
[Generate DataSet Script](./CreatingSampleData.md)

## Datasæt

Et godt eksempel på et sample datasæt er [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (tilgængeligt på Huggingface).  
Sample datasættet indeholder Burberry-produkter sammen med metadata om produktkategori, pris og titel med i alt 3.040 rækker, hvor hver række repræsenterer et unikt produkt. Dette datasæt giver os mulighed for at teste modellens evne til at forstå og fortolke visuelle data ved at generere beskrivende tekst, der fanger detaljerede visuelle elementer og brandspecifikke karakteristika.

**Note:** Du kan bruge ethvert datasæt, der inkluderer billeder.

## Kompleks Ræsonnering

Modellen skal ræsonnere omkring priser og navngivning ud fra kun billedet. Det kræver, at modellen ikke blot genkender visuelle træk, men også forstår deres betydning i forhold til produktværdi og branding. Ved at syntetisere præcise tekstbeskrivelser ud fra billeder fremhæver projektet potentialet i at integrere visuelle data for at forbedre modellernes ydeevne og alsidighed i virkelige anvendelser.

## Phi-3 Vision Arkitektur

Modelarkitekturen er en multimodal version af Phi-3. Den behandler både tekst- og billeddata og integrerer disse input i en samlet sekvens for en omfattende forståelse og generering. Modellen bruger separate embeddingslag for tekst og billeder. Teksttokens omdannes til tætte vektorer, mens billeder behandles gennem en CLIP vision-model for at udtrække feature embeddings. Disse billede-embeddings projiceres derefter, så de matcher dimensionerne af tekst-embeddings, hvilket sikrer, at de kan integreres problemfrit.

## Integration af Tekst- og Billede-Embeddings

Specielle tokens i tekstsekvensen angiver, hvor billede-embeddings skal indsættes. Under behandlingen erstattes disse specielle tokens med de tilsvarende billede-embeddings, hvilket gør det muligt for modellen at håndtere tekst og billeder som en enkelt sekvens. Prompten for vores datasæt er formateret med det specielle <|image|> token som følger:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Eksempelkode
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.