## Peenhäälestamise stsenaariumid

![Peenhäälestamine Microsofti teenustega](../../../../imgs/03/intro/FinetuningwithMS.png)

**Platvorm** See hõlmab erinevaid tehnoloogiaid, nagu Azure AI Foundry, Azure Machine Learning, AI Tools, Kaito ja ONNX Runtime.

**Infrastruktuur** See hõlmab protsessoreid (CPU) ja FPGA-sid, mis on peenhäälestamise protsessi jaoks hädavajalikud. Siin on ikoonid iga tehnoloogia jaoks.

**Tööriistad ja raamistikud** See hõlmab ONNX Runtime'i. Siin on ikoonid nende tehnoloogiate jaoks.  
[Lisa ikoonid ONNX Runtime'i jaoks]

Microsofti tehnoloogiate abil peenhäälestamise protsess hõlmab mitmeid komponente ja tööriistu. Nende tehnoloogiate mõistmise ja kasutamise abil saame tõhusalt oma rakendusi peenhäälestada ja luua paremaid lahendusi.

## Mudel kui teenus

Peenhäälesta mudelit, kasutades hostitud peenhäälestamist, ilma et oleks vaja arvutusressursse luua ja hallata.

![MaaS Peenhäälestamine](../../../../imgs/03/intro/MaaSfinetune.png)

Serverivaba peenhäälestamine on saadaval Phi-3-mini ja Phi-3-medium mudelite jaoks, võimaldades arendajatel kiiresti ja lihtsalt kohandada mudeleid pilve- ja servastsenaariumide jaoks, ilma et oleks vaja arvutusressursse korraldada. Samuti oleme teatanud, et Phi-3-small on nüüd saadaval meie Models-as-a-Service pakkumise kaudu, et arendajad saaksid kiiresti ja lihtsalt alustada tehisintellekti arendamist, ilma et peaksid haldama taustal olevat infrastruktuuri.

## Mudel kui platvorm

Kasutajad haldavad oma arvutusressursse, et peenhäälestada oma mudeleid.

![Maap Peenhäälestamine](../../../../imgs/03/intro/MaaPFinetune.png)

[Peenhäälestamise näidis](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Peenhäälestamise stsenaariumid

| | | | | | | |
|-|-|-|-|-|-|-|
|Stsenaarium|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|Eeltreenitud LLM-ide kohandamine konkreetsete ülesannete või valdkondade jaoks|Jah|Jah|Jah|Jah|Jah|Jah|
|Peenhäälestamine NLP ülesannete jaoks, nagu teksti klassifitseerimine, nimede tuvastamine ja masintõlge|Jah|Jah|Jah|Jah|Jah|Jah|
|Peenhäälestamine küsimuste-vastuste ülesannete jaoks|Jah|Jah|Jah|Jah|Jah|Jah|
|Peenhäälestamine inimlaadsete vastuste genereerimiseks vestlusrobotites|Jah|Jah|Jah|Jah|Jah|Jah|
|Peenhäälestamine muusika, kunsti või muude loominguliste väljundite genereerimiseks|Jah|Jah|Jah|Jah|Jah|Jah|
|Arvutus- ja rahaliste kulude vähendamine|Jah|Jah|Ei|Jah|Jah|Ei|
|Mälu kasutamise vähendamine|Ei|Jah|Ei|Jah|Jah|Jah|
|Vähemate parameetrite kasutamine tõhusaks peenhäälestamiseks|Ei|Jah|Jah|Ei|Ei|Jah|
|Mälu tõhus andmeparalleelsus, mis võimaldab kasutada kõigi saadaolevate GPU-seadmete kogumälu|Ei|Ei|Ei|Jah|Jah|Jah|

## Peenhäälestamise jõudluse näited

![Peenhäälestamise jõudlus](../../../../imgs/03/intro/Finetuningexamples.png)

---

**Vastutusest loobumine**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta arusaamatuste või valesti tõlgenduste eest, mis võivad tuleneda selle tõlke kasutamisest.