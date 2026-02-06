# **Inference Phi-3 kohalikus serveris**

Me saame juurutada Phi-3 kohalikus serveris. Kasutajad võivad valida [Ollama](https://ollama.com) või [LM Studio](https://llamaedge.com) lahenduste vahel või kirjutada oma koodi. Phi-3 kohalike teenustega saab ühendust luua [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) või [Langchain](https://www.langchain.com/) kaudu, et luua Copilot rakendusi.


## **Semantic Kernel'i kasutamine Phi-3-mini juurde pääsemiseks**

Copilot rakenduses loome rakendusi läbi Semantic Kernel'i / LangChain'i. Selline rakenduste raamistik on üldiselt ühilduv Azure OpenAI Service / OpenAI mudelitega ning toetab ka avatud lähtekoodiga mudeleid Hugging Face'is ja kohalikke mudeleid. Mida peaksime tegema, kui tahame kasutada Semantic Kernel'it Phi-3-mini juurde pääsemiseks? Näiteks .NET-i kasutades saame seda kombineerida Hugging Face Connector'iga Semantic Kernel'is. Vaikimisi vastab see Hugging Face'i mudeli ID-le (esmakordsel kasutamisel laaditakse mudel Hugging Face'ist alla, mis võtab aega). Samuti saab ühenduda loodud kohaliku teenusega. Võrreldes kahega soovitame kasutada viimast, kuna see pakub suuremat autonoomiat, eriti ettevõtte rakendustes.

![sk](../../../../../imgs/01/03/LocalServer/sk.png)


Jooniselt on näha, et kohalike teenuste juurde pääsemine läbi Semantic Kernel'i võimaldab hõlpsasti ühenduda ise loodud Phi-3-mini mudeli serveriga. Siin on käivitamise tulemus:


![skrun](../../../../../imgs/01/03/LocalServer/skrun.png)

***Näidiskood*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.