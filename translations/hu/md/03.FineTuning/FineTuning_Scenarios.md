## Finomhangolási Forgatókönyvek

![FineTuning with MS Services](../../../../translated_images/hu/FinetuningwithMS.3d0cec8ae693e094.webp)

Ez a rész áttekintést nyújt a Microsoft Foundry és az Azure környezetek finomhangolási forgatókönyveiről, beleértve a telepítési modelleket, az infrastruktúra rétegeket és a gyakran használt optimalizációs technikákat.

**Platform**  
Ide tartoznak a felügyelt szolgáltatások, mint a Microsoft Foundry (korábban Microsoft Foundry) és az Azure Machine Learning, amelyek modellkezelést, összefűzést, kísérletkövetést és telepítési munkafolyamatokat biztosítanak.

**Infrastruktúra**  
A finomhangoláshoz skálázható számítási erőforrásokra van szükség. Az Azure környezetekben ez tipikusan GPU-alapú virtuális gépeket és CPU erőforrásokat foglal magában könnyű munkaterhelésekhez, valamint skálázható tárolót az adatállományok és ellenőrzőpontok számára.

**Eszközök és Keretrendszerek**  
A finomhangolási munkafolyamatok gyakran támaszkodnak olyan keretrendszerekre és optimalizációs könyvtárakra, mint a Hugging Face Transformers, DeepSpeed és PEFT (Parameter-Efficient Fine-Tuning).

A finomhangolási folyamat a Microsoft technológiáival átfogja a platform szolgáltatásokat, a számítási infrastruktúrát és a tanulási keretrendszereket. E komponensek együttműködésének megértésével a fejlesztők hatékonyan tudják alapmodelljeiket specifikus feladatokra és gyártási forgatókönyvekre szabni.

## Modell mint Szolgáltatás

Finomhangold a modellt hostolt finomhangolással, számítási erőforrás létrehozása és kezelése nélkül.

![MaaS Fine Tuning](../../../../translated_images/hu/MaaSfinetune.3eee4630607aff0d.webp)

A szerver nélküli finomhangolás most elérhető a Phi-3, Phi-3.5 és Phi-4 modellcsaládokhoz, lehetővé téve a fejlesztők számára, hogy gyorsan és egyszerűen testre szabják a modelleket felhő és élő környezetekhez számítási erőforrás biztosítása nélkül.

## Modell mint Platform

A felhasználók a saját számítási erőforrásaikat kezelik, hogy finomhangolják modelljeiket.

![Maap Fine Tuning](../../../../translated_images/hu/MaaPFinetune.fd3829c1122f5d1c.webp)

[Finomhangolási Minta](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Finomhangolási Technikák Összehasonlítása

|Forgatókönyv|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Előre tanított LLM-ek adaptálása specifikus feladatokra vagy domainekre|Igen|Igen|Igen|Igen|Igen|Igen|
|Finomhangolás NLP feladatokra, mint szöveg osztályozás, névfelismerés és gépi fordítás|Igen|Igen|Igen|Igen|Igen|Igen|
|Finomhangolás kérdés-válasz feladatokra|Igen|Igen|Igen|Igen|Igen|Igen|
|Finomhangolás emberihez hasonló válaszok generálására chatbotokban|Igen|Igen|Igen|Igen|Igen|Igen|
|Finomhangolás zene, művészet vagy egyéb kreatív formák generálásához|Igen|Igen|Igen|Igen|Igen|Igen|
|Számítási és pénzügyi költségek csökkentése|Igen|Igen|Igen|Igen|Igen|Igen|
|Memóriahasználat csökkentése|Igen|Igen|Igen|Igen|Igen|Igen|
|Kevesebb paraméter használata a hatékony finomhangoláshoz|Igen|Igen|Igen|Nem|Nem|Igen|
|Adatpárhuzamosítás memóriahatékony formája, amely hozzáférést biztosít az összes rendelkezésre álló GPU eszköz együttes memóriájához|Nem|Nem|Nem|Igen|Igen|Nem|

> [!NOTE]
> A LoRA, QLoRA, PEFT és DoRA paraméter-hatékony finomhangolási módszerek, míg a DeepSpeed és ZeRO az elosztott tanulásra és memóriaoptimalizációra fókuszál.

## Finomhangolási Teljesítmény Példák

![Finetuning Performance](../../../../translated_images/hu/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást ajánlunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy helytelen értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->