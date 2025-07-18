<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-07-16T22:11:04+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "ms"
}
-->
# **Pengkuantitian Keluarga Phi menggunakan llama.cpp**

## **Apa itu llama.cpp**

llama.cpp adalah perpustakaan perisian sumber terbuka yang ditulis terutamanya dalam C++ yang menjalankan inferens pada pelbagai Model Bahasa Besar (LLM), seperti Llama. Matlamat utamanya adalah untuk menyediakan prestasi terkini bagi inferens LLM merentasi pelbagai jenis perkakasan dengan persediaan yang minimum. Selain itu, terdapat juga sambungan Python untuk perpustakaan ini, yang menawarkan API tahap tinggi untuk pelengkap teks dan pelayan web yang serasi dengan OpenAI.

Matlamat utama llama.cpp adalah untuk membolehkan inferens LLM dengan persediaan minimum dan prestasi terkini pada pelbagai jenis perkakasan - secara tempatan dan di awan.

- Pelaksanaan C/C++ tulen tanpa sebarang kebergantungan
- Apple silicon diberi keutamaan - dioptimumkan melalui ARM NEON, Accelerate dan rangka kerja Metal
- Sokongan AVX, AVX2 dan AVX512 untuk seni bina x86
- Pengkuantitian integer 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, dan 8-bit untuk inferens lebih pantas dan penggunaan memori yang dikurangkan
- Kernel CUDA tersuai untuk menjalankan LLM pada GPU NVIDIA (sokongan untuk GPU AMD melalui HIP)
- Sokongan backend Vulkan dan SYCL
- Inferens hibrid CPU+GPU untuk mempercepatkan sebahagian model yang lebih besar daripada kapasiti VRAM keseluruhan

## **Pengkuantitian Phi-3.5 dengan llama.cpp**

Model Phi-3.5-Instruct boleh dikuantitikan menggunakan llama.cpp, tetapi Phi-3.5-Vision dan Phi-3.5-MoE belum disokong lagi. Format yang ditukar oleh llama.cpp adalah gguf, yang juga merupakan format pengkuantitian yang paling banyak digunakan.

Terdapat banyak model dalam format GGUF yang dikuantitikan di Hugging Face. AI Foundry, Ollama, dan LlamaEdge bergantung pada llama.cpp, jadi model GGUF juga sering digunakan.

### **Apa itu GGUF**

GGUF adalah format binari yang dioptimumkan untuk pemuatan dan penyimpanan model yang pantas, menjadikannya sangat cekap untuk tujuan inferens. GGUF direka untuk digunakan dengan GGML dan pelaksana lain. GGUF dibangunkan oleh @ggerganov yang juga merupakan pembangun llama.cpp, rangka kerja inferens LLM C/C++ yang popular. Model yang dibangunkan pada awalnya dalam rangka kerja seperti PyTorch boleh ditukar ke format GGUF untuk digunakan dengan enjin tersebut.

### **ONNX vs GGUF**

ONNX adalah format pembelajaran mesin/pembelajaran mendalam tradisional, yang disokong dengan baik dalam pelbagai Rangka Kerja AI dan mempunyai senario penggunaan yang baik pada peranti tepi. Manakala GGUF, ia berasaskan llama.cpp dan boleh dikatakan dihasilkan dalam era GenAI. Kedua-duanya mempunyai kegunaan yang serupa. Jika anda mahukan prestasi lebih baik pada perkakasan terbenam dan lapisan aplikasi, ONNX mungkin pilihan anda. Jika anda menggunakan rangka kerja dan teknologi terbitan dari llama.cpp, maka GGUF mungkin lebih sesuai.

### **Pengkuantitian Phi-3.5-Instruct menggunakan llama.cpp**

**1. Konfigurasi Persekitaran**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Pengkuantitian**

Menggunakan llama.cpp untuk menukar Phi-3.5-Instruct ke FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Pengkuantitian Phi-3.5 ke INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Ujian**

Pasang llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Nota*** 

Jika anda menggunakan Apple Silicon, sila pasang llama-cpp-python seperti berikut


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Ujian 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Sumber**

1. Ketahui lebih lanjut tentang llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. Ketahui lebih lanjut tentang onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. Ketahui lebih lanjut tentang GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.