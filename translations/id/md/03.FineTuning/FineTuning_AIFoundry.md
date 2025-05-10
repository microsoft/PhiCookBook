<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c1559c5af6caccf6f623fd43a6b3a9a3",
  "translation_date": "2025-05-09T20:34:41+00:00",
  "source_file": "md/03.FineTuning/FineTuning_AIFoundry.md",
  "language_code": "id"
}
-->
# Fine-tuning Phi-3 dengan Azure AI Foundry

Mari kita jelajahi cara melakukan fine-tuning model bahasa Phi-3 Mini milik Microsoft menggunakan Azure AI Foundry. Fine-tuning memungkinkan Anda menyesuaikan Phi-3 Mini untuk tugas tertentu, sehingga menjadi lebih kuat dan lebih peka terhadap konteks.

## Pertimbangan

- **Kemampuan:** Model mana saja yang bisa di-fine-tune? Apa yang bisa dilakukan oleh model dasar setelah di-fine-tune?
- **Biaya:** Bagaimana model harga untuk fine tuning?
- **Kustomisasi:** Seberapa banyak saya bisa memodifikasi model dasar – dan dengan cara apa saja?
- **Kemudahan:** Bagaimana proses fine tuning sebenarnya berlangsung – apakah saya perlu menulis kode khusus? Apakah saya perlu menyediakan komputasi sendiri?
- **Keamanan:** Model yang di-fine-tune dikenal memiliki risiko keamanan – apakah ada pengaman untuk mencegah dampak yang tidak diinginkan?

![AIFoundry Models](../../../../translated_images/AIFoundryModels.4440430c9f07dbd6c625971422e7b9a5b9cb91fa046e447ba9ea41457860532f.id.png)

## Persiapan untuk fine-tuning

### Prasyarat

> [!NOTE]
> Untuk model keluarga Phi-3, penawaran fine-tune dengan model bayar sesuai penggunaan hanya tersedia untuk hub yang dibuat di wilayah **East US 2**.

- Langganan Azure. Jika Anda belum memiliki langganan Azure, buat [akun Azure berbayar](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) untuk memulai.

