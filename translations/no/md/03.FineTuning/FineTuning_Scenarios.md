## Finjusteringsscenarier

![FineTuning with MS Services](../../../../translated_images/no/FinetuningwithMS.3d0cec8ae693e094.webp)

Denne delen gir en oversikt over finjusteringsscenarier i Microsoft Foundry- og Azure-miljøer, inkludert distribusjonsmodeller, infrastrukturlag og vanlig brukte optimaliseringsteknikker.

**Plattform**  
Dette inkluderer administrerte tjenester som Microsoft Foundry (tidligere Microsoft Foundry) og Azure Machine Learning, som tilbyr modelladministrasjon, orkestrering, eksperimentsporing og distribusjonsarbeidsflyter.

**Infrastruktur**  
Finjustering krever skalerbare beregningsressurser. I Azure-miljøer inkluderer dette vanligvis GPU-baserte virtuelle maskiner og CPU-ressurser for lette arbeidsbelastninger, sammen med skalerbar lagring for datasett og sjekkpunkt.

**Verktøy og rammeverk**  
Finjusteringsarbeidsflyter er ofte basert på rammeverk og optimaliseringsbiblioteker som Hugging Face Transformers, DeepSpeed og PEFT (Parameter-Efficient Fine-Tuning).

Finjusteringsprosessen med Microsoft-teknologier spenner over plattformtjenester, beregningsinfrastruktur og treningsrammeverk. Ved å forstå hvordan disse komponentene samarbeider, kan utviklere effektivt tilpasse grunnmodeller til spesifikke oppgaver og produksjonsscenarier.

## Modell som tjeneste

Finjuster modellen ved hjelp av hostet finjustering, uten behov for å opprette og administrere beregning.

![MaaS Fine Tuning](../../../../translated_images/no/MaaSfinetune.3eee4630607aff0d.webp)

Serverløs finjustering er nå tilgjengelig for Phi-3, Phi-3.5 og Phi-4 modelfamilier, noe som gjør det mulig for utviklere å raskt og enkelt tilpasse modellene for sky- og kant-scenarier uten å måtte ordne med beregningsressurser.

## Modell som plattform

Brukere administrerer egen beregning for å finjustere sine modeller.

![Maap Fine Tuning](../../../../translated_images/no/MaaPFinetune.fd3829c1122f5d1c.webp)

[Finjusteringseksempel](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Sammenligning av finjusteringsteknikker

|Scenario|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Tilpasning av forhåndstrente LLM-er til spesifikke oppgaver eller domener|Ja|Ja|Ja|Ja|Ja|Ja|
|Finjustering for NLP-oppgaver som tekstoppsummering, navngitt enhetsgjenkjenning og maskinoversettelse|Ja|Ja|Ja|Ja|Ja|Ja|
|Finjustering for QA-oppgaver|Ja|Ja|Ja|Ja|Ja|Ja|
|Finjustering for å generere menneskelignende svar i chatboter|Ja|Ja|Ja|Ja|Ja|Ja|
|Finjustering for å generere musikk, kunst eller andre former for kreativitet|Ja|Ja|Ja|Ja|Ja|Ja|
|Reduksjon av beregnings- og kostnadsutgifter|Ja|Ja|Ja|Ja|Ja|Ja|
|Reduksjon av minnebruk|Ja|Ja|Ja|Ja|Ja|Ja|
|Bruk av færre parametere for effektiv finjustering|Ja|Ja|Ja|Nei|Nei|Ja|
|Minnesparende form for dataparallellitet som gir tilgang til den samlede GPU-minnet til alle tilgjengelige GPU-enheter|Nei|Nei|Nei|Ja|Ja|Nei|

> [!NOTE]
> LoRA, QLoRA, PEFT og DoRA er parametereffektive finjusteringsmetoder, mens DeepSpeed og ZeRO fokuserer på distribuert trening og minneoptimalisering.

## Eksempler på finjusteringsytelse

![Finetuning Performance](../../../../translated_images/no/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->