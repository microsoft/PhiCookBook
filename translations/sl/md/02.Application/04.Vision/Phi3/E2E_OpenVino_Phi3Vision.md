<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-07-17T05:06:12+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "sl"
}
-->
Ta predstavitev prikazuje, kako uporabiti predhodno naučen model za generiranje Python kode na podlagi slike in besedilnega poziva.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Tukaj je po korakih razlaga:

1. **Uvozi in nastavitev**:
   - Uvožene so potrebne knjižnice in moduli, vključno z `requests`, `PIL` za obdelavo slik in `transformers` za upravljanje modela in procesiranje.

2. **Nalaganje in prikaz slike**:
   - Slika (`demo.png`) se odpre z uporabo knjižnice `PIL` in prikaže.

3. **Določitev poziva**:
   - Ustvari se sporočilo, ki vključuje sliko in zahtevo za generiranje Python kode za obdelavo slike in njeno shranjevanje z uporabo `plt` (matplotlib).

4. **Nalaganje procesorja**:
   - `AutoProcessor` se naloži iz predhodno naučenega modela, ki je shranjen v mapi `out_dir`. Ta procesor bo obdelal besedilne in slikovne vnose.

5. **Ustvarjanje poziva**:
   - Metoda `apply_chat_template` se uporabi za oblikovanje sporočila v poziv, primeren za model.

6. **Procesiranje vhodov**:
   - Poziv in slika se pretvorita v tenzorje, ki jih model lahko razume.

7. **Nastavitev argumentov za generiranje**:
   - Določeni so argumenti za proces generiranja modela, vključno z največjim številom novih tokenov za generiranje in ali naj se izhod vzorči.

8. **Generiranje kode**:
   - Model generira Python kodo na podlagi vhodov in nastavljenih argumentov. Za upravljanje izhoda se uporablja `TextStreamer`, ki preskoči poziv in posebne tokene.

9. **Izhod**:
   - Izpisana je generirana koda, ki naj bi vsebovala Python kodo za obdelavo slike in njeno shranjevanje, kot je določeno v pozivu.

Ta predstavitev prikazuje, kako izkoristiti predhodno naučen model z uporabo OpenVino za dinamično generiranje kode na podlagi uporabniškega vnosa in slik.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.