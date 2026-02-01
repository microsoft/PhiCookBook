# **Inference Phi-3 di Nvidia Jetson**

Nvidia Jetson adalah rangkaian papan komputasi embedded dari Nvidia. Model Jetson TK1, TX1, dan TX2 semuanya menggunakan prosesor Tegra (atau SoC) dari Nvidia yang mengintegrasikan unit pemrosesan pusat (CPU) dengan arsitektur ARM. Jetson adalah sistem berdaya rendah yang dirancang untuk mempercepat aplikasi pembelajaran mesin. Nvidia Jetson digunakan oleh pengembang profesional untuk menciptakan produk AI terobosan di berbagai industri, serta oleh pelajar dan penggemar untuk pembelajaran AI secara langsung dan membuat proyek-proyek menakjubkan. SLM diterapkan pada perangkat edge seperti Jetson, yang memungkinkan implementasi skenario aplikasi AI generatif industri yang lebih baik.

## Deployment di NVIDIA Jetson:
Pengembang yang bekerja pada robotika otonom dan perangkat embedded dapat memanfaatkan Phi-3 Mini. Ukuran Phi-3 yang relatif kecil membuatnya ideal untuk deployment di edge. Parameter telah disetel dengan cermat selama pelatihan, memastikan akurasi tinggi dalam respons.

### Optimasi TensorRT-LLM:
[TensorRT-LLM library](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) dari NVIDIA mengoptimalkan inferensi model bahasa besar. Library ini mendukung jendela konteks panjang Phi-3 Mini, meningkatkan throughput dan latensi. Optimasi mencakup teknik seperti LongRoPE, FP8, dan inflight batching.

### Ketersediaan dan Deployment:
Pengembang dapat mengeksplorasi Phi-3 Mini dengan jendela konteks 128K di [NVIDIA's AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/). Phi-3 Mini dikemas sebagai NVIDIA NIM, sebuah microservice dengan API standar yang dapat dideploy di mana saja. Selain itu, ada [implementasi TensorRT-LLM di GitHub](https://github.com/NVIDIA/TensorRT-LLM).

## **1. Persiapan**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+

c. Cuda 11.8

d. Python 3.8+

## **2. Menjalankan Phi-3 di Jetson**

Kita bisa memilih [Ollama](https://ollama.com) atau [LlamaEdge](https://llamaedge.com)

Jika ingin menggunakan gguf di cloud dan perangkat edge secara bersamaan, LlamaEdge bisa dipahami sebagai WasmEdge (WasmEdge adalah runtime WebAssembly yang ringan, berperforma tinggi, dan skalabel, cocok untuk aplikasi cloud native, edge, dan terdesentralisasi. Mendukung aplikasi serverless, fungsi embedded, microservices, smart contracts, dan perangkat IoT). Anda dapat mendepoy model kuantitatif gguf ke perangkat edge dan cloud melalui LlamaEdge.

![llamaedge](../../../../../translated_images/id/llamaedge.e9d6ff96dff11cf7.webp)

Berikut langkah-langkah penggunaannya

1. Instal dan unduh pustaka serta file terkait

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**Catatan**: llama-api-server.wasm dan chatbot-ui harus berada di direktori yang sama

2. Jalankan skrip di terminal

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

Berikut hasil jalannya

![llamaedgerun](../../../../../translated_images/id/llamaedgerun.bed921516c9a821c.webp)

***Kode contoh*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

Singkatnya, Phi-3 Mini merupakan lompatan maju dalam pemodelan bahasa, menggabungkan efisiensi, kesadaran konteks, dan keunggulan optimasi dari NVIDIA. Baik Anda membangun robot atau aplikasi edge, Phi-3 Mini adalah alat yang sangat berguna untuk diketahui.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.