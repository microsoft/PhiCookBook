# **Menggunakan Phi-3 di Microsoft Foundry**

Dengan perkembangan Generative AI, kami berharap menggunakan platform terpadu untuk mengelola berbagai LLM dan SLM, integrasi data perusahaan, operasi fine-tuning/RAG, dan evaluasi berbagai bisnis perusahaan setelah mengintegrasikan LLM dan SLM, dll., sehingga AI generatif dapat diterapkan aplikasi Cerdas dengan lebih baik. [Microsoft Foundry](https://ai.azure.com) adalah platform aplikasi generatif AI tingkat perusahaan.

![aistudo](../../../../translated_images/id/aifoundry_home.f28a8127c96c7d93.webp)

Dengan Microsoft Foundry, Anda dapat mengevaluasi respons model bahasa besar (LLM) dan mengatur komponen aplikasi prompt dengan prompt flow untuk kinerja yang lebih baik. Platform ini memfasilitasi skalabilitas untuk mengubah bukti konsep menjadi produksi penuh dengan mudah. Pemantauan dan penyempurnaan terus-menerus mendukung keberhasilan jangka panjang.

Kita dapat dengan cepat menerapkan model Phi-3 di Microsoft Foundry melalui langkah-langkah sederhana, lalu menggunakan Microsoft Foundry untuk menyelesaikan Playground/Chat terkait Phi-3, Fine-tuning, evaluasi, dan pekerjaan terkait lainnya.

## **1. Persiapan**

Jika Anda sudah menginstal [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) di mesin Anda, menggunakan template ini sesederhana menjalankan perintah ini di direktori baru.

## Pembuatan Manual

Membuat proyek dan hub Microsoft Foundry adalah cara yang bagus untuk mengatur dan mengelola pekerjaan AI Anda. Berikut panduan langkah demi langkah untuk memulai:

### Membuat Proyek di Microsoft Foundry

1. **Buka Microsoft Foundry**: Masuk ke portal Microsoft Foundry.
2. **Buat Proyek**:
   - Jika Anda sedang berada dalam proyek, pilih "Microsoft Foundry" di kiri atas halaman untuk menuju ke halaman Beranda.
   - Pilih "+ Create project".
   - Masukkan nama untuk proyek tersebut.
   - Jika Anda memiliki hub, akan dipilih secara default. Jika Anda memiliki akses ke lebih dari satu hub, Anda dapat memilih hub lain dari dropdown. Jika Anda ingin membuat hub baru, pilih "Create new hub" dan beri nama.
   - Pilih "Create".

### Membuat Hub di Microsoft Foundry

1. **Buka Microsoft Foundry**: Masuk dengan akun Azure Anda.
2. **Buat Hub**:
   - Pilih pusat Manajemen dari menu kiri.
   - Pilih "All resources", lalu panah bawah di samping "+ New project" dan pilih "+ New hub".
   - Di dialog "Create a new hub", masukkan nama untuk hub Anda (misalnya, contoso-hub) dan ubah bidang lain sesuai keinginan.
   - Pilih "Next", tinjau informasinya, lalu pilih "Create".

Untuk instruksi yang lebih rinci, Anda dapat merujuk ke [dokumentasi resmi Microsoft](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Setelah berhasil dibuat, Anda dapat mengakses studio yang Anda buat melalui [ai.azure.com](https://ai.azure.com/)

Di AI Foundry dapat ada beberapa proyek. Buat proyek di AI Foundry untuk persiapan.

Buat Microsoft Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. Men-deploy model Phi di Microsoft Foundry**

Klik opsi Explore dari proyek untuk masuk ke Model Catalog dan pilih Phi-3

Pilih Phi-3-mini-4k-instruct

Klik 'Deploy' untuk men-deploy model Phi-3-mini-4k-instruct

> [!NOTE]
>
> Anda dapat memilih daya komputasi saat men-deploy

## **3. Playground Chat Phi di Microsoft Foundry**

Pergi ke halaman deployment, pilih Playground, dan chat dengan Phi-3 dari Microsoft Foundry

## **4. Men-deploy Model dari Microsoft Foundry**

Untuk men-deploy model dari Azure Model Catalog, Anda dapat mengikuti langkah-langkah ini:

- Masuk ke Microsoft Foundry.
- Pilih model yang ingin Anda deploy dari katalog model Microsoft Foundry.
- Pada halaman Detail model, pilih Deploy lalu pilih Serverless API dengan Azure AI Content Safety.
- Pilih proyek tempat Anda ingin men-deploy model Anda. Untuk menggunakan penawaran Serverless API, workspace Anda harus berada di wilayah East US 2 atau Sweden Central. Anda dapat menyesuaikan Nama Deployment.
- Pada wizard deployment, pilih Pricing and terms untuk mempelajari harga dan ketentuan penggunaan.
- Pilih Deploy. Tunggu hingga deployment siap dan Anda dialihkan ke halaman Deployments.
- Pilih Open in playground untuk mulai berinteraksi dengan model.
- Anda dapat kembali ke halaman Deployments, pilih deployment, dan catat URL Target endpoint serta Secret Key, yang dapat Anda gunakan untuk memanggil deployment dan menghasilkan completions.
- Anda selalu dapat menemukan detail endpoint, URL, dan kunci akses dengan menavigasi ke tab Build dan memilih Deployments dari bagian Components.

> [!NOTE]
> Harap dicatat bahwa akun Anda harus memiliki izin peran Azure AI Developer pada Resource Group untuk melakukan langkah-langkah ini.

## **5. Menggunakan Phi API di Microsoft Foundry**

Anda dapat mengakses https://{Your project name}.region.inference.ml.azure.com/swagger.json melalui Postman GET dan menggabungkannya dengan Key untuk mempelajari antarmuka yang disediakan

Anda dapat memperoleh parameter permintaan dengan sangat mudah, serta parameter responsnya.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->