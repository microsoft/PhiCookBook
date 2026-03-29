# Fine-tuning Phi-3 dengan Microsoft Foundry

Mari kita jelajahi cara melakukan fine-tuning pada model bahasa Phi-3 Mini dari Microsoft menggunakan Microsoft Foundry. Fine-tuning memungkinkan Anda menyesuaikan Phi-3 Mini untuk tugas tertentu, menjadikannya lebih kuat dan paham konteks.

## Pertimbangan

- **Kemampuan:** Model mana saja yang bisa di-fine-tune? Apa yang dapat dilakukan model dasar setelah di-fine-tune?
- **Biaya:** Bagaimana model harga untuk fine-tuning.
- **Kustomisasi:** Seberapa banyak saya dapat memodifikasi model dasar – dan dengan cara apa?
- **Kenyamanan:** Bagaimana proses fine-tuning dilakukan – apakah saya perlu menulis kode khusus? Apakah saya perlu menyediakan komputasi sendiri?
- **Keamanan:** Model yang di-fine-tune diketahui memiliki risiko keamanan – apakah ada pengaman untuk melindungi dari bahaya yang tidak diinginkan?

![AIFoundry Models](../../../../translated_images/id/AIFoundryModels.0e1b16f7d0b09b73.webp)

## Persiapan untuk fine-tuning

### Prasyarat

> [!NOTE]
> Untuk model keluarga Phi-3, penawaran fine-tune pay-as-you-go hanya tersedia pada hub yang dibuat di wilayah **East US 2**.

- Langganan Azure. Jika Anda belum memiliki langganan Azure, buat [akun Azure berbayar](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) untuk memulai.

