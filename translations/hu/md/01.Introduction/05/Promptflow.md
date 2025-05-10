<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cbe7629d254f1043193b7fe22524d55",
  "translation_date": "2025-05-09T15:19:57+00:00",
  "source_file": "md/01.Introduction/05/Promptflow.md",
  "language_code": "hu"
}
-->
# **Ismerkedés a Promptflow-val**

A [Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) egy vizuális munkafolyamat-automatizálási eszköz, amely lehetővé teszi a felhasználók számára, hogy előre elkészített sablonok és egyedi csatlakozók segítségével automatizált munkafolyamatokat hozzanak létre. Arra tervezték, hogy fejlesztők és üzleti elemzők gyorsan építhessenek automatizált folyamatokat olyan feladatokhoz, mint az adatkezelés, együttműködés és folyamatoptimalizálás. A Prompt Flow segítségével könnyedén összekapcsolhatók különböző szolgáltatások, alkalmazások és rendszerek, valamint automatizálhatók összetett üzleti folyamatok.

A Microsoft Prompt Flow célja az AI alkalmazások teljes fejlesztési ciklusának egyszerűsítése, melyeket nagy nyelvi modellek (LLM-ek) hajtanak. Legyen szó ötletelésről, prototípus-készítésről, tesztelésről, értékelésről vagy LLM-alapú alkalmazások bevezetéséről, a Prompt Flow leegyszerűsíti a folyamatot, és lehetővé teszi, hogy professzionális minőségű LLM alkalmazásokat építsünk.

## A Microsoft Prompt Flow főbb funkciói és előnyei:

**Interaktív szerkesztési élmény**

A Prompt Flow vizuálisan ábrázolja a munkafolyamat szerkezetét, így könnyű átlátni és navigálni a projekteken.
Jegyzetfüzet-szerű kódolási élményt kínál a hatékony munkafolyamat-fejlesztéshez és hibakereséshez.

**Prompt variánsok és hangolás**

Hozz létre és hasonlíts össze több prompt variánst az iteratív finomítás érdekében. Értékeld a különböző promptok teljesítményét, és válaszd ki a leghatékonyabbat.

**Beépített értékelési munkafolyamatok**

A beépített értékelő eszközökkel mérheted a promptok és munkafolyamatok minőségét és hatékonyságát.
Megértheted, mennyire jól teljesítenek az LLM-alapú alkalmazásaid.

**Átfogó erőforrások**

A Prompt Flow tartalmaz egy könyvtárat beépített eszközökkel, mintákkal és sablonokkal. Ezek a források fejlesztési kiindulópontként szolgálnak, ösztönzik a kreativitást és felgyorsítják a munkát.

**Együttműködés és vállalati felkészültség**

Támogatja a csapatmunkát, lehetővé téve, hogy többen dolgozzanak együtt promptfejlesztési projekteken.
Fenntartja a verziókövetést és hatékonyan segíti a tudásmegosztást. Egyszerűsíti a teljes promptfejlesztési folyamatot a fejlesztéstől az értékelésen át a bevezetésig és monitorozásig.

## Értékelés a Prompt Flow-ban

A Microsoft Prompt Flow-ban az értékelés kulcsszerepet játszik abban, hogy felmérjük AI modelljeink teljesítményét. Nézzük meg, hogyan testreszabhatod az értékelési munkafolyamatokat és mérőszámokat a Prompt Flow-ban:

![PFVizualise](../../../../../translated_images/pfvisualize.93c453890f4088830217fa7308b1a589058ed499bbfff160c85676066b5cbf2d.hu.png)

**Értékelés megértése a Prompt Flow-ban**

A Prompt Flow-ban egy munkafolyamat egy olyan csomópont-sorozatot jelent, amely bemeneteket dolgoz fel és kimeneteket generál. Az értékelési munkafolyamatok speciális típusú munkafolyamatok, melyek egy futás teljesítményét mérik adott kritériumok és célok alapján.

**Az értékelési munkafolyamatok fő jellemzői**

Általában a tesztelendő munkafolyamat után futnak, annak kimeneteit használva.
Pontszámokat vagy mérőszámokat számítanak ki a tesztelt munkafolyamat teljesítményének mérésére. Ezek a mérőszámok lehetnek pontosság, relevanciaértékek vagy más releváns mutatók.

### Értékelési munkafolyamatok testreszabása

**Bemenetek definiálása**

Az értékelési munkafolyamatoknak a tesztelt futás kimeneteit kell fogadniuk. A bemeneteket hasonlóan definiáld, mint a szokásos munkafolyamatoknál.
Például, ha egy QnA munkafolyamatot értékelsz, nevezz el egy bemenetet "answer"-nek. Ha egy osztályozó munkafolyamatot értékelsz, nevezz el egy bemenetet "category"-nek. Szükség lehet a valós címkéket (ground truth) is fogadó bemenetekre.

**Kimenetek és mérőszámok**

Az értékelési munkafolyamatok olyan eredményeket adnak, amelyek a tesztelt munkafolyamat teljesítményét mérik. A mérőszámok Python vagy LLM segítségével számolhatók ki. A log_metric() függvénnyel naplózhatod a releváns mérőszámokat.

**Testreszabott értékelési munkafolyamatok használata**

Fejleszd ki saját, egyedi értékelési munkafolyamatodat, amely az adott feladatokhoz és célokhoz igazodik.
Testreszabhatod a mérőszámokat az értékelési céljaid szerint.
Ezt a testreszabott értékelési munkafolyamatot alkalmazhatod nagy volumenű tesztelésekhez is.

## Beépített értékelési módszerek

A Prompt Flow beépített értékelési módszereket is kínál.
Batch futtatásokat adhatsz be, és ezeket a módszereket használhatod a munkafolyamat teljesítményének értékelésére nagy adathalmazokon.
Megtekintheted az értékelési eredményeket, összehasonlíthatod a mérőszámokat, és szükség szerint iterálhatsz.
Ne feledd, az értékelés elengedhetetlen annak biztosításához, hogy AI modelljeid megfeleljenek a kívánt kritériumoknak és céloknak. Részletes útmutatásért keresd fel a hivatalos dokumentációt a Microsoft Prompt Flow értékelési munkafolyamatainak fejlesztéséhez és használatához.

Összefoglalva, a Microsoft Prompt Flow lehetővé teszi a fejlesztők számára, hogy magas színvonalú LLM alkalmazásokat hozzanak létre azáltal, hogy leegyszerűsíti a promptfejlesztést és robusztus fejlesztési környezetet biztosít. Ha LLM-ekkel dolgozol, a Prompt Flow értékes eszköz lehet számodra. Részletes útmutatókért az értékelési munkafolyamatok fejlesztéséhez és használatához látogasd meg a [Prompt Flow Evaluation Documents](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo) oldalt.

**Jogi nyilatkozat**:  
Ezt a dokumentumot az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy helytelen értelmezésekért.