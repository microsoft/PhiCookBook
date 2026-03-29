# **Menggunakan Microsoft Foundry untuk evaluasi**

![aistudo](../../../../../translated_images/id/AIFoundry.9e0b513e999a1c5a.webp)

Cara mengevaluasi aplikasi AI generatif Anda menggunakan [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Baik Anda sedang menilai percakapan sekali putar atau multi putar, Microsoft Foundry menyediakan alat untuk mengevaluasi kinerja dan keamanan model.

![aistudo](../../../../../translated_images/id/AIPortfolio.69da59a8e1eaa70f.webp)

## Cara mengevaluasi aplikasi AI generatif dengan Microsoft Foundry
Untuk instruksi lebih detail, lihat [Dokumentasi Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Berikut adalah langkah-langkah untuk memulai:

## Mengevaluasi Model AI Generatif di Microsoft Foundry

**Prasyarat**

- Dataset pengujian dalam format CSV atau JSON.
- Model AI generatif yang sudah dideploy (seperti Phi-3, GPT 3.5, GPT 4, atau model Davinci).
- Runtime dengan instance komputasi untuk menjalankan evaluasi.

## Metode Evaluasi Bawaan

Microsoft Foundry memungkinkan Anda mengevaluasi percakapan sekali putar maupun percakapan kompleks multi putar.
Untuk skenario Retrieval Augmented Generation (RAG), di mana model didasarkan pada data tertentu, Anda dapat menilai kinerja menggunakan metrik evaluasi bawaan.
Selain itu, Anda dapat mengevaluasi skenario penjawaban pertanyaan sekali putar secara umum (non-RAG).

## Membuat Evaluasi Run

Dari UI Microsoft Foundry, navigasikan ke halaman Evaluate atau halaman Prompt Flow.
Ikuti wizard pembuatan evaluasi untuk mengatur evaluasi run. Berikan nama opsional untuk evaluasi Anda.
Pilih skenario yang sesuai dengan tujuan aplikasi Anda.
Pilih satu atau lebih metrik evaluasi untuk menilai keluaran model.

## Alur Evaluasi Kustom (Opsional)

Untuk fleksibilitas lebih besar, Anda dapat membuat alur evaluasi kustom. Sesuaikan proses evaluasi berdasarkan kebutuhan spesifik Anda.

## Melihat Hasil

Setelah menjalankan evaluasi, catat, lihat, dan analisis metrik evaluasi secara mendetail di Microsoft Foundry. Dapatkan wawasan tentang kemampuan dan keterbatasan aplikasi Anda.

**Note** Microsoft Foundry saat ini masih dalam tahap preview publik, jadi gunakan untuk eksperimen dan pengembangan saja. Untuk beban kerja produksi, pertimbangkan opsi lain. Jelajahi [dokumentasi AI Foundry resmi](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) untuk informasi lebih lengkap dan instruksi langkah demi langkah.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, mohon diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->