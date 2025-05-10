<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-05-09T21:48:01+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "sv"
}
-->
# Phi-3-Vision-128K-Instruct Projektöversikt

## Modellen

Phi-3-Vision-128K-Instruct, en lättviktig, toppmodern multimodal modell, är kärnan i detta projekt. Den tillhör Phi-3 modellfamiljen och stödjer en kontextlängd på upp till 128 000 tokens. Modellen tränades på en mångsidig dataset som inkluderar syntetiska data och noggrant filtrerade offentligt tillgängliga webbplatser, med fokus på högkvalitativt innehåll som kräver avancerad resonemangsförmåga. Träningsprocessen inkluderade övervakad finjustering och direkt preferensoptimering för att säkerställa noggrann efterlevnad av instruktioner, samt robusta säkerhetsåtgärder.

## Att skapa exempeldata är avgörande av flera skäl:

1. **Testning**: Exempeldata gör det möjligt att testa din applikation under olika scenarier utan att påverka verkliga data. Detta är särskilt viktigt under utvecklings- och testfaserna.

2. **Prestandaoptimering**: Med exempeldata som efterliknar skalan och komplexiteten hos verkliga data kan du identifiera prestandaflaskhalsar och optimera din applikation därefter.

3. **Prototypframtagning**: Exempeldata kan användas för att skapa prototyper och mockups, vilket hjälper till att förstå användarkrav och få feedback.

4. **Dataanalys**: Inom datavetenskap används exempeldata ofta för utforskande dataanalys, modellträning och algoritmtestning.

5. **Säkerhet**: Att använda exempeldata i utvecklings- och testmiljöer kan hjälpa till att förhindra oavsiktliga dataläckor av känsliga verkliga data.

6. **Inlärning**: Om du lär dig en ny teknik eller verktyg kan arbete med exempeldata ge ett praktiskt sätt att tillämpa det du lärt dig.

Kom ihåg att kvaliteten på din exempeldata kan påverka dessa aktiviteter avsevärt. Den bör vara så lik verkliga data som möjligt vad gäller struktur och variation.

### Skapa Exempeldata
[Generate DataSet Script](./CreatingSampleData.md)

## Dataset

Ett bra exempel på en exempel-dataset är [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (tillgängligt på Huggingface).  
Exempeldata för Burberry-produkter tillsammans med metadata om produktkategori, pris och titel med totalt 3 040 rader, där varje rad representerar en unik produkt. Denna dataset låter oss testa modellens förmåga att förstå och tolka visuell data, samt generera beskrivande text som fångar detaljerade visuella inslag och varumärkesspecifika kännetecken.

**Note:** Du kan använda vilken dataset som helst som innehåller bilder.

## Komplex Resonerande Förmåga

Modellen behöver resonera kring priser och namngivning utifrån endast bilden. Detta kräver att modellen inte bara känner igen visuella egenskaper utan också förstår deras betydelse i termer av produktvärde och varumärkesprofil. Genom att syntetisera korrekta textbeskrivningar från bilder lyfter projektet fram potentialen i att integrera visuell data för att förbättra modellernas prestanda och mångsidighet i verkliga tillämpningar.

## Phi-3 Vision Arkitektur

Modellarkitekturen är en multimodal version av Phi-3. Den bearbetar både text- och bilddata och integrerar dessa insatser till en enhetlig sekvens för en heltäckande förståelse och genereringsuppgifter. Modellen använder separata inbäddningslager för text och bilder. Texttokens omvandlas till täta vektorer, medan bilder bearbetas genom en CLIP vision-modell för att extrahera funktionsinbäddningar. Dessa bildinbäddningar projiceras sedan för att matcha textinbäddningarnas dimensioner, vilket säkerställer att de kan integreras sömlöst.

## Integration av Text- och Bildinbäddningar

Specialtokens i textsekvensen anger var bildinbäddningarna ska infogas. Under bearbetning ersätts dessa specialtokens med motsvarande bildinbäddningar, vilket gör att modellen kan hantera text och bilder som en enda sekvens. Prompten för vår dataset formateras med specialtoken <|image|> enligt följande:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Exempel på Kod
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För viktig information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.