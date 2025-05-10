<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a1e48b628022485aac989c9f733e792",
  "translation_date": "2025-05-09T20:13:30+00:00",
  "source_file": "md/02.QuickStart/AzureAIFoundry_QuickStart.md",
  "language_code": "id"
}
-->
# **Menggunakan Phi-3 di Azure AI Foundry**

Dengan perkembangan Generative AI, kami berharap dapat menggunakan platform terpadu untuk mengelola berbagai LLM dan SLM, integrasi data perusahaan, operasi fine-tuning/RAG, serta evaluasi berbagai bisnis perusahaan setelah mengintegrasikan LLM dan SLM, dll., sehingga aplikasi generative AI dapat diimplementasikan dengan lebih baik. [Azure AI Foundry](https://ai.azure.com) adalah platform aplikasi generative AI tingkat perusahaan.

![aistudo](../../../../translated_images/aifoundry_home.ffa4fe13d11f26171097f8666a1db96ac0979ffa1adde80374c60d1136c7e1de.id.png)

Dengan Azure AI Foundry, Anda dapat mengevaluasi respons model bahasa besar (LLM) dan mengatur komponen aplikasi prompt dengan prompt flow untuk kinerja yang lebih baik. Platform ini memudahkan skalabilitas untuk mengubah bukti konsep menjadi produksi penuh dengan mudah. Pemantauan dan penyempurnaan berkelanjutan mendukung keberhasilan jangka panjang.

Kita dapat dengan cepat menerapkan model Phi-3 di Azure AI Foundry melalui langkah-langkah sederhana, lalu menggunakan Azure AI Foundry untuk menyelesaikan Playground/Chat, Fine-tuning, evaluasi, dan pekerjaan terkait Phi-3 lainnya.

## **1. Persiapan**

Jika Anda sudah memiliki [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) terpasang di mesin Anda, menggunakan template ini semudah menjalankan perintah ini di direktori baru.

## Pembuatan Manual

Membuat proyek dan hub Microsoft Azure AI Foundry adalah cara yang bagus untuk mengatur dan mengelola pekerjaan AI Anda. Berikut panduan langkah demi langkah untuk memulai:

### Membuat Proyek di Azure AI Foundry

1. **Buka Azure AI Foundry**: Masuk ke portal Azure AI Foundry.
2. **Buat Proyek**:
   - Jika Anda sedang berada di dalam proyek, pilih "Azure AI Foundry" di kiri atas halaman untuk kembali ke halaman Beranda.
   - Pilih "+ Create project".
   - Masukkan nama untuk proyek tersebut.
   - Jika Anda memiliki hub, hub tersebut akan dipilih secara default. Jika Anda memiliki akses ke lebih dari satu hub, Anda dapat memilih yang lain dari dropdown. Jika ingin membuat hub baru, pilih "Create new hub" dan masukkan nama.
   - Pilih "Create".

### Membuat Hub di Azure AI Foundry

1. **Buka Azure AI Foundry**: Masuk dengan akun Azure Anda.
2. **Buat Hub**:
   - Pilih Management center dari menu sebelah kiri.
   - Pilih "All resources", lalu panah bawah di samping "+ New project" dan pilih "+ New hub".
   - Di dialog "Create a new hub", masukkan nama hub Anda (misalnya contoso-hub) dan sesuaikan bidang lain sesuai keinginan.
   - Pilih "Next", tinjau informasinya, lalu pilih "Create".

Untuk instruksi lebih rinci, Anda dapat merujuk ke [dokumentasi resmi Microsoft](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Setelah berhasil dibuat, Anda dapat mengakses studio yang dibuat melalui [ai.azure.com](https://ai.azure.com/)

Di satu AI Foundry bisa ada beberapa proyek. Buat proyek di AI Foundry sebagai persiapan.

Buat Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. Menerapkan model Phi di Azure AI Foundry**

Klik opsi Explore pada proyek untuk masuk ke Model Catalog dan pilih Phi-3

Pilih Phi-3-mini-4k-instruct

Klik 'Deploy' untuk menerapkan model Phi-3-mini-4k-instruct

> [!NOTE]
>
> Anda dapat memilih daya komputasi saat menerapkan

## **3. Playground Chat Phi di Azure AI Foundry**

Buka halaman deployment, pilih Playground, dan chat dengan Phi-3 di Azure AI Foundry

## **4. Menerapkan Model dari Azure AI Foundry**

Untuk menerapkan model dari Azure Model Catalog, Anda dapat mengikuti langkah-langkah berikut:

- Masuk ke Azure AI Foundry.
- Pilih model yang ingin Anda terapkan dari katalog model Azure AI Foundry.
- Di halaman Detail model, pilih Deploy lalu pilih Serverless API dengan Azure AI Content Safety.
- Pilih proyek tempat Anda ingin menerapkan model. Untuk menggunakan penawaran Serverless API, workspace Anda harus berada di wilayah East US 2 atau Sweden Central. Anda dapat menyesuaikan nama Deployment.
- Pada wizard deployment, pilih Pricing and terms untuk mempelajari harga dan ketentuan penggunaan.
- Pilih Deploy. Tunggu hingga deployment siap dan Anda diarahkan ke halaman Deployments.
- Pilih Open in playground untuk mulai berinteraksi dengan model.
- Anda dapat kembali ke halaman Deployments, pilih deployment, dan catat Target URL endpoint serta Secret Key, yang dapat Anda gunakan untuk memanggil deployment dan menghasilkan output.
- Anda selalu dapat menemukan detail endpoint, URL, dan kunci akses dengan membuka tab Build dan memilih Deployments dari bagian Components.

> [!NOTE]
> Harap dicatat bahwa akun Anda harus memiliki izin peran Azure AI Developer pada Resource Group untuk melakukan langkah-langkah ini.

## **5. Menggunakan Phi API di Azure AI Foundry**

Anda dapat mengakses https://{Your project name}.region.inference.ml.azure.com/swagger.json melalui Postman GET dan menggabungkannya dengan Key untuk mempelajari antarmuka yang disediakan

Anda dapat dengan mudah mendapatkan parameter permintaan, serta parameter respons.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.