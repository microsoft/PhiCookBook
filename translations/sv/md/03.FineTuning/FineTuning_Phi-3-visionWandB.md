<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-07-17T08:10:45+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "sv"
}
-->
# Phi-3-Vision-128K-Instruct Projektöversikt

## Modellen

Phi-3-Vision-128K-Instruct, en lättviktig, toppmodern multimodal modell, är kärnan i detta projekt. Den tillhör Phi-3-modellfamiljen och stödjer en kontextlängd på upp till 128 000 tokens. Modellen tränades på en mångsidig datamängd som inkluderar syntetiska data och noggrant filtrerade offentligt tillgängliga webbplatser, med fokus på högkvalitativt, resonemangsintensivt innehåll. Träningsprocessen inkluderade övervakad finjustering och direkt preferensoptimering för att säkerställa exakt följsamhet till instruktioner, samt robusta säkerhetsåtgärder.

## Att skapa exempeldata är avgörande av flera skäl:

1. **Testning**: Exempeldata gör det möjligt att testa din applikation under olika scenarier utan att påverka verkliga data. Detta är särskilt viktigt under utvecklings- och testfaserna.

2. **Prestandaoptimering**: Med exempeldata som efterliknar skalan och komplexiteten hos verkliga data kan du identifiera prestandaflaskhalsar och optimera din applikation därefter.

3. **Prototypframtagning**: Exempeldata kan användas för att skapa prototyper och mockups, vilket hjälper till att förstå användarkrav och få feedback.

4. **Dataanalys**: Inom datavetenskap används exempeldata ofta för explorativ dataanalys, modellträning och algoritmtestning.

5. **Säkerhet**: Att använda exempeldata i utvecklings- och testmiljöer kan hjälpa till att förhindra oavsiktliga dataläckor av känslig verklig data.

6. **Inlärning**: Om du lär dig en ny teknik eller verktyg kan arbete med exempeldata ge ett praktiskt sätt att tillämpa det du lärt dig.

Kom ihåg att kvaliteten på din exempeldata kan påverka dessa aktiviteter avsevärt. Den bör vara så lik verkliga data som möjligt när det gäller struktur och variation.

### Skapa Exempeldata
[Generate DataSet Script](./CreatingSampleData.md)

## Dataset

Ett bra exempel på ett exempel-dataset är [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (tillgängligt på Huggingface).  
Exempel-datasetet för Burberry-produkter innehåller metadata om produktkategori, pris och titel med totalt 3 040 rader, där varje rad representerar en unik produkt. Detta dataset låter oss testa modellens förmåga att förstå och tolka visuella data, och generera beskrivande text som fångar invecklade visuella detaljer och varumärkesspecifika egenskaper.

**Note:** Du kan använda vilket dataset som helst som inkluderar bilder.

## Komplexa resonemang

Modellen behöver resonera kring priser och namngivning baserat endast på bilden. Detta kräver att modellen inte bara känner igen visuella egenskaper utan också förstår deras betydelse i termer av produktvärde och varumärke. Genom att syntetisera korrekta textbeskrivningar från bilder visar projektet potentialen i att integrera visuell data för att förbättra modellernas prestanda och mångsidighet i verkliga tillämpningar.

## Phi-3 Vision Arkitektur

Modellarkitekturen är en multimodal version av Phi-3. Den bearbetar både text- och bilddata och integrerar dessa indata till en enhetlig sekvens för omfattande förståelse och generering. Modellen använder separata inbäddningslager för text och bilder. Texttokens omvandlas till täta vektorer, medan bilder bearbetas genom en CLIP-visionmodell för att extrahera funktionsinbäddningar. Dessa bildinbäddningar projiceras sedan för att matcha dimensionerna hos textinbäddningarna, vilket säkerställer att de kan integreras sömlöst.

## Integration av text- och bildinbäddningar

Speciella tokens i textsekvensen anger var bildinbäddningarna ska infogas. Under bearbetningen ersätts dessa specialtokens med motsvarande bildinbäddningar, vilket gör att modellen kan hantera text och bilder som en enda sekvens. Prompten för vårt dataset formateras med den speciella <|image|>-token enligt följande:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Exempel på kod
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.