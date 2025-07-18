<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-07-17T05:04:02+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "no"
}
-->
Denne demoen viser hvordan man bruker en forhåndstrent modell til å generere Python-kode basert på et bilde og en tekstprompt.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Her er en trinnvis forklaring:

1. **Imports og oppsett**:
   - De nødvendige bibliotekene og modulene importeres, inkludert `requests`, `PIL` for bildebehandling, og `transformers` for håndtering av modellen og prosessering.

2. **Laste inn og vise bildet**:
   - En bildefil (`demo.png`) åpnes ved hjelp av `PIL`-biblioteket og vises.

3. **Definere prompten**:
   - En melding opprettes som inkluderer bildet og en forespørsel om å generere Python-kode for å behandle bildet og lagre det ved hjelp av `plt` (matplotlib).

4. **Laste inn prosessoren**:
   - `AutoProcessor` lastes fra en forhåndstrent modell spesifisert av `out_dir`-mappen. Denne prosessoren håndterer tekst- og bildeinput.

5. **Opprette prompten**:
   - Metoden `apply_chat_template` brukes for å formatere meldingen til en prompt som passer for modellen.

6. **Prosessere inputene**:
   - Prompten og bildet prosesseres til tensorer som modellen kan forstå.

7. **Sette generasjonsargumenter**:
   - Argumenter for modellens generasjonsprosess defineres, inkludert maks antall nye tokens som skal genereres og om output skal samples.

8. **Generere koden**:
   - Modellen genererer Python-koden basert på input og generasjonsargumentene. `TextStreamer` brukes for å håndtere output, og hopper over prompt og spesialtegn.

9. **Output**:
   - Den genererte koden skrives ut, og skal inkludere Python-kode for å behandle bildet og lagre det som spesifisert i prompten.

Denne demoen illustrerer hvordan man kan utnytte en forhåndstrent modell med OpenVino for å generere kode dynamisk basert på brukerinput og bilder.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.