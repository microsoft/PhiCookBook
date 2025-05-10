<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-05-09T20:02:51+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "hr"
}
-->
Ovaj demo prikazuje kako koristiti unaprijed istrenirani model za generiranje Python koda na temelju slike i tekstualnog upita.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Evo objašnjenja korak po korak:

1. **Uvozi i postavljanje**:
   - Uvoze se potrebne biblioteke i moduli, uključujući `requests`, `PIL` za obradu slike te `transformers` za rad s modelom i procesiranje.

2. **Učitavanje i prikaz slike**:
   - Otvara se datoteka slike (`demo.png`) pomoću biblioteke `PIL` i prikazuje se.

3. **Definiranje upita**:
   - Kreira se poruka koja uključuje sliku i zahtjev za generiranjem Python koda za obradu slike i spremanje pomoću `plt` (matplotlib).

4. **Učitavanje procesora**:
   - `AutoProcessor` se učitava iz unaprijed istreniranog modela smještenog u direktoriju `out_dir`. Taj procesor će obrađivati tekstualne i slikovne ulaze.

5. **Kreiranje upita**:
   - Metoda `apply_chat_template` koristi se za formatiranje poruke u upit prikladan za model.

6. **Obrada ulaza**:
   - Upit i slika se pretvaraju u tenzore koje model može razumjeti.

7. **Postavljanje argumenata generiranja**:
   - Definiraju se argumenti za proces generiranja modela, uključujući maksimalan broj novih tokena za generiranje i hoće li se koristiti uzorkovanje izlaza.

8. **Generiranje koda**:
   - Model generira Python kod na temelju ulaza i postavljenih argumenata. Za obradu izlaza koristi se `TextStreamer`, koji preskače upit i posebne tokene.

9. **Izlaz**:
   - Ispisuje se generirani kod, koji bi trebao sadržavati Python kod za obradu slike i spremanje prema uputama iz upita.

Ovaj demo pokazuje kako iskoristiti unaprijed istrenirani model koristeći OpenVino za dinamičko generiranje koda na temelju korisničkih unosa i slika.

**Odricanje od odgovornosti**:  
Ovaj dokument preveden je korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.