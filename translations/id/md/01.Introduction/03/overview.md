<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-09T12:29:20+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "id"
}
-->
Dalam konteks Phi-3-mini, inference mengacu pada proses menggunakan model untuk membuat prediksi atau menghasilkan output berdasarkan data input. Izinkan saya memberikan lebih banyak detail tentang Phi-3-mini dan kemampuan inference-nya.

Phi-3-mini adalah bagian dari seri model Phi-3 yang dirilis oleh Microsoft. Model-model ini dirancang untuk mendefinisikan ulang apa yang mungkin dilakukan dengan Small Language Models (SLM).

Berikut beberapa poin penting tentang Phi-3-mini dan kemampuan inference-nya:

## **Ikhtisar Phi-3-mini:**
- Phi-3-mini memiliki ukuran parameter sebesar 3,8 miliar.
- Model ini dapat dijalankan tidak hanya pada perangkat komputasi tradisional tetapi juga pada perangkat edge seperti perangkat mobile dan perangkat IoT.
- Peluncuran Phi-3-mini memungkinkan individu dan perusahaan untuk menerapkan SLM pada berbagai perangkat keras, terutama di lingkungan dengan sumber daya terbatas.
- Model ini mendukung berbagai format model, termasuk format PyTorch tradisional, versi terkuantisasi dari format gguf, dan versi terkuantisasi berbasis ONNX.

## **Mengakses Phi-3-mini:**
Untuk mengakses Phi-3-mini, Anda dapat menggunakan [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) dalam aplikasi Copilot. Semantic Kernel umumnya kompatibel dengan Azure OpenAI Service, model open-source di Hugging Face, dan model lokal.
Anda juga dapat menggunakan [Ollama](https://ollama.com) atau [LlamaEdge](https://llamaedge.com) untuk memanggil model terkuantisasi. Ollama memungkinkan pengguna individu memanggil berbagai model terkuantisasi, sementara LlamaEdge menyediakan ketersediaan lintas platform untuk model GGUF.

## **Model Terkuantisasi:**
Banyak pengguna lebih memilih menggunakan model terkuantisasi untuk inference lokal. Misalnya, Anda dapat langsung menjalankan Ollama run Phi-3 atau mengonfigurasinya secara offline menggunakan Modelfile. Modelfile menentukan jalur file GGUF dan format prompt.

## **Kemungkinan Generative AI:**
Menggabungkan SLM seperti Phi-3-mini membuka kemungkinan baru untuk generative AI. Inference hanyalah langkah pertama; model-model ini dapat digunakan untuk berbagai tugas dalam skenario dengan sumber daya terbatas, keterbatasan latensi, dan pembatasan biaya.

## **Membuka Potensi Generative AI dengan Phi-3-mini: Panduan Inference dan Deployment**  
Pelajari cara menggunakan Semantic Kernel, Ollama/LlamaEdge, dan ONNX Runtime untuk mengakses dan melakukan inference pada model Phi-3-mini, serta jelajahi kemungkinan generative AI dalam berbagai skenario aplikasi.

**Fitur**  
Inference model phi3-mini di:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Singkatnya, Phi-3-mini memungkinkan pengembang untuk mengeksplorasi berbagai format model dan memanfaatkan generative AI dalam berbagai skenario aplikasi.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.