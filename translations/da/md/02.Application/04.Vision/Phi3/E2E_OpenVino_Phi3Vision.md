Denne demo viser, hvordan man bruger en forudtrænet model til at generere Python-kode baseret på et billede og en tekstprompt.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Her er en trin-for-trin forklaring:

1. **Imports og opsætning**:
   - De nødvendige biblioteker og moduler importeres, herunder `requests`, `PIL` til billedbehandling og `transformers` til håndtering af modellen og processen.

2. **Indlæsning og visning af billedet**:
   - En billedfil (`demo.png`) åbnes med `PIL`-biblioteket og vises.

3. **Definering af prompten**:
   - En besked oprettes, som inkluderer billedet og en anmodning om at generere Python-kode til at behandle billedet og gemme det ved hjælp af `plt` (matplotlib).

4. **Indlæsning af processoren**:
   - `AutoProcessor` indlæses fra en forudtrænet model, der er angivet i `out_dir`-mappen. Denne processor håndterer tekst- og billedinput.

5. **Oprettelse af prompten**:
   - Metoden `apply_chat_template` bruges til at formatere beskeden til en prompt, der passer til modellen.

6. **Behandling af input**:
   - Prompten og billedet behandles til tensorer, som modellen kan forstå.

7. **Indstilling af genereringsparametre**:
   - Parametre for modellens genereringsproces defineres, herunder det maksimale antal nye tokens, der skal genereres, og om output skal samples.

8. **Generering af koden**:
   - Modellen genererer Python-koden baseret på input og genereringsparametre. `TextStreamer` bruges til at håndtere outputtet, hvor prompt og specialtegn springes over.

9. **Output**:
   - Den genererede kode printes, og den bør indeholde Python-kode til at behandle billedet og gemme det som angivet i prompten.

Denne demo illustrerer, hvordan man kan udnytte en forudtrænet model med OpenVino til dynamisk at generere kode baseret på brugerinput og billeder.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.