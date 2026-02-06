See demo näitab, kuidas kasutada eelõpetatud mudelit Python-koodi genereerimiseks pildi ja tekstilise juhise põhjal.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Siin on samm-sammuline selgitus:

1. **Importimine ja seadistamine**:
   - Vajalikud teegid ja moodulid imporditakse, sealhulgas `requests`, `PIL` pilditöötluseks ja `transformers` mudeli ja töötlemise haldamiseks.

2. **Pildi laadimine ja kuvamine**:
   - Pildifail (`demo.png`) avatakse `PIL` teegi abil ja kuvatakse.

3. **Juhise määratlemine**:
   - Koostatakse sõnum, mis sisaldab pilti ja palvet genereerida Python-kood pildi töötlemiseks ja selle salvestamiseks `plt` (matplotlib) abil.

4. **Protsessori laadimine**:
   - `AutoProcessor` laaditakse eelõpetatud mudelist, mis on määratud `out_dir` kataloogis. See protsessor töötleb tekstilisi ja visuaalseid sisendeid.

5. **Juhise loomine**:
   - `apply_chat_template` meetodit kasutatakse sõnumi vormindamiseks mudelile sobivaks juhiseks.

6. **Sisendite töötlemine**:
   - Juhis ja pilt töödeldakse tensoriteks, mida mudel suudab mõista.

7. **Generatsiooni argumentide määramine**:
   - Määratakse mudeli generatsiooniprotsessi argumendid, sealhulgas maksimaalne uute tokenite arv ja kas väljundit tuleks proovida.

8. **Koodi genereerimine**:
   - Mudel genereerib Python-koodi sisendite ja generatsiooni argumentide põhjal. `TextStreamer` kasutatakse väljundi haldamiseks, jättes vahele juhise ja spetsiaalsed tokenid.

9. **Väljund**:
   - Genereeritud kood prinditakse, mis peaks sisaldama Python-koodi pildi töötlemiseks ja salvestamiseks vastavalt juhisele.

See demo illustreerib, kuidas kasutada eelõpetatud mudelit OpenVino abil, et dünaamiliselt genereerida koodi vastavalt kasutaja sisendile ja piltidele.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.