# Prisidėjimas

Šis projektas laukia jūsų indėlio ir pasiūlymų. Dauguma indėlių reikalauja, kad sutiktumėte su Contributor License Agreement (CLA), kuriame deklaruojate, jog turite teisę suteikti mums teises naudoti jūsų indėlį. Daugiau informacijos rasite [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com).

Kai pateikiate „pull request“, CLA botas automatiškai nustatys, ar reikia pateikti CLA, ir atitinkamai pažymės PR (pvz., statuso patikrinimu, komentaru). Tiesiog vykdykite boto pateiktas instrukcijas. Tai reikės padaryti tik vieną kartą visuose saugyklose, naudojančiose mūsų CLA.

## Elgesio kodeksas

Šis projektas priėmė [Microsoft atvirojo kodo elgesio kodeksą](https://opensource.microsoft.com/codeofconduct/). Daugiau informacijos rasite [Elgesio kodekso DUK](https://opensource.microsoft.com/codeofconduct/faq/) arba susisiekite el. paštu [opencode@microsoft.com](mailto:opencode@microsoft.com), jei turite papildomų klausimų ar komentarų.

## Atsargumo priemonės kuriant problemas

Prašome nerašyti „GitHub“ problemų dėl bendrų palaikymo klausimų, nes „GitHub“ sąrašas turėtų būti naudojamas funkcijų užklausoms ir klaidų ataskaitoms. Tokiu būdu galime lengviau sekti tikras problemas ar klaidas kode ir atskirti bendrą diskusiją nuo faktinio kodo.

## Kaip prisidėti

### „Pull Request“ gairės

Pateikdami „pull request“ (PR) į Phi-3 CookBook saugyklą, laikykitės šių gairių:

- **Fork saugyklą**: Visada fork'inkite saugyklą į savo paskyrą prieš atlikdami pakeitimus.

- **Atskiri „pull request“ (PR)**:
  - Kiekvieną pakeitimų tipą pateikite atskirame PR. Pavyzdžiui, klaidų taisymai ir dokumentacijos atnaujinimai turėtų būti pateikti atskiruose PR.
  - Rašybos klaidų taisymai ir nedideli dokumentacijos atnaujinimai gali būti sujungti į vieną PR, jei tai tinkama.

- **Spręskite susijungimo konfliktus**: Jei jūsų „pull request“ rodo susijungimo konfliktus, atnaujinkite savo vietinę `main` šaką, kad ji atitiktų pagrindinę saugyklą prieš atlikdami pakeitimus.

- **Vertimų pateikimas**: Pateikdami vertimo PR, įsitikinkite, kad vertimo aplanke yra visų originalaus aplanko failų vertimai.

### Rašymo gairės

Norėdami užtikrinti nuoseklumą visuose dokumentuose, laikykitės šių gairių:

- **URL formatavimas**: Apgaubkite visus URL kvadratiniais skliaustais, po kurių eina skliaustai, be papildomų tarpų aplink ar viduje. Pavyzdžiui: `[example](https://www.microsoft.com)`.

- **Santykinės nuorodos**: Naudokite `./` santykinėms nuorodoms, nukreipiančioms į failus ar aplankus dabartiniame kataloge, ir `../` tiems, kurie yra aukštesniame kataloge. Pavyzdžiui: `[example](../../path/to/file)` arba `[example](../../../path/to/file)`.

- **Ne šalies specifiniai lokalės**: Įsitikinkite, kad jūsų nuorodose nėra šalies specifinių lokalės. Pavyzdžiui, venkite `/en-us/` arba `/en/`.

- **Vaizdų saugojimas**: Visus vaizdus saugokite `./imgs` aplanke.

- **Aprašomieji vaizdų pavadinimai**: Pavadinkite vaizdus aprašomai, naudodami anglų kalbos simbolius, skaičius ir brūkšnelius. Pavyzdžiui: `example-image.jpg`.

## „GitHub“ darbo eigos

Kai pateikiate „pull request“, bus paleistos šios darbo eigos, kad patikrintų pakeitimus. Laikykitės toliau pateiktų instrukcijų, kad jūsų „pull request“ praeitų darbo eigos patikrinimus:

- [Patikrinkite sugadintas santykines nuorodas](../..)
- [Patikrinkite, ar URL neturi lokalės](../..)

### Patikrinkite sugadintas santykines nuorodas

Ši darbo eiga užtikrina, kad visos santykinės nuorodos jūsų failuose yra teisingos.

1. Norėdami įsitikinti, kad jūsų nuorodos veikia tinkamai, atlikite šiuos veiksmus naudodami VS Code:
    - Užveskite pelės žymeklį ant bet kurios nuorodos savo failuose.
    - Paspauskite **Ctrl + Click**, kad pereitumėte prie nuorodos.
    - Jei spustelėsite nuorodą ir ji neveiks lokaliai, tai sukels darbo eigos klaidą ir neveiks „GitHub“.

1. Norėdami išspręsti šią problemą, atlikite šiuos veiksmus naudodami VS Code pateiktas kelio pasiūlymus:
    - Įveskite `./` arba `../`.
    - VS Code pasiūlys pasirinkti iš galimų variantų pagal tai, ką įvedėte.
    - Sekite kelią, spustelėdami norimą failą ar aplanką, kad įsitikintumėte, jog jūsų kelias yra teisingas.

Kai pridėsite teisingą santykinį kelią, išsaugokite ir įkelkite pakeitimus.

### Patikrinkite, ar URL neturi lokalės

Ši darbo eiga užtikrina, kad jokiuose interneto URL nėra šalies specifinės lokalės. Kadangi ši saugykla yra prieinama globaliai, svarbu užtikrinti, kad URL neturėtų jūsų šalies lokalės.

1. Norėdami patikrinti, ar jūsų URL neturi šalies lokalės, atlikite šiuos veiksmus:

    - Patikrinkite tekstą, pvz., `/en-us/`, `/en/` ar bet kurią kitą kalbos lokalę URL.

    - Jei jūsų URL nėra šių lokalės, tada praeisite šį patikrinimą.

1. Norėdami išspręsti šią problemą, atlikite šiuos veiksmus:
    - Atidarykite darbo eigos nurodytą failo kelią.
    - Pašalinkite šalies lokalę iš URL.

Kai pašalinsite šalies lokalę, išsaugokite ir įkelkite pakeitimus.

### Patikrinkite sugadintas URL

Ši darbo eiga užtikrina, kad visi interneto URL jūsų failuose veikia ir grąžina 200 statuso kodą.

1. Norėdami patikrinti, ar jūsų URL veikia tinkamai, atlikite šiuos veiksmus:
    - Patikrinkite URL būseną savo failuose.

2. Norėdami ištaisyti sugadintus URL, atlikite šiuos veiksmus:
    - Atidarykite failą, kuriame yra sugadintas URL.
    - Atnaujinkite URL į teisingą.

Kai ištaisysite URL, išsaugokite ir įkelkite pakeitimus.

> [!NOTE]
>
> Gali būti atvejų, kai URL patikrinimas nepavyksta, nors nuoroda yra pasiekiama. Tai gali nutikti dėl kelių priežasčių, įskaitant:
>
> - **Tinklo apribojimai:** „GitHub“ veiksmų serveriai gali turėti tinklo apribojimų, kurie neleidžia pasiekti tam tikrų URL.
> - **Laiko apribojimo problemos:** URL, kuriems reikia per daug laiko atsakyti, gali sukelti laiko apribojimo klaidą darbo eigoje.
> - **Laikinos serverio problemos:** Kartais serverio prastovos ar priežiūra gali laikinai padaryti URL nepasiekiamą tikrinimo metu.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.