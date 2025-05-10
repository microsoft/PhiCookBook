<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:43:33+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "hu"
}
-->
# Hozzájárulás

Ez a projekt szívesen fogad hozzájárulásokat és javaslatokat. A legtöbb hozzájáruláshoz el kell fogadnod egy Contributor License Agreement (CLA) nevű szerződést, amelyben kijelented, hogy jogod van a hozzájárulásod felhasználására, és ténylegesen meg is adod nekünk ezt a jogot. Részletekért látogass el ide: [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Amikor pull request-et nyújtasz be, egy CLA bot automatikusan eldönti, hogy szükséges-e CLA-t benyújtanod, és megfelelően jelöli a PR-t (például státuszellenőrzéssel vagy kommenttel). Egyszerűen kövesd a bot utasításait. Ezt csak egyszer kell megtenned az összes CLA-t használó repóban.

## Magatartási kódex

Ez a projekt a [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) magatartási kódexet alkalmazza.  
További információért olvasd el a [Code of Conduct GYIK-et](https://opensource.microsoft.com/codeofconduct/faq/) vagy írj az [opencode@microsoft.com](mailto:opencode@microsoft.com) címre kérdéseiddel vagy észrevételeiddel.

## Figyelmeztetések hibajegyek létrehozásához

Kérjük, ne nyiss GitHub hibajegyeket általános támogatási kérdések miatt, mivel a GitHub lista funkciókérések és hibajelentések nyomon követésére szolgál. Így könnyebben tudjuk követni a tényleges kódhibákat, és az általános vitákat elkülöníthetjük a tényleges kódtól.

## Hogyan járulhatsz hozzá

### Pull request irányelvek

Amikor pull request-et (PR) nyújtasz be a Phi-3 CookBook repóba, kérjük, kövesd az alábbi irányelveket:

- **Forkold a repót**: Mindig előbb forkold a repót a saját fiókodba, mielőtt módosításokat végeznél.

- **Különálló pull requestek (PR-ek)**:
  - Minden változtatást külön PR-ben nyújts be. Például hibajavításokat és dokumentációs frissítéseket külön PR-ekben.
  - Helyesírási hibák és kisebb dokumentációs módosítások esetén egy PR-ben is összefoghatók, ha indokolt.

- **Merge konfliktusok kezelése**: Ha a pull request-ed merge konfliktust jelez, frissítsd a helyi `main` ágat, hogy megfeleljen a fő repónak, mielőtt módosításokat végzel.

- **Fordítások beküldése**: Fordítási PR benyújtásakor győződj meg róla, hogy a fordítási mappa tartalmazza az eredeti mappa összes fájljának fordítását.

### Fordítási irányelvek

> [!IMPORTANT]
>
> Amikor ebben a repóban szöveget fordítasz, ne használj gépi fordítást. Csak olyan nyelveken vállalj fordítást, amelyekben jártas vagy.

Ha jártas vagy egy nem angol nyelvben, segíthetsz a tartalom fordításában. A fordításaid megfelelő integrálása érdekében kérjük, kövesd az alábbi irányelveket:

- **Fordítási mappa létrehozása**: Navigálj a megfelelő szakasz mappájába, és hozz létre egy fordítási mappát a nyelved számára. Például:
  - Bevezető szakaszhoz: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Gyors kezdés szakaszhoz: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Folytasd ezt a mintát a többi szakasznál (03.Inference, 04.Finetuning, stb.)

- **Relatív útvonalak frissítése**: Fordítás közben módosítsd a mappaszerkezetet úgy, hogy a markdown fájlokban lévő relatív útvonalak elejére `../../`-t illessz be, hogy a linkek helyesen működjenek. Például:
  - Cseréld le `(../../imgs/01/phi3aisafety.png)`-t `(../../../../imgs/01/phi3aisafety.png)`-re

- **Fordítások rendszerezése**: Minden lefordított fájlt a megfelelő szakasz fordítási mappájába tegyél. Például, ha a bevezető szakaszt fordítod spanyolra, így hozz létre mappát:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Teljes PR benyújtása**: Győződj meg róla, hogy egy PR tartalmazza az adott szakasz összes lefordított fájlját. Nem fogadunk el részleges fordításokat egy szakaszhoz. Fordítási PR benyújtásakor ügyelj arra, hogy a fordítási mappa tartalmazza az eredeti mappa összes fájljának fordítását.

### Írási irányelvek

Az összes dokumentum egységessége érdekében kérjük, tartsd be az alábbi irányelveket:

- **URL formázás**: Minden URL-t zárj szögletes zárójelbe, amit kerek zárójel követ, szóközök nélkül. Például: `[example](https://www.microsoft.com)`.

- **Relatív linkek**: Használd `./`-t relatív linkekhez, amelyek az aktuális könyvtár fájljaira vagy mappáira mutatnak, és `../`-t a szülő könyvtárban lévő fájlokra vagy mappákra. Például: `[example](../../path/to/file)` vagy `[example](../../../path/to/file)`.

- **Nem ország-specifikus lokalizációk**: Ügyelj arra, hogy a linkjeid ne tartalmazzanak ország-specifikus lokalizációkat. Például kerüld a `/en-us/` vagy `/en/` használatát.

- **Képtárolás**: Minden képet a `./imgs` mappában tárolj.

- **Leíró képnevek**: A képek nevei legyenek beszédesek, angol betűket, számokat és kötőjeleket használva. Például: `example-image.jpg`.

## GitHub munkafolyamatok

Amikor pull request-et nyújtasz be, az alábbi munkafolyamatok indulnak el a változtatások érvényesítésére. Kövesd az alábbi utasításokat, hogy a PR-ed átmenjen a munkafolyamat ellenőrzéseken:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Ez a munkafolyamat biztosítja, hogy az összes relatív útvonal a fájljaidban helyes legyen.

1. A linkjeid helyes működésének ellenőrzéséhez végezd el a következőket VS Code használatával:
    - Mozgasd az egeret bármelyik link fölé a fájlokban.
    - Nyomd meg a **Ctrl + Klikk** kombinációt, hogy a linkre navigálj.
    - Ha a link helyileg nem működik, a munkafolyamat elindul, és GitHubon sem fog működni.

1. A hiba javításához használd a VS Code által javasolt útvonalakat:
    - Írd be `./` vagy `../`.
    - A VS Code felajánlja a választható lehetőségeket az általad begépelt alapján.
    - Kattints a kívánt fájlra vagy mappára, hogy biztosítsd az útvonal helyességét.

Ha megadtad a helyes relatív útvonalat, mentsd el és push-old a változtatásokat.

### Check URLs Don't Have Locale

Ez a munkafolyamat ellenőrzi, hogy a webes URL-ek ne tartalmazzanak ország-specifikus lokalizációt. Mivel ez a repó globálisan elérhető, fontos, hogy az URL-ek ne tartalmazzanak az országodhoz kötött lokalizációt.

1. Az URL-ek ellenőrzéséhez végezd el a következőket:

    - Keress olyan szövegeket, mint `/en-us/`, `/en/` vagy bármilyen más nyelvi lokalizáció az URL-ekben.
    - Ha nem találsz ilyeneket az URL-ekben, átmentél az ellenőrzésen.

1. A probléma javításához:

    - Nyisd meg a munkafolyamat által kiemelt fájlútvonalat.
    - Távolítsd el az ország-specifikus lokalizációt az URL-ekből.

Ha eltávolítottad a lokalizációt, mentsd el és push-old a változtatásokat.

### Check Broken Urls

Ez a munkafolyamat ellenőrzi, hogy a fájljaidban lévő webes URL-ek működnek-e és 200-as státuszkódot adnak vissza.

1. Az URL-ek működésének ellenőrzéséhez:

    - Ellenőrizd az URL-ek státuszát a fájlokban.

2. Hibás URL-ek javításához:

    - Nyisd meg a hibás URL-t tartalmazó fájlt.
    - Frissítsd az URL-t a helyesre.

Ha kijavítottad az URL-eket, mentsd el és push-old a változtatásokat.

> [!NOTE]
>
> Előfordulhat, hogy az URL-ellenőrzés hibát jelez, még ha a link elérhető is. Ennek több oka lehet, például:
>
> - **Hálózati korlátozások:** A GitHub Actions szerverek hálózati korlátozások miatt nem férhetnek hozzá bizonyos URL-ekhez.
> - **Időtúllépés:** Az URL-ek, amelyek túl sokáig válaszolnak, időtúllépési hibát válthatnak ki a munkafolyamatban.
> - **Ideiglenes szerverproblémák:** Időszakos szerverleállás vagy karbantartás miatt az URL ideiglenesen nem elérhető az ellenőrzés során.

**Jogi nyilatkozat**:  
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.