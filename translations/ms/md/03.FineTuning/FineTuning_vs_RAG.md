<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e010400c2918557b36bb932a14004c",
  "translation_date": "2025-07-17T09:30:38+00:00",
  "source_file": "md/03.FineTuning/FineTuning_vs_RAG.md",
  "language_code": "ms"
}
-->
## Penalaan Halus vs RAG

## Penjanaan Dipertingkatkan dengan Pengambilan (RAG)

RAG adalah gabungan pengambilan data + penjanaan teks. Data berstruktur dan tidak berstruktur dalam perusahaan disimpan dalam pangkalan data vektor. Apabila mencari kandungan yang relevan, ringkasan dan kandungan yang berkaitan akan ditemui untuk membentuk konteks, dan keupayaan pelengkap teks LLM/SLM digabungkan untuk menghasilkan kandungan.

## Proses RAG
![FinetuningvsRAG](../../../../translated_images/ms/rag.2014adc59e6f6007.png)

## Penalaan Halus
Penalaan halus adalah berdasarkan penambahbaikan model tertentu. Ia tidak perlu bermula dengan algoritma model, tetapi data perlu dikumpul secara berterusan. Jika anda mahukan istilah dan ungkapan bahasa yang lebih tepat dalam aplikasi industri, penalaan halus adalah pilihan yang lebih baik. Tetapi jika data anda kerap berubah, penalaan halus boleh menjadi rumit.

## Cara Memilih
Jika jawapan kita memerlukan pengenalan data luaran, RAG adalah pilihan terbaik

Jika anda perlu menghasilkan pengetahuan industri yang stabil dan tepat, penalaan halus adalah pilihan yang baik. RAG mengutamakan pengambilan kandungan yang relevan tetapi mungkin tidak selalu tepat dalam nuansa khusus.

Penalaan halus memerlukan set data berkualiti tinggi, dan jika hanya melibatkan data dalam skop kecil, ia tidak akan memberi banyak perbezaan. RAG lebih fleksibel  
Penalaan halus adalah kotak hitam, satu metafizik, dan sukar untuk memahami mekanisme dalaman. Tetapi RAG memudahkan pencarian sumber data, dengan itu dapat menyesuaikan halusinasi atau kesilapan kandungan dengan lebih berkesan serta memberikan ketelusan yang lebih baik.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.