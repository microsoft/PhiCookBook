## Peenhäälestamine vs RAG

## Retrieval Augmented Generation

RAG ühendab andmete otsingu ja teksti genereerimise. Ettevõtte struktureeritud ja struktureerimata andmed salvestatakse vektordaatabaasi. Kui otsitakse asjakohast sisu, leitakse vastav kokkuvõte ja sisu, et moodustada kontekst, ning LLM/SLM-i teksti täiendamise võimekust kasutatakse sisu loomiseks.

## RAG protsess
![FinetuningvsRAG](../../../../imgs/03/intro/rag.png)

## Peenhäälestamine
Peenhäälestamine põhineb olemasoleva mudeli täiustamisel. See ei nõua mudelialgoritmi nullist alustamist, kuid andmeid tuleb pidevalt koguda. Kui tööstusrakendustes on vaja täpsemaid termineid ja keelekasutust, on peenhäälestamine parem valik. Kuid kui teie andmed muutuvad sageli, võib peenhäälestamine muutuda keeruliseks.

## Kuidas valida
Kui meie vastus vajab väliste andmete kaasamist, on RAG parim valik.

Kui on vaja esitada stabiilset ja täpset tööstusalast teadmust, on peenhäälestamine hea valik. RAG keskendub asjakohase sisu leidmisele, kuid ei pruugi alati tabada spetsialiseeritud nüansse.

Peenhäälestamine nõuab kvaliteetset andmekogumit, ja kui tegemist on vaid väikese andmehulga, ei pruugi see palju muutust tuua. RAG on paindlikum.  
Peenhäälestamine on nagu must kast, metafüüsika, ja selle sisemisi mehhanisme on raske mõista. Kuid RAG võimaldab lihtsamalt leida andmete allika, mis aitab tõhusalt korrigeerida hallutsinatsioone või sisuvigu ning pakub paremat läbipaistvust.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.