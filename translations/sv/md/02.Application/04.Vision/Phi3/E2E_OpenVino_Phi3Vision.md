<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-07-17T05:03:46+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "sv"
}
-->
Denna demo visar hur man använder en förtränad modell för att generera Python-kod baserat på en bild och en textprompt.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Här är en steg-för-steg förklaring:

1. **Imports och uppsättning**:
   - De nödvändiga biblioteken och modulerna importeras, inklusive `requests`, `PIL` för bildbehandling och `transformers` för att hantera modellen och bearbetningen.

2. **Ladda och visa bilden**:
   - En bildfil (`demo.png`) öppnas med `PIL`-biblioteket och visas.

3. **Definiera prompten**:
   - Ett meddelande skapas som inkluderar bilden och en förfrågan om att generera Python-kod för att bearbeta bilden och spara den med `plt` (matplotlib).

4. **Ladda processorn**:
   - `AutoProcessor` laddas från en förtränad modell som anges av katalogen `out_dir`. Denna processor hanterar text- och bildinmatningar.

5. **Skapa prompten**:
   - Metoden `apply_chat_template` används för att formatera meddelandet till en prompt som passar modellen.

6. **Bearbeta indata**:
   - Prompten och bilden bearbetas till tensorer som modellen kan förstå.

7. **Ställ in genereringsargument**:
   - Argument för modellens genereringsprocess definieras, inklusive max antal nya tokens att generera och om utdata ska samplas.

8. **Generera koden**:
   - Modellen genererar Python-koden baserat på indata och genereringsargument. `TextStreamer` används för att hantera utdata, och hoppar över prompten och specialtecken.

9. **Utdata**:
   - Den genererade koden skrivs ut, vilket bör inkludera Python-kod för att bearbeta bilden och spara den enligt prompten.

Denna demo visar hur man kan använda en förtränad modell med OpenVino för att dynamiskt generera kod baserat på användarens inmatning och bilder.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.