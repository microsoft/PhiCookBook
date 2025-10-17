<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-10-11T12:26:38+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "et"
}
-->
# **Phi perekonna kvantifitseerimine**

Mudeli kvantifitseerimine viitab protsessile, kus tehisnärvivõrgu mudeli parameetrid (näiteks kaalud ja aktivatsiooniväärtused) kaardistatakse suurest väärtuste vahemikust (tavaliselt pidevast vahemikust) väiksemasse lõplikku väärtuste vahemikku. See tehnoloogia aitab vähendada mudeli suurust ja arvutuslikku keerukust ning parandada mudeli töö efektiivsust ressursipiirangutega keskkondades, nagu mobiilseadmed või manussüsteemid. Mudeli kvantifitseerimine saavutab tihendamise, vähendades parameetrite täpsust, kuid see toob kaasa ka teatud täpsuse kaotuse. Seetõttu on kvantifitseerimise protsessis oluline tasakaalustada mudeli suurust, arvutuslikku keerukust ja täpsust. Levinud kvantifitseerimismeetodid hõlmavad fikseeritud punkti kvantifitseerimist, ujuvpunktilist kvantifitseerimist jne. Sobiva kvantifitseerimisstrateegia saab valida vastavalt konkreetsele olukorrale ja vajadustele.

Meie eesmärk on juurutada GenAI mudel ääreseadmetele ja võimaldada rohkematel seadmetel siseneda GenAI stsenaariumidesse, nagu mobiilseadmed, AI PC/Copilot+PC ja traditsioonilised IoT-seadmed. Kvantifitseeritud mudeli abil saame seda juurutada erinevatele ääreseadmetele vastavalt seadme tüübile. Kombineerides riistvaratootjate pakutud mudeli kiirendusraamistiku ja kvantifitseeritud mudeli, saame luua paremaid SLM-i rakendusstsenaariume.

Kvantifitseerimise stsenaariumis on meil erinevad täpsused (INT4, INT8, FP16, FP32). Järgnevalt on selgitus levinud kvantifitseerimistäpsuste kohta.

### **INT4**

INT4 kvantifitseerimine on radikaalne kvantifitseerimismeetod, mis kvantifitseerib mudeli kaalud ja aktivatsiooniväärtused 4-bitisteks täisarvudeks. INT4 kvantifitseerimine põhjustab tavaliselt suuremat täpsuse kaotust, kuna esitusvahemik on väiksem ja täpsus madalam. Kuid võrreldes INT8 kvantifitseerimisega võib INT4 kvantifitseerimine veelgi vähendada mudeli salvestusnõudeid ja arvutuslikku keerukust. Tuleb märkida, et INT4 kvantifitseerimine on praktilistes rakendustes suhteliselt haruldane, kuna liiga madal täpsus võib põhjustada mudeli jõudluse olulist halvenemist. Lisaks ei toeta kõik riistvarad INT4 operatsioone, seega tuleb kvantifitseerimismeetodi valimisel arvestada riistvara ühilduvust.

### **INT8**

INT8 kvantifitseerimine on protsess, kus mudeli kaalud ja aktivatsioonid teisendatakse ujuvpunktilistest arvudest 8-bitisteks täisarvudeks. Kuigi INT8 täisarvude esitusvahemik on väiksem ja täpsus madalam, võib see oluliselt vähendada salvestus- ja arvutusnõudeid. INT8 kvantifitseerimisel läbivad mudeli kaalud ja aktivatsiooniväärtused kvantifitseerimisprotsessi, mis hõlmab skaleerimist ja nihutamist, et säilitada võimalikult palju algset ujuvpunktilist teavet. Järelduste tegemisel dekvantifitseeritakse need kvantifitseeritud väärtused tagasi ujuvpunktilisteks arvudeks arvutamiseks ja seejärel kvantifitseeritakse need uuesti INT8-ks järgmise sammu jaoks. See meetod suudab enamikus rakendustes pakkuda piisavat täpsust, säilitades samal ajal kõrge arvutustõhususe.

### **FP16**

FP16 formaat, ehk 16-bitised ujuvpunktilised arvud (float16), vähendab mälukasutust poole võrra võrreldes 32-bitiste ujuvpunktiliste arvudega (float32), mis on suurte süvaõppe rakenduste puhul märkimisväärne eelis. FP16 formaat võimaldab laadida suuremaid mudeleid või töödelda rohkem andmeid sama GPU mälupiirangu raames. Kuna kaasaegne GPU riistvara toetab üha enam FP16 operatsioone, võib FP16 formaadi kasutamine tuua kaasa ka arvutuskiiruse paranemise. Kuid FP16 formaadil on ka oma olemuslikud puudused, nimelt madalam täpsus, mis võib mõnel juhul põhjustada arvulist ebastabiilsust või täpsuse kaotust.

### **FP32**

FP32 formaat pakub suuremat täpsust ja suudab täpselt esitada laia väärtuste vahemikku. Stsenaariumides, kus tehakse keerulisi matemaatilisi operatsioone või on vaja kõrgetäpsuslikke tulemusi, eelistatakse FP32 formaati. Kuid kõrge täpsus tähendab ka suuremat mälukasutust ja pikemat arvutusaega. Suurte süvaõppe mudelite puhul, eriti kui mudeliparameetreid ja andmemahtu on palju, võib FP32 formaat põhjustada GPU mälu puudujääki või järelduskiiruse vähenemist.

Mobiilseadmetes või IoT-seadmetes saame teisendada Phi-3.x mudelid INT4-ks, samas kui AI PC / Copilot PC võib kasutada suuremat täpsust, nagu INT8, FP16, FP32.

Praegu on erinevatel riistvaratootjatel erinevad raamistikud generatiivsete mudelite toetamiseks, näiteks Inteli OpenVINO, Qualcomi QNN, Apple'i MLX ja Nvidia CUDA. Kombineerides mudeli kvantifitseerimist, saab neid kasutada lokaalseks juurutamiseks.

Tehnoloogia osas on meil kvantifitseerimise järel erinevad formaaditoetused, nagu PyTorch / Tensorflow formaat, GGUF ja ONNX. Olen teinud GGUF-i ja ONNX-i formaadi võrdluse ja rakendusstsenaariumid. Siin soovitan ONNX kvantifitseerimisformaati, millel on hea tugi mudeliraamistikust riistvarani. Selles peatükis keskendume ONNX Runtime'ile GenAI jaoks, OpenVINO-le ja Apple MLX-ile mudeli kvantifitseerimiseks (kui teil on parem viis, saate selle meile esitada PR-i kaudu).

**See peatükk sisaldab**

1. [Phi-3.5 / 4 kvantifitseerimine kasutades llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Phi-3.5 / 4 kvantifitseerimine kasutades Generative AI laiendusi onnxruntime jaoks](./UsingORTGenAIQuantifyingPhi.md)

3. [Phi-3.5 / 4 kvantifitseerimine kasutades Inteli OpenVINO-d](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Phi-3.5 / 4 kvantifitseerimine kasutades Apple MLX raamistikku](./UsingAppleMLXQuantifyingPhi.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.