<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-07-09T18:50:15+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sl"
}
-->
# Prispevanje

Ta projekt sprejema prispevke in predloge. Večina prispevkov zahteva, da se strinjate s Contributor License Agreement (CLA), s katerim izjavite, da imate pravico in dejansko omogočate uporabo vašega prispevka. Za podrobnosti obiščite [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Ko oddate pull request, bo CLA bot samodejno preveril, ali morate predložiti CLA, in ustrezno označil PR (npr. statusni pregled, komentar). Preprosto sledite navodilom bota. To boste morali storiti le enkrat za vse repozitorije, ki uporabljajo naš CLA.

## Kodeks vedenja

Ta projekt je sprejel [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Za več informacij preberite [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ali pa se obrnite na [opencode@microsoft.com](mailto:opencode@microsoft.com) za dodatna vprašanja ali komentarje.

## Opozorila pri ustvarjanju težav

Prosimo, da ne odpirate GitHub issue-jev za splošna vprašanja podpore, saj je seznam na GitHubu namenjen zahtevam za funkcionalnosti in poročilom o napakah. Tako lažje sledimo dejanskim težavam ali napakam v kodi in ločimo splošno razpravo od same kode.

## Kako prispevati

### Smernice za pull requeste

Ko oddajate pull request (PR) v repozitorij Phi-3 CookBook, upoštevajte naslednje smernice:

- **Razvejajte repozitorij**: Vedno razvejajte repozitorij na svoj račun, preden naredite spremembe.

- **Ločeni pull requesti (PR)**:
  - Vsako vrsto spremembe oddajte v svojem pull requestu. Na primer, popravki napak in posodobitve dokumentacije naj bodo v ločenih PR-jih.
  - Popravki tipkarskih napak in manjše posodobitve dokumentacije se lahko združijo v en PR, kjer je to primerno.

- **Reševanje konfliktov združevanja**: Če vaš pull request kaže konflikte združevanja, posodobite svojo lokalno vejo `main`, da bo usklajena z glavnim repozitorijem, preden naredite spremembe.

- **Oddaja prevodov**: Pri oddaji prevoda poskrbite, da mapa s prevodi vsebuje prevode za vse datoteke iz izvirne mape.

### Smernice za pisanje

Za zagotovitev doslednosti v vseh dokumentih upoštevajte naslednje smernice:

- **Oblika URL-jev**: Vse URL-je ovijte v oglate oklepaje, ki jim sledijo okrogli oklepaji, brez dodatnih presledkov znotraj ali okoli njih. Na primer: `[example](https://www.microsoft.com)`.

- **Relativne povezave**: Za relativne povezave do datotek ali map v trenutni mapi uporabite `./`, za tiste v nadrejeni mapi pa `../`. Na primer: `[example](../../path/to/file)` ali `[example](../../../path/to/file)`.

- **Ne uporabljajte lokalnih nastavitev za države**: Poskrbite, da vaše povezave ne vsebujejo lokalnih nastavitev za države. Na primer, izogibajte se `/en-us/` ali `/en/`.

- **Shranjevanje slik**: Vse slike shranjujte v mapo `./imgs`.

- **Opisna imena slik**: Slike poimenujte opisno z uporabo angleških znakov, številk in vezajev. Na primer: `example-image.jpg`.

## GitHub delovni tokovi

Ko oddate pull request, se sprožijo naslednji delovni tokovi za preverjanje sprememb. Sledite spodnjim navodilom, da zagotovite uspešno opravljenost teh preverjanj:

- [Preveri pokvarjene relativne poti](../..)
- [Preveri, da URL-ji nimajo lokalnih nastavitev](../..)

### Preveri pokvarjene relativne poti

Ta delovni tok zagotavlja, da so vse relativne poti v vaših datotekah pravilne.

1. Da preverite, ali vaše povezave delujejo pravilno, izvedite naslednje korake v VS Code:
    - Postavite kazalec nad katerokoli povezavo v datotekah.
    - Pritisnite **Ctrl + Klik**, da odprete povezavo.
    - Če povezava lokalno ne deluje, bo to sprožilo delovni tok in povezava ne bo delovala tudi na GitHubu.

1. Za odpravo te težave izvedite naslednje korake z uporabo predlog poti, ki jih ponuja VS Code:
    - Vnesite `./` ali `../`.
    - VS Code vam bo ponudil možnosti glede na vneseno.
    - S klikom na želeno datoteko ali mapo sledite poti, da zagotovite pravilnost poti.

Ko dodate pravilno relativno pot, shranite in potisnite spremembe.

### Preveri, da URL-ji nimajo lokalnih nastavitev

Ta delovni tok zagotavlja, da noben spletni URL ne vsebuje lokalnih nastavitev za državo. Ker je ta repozitorij dostopen globalno, je pomembno, da URL-ji ne vsebujejo lokalnih nastavitev vaše države.

1. Za preverjanje, da vaši URL-ji ne vsebujejo lokalnih nastavitev, izvedite naslednje korake:

    - Preverite, ali se v URL-jih pojavljajo nizi, kot so `/en-us/`, `/en/` ali druge jezikovne lokalne nastavitve.
    - Če teh ni, boste ta pregled opravili.

1. Za odpravo te težave izvedite naslednje korake:
    - Odprite datoteko, ki jo je delovni tok označil.
    - Odstranite lokalne nastavitve države iz URL-jev.

Ko odstranite lokalne nastavitve države, shranite in potisnite spremembe.

### Preveri pokvarjene URL-je

Ta delovni tok zagotavlja, da so vsi spletni URL-ji v vaših datotekah delujoči in vračajo statusno kodo 200.

1. Za preverjanje, da vaši URL-ji delujejo pravilno, izvedite naslednje korake:
    - Preverite status URL-jev v vaših datotekah.

2. Za odpravo pokvarjenih URL-jev izvedite naslednje korake:
    - Odprite datoteko, ki vsebuje pokvarjen URL.
    - Posodobite URL na pravilen.

Ko popravite URL-je, shranite in potisnite spremembe.

> [!NOTE]
>
> Lahko se zgodi, da pregled URL-jev ne uspe, čeprav je povezava dostopna. To se lahko zgodi iz več razlogov, med drugim:
>
> - **Omejitve omrežja:** Strežniki GitHub actions imajo lahko omrežne omejitve, ki preprečujejo dostop do določenih URL-jev.
> - **Težave s časovno omejitvijo:** URL-ji, ki se odzovejo prepočasi, lahko sprožijo napako zaradi poteka časa v delovnem toku.
> - **Začasne težave s strežnikom:** Občasni izpadi ali vzdrževanje strežnika lahko začasno onemogočijo dostop do URL-ja med preverjanjem.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.