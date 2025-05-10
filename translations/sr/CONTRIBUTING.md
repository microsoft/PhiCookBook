<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:45:04+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sr"
}
-->
# Contribuisanje

Ovaj projekat pozdravlja doprinose i sugestije. Većina doprinosa zahteva da se saglasite sa
Contributor License Agreement (CLA) koji potvrđuje da imate pravo i da nam zaista dajete
dozvolu da koristimo vaš doprinos. Za detalje posetite [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Kada pošaljete pull request, CLA bot će automatski odrediti da li treba da dostavite
CLA i odgovarajuće obeležiti PR (npr. status check, komentar). Jednostavno pratite uputstva
koja daje bot. Ovo je potrebno uraditi samo jednom za sve repozitorijume koji koriste naš CLA.

## Kodeks ponašanja

Ovaj projekat je usvojio [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Za više informacija pročitajte [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ili kontaktirajte [opencode@microsoft.com](mailto:opencode@microsoft.com) za dodatna pitanja ili komentare.

## Upozorenja za kreiranje problema

Molimo vas da ne otvarate GitHub issues za opšta pitanja podrške jer se GitHub lista koristi za zahteve za funkcionalnost i prijave grešaka. Na ovaj način možemo lakše pratiti stvarne probleme ili bagove u kodu i držati opštu diskusiju odvojenu od samog koda.

## Kako doprineti

### Pravila za pull requestove

Kada šaljete pull request (PR) u Phi-3 CookBook repozitorijum, molimo vas da koristite sledeće smernice:

- **Forkujte repozitorijum**: Uvek prvo forkujte repozitorijum na svoj nalog pre nego što napravite izmene.

- **Odvojeni pull requestovi (PR)**:
  - Pošaljite svaki tip izmene u posebnom pull requestu. Na primer, ispravke grešaka i ažuriranja dokumentacije treba da budu u odvojenim PR-ovima.
  - Ispravke tipfelera i manje izmene dokumentacije mogu se spojiti u jedan PR gde je to prikladno.

- **Rešavanje konflikata spajanja**: Ako vaš pull request pokazuje konflikte pri spajanju, ažurirajte lokalnu `main` granu da odgovara glavnom repozitorijumu pre nego što napravite izmene.

- **Podnošenje prevoda**: Kada šaljete prevod, proverite da prevodilačka fascikla sadrži prevode za sve fajlove iz originalne fascikle.

### Smernice za prevod

> [!IMPORTANT]
>
> Prilikom prevođenja teksta u ovom repozitorijumu, nemojte koristiti mašinski prevod. Prevode pravite samo za jezike u kojima ste stručni.

Ako ste vešti u nekom jeziku osim engleskog, možete pomoći sa prevodom sadržaja. Pratite sledeće korake da bi vaši prevodi bili pravilno integrisani:

- **Kreirajte prevodilačku fasciklu**: Idite do odgovarajuće fascikle sekcije i napravite prevodilačku fasciklu za jezik na koji doprinosite. Na primer:
  - Za uvodnu sekciju: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Za sekciju brzog početka: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Nastavite ovim redosledom za ostale sekcije (03.Inference, 04.Finetuning, itd.)

- **Ažurirajte relativne putanje**: Prilikom prevođenja, prilagodite strukturu fascikli dodavanjem `../../` na početak relativnih putanja u markdown fajlovima da bi linkovi pravilno funkcionisali. Na primer, promenite:
  - `(../../imgs/01/phi3aisafety.png)` u `(../../../../imgs/01/phi3aisafety.png)`

- **Organizujte prevode**: Svaki prevedeni fajl treba da bude smešten u odgovarajuću prevodilačku fasciklu sekcije. Na primer, ako prevodite uvodnu sekciju na španski, kreiraćete sledeće:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Pošaljite kompletan PR**: Proverite da svi prevedeni fajlovi za određenu sekciju budu uključeni u jedan PR. Ne prihvatamo delimične prevode za sekciju. Kada šaljete prevod, uverite se da prevodilačka fascikla sadrži prevode za sve fajlove iz originalne fascikle.

### Smernice za pisanje

Da bismo obezbedili doslednost u svim dokumentima, koristite sledeće smernice:

- **Formatiranje URL-ova**: Sve URL-ove stavljajte u uglaste zagrade, a zatim u obične zagrade, bez dodatnih razmaka unutar ili oko njih. Na primer: `[example](https://www.microsoft.com)`.

- **Relativni linkovi**: Koristite `./` za relativne linkove ka fajlovima ili fasciklama u trenutnom direktorijumu, i `../` za one u nadređenom direktorijumu. Na primer: `[example](../../path/to/file)` ili `[example](../../../path/to/file)`.

- **Ne koristite lokalizacije specifične za zemlju**: Proverite da linkovi ne sadrže lokalizacije specifične za zemlju. Na primer, izbegavajte `/en-us/` ili `/en/`.

- **Skladištenje slika**: Sve slike čuvajte u `./imgs` fascikli.

- **Opisna imena slika**: Imenujte slike opisno koristeći engleska slova, brojeve i crtice. Na primer: `example-image.jpg`.

## GitHub radni tokovi

Kada pošaljete pull request, sledeći radni tokovi će se pokrenuti da potvrde izmene. Pratite uputstva ispod da biste osigurali da vaš pull request prođe provere radnog toka:

- [Provera pokvarenih relativnih putanja](../..)
- [Provera da URL-ovi nemaju lokalizaciju](../..)

### Provera pokvarenih relativnih putanja

Ovaj radni tok proverava da su sve relativne putanje u vašim fajlovima ispravne.

1. Da biste proverili da li linkovi funkcionišu, uradite sledeće u VS Code-u:
    - Pređite mišem preko bilo kog linka u fajlovima.
    - Pritisnite **Ctrl + Klik** da otvorite link.
    - Ako link ne radi lokalno, pokrenuće se radni tok i neće raditi na GitHub-u.

1. Da biste rešili ovaj problem, sledite predloge za putanje koje nudi VS Code:
    - Ukucajte `./` ili `../`.
    - VS Code će vam ponuditi opcije na osnovu onoga što ste uneli.
    - Izaberite odgovarajući fajl ili fasciklu da biste osigurali da je putanja tačna.

Kada dodate ispravnu relativnu putanju, sačuvajte i push-ujte izmene.

### Provera da URL-ovi nemaju lokalizaciju

Ovaj radni tok proverava da nijedan web URL ne sadrži lokalizaciju specifičnu za zemlju. Pošto je ovaj repozitorijum dostupan globalno, važno je da URL-ovi ne sadrže lokalizaciju vaše zemlje.

1. Da proverite da URL-ovi nemaju lokalizaciju, uradite sledeće:

    - Proverite da li se u URL-ovima pojavljuju tekstovi kao što su `/en-us/`, `/en/` ili bilo koja druga lokalizacija jezika.
    - Ako ih nema, prolazite ovu proveru.

1. Da rešite ovaj problem, uradite sledeće:
    - Otvorite fajl označen u radnom toku.
    - Uklonite lokalizaciju zemlje iz URL-ova.

Kada uklonite lokalizaciju, sačuvajte i push-ujte izmene.

### Provera pokvarenih URL-ova

Ovaj radni tok proverava da li su svi web URL-ovi u vašim fajlovima aktivni i vraćaju statusni kod 200.

1. Da proverite da URL-ovi rade ispravno, uradite sledeće:
    - Proverite status URL-ova u vašim fajlovima.

2. Da popravite pokvarene URL-ove, uradite sledeće:
    - Otvorite fajl koji sadrži pokvareni URL.
    - Ažurirajte URL na ispravan.

Kada popravite URL-ove, sačuvajte i push-ujte izmene.

> [!NOTE]
>
> Mogu postojati slučajevi kada provera URL-ova ne uspe iako je link dostupan. Razlozi mogu biti:
>
> - **Mrežna ograničenja:** GitHub serverski radni tokovi mogu imati mrežna ograničenja koja sprečavaju pristup određenim URL-ovima.
> - **Problemi sa vremenom čekanja:** URL-ovi koji sporo odgovaraju mogu izazvati timeout grešku u radnom toku.
> - **Privremeni problemi sa serverom:** Povremeni prekidi ili održavanje servera mogu učiniti URL privremeno nedostupnim tokom provere.

**Одрицање од одговорности**:  
Овај документ је преведен помоћу AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде прецизан, молимо вас да имате у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални превод од стране људског преводиоца. Нисмо одговорни за било каква неспоразума или погрешна тумачења настала коришћењем овог превода.