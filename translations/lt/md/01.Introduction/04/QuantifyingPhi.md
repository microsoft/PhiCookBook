<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-09-12T14:52:29+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "lt"
}
-->
# **Phi šeimos kvantifikavimas**

Modelio kvantifikavimas reiškia procesą, kai neuroninio tinklo modelio parametrai (tokie kaip svoriai ir aktyvavimo reikšmės) yra perkelti iš didelio reikšmių diapazono (dažniausiai nenutrūkstamo diapazono) į mažesnį, baigtinį reikšmių diapazoną. Ši technologija gali sumažinti modelio dydį ir skaičiavimo sudėtingumą bei pagerinti modelio veikimo efektyvumą aplinkose, kuriose riboti resursai, pavyzdžiui, mobiliuosiuose įrenginiuose ar įterptinėse sistemose. Modelio kvantifikavimas pasiekia suspaudimą sumažindamas parametrų tikslumą, tačiau tai taip pat sukelia tam tikrą tikslumo praradimą. Todėl kvantifikavimo procese būtina subalansuoti modelio dydį, skaičiavimo sudėtingumą ir tikslumą. Dažniausiai naudojami kvantifikavimo metodai apima fiksuoto taško kvantifikavimą, slankiojo taško kvantifikavimą ir kt. Galite pasirinkti tinkamą kvantifikavimo strategiją pagal konkrečią situaciją ir poreikius.

Tikimės, kad GenAI modelį galėsime diegti kraštiniuose įrenginiuose ir leisti daugiau įrenginių dalyvauti GenAI scenarijuose, tokiuose kaip mobilieji įrenginiai, AI PC / Copilot+PC ir tradiciniai IoT įrenginiai. Naudodami kvantifikavimo modelį, galime jį pritaikyti skirtingiems kraštiniams įrenginiams, atsižvelgiant į jų specifikacijas. Derinant su modelio spartinimo sistemomis ir kvantifikavimo modeliais, kuriuos teikia techninės įrangos gamintojai, galime sukurti geresnius SLM taikymo scenarijus.

Kvantifikavimo scenarijuose turime skirtingus tikslumo lygius (INT4, INT8, FP16, FP32). Toliau pateikiamas dažniausiai naudojamų kvantifikavimo tikslumo lygių paaiškinimas.

### **INT4**

INT4 kvantifikavimas yra radikalus kvantifikavimo metodas, kuris modelio svorius ir aktyvavimo reikšmes kvantifikuoja į 4 bitų sveikuosius skaičius. INT4 kvantifikavimas dažniausiai sukelia didesnį tikslumo praradimą dėl mažesnio reprezentavimo diapazono ir žemesnio tikslumo. Tačiau, palyginti su INT8 kvantifikavimu, INT4 kvantifikavimas gali dar labiau sumažinti modelio saugojimo reikalavimus ir skaičiavimo sudėtingumą. Reikėtų pažymėti, kad INT4 kvantifikavimas praktiniuose taikymuose yra gana retas, nes per mažas tikslumas gali sukelti reikšmingą modelio veikimo pablogėjimą. Be to, ne visa techninė įranga palaiko INT4 operacijas, todėl renkantis kvantifikavimo metodą reikia atsižvelgti į techninės įrangos suderinamumą.

### **INT8**

INT8 kvantifikavimas yra procesas, kai modelio svoriai ir aktyvavimo reikšmės iš slankiojo taško skaičių konvertuojami į 8 bitų sveikuosius skaičius. Nors INT8 sveikieji skaičiai turi mažesnį reprezentavimo diapazoną ir mažesnį tikslumą, jie gali reikšmingai sumažinti saugojimo ir skaičiavimo reikalavimus. INT8 kvantifikavimo metu modelio svoriai ir aktyvavimo reikšmės pereina kvantifikavimo procesą, įskaitant skalavimą ir poslinkį, kad būtų kuo labiau išsaugota pradinė slankiojo taško informacija. Inference metu šios kvantifikuotos reikšmės bus dekvantifikuotos atgal į slankiojo taško skaičius skaičiavimui, o vėliau vėl kvantifikuotos į INT8 kitam žingsniui. Šis metodas daugumoje taikymų gali užtikrinti pakankamą tikslumą, išlaikant aukštą skaičiavimo efektyvumą.

### **FP16**

FP16 formatas, tai yra 16 bitų slankiojo taško skaičiai (float16), sumažina atminties naudojimą perpus, palyginti su 32 bitų slankiojo taško skaičiais (float32), ir turi reikšmingų pranašumų didelio masto giluminio mokymosi taikymuose. FP16 formatas leidžia įkelti didesnius modelius arba apdoroti daugiau duomenų, esant tiems patiems GPU atminties apribojimams. Kadangi moderni GPU techninė įranga vis dažniau palaiko FP16 operacijas, FP16 formato naudojimas taip pat gali pagerinti skaičiavimo greitį. Tačiau FP16 formatas turi ir savo trūkumų, būtent mažesnį tikslumą, kuris kai kuriais atvejais gali sukelti skaitmeninį nestabilumą arba tikslumo praradimą.

### **FP32**

FP32 formatas užtikrina didesnį tikslumą ir gali tiksliai reprezentuoti platų reikšmių diapazoną. Scenarijuose, kuriuose atliekamos sudėtingos matematinės operacijos arba reikalingi aukšto tikslumo rezultatai, pirmenybė teikiama FP32 formatui. Tačiau didelis tikslumas taip pat reiškia didesnį atminties naudojimą ir ilgesnį skaičiavimo laiką. Didelio masto giluminio mokymosi modeliams, ypač kai yra daug modelio parametrų ir didžiulis duomenų kiekis, FP32 formatas gali sukelti GPU atminties trūkumą arba sumažinti inference greitį.

Mobiliesiems įrenginiams ar IoT įrenginiams galime konvertuoti Phi-3.x modelius į INT4, o AI PC / Copilot PC gali naudoti didesnį tikslumą, pavyzdžiui, INT8, FP16, FP32.

Šiuo metu skirtingi techninės įrangos gamintojai turi skirtingas sistemas, palaikančias generatyvinius modelius, tokias kaip Intel OpenVINO, Qualcomm QNN, Apple MLX ir Nvidia CUDA, ir kartu su modelio kvantifikavimu galima atlikti vietinį diegimą.

Technologiniu požiūriu, po kvantifikavimo turime skirtingų formatų palaikymą, tokių kaip PyTorch / Tensorflow formatas, GGUF ir ONNX. Atlikau formatų palyginimą ir taikymo scenarijus tarp GGUF ir ONNX. Čia rekomenduoju ONNX kvantifikavimo formatą, kuris turi gerą palaikymą nuo modelio sistemos iki techninės įrangos. Šiame skyriuje daugiausia dėmesio skirsime ONNX Runtime GenAI, OpenVINO ir Apple MLX modelio kvantifikavimui (jei turite geresnį būdą, galite jį pateikti mums, pateikdami PR).

**Šis skyrius apima**

1. [Phi-3.5 / 4 kvantifikavimas naudojant llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Phi-3.5 / 4 kvantifikavimas naudojant generatyvinius AI plėtinius onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Phi-3.5 / 4 kvantifikavimas naudojant Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Phi-3.5 / 4 kvantifikavimas naudojant Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.