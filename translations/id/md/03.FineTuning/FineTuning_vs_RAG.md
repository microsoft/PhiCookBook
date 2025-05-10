<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e010400c2918557b36bb932a14004c",
  "translation_date": "2025-05-09T22:16:34+00:00",
  "source_file": "md/03.FineTuning/FineTuning_vs_RAG.md",
  "language_code": "id"
}
-->
## Finetuning vs RAG

## Retrieval Augmented Generation

RAG adalah pengambilan data + pembuatan teks. Data terstruktur dan tidak terstruktur dari perusahaan disimpan dalam database vektor. Saat mencari konten yang relevan, ringkasan dan konten yang sesuai ditemukan untuk membentuk konteks, lalu kemampuan penyelesaian teks dari LLM/SLM digabungkan untuk menghasilkan konten.

## Proses RAG
![FinetuningvsRAG](../../../../translated_images/rag.36e7cb856f120334d577fde60c6a5d7c5eecae255dac387669303d30b4b3efa4.id.png)

## Fine-tuning
Fine-tuning didasarkan pada peningkatan suatu model tertentu. Tidak perlu memulai dari algoritma model, tapi data harus terus dikumpulkan. Jika Anda menginginkan terminologi dan ekspresi bahasa yang lebih tepat dalam aplikasi industri, fine-tuning adalah pilihan yang lebih baik. Namun jika data Anda sering berubah, fine-tuning bisa menjadi rumit.

## Cara memilih
Jika jawaban kita membutuhkan pengenalan data eksternal, RAG adalah pilihan terbaik.

Jika Anda perlu menghasilkan pengetahuan industri yang stabil dan tepat, fine-tuning akan menjadi pilihan yang baik. RAG mengutamakan pengambilan konten relevan tapi mungkin tidak selalu menangkap nuansa khusus.

Fine-tuning membutuhkan dataset berkualitas tinggi, dan jika hanya pada cakupan data kecil, tidak akan banyak berpengaruh. RAG lebih fleksibel.  
Fine-tuning adalah kotak hitam, sebuah metafisika, dan sulit memahami mekanisme internalnya. Namun RAG memudahkan menemukan sumber data, sehingga bisa secara efektif mengatur halusinasi atau kesalahan konten dan memberikan transparansi yang lebih baik.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.