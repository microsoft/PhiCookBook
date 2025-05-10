<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:45:43+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sl"
}
-->
# Contributing

Ta projekt sprejema prispevke in predloge. Večina prispevkov zahteva, da se strinjate s
Contributor License Agreement (CLA), s katerim izjavite, da imate pravico in dejansko dovolite,
da uporabimo vaš prispevek. Za podrobnosti obiščite [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Ko pošljete pull request, bo CLA bot samodejno preveril, ali morate predložiti
CLA in ustrezno označil PR (npr. statusni pregled, komentar). Preprosto sledite navodilom
bota. To boste morali storiti samo enkrat za vse repozitorije, ki uporabljajo naš CLA.

## Code of Conduct

Ta projekt je sprejel [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Za več informacij preberite [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ali kontaktirajte [opencode@microsoft.com](mailto:opencode@microsoft.com) za dodatna vprašanja ali komentarje.

## Cautions for creating issues

Prosim, ne odpirajte GitHub issue-jev za splošna podporna vprašanja, saj je GitHub seznam namenjen zahtevam po novih funkcijah in prijavam napak. Tako bomo lažje spremljali dejanske težave ali napake v kodi in ločili splošno razpravo od dejanske kode.

## How to Contribute

### Pull Requests Guidelines

Ko pošiljate pull request (PR) v Phi-3 CookBook repozitorij, upoštevajte naslednja navodila:

- **Forkajte repozitorij**: Vedno najprej forkajte repozitorij na svoj račun, preden naredite spremembe.

- **Ločeni pull requesti (PR)**:
  - Vsako vrsto spremembe oddajte v svojem pull requestu. Na primer, popravki napak in posodobitve dokumentacije naj bodo v ločenih PR-jih.
  - Popravki tipkarskih napak in manjše posodobitve dokumentacije se lahko združijo v en PR, kjer je to primerno.

- **Reševanje združevanjskih konfliktov**: Če vaš pull request kaže konflikte pri združevanju, posodobite svojo lokalno `main` vejo, da bo ustrezala glavnemu repozitoriju, preden naredite spremembe.

- **Oddaja prevodov**: Pri pošiljanju prevodov poskrbite, da prevajalska mapa vključuje prevode za vse datoteke v izvirni mapi.

### Translation Guidelines

> [!IMPORTANT]
>
> Pri prevajanju besedila v tem repozitoriju ne uporabljajte strojnega prevajanja. Prevajajte samo jezike, v katerih ste vešči.

Če obvladate jezik, ki ni angleščina, lahko pomagate s prevajanjem vsebine. Za pravilno vključitev vaših prevodov sledite tem navodilom:

- **Ustvarite prevajalsko mapo**: Pojdite v ustrezno mapo sekcije in ustvarite prevajalsko mapo za jezik, v katerega prevajate. Na primer:
  - Za uvodno sekcijo: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Za sekcijo hitrega začetka: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Nadaljujte po istem vzorcu za druge sekcije (03.Inference, 04.Finetuning itd.)

- **Posodobite relativne poti**: Pri prevajanju prilagodite strukturo map tako, da dodate `../../` na začetek relativnih poti v markdown datotekah, da bodo povezave pravilno delovale. Na primer, spremenite:
  - `(../../imgs/01/phi3aisafety.png)` v `(../../../../imgs/01/phi3aisafety.png)`

- **Organizirajte prevode**: Vsaka prevedena datoteka naj bo v prevajalski mapi ustrezne sekcije. Na primer, če prevajate uvodno sekcijo v španščino, ustvarite:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Oddajte celovit PR**: Poskrbite, da bo PR vseboval vse prevedene datoteke za določeno sekcijo. Ne sprejemamo delnih prevodov sekcije. Pri prevodih zagotovite, da mapa prevodov vključuje vse datoteke iz izvirne mape.

### Writing Guidelines

Za doslednost vseh dokumentov upoštevajte naslednja navodila:

- **Oblika URL-jev**: Vse URL-je ovijte v oglate oklepaje, ki jim sledijo okrogli oklepaji, brez dodatnih presledkov. Na primer: `[example](https://www.microsoft.com)`.

- **Relativne povezave**: Za relativne povezave do datotek ali map v trenutni mapi uporabite `./`, za tiste v nadrejeni mapi pa `../`. Na primer: `[example](../../path/to/file)` ali `[example](../../../path/to/file)`.

- **Ne uporabljajte lokalnih nastavitev za države**: Preverite, da vaše povezave ne vsebujejo lokalnih nastavitev za države. Na primer, izogibajte se `/en-us/` ali `/en/`.

- **Shranjevanje slik**: Vse slike shranjujte v mapo `./imgs`.

- **Opisna imena slik**: Imena slik naj bodo opisna in naj vsebujejo angleške znake, številke in pomišljaje. Na primer: `example-image.jpg`.

## GitHub Workflows

Ko pošljete pull request, se sprožijo naslednji poteki dela, ki preverijo spremembe. Za uspešno preverjanje sledite spodnjim navodilom:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Ta potek dela preverja, da so vse relativne poti v vaših datotekah pravilne.

1. Za preverjanje delovanja povezav izvedite naslednje korake v VS Code:
    - Postavite kurzor nad katerokoli povezavo v datotekah.
    - Pritisnite **Ctrl + Click**, da odprete povezavo.
    - Če povezava ne deluje lokalno, bo sprožila potek dela in ne bo delovala na GitHubu.

1. Za odpravo težave uporabite predloge poti, ki jih ponuja VS Code:
    - Vnesite `./` ali `../`.
    - VS Code vam bo ponudil možnosti glede na vaš vnos.
    - Kliknite na želeno datoteko ali mapo, da potrdite pravilno pot.

Ko dodate pravilno relativno pot, shranite in potisnite spremembe.

### Check URLs Don't Have Locale

Ta potek dela preverja, da spletni URL-ji ne vsebujejo lokalnih nastavitev za državo. Ker je ta repozitorij dostopen globalno, je pomembno, da URL-ji ne vsebujejo lokalnih nastavitev.

1. Za preverjanje, da URL-ji ne vsebujejo lokalnih nastavitev države, naredite naslednje:

    - Preverite, da v URL-jih ni besedila kot sta `/en-us/`, `/en/` ali drugih lokalnih nastavitev jezika.
    - Če teh ni, boste test opravili.

1. Za odpravo težave naredite naslednje:
    - Odprite datoteko, ki jo je potek dela označil.
    - Odstranite lokalne nastavitve države iz URL-jev.

Ko odstranite lokalne nastavitve države, shranite in potisnite spremembe.

### Check Broken Urls

Ta potek dela preverja, da so vsi spletni URL-ji v vaših datotekah delujoči in vračajo statusno kodo 200.

1. Za preverjanje delovanja URL-jev naredite naslednje:
    - Preverite status URL-jev v datotekah.

2. Za odpravo nedelujočih URL-jev naredite naslednje:
    - Odprite datoteko z nedelujočim URL-jem.
    - Posodobite URL na pravilen.

Ko popravite URL-je, shranite in potisnite spremembe.

> [!NOTE]
>
> Lahko se zgodi, da kljub dostopnosti povezave test URL-jev ne uspe. To se lahko zgodi iz več razlogov, vključno z:
>
> - **Omejitve omrežja:** GitHub actions strežniki imajo lahko omejitve dostopa do nekaterih URL-jev.
> - **Težave s časom odziva:** URL-ji, ki se odzovejo prepočasi, lahko sprožijo timeout napako v poteku dela.
> - **Začasne težave strežnika:** Občasni izpadi ali vzdrževanje strežnika lahko začasno onemogočijo dostop do URL-ja med preverjanjem.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne prevzemamo odgovornosti.