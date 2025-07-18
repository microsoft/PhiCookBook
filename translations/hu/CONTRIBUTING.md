<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-07-16T14:44:57+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "hu"
}
-->
# Hozzájárulás

Ez a projekt szívesen fogad hozzájárulásokat és javaslatokat. A legtöbb hozzájáruláshoz el kell fogadnod egy Contributor License Agreement (CLA) nevű licencszerződést, amelyben kijelented, hogy jogodban áll, és ténylegesen megadod nekünk a hozzájárulásod használatának jogát. Részletekért látogass el ide: [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Amikor pull request-et nyújtasz be, egy CLA bot automatikusan megállapítja, hogy szükséges-e CLA-t benyújtanod, és ennek megfelelően jelöli meg a PR-t (például státusz ellenőrzés, komment). Egyszerűen kövesd a bot utasításait. Ezt csak egyszer kell megtenned az összes CLA-t használó repóban.

## Magatartási kódex

Ez a projekt elfogadta a [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) magatartási kódexet.  
További információkért olvasd el a [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) oldalt, vagy írj az [opencode@microsoft.com](mailto:opencode@microsoft.com) címre, ha kérdésed vagy észrevételed van.

## Figyelmeztetések a hibajegyek létrehozásához

Kérjük, ne nyiss GitHub hibajegyeket általános támogatási kérdések miatt, mivel a GitHub lista a funkciókérések és hibajelentések számára van fenntartva. Így könnyebben nyomon követhetjük a tényleges problémákat vagy hibákat a kódban, és a általános beszélgetést elkülöníthetjük a tényleges kódtól.

## Hogyan járulhatsz hozzá

### Pull Request irányelvek

Amikor pull request-et (PR) nyújtasz be a Phi-3 CookBook repóba, kérjük, kövesd az alábbi irányelveket:

- **Forkold a repót**: Mindig forkold a repót a saját fiókodba, mielőtt módosításokat végzel.

- **Külön pull requestek (PR)**:
  - Minden változtatást külön PR-ben nyújts be. Például hibajavításokat és dokumentáció frissítéseket külön PR-ben.
  - Elgépelés javításokat és kisebb dokumentációs frissítéseket egy PR-ben is össze lehet vonni, ha indokolt.

- **Merge konfliktusok kezelése**: Ha a pull request-ed merge konfliktusokat jelez, frissítsd a helyi `main` ágadat, hogy tükrözze a fő repót, mielőtt módosítanál.

- **Fordítások benyújtása**: Fordítási PR benyújtásakor győződj meg róla, hogy a fordítási mappa tartalmazza az eredeti mappa összes fájljának fordítását.

### Írási irányelvek

Az összes dokumentum egységessége érdekében kérjük, használd az alábbi irányelveket:

- **URL formázás**: Minden URL-t zárj szögletes zárójelbe, majd kerek zárójelbe, szóközök nélkül. Például: `[példa](https://www.microsoft.com)`.

- **Relatív linkek**: Használd a `./`-t a jelenlegi könyvtárban lévő fájlokra vagy mappákra mutató relatív linkekhez, és a `../`-t a szülő könyvtárban lévőkhöz. Például: `[példa](../../path/to/file)` vagy `[példa](../../../path/to/file)`.

- **Nem ország-specifikus lokalizációk**: Ügyelj arra, hogy a linkjeid ne tartalmazzanak ország-specifikus lokalizációkat. Például kerüld a `/en-us/` vagy `/en/` használatát.

- **Képtárolás**: Minden képet a `./imgs` mappában tárolj.

- **Leíró képfájlnevek**: A képek neve legyen leíró jellegű, angol karakterekből, számokból és kötőjelekből álljon. Például: `example-image.jpg`.

## GitHub munkafolyamatok

Amikor pull request-et nyújtasz be, az alábbi munkafolyamatok futnak le a változtatások ellenőrzésére. Kövesd az alábbi utasításokat, hogy a pull request-ed átmenjen a munkafolyamat ellenőrzéseken:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Ez a munkafolyamat ellenőrzi, hogy az összes relatív útvonal helyes-e a fájljaidban.

1. Annak érdekében, hogy a linkjeid megfelelően működjenek, végezd el a következő lépéseket VS Code-ban:
    - Vidd az egeret bármelyik link fölé a fájljaidban.
    - Nyomd meg a **Ctrl + Klikk** kombinációt a link megnyitásához.
    - Ha a link helyileg nem működik, az elindítja a munkafolyamatot, és a GitHubon sem fog működni.

1. A probléma javításához használd a VS Code által javasolt útvonalakat:
    - Írd be a `./` vagy `../` karaktereket.
    - A VS Code felajánlja a választható lehetőségeket az általad beírt alapján.
    - Kövesd az útvonalat úgy, hogy rákattintasz a kívánt fájlra vagy mappára, hogy biztosan helyes legyen az útvonal.

Miután hozzáadtad a helyes relatív útvonalat, mentsd el és push-old a változtatásokat.

### Check URLs Don't Have Locale

Ez a munkafolyamat ellenőrzi, hogy a webes URL-ek nem tartalmaznak ország-specifikus lokalizációt. Mivel ez a repó globálisan elérhető, fontos, hogy az URL-ek ne tartalmazzanak országod lokalizációját.

1. Az URL-ek ellenőrzéséhez végezd el a következőket:

    - Nézd meg, hogy az URL-ekben nincs-e olyan szöveg, mint `/en-us/`, `/en/` vagy bármilyen más nyelvi lokalizáció.
    - Ha ezek nem szerepelnek az URL-ekben, akkor átmentél az ellenőrzésen.

1. A probléma javításához végezd el a következőket:
    - Nyisd meg a munkafolyamat által kiemelt fájlútvonalat.
    - Távolítsd el az ország lokalizációját az URL-ekből.

Miután eltávolítottad az ország lokalizációját, mentsd el és push-old a változtatásokat.

### Check Broken Urls

Ez a munkafolyamat ellenőrzi, hogy a fájljaidban szereplő webes URL-ek működnek-e és 200-as státuszkódot adnak-e vissza.

1. Az URL-ek helyes működésének ellenőrzéséhez végezd el a következőket:
    - Ellenőrizd az URL-ek státuszát a fájljaidban.

2. A hibás URL-ek javításához végezd el a következőket:
    - Nyisd meg azt a fájlt, amely a hibás URL-t tartalmazza.
    - Frissítsd az URL-t a helyesre.

Miután javítottad az URL-eket, mentsd el és push-old a változtatásokat.

> [!NOTE]
>
> Előfordulhat, hogy az URL ellenőrzés hibát jelez, még akkor is, ha a link elérhető. Ennek több oka lehet, például:
>
> - **Hálózati korlátozások:** A GitHub actions szerverek hálózati korlátozásokkal rendelkezhetnek, amelyek megakadályozzák bizonyos URL-ek elérését.
> - **Időtúllépés:** Azok az URL-ek, amelyek túl sokáig válaszolnak, időtúllépési hibát válthatnak ki a munkafolyamatban.
> - **Átmeneti szerverproblémák:** Időszakos szerverleállások vagy karbantartások miatt az URL ideiglenesen nem elérhető a validálás során.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.