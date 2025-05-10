<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-05-09T20:02:58+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "sl"
}
-->
Ta demo prikazuje, kako uporabiti vnaprej naučen model za generiranje Python kode na podlagi slike in besedilnega poziva.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Tukaj je razlaga korak za korakom:

1. **Uvozi in nastavitev**:
   - Uvožene so potrebne knjižnice in moduli, vključno z `requests`, `PIL` za obdelavo slik ter `transformers` za upravljanje modela in procesiranje.

2. **Nalaganje in prikaz slike**:
   - Datoteka slike (`demo.png`) se odpre z uporabo knjižnice `PIL` in prikaže.

3. **Določitev poziva**:
   - Ustvari se sporočilo, ki vključuje sliko in zahtevo po generiranju Python kode za obdelavo slike ter shranjevanje z uporabo `plt` (matplotlib).

4. **Nalaganje procesorja**:
   - `AutoProcessor` se naloži iz vnaprej naučenega modela, določenega z direktorijem `out_dir`. Ta procesor bo obdelal besedilo in vhodne slike.

5. **Ustvarjanje poziva**:
   - Metoda `apply_chat_template` se uporabi za oblikovanje sporočila v poziv, primeren za model.

6. **Obdelava vhodov**:
   - Poziv in slika se pretvorita v tenzorje, ki jih model lahko razume.

7. **Nastavitev argumentov generiranja**:
   - Določeni so argumenti za generiranje modela, vključno z največjim številom novih tokenov za generiranje in ali naj se izhod vzorči.

8. **Generiranje kode**:
   - Model generira Python kodo na podlagi vhodov in nastavitev generiranja. `TextStreamer` se uporabi za obdelavo izhoda, pri čemer se preskočijo poziv in posebni tokeni.

9. **Izhod**:
   - Natisnjena je generirana koda, ki naj bi vključevala Python kodo za obdelavo slike in njeno shranjevanje, kot je določeno v pozivu.

Ta demo prikazuje, kako izkoristiti vnaprej naučen model z uporabo OpenVino za dinamično generiranje kode na podlagi uporabniškega vnosa in slik.

**Opozorilo**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitna nesporazumevanja ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.