- Sebuah [proyek AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Kontrol akses berbasis peran Azure (Azure RBAC) digunakan untuk memberikan akses ke operasi di Azure AI Foundry. Untuk melakukan langkah-langkah dalam artikel ini, akun pengguna Anda harus diberikan __peran Azure AI Developer__ pada grup sumber daya.

### Pendaftaran penyedia langganan

Pastikan langganan terdaftar pada penyedia sumber daya `Microsoft.Network`.

1. Masuk ke [portal Azure](https://portal.azure.com).
1. Pilih **Subscriptions** dari menu sebelah kiri.
1. Pilih langganan yang ingin Anda gunakan.
1. Pilih **AI project settings** > **Resource providers** dari menu sebelah kiri.
1. Pastikan **Microsoft.Network** ada dalam daftar penyedia sumber daya. Jika belum, tambahkan.

### Persiapan data

Siapkan data pelatihan dan validasi untuk fine-tuning model Anda. Set data pelatihan dan validasi terdiri dari contoh input dan output sesuai bagaimana Anda ingin model bekerja.

Pastikan semua contoh pelatihan mengikuti format yang diharapkan untuk inferensi. Untuk melakukan fine-tuning dengan efektif, pastikan dataset seimbang dan beragam.

Ini meliputi menjaga keseimbangan data, memasukkan berbagai skenario, dan secara berkala memperbaiki data pelatihan agar sesuai dengan harapan dunia nyata, sehingga menghasilkan respons model yang lebih akurat dan seimbang.

Jenis model yang berbeda membutuhkan format data pelatihan yang berbeda.

### Chat Completion

Data pelatihan dan validasi yang Anda gunakan **harus** diformat sebagai dokumen JSON Lines (JSONL). Untuk `Phi-3-mini-128k-instruct`, dataset fine-tuning harus diformat dalam format percakapan yang digunakan oleh API Chat completions.

### Contoh format file

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Tipe file yang didukung adalah JSON Lines. File diunggah ke datastore default dan tersedia dalam proyek Anda.

## Fine-Tuning Phi-3 dengan Azure AI Foundry

Azure AI Foundry memungkinkan Anda menyesuaikan model bahasa besar dengan dataset pribadi menggunakan proses yang dikenal sebagai fine-tuning. Fine-tuning memberikan nilai signifikan dengan memungkinkan kustomisasi dan optimasi untuk tugas dan aplikasi tertentu. Ini menghasilkan peningkatan performa, efisiensi biaya, pengurangan latensi, dan keluaran yang disesuaikan.

![Finetune AI Foundry](../../../../translated_images/AIFoundryfinetune.69ddc22d1ab08167a7e53a911cd33c749d99fea4047801a836ceb6eec66c5719.id.png)

### Membuat Proyek Baru

1. Masuk ke [Azure AI Foundry](https://ai.azure.com).

1. Pilih **+New project** untuk membuat proyek baru di Azure AI Foundry.

    ![FineTuneSelect](../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.id.png)

1. Lakukan tugas berikut:

    - Nama **Hub** proyek. Harus unik.
    - Pilih **Hub** yang akan digunakan (buat baru jika perlu).

    ![FineTuneSelect](../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.id.png)

1. Lakukan tugas berikut untuk membuat hub baru:

    - Masukkan **Nama Hub**. Harus unik.
    - Pilih **Subscription** Azure Anda.
    - Pilih **Resource group** yang akan digunakan (buat baru jika perlu).
    - Pilih **Lokasi** yang Anda inginkan.
    - Pilih **Connect Azure AI Services** yang akan digunakan (buat baru jika perlu).
    - Pilih **Connect Azure AI Search** ke opsi **Skip connecting**.

    ![FineTuneSelect](../../../../translated_images/create-hub.b93d390a6d3eebd4c33eb7e4ea6ef41fd69c4d39f21339d4bda51af9ed70505f.id.png)

1. Pilih **Next**.
1. Pilih **Create a project**.

### Persiapan Data

Sebelum fine-tuning, kumpulkan atau buat dataset yang relevan dengan tugas Anda, seperti instruksi chat, pasangan tanya jawab, atau data teks relevan lainnya. Bersihkan dan pra-proses data ini dengan menghilangkan noise, menangani nilai yang hilang, dan melakukan tokenisasi teks.

### Fine-tune model Phi-3 di Azure AI Foundry

> [!NOTE]
> Fine-tuning model Phi-3 saat ini didukung untuk proyek yang berlokasi di East US 2.

1. Pilih **Model catalog** dari tab sebelah kiri.

1. Ketik *phi-3* di **search bar** dan pilih model phi-3 yang ingin Anda gunakan.

    ![FineTuneSelect](../../../../translated_images/select-model.02eef2cbb5b7e61a86526b05bd5ec9822fd6b2abae4e38fd5d9bdef541dfb967.id.png)

1. Pilih **Fine-tune**.

    ![FineTuneSelect](../../../../translated_images/select-finetune.88cf562034f78baf0b7f41511fd4c45e1f068104238f1397661b9402ff9e2e09.id.png)

1. Masukkan **Nama model fine-tuned**.

    ![FineTuneSelect](../../../../translated_images/finetune1.8a20c66f797cc7ede7feb789a45c42713b7aeadfeb01dbc34446019db5c189d4.id.png)

1. Pilih **Next**.

1. Lakukan tugas berikut:

    - Pilih **jenis tugas** ke **Chat completion**.
    - Pilih **Data pelatihan** yang ingin digunakan. Anda dapat mengunggahnya melalui data Azure AI Foundry atau dari lingkungan lokal Anda.

    ![FineTuneSelect](../../../../translated_images/finetune2.47df1aa177096dbaa01e4d64a06eb3f46a29718817fa706167af3ea01419a32f.id.png)

1. Pilih **Next**.

1. Unggah **Data validasi** yang ingin digunakan, atau Anda dapat memilih **Automatic split of training data**.

    ![FineTuneSelect](../../../../translated_images/finetune3.e887e47240626c31f969532610c965594635c91cf3f94639fa60fb5d2bbd8f93.id.png)

1. Pilih **Next**.

1. Lakukan tugas berikut:

    - Pilih **Pengali ukuran batch** yang ingin digunakan.
    - Pilih **Learning rate** yang ingin digunakan.
    - Pilih **Epochs** yang ingin digunakan.

    ![FineTuneSelect](../../../../translated_images/finetune4.9f47c2fad66fddd0f091b62a2fa6ac23260226ab841287805d843ebc83761801.id.png)

1. Pilih **Submit** untuk memulai proses fine-tuning.

    ![FineTuneSelect](../../../../translated_images/select-submit.b5344fd77e49bfb6d4efe72e713f6a46f04323d871c118bbf59bf0217698dfee.id.png)

1. Setelah model Anda selesai di-fine-tune, status akan ditampilkan sebagai **Completed**, seperti yang terlihat pada gambar di bawah. Sekarang Anda bisa menerapkan model dan menggunakannya di aplikasi Anda sendiri, di playground, atau di prompt flow. Untuk informasi lebih lanjut, lihat [Cara menerapkan keluarga model bahasa kecil Phi-3 dengan Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/completed.f4be2c6e660d8ba908d1d23e2102925cc31e57cbcd60fb10e7ad3b7925f585c4.id.png)

> [!NOTE]
> Untuk informasi lebih rinci tentang fine-tuning Phi-3, silakan kunjungi [Fine-tune Phi-3 models in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Membersihkan model yang sudah di-fine-tune

Anda dapat menghapus model yang sudah di-fine-tune dari daftar model fine-tuning di [Azure AI Foundry](https://ai.azure.com) atau dari halaman detail model. Pilih model yang ingin dihapus dari halaman Fine-tuning, lalu pilih tombol Delete untuk menghapus model tersebut.

> [!NOTE]
> Anda tidak bisa menghapus model kustom jika masih ada deployment yang aktif. Anda harus menghapus deployment model terlebih dahulu sebelum dapat menghapus model kustom.

## Biaya dan kuota

### Pertimbangan biaya dan kuota untuk model Phi-3 yang di-fine-tune sebagai layanan

Model Phi yang di-fine-tune sebagai layanan ditawarkan oleh Microsoft dan terintegrasi dengan Azure AI Foundry untuk digunakan. Anda dapat menemukan harga saat [menerapkan](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) atau fine-tuning model di tab Harga dan ketentuan pada wizard deployment.

## Penyaringan konten

Model yang diterapkan sebagai layanan dengan bayar sesuai penggunaan dilindungi oleh Azure AI Content Safety. Saat diterapkan ke endpoint real-time, Anda dapat memilih untuk tidak menggunakan fitur ini. Dengan Azure AI Content Safety diaktifkan, baik prompt maupun hasil completions melewati serangkaian model klasifikasi yang bertujuan mendeteksi dan mencegah keluaran konten berbahaya. Sistem penyaringan konten mendeteksi dan mengambil tindakan pada kategori konten berbahaya tertentu baik pada prompt input maupun output completions. Pelajari lebih lanjut tentang [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Konfigurasi Fine-Tuning**

Hyperparameter: Tentukan hyperparameter seperti learning rate, ukuran batch, dan jumlah epoch pelatihan.

**Fungsi Loss**

Pilih fungsi loss yang sesuai untuk tugas Anda (misalnya, cross-entropy).

**Optimizer**

Pilih optimizer (misalnya, Adam) untuk pembaruan gradien selama pelatihan.

**Proses Fine-Tuning**

- Muat Model Pre-Trained: Muat checkpoint Phi-3 Mini.
- Tambahkan Layer Kustom: Tambahkan layer spesifik tugas (misalnya, kepala klasifikasi untuk instruksi chat).

**Latih Model**
Fine-tune model menggunakan dataset yang sudah disiapkan. Pantau kemajuan pelatihan dan sesuaikan hyperparameter jika diperlukan.

**Evaluasi dan Validasi**

Set Validasi: Pisahkan data Anda menjadi set pelatihan dan validasi.

**Evaluasi Performa**

Gunakan metrik seperti akurasi, skor F1, atau perplexity untuk menilai performa model.

## Simpan Model Fine-Tuned

**Checkpoint**
Simpan checkpoint model yang sudah di-fine-tune untuk penggunaan di masa depan.

## Deployment

- Terapkan sebagai Layanan Web: Terapkan model fine-tuned Anda sebagai layanan web di Azure AI Foundry.
- Uji Endpoint: Kirim kueri uji ke endpoint yang sudah diterapkan untuk memverifikasi fungsinya.

## Iterasi dan Perbaikan

Iterasi: Jika performa belum memuaskan, lakukan iterasi dengan menyesuaikan hyperparameter, menambah data, atau fine-tuning untuk epoch tambahan.

## Pantau dan Perbaiki

Pantau perilaku model secara terus-menerus dan lakukan perbaikan sesuai kebutuhan.

## Kustomisasi dan Perluas

Tugas Kustom: Phi-3 Mini bisa di-fine-tune untuk berbagai tugas selain instruksi chat. Jelajahi kasus penggunaan lainnya!
Eksperimen: Coba berbagai arsitektur, kombinasi layer, dan teknik untuk meningkatkan performa.

> [!NOTE]
> Fine-tuning adalah proses iteratif. Eksperimen, pelajari, dan sesuaikan model Anda untuk mendapatkan hasil terbaik sesuai tugas spesifik Anda!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.