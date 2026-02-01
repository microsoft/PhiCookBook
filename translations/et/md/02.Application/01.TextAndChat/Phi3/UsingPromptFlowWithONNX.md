# Windows GPU kasutamine PromptFlow lahenduse loomiseks Phi-3.5-Instruct ONNX-iga

Järgnevas dokumendis on näide, kuidas kasutada PromptFlow'd koos ONNX-iga (Open Neural Network Exchange) AI-rakenduste arendamiseks, mis põhinevad Phi-3 mudelitel.

PromptFlow on arendustööriistade komplekt, mis on loodud LLM-põhiste (Large Language Model) AI-rakenduste arendustsükli lihtsustamiseks alates ideest ja prototüüpimisest kuni testimise ja hindamiseni.

PromptFlow ja ONNX-i integreerimise abil saavad arendajad:

- Optimeerida mudeli jõudlust: Kasutada ONNX-i tõhusaks mudeli järeldamiseks ja juurutamiseks.
- Lihtsustada arendust: Kasutada PromptFlow'd töövoo haldamiseks ja korduvate ülesannete automatiseerimiseks.
- Parandada koostööd: Luua parem koostöö meeskonnaliikmete vahel, pakkudes ühtset arenduskeskkonda.

**PromptFlow** on arendustööriistade komplekt, mis on loodud LLM-põhiste AI-rakenduste arendustsükli lihtsustamiseks alates ideest, prototüüpimisest, testimisest, hindamisest kuni tootmisse juurutamise ja jälgimiseni. See muudab promptide inseneeria palju lihtsamaks ja võimaldab luua tootmiskvaliteediga LLM-rakendusi.

PromptFlow saab ühendada OpenAI, Azure OpenAI Service'i ja kohandatavate mudelitega (Huggingface, kohalikud LLM/SLM-id). Me soovime juurutada Phi-3.5 kvantiseeritud ONNX-mudelit kohalikes rakendustes. PromptFlow aitab meil paremini planeerida oma äri ja luua kohalikke lahendusi, mis põhinevad Phi-3.5-l. Selles näites ühendame ONNX Runtime GenAI Library, et luua PromptFlow lahendus, mis põhineb Windows GPU-l.

## **Paigaldamine**

### **ONNX Runtime GenAI Windows GPU jaoks**

Loe juhendit ONNX Runtime GenAI seadistamiseks Windows GPU jaoks [klõpsa siia](./ORTWindowGPUGuideline.md)

### **PromptFlow seadistamine VSCode'is**

1. Paigalda PromptFlow VS Code laiendus

![pfvscode](../../../../../../imgs/02/pfonnx/pfvscode.png)

2. Pärast PromptFlow VS Code laienduse paigaldamist klõpsa laiendusel ja vali **Installation dependencies**, järgides juhendit PromptFlow SDK paigaldamiseks oma keskkonda.

![pfsetup](../../../../../../imgs/02/pfonnx/pfsetup.png)

3. Laadi alla [Näidiskood](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) ja ava see näidis VS Code'is.

![pfsample](../../../../../../imgs/02/pfonnx/pfsample.png)

4. Ava **flow.dag.yaml**, et valida oma Python keskkond.

![pfdag](../../../../../../imgs/02/pfonnx/pfdag.png)

   Ava **chat_phi3_ort.py**, et muuta oma Phi-3.5-instruct ONNX-mudeli asukohta.

![pfphi](../../../../../../imgs/02/pfonnx/pfphi.png)

5. Käivita oma PromptFlow testimiseks.

Ava **flow.dag.yaml** ja klõpsa visuaalsel redaktoril.

![pfv](../../../../../../imgs/02/pfonnx/pfv.png)

Pärast klõpsamist käivita see testimiseks.

![pfflow](../../../../../../imgs/02/pfonnx/pfflow.png)

1. Sa saad terminalis käivitada batch'i, et näha rohkem tulemusi.

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Sa saad tulemusi vaadata oma vaikimisi veebibrauseris.

![pfresult](../../../../../../imgs/02/pfonnx/pfresult.png)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.