<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-07-17T08:11:12+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "no"
}
-->
# Phi-3-Vision-128K-Instruct Prosjektoversikt

## Modellen

Phi-3-Vision-128K-Instruct, en lettvekts, toppmoderne multimodal modell, er kjernen i dette prosjektet. Den er en del av Phi-3 modellfamilien og støtter en kontekstlengde på opptil 128 000 tokens. Modellen ble trent på et variert datasett som inkluderer syntetiske data og nøye filtrerte offentlig tilgjengelige nettsider, med fokus på innhold av høy kvalitet og krevende resonnement. Treningsprosessen inkluderte veiledet finjustering og direkte preferanseoptimalisering for å sikre nøyaktig etterlevelse av instruksjoner, samt robuste sikkerhetstiltak.

## Å lage eksemplardata er viktig av flere grunner:

1. **Testing**: Eksemplardata lar deg teste applikasjonen under ulike scenarier uten å påvirke ekte data. Dette er spesielt viktig i utviklings- og stagingfaser.

2. **Ytelsesoptimalisering**: Med eksemplardata som etterligner omfanget og kompleksiteten til ekte data, kan du identifisere ytelsesflaskehalser og optimalisere applikasjonen deretter.

3. **Prototyping**: Eksemplardata kan brukes til å lage prototyper og mockups, noe som hjelper med å forstå brukerbehov og få tilbakemeldinger.

4. **Dataanalyse**: Innen datavitenskap brukes ofte eksemplardata til utforskende dataanalyse, modelltrening og testing av algoritmer.

5. **Sikkerhet**: Bruk av eksemplardata i utviklings- og testmiljøer kan bidra til å forhindre utilsiktede lekkasjer av sensitiv ekte data.

6. **Læring**: Hvis du lærer en ny teknologi eller verktøy, gir arbeid med eksemplardata en praktisk måte å anvende det du har lært på.

Husk at kvaliteten på eksemplardataene dine kan ha stor betydning for disse aktivitetene. De bør være så nær ekte data som mulig når det gjelder struktur og variasjon.

### Oppretting av eksemplardata
[Generate DataSet Script](./CreatingSampleData.md)

## Datasett

Et godt eksempel på et eksempeldatasett er [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (tilgjengelig på Huggingface).  
Eksempeldatasettet inneholder Burberry-produkter sammen med metadata om produktkategori, pris og tittel, med totalt 3 040 rader, hvor hver rad representerer et unikt produkt. Dette datasettet lar oss teste modellens evne til å forstå og tolke visuelle data, og generere beskrivende tekst som fanger opp detaljerte visuelle trekk og merkevarespesifikke kjennetegn.

**Note:** Du kan bruke hvilket som helst datasett som inkluderer bilder.

## Kompleks resonnement

Modellen må resonnere rundt priser og navn basert kun på bildet. Dette krever at modellen ikke bare gjenkjenner visuelle trekk, men også forstår deres betydning i forhold til produktverdi og merkevarebygging. Ved å syntetisere nøyaktige tekstbeskrivelser fra bilder, viser prosjektet potensialet i å integrere visuelle data for å forbedre modellens ytelse og allsidighet i virkelige applikasjoner.

## Phi-3 Vision Arkitektur

Modellarkitekturen er en multimodal versjon av Phi-3. Den behandler både tekst- og bildedata, og integrerer disse inputtene til en samlet sekvens for helhetlig forståelse og generering. Modellen bruker separate embedding-lag for tekst og bilder. Teksttokens konverteres til tette vektorer, mens bilder behandles gjennom en CLIP vision-modell for å hente ut feature embeddings. Disse bildeembeddingene projiseres deretter for å matche dimensjonene til tekstembeddingene, slik at de kan integreres sømløst.

## Integrasjon av tekst- og bildeembedding

Spesialtokens i tekstsekvensen indikerer hvor bildeembeddingene skal settes inn. Under behandlingen erstattes disse spesialtokenene med de tilsvarende bildeembeddingene, noe som gjør at modellen kan håndtere tekst og bilder som én enkelt sekvens. Prompten for datasettet vårt er formatert med den spesielle <|image|>-tokenen som følger:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Eksempelkode
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.