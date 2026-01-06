<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-05T14:48:34+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "et"
}
-->
# **Phi perekonna kvantimine**

Mudeli kvantimine viitab protsessile, kus närvivõrgu mudeli parameetrid (näiteks kaalud ja aktivatsiooniväärtused) kaardistatakse suurest väärtuse vahemikust (tavaliselt pidevast väärtuse vahemikust) väiksemasse lõplikku väärtuse vahemikku. See tehnoloogia võimaldab mudeli suurust ja arvutuslikku keerukust vähendada ning parandada mudeli töö efektiivsust ressursinappuses keskkondades nagu mobiilseadmed või manussüsteemid. Mudeli kvantimine saavutab tihendamise, vähendades parameetrite täpsust, kuid toob kaasa ka teatud täpsuskadude. Seetõttu tuleb kvantimisprotsessis tasakaalustada mudeli suurus, arvutuslik keerukus ja täpsus. Levinumad kvantimismeetodid hõlmavad fikseeritud koma kvantimist, ujuvkomaga kvantimist jms. Konkreetse stsenaariumi ja vajaduste järgi saab valida sobiva kvantimisstrateegia.

Soovime GenAI mudelit servaseadmetesse juurutada ning lubada rohkem seadmetel GenAI stsenaariumitesse siseneda, näiteks mobiilseadmed, AI PC/Copilot+PC ja traditsioonilised IoT seadmed. Kvantimismudeli kaudu saame selle juurutada erinevatesse servaseadmetesse vastavalt seadme tüübile. Koos riistvaratootjate poolt pakutava mudeli kiirendusraamistiku ja kvantimismudeliga saame ehitada paremaid SLM rakendusstsenaariume.

Kvantimistsenaariumis on meil erinevad täpsused (INT4, INT8, FP16, FP32). Järgnevalt on seletatud tavaliselt kasutatavaid kvantimise täpsusi.

### **INT4**

INT4 kvantimine on radikaalne kvantimismeetod, mis kvantib mudeli kaalud ja aktivatsiooniväärtused 4-bitisteks täisarvudeks. INT4 kvantimine põhjustab tavaliselt suuremaid täpsuskadusid väiksema esitlusvahemiku ja madalama täpsuse tõttu. Kuid võrreldes INT8 kvantimisega võib INT4 kvantimine veelgi vähendada salvestusnõudeid ja arvutuslikku keerukust. Tuleb märkida, et INT4 kvantimine on praktilistes rakendustes suhteliselt harv, kuna liiga madal täpsus võib põhjustada mudeli jõudluse olulist langust. Lisaks ei toeta kõik riistvara INT4 operatsioone, seega tuleb kvantimismeetodit valides arvestada riistvara ühilduvust.

### **INT8**

INT8 kvantimine on protsess, kus mudeli kaalud ja aktivatsioonid teisendatakse ujuvkomaarvudelt 8-bitisteks täisarvudeks. Kuigi INT8 täisarvud esindavad väiksemat ja vähem täpset numbrivahemikku, vähendab see oluliselt salvestus- ja arvutusnõudeid. INT8 kvantimisel läbivad mudeli kaalud ja aktivatsiooniväärtused kvantimisprotsessi, mis hõlmab skaleerimist ja nihutamist, et säilitada algset ujuvkomateavet võimalikult palju. Järeldamisel kodeeritakse need kvantitud väärtused tagasi ujuvkomaarvudeks arvutusteks ja seejärel jälle INT8-ks järgmiseks sammuks. See meetod võimaldab enamikus rakendustes piisavat täpsust samal ajal hoides kõrget arvutuslikku efektiivsust.

### **FP16**

FP16 formaat, ehk 16-bitised ujuvkomaarvud (float16), vähendab mälumahu poole võrra võrreldes 32-bitiste ujuvkomaarvudega (float32), mis annab olulisi eeliseid ulatuslikes süvaõppimise rakendustes. FP16 formaat võimaldab laadida suuremaid mudeleid või töödelda rohkem andmeid samades GPU mälupiirides. Kuna kaasaegsed GPU riistvarad toetavad üha enam FP16 operatsioone, võib FP16 formaadi kasutamine parandada ka arvutussagedust. Siiski on FP16 formaadil ka oma piirangud, nimelt madalam täpsus, mis võib mõnel juhul põhjustada arvutusliku stabiilsuse puudumist või täpsuskadusid.

### **FP32**

FP32 formaat tagab kõrgema täpsuse ning suudab täpselt esindada laia väärtuste vahemikku. Sellistes olukordades, kus tehakse keerukaid matemaatilisi operatsioone või on vajalikud kõrge täpsusega tulemused, on eelistatud FP32 formaat. Kuid kõrge täpsus tähendab ka rohkem mälukasutust ja pikemat arvutusaega. Ulatuslike süvaõppimise mudelite puhul, eriti kui on palju mudeliparameetreid ja tohutult andmeid, võib FP32 formaat põhjustada GPU mälu puudujääki või järeldamise kiiruse langust.

Mobiilseadmetes või IoT seadmetes saame Phi-3.x mudeleid teisendada INT4 formaati, samas kui AI PC / Copilot PC võivad kasutada kõrgemat täpsust nagu INT8, FP16 või FP32.

Praegu pakuvad erinevad riistvaratootjad erinevaid raamistikke generatiivsete mudelite toetamiseks, nagu Inteli OpenVINO, Qualcommi QNN, Apple’i MLX ja Nvidia CUDA jm, mida koos mudeli kvantimisega saab kasutada lokaalseks juurutamiseks.

Tehnoloogiliselt on kvantimise järel toetatud erinevaid formaate, näiteks PyTorch / TensorFlow formaat, GGUF ja ONNX. Olen teinud vormingute võrdluse ja rakendusstsenaariumid GGUF ja ONNX vahel. Siin soovitan ONNX kvantimisformaati, millel on hea tugi mudeliraamistiku ja riistvara vahel. Selles peatükis keskendume ONNX Runtime'ile GenAI jaoks, OpenVINOle ja Apple MLX-le mudeli kvantimise teostamiseks (kui teil on parem lahendus, saate selle meile ka PR-i kaudu saata).

**See peatükk sisaldab**

1. [Phi-3.5 / 4 kvantimine kasutades llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Phi-3.5 / 4 kvantimine kasutades Generative AI laiendusi onnxruntime jaoks](./UsingORTGenAIQuantifyingPhi.md)

3. [Phi-3.5 / 4 kvantimine kasutades Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Phi-3.5 / 4 kvantimine kasutades Apple MLX raamistiku](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest vabastamine**:
See dokument on tõlgitud tehisintellektipõhise tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi me püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument oma emakeeles tuleks pidada autoriteetseks allikaks. Kriitilise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selles tõlkes sisalduvate ekslike tõlgenduste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->