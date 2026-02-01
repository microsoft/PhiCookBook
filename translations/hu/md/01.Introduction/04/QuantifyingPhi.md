# **Phi család kvantálása**

A modell kvantálása azt a folyamatot jelenti, amikor egy neurális hálózati modellben található paramétereket (például súlyokat és aktivációs értékeket) egy nagy értéktartományból (általában folytonos értéktartományból) egy kisebb véges értéktartományba térképezünk át. Ez a technológia csökkentheti a modell méretét és számítási összetettségét, valamint javíthatja a modell működési hatékonyságát erőforrás-korlátozott környezetekben, mint például mobil eszközökön vagy beágyazott rendszerekben. A modell kvantálás a paraméterek pontosságának csökkentésével éri el a tömörítést, de ez pontosságvesztéssel is jár. Ezért a kvantálási folyamat során egyensúlyt kell találni a modell mérete, számítási komplexitása és pontossága között. A gyakori kvantálási módszerek közé tartozik a fixpontos kvantálás, lebegőpontos kvantálás stb. A konkrét helyzet és igények szerint lehet kiválasztani a megfelelő kvantálási stratégiát.

Arra törekszünk, hogy a GenAI modellt él- eszközökre telepítsük, és több eszközt juttassunk el a GenAI felhasználási környezetekhez, mint például mobil eszközök, AI PC/Copilot+PC és a hagyományos IoT eszközök. A kvantált modelleken keresztül különböző él-eszközökre telepíthetjük őket az eszközök alapján. A hardvergyártók által biztosított modellgyorsító keretrendszerekkel és kvantált modellekkel együtt jobb SLM alkalmazási forgatókönyveket építhetünk.

A kvantálási forgatókönyvben különböző pontosságokat használunk (INT4, INT8, FP16, FP32). Az alábbiakban a gyakran használt kvantálási pontosságokat ismertetjük

### **INT4**

Az INT4 kvantálás egy radikális kvantálási módszer, amely a modell súlyait és aktivációs értékeit 4 bites egész számokká kvantálja. Az INT4 kvantálás általában nagyobb pontosságvesztéssel jár a kisebb ábrázolási tartomány és alacsonyabb precizitás miatt. Ugyanakkor az INT8 kvantáláshoz képest az INT4 további csökkentést tesz lehetővé a modell tárolási igényeiben és számítási komplexitásában. Fontos megjegyezni, hogy az INT4 kvantálás a gyakorlatban viszonylag ritka, mert az túl alacsony pontosság jelentős teljesítményromlást okozhat a modellben. Továbbá nem minden hardver támogatja az INT4 műveleteket, így a hardver-kompatibilitást is figyelembe kell venni a kvantálási módszer kiválasztásakor.

### **INT8**

Az INT8 kvantálás a modell súlyainak és aktivációinak lebegőpontos számokról 8 bites egész számokra való átalakítása. Bár az INT8 egész számok ábrázolási tartománya kisebb és kevésbé pontos, jelentősen csökkentheti a tárolási és számítási igényeket. Az INT8 kvantálás során a modell súlyai és aktivációs értékei egy kvantálási folyamaton mennek keresztül, amely skálázást és eltolást tartalmaz a lebegőpontos eredeti információ lehető legteljesebb megőrzése érdekében. A kiértékelés során ezek a kvantált értékek visszaalakításra kerülnek lebegőpontos számokká a számításokhoz, majd újra kvantálásra kerülnek INT8 formátumba a következő lépéshez. Ez a módszer a legtöbb alkalmazásban elegendő pontosságot biztosít, miközben magas számítási hatékonyságot tart fenn.

### **FP16**

Az FP16 formátum, azaz 16 bites lebegőpontos számok (float16) a 32 bites lebegőpontos (float32) számokhoz képest a memóriahasználatot felére csökkenti, ami jelentős előnyt jelent nagyméretű mélytanulási alkalmazásokban. Az FP16 formátum lehetővé teszi nagyobb modellek betöltését vagy több adat feldolgozását ugyanazon GPU memória korlátok között. A modern GPU hardverek egyre inkább támogatják az FP16 műveleteket, így az FP16 formátum használata akár a számítási sebesség javulásához is vezethet. Ugyanakkor az FP16 formátum inherens hátránya az alacsonyabb precizitás, ami bizonyos esetekben számtani instabilitást vagy pontosságvesztést okozhat.

### **FP32**

Az FP32 formátum nagyobb pontosságot biztosít, és széles értéktartományt képes pontosan ábrázolni. Olyan esetekben, amikor összetett matematikai műveleteket kell végrehajtani vagy nagy pontosságú eredmények szükségesek, az FP32 formátum előnyös. Ugyanakkor a nagy pontosság több memóriafelhasználást és hosszabb számítási időt jelent. Nagyméretű mélytanulási modellek esetében, különösen sok modellparaméter és nagy mennyiségű adat esetén az FP32 formátum okozhat GPU memória elégtelenséget vagy a kiértékelési sebesség csökkenését.

Mobil eszközökön vagy IoT eszközökön a Phi-3.x modelleket átalakíthatjuk INT4-re, míg AI PC / Copilot PC esetén magasabb pontosságokat lehet alkalmazni, például INT8, FP16, FP32.

Jelenleg különböző hardvergyártóknak eltérő keretrendszerei vannak a generatív modellek támogatására, például az Intel OpenVINO, Qualcomm QNN, Apple MLX és Nvidia CUDA, melyeket a modell kvantálással kombinálva lehet helyben telepíteni.

Technológiai oldalról a kvantálás után különböző formátumtámogatásokkal rendelkezünk, mint például PyTorch / TensorFlow formátum, GGUF és ONNX. Elvégeztem egy formátum összehasonlítást és alkalmazási forgatókönyveket a GGUF és ONNX között. Itt az ONNX kvantálási formátumot ajánlom, amely jó támogatottsággal rendelkezik a modell keretrendszertől a hardverig. Ebben a fejezetben az ONNX Runtime for GenAI, OpenVINO és Apple MLX használatára fókuszálunk a modell kvantálás elvégzéséhez (ha jobb megoldásod van, azt PR beküldésével megoszthatod velünk).

**Ez a fejezet tartalmazza**

1. [Phi-3.5 / 4 kvantálása llama.cpp használatával](./UsingLlamacppQuantifyingPhi.md)

2. [Phi-3.5 / 4 kvantálása Generatív AI kiterjesztésekkel onnxruntime-hoz](./UsingORTGenAIQuantifyingPhi.md)

3. [Phi-3.5 / 4 kvantálása Intel OpenVINO használatával](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Phi-3.5 / 4 kvantálása Apple MLX keretrendszerrel](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár igyekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum a saját nyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális, emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből eredő félreértésekért vagy hibás értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->