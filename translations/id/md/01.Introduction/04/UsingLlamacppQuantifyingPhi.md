# **Mengkuantisasi Keluarga Phi menggunakan llama.cpp**

## **Apa itu llama.cpp**

llama.cpp adalah perpustakaan perangkat lunak open-source yang terutama ditulis dalam C++ yang melakukan inferensi pada berbagai Large Language Models (LLM), seperti Llama. Tujuan utamanya adalah menyediakan performa terbaik untuk inferensi LLM di berbagai perangkat keras dengan pengaturan yang minimal. Selain itu, tersedia juga binding Python untuk perpustakaan ini, yang menawarkan API tingkat tinggi untuk penyelesaian teks dan server web yang kompatibel dengan OpenAI.

Tujuan utama llama.cpp adalah memungkinkan inferensi LLM dengan pengaturan minimal dan performa terbaik di berbagai perangkat keras - baik secara lokal maupun di cloud.

- Implementasi murni C/C++ tanpa ketergantungan apapun
- Apple silicon didukung secara penuh - dioptimalkan melalui ARM NEON, Accelerate, dan framework Metal
- Dukungan AVX, AVX2, dan AVX512 untuk arsitektur x86
- Kuantisasi integer 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, dan 8-bit untuk inferensi lebih cepat dan penggunaan memori yang lebih rendah
- Kernel CUDA khusus untuk menjalankan LLM di GPU NVIDIA (dukungan untuk GPU AMD melalui HIP)
- Dukungan backend Vulkan dan SYCL
- Inferensi hybrid CPU+GPU untuk mempercepat sebagian model yang lebih besar dari kapasitas total VRAM

## **Mengkuantisasi Phi-3.5 dengan llama.cpp**

Model Phi-3.5-Instruct dapat dikuantisasi menggunakan llama.cpp, namun Phi-3.5-Vision dan Phi-3.5-MoE belum didukung. Format yang dikonversi oleh llama.cpp adalah gguf, yang juga merupakan format kuantisasi yang paling banyak digunakan.

Terdapat banyak model dalam format GGUF yang sudah dikuantisasi di Hugging Face. AI Foundry, Ollama, dan LlamaEdge mengandalkan llama.cpp, sehingga model GGUF juga sering digunakan.

### **Apa itu GGUF**

GGUF adalah format biner yang dioptimalkan untuk pemuatan dan penyimpanan model yang cepat, sehingga sangat efisien untuk keperluan inferensi. GGUF dirancang untuk digunakan dengan GGML dan eksekutor lainnya. GGUF dikembangkan oleh @ggerganov yang juga merupakan pengembang llama.cpp, sebuah framework inferensi LLM populer berbasis C/C++. Model yang awalnya dikembangkan di framework seperti PyTorch dapat dikonversi ke format GGUF untuk digunakan dengan engine tersebut.

### **ONNX vs GGUF**

ONNX adalah format machine learning/deep learning tradisional, yang didukung dengan baik di berbagai Framework AI dan memiliki skenario penggunaan yang baik di perangkat edge. Sedangkan GGUF berbasis pada llama.cpp dan bisa dikatakan diproduksi di era GenAI. Keduanya memiliki kegunaan yang mirip. Jika Anda menginginkan performa lebih baik di perangkat keras embedded dan lapisan aplikasi, ONNX mungkin pilihan Anda. Jika Anda menggunakan framework turunan dan teknologi dari llama.cpp, maka GGUF bisa jadi lebih baik.

### **Kuantisasi Phi-3.5-Instruct menggunakan llama.cpp**

**1. Konfigurasi Lingkungan**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kuantisasi**

Menggunakan llama.cpp untuk mengonversi Phi-3.5-Instruct ke FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Mengkuantisasi Phi-3.5 ke INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Pengujian**

Pasang llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Catatan*** 

Jika Anda menggunakan Apple Silicon, silakan pasang llama-cpp-python seperti ini


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Pengujian 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Sumber Daya**

1. Pelajari lebih lanjut tentang llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)  
2. Pelajari lebih lanjut tentang onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  
3. Pelajari lebih lanjut tentang GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.