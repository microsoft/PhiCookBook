# **Inference Phi-3 di Android**

Mari kita jelajahi bagaimana Anda dapat melakukan inference dengan Phi-3-mini di perangkat Android. Phi-3-mini adalah seri model baru dari Microsoft yang memungkinkan penerapan Large Language Models (LLM) pada perangkat edge dan perangkat IoT.

## Semantic Kernel dan Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) adalah kerangka aplikasi yang memungkinkan Anda membuat aplikasi yang kompatibel dengan Azure OpenAI Service, model OpenAI, dan bahkan model lokal. Jika Anda baru mengenal Semantic Kernel, kami sarankan untuk melihat [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Mengakses Phi-3-mini Menggunakan Semantic Kernel

Anda dapat menggabungkannya dengan Hugging Face Connector di Semantic Kernel. Lihat [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Secara default, ini mengacu pada model ID di Hugging Face. Namun, Anda juga bisa terhubung ke server model Phi-3-mini yang dibangun secara lokal.

### Memanggil Model Kuantisasi dengan Ollama atau LlamaEdge

Banyak pengguna lebih memilih menggunakan model kuantisasi untuk menjalankan model secara lokal. [Ollama](https://ollama.com/) dan [LlamaEdge](https://llamaedge.com) memungkinkan pengguna individu memanggil berbagai model kuantisasi:

#### Ollama

Anda bisa langsung menjalankan `ollama run Phi-3` atau mengonfigurasinya secara offline dengan membuat `Modelfile` yang berisi path ke file `.gguf` Anda.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Jika Anda ingin menggunakan file `.gguf` di cloud dan perangkat edge secara bersamaan, LlamaEdge adalah pilihan yang tepat. Anda bisa merujuk ke [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) ini untuk memulai.

### Instal dan Jalankan di Ponsel Android

1. **Unduh aplikasi MLC Chat** (Gratis) untuk ponsel Android.  
2. Unduh file APK (148MB) dan pasang di perangkat Anda.  
3. Buka aplikasi MLC Chat. Anda akan melihat daftar model AI, termasuk Phi-3-mini.

Singkatnya, Phi-3-mini membuka peluang menarik untuk AI generatif di perangkat edge, dan Anda bisa mulai mengeksplorasi kemampuannya di Android.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.