<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:45:24+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "hr"
}
-->
# Contributing

Ovaj projekt prihvaća doprinose i prijedloge. Većina doprinosa zahtijeva da se složite s
Contributor License Agreement (CLA) koji potvrđuje da imate pravo i stvarno nam dajete
prava za korištenje vašeg doprinosa. Za detalje, posjetite [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Kada pošaljete pull request, CLA bot će automatski odrediti trebate li pružiti
CLA i odgovarajuće označiti PR (npr. status check, komentar). Jednostavno slijedite upute
koje daje bot. Ovo je potrebno napraviti samo jednom za sve repozitorije koji koriste naš CLA.

## Code of Conduct

Ovaj projekt je usvojio [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Za više informacija pročitajte [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ili kontaktirajte [opencode@microsoft.com](mailto:opencode@microsoft.com) za dodatna pitanja ili komentare.

## Cautions for creating issues

Molimo vas da ne otvarate GitHub issues za opća pitanja podrške jer se GitHub lista treba koristiti za zahtjeve za nove značajke i prijave bugova. Na taj način lakše pratimo stvarne probleme ili greške u kodu i držimo opću raspravu odvojenu od samog koda.

## How to Contribute

### Pull Requests Guidelines

Prilikom slanja pull requesta (PR) u Phi-3 CookBook repozitorij, molimo koristite sljedeće smjernice:

- **Forkajte repozitorij**: Uvijek forkajte repozitorij na svoj račun prije nego što napravite izmjene.

- **Odvojeni pull requestovi (PR)**:
  - Pošaljite svaki tip promjene u zasebnom pull requestu. Na primjer, ispravci bugova i ažuriranja dokumentacije trebaju biti u odvojenim PR-ovima.
  - Ispravci tipfelera i manja ažuriranja dokumentacije mogu se kombinirati u jedan PR gdje je to prikladno.

- **Rješavanje konflikata spajanja**: Ako vaš pull request pokazuje konflikte pri spajanju, ažurirajte lokalnu `main` granu tako da odgovara glavnom repozitoriju prije nego što napravite izmjene.

- **Slanje prijevoda**: Prilikom slanja PR-a s prijevodom, osigurajte da mapa s prijevodima sadrži prijevode za sve datoteke u izvornom direktoriju.

### Translation Guidelines

> [!IMPORTANT]
>
> Prilikom prevođenja teksta u ovom repozitoriju, nemojte koristiti strojno prevođenje. Prijavite se za prijevode samo na jezicima kojima dobro govorite.

Ako ste vješti u nekom jeziku osim engleskog, možete pomoći s prijevodom sadržaja. Slijedite ove korake kako biste osigurali pravilnu integraciju vaših prijevoda, koristite sljedeće smjernice:

- **Kreirajte mapu za prijevod**: Idite u odgovarajući odjeljak i napravite mapu za prijevod za jezik na koji doprinosite. Na primjer:
  - Za uvodni odjeljak: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Za odjeljak za brzi početak: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Nastavite isti obrazac za ostale odjeljke (03.Inference, 04.Finetuning, itd.)

- **Ažurirajte relativne putanje**: Prilikom prevođenja, prilagodite strukturu mapa dodavanjem `../../` na početak relativnih putanja unutar markdown datoteka kako bi linkovi ispravno funkcionirali. Na primjer, promijenite:
  - `(../../imgs/01/phi3aisafety.png)` u `(../../../../imgs/01/phi3aisafety.png)`

- **Organizirajte svoje prijevode**: Svaka prevedena datoteka treba biti smještena u odgovarajuću mapu za prijevod u okviru sekcije. Na primjer, ako prevodite uvodni odjeljak na španjolski, napravite:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Pošaljite kompletan PR**: Osigurajte da su svi prevedeni dokumenti za određeni odjeljak uključeni u jedan PR. Ne prihvaćamo djelomične prijevode za odjeljak. Prilikom slanja PR-a s prijevodom, provjerite da mapa s prijevodima sadrži prijevode za sve datoteke iz izvornog direktorija.

### Writing Guidelines

Kako bi se osigurala dosljednost u svim dokumentima, molimo koristite sljedeće smjernice:

- **Formatiranje URL-ova**: Stavite sve URL-ove u uglate zagrade, a zatim u okrugle, bez dodatnih razmaka. Na primjer: `[example](https://www.microsoft.com)`.

- **Relativni linkovi**: Koristite `./` za relativne linkove na datoteke ili mape u trenutnom direktoriju, i `../` za one u roditeljskom direktoriju. Na primjer: `[example](../../path/to/file)` ili `[example](../../../path/to/file)`.

- **Ne koristiti lokalizacije specifične za zemlju**: Provjerite da linkovi ne sadrže lokalizacije specifične za zemlju. Na primjer, izbjegavajte `/en-us/` ili `/en/`.

- **Pohrana slika**: Sve slike spremite u `./imgs` mapu.

- **Opisna imena slika**: Imenovanje slika treba biti opisno koristeći engleske znakove, brojeve i crtice. Na primjer: `example-image.jpg`.

## GitHub Workflows

Kada pošaljete pull request, sljedeći workflow-i će se pokrenuti kako bi provjerili promjene. Slijedite upute ispod kako bi vaš pull request prošao provjere workflow-a:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Ovaj workflow provjerava jesu li sve relativne putanje u vašim datotekama ispravne.

1. Kako biste bili sigurni da linkovi rade ispravno, napravite sljedeće u VS Code-u:
    - Postavite pokazivač miša na bilo koji link u datotekama.
    - Pritisnite **Ctrl + Click** da biste otvorili link.
    - Ako kliknete na link i on ne radi lokalno, workflow će se pokrenuti i neće raditi na GitHubu.

1. Za ispravljanje problema, koristite prijedloge putanja koje nudi VS Code:
    - Upisujte `./` ili `../`.
    - VS Code će vam ponuditi opcije na temelju onoga što ste upisali.
    - Slijedite put klikom na željenu datoteku ili mapu kako biste bili sigurni da je put ispravan.

Nakon što ste dodali ispravnu relativnu putanju, spremite i pushajte promjene.

### Check URLs Don't Have Locale

Ovaj workflow provjerava da web URL-ovi ne sadrže lokalizaciju specifičnu za zemlju. Kako je ovaj repozitorij dostupan globalno, važno je da URL-ovi ne sadrže lokalizaciju vaše zemlje.

1. Kako biste provjerili da URL-ovi nemaju lokalizacije, napravite sljedeće:

    - Provjerite ima li u URL-ovima tekst poput `/en-us/`, `/en/` ili drugih jezičnih lokalizacija.
    - Ako ih nema, proći ćete ovu provjeru.

1. Za ispravljanje problema, napravite sljedeće:
    - Otvorite datoteku koju workflow označi.
    - Uklonite lokalizaciju zemlje iz URL-ova.

Nakon uklanjanja lokalizacije, spremite i pushajte promjene.

### Check Broken Urls

Ovaj workflow provjerava rade li svi web URL-ovi u vašim datotekama i vraćaju statusni kod 200.

1. Kako biste provjerili rade li URL-ovi ispravno, napravite sljedeće:
    - Provjerite status URL-ova u vašim datotekama.

2. Za ispravljanje neispravnih URL-ova, napravite sljedeće:
    - Otvorite datoteku koja sadrži neispravan URL.
    - Ažurirajte URL na ispravan.

Nakon što ste popravili URL-ove, spremite i pushajte promjene.

> [!NOTE]
>
> Mogu postojati slučajevi kada provjera URL-ova ne uspije iako je link dostupan. To može biti zbog:
>
> - **Mrežnih ograničenja:** GitHub akcijski serveri mogu imati mrežna ograničenja koja sprječavaju pristup nekim URL-ovima.
> - **Problemi s vremenom odziva:** URL-ovi koji sporo odgovaraju mogu izazvati timeout grešku u workflow-u.
> - **Privremeni problemi na serveru:** Povremeni prekidi rada ili održavanje servera mogu privremeno učiniti URL nedostupnim tijekom provjere.

**Odricanje od odgovornosti**:  
Ovaj dokument preveden je pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.