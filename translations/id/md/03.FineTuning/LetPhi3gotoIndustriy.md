<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "743d7e9cb9c4e8ea642d77bee657a7fa",
  "translation_date": "2025-07-17T09:59:05+00:00",
  "source_file": "md/03.FineTuning/LetPhi3gotoIndustriy.md",
  "language_code": "id"
}
-->
# **Biarkan Phi-3 menjadi ahli industri**

Untuk menerapkan model Phi-3 ke dalam sebuah industri, Anda perlu menambahkan data bisnis industri ke model Phi-3. Kami memiliki dua opsi berbeda, yang pertama adalah RAG (Retrieval Augmented Generation) dan yang kedua adalah Fine Tuning.

## **RAG vs Fine-Tuning**

### **Retrieval Augmented Generation**

RAG adalah pengambilan data + pembuatan teks. Data terstruktur dan tidak terstruktur dari perusahaan disimpan dalam database vektor. Saat mencari konten yang relevan, ringkasan dan konten yang relevan ditemukan untuk membentuk konteks, dan kemampuan penyelesaian teks dari LLM/SLM digabungkan untuk menghasilkan konten.

### **Fine-tuning**

Fine-tuning adalah peningkatan dari model tertentu. Ini tidak perlu dimulai dari algoritma model, tetapi data perlu terus dikumpulkan. Jika Anda menginginkan terminologi dan ekspresi bahasa yang lebih tepat dalam aplikasi industri, fine-tuning adalah pilihan yang lebih baik. Namun jika data Anda sering berubah, fine-tuning bisa menjadi rumit.

### **Cara memilih**

1. Jika jawaban kita memerlukan pengenalan data eksternal, RAG adalah pilihan terbaik

2. Jika Anda perlu menghasilkan pengetahuan industri yang stabil dan tepat, fine-tuning akan menjadi pilihan yang baik. RAG mengutamakan menarik konten relevan tetapi mungkin tidak selalu menangkap nuansa khusus secara tepat.

3. Fine-tuning membutuhkan dataset berkualitas tinggi, dan jika hanya data dalam cakupan kecil, perbedaannya tidak akan signifikan. RAG lebih fleksibel

4. Fine-tuning adalah kotak hitam, sebuah metafisika, dan sulit untuk memahami mekanisme internalnya. Namun RAG dapat memudahkan menemukan sumber data, sehingga secara efektif mengatur halusinasi atau kesalahan konten dan memberikan transparansi yang lebih baik.

### **Skenario**

1. Industri vertikal yang membutuhkan kosakata dan ekspresi profesional khusus, ***Fine-tuning*** adalah pilihan terbaik

2. Sistem QA, yang melibatkan sintesis berbagai titik pengetahuan, ***RAG*** adalah pilihan terbaik

3. Kombinasi alur bisnis otomatis ***RAG + Fine-tuning*** adalah pilihan terbaik

## **Cara menggunakan RAG**

![rag](../../../../translated_images/id/rag.2014adc59e6f6007.png)

Database vektor adalah kumpulan data yang disimpan dalam bentuk matematis. Database vektor memudahkan model pembelajaran mesin untuk mengingat input sebelumnya, memungkinkan pembelajaran mesin digunakan untuk mendukung kasus penggunaan seperti pencarian, rekomendasi, dan pembuatan teks. Data dapat diidentifikasi berdasarkan metrik kesamaan, bukan kecocokan tepat, sehingga model komputer dapat memahami konteks data.

Database vektor adalah kunci untuk mewujudkan RAG. Kita dapat mengubah data menjadi penyimpanan vektor melalui model vektor seperti text-embedding-3, jina-ai-embedding, dan lain-lain.

Pelajari lebih lanjut tentang membuat aplikasi RAG di [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo)

## **Cara menggunakan Fine-tuning**

Algoritma yang umum digunakan dalam Fine-tuning adalah Lora dan QLora. Bagaimana cara memilih?
- [Pelajari lebih lanjut dengan notebook contoh ini](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Contoh Python FineTuning Sample](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora dan QLora**

![lora](../../../../translated_images/id/qlora.e6446c988ee04ca0.png)

LoRA (Low-Rank Adaptation) dan QLoRA (Quantized Low-Rank Adaptation) adalah teknik yang digunakan untuk fine-tuning model bahasa besar (LLM) menggunakan Parameter Efficient Fine Tuning (PEFT). Teknik PEFT dirancang untuk melatih model lebih efisien dibandingkan metode tradisional.  
LoRA adalah teknik fine-tuning mandiri yang mengurangi penggunaan memori dengan menerapkan aproksimasi low-rank pada matriks pembaruan bobot. Ini menawarkan waktu pelatihan yang cepat dan mempertahankan performa yang mendekati metode fine-tuning tradisional.

QLoRA adalah versi pengembangan dari LoRA yang menggabungkan teknik kuantisasi untuk mengurangi penggunaan memori lebih jauh. QLoRA mengkuantisasi presisi parameter bobot dalam LLM yang sudah dilatih sebelumnya menjadi presisi 4-bit, yang lebih efisien memori dibandingkan LoRA. Namun, pelatihan QLoRA sekitar 30% lebih lambat daripada pelatihan LoRA karena adanya langkah kuantisasi dan dekuantisasi tambahan.

QLoRA menggunakan LoRA sebagai pelengkap untuk memperbaiki kesalahan yang muncul selama proses kuantisasi. QLoRA memungkinkan fine-tuning model besar dengan miliaran parameter pada GPU yang relatif kecil dan mudah didapat. Misalnya, QLoRA dapat melakukan fine-tuning model 70B parameter yang biasanya membutuhkan 36 GPU hanya dengan 2 GPU.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.