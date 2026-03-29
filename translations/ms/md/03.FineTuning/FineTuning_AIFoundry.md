# Penalaan Halus Phi-3 dengan Microsoft Foundry

 Mari kita terokai cara untuk melakukan penalaan halus model bahasa Phi-3 Mini Microsoft menggunakan Microsoft Foundry. Penalaan halus membolehkan anda menyesuaikan Phi-3 Mini untuk tugasan tertentu, menjadikannya lebih berkuasa dan peka konteks.

## Pertimbangan

- **Keupayaan:** Model mana yang boleh ditala halus? Apakah yang boleh dilakukan oleh model asas selepas ditala halus?
- **Kos:** Apakah model harga untuk penalaan halus
**Kebolehpenyesuaian:** Sejauh mana saya boleh mengubah suai model asas – dan dalam cara apa?
- **Kemudahan:** Bagaimana sebenarnya penalaan halus dijalankan – adakah saya perlu menulis kod tersuai? Adakah saya perlu menyediakan pengkomputeran saya sendiri?
- **Keselamatan:** Model yang ditala halus diketahui mempunyai risiko keselamatan – adakah terdapat tembok pelindung untuk mengelakkan kemudaratan yang tidak disengajakan?

![AIFoundry Models](../../../../translated_images/ms/AIFoundryModels.0e1b16f7d0b09b73.webp)

## Penyediaan untuk penalaan halus

### Prasyarat

> [!NOTE]
> Untuk model keluarga Phi-3, penawaran penalaan halus bayaran ikut guna hanya tersedia dengan hab yang dibuat di wilayah **East US 2**.

- Langganan Azure. Jika anda tidak mempunyai langganan Azure, buat akaun Azure berbayar [paid Azure account](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) untuk bermula.

