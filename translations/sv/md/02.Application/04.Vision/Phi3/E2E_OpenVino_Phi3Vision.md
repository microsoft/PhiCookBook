<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-05-09T20:00:37+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "sv"
}
-->
Denna demo visar hur man använder en förtränad modell för att generera Python-kod baserat på en bild och en textprompt.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Här är en steg-för-steg förklaring:

1. **Imports och Setup**:
   - De nödvändiga biblioteken och modulerna importeras, inklusive `requests`, `PIL` för bildbehandling, och `transformers` för hantering av modellen och bearbetning.

2. **Ladda och Visa Bilden**:
   - En bildfil (`demo.png`) öppnas med hjälp av `PIL`-biblioteket och visas.

3. **Definiera Prompten**:
   - Ett meddelande skapas som inkluderar bilden och en förfrågan om att generera Python-kod för att bearbeta bilden och spara den med `plt` (matplotlib).

4. **Ladda Processorn**:
   - `AutoProcessor` laddas från en förtränad modell som anges av `out_dir`-katalogen. Denna processor hanterar text- och bildinmatningar.

5. **Skapa Prompten**:
   - Metoden `apply_chat_template` används för att formatera meddelandet till en prompt som är lämplig för modellen.

6. **Bearbeta Inmatningarna**:
   - Prompten och bilden bearbetas till tensorer som modellen kan förstå.

7. **Ställ in Genereringsargument**:
   - Argument för modellens genereringsprocess definieras, inklusive max antal nya tokens att generera och om output ska samplas.

8. **Generera Koden**:
   - Modellen genererar Python-koden baserat på inmatningarna och genereringsargumenten. `TextStreamer` används för att hantera output, där prompt och specialtecken hoppas över.

9. **Output**:
   - Den genererade koden skrivs ut, vilket bör inkludera Python-kod för att bearbeta bilden och spara den enligt prompten.

Denna demo illustrerar hur man kan utnyttja en förtränad modell med OpenVino för att dynamiskt generera kod baserat på användarinmatning och bilder.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.