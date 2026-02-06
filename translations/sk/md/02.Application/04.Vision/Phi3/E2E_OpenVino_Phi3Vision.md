Táto ukážka demonštruje, ako použiť predtrénovaný model na generovanie Python kódu na základe obrázka a textového zadania.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Tu je krok za krokom vysvetlenie:

1. **Importy a nastavenie**:
   - Importujú sa potrebné knižnice a moduly, vrátane `requests`, `PIL` na spracovanie obrázkov a `transformers` na prácu s modelom a spracovanie.

2. **Načítanie a zobrazenie obrázka**:
   - Obrázok (`demo.png`) sa otvorí pomocou knižnice `PIL` a zobrazí sa.

3. **Definovanie zadania**:
   - Vytvorí sa správa, ktorá obsahuje obrázok a požiadavku na vygenerovanie Python kódu na spracovanie obrázka a jeho uloženie pomocou `plt` (matplotlib).

4. **Načítanie procesora**:
   - `AutoProcessor` sa načíta z predtrénovaného modelu určeného adresárom `out_dir`. Tento procesor spracuje textové a obrazové vstupy.

5. **Vytvorenie zadania**:
   - Metóda `apply_chat_template` sa použije na formátovanie správy do podoby vhodnej pre model.

6. **Spracovanie vstupov**:
   - Zadanie a obrázok sa spracujú do tensorov, ktoré model dokáže pochopiť.

7. **Nastavenie argumentov generovania**:
   - Definujú sa parametre pre generovanie modelom, vrátane maximálneho počtu nových tokenov a či sa má výstup náhodne vzorkovať.

8. **Generovanie kódu**:
   - Model vygeneruje Python kód na základe vstupov a nastavených parametrov. Na spracovanie výstupu sa použije `TextStreamer`, ktorý preskočí zadanie a špeciálne tokeny.

9. **Výstup**:
   - Vygenerovaný kód sa vytlačí, mal by obsahovať Python kód na spracovanie obrázka a jeho uloženie podľa zadania.

Táto ukážka ilustruje, ako využiť predtrénovaný model s OpenVino na dynamické generovanie kódu na základe vstupu používateľa a obrázkov.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.