- Projek [AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Kawalan akses berasaskan peranan Azure (Azure RBAC) digunakan untuk memberikan akses ke operasi dalam Microsoft Foundry. Untuk menjalankan langkah-langkah dalam artikel ini, akaun pengguna anda mesti diberikan __peranan Pembangun AI Azure__ pada kumpulan sumber.

### Pendaftaran penyedia langganan

Sahkan langganan didaftarkan kepada pembekal sumber `Microsoft.Network`.

1. Log masuk ke [portal Azure](https://portal.azure.com).
1. Pilih **Langganan** dari menu kiri.
1. Pilih langganan yang anda ingin gunakan.
1. Pilih **Tetapan projek AI** > **Penyedia sumber** dari menu kiri.
1. Sahkan bahawa **Microsoft.Network** berada dalam senarai penyedia sumber. Jika tidak, tambahkannya.

### Penyediaan data

Sediakan data latihan dan pengesahan anda untuk menala halus model anda. Set data latihan dan pengesahan anda terdiri daripada contoh input dan output tentang bagaimana anda ingin model berfungsi.

Pastikan semua contoh latihan anda mengikuti format yang dijangka untuk inferens. Untuk menala halus model dengan berkesan, pastikan dataset seimbang dan pelbagai.

Ini melibatkan mengekalkan keseimbangan data, termasuk pelbagai senario, dan secara berkala memperhalusi data latihan supaya selari dengan jangkaan dunia nyata, yang akhirnya membawa kepada respons model yang lebih tepat dan seimbang.

Jenis model yang berbeza memerlukan format data latihan yang berbeza.

### Lengkapkan Sembang

Data latihan dan pengesahan yang anda gunakan **mestilah** diformatkan sebagai dokumen JSON Lines (JSONL). Untuk `Phi-3-mini-128k-instruct`, dataset penalaan halus mesti diformatkan dalam format perbualan yang digunakan oleh API Lengkapkan Sembang.

### Contoh format fail

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Jenis fail yang disokong adalah JSON Lines. Fail-fail dimuat naik ke stor data lalai dan disediakan dalam projek anda.

## Penalaan Halus Phi-3 dengan Microsoft Foundry

Microsoft Foundry membolehkan anda menyesuaikan model bahasa besar dengan set data peribadi anda menggunakan proses yang dikenali sebagai penalaan halus. Penalaan halus memberikan nilai yang signifikan dengan membolehkan penyesuaian dan pengoptimuman untuk tugasan dan aplikasi tertentu. Ia membawa kepada prestasi yang lebih baik, kecekapan kos, kelewatan yang dikurangkan, dan hasil yang disesuaikan.

![Finetune AI Foundry](../../../../translated_images/ms/AIFoundryfinetune.193aaddce48d553c.webp)

### Buat Projek Baru

1. Log masuk ke [Microsoft Foundry](https://ai.azure.com).

1. Pilih **+Projek baru** untuk membuat projek baru dalam Microsoft Foundry.

    ![FineTuneSelect](../../../../translated_images/ms/select-new-project.cd31c0404088d7a3.webp)

1. Lakukan tugas berikut:

    - Nama **Hab** projek. Ia mesti nilai unik.
    - Pilih **Hab** yang hendak digunakan (buat satu yang baru jika perlu).

    ![FineTuneSelect](../../../../translated_images/ms/create-project.ca3b71298b90e420.webp)

1. Lakukan tugasan berikut untuk membuat hab baru:

    - Masukkan **Nama Hab**. Ia mesti nilai unik.
    - Pilih **Langganan** Azure anda.
    - Pilih **Kumpulan sumber** yang hendak digunakan (buat satu baru jika perlu).
    - Pilih **Lokasi** yang ingin digunakan.
    - Pilih **Sambungkan Perkhidmatan AI Azure** yang hendak digunakan (buat satu baru jika perlu).
    - Pilih **Sambungkan Carian AI Azure** ke **Langkau sambungan**.

    ![FineTuneSelect](../../../../translated_images/ms/create-hub.49e53d235e80779e.webp)

1. Pilih **Seterusnya**.
1. Pilih **Buat projek**.

### Penyediaan Data

Sebelum penalaan halus, kumpul atau buat dataset yang berkaitan dengan tugasan anda, seperti arahan sembang, pasangan soalan-jawapan, atau apa-apa data teks yang relevan. Bersihkan dan pra-proses data ini dengan menghapuskan gangguan, mengendalikan nilai hilang, dan menokennya.

### Penalaan halus model Phi-3 dalam Microsoft Foundry

> [!NOTE]
> Penalaan halus model Phi-3 kini disokong dalam projek yang terletak di East US 2.

1. Pilih **Katalog model** dari tab sisi kiri.

1. Taip *phi-3* dalam **bar carian** dan pilih model phi-3 yang anda ingin gunakan.

    ![FineTuneSelect](../../../../translated_images/ms/select-model.60ef2d4a6a3cec57.webp)

1. Pilih **Penalaan halus**.

    ![FineTuneSelect](../../../../translated_images/ms/select-finetune.a976213b543dd9d8.webp)

1. Masukkan **Nama model yang telah ditala halus**.

    ![FineTuneSelect](../../../../translated_images/ms/finetune1.c2b39463f0d34148.webp)

1. Pilih **Seterusnya**.

1. Lakukan tugas berikut:

    - Pilih **jenis tugasan** kepada **Lengkapkan sembang**.
    - Pilih **data latihan** yang anda ingin gunakan. Anda boleh memuat naik melalui data Microsoft Foundry atau dari persekitaran tempatan anda.

    ![FineTuneSelect](../../../../translated_images/ms/finetune2.43cb099b1a94442d.webp)

1. Pilih **Seterusnya**.

1. Muat naik **data pengesahan** yang anda ingin gunakan, atau anda boleh pilih **Pisahan automatik data latihan**.

    ![FineTuneSelect](../../../../translated_images/ms/finetune3.fd96121b67dcdd92.webp)

1. Pilih **Seterusnya**.

1. Lakukan tugasan berikut:

    - Pilih **peningkat gandaan saiz kumpulan** yang anda mahu gunakan.
    - Pilih **kadar pembelajaran** yang anda mahu gunakan.
    - Pilih **Epoch** yang anda mahu gunakan.

    ![FineTuneSelect](../../../../translated_images/ms/finetune4.e18b80ffccb5834a.webp)

1. Pilih **Hantar** untuk memulakan proses penalaan halus.

    ![FineTuneSelect](../../../../translated_images/ms/select-submit.0a3802d581bac271.webp)


1. Setelah model anda selesai ditala halus, status akan dipaparkan sebagai **Selesai**, seperti yang ditunjukkan dalam gambar di bawah. Kini anda boleh menggerakkan model dan menggunakannya dalam aplikasi anda sendiri, di playgraund, atau dalam aliran arahan. Untuk maklumat lanjut, lihat [Cara menggerakkan model keluarga kecil Phi-3 dengan Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/ms/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Untuk maklumat lebih terperinci tentang penalaan halus Phi-3, sila lawati [Penalaan halus model Phi-3 dalam Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Bersihkan model yang telah ditala halus anda

Anda boleh memadam model yang telah ditala halus dari senarai model penalaan halus di [Microsoft Foundry](https://ai.azure.com) atau dari halaman butiran model. Pilih model yang ditala halus yang ingin dipadam dari halaman Penalaan Halus, kemudian pilih butang Padam untuk memadam model yang ditala halus tersebut.

> [!NOTE]
> Anda tidak boleh memadam model tersuai jika ia mempunyai penggerakan sedia ada. Anda mesti memadam penggerakan model anda terlebih dahulu sebelum anda boleh memadam model tersuai anda.

## Kos dan kuota

### Pertimbangan kos dan kuota untuk model Phi-3 yang ditala halus sebagai perkhidmatan

Model Phi yang ditala halus sebagai perkhidmatan ditawarkan oleh Microsoft dan diintegrasikan dengan Microsoft Foundry untuk kegunaan. Anda boleh mendapatkan harga semasa [menggerakkan](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) atau menala halus model di bawah tab Harga dan terma pada wizard penggerakan.

## Penapisan kandungan

Model yang digerakkan sebagai perkhidmatan bayaran ikut guna dilindungi oleh Azure AI Content Safety. Apabila digerakkan ke titik akhir masa nyata, anda boleh memilih untuk tidak menggunakan keupayaan ini. Dengan keselamatan kandungan Azure AI diaktifkan, kedua-dua permintaan dan jawapan melalui satu ansambel model klasifikasi yang bertujuan mengesan dan menghalang keluaran kandungan berbahaya. Sistem penapisan kandungan mengesan dan mengambil tindakan terhadap kategori kandungan berbahaya tertentu dalam kedua-dua permintaan input dan jawapan output. Ketahui lebih lanjut mengenai [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Konfigurasi Penalaan Halus**

Hiperparameter: Tetapkan hiperparameter seperti kadar pembelajaran, saiz kumpulan, dan bilangan epoch latihan.

**Fungsi Kerugian**

Pilih fungsi kerugian yang sesuai untuk tugasan anda (contohnya, cross-entropy).

**Pengoptimum**

Pilih pengoptimum (contohnya, Adam) untuk kemas kini kecerunan semasa latihan.

**Proses Penalaan Halus**

- Muat Model Pra-Latih: Muatkan penanda tempat Phi-3 Mini.
- Tambah Lapisan Tersuai: Tambah lapisan khusus tugasan (contohnya, kepala klasifikasi untuk arahan sembang).

**Latih Model**
Tala halus model menggunakan dataset yang telah disediakan. Pantau kemajuan latihan dan sesuaikan hiperparameter jika perlu.

**Penilaian dan Pengesahan**

Set Pengesahan: Bahagikan data anda kepada set latihan dan pengesahan.

**Nilai Prestasi**

Gunakan metrik seperti ketepatan, skor F1, atau kekeliruan untuk menilai prestasi model.

## Simpan Model yang Telah Ditala Halus

**Tanda Tempat**
Simpan tanda tempat model yang telah ditala halus untuk kegunaan masa depan.

## Penggerakan

- Gerakkan sebagai Perkhidmatan Web: Gerakkan model yang telah ditala halus sebagai perkhidmatan web dalam Microsoft Foundry.
- Uji Titik Akhir: Hantar pertanyaan ujian ke titik akhir yang digerakkan untuk mengesahkan fungsinya.

## Ulang dan Baiki

Ulang: Jika prestasi tidak memuaskan, ulang dengan melaraskan hiperparameter, menambah lebih banyak data, atau menala halus untuk lebih banyak epoch.

## Pantau dan Perhalusi

Pantau secara berterusan tingkah laku model dan perhalusi jika perlu.

## Sesuaikan dan Luaskan

Tugasan Tersuai: Phi-3 Mini boleh ditala halus untuk pelbagai tugasan selain arahan sembang. Terokai kegunaan lain!
Eksperimen: Cuba seni bina berbeza, gabungan lapisan, dan teknik untuk meningkatkan prestasi.

> [!NOTE]
> Penalaan halus adalah proses berulang. Eksperimen, pelajari, dan sesuaikan model anda untuk mencapai hasil terbaik bagi tugasan khusus anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sah. Untuk maklumat kritikal, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->