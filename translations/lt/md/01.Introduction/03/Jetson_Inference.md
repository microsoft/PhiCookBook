# **Inference Phi-3 Nvidia Jetson įrenginiuose**

Nvidia Jetson – tai Nvidia sukurtų įterptinių kompiuterių plokščių serija. Jetson TK1, TX1 ir TX2 modeliai turi Tegra procesorių (arba SoC) iš Nvidia, kuris integruoja ARM architektūros centrinį procesorių (CPU). Jetson yra mažos energijos sistemos, sukurtos mašininio mokymosi programų spartinimui. Nvidia Jetson naudojamas profesionalių kūrėjų, siekiančių kurti pažangius dirbtinio intelekto produktus įvairiose pramonės šakose, taip pat studentų ir entuziastų, norinčių praktiškai mokytis dirbtinio intelekto ir kurti įspūdingus projektus. SLM diegiamas kraštiniuose įrenginiuose, tokiuose kaip Jetson, siekiant geresnio pramoninių generatyvinio dirbtinio intelekto taikymo scenarijų įgyvendinimo.

## Diegimas NVIDIA Jetson įrenginiuose:
Kūrėjai, dirbantys su autonominiais robotais ir įterptiniais įrenginiais, gali pasinaudoti Phi-3 Mini. Phi-3 kompaktiškas dydis daro jį idealiu kraštiniam diegimui. Parametrai buvo kruopščiai sureguliuoti mokymo metu, užtikrinant aukštą atsakymų tikslumą.

### TensorRT-LLM optimizavimas:
NVIDIA [TensorRT-LLM biblioteka](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) optimizuoja didelių kalbos modelių inferenciją. Ji palaiko Phi-3 Mini ilgą konteksto langą, gerindama tiek pralaidumą, tiek vėlinimą. Optimizavimas apima tokias technikas kaip LongRoPE, FP8 ir užklausų grupavimas realiu laiku.

### Prieinamumas ir diegimas:
Kūrėjai gali išbandyti Phi-3 Mini su 128K konteksto langu [NVIDIA AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/) platformoje. Jis pateikiamas kaip NVIDIA NIM – mikroservisas su standartiniu API, kurį galima diegti bet kur. Be to, [TensorRT-LLM įgyvendinimai GitHub](https://github.com/NVIDIA/TensorRT-LLM).

## **1. Paruošimas**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+
   
c. Cuda 11.8
   
d. Python 3.8+

## **2. Phi-3 paleidimas Jetson įrenginiuose**

Galime pasirinkti [Ollama](https://ollama.com) arba [LlamaEdge](https://llamaedge.com).

Jei norite naudoti gguf debesyje ir kraštiniuose įrenginiuose tuo pačiu metu, LlamaEdge galima suprasti kaip WasmEdge (WasmEdge yra lengvas, aukštos kokybės, skalabilus WebAssembly vykdymo aplinka, tinkama debesų, kraštinių ir decentralizuotų programų kūrimui. Ji palaiko serverless programas, įterptines funkcijas, mikroservisus, išmaniąsias sutartis ir IoT įrenginius. Naudodami LlamaEdge galite diegti gguf kiekybinį modelį kraštiniuose įrenginiuose ir debesyje.

![llamaedge](../../../../../imgs/01/03/Jetson/llamaedge.jpg)

Štai žingsniai, kaip naudotis:

1. Įdiekite ir atsisiųskite susijusias bibliotekas ir failus

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**Pastaba**: llama-api-server.wasm ir chatbot-ui turi būti toje pačioje direktorijoje.

2. Paleiskite skriptus terminale

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

Štai paleidimo rezultatas:

![llamaedgerun](../../../../../imgs/01/03/Jetson/llamaedgerun.png)

***Pavyzdinis kodas*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

Apibendrinant, Phi-3 Mini yra reikšmingas žingsnis į priekį kalbos modeliavime, derinant efektyvumą, konteksto suvokimą ir NVIDIA optimizavimo pranašumus. Nesvarbu, ar kuriate robotus, ar kraštines programas, Phi-3 Mini yra galingas įrankis, kurį verta žinoti.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.