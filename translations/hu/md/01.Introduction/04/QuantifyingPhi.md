<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-05-09T13:35:18+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "hu"
}
-->
# **Phi család kvantálása**

A modell kvantálás a folyamat, amely során egy neurális hálózat modell paramétereit (például súlyokat és aktivációs értékeket) egy nagy értéktartományból (általában folytonos értéktartományból) egy kisebb, véges értéktartományba térképezik át. Ez a technológia csökkentheti a modell méretét és számítási összetettségét, valamint javíthatja a modell működési hatékonyságát erőforrás-korlátozott környezetekben, például mobil eszközökön vagy beágyazott rendszerekben. A modell kvantálása a paraméterek pontosságának csökkentésével ér el tömörítést, ugyanakkor bizonyos pontosságvesztéssel jár. Ezért a kvantálás során egyensúlyt kell találni a modell mérete, számítási összetettsége és pontossága között. Gyakori kvantálási módszerek közé tartozik a fixpontos kvantálás, a lebegőpontos kvantálás stb. A konkrét helyzet és igények alapján választható a megfelelő kvantálási stratégia.

Célunk, hogy a GenAI modelleket élő eszközökre telepítsük, és így több eszköz kapcsolódhasson a GenAI szcenáriókhoz, mint például mobil eszközök, AI PC/Copilot+PC, valamint hagyományos IoT eszközök. A kvantált modelleken keresztül különböző élő eszközökre telepíthetjük azokat, az adott eszközök alapján. A hardvergyártók által biztosított modellgyorsító keretrendszerekkel és kvantált modellekkel kombinálva jobb SLM alkalmazási forgatókönyveket építhetünk ki.

A kvantálási szcenáriókban különböző pontosságokat használunk (INT4, INT8, FP16, FP32). Az alábbiakban ismertetjük a gyakran használt kvantálási pontosságokat.

### **INT4**

Az INT4 kvantálás egy radikális kvantálási módszer, amely a modell súlyait és aktivációs értékeit 4 bites egész számokra kvantálja. Az INT4 kvantálás általában nagyobb pontosságvesztéssel jár, mivel a reprezentációs tartomány kisebb és a pontosság alacsonyabb. Ugyanakkor az INT8-hoz képest az INT4 kvantálás tovább csökkentheti a modell tárolási igényét és számítási összetettségét. Fontos megjegyezni, hogy az INT4 kvantálás viszonylag ritka a gyakorlatban, mivel a túl alacsony pontosság jelentős teljesítményromláshoz vezethet. Emellett nem minden hardver támogatja az INT4 műveleteket, ezért a hardver kompatibilitását is figyelembe kell venni a kvantálási módszer kiválasztásakor.

### **INT8**

Az INT8 kvantálás a modell súlyainak és aktivációinak lebegőpontos értékekből 8 bites egész számokká alakítását jelenti. Bár az INT8 egész számok által képviselt numerikus tartomány kisebb és kevésbé pontos, jelentősen csökkentheti a tárolási és számítási igényeket. Az INT8 kvantálás során a modell súlyai és aktivációs értékei egy kvantálási folyamaton mennek keresztül, amely magában foglalja a skálázást és eltolást, hogy a lehető legjobban megőrizzék az eredeti lebegőpontos információt. Az inferencia során ezek a kvantált értékek visszaalakításra kerülnek lebegőpontos számokká a számításhoz, majd ismét kvantálásra az INT8 formátumba a következő lépéshez. Ez a módszer a legtöbb alkalmazásban elegendő pontosságot biztosít, miközben magas számítási hatékonyságot tart fenn.

### **FP16**

Az FP16 formátum, azaz a 16 bites lebegőpontos számok (float16) a memóriaterhelést a 32 bites lebegőpontos számokhoz (float32) képest a felére csökkentik, ami jelentős előnyt jelent nagy léptékű mélytanulási alkalmazásokban. Az FP16 formátum lehetővé teszi nagyobb modellek betöltését vagy több adat feldolgozását ugyanazon GPU memóriahatárok között. Mivel a modern GPU hardverek egyre inkább támogatják az FP16 műveleteket, az FP16 formátum használata számítási sebesség javulást is hozhat. Ugyanakkor az FP16 formátumnak megvannak a maga hátrányai is, nevezetesen az alacsonyabb pontosság, ami bizonyos esetekben numerikus instabilitáshoz vagy pontosságvesztéshez vezethet.

### **FP32**

Az FP32 formátum nagyobb pontosságot biztosít, és képes széles értéktartományt pontosan ábrázolni. Olyan helyzetekben, ahol összetett matematikai műveleteket végeznek vagy nagy pontosságú eredmények szükségesek, az FP32 formátum az előnyösebb. Ugyanakkor a nagy pontosság több memóriahasználatot és hosszabb számítási időt jelent. Nagyléptékű mélytanulási modellek esetén, különösen ha sok modellparaméter és hatalmas adatmennyiség van, az FP32 formátum GPU memóriahiányt vagy lassabb inferencia sebességet eredményezhet.

Mobil eszközökön vagy IoT eszközökön a Phi-3.x modelleket átalakíthatjuk INT4-re, míg AI PC / Copilot PC magasabb pontosságot, például INT8, FP16 vagy FP32 formátumot használhat.

Jelenleg különböző hardvergyártók eltérő keretrendszereket kínálnak generatív modellek támogatására, például az Intel OpenVINO-t, a Qualcomm QNN-t, az Apple MLX-et és az Nvidia CUDA-t, amelyeket modell kvantálással kombinálva helyi telepítést valósíthatunk meg.

Technológiai szempontból a kvantálás után több formátumot támogatunk, például PyTorch / Tensorflow formátumot, GGUF-et és ONNX-et. Elkészítettem egy összehasonlítást és alkalmazási forgatókönyveket a GGUF és az ONNX között. Itt az ONNX kvantálási formátumot ajánlom, amely jó támogatást kap a modell keretrendszerektől a hardverig. Ebben a fejezetben az ONNX Runtime GenAI, OpenVINO és Apple MLX használatával fogunk modell kvantálást végezni (ha jobb módszered van, nyugodtan küldd el PR formájában).

**Ez a fejezet tartalmazza**

1. [Phi-3.5 / 4 kvantálása llama.cpp segítségével](./UsingLlamacppQuantifyingPhi.md)

2. [Phi-3.5 / 4 kvantálása Generative AI kiterjesztésekkel onnxruntime-hoz](./UsingORTGenAIQuantifyingPhi.md)

3. [Phi-3.5 / 4 kvantálása Intel OpenVINO-val](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Phi-3.5 / 4 kvantálása Apple MLX keretrendszerrel](./UsingAppleMLXQuantifyingPhi.md)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár igyekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt szakmai, emberi fordítást igénybe venni. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy félreértelmezésekért.