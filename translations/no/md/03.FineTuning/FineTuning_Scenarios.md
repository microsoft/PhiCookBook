<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cb5648935f63edc17e95ce38f23adc32",
  "translation_date": "2025-05-09T21:56:03+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Scenarios.md",
  "language_code": "no"
}
-->
## Finjusteringsscenarier

![Finjustering med MS-tjenester](../../../../translated_images/FinetuningwithMS.25759a0154a97ad90e43a6cace37d6bea87f0ac0236ada3ad5d4a1fbacc3bdf7.no.png)

**Plattform** Dette inkluderer ulike teknologier som Azure AI Foundry, Azure Machine Learning, AI-verktøy, Kaito og ONNX Runtime.

**Infrastruktur** Dette inkluderer CPU og FPGA, som er essensielle for finjusteringsprosessen. La meg vise deg ikonene for hver av disse teknologiene.

**Verktøy og rammeverk** Dette inkluderer ONNX Runtime og ONNX Runtime. La meg vise deg ikonene for hver av disse teknologiene.  
[Sett inn ikoner for ONNX Runtime og ONNX Runtime]

Finjusteringsprosessen med Microsoft-teknologier involverer ulike komponenter og verktøy. Ved å forstå og bruke disse teknologiene kan vi effektivt finjustere applikasjonene våre og lage bedre løsninger.

## Modell som tjeneste

Finjuster modellen ved hjelp av hostet finjustering, uten behov for å opprette og administrere datakraft.

![MaaS Finjustering](../../../../translated_images/MaaSfinetune.6184d80a336ea9d7bb67a581e9e5d0b021cafdffff7ba257c2012e2123e0d77e.no.png)

Serverløs finjustering er tilgjengelig for Phi-3-mini og Phi-3-medium modeller, noe som gjør det mulig for utviklere å raskt og enkelt tilpasse modellene for sky- og edge-scenarier uten å måtte ordne med datakraft. Vi har også annonsert at Phi-3-small nå er tilgjengelig gjennom vårt Models-as-a-Service-tilbud, slik at utviklere raskt og enkelt kan komme i gang med AI-utvikling uten å måtte håndtere underliggende infrastruktur.

## Modell som plattform

Brukere administrerer sin egen datakraft for å finjustere modellene sine.

![Maap Finjustering](../../../../translated_images/MaaPFinetune.cf8b08ef05bf57f362da90834be87562502f4370de4a7325a9fb03b8c008e5e7.no.png)

[Finjusteringseksempel](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Finjusteringsscenarier

| | | | | | | |
|-|-|-|-|-|-|-|
|Scenario|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|Tilpasse forhåndstrente LLM-er til spesifikke oppgaver eller domener|Ja|Ja|Ja|Ja|Ja|Ja|
|Finjustering for NLP-oppgaver som tekstklassifisering, navngitt entity-gjenkjenning og maskinoversettelse|Ja|Ja|Ja|Ja|Ja|Ja|
|Finjustering for QA-oppgaver|Ja|Ja|Ja|Ja|Ja|Ja|
|Finjustering for å generere menneskelignende svar i chatboter|Ja|Ja|Ja|Ja|Ja|Ja|
|Finjustering for å generere musikk, kunst eller andre former for kreativitet|Ja|Ja|Ja|Ja|Ja|Ja|
|Redusere beregnings- og kostnadsnivå|Ja|Ja|Nei|Ja|Ja|Nei|
|Redusere minnebruk|Nei|Ja|Nei|Ja|Ja|Ja|
|Bruke færre parametere for effektiv finjustering|Nei|Ja|Ja|Nei|Nei|Ja|
|Minneeffektiv form for dataparellisme som gir tilgang til samlet GPU-minne på alle tilgjengelige GPU-enheter|Nei|Nei|Nei|Ja|Ja|Ja|

## Eksempler på finjusteringsytelse

![Finjusteringsytelse](../../../../translated_images/Finetuningexamples.9dbf84557eef43e011eb7cadf51f51686f9245f7953e2712a27095ab7d18a6d1.no.png)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.