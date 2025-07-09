<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-07-09T18:48:55+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "hr"
}
-->
# Doprinos

Ovaj projekt prihvaća doprinose i prijedloge. Većina doprinosa zahtijeva da pristanete na Contributor License Agreement (CLA) kojim izjavljujete da imate pravo i doista nam dajete prava za korištenje vašeg doprinosa. Za detalje posjetite [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Kada pošaljete pull request, CLA bot će automatski provjeriti trebate li dostaviti CLA i označiti PR na odgovarajući način (npr. status check, komentar). Jednostavno slijedite upute koje vam bot daje. Ovo ćete morati napraviti samo jednom za sve repozitorije koji koriste naš CLA.

## Kodeks ponašanja

Ovaj projekt je usvojio [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Za više informacija pročitajte [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ili kontaktirajte [opencode@microsoft.com](mailto:opencode@microsoft.com) za dodatna pitanja ili komentare.

## Upozorenja za kreiranje issue-a

Molimo vas da ne otvarate GitHub issue-e za opća pitanja podrške jer se GitHub lista treba koristiti za zahtjeve za nove značajke i prijave bugova. Na taj način lakše pratimo stvarne probleme ili bugove u kodu i držimo opću raspravu odvojenu od samog koda.

## Kako doprinijeti

### Smjernice za pull requestove

Prilikom slanja pull requesta (PR) u Phi-3 CookBook repozitorij, molimo koristite sljedeće smjernice:

- **Forkajte repozitorij**: Uvijek forkajte repozitorij na svoj račun prije nego što napravite izmjene.

- **Odvojeni pull requestovi (PR)**:
  - Svaku vrstu promjene pošaljite u zasebnom pull requestu. Na primjer, ispravke bugova i ažuriranja dokumentacije trebaju biti u odvojenim PR-ovima.
  - Ispravke tipfelera i manje izmjene dokumentacije mogu se po potrebi kombinirati u jedan PR.

- **Rješavanje konflikata spajanja**: Ako vaš pull request pokazuje konflikte pri spajanju, ažurirajte lokalnu `main` granu da odgovara glavnom repozitoriju prije nego što napravite izmjene.

- **Podnošenje prijevoda**: Prilikom slanja PR-a s prijevodom, provjerite da mapa s prijevodom sadrži prijevode za sve datoteke iz originalne mape.

### Smjernice za pisanje

Kako bismo osigurali dosljednost u svim dokumentima, molimo koristite sljedeće smjernice:

- **Formatiranje URL-ova**: Sve URL-ove stavite u uglate zagrade, a zatim u okrugle zagrade bez dodatnih razmaka oko ili unutar njih. Na primjer: `[example](https://www.microsoft.com)`.

- **Relativne poveznice**: Koristite `./` za relativne poveznice koje upućuju na datoteke ili mape u trenutnom direktoriju, a `../` za one u roditeljskom direktoriju. Na primjer: `[example](../../path/to/file)` ili `[example](../../../path/to/file)`.

- **Ne koristite lokalizacije specifične za zemlju**: Provjerite da vaše poveznice ne sadrže lokalizacije specifične za zemlju. Na primjer, izbjegavajte `/en-us/` ili `/en/`.

- **Spremanje slika**: Sve slike spremite u mapu `./imgs`.

- **Opisni nazivi slika**: Slike imenujte opisno koristeći engleska slova, brojeve i crtice. Na primjer: `example-image.jpg`.

## GitHub radni tokovi

Kada pošaljete pull request, pokrenut će se sljedeći radni tokovi za provjeru promjena. Slijedite upute u nastavku kako biste osigurali da vaš pull request prođe provjere:

- [Provjera ispravnosti relativnih putanja](../..)
- [Provjera da URL-ovi nemaju lokalizaciju](../..)

### Provjera ispravnosti relativnih putanja

Ovaj radni tok osigurava da su sve relativne putanje u vašim datotekama ispravne.

1. Kako biste provjerili rade li vaše poveznice ispravno, napravite sljedeće u VS Code-u:
    - Zadržite pokazivač miša iznad bilo koje poveznice u datotekama.
    - Pritisnite **Ctrl + Klik** da biste otvorili poveznicu.
    - Ako kliknete na poveznicu i ona ne radi lokalno, to će pokrenuti radni tok i neće raditi ni na GitHubu.

1. Za ispravak ovog problema, napravite sljedeće koristeći prijedloge putanja koje nudi VS Code:
    - Upisujte `./` ili `../`.
    - VS Code će vam ponuditi dostupne opcije na temelju onoga što ste upisali.
    - Slijedite putanju klikom na željenu datoteku ili mapu kako biste bili sigurni da je putanja ispravna.

Nakon što ste dodali ispravnu relativnu putanju, spremite i pošaljite promjene.

### Provjera da URL-ovi nemaju lokalizaciju

Ovaj radni tok osigurava da nijedan web URL ne sadrži lokalizaciju specifičnu za zemlju. Budući da je ovaj repozitorij dostupan globalno, važno je osigurati da URL-ovi ne sadrže lokalizaciju vaše zemlje.

1. Kako biste provjerili da vaši URL-ovi nemaju lokalizaciju zemlje, napravite sljedeće:

    - Provjerite ima li u URL-ovima tekst poput `/en-us/`, `/en/` ili bilo koju drugu jezičnu lokalizaciju.
    - Ako ih nema, proći ćete ovu provjeru.

1. Za ispravak ovog problema, napravite sljedeće:
    - Otvorite datoteku čija je putanja označena u radnom toku.
    - Uklonite lokalizaciju zemlje iz URL-ova.

Nakon što uklonite lokalizaciju zemlje, spremite i pošaljite promjene.

### Provjera ispravnosti URL-ova

Ovaj radni tok osigurava da svi web URL-ovi u vašim datotekama rade i vraćaju statusni kod 200.

1. Kako biste provjerili rade li vaši URL-ovi ispravno, napravite sljedeće:
    - Provjerite status URL-ova u vašim datotekama.

2. Za ispravak bilo kojih neispravnih URL-ova, napravite sljedeće:
    - Otvorite datoteku koja sadrži neispravan URL.
    - Ažurirajte URL na ispravan.

Nakon što ste ispravili URL-ove, spremite i pošaljite promjene.

> [!NOTE]
>
> Mogu postojati slučajevi kada provjera URL-ova ne uspije iako je poveznica dostupna. To se može dogoditi iz nekoliko razloga, uključujući:
>
> - **Mrežna ograničenja:** GitHub actions serveri mogu imati mrežna ograničenja koja sprječavaju pristup određenim URL-ovima.
> - **Problemi s vremenom čekanja:** URL-ovi koji sporo odgovaraju mogu izazvati timeout grešku u radnom toku.
> - **Privremeni problemi sa serverom:** Povremeni prekidi rada ili održavanje servera mogu privremeno učiniti URL nedostupnim tijekom provjere.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.