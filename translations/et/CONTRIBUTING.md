<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-10-11T11:29:58+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "et"
}
-->
# Kaastöö

See projekt ootab kaastööd ja ettepanekuid. Enamik kaastöid nõuab, et nõustuksite Kaastöö Litsentsilepinguga (CLA), mis kinnitab, et teil on õigus anda meile õigused teie panuse kasutamiseks. Lisateabe saamiseks külastage [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com).

Kui esitate tõmbenõude (pull request), määrab CLA bot automaatselt, kas peate CLA-d esitama, ja märgistab PR-i vastavalt (nt olekukontroll, kommentaar). Järgige lihtsalt boti antud juhiseid. Seda peate tegema ainult üks kord kõigi meie CLA-d kasutavate repositooriumide puhul.

## Käitumisjuhend

See projekt on omaks võtnud [Microsofti avatud lähtekoodi käitumisjuhendi](https://opensource.microsoft.com/codeofconduct/). Lisateabe saamiseks lugege [käitumisjuhendi KKK-d](https://opensource.microsoft.com/codeofconduct/faq/) või võtke ühendust [opencode@microsoft.com](mailto:opencode@microsoft.com), kui teil on täiendavaid küsimusi või kommentaare.

## Ettevaatusabinõud probleemide loomisel

Palun ärge avage GitHubi probleeme üldiste tugiküsimuste jaoks, kuna GitHubi loendit tuleks kasutada funktsioonisoovide ja veateadete jaoks. Nii saame hõlpsamini jälgida tegelikke probleeme või vigu koodis ja hoida üldise arutelu eraldi tegelikust koodist.

## Kuidas panustada

### Tõmbenõuete juhised

Kui esitate tõmbenõude (PR) Phi-3 CookBook repositooriumile, järgige järgmisi juhiseid:

- **Forkige repositoorium**: Forkige alati repositoorium oma kontole enne muudatuste tegemist.

- **Eraldi tõmbenõuded (PR)**:
  - Esitage iga muudatuse tüüp eraldi tõmbenõudes. Näiteks veaparandused ja dokumentatsiooni uuendused tuleks esitada eraldi PR-ides.
  - Tippveaparandused ja väiksemad dokumentatsiooni uuendused võivad vajadusel olla kombineeritud ühte PR-i.

- **Lahendage ühinemiskonfliktid**: Kui teie tõmbenõue näitab ühinemiskonflikte, värskendage oma kohalikku `main` haru, et see peegeldaks peamist repositooriumi enne muudatuste tegemist.

- **Tõlke esitamine**: Kui esitate tõlke PR-i, veenduge, et tõlkefolder sisaldaks tõlkeid kõigile originaalfailide folderis olevatele failidele.

### Kirjutamise juhised

Konsistentsi tagamiseks kõigis dokumentides kasutage järgmisi juhiseid:

- **URL-i vormindamine**: Ümbritsege kõik URL-id nurksulgudega, millele järgneb sulgudes olev link, ilma lisaruumideta nende ümber või sees. Näiteks: `[näide](https://www.microsoft.com)`.

- **Suhtelised lingid**: Kasutage `./` suhteliste linkide jaoks, mis viitavad failidele või folderitele praeguses kataloogis, ja `../` nende jaoks, mis asuvad ülemises kataloogis. Näiteks: `[näide](../../path/to/file)` või `[näide](../../../path/to/file)`.

- **Mitte riigispetsiifilised lokaadid**: Veenduge, et teie lingid ei sisaldaks riigispetsiifilisi lokaate. Näiteks vältige `/en-us/` või `/en/`.

- **Piltide salvestamine**: Salvestage kõik pildid `./imgs` folderisse.

- **Kirjeldavad pildinimed**: Nimetage pildid kirjeldavalt, kasutades ingliskeelseid tähemärke, numbreid ja kriipse. Näiteks: `näide-pilt.jpg`.

## GitHubi töövood

Kui esitate tõmbenõude, käivitatakse järgmised töövood muudatuste valideerimiseks. Järgige allolevaid juhiseid, et tagada teie tõmbenõude läbimine töövoo kontrollidest:

- [Kontrollige katkiseid suhtelisi teid](../..)
- [Kontrollige, et URL-id ei sisaldaks lokaate](../..)

### Kontrollige katkiseid suhtelisi teid

See töövoog tagab, et kõik suhtelised teed teie failides on õiged.

1. Veendumaks, et teie lingid töötavad korralikult, tehke järgmised toimingud VS Code'is:
    - Liikuge hiirega üle mis tahes lingi oma failides.
    - Vajutage **Ctrl + Click**, et lingile navigeerida.
    - Kui klõpsate lingil ja see ei tööta kohapeal, käivitab see töövoo ja ei tööta GitHubis.

1. Selle probleemi lahendamiseks tehke järgmised toimingud, kasutades VS Code'i pakutud teesoovitusi:
    - Sisestage `./` või `../`.
    - VS Code kuvab valikud, mille hulgast valida, lähtudes teie sisestusest.
    - Järgige teed, klõpsates soovitud failil või folderil, et tagada teie tee õigsus.

Kui olete lisanud õige suhtelise tee, salvestage ja lükake oma muudatused üles.

### Kontrollige, et URL-id ei sisaldaks lokaate

See töövoog tagab, et ükski veebiaadress ei sisalda riigispetsiifilist lokaati. Kuna see repositoorium on globaalselt kättesaadav, on oluline tagada, et URL-id ei sisaldaks teie riigi lokaati.

1. Veendumaks, et teie URL-id ei sisalda riigilokaate, tehke järgmised toimingud:

    - Kontrollige tekstide `/en-us/`, `/en/` või mis tahes muu keele lokaadi olemasolu URL-ides.
    - Kui need ei esine teie URL-ides, siis läbite selle kontrolli.

1. Selle probleemi lahendamiseks tehke järgmised toimingud:
    - Avage töövoo poolt esile tõstetud failitee.
    - Eemaldage URL-idest riigilokaadid.

Kui olete riigilokaadid eemaldanud, salvestage ja lükake oma muudatused üles.

### Kontrollige katkiseid URL-e

See töövoog tagab, et kõik veebiaadressid teie failides töötavad ja tagastavad 200 olekukoodi.

1. Veendumaks, et teie URL-id töötavad õigesti, tehke järgmised toimingud:
    - Kontrollige URL-ide olekut oma failides.

2. Katkiste URL-ide parandamiseks tehke järgmised toimingud:
    - Avage fail, mis sisaldab katkist URL-i.
    - Uuendage URL-i õigele.

Kui olete URL-id parandanud, salvestage ja lükake oma muudatused üles.

> [!NOTE]
>
> Võib esineda juhtumeid, kus URL-i kontroll ebaõnnestub, kuigi link on juurdepääsetav. See võib juhtuda mitmel põhjusel, sealhulgas:
>
> - **Võrgupiirangud:** GitHubi tegevusserveritel võivad olla võrgupiirangud, mis takistavad juurdepääsu teatud URL-idele.
> - **Ajapiirangud:** URL-id, mis reageerivad liiga kaua, võivad töövoos ajapiirangu vea käivitada.
> - **Ajutised serveriprobleemid:** Aeg-ajalt esinev serveri seisak või hooldus võib muuta URL-i valideerimise ajal ajutiselt kättesaamatuks.

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.