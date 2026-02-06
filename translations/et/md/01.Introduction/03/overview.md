Inference tähendab Phi-3-mini kontekstis protsessi, kus mudelit kasutatakse ennustuste tegemiseks või väljundite genereerimiseks sisendandmete põhjal. Siin on rohkem teavet Phi-3-mini ja selle järeldusvõime kohta.

Phi-3-mini kuulub Microsofti poolt välja antud Phi-3 mudelite seeriasse. Need mudelid on loodud selleks, et muuta väikeste keelemudelite (SLM) võimaluste piire.

Siin on mõned olulised punktid Phi-3-mini ja selle järeldusvõime kohta:

## **Phi-3-mini Ülevaade:**
- Phi-3-mini mudelil on 3,8 miljardi parameetri suurus.
- Seda saab käitada mitte ainult traditsioonilistel arvutusseadmetel, vaid ka servaseadmetel, nagu mobiilseadmed ja IoT-seadmed.
- Phi-3-mini väljalase võimaldab nii üksikisikutel kui ka ettevõtetel juurutada SLM-e erinevatel riistvaraseadmetel, eriti piiratud ressurssidega keskkondades.
- Mudel hõlmab erinevaid formaate, sealhulgas traditsiooniline PyTorchi formaat, kvantiseeritud gguf-formaat ja ONNX-põhine kvantiseeritud versioon.

## **Phi-3-mini Juurdepääs:**
Phi-3-mini mudelile pääsemiseks saate kasutada [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) Copiloti rakenduses. Semantic Kernel ühildub üldiselt Azure OpenAI teenusega, avatud lähtekoodiga mudelitega Hugging Face'is ja kohalike mudelitega.
Samuti saate kasutada [Ollama](https://ollama.com) või [LlamaEdge](https://llamaedge.com), et kutsuda kvantiseeritud mudeleid. Ollama võimaldab üksikkasutajatel kutsuda erinevaid kvantiseeritud mudeleid, samas kui LlamaEdge pakub GGUF-mudelite platvormidevahelist kättesaadavust.

## **Kvantiseeritud Mudelid:**
Paljud kasutajad eelistavad kasutada kvantiseeritud mudeleid kohaliku järelduse jaoks. Näiteks saate otse käivitada Ollama run Phi-3 või konfigureerida seda võrguühenduseta Modelfile'i abil. Modelfile määrab GGUF-faili tee ja viiteformaadi.

## **Generatiivse AI Võimalused:**
SLM-ide, nagu Phi-3-mini, kombineerimine avab uusi võimalusi generatiivse AI jaoks. Järeldus on vaid esimene samm; neid mudeleid saab kasutada erinevate ülesannete jaoks piiratud ressursside, viivituste ja kulude tingimustes.

## **Generatiivse AI Avamine Phi-3-mini abil: Juhend järelduse ja juurutamise kohta**
Õppige kasutama Semantic Kernelit, Ollama/LlamaEdge'i ja ONNX Runtime'i, et pääseda Phi-3-mini mudelitele ja teha järeldusi, ning uurige generatiivse AI võimalusi erinevates rakendustsenaariumides.

**Funktsioonid**
Phi-3-mini mudeli järeldus:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Kokkuvõttes võimaldab Phi-3-mini arendajatel uurida erinevaid mudeliformaate ja kasutada generatiivset AI-d mitmesugustes rakendustsenaariumides.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.