- Sebuah [proyek AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Kontrol akses berbasis peran Azure (Azure RBAC) digunakan untuk memberikan akses ke operasi di Microsoft Foundry. Untuk melakukan langkah-langkah dalam artikel ini, akun pengguna Anda harus diberikan __peran Azure AI Developer__ pada grup sumber daya.

### Registrasi penyedia langganan

Pastikan langganan sudah terdaftar pada penyedia sumber daya `Microsoft.Network`.

1. Masuk ke [portal Azure](https://portal.azure.com).
1. Pilih **Subscriptions** dari menu sebelah kiri.
1. Pilih langganan yang ingin Anda gunakan.
1. Pilih **AI project settings** > **Resource providers** dari menu sebelah kiri.
1. Pastikan **Microsoft.Network** ada dalam daftar penyedia sumber daya. Jika tidak, tambahkan.

### Persiapan data

Siapkan data pelatihan dan data validasi untuk fine-tuning model Anda. Data pelatihan dan data validasi terdiri dari contoh input dan output tentang bagaimana Anda ingin model bekerja.

Pastikan semua contoh pelatihan mengikuti format yang diharapkan untuk inferensi. Untuk melakukan fine-tuning model secara efektif, pastikan dataset seimbang dan beragam.

Hal ini meliputi menjaga keseimbangan data, memasukkan berbagai skenario, dan secara berkala memperbaiki data pelatihan agar selaras dengan ekspektasi dunia nyata, yang pada akhirnya menghasilkan respons model yang lebih akurat dan seimbang.

Jenis model berbeda membutuhkan format data pelatihan yang berbeda.

### Penyelesaian Chat

Data pelatihan dan validasi yang Anda gunakan **harus** diformat sebagai dokumen JSON Lines (JSONL). Untuk `Phi-3-mini-128k-instruct`, dataset fine-tuning harus diformat dalam format percakapan yang digunakan oleh API penyelesaian Chat.

### Contoh format file

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```
  
Jenis file yang didukung adalah JSON Lines. File diunggah ke datastore default dan dibuat tersedia dalam proyek Anda.

## Fine-Tuning Phi-3 dengan Microsoft Foundry

Microsoft Foundry memungkinkan Anda menyesuaikan model bahasa besar dengan dataset pribadi menggunakan proses yang disebut fine-tuning. Fine-tuning memberikan nilai signifikan dengan memungkinkan kustomisasi dan optimasi untuk tugas dan aplikasi tertentu. Hal ini menghasilkan performa yang lebih baik, efisiensi biaya, latensi yang berkurang, dan output yang disesuaikan.

![Finetune AI Foundry](../../../../translated_images/id/AIFoundryfinetune.193aaddce48d553c.webp)

### Membuat Proyek Baru

1. Masuk ke [Microsoft Foundry](https://ai.azure.com).

1. Pilih **+New project** untuk membuat proyek baru di Microsoft Foundry.

    ![FineTuneSelect](../../../../translated_images/id/select-new-project.cd31c0404088d7a3.webp)

1. Lakukan tugas berikut:

    - Nama **Hub** proyek. Harus berupa nilai unik.
    - Pilih **Hub** yang ingin digunakan (buat baru jika diperlukan).

    ![FineTuneSelect](../../../../translated_images/id/create-project.ca3b71298b90e420.webp)

1. Lakukan tugas berikut untuk membuat hub baru:

    - Masukkan **Hub name**. Harus berupa nilai unik.
    - Pilih **Subscription** Azure Anda.
    - Pilih **Resource group** yang ingin digunakan (buat baru jika diperlukan).
    - Pilih **Location** yang ingin Anda pakai.
    - Pilih **Connect Azure AI Services** yang ingin dipakai (buat baru jika diperlukan).
    - Pilih **Connect Azure AI Search** ke **Skip connecting**.

    ![FineTuneSelect](../../../../translated_images/id/create-hub.49e53d235e80779e.webp)

1. Pilih **Next**.
1. Pilih **Create a project**.

### Persiapan Data

Sebelum fine-tuning, kumpulkan atau buat dataset yang relevan dengan tugas Anda, seperti instruksi chat, pasangan tanya jawab, atau data teks relevan lainnya. Bersihkan dan pra-proses data ini dengan menghilangkan noise, menangani nilai hilang, dan men-tokenisasi teks.

### Fine-tune model Phi-3 dalam Microsoft Foundry

> [!NOTE]
> Fine-tuning model Phi-3 saat ini didukung hanya untuk proyek yang berada di East US 2.

1. Pilih **Model catalog** dari tab sebelah kiri.

1. Ketik *phi-3* di **bar pencarian** dan pilih model phi-3 yang ingin Anda gunakan.

    ![FineTuneSelect](../../../../translated_images/id/select-model.60ef2d4a6a3cec57.webp)

1. Pilih **Fine-tune**.

    ![FineTuneSelect](../../../../translated_images/id/select-finetune.a976213b543dd9d8.webp)

1. Masukkan **Nama model fine-tuned**.

    ![FineTuneSelect](../../../../translated_images/id/finetune1.c2b39463f0d34148.webp)

1. Pilih **Next**.

1. Lakukan tugas berikut:

    - Pilih **jenis tugas** menjadi **Chat completion**.
    - Pilih **Data training** yang ingin Anda gunakan. Anda dapat mengunggahnya melalui data Microsoft Foundry atau dari lingkungan lokal Anda.

    ![FineTuneSelect](../../../../translated_images/id/finetune2.43cb099b1a94442d.webp)

1. Pilih **Next**.

1. Unggah **Data Validasi** yang ingin digunakan, atau Anda dapat memilih **Automatic split of training data**.

    ![FineTuneSelect](../../../../translated_images/id/finetune3.fd96121b67dcdd92.webp)

1. Pilih **Next**.

1. Lakukan tugas berikut:

    - Pilih **Pengali ukuran batch** yang ingin digunakan.
    - Pilih **Learning rate** yang ingin digunakan.
    - Pilih **Epochs** yang ingin digunakan.

    ![FineTuneSelect](../../../../translated_images/id/finetune4.e18b80ffccb5834a.webp)

1. Pilih **Submit** untuk memulai proses fine-tuning.

    ![FineTuneSelect](../../../../translated_images/id/select-submit.0a3802d581bac271.webp)

1. Setelah model Anda selesai di-fine-tune, status akan ditampilkan sebagai **Completed**, seperti yang terlihat pada gambar di bawah. Kini Anda dapat menerapkan model dan menggunakannya dalam aplikasi Anda sendiri, di playground, atau dalam prompt flow. Untuk informasi lebih lanjut, lihat [Cara menerapkan keluarga model bahasa kecil Phi-3 dengan Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/id/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Untuk informasi lebih detail tentang fine-tuning Phi-3, silakan kunjungi [Fine-tune model Phi-3 di Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Membersihkan model fine-tuned Anda

Anda dapat menghapus model fine-tuned dari daftar model fine-tuning di [Microsoft Foundry](https://ai.azure.com) atau dari halaman detail model. Pilih model fine-tuned yang ingin dihapus dari halaman Fine-tuning, kemudian pilih tombol Hapus untuk menghapus model fine-tuned tersebut.

> [!NOTE]
> Anda tidak dapat menghapus model kustom jika ada deployment yang berjalan. Anda harus terlebih dahulu menghapus deployment model Anda sebelum dapat menghapus model kustom tersebut.

## Biaya dan kuota

### Pertimbangan biaya dan kuota untuk model Phi-3 fine-tuned sebagai layanan

Model Phi yang di-fine-tune sebagai layanan disediakan oleh Microsoft dan terintegrasi dengan Microsoft Foundry untuk digunakan. Anda dapat menemukan harga saat [menerapkan](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) atau melakukan fine-tuning model di bawah tab Harga dan ketentuan pada wizard deployment.

## Penyaringan konten

Model yang dideploy sebagai layanan dengan sistem pay-as-you-go dilindungi oleh Azure AI Content Safety. Ketika dideploy ke endpoint real-time, Anda dapat memilih untuk menonaktifkan kemampuan ini. Dengan fitur Azure AI content safety aktif, baik prompt maupun hasil penyelesaian melewati serangkaian model klasifikasi yang bertujuan mendeteksi dan mencegah keluaran konten berbahaya. Sistem penyaringan konten mendeteksi dan mengambil tindakan terhadap kategori-kategori konten yang potensi membahayakan baik pada prompt input maupun output penyelesaian. Pelajari lebih lanjut tentang [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Konfigurasi Fine-Tuning**

Hyperparameters: Definisikan hyperparameter seperti learning rate, ukuran batch, dan jumlah epoch pelatihan.

**Fungsi Loss**

Pilih fungsi loss yang sesuai untuk tugas Anda (misalnya, cross-entropy).

**Optimizer**

Pilih optimizer (misalnya, Adam) untuk pembaruan gradien selama pelatihan.

**Proses Fine-Tuning**

- Muat Model Pra-Latih: Muat checkpoint Phi-3 Mini.
- Tambah Layer Kustom: Tambahkan layer khusus tugas (misalnya, kepala klasifikasi untuk instruksi chat).

**Latih Model**  
Lakukan fine-tuning model menggunakan dataset yang telah disiapkan. Pantau kemajuan pelatihan dan sesuaikan hyperparameter sesuai kebutuhan.

**Evaluasi dan Validasi**

Set Validasi: Pisahkan data Anda menjadi set pelatihan dan validasi.

**Evaluasi Performa**

Gunakan metrik seperti akurasi, skor F1, atau perplexity untuk menilai kinerja model.

## Simpan Model Fine-Tuned

**Checkpoint**  
Simpan checkpoint model fine-tuned untuk penggunaan di masa depan.

## Deployment

- Deploy sebagai Layanan Web: Deploy model fine-tuned Anda sebagai layanan web di Microsoft Foundry.
- Uji Endpoint: Kirim kueri uji ke endpoint yang dideploy untuk memverifikasi fungsi.

## Iterasi dan Perbaikan

Iterasi: Jika performa belum memuaskan, lakukan iterasi dengan menyesuaikan hyperparameter, menambah data, atau fine-tuning untuk epoch tambahan.

## Monitor dan Refinasi

Pantau perilaku model secara terus-menerus dan lakukan refinasi bila diperlukan.

## Kustomisasi dan Perluasan

Tugas Kustom: Phi-3 Mini dapat di-fine-tune untuk berbagai tugas selain instruksi chat. Jelajahi kasus penggunaan lainnya!  
Eksperimen: Cobalah arsitektur, kombinasi layer, dan teknik berbeda untuk meningkatkan performa.

> [!NOTE]
> Fine-tuning adalah proses iteratif. Bereksperimenlah, belajar, dan sesuaikan model Anda untuk mencapai hasil terbaik pada tugas yang Anda inginkan!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk keakuratan, mohon diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau kesalahan interpretasi yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->