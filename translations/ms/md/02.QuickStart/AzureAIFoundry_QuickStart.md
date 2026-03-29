# **Menggunakan Phi-3 dalam Microsoft Foundry**

Dengan perkembangan Generative AI, kami berharap untuk menggunakan platform sehenti untuk menguruskan pelbagai LLM dan SLM, integrasi data perusahaan, operasi penalaan halus/RAG, dan penilaian pelbagai perniagaan perusahaan selepas mengintegrasikan LLM dan SLM, dan lain-lain, supaya aplikasi AI generatif boleh dilaksanakan dengan lebih baik. [Microsoft Foundry](https://ai.azure.com) adalah platform aplikasi generatif AI tahap perusahaan.

![aistudo](../../../../translated_images/ms/aifoundry_home.f28a8127c96c7d93.webp)

Dengan Microsoft Foundry, anda boleh menilai respons model bahasa besar (LLM) dan mengorkestrakan komponen aplikasi prompt dengan aliran prompt untuk prestasi yang lebih baik. Platform ini memudahkan kebolehskalaan untuk mengubah bukti konsep menjadi produksi sepenuhnya dengan mudah. Pemantauan dan penambahbaikan berterusan menyokong kejayaan jangka panjang.

Kami boleh dengan cepat menyebarkan model Phi-3 di Microsoft Foundry melalui langkah mudah, dan kemudian menggunakan Microsoft Foundry untuk melengkapkan kerja berkaitan Playground/Chat, Penalaan Halus, penilaian dan kerja berkaitan Phi-3 lain.

## **1. Persediaan**

Jika anda sudah memasang [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) pada mesin anda, menggunakan templat ini adalah semudah menjalankan arahan ini dalam direktori baru.

## Penciptaan Manual

Mewujudkan projek dan hub Microsoft Foundry adalah cara yang bagus untuk mengatur dan mengurus kerja AI anda. Berikut adalah panduan langkah demi langkah untuk memulakan:

### Mewujudkan Projek dalam Microsoft Foundry

1. **Pergi ke Microsoft Foundry**: Log masuk ke portal Microsoft Foundry.
2. **Cipta Projek**:
   - Jika anda berada dalam projek, pilih "Microsoft Foundry" di sudut kiri atas halaman untuk pergi ke halaman Utama.
   - Pilih "+ Cipta projek".
   - Masukkan nama untuk projek.
   - Jika anda sudah ada hub, ia akan dipilih secara lalai. Jika anda mempunyai akses ke lebih dari satu hub, anda boleh memilih yang lain dari dropdown. Jika anda mahu mencipta hub baru, pilih "Cipta hub baru" dan berikan nama.
   - Pilih "Cipta".

### Mewujudkan Hub dalam Microsoft Foundry

1. **Pergi ke Microsoft Foundry**: Log masuk dengan akaun Azure anda.
2. **Cipta Hub**:
   - Pilih pusat Pengurusan dari menu kiri.
   - Pilih "Semua sumber", kemudian panah ke bawah sebelah "+ Projek baru" dan pilih "+ Hub baru".
   - Dalam dialog "Cipta hub baru", masukkan nama untuk hub anda (contohnya, contoso-hub) dan ubah medan lain mengikut kehendak.
   - Pilih "Seterusnya", semak maklumat, kemudian pilih "Cipta".

Untuk arahan yang lebih terperinci, anda boleh rujuk dokumentasi rasmi [Microsoft](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Selepas penciptaan berjaya, anda boleh mengakses studio yang anda cipta melalui [ai.azure.com](https://ai.azure.com/)

Boleh ada pelbagai projek dalam satu AI Foundry. Cipta projek dalam AI Foundry untuk bersedia.

Cipta Microsoft Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. Menyebarkan model Phi dalam Microsoft Foundry**

Klik pilihan Terokai pada projek untuk masuk ke Katalog Model dan pilih Phi-3

Pilih Phi-3-mini-4k-instruct

Klik 'Sebar' untuk menyebarkan model Phi-3-mini-4k-instruct

> [!NOTE]
>
> Anda boleh memilih kuasa pengkomputeran semasa penyebaran

## **3. Playground Chat Phi dalam Microsoft Foundry**

Pergi ke halaman penyebaran, pilih Playground, dan berbual dengan Phi-3 Microsoft Foundry

## **4. Menyebarkan Model dari Microsoft Foundry**

Untuk menyebarkan model dari Katalog Model Azure, anda boleh ikut langkah berikut:

- Log masuk ke Microsoft Foundry.
- Pilih model yang anda mahu sebarkan dari katalog model Microsoft Foundry.
- Pada halaman Butiran model, pilih Sebar dan kemudian pilih API Tanpa Server dengan Azure AI Content Safety.
- Pilih projek di mana anda mahu menyebarkan model anda. Untuk menggunakan tawaran API Tanpa Server, ruang kerja anda mesti berada di rantau East US 2 atau Sweden Central. Anda boleh menyesuaikan nama Penyebaran.
- Pada wizard penyebaran, pilih Harga dan terma untuk mengetahui tentang harga dan terma penggunaan.
- Pilih Sebar. Tunggu sehingga penyebaran siap dan anda dialihkan ke halaman Penyebaran.
- Pilih Buka dalam playground untuk mula berinteraksi dengan model.
- Anda boleh kembali ke halaman Penyebaran, pilih penyebaran, dan ambil perhatian URL Sasaran titik akhir dan Kunci Rahsia, yang boleh anda gunakan untuk memanggil penyebaran dan menjana hasil.
- Anda sentiasa boleh mencari butiran titik akhir, URL, dan kunci akses dengan menuju ke tab Build dan memilih Penyebaran dari bahagian Komponen.

> [!NOTE]
> Sila ambil perhatian akaun anda mesti mempunyai kebenaran peranan Pembangun Azure AI pada Kumpulan Sumber untuk melaksanakan langkah ini.

## **5. Menggunakan Phi API dalam Microsoft Foundry**

Anda boleh akses https://{Nama projek anda}.region.inference.ml.azure.com/swagger.json melalui Postman GET dan gabungkan dengan Kunci untuk mempelajari antaramuka yang disediakan

Anda boleh mendapatkan parameter permintaan dengan sangat mudah, serta parameter respons.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber autoritatif. Untuk maklumat kritikal, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->