Ovaj demo prikazuje kako koristiti unaprijed istrenirani model za generiranje Python koda na temelju slike i tekstualnog upita.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Evo korak-po-korak objašnjenja:

1. **Uvozi i postavljanje**:
   - Uvoze se potrebne biblioteke i moduli, uključujući `requests`, `PIL` za obradu slika i `transformers` za rad s modelom i obradom.

2. **Učitavanje i prikaz slike**:
   - Otvara se slikovna datoteka (`demo.png`) pomoću `PIL` biblioteke i prikazuje se.

3. **Definiranje upita**:
   - Kreira se poruka koja uključuje sliku i zahtjev za generiranjem Python koda za obradu slike i spremanje pomoću `plt` (matplotlib).

4. **Učitavanje procesora**:
   - `AutoProcessor` se učitava iz unaprijed istreniranog modela navedenog u direktoriju `out_dir`. Ovaj procesor će obrađivati tekstualne i slikovne ulaze.

5. **Kreiranje upita**:
   - Metoda `apply_chat_template` koristi se za formatiranje poruke u upit prikladan za model.

6. **Obrada ulaza**:
   - Upit i slika se obrađuju u tenzore koje model može razumjeti.

7. **Postavljanje argumenata za generiranje**:
   - Definiraju se argumenti za proces generiranja modela, uključujući maksimalan broj novih tokena za generiranje i hoće li se koristiti uzorkovanje izlaza.

8. **Generiranje koda**:
   - Model generira Python kod na temelju ulaza i argumenata za generiranje. `TextStreamer` se koristi za upravljanje izlazom, preskačući upit i posebne tokene.

9. **Izlaz**:
   - Ispisuje se generirani kod, koji bi trebao sadržavati Python kod za obradu slike i spremanje, kako je navedeno u upitu.

Ovaj demo pokazuje kako iskoristiti unaprijed istrenirani model koristeći OpenVino za dinamičko generiranje koda na temelju korisničkog unosa i slika.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.