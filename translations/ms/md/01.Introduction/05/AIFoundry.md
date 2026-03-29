# **Menggunakan Microsoft Foundry untuk penilaian**

![aistudo](../../../../../translated_images/ms/AIFoundry.9e0b513e999a1c5a.webp)

Cara menilai aplikasi AI generatif anda menggunakan [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Sama ada anda menilai perbualan satu pusingan atau pelbagai pusingan, Microsoft Foundry menyediakan alat untuk menilai prestasi dan keselamatan model.

![aistudo](../../../../../translated_images/ms/AIPortfolio.69da59a8e1eaa70f.webp)

## Cara menilai aplikasi AI generatif dengan Microsoft Foundry
Untuk arahan terperinci lihat [Dokumentasi Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Berikut adalah langkah-langkah untuk memulakan:

## Menilai Model AI Generatif dalam Microsoft Foundry

**Prasyarat**

- Dataset ujian dalam format CSV atau JSON.
- Model AI generatif telah diterapkan (seperti Phi-3, GPT 3.5, GPT 4, atau model Davinci).
- Runtime dengan instance pengkomputeran untuk menjalankan penilaian.

## Metrik Penilaian Terbina Dalam

Microsoft Foundry membolehkan anda menilai perbualan satu pusingan dan yang kompleks, pelbagai pusingan.
Untuk senario Retrieval Augmented Generation (RAG), di mana model berasaskan data tertentu, anda boleh menilai prestasi menggunakan metrik penilaian terbina dalam.
Selain itu, anda boleh menilai senario menjawab soalan satu pusingan biasa (bukan RAG).

## Membuat Larian Penilaian

Dari antara muka Microsoft Foundry, pergi ke halaman Evaluate atau halaman Prompt Flow.
Ikuti wizard penciptaan penilaian untuk menetapkan larian penilaian. Berikan nama pilihan untuk penilaian anda.
Pilih senario yang selaras dengan objektif aplikasi anda.
Pilih satu atau lebih metrik penilaian untuk menilai output model.

## Aliran Penilaian Tersuai (Pilihan)

Untuk fleksibiliti lebih besar, anda boleh mewujudkan aliran penilaian tersuai. Sesuaikan proses penilaian mengikut keperluan khusus anda.

## Melihat Keputusan

Selepas menjalankan penilaian, rekod, lihat, dan analisa metrik penilaian terperinci dalam Microsoft Foundry. Dapatkan pandangan tentang kebolehan dan had aplikasi anda.



**Note** Microsoft Foundry kini dalam pratonton awam, jadi gunakannya untuk tujuan eksperimen dan pembangunan. Untuk beban kerja pengeluaran, pertimbangkan pilihan lain. Terokai [dokumentasi rasmi AI Foundry](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) untuk maklumat lanjut dan arahan langkah demi langkah.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber yang sah. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->