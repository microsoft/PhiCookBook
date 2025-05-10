<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-05-09T20:02:44+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "sr"
}
-->
Ovaj demo prikazuje kako koristiti unapred istreniran model za generisanje Python koda na osnovu slike i tekstualnog upita.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Evo objašnjenja korak po korak:

1. **Uvozi i podešavanje**:
   - Potrebne biblioteke i moduli se uvoze, uključujući `requests`, `PIL` za obradu slika, i `transformers` za rukovanje modelom i procesiranje.

2. **Učitavanje i prikaz slike**:
   - Slika (`demo.png`) se otvara koristeći biblioteku `PIL` i prikazuje.

3. **Definisanje upita**:
   - Kreira se poruka koja uključuje sliku i zahtev za generisanjem Python koda za obradu slike i njeno čuvanje koristeći `plt` (matplotlib).

4. **Učitavanje procesora**:
   - `AutoProcessor` se učitava iz unapred istreniranog modela koji je smešten u direktorijumu `out_dir`. Ovaj procesor obrađuje tekstualne i slikovne ulaze.

5. **Kreiranje upita**:
   - Metoda `apply_chat_template` se koristi za formatiranje poruke u upit pogodan za model.

6. **Obrada ulaza**:
   - Upit i slika se obrađuju u tensore koje model može razumeti.

7. **Podešavanje argumenata za generisanje**:
   - Definišu se argumenti za proces generisanja modela, uključujući maksimalan broj novih tokena koje treba generisati i da li se izlaz treba uzorkovati.

8. **Generisanje koda**:
   - Model generiše Python kod na osnovu ulaza i argumenata za generisanje. `TextStreamer` se koristi za obradu izlaza, preskačući upit i specijalne tokene.

9. **Izlaz**:
   - Generisani kod se štampa, koji bi trebalo da sadrži Python kod za obradu slike i njeno čuvanje kako je navedeno u upitu.

Ovaj demo pokazuje kako iskoristiti unapred istreniran model koristeći OpenVino za dinamičko generisanje koda na osnovu korisničkog unosa i slika.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, молимо имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални превод од стране људског преводиоца. Нисмо одговорни за било каква неспоразума или погрешна тумачења настала коришћењем овог превода.