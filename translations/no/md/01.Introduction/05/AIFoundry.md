<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7b4235159486df4000e16b7b46ddfec3",
  "translation_date": "2025-07-16T22:31:57+00:00",
  "source_file": "md/01.Introduction/05/AIFoundry.md",
  "language_code": "no"
}
-->
# **Bruke Azure AI Foundry til evaluering**

![aistudo](../../../../../translated_images/no/AIFoundry.9e0b513e999a1c5a.png)

Hvordan evaluere din generative AI-applikasjon ved hjelp av [Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Enten du vurderer enkle eller komplekse samtaler med flere runder, gir Azure AI Foundry verktøy for å evaluere modellens ytelse og sikkerhet.

![aistudo](../../../../../translated_images/no/AIPortfolio.69da59a8e1eaa70f.png)

## Hvordan evaluere generative AI-apper med Azure AI Foundry
For mer detaljerte instruksjoner, se [Azure AI Foundry-dokumentasjonen](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Her er stegene for å komme i gang:

## Evaluering av generative AI-modeller i Azure AI Foundry

**Forutsetninger**

- Et testdatasett i CSV- eller JSON-format.
- En distribuert generativ AI-modell (som Phi-3, GPT 3.5, GPT 4 eller Davinci-modeller).
- En runtime med en compute-instans for å kjøre evalueringen.

## Innebygde evalueringsmetrikker

Azure AI Foundry lar deg evaluere både enkle og komplekse samtaler med flere runder.  
For Retrieval Augmented Generation (RAG)-scenarier, hvor modellen er basert på spesifikk data, kan du vurdere ytelsen ved hjelp av innebygde evalueringsmetrikker.  
I tillegg kan du evaluere generelle enkle spørsmål-og-svar-scenarier (ikke-RAG).

## Opprette en evalueringskjøring

Fra Azure AI Foundry UI, naviger til enten Evaluate-siden eller Prompt Flow-siden.  
Følg veiviseren for å sette opp en evalueringskjøring. Gi et valgfritt navn til evalueringen din.  
Velg scenariet som samsvarer med målene for applikasjonen din.  
Velg en eller flere evalueringsmetrikker for å vurdere modellens output.

## Tilpasset evalueringsflyt (valgfritt)

For større fleksibilitet kan du opprette en tilpasset evalueringsflyt. Tilpass evalueringsprosessen basert på dine spesifikke behov.

## Se resultater

Etter at evalueringen er kjørt, kan du logge, se og analysere detaljerte evalueringsmetrikker i Azure AI Foundry. Få innsikt i applikasjonens styrker og begrensninger.

**Note** Azure AI Foundry er for øyeblikket i offentlig forhåndsvisning, så bruk det til eksperimentering og utvikling. For produksjonsarbeidsbelastninger bør du vurdere andre alternativer. Utforsk den offisielle [AI Foundry-dokumentasjonen](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) for flere detaljer og trinnvise instruksjoner.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.