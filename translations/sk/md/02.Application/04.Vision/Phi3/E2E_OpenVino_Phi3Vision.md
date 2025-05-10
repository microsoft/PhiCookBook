<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-05-09T20:02:09+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "sk"
}
-->
Táto ukážka demonštruje, ako použiť predtrénovaný model na generovanie Python kódu na základe obrázka a textového podnetu.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Tu je krok za krokom vysvetlenie:

1. **Importy a nastavenie**:
   - Importujú sa potrebné knižnice a moduly, vrátane `requests`, `PIL` na spracovanie obrázkov a `transformers` na prácu s modelom a spracovanie.

2. **Načítanie a zobrazenie obrázka**:
   - Obrázok (`demo.png`) sa otvorí pomocou knižnice `PIL` a zobrazí sa.

3. **Definovanie podnetu**:
   - Vytvorí sa správa, ktorá obsahuje obrázok a požiadavku na vygenerovanie Python kódu na spracovanie obrázka a jeho uloženie pomocou `plt` (matplotlib).

4. **Načítanie procesora**:
   - `AutoProcessor` sa načíta z predtrénovaného modelu určeného adresárom `out_dir`. Tento procesor spracuje textové a obrazové vstupy.

5. **Vytvorenie podnetu**:
   - Metóda `apply_chat_template` sa použije na formátovanie správy do podnetu vhodného pre model.

6. **Spracovanie vstupov**:
   - Podnet a obrázok sa spracujú na tensory, ktoré model dokáže pochopiť.

7. **Nastavenie argumentov generovania**:
   - Definujú sa argumenty pre generovanie modelom, vrátane maximálneho počtu nových tokenov a či sa má výstup vzorkovať.

8. **Generovanie kódu**:
   - Model vygeneruje Python kód na základe vstupov a argumentov generovania. Na spracovanie výstupu sa použije `TextStreamer`, ktorý preskočí podnet a špeciálne tokeny.

9. **Výstup**:
   - Vygenerovaný kód sa vytlačí, mal by obsahovať Python kód na spracovanie obrázka a jeho uloženie podľa podnetu.

Táto ukážka ilustruje, ako využiť predtrénovaný model pomocou OpenVino na dynamické generovanie kódu na základe vstupu používateľa a obrázkov.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.