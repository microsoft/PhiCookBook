# **Phi šeimos kiekinimas**

Modelio kiekinimas reiškia procesą, kai neuroninio tinklo modelio parametrai (pvz., svoriai ir aktyvacijos reikšmės) perskaičiuojami iš didelės reikšmių srities (dažniausiai tęstinės reikšmių srities) į mažesnę galutinę reikšmių sritį. Ši technologija gali sumažinti modelio dydį ir skaičiavimo sudėtingumą bei pagerinti modelio veikimo efektyvumą išteklių ribotose aplinkose, tokiose kaip mobilieji įrenginiai arba įterptinės sistemos. Modelio kiekinimas pasiekia suspaudimą sumažindamas parametrų tikslumą, tačiau taip pat įveda tam tikrą tikslumo nuostolį. Todėl kiekinimo procese būtina subalansuoti modelio dydį, skaičiavimo sudėtingumą ir tikslumą. Įprasti kiekinimo metodai apima fiksuoto kablelio kiekinimą, plaukiojančio kablelio kiekinimą ir kt. Galite pasirinkti tinkamą kiekinimo strategiją pagal konkretų scenarijų ir poreikius.

Trokštame diegti GenAI modelį į krašto įrenginius ir leisti daugiau įrenginių patekti į GenAI scenarijus, kaip mobilieji įrenginiai, AI PC/Copilot+PC, tradiciniai IoT įrenginiai. Per kiekinimo modelį galime jį diegti įvairiuose krašto įrenginiuose, remdamiesi skirtingais įrenginiais. Derindami su modelio pagreitinimo sistema ir kiekinimo modeliu, kurį teikia aparatūros gamintojai, galime kurti geresnius SLM programų scenarijus.

Kiekinimo scenarijuje turime skirtingą tikslumą (INT4, INT8, FP16, FP32). Toliau pateikiamas dažniausiai naudojamų kiekinimo tikslumų paaiškinimas.

### **INT4**

INT4 kiekinimas yra radikalus kiekinimo metodas, kuriuo modelio svoriai ir aktyvacijos reikšmės kiekinamos į 4 bitų sveikuosius skaičius. Dėl mažesnės atstovavimo srities ir mažesnio tikslumo INT4 kiekinimas paprastai sukelia didesnį tikslumo praradimą. Tačiau, palyginus su INT8 kiekinimu, INT4 kiekinimas gali dar labiau sumažinti modelio saugojimo reikalavimus ir skaičiavimo sudėtingumą. Reikėtų pažymėti, kad INT4 kiekinimas praktikoje yra gana retas, nes per mažas tikslumas gali sukelti reikšmingą modelio našumo sumažėjimą. Be to, ne visa aparatūra palaiko INT4 operacijas, todėl renkantis kiekinimo metodą reikia atsižvelgti į aparatinę suderinamumą.

### **INT8**

INT8 kiekinimas yra procesas, kai modelio svoriai ir aktyvacijos skaičiuojami iš plaukiojančio kablelio skaičių į 8 bitų sveikuosius skaičius. Nors INT8 sveikųjų skaičių atstovaujama skaitinė reikšmių sritis yra mažesnė ir mažiau tiksli, jis gerokai sumažina saugojimo ir skaičiavimo reikalavimus. INT8 kiekinimo metu modelio svoriai ir aktyvacijos reikšmės pereina kiekinimo procesą, įskaitant mastelį ir poslinkį, kad būtų išsaugota kuo daugiau originalios plaukiojančio kablelio informacijos. Infernso metu šios kiekinamos reikšmės dekiuinuojamos atgal į plaukiojančio kablelio skaičius skaičiavimui, o po to vėl kiekinamos į INT8 kitam žingsniui. Šis metodas daugeliu atvejų gali suteikti pakankamą tikslumą išlaikant aukštą skaičiavimo efektyvumą.

### **FP16**

FP16 formatas, tai yra 16 bitų plaukiojantieji skaičiai (float16), sumažina atminties naudojimą perpus, palyginti su 32 bitų plaukiojančio kablelio skaičiais (float32), kas turi reikšmingų privalumų didelio masto giluminio mokymosi programose. FP16 formatas leidžia įkelti didesnius modelius arba apdoroti daugiau duomenų toje pačioje GPU atminties ribose. Kadangi šiuolaikinė GPU aparatinė įranga toliau palaiko FP16 operacijas, FP16 formato naudojimas gali taip pat pagerinti skaičiavimo greitį. Tačiau FP16 formate taip pat yra savo trūkumų, būtent mažesnis tikslumas, kuris kai kuriais atvejais gali sukelti skaitmeninius nestabilumus ar tikslumo praradimą.

### **FP32**

FP32 formatas suteikia didesnį tikslumą ir gali tiksliai atstovauti platų reikšmių spektrą. Sudėtingų matematinių operacijų atlikimo arba aukšto tikslumo rezultatams reikalaujančiuose scenarijuose pageidaujamas FP32 formatas. Tačiau didelis tikslumas reiškia ir didesnį atminties naudojimą bei ilgesnį skaičiavimo laiką. Didelio masto giluminio mokymosi modeliuose, ypač kai daug modelio parametrų ir didelis duomenų kiekis, FP32 formatas gali sukelti GPU atminties nepakankamumą arba sumažinti inferenso greitį.

Mobiliose ar IoT įrenginiuose galime Phi-3.x modelius konvertuoti į INT4, o AI PC / Copilot PC gali naudoti aukštesnį tikslumą, pvz., INT8, FP16, FP32.

Šiuo metu įvairūs aparatūros gamintojai turi skirtingus pagrindus generatyviniams modeliams palaikyti, tokius kaip Intel OpenVINO, Qualcomm QNN, Apple MLX ir Nvidia CUDA, derindami su modelio kiekinimu, kad atliktų vietinį diegimą.

Technologijų požiūriu, po kiekinimo palaikome skirtingus formatus, pavyzdžiui, PyTorch / TensorFlow formatą, GGUF ir ONNX. Parengiau formatų palyginimą ir taikymo scenarijus tarp GGUF ir ONNX. Čia rekomenduoju ONNX kiekinimo formatą, kuris turi gerą palaikymą nuo modelio pagrindo iki aparatinės įrangos. Šiame skyriuje sutelksime dėmesį į ONNX Runtime GenAI, OpenVINO ir Apple MLX modelio kiekinimui (jei turite geresnį būdą, galite jį pateikti, siųsdami PR).

**Šis skyrius apima**

1. [Phi-3.5 / 4 kiekinimą naudojant llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Phi-3.5 / 4 kiekinimą naudojant Generatyvinių AI plėtinius onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Phi-3.5 / 4 kiekinimą naudojant Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Phi-3.5 / 4 kiekinimą naudojant Apple MLX sistemą](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turi būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingą interpretavimą, kilusį dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->