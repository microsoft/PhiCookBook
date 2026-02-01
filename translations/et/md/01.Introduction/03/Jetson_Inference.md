# **Inference Phi-3 Nvidia Jetsonil**

Nvidia Jetson on Nvidia loodud manussüsteemide arvutiplatvormide seeria. Jetson TK1, TX1 ja TX2 mudelid sisaldavad Nvidia Tegra protsessorit (või SoC), mis integreerib ARM-arhitektuuriga keskprotsessori (CPU). Jetson on madala energiatarbega süsteem, mis on loodud masinõppe rakenduste kiirendamiseks. Nvidia Jetsonit kasutavad professionaalsed arendajad, et luua murrangulisi tehisintellekti tooteid kõikides tööstusharudes, samuti õpilased ja entusiastid praktiliseks tehisintellekti õppimiseks ja hämmastavate projektide loomiseks. SLM-i kasutatakse servaseadmetes, nagu Jetson, mis võimaldab tööstuslike generatiivse tehisintellekti rakenduste paremat teostamist.

## Juurutamine NVIDIA Jetsonil:
Arendajad, kes töötavad autonoomsete robotite ja manusseadmetega, saavad kasutada Phi-3 Mini. Phi-3 väike suurus muudab selle ideaalseks servaseadmetes kasutamiseks. Parameetrid on treeningu käigus hoolikalt häälestatud, tagades vastuste kõrge täpsuse.

### TensorRT-LLM optimeerimine:
NVIDIA [TensorRT-LLM teek](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) optimeerib suurte keelemudelite järeldusi. See toetab Phi-3 Mini pikka kontekstakent, parandades nii läbilaskevõimet kui ka latentsust. Optimeerimiste hulka kuuluvad sellised tehnikad nagu LongRoPE, FP8 ja inflight batching.

### Saadavus ja juurutamine:
Arendajad saavad uurida Phi-3 Mini võimalusi 128K kontekstakna abil [NVIDIA AI lehel](https://www.nvidia.com/en-us/ai-data-science/generative-ai/). See on pakendatud NVIDIA NIM-ina, mis on standardse API-ga mikroteenus ja mida saab juurutada kõikjal. Lisaks on saadaval [TensorRT-LLM implementatsioonid GitHubis](https://github.com/NVIDIA/TensorRT-LLM).

## **1. Ettevalmistus**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+
   
c. Cuda 11.8
   
d. Python 3.8+

## **2. Phi-3 käivitamine Jetsonil**

Me saame valida [Ollama](https://ollama.com) või [LlamaEdge](https://llamaedge.com)

Kui soovite kasutada gguf-i nii pilves kui ka servaseadmetes, võib LlamaEdge'i mõista kui WasmEdge'i (WasmEdge on kerge, suure jõudlusega ja skaleeritav WebAssembly käituskeskkond, mis sobib pilvepõhiste, serva- ja detsentraliseeritud rakenduste jaoks. See toetab serverivabasid rakendusi, manustatud funktsioone, mikroteenuseid, nutilepinguid ja IoT-seadmeid. Saate juurutada gguf-i kvantitatiivse mudeli servaseadmetesse ja pilve LlamaEdge'i kaudu.

![llamaedge](../../../../../imgs/01/03/Jetson/llamaedge.jpg)

Siin on sammud kasutamiseks:

1. Installige ja laadige alla seotud teegid ja failid

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**Märkus**: llama-api-server.wasm ja chatbot-ui peavad olema samas kaustas

2. Käivitage skriptid terminalis

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

Siin on käivitamise tulemus:

![llamaedgerun](../../../../../imgs/01/03/Jetson/llamaedgerun.png)

***Näidiskood*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

Kokkuvõttes esindab Phi-3 Mini suurt edasiminekut keelemudelite vallas, ühendades tõhususe, kontekstitundlikkuse ja NVIDIA optimeerimisvõimekuse. Olenemata sellest, kas ehitate roboteid või servarakendusi, on Phi-3 Mini võimas tööriist, mida tasub teada.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.