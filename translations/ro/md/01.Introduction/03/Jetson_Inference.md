<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be4101a30d98e95a71d42c276e8bcd37",
  "translation_date": "2025-07-16T20:45:13+00:00",
  "source_file": "md/01.Introduction/03/Jetson_Inference.md",
  "language_code": "ro"
}
-->
# **Inferență Phi-3 pe Nvidia Jetson**

Nvidia Jetson este o serie de plăci de calcul încorporate de la Nvidia. Modelele Jetson TK1, TX1 și TX2 sunt echipate cu un procesor Tegra (sau SoC) de la Nvidia, care integrează o unitate centrală de procesare (CPU) cu arhitectură ARM. Jetson este un sistem cu consum redus de energie, conceput pentru accelerarea aplicațiilor de învățare automată. Nvidia Jetson este folosit de dezvoltatori profesioniști pentru a crea produse AI revoluționare în diverse industrii, dar și de studenți și pasionați pentru învățare practică în domeniul AI și realizarea unor proiecte impresionante. SLM este implementat pe dispozitive edge precum Jetson, ceea ce permite o aplicare mai bună a scenariilor industriale de AI generativ.

## Implementare pe NVIDIA Jetson:
Dezvoltatorii care lucrează la robotică autonomă și dispozitive încorporate pot folosi Phi-3 Mini. Dimensiunea relativ mică a lui Phi-3 îl face ideal pentru implementarea la marginea rețelei (edge). Parametrii au fost ajustați cu atenție în timpul antrenamentului, asigurând o acuratețe ridicată a răspunsurilor.

### Optimizarea TensorRT-LLM:
Biblioteca [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) de la NVIDIA optimizează inferența modelelor mari de limbaj. Aceasta suportă fereastra lungă de context a lui Phi-3 Mini, îmbunătățind atât debitul, cât și latența. Optimizările includ tehnici precum LongRoPE, FP8 și procesarea în loturi în zbor (inflight batching).

### Disponibilitate și implementare:
Dezvoltatorii pot explora Phi-3 Mini cu fereastra de context de 128K pe [NVIDIA AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/). Este oferit ca un NVIDIA NIM, un microserviciu cu API standard care poate fi implementat oriunde. În plus, [implementările TensorRT-LLM pe GitHub](https://github.com/NVIDIA/TensorRT-LLM).

## **1. Pregătire**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+

c. Cuda 11.8

d. Python 3.8+

## **2. Rularea Phi-3 pe Jetson**

Putem alege între [Ollama](https://ollama.com) sau [LlamaEdge](https://llamaedge.com)

Dacă dorești să folosești gguf atât în cloud, cât și pe dispozitive edge, LlamaEdge poate fi înțeles ca WasmEdge (WasmEdge este un runtime WebAssembly ușor, performant și scalabil, potrivit pentru aplicații cloud native, edge și descentralizate. Suportă aplicații serverless, funcții încorporate, microservicii, contracte inteligente și dispozitive IoT). Poți implementa modelul cantitativ gguf pe dispozitive edge și în cloud prin LlamaEdge.

![llamaedge](../../../../../translated_images/llamaedge.e9d6ff96dff11cf7.ro.jpg)

Pașii pentru utilizare:

1. Instalează și descarcă bibliotecile și fișierele necesare

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**Notă**: llama-api-server.wasm și chatbot-ui trebuie să fie în același director

2. Rulează scripturile în terminal

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

Iată rezultatul rulării

![llamaedgerun](../../../../../translated_images/llamaedgerun.bed921516c9a821c.ro.png)

***Cod exemplu*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

În concluzie, Phi-3 Mini reprezintă un salt înainte în modelarea limbajului, combinând eficiența, conștientizarea contextului și expertiza NVIDIA în optimizare. Indiferent dacă dezvolți roboți sau aplicații edge, Phi-3 Mini este un instrument puternic de luat în considerare.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.