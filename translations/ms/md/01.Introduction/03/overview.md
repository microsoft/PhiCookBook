Dalam konteks Phi-3-mini, inferens merujuk kepada proses menggunakan model untuk membuat ramalan atau menghasilkan output berdasarkan data input. Izinkan saya memberikan lebih banyak maklumat tentang Phi-3-mini dan keupayaan inferensnya.

Phi-3-mini adalah sebahagian daripada siri model Phi-3 yang dikeluarkan oleh Microsoft. Model-model ini direka untuk mentakrif semula apa yang mungkin dengan Model Bahasa Kecil (SLM).

Berikut adalah beberapa perkara penting mengenai Phi-3-mini dan keupayaan inferensnya:

## **Gambaran Keseluruhan Phi-3-mini:**
- Phi-3-mini mempunyai saiz parameter sebanyak 3.8 bilion.
- Ia boleh dijalankan bukan sahaja pada peranti pengkomputeran tradisional tetapi juga pada peranti edge seperti peranti mudah alih dan peranti IoT.
- Pelepasan Phi-3-mini membolehkan individu dan perusahaan menggunakan SLM pada pelbagai peranti perkakasan, terutamanya dalam persekitaran yang terhad sumber.
- Ia merangkumi pelbagai format model, termasuk format PyTorch tradisional, versi kuantisasi format gguf, dan versi kuantisasi berasaskan ONNX.

## **Mengakses Phi-3-mini:**
Untuk mengakses Phi-3-mini, anda boleh menggunakan [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) dalam aplikasi Copilot. Semantic Kernel secara amnya serasi dengan Azure OpenAI Service, model sumber terbuka di Hugging Face, dan model tempatan.  
Anda juga boleh menggunakan [Ollama](https://ollama.com) atau [LlamaEdge](https://llamaedge.com) untuk memanggil model kuantisasi. Ollama membolehkan pengguna individu memanggil pelbagai model kuantisasi, manakala LlamaEdge menyediakan ketersediaan merentas platform untuk model GGUF.

## **Model Kuantisasi:**
Ramai pengguna lebih suka menggunakan model kuantisasi untuk inferens tempatan. Contohnya, anda boleh terus menjalankan Ollama run Phi-3 atau mengkonfigurasikannya secara luar talian menggunakan Modelfile. Modelfile menentukan laluan fail GGUF dan format prompt.

## **Kemungkinan AI Generatif:**
Menggabungkan SLM seperti Phi-3-mini membuka peluang baru untuk AI generatif. Inferens hanyalah langkah pertama; model-model ini boleh digunakan untuk pelbagai tugasan dalam senario yang terhad sumber, terikat latensi, dan terhad kos.

## **Membuka Potensi AI Generatif dengan Phi-3-mini: Panduan untuk Inferens dan Penyebaran**  
Pelajari cara menggunakan Semantic Kernel, Ollama/LlamaEdge, dan ONNX Runtime untuk mengakses dan melakukan inferens model Phi-3-mini, serta terokai kemungkinan AI generatif dalam pelbagai senario aplikasi.

**Ciri-ciri**  
Inferens model phi3-mini dalam:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

Secara ringkas, Phi-3-mini membolehkan pembangun meneroka pelbagai format model dan memanfaatkan AI generatif dalam pelbagai senario aplikasi.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.