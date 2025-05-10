<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7b4235159486df4000e16b7b46ddfec3",
  "translation_date": "2025-05-09T15:01:22+00:00",
  "source_file": "md/01.Introduction/05/AIFoundry.md",
  "language_code": "id"
}
-->
# **Menggunakan Azure AI Foundry untuk evaluasi**

![aistudo](../../../../../translated_images/AIFoundry.61da8c74bccc0241ce9a4cb53a170912245871de9235043afcb796ccbc076fdc.id.png)

Cara mengevaluasi aplikasi AI generatif Anda menggunakan [Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Baik Anda menilai percakapan satu putaran atau multi putaran, Azure AI Foundry menyediakan alat untuk mengevaluasi kinerja dan keamanan model.

![aistudo](../../../../../translated_images/AIPortfolio.5aaa2b25e9157624a4542fe041d66a96a1c1ec6007e4e5aadd926c6ec8ce18b3.id.png)

## Cara mengevaluasi aplikasi AI generatif dengan Azure AI Foundry
Untuk instruksi lebih lengkap, lihat [Dokumentasi Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Berikut langkah-langkah untuk memulai:

## Mengevaluasi Model AI Generatif di Azure AI Foundry

**Prasyarat**

- Dataset uji dalam format CSV atau JSON.
- Model AI generatif yang sudah diterapkan (seperti Phi-3, GPT 3.5, GPT 4, atau model Davinci).
- Runtime dengan instance komputasi untuk menjalankan evaluasi.

## Metrik Evaluasi Bawaan

Azure AI Foundry memungkinkan Anda mengevaluasi percakapan satu putaran maupun percakapan kompleks multi putaran.  
Untuk skenario Retrieval Augmented Generation (RAG), di mana model didasarkan pada data tertentu, Anda dapat menilai kinerja menggunakan metrik evaluasi bawaan.  
Selain itu, Anda juga dapat mengevaluasi skenario tanya jawab satu putaran secara umum (non-RAG).

## Membuat Evaluasi Run

Dari UI Azure AI Foundry, buka halaman Evaluate atau halaman Prompt Flow.  
Ikuti wizard pembuatan evaluasi untuk mengatur evaluasi run. Berikan nama opsional untuk evaluasi Anda.  
Pilih skenario yang sesuai dengan tujuan aplikasi Anda.  
Pilih satu atau lebih metrik evaluasi untuk menilai keluaran model.

## Alur Evaluasi Kustom (Opsional)

Untuk fleksibilitas lebih, Anda dapat membuat alur evaluasi kustom. Sesuaikan proses evaluasi sesuai kebutuhan spesifik Anda.

## Melihat Hasil

Setelah menjalankan evaluasi, catat, lihat, dan analisis metrik evaluasi secara rinci di Azure AI Foundry. Dapatkan wawasan tentang kemampuan dan keterbatasan aplikasi Anda.

**Note** Azure AI Foundry saat ini dalam versi pratinjau publik, jadi gunakan untuk eksperimen dan pengembangan. Untuk beban kerja produksi, pertimbangkan opsi lain. Jelajahi dokumentasi resmi [AI Foundry](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) untuk informasi lebih lanjut dan panduan langkah demi langkah.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi yang sangat penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.