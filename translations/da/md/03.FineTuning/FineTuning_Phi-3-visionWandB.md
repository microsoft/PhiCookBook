<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-05-09T21:48:11+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "da"
}
-->
# Phi-3-Vision-128K-Instruct Projektoversigt

## Modellen

Phi-3-Vision-128K-Instruct, en letvægts, avanceret multimodal model, er kernen i dette projekt. Den er en del af Phi-3 model-familien og understøtter en kontekstlængde på op til 128.000 tokens. Modellen er trænet på et varieret datasæt, der inkluderer syntetiske data og omhyggeligt filtrerede offentligt tilgængelige hjemmesider, med fokus på indhold af høj kvalitet og krævende ræsonnement. Træningsprocessen omfattede overvåget finjustering og direkte præferenceoptimering for at sikre præcis overholdelse af instruktioner samt robuste sikkerhedsforanstaltninger.

## Oprettelse af sample data er vigtigt af flere grunde:

1. **Testning**: Sample data giver dig mulighed for at teste din applikation under forskellige scenarier uden at påvirke rigtige data. Dette er især vigtigt i udviklings- og stagingfaserne.

2. **Performanceoptimering**: Med sample data, der efterligner skalaen og kompleksiteten af rigtige data, kan du identificere performance-flaskehalse og optimere din applikation derefter.

3. **Prototyping**: Sample data kan bruges til at skabe prototyper og mockups, hvilket hjælper med at forstå brugerkrav og indhente feedback.

4. **Dataanalyse**: Inden for datavidenskab bruges sample data ofte til eksplorativ dataanalyse, modeltræning og algoritmetestning.

5. **Sikkerhed**: Brug af sample data i udviklings- og testmiljøer kan hjælpe med at forhindre utilsigtede datalækager af følsomme rigtige data.

6. **Læring**: Hvis du lærer en ny teknologi eller værktøj, kan arbejde med sample data give en praktisk måde at anvende det lærte på.

Husk, kvaliteten af dit sample data kan have stor betydning for disse aktiviteter. Det bør være så tæt som muligt på de rigtige data med hensyn til struktur og variation.

### Oprettelse af Sample Data
[Generate DataSet Script](./CreatingSampleData.md)

## Datasæt

Et godt eksempel på et sample datasæt er [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (tilgængeligt på Huggingface).  
Sample datasættet indeholder Burberry-produkter sammen med metadata om produkternes kategori, pris og titel med i alt 3.040 rækker, hvor hver repræsenterer et unikt produkt. Dette datasæt giver os mulighed for at teste modellens evne til at forstå og fortolke visuelle data ved at generere beskrivende tekst, der fanger komplekse visuelle detaljer og brandspecifikke karakteristika.

**Note:** Du kan bruge ethvert datasæt, der indeholder billeder.

## Kompleks Ræsonnering

Modellen skal ræsonnere omkring priser og navngivning ud fra kun billedet. Dette kræver, at modellen ikke blot genkender visuelle træk, men også forstår deres betydning i forhold til produktværdi og branding. Ved at syntetisere præcise tekstbeskrivelser ud fra billeder fremhæver projektet potentialet i at integrere visuelle data for at forbedre modellernes ydeevne og alsidighed i virkelige anvendelser.

## Phi-3 Vision Arkitektur

Modelarkitekturen er en multimodal version af en Phi-3. Den behandler både tekst- og billeddata og integrerer disse input i en samlet sekvens for omfattende forståelse og generering. Modellen bruger separate embedding-lag til tekst og billeder. Teksttokens omdannes til tætte vektorer, mens billeder behandles gennem en CLIP vision-model for at udtrække feature embeddings. Disse billede-embeddings projiceres derefter, så de matcher dimensionerne på tekst-embeddings, hvilket sikrer en problemfri integration.

## Integration af Tekst- og Billede-Embeddings

Specielle tokens i tekstsekvensen angiver, hvor billede-embeddings skal indsættes. Under behandlingen erstattes disse specielle tokens med de tilsvarende billede-embeddings, hvilket gør det muligt for modellen at håndtere tekst og billeder som en enkelt sekvens. Prompten til vores datasæt er formateret med det specielle <|image|>-token som følger:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Eksempel på kode
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.