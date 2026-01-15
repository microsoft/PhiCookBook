<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cbe7629d254f1043193b7fe22524d55",
  "translation_date": "2025-07-16T22:43:52+00:00",
  "source_file": "md/01.Introduction/05/Promptflow.md",
  "language_code": "hu"
}
-->
# **Ismerkedés a Promptflow-val**

[Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) egy vizuális munkafolyamat-automatizálási eszköz, amely lehetővé teszi a felhasználók számára, hogy előre elkészített sablonok és egyedi csatlakozók segítségével automatizált munkafolyamatokat hozzanak létre. Arra tervezték, hogy fejlesztők és üzleti elemzők gyorsan építhessenek automatizált folyamatokat olyan feladatokhoz, mint az adatkezelés, együttműködés és folyamatoptimalizálás. A Prompt Flow segítségével a felhasználók könnyedén összekapcsolhatnak különböző szolgáltatásokat, alkalmazásokat és rendszereket, és automatizálhatják az összetett üzleti folyamatokat.

A Microsoft Prompt Flow célja, hogy egyszerűsítse a nagynyelvű modelleken (LLM-ek) alapuló AI-alkalmazások teljes fejlesztési ciklusát. Legyen szó ötletelésről, prototípus-készítésről, tesztelésről, értékelésről vagy LLM-alapú alkalmazások élesítéséről, a Prompt Flow leegyszerűsíti a folyamatot, és lehetővé teszi, hogy professzionális minőségű LLM alkalmazásokat építs.

## A Microsoft Prompt Flow főbb jellemzői és előnyei:

**Interaktív szerkesztési élmény**

A Prompt Flow vizuálisan ábrázolja a munkafolyamat szerkezetét, így könnyen átlátható és kezelhető a projekt.
Jegyzetfüzet-szerű kódolási élményt kínál a hatékony munkafolyamat-fejlesztéshez és hibakereséshez.

**Prompt variánsok és finomhangolás**

Hozz létre és hasonlíts össze több prompt variánst az iteratív finomítás érdekében. Értékeld a különböző promptok teljesítményét, és válaszd ki a leghatékonyabbat.

**Beépített értékelési munkafolyamatok**

Értékeld a promptok és munkafolyamatok minőségét és hatékonyságát a beépített értékelő eszközökkel.
Ismerd meg, mennyire jól teljesítenek az LLM-alapú alkalmazásaid.

**Átfogó erőforrások**

A Prompt Flow tartalmaz egy könyvtárat beépített eszközökkel, példákkal és sablonokkal. Ezek az erőforrások kiindulópontként szolgálnak a fejlesztéshez, inspirációt nyújtanak, és felgyorsítják a folyamatot.

**Együttműködés és vállalati felkészültség**

Támogatja a csapatmunkát, lehetővé téve, hogy több felhasználó dolgozzon együtt prompt fejlesztési projekteken.
Fenntartja a verziókezelést és hatékonyan osztja meg a tudást. Egyszerűsíti a teljes prompt fejlesztési folyamatot a fejlesztéstől és értékeléstől az élesítésig és monitorozásig.

## Értékelés a Prompt Flow-ban

A Microsoft Prompt Flow-ban az értékelés kulcsfontosságú szerepet játszik az AI modellek teljesítményének mérésében. Nézzük meg, hogyan testreszabhatod az értékelési munkafolyamatokat és metrikákat a Prompt Flow-ban:

![PFVizualise](../../../../../translated_images/hu/pfvisualize.c1d9ca75baa2a222.png)

**Az értékelés megértése a Prompt Flow-ban**

A Prompt Flow-ban egy munkafolyamat egy olyan csomópontok sorozatát jelenti, amely bemenetet dolgoz fel és kimenetet generál. Az értékelési munkafolyamatok speciális típusú folyamatok, amelyeket arra terveztek, hogy egy futtatás teljesítményét adott kritériumok és célok alapján mérjék.

**Az értékelési munkafolyamatok fő jellemzői**

Általában a tesztelendő munkafolyamat után futnak, annak kimeneteit használva. Pontszámokat vagy metrikákat számolnak a tesztelt munkafolyamat teljesítményének mérésére. A metrikák lehetnek pontosság, relevancia értékek vagy bármilyen más releváns mérőszám.

### Értékelési munkafolyamatok testreszabása

**Bemenetek definiálása**

Az értékelési munkafolyamatoknak meg kell kapniuk a tesztelendő futtatás kimeneteit. A bemeneteket hasonlóan kell definiálni, mint a szokásos munkafolyamatoknál.
Például, ha egy QnA munkafolyamatot értékelsz, nevezd el a bemenetet "answer"-nek. Ha egy osztályozó munkafolyamatot értékelsz, nevezd el "category"-nek. Szükség lehet a valós címkék (ground truth) bemeneteire is.

**Kimenetek és metrikák**

Az értékelési munkafolyamatok olyan eredményeket állítanak elő, amelyek mérik a tesztelt munkafolyamat teljesítményét. A metrikákat Python vagy LLM segítségével lehet kiszámítani. Használd a log_metric() függvényt a releváns metrikák naplózásához.

**Testreszabott értékelési munkafolyamatok használata**

Fejlessz ki saját értékelési munkafolyamatot, amely az adott feladataidhoz és céljaidhoz igazodik. Testreszabhatod a metrikákat az értékelési céljaid szerint.
Alkalmazd ezt a testreszabott értékelési munkafolyamatot nagyobb tesztelési futtatásokra.

## Beépített értékelési módszerek

A Prompt Flow beépített értékelési módszereket is kínál.
Batch futtatásokat adhatsz be, és ezeket a módszereket használhatod annak értékelésére, hogy a munkafolyamatod hogyan teljesít nagy adathalmazokon.
Tekintsd meg az értékelési eredményeket, hasonlítsd össze a metrikákat, és szükség szerint iterálj.
Ne feledd, az értékelés elengedhetetlen annak biztosításához, hogy az AI modelleid megfeleljenek a kívánt kritériumoknak és céloknak. Részletes útmutatókért tekintsd meg a hivatalos dokumentációt a Microsoft Prompt Flow értékelési munkafolyamatainak fejlesztéséről és használatáról.

Összefoglalva, a Microsoft Prompt Flow lehetővé teszi a fejlesztők számára, hogy magas minőségű LLM alkalmazásokat hozzanak létre azáltal, hogy leegyszerűsíti a prompt fejlesztést és egy robusztus fejlesztői környezetet biztosít. Ha LLM-ekkel dolgozol, a Prompt Flow értékes eszköz lehet számodra. Tekintsd meg a [Prompt Flow Értékelési Dokumentumokat](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo) a Microsoft Prompt Flow értékelési munkafolyamatainak fejlesztéséről és használatáról szóló részletes útmutatókért.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.