<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "743d7e9cb9c4e8ea642d77bee657a7fa",
  "translation_date": "2025-10-11T11:45:35+00:00",
  "source_file": "md/03.FineTuning/LetPhi3gotoIndustriy.md",
  "language_code": "et"
}
-->
# **Las Phi-3 saada tööstusekspert**

Et viia Phi-3 mudel tööstusesse, tuleb mudelisse lisada tööstuse ärialaseid andmeid. Selleks on kaks erinevat võimalust: RAG (Retrieval Augmented Generation) ja Fine Tuning.

## **RAG vs Fine-Tuning**

### **Retrieval Augmented Generation**

RAG ühendab andmete otsingu ja tekstigeneratsiooni. Ettevõtte struktureeritud ja struktureerimata andmed salvestatakse vektordaatabaasi. Otsides asjakohast sisu, leitakse vastav kokkuvõte ja kontekst ning kombineeritakse LLM/SLM tekstitäiendamise võimekus, et genereerida sisu.

### **Fine-tuning**

Fine-tuning põhineb olemasoleva mudeli täiustamisel. See ei nõua mudelialgoritmi nullist alustamist, kuid andmeid tuleb pidevalt koguda. Kui tööstusrakendustes on vaja täpsemat terminoloogiat ja keelekasutust, on fine-tuning parem valik. Kuid kui andmed muutuvad sageli, võib fine-tuning muutuda keeruliseks.

### **Kuidas valida**

1. Kui vastus nõuab väliste andmete kaasamist, on RAG parim valik.

2. Kui on vaja stabiilset ja täpset tööstusalast teadmist, on fine-tuning hea valik. RAG keskendub asjakohase sisu leidmisele, kuid ei pruugi alati tabada spetsialiseeritud nüansse.

3. Fine-tuning vajab kvaliteetset andmekogumit, kuid kui andmed on piiratud ulatusega, ei pruugi see palju muuta. RAG on paindlikum.

4. Fine-tuning on nagu must kast, keeruline mõista selle sisemisi mehhanisme. Kuid RAG võimaldab lihtsamalt leida andmete allika, aidates tõhusalt korrigeerida eksitusi või sisuvigu ning pakkudes paremat läbipaistvust.

### **Kasutusjuhtumid**

1. Vertikaalsed tööstused, mis vajavad spetsiifilist erialaterminoloogiat ja väljendusi, ***Fine-tuning*** on parim valik.

2. KKK-süsteem, mis hõlmab erinevate teadmistepunktide sünteesi, ***RAG*** on parim valik.

3. Automaatse ärivoo kombinatsioon ***RAG + Fine-tuning*** on parim valik.

## **Kuidas kasutada RAG-i**

![rag](../../../../imgs/03/intro/rag.png)

Vektordaatabaas on matemaatilisel kujul salvestatud andmete kogum. Vektordaatabaasid muudavad masinõppemudelitele varasemate sisendite meeldejätmise lihtsamaks, võimaldades masinõpet kasutada otsingu, soovituste ja tekstigeneratsiooni rakendustes. Andmeid saab tuvastada sarnasuse mõõdikute alusel, mitte täpse vastavuse järgi, võimaldades arvutimudelitel mõista andmete konteksti.

Vektordaatabaas on RAG-i realiseerimise võti. Saame andmed vektorite kujul salvestada vektormudelite, nagu text-embedding-3, jina-ai-embedding, jne abil.

Lisateave RAG-i rakenduse loomise kohta [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo)

## **Kuidas kasutada Fine-tuningut**

Fine-tuningus kasutatakse tavaliselt algoritme Lora ja QLora. Kuidas valida?
- [Lisateave selle näidisnotebookiga](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Näide Python FineTuning skriptist](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora ja QLora**

![lora](../../../../imgs/03/intro/qlora.png)

LoRA (Low-Rank Adaptation) ja QLoRA (Quantized Low-Rank Adaptation) on mõlemad tehnikad, mida kasutatakse suurte keelemudelite (LLM) peenhäälestamiseks, rakendades parameetrite efektiivset peenhäälestust (PEFT). PEFT-tehnikad on loodud mudelite tõhusamaks treenimiseks võrreldes traditsiooniliste meetoditega.  
LoRA on iseseisev peenhäälestamise tehnika, mis vähendab mälukasutust, rakendades madala astme lähendust kaalu uuendusmaatriksile. See pakub kiiret treeninguaega ja säilitab jõudluse, mis on lähedane traditsioonilistele peenhäälestamise meetoditele.

QLoRA on LoRA laiendatud versioon, mis sisaldab kvantiseerimistehnikaid mälukasutuse edasiseks vähendamiseks. QLoRA kvantiseerib eeltreenitud LLM-i kaaluparameetrite täpsuse 4-bitisele täpsusele, mis on mälusäästlikum kui LoRA. Kuid QLoRA treenimine on umbes 30% aeglasem kui LoRA treenimine täiendavate kvantiseerimis- ja dekvantiseerimisetappide tõttu.

QLoRA kasutab LoRA-d lisana, et parandada kvantiseerimisvigade tõttu tekkinud vigu. QLoRA võimaldab massiivsete mudelite, millel on miljardeid parameetreid, peenhäälestamist suhteliselt väikestel ja laialdaselt kättesaadavatel GPU-del. Näiteks QLoRA suudab peenhäälestada 70B parameetriga mudelit, mis vajab 36 GPU-d, kasutades ainult 2.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.