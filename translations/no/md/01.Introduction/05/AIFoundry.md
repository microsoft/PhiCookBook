<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7b4235159486df4000e16b7b46ddfec3",
  "translation_date": "2025-05-09T14:59:25+00:00",
  "source_file": "md/01.Introduction/05/AIFoundry.md",
  "language_code": "no"
}
-->
# **Bruke Azure AI Foundry for evaluering**

![aistudo](../../../../../translated_images/AIFoundry.61da8c74bccc0241ce9a4cb53a170912245871de9235043afcb796ccbc076fdc.no.png)

Hvordan evaluere din generative AI-applikasjon ved hjelp av [Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Enten du vurderer enkle eller flerstegs samtaler, tilbyr Azure AI Foundry verktøy for å evaluere modellens ytelse og sikkerhet.

![aistudo](../../../../../translated_images/AIPortfolio.5aaa2b25e9157624a4542fe041d66a96a1c1ec6007e4e5aadd926c6ec8ce18b3.no.png)

## Hvordan evaluere generative AI-apper med Azure AI Foundry
For mer detaljert veiledning, se [Azure AI Foundry-dokumentasjonen](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Her er trinnene for å komme i gang:

## Evaluering av generative AI-modeller i Azure AI Foundry

**Forutsetninger**

- Et testdatasett i CSV- eller JSON-format.
- En distribuert generativ AI-modell (som Phi-3, GPT 3.5, GPT 4 eller Davinci-modeller).
- En runtime med en compute-instans for å kjøre evalueringen.

## Innebygde evalueringsmetoder

Azure AI Foundry lar deg evaluere både enkle og komplekse, flerstegs samtaler.  
For Retrieval Augmented Generation (RAG)-scenarier, hvor modellen er basert på spesifikk data, kan du vurdere ytelsen med innebygde evalueringsmetoder.  
I tillegg kan du evaluere generelle enkle spørsmål-og-svar-scenarier (ikke-RAG).

## Opprette en evalueringskjøring

Fra Azure AI Foundry UI, gå til enten Evaluate-siden eller Prompt Flow-siden.  
Følg veiviseren for å sette opp en evalueringskjøring. Gi et valgfritt navn til evalueringen din.  
Velg scenarioet som samsvarer med målene til applikasjonen din.  
Velg ett eller flere evalueringsmetoder for å vurdere modellens output.

## Tilpasset evalueringsflyt (valgfritt)

For større fleksibilitet kan du opprette en tilpasset evalueringsflyt. Tilpass evalueringsprosessen basert på dine spesifikke behov.

## Se resultater

Etter å ha kjørt evalueringen, logg, se og analyser detaljerte evalueringsmetrikker i Azure AI Foundry. Få innsikt i applikasjonens evner og begrensninger.

**Note** Azure AI Foundry er foreløpig i offentlig forhåndsvisning, så bruk det til eksperimentering og utvikling. For produksjonsarbeidsbelastninger, vurder andre alternativer. Utforsk den offisielle [AI Foundry-dokumentasjonen](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) for mer informasjon og trinnvise instruksjoner.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved bruk av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.