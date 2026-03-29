## Peenhäälestamise stsenaariumid

![FineTuning with MS Services](../../../../translated_images/et/FinetuningwithMS.3d0cec8ae693e094.webp)

See jaotis annab ülevaate peenhäälestamise stsenaariumitest Microsoft Foundry ja Azure keskkondades, sealhulgas juurutusmudelitest, infrastruktuuri kihtidest ja tavaliselt kasutatavatest optimeerimistehnikatest.

**Platvorm**  
Siia kuuluvad haldusteenused nagu Microsoft Foundry (varem Microsoft Foundry) ja Azure Machine Learning, mis pakuvad mudeli haldust, orkestreerimist, katsete jälgimist ja juurutusvooge.

**Infrastruktuur**  
Peenhäälestamiseks on vaja skaleeritavaid arvutusressursse. Azure keskkondades hõlmab see tavaliselt GPU-põhiseid virtuaalmasinaid ja CPU ressursse kergeteks töökoormusteks, samuti skaleeritavat salvestust andmekogumite ja kontrollpunktide jaoks.

**Tööriistad ja raamistik**  
Peenhäälestamise töövood tuginevad tavaliselt raamistikest ja optimeerimisteekidest nagu Hugging Face Transformers, DeepSpeed ja PEFT (parameetri-efektiivne peenhäälestus).

Peenhäälestamise protsess Microsofti tehnoloogiatega hõlmab platvormiteenuseid, arvutusinfrastruktuuri ja treeninguraamistikke. Mõistes, kuidas need komponendid koos töötavad, saavad arendajad efektiivselt kohandada baasml mudeleid konkreetseteks ülesanneteks ja tootmisstsenaariumiteks.

## Mudel teenusena

Peenhäälestage mudelit majutatud peenhäälestusega ilma vajaduseta luua ja hallata arvutusressursse.

![MaaS Fine Tuning](../../../../translated_images/et/MaaSfinetune.3eee4630607aff0d.webp)

Serverita peenhäälestus on nüüd saadaval Phi-3, Phi-3.5 ja Phi-4 mudelifamiljadele, võimaldades arendajatel kiiresti ja lihtsalt kohandada mudeleid pilve- ja servastsenaariumiteks ilma arvutuse korraldamiseta.

## Mudel platvormina

Kasutajad haldavad oma arvutusressursse, et peenhäälestada oma mudeleid.

![Maap Fine Tuning](../../../../translated_images/et/MaaPFinetune.fd3829c1122f5d1c.webp)

[Fine Tuning Sample](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Peenhäälestuse tehnikate võrdlus

|Stsenaarium|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Eeltreenitud suurte keelemudelite kohandamine konkreetseteks ülesanneteks või domeenideks|Jah|Jah|Jah|Jah|Jah|Jah|
|Peenhäälestus NLP ülesannete jaoks nagu teksti klassifitseerimine, nimetatud isikute tuvastamine ja masintõlge|Jah|Jah|Jah|Jah|Jah|Jah|
|Peenhäälestus küsimustele vastamise ülesannete jaoks|Jah|Jah|Jah|Jah|Jah|Jah|
|Peenhäälestus inimlaadsete vastuste genereerimiseks juturobotites|Jah|Jah|Jah|Jah|Jah|Jah|
|Peenhäälestus muusika, kunsti või muu loomingulise sisu genereerimiseks|Jah|Jah|Jah|Jah|Jah|Jah|
|Arvutus- ja rahaliste kulude vähendamine|Jah|Jah|Jah|Jah|Jah|Jah|
|Mälu kasutuse vähendamine|Jah|Jah|Jah|Jah|Jah|Jah|
|Vähemate parameetrite kasutamine tõhusaks peenhäälestuseks|Jah|Jah|Jah|Ei|Ei|Jah|
|Mälusäästlik andmete paralleelsuse vorm, mis võimaldab kasutada kõigi olemasolevate GPU seadmete liitmälu|Ei|Ei|Ei|Jah|Jah|Ei|

> [!NOTE]
> LoRA, QLoRA, PEFT ja DoRA on parameetri-effektiivsed peenhäälestusmeetodid, samas kui DeepSpeed ja ZeRO keskenduvad jaotatud treeningule ja mälutalitlusele.

## Peenhäälestuse jõudluse näited

![Finetuning Performance](../../../../translated_images/et/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüdleme täpsuse poole, palun pange tähele, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle emakeeles tuleks pidada ametlikuks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->