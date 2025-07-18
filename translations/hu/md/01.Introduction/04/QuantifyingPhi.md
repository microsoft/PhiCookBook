<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-07-16T21:49:34+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "hu"
}
-->
# **Phi család kvantálása**

A modell kvantálása azt a folyamatot jelenti, amikor egy neurális hálózati modell paramétereit (például súlyokat és aktivációs értékeket) egy nagy értéktartományból (általában folytonos értéktartományból) egy kisebb, véges értéktartományba térképezzük át. Ez a technológia csökkentheti a modell méretét és számítási összetettségét, valamint javíthatja a modell működési hatékonyságát erőforrás-korlátozott környezetekben, például mobil eszközökön vagy beágyazott rendszerekben. A modell kvantálása a paraméterek pontosságának csökkentésével éri el a tömörítést, ugyanakkor bizonyos pontosságvesztéssel is jár. Ezért a kvantálási folyamat során egyensúlyt kell találni a modell mérete, számítási összetettsége és pontossága között. Gyakori kvantálási módszerek közé tartozik a fixpontos kvantálás, a lebegőpontos kvantálás stb. A konkrét helyzet és igények alapján választható a megfelelő kvantálási stratégia.

Célunk, hogy a GenAI modelleket élő eszközökre telepítsük, és több eszközt vonjunk be GenAI forgatókönyvekbe, például mobil eszközöket, AI PC/Copilot+PC-ket és hagyományos IoT eszközöket. A kvantált modellek segítségével különböző élő eszközökre telepíthetjük a modellt az eszközök sajátosságai szerint. A hardvergyártók által biztosított modellgyorsító keretrendszerekkel és kvantált modellekkel kombinálva jobb SLM alkalmazási forgatókönyveket építhetünk ki.

A kvantálási forgatókönyvben különböző pontosságokkal dolgozunk (INT4, INT8, FP16, FP32). Az alábbiakban ismertetjük a leggyakrabban használt kvantálási pontosságokat.

### **INT4**

Az INT4 kvantálás egy radikális kvantálási módszer, amely a modell súlyait és aktivációs értékeit 4 bites egész számokká alakítja. Az INT4 kvantálás általában nagyobb pontosságvesztéssel jár a kisebb ábrázolási tartomány és alacsonyabb pontosság miatt. Ugyanakkor az INT8 kvantáláshoz képest tovább csökkentheti a modell tárolási igényét és számítási összetettségét. Fontos megjegyezni, hogy az INT4 kvantálás a gyakorlatban viszonylag ritka, mert a túl alacsony pontosság jelentős teljesítményromláshoz vezethet. Emellett nem minden hardver támogatja az INT4 műveleteket, ezért a kvantálási módszer kiválasztásakor figyelembe kell venni a hardver kompatibilitását.

### **INT8**

Az INT8 kvantálás során a modell súlyait és aktivációit lebegőpontos számokról 8 bites egész számokra alakítjuk át. Bár az INT8 egész számok által ábrázolt numerikus tartomány kisebb és kevésbé pontos, jelentősen csökkenti a tárolási és számítási igényeket. Az INT8 kvantálás során a modell súlyai és aktivációs értékei egy kvantálási folyamaton mennek keresztül, amely magában foglalja a skálázást és az eltolást, hogy a lehető legjobban megőrizzék az eredeti lebegőpontos információt. Az inferencia során ezek a kvantált értékek visszaalakításra kerülnek lebegőpontos számokká a számításhoz, majd ismét INT8 formátumba kvantálódnak a következő lépéshez. Ez a módszer a legtöbb alkalmazásban elegendő pontosságot biztosít, miközben magas számítási hatékonyságot tart fenn.

### **FP16**

Az FP16 formátum, azaz a 16 bites lebegőpontos számok (float16) a 32 bites lebegőpontos számokhoz (float32) képest a memóriahasználatot felére csökkenti, ami jelentős előnyt jelent a nagyméretű mélytanulási alkalmazásokban. Az FP16 formátum lehetővé teszi nagyobb modellek betöltését vagy több adat feldolgozását ugyanazon GPU memóriahatárok között. Mivel a modern GPU hardverek egyre inkább támogatják az FP16 műveleteket, az FP16 formátum használata javíthatja a számítási sebességet is. Ugyanakkor az FP16 formátumnak megvannak a maga hátrányai is, nevezetesen az alacsonyabb pontosság, ami bizonyos esetekben numerikus instabilitáshoz vagy pontosságvesztéshez vezethet.

### **FP32**

Az FP32 formátum magasabb pontosságot biztosít, és széles értéktartományt képes pontosan ábrázolni. Olyan helyzetekben, ahol összetett matematikai műveleteket végeznek vagy nagy pontosságú eredmények szükségesek, az FP32 formátum az előnyösebb. Ugyanakkor a magas pontosság több memóriahasználatot és hosszabb számítási időt jelent. Nagyméretű mélytanulási modellek esetén, különösen ha sok modellparaméter és hatalmas adatállomány van, az FP32 formátum GPU memóriahiányt vagy az inferencia sebességének csökkenését okozhatja.

Mobil eszközökön vagy IoT eszközökön a Phi-3.x modelleket INT4-re konvertálhatjuk, míg AI PC / Copilot PC esetén magasabb pontosságok, például INT8, FP16 vagy FP32 használhatók.

Jelenleg különböző hardvergyártók eltérő keretrendszereket kínálnak generatív modellek támogatására, mint például az Intel OpenVINO, Qualcomm QNN, Apple MLX és Nvidia CUDA, amelyeket a modell kvantálással kombinálva helyi telepítésre használhatunk.

Technológiai szempontból a kvantálás után különböző formátumtámogatások állnak rendelkezésre, például PyTorch / Tensorflow formátum, GGUF és ONNX. Készítettem egy formátum összehasonlítást és alkalmazási forgatókönyveket a GGUF és az ONNX között. Itt az ONNX kvantálási formátumot ajánlom, amely jó támogatást élvez a modellkeretrendszertől a hardverig. Ebben a fejezetben az ONNX Runtime GenAI, OpenVINO és Apple MLX használatára fókuszálunk a modell kvantálásához (ha jobb megoldásod van, PR beküldésével megoszthatod velünk).

**Ez a fejezet tartalmazza**

1. [Phi-3.5 / 4 kvantálása llama.cpp használatával](./UsingLlamacppQuantifyingPhi.md)

2. [Phi-3.5 / 4 kvantálása Generative AI kiterjesztésekkel onnxruntime-hoz](./UsingORTGenAIQuantifyingPhi.md)

3. [Phi-3.5 / 4 kvantálása Intel OpenVINO használatával](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Phi-3.5 / 4 kvantálása Apple MLX keretrendszerrel](./UsingAppleMLXQuantifyingPhi.md)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.