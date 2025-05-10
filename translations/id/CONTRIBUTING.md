<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:42:26+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "id"
}
-->
# Contributing

Proyek ini menyambut kontribusi dan saran. Sebagian besar kontribusi mengharuskan Anda menyetujui
Contributor License Agreement (CLA) yang menyatakan bahwa Anda memiliki hak, dan memang memberikan,
hak kepada kami untuk menggunakan kontribusi Anda. Untuk detailnya, kunjungi [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Saat Anda mengirimkan pull request, bot CLA akan secara otomatis menentukan apakah Anda perlu menyediakan
CLA dan menghias PR sesuai (misalnya, pemeriksaan status, komentar). Cukup ikuti instruksi
yang diberikan oleh bot. Anda hanya perlu melakukan ini sekali untuk semua repositori yang menggunakan CLA kami.

## Code of Conduct

Proyek ini telah mengadopsi [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Untuk informasi lebih lanjut, baca [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) atau hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) jika ada pertanyaan atau komentar tambahan.

## Cautions for creating issues

Harap jangan membuka isu GitHub untuk pertanyaan dukungan umum karena daftar GitHub sebaiknya digunakan untuk permintaan fitur dan laporan bug. Dengan cara ini, kami dapat lebih mudah melacak isu atau bug nyata dari kode dan menjaga diskusi umum terpisah dari kode sebenarnya.

## How to Contribute

### Pull Requests Guidelines

Saat mengirim pull request (PR) ke repositori Phi-3 CookBook, harap gunakan panduan berikut:

- **Fork Repository**: Selalu fork repositori ke akun Anda sendiri sebelum melakukan modifikasi.

- **Pisahkan pull request (PR)**:
  - Kirim setiap jenis perubahan dalam pull request terpisah. Misalnya, perbaikan bug dan pembaruan dokumentasi harus dikirim dalam PR yang berbeda.
  - Perbaikan typo dan pembaruan dokumentasi kecil dapat digabungkan dalam satu PR jika sesuai.

- **Tangani konflik merge**: Jika pull request Anda menunjukkan konflik merge, perbarui cabang lokal `main` Anda agar sesuai dengan repositori utama sebelum melakukan modifikasi.

- **Pengiriman terjemahan**: Saat mengirim PR terjemahan, pastikan folder terjemahan mencakup terjemahan untuk semua file dalam folder asli.

### Translation Guidelines

> [!IMPORTANT]
>
> Saat menerjemahkan teks dalam repositori ini, jangan gunakan terjemahan mesin. Hanya sukarelawan yang fasih dalam bahasa tersebut yang boleh menerjemahkan.

Jika Anda fasih dalam bahasa selain Inggris, Anda dapat membantu menerjemahkan konten. Ikuti langkah-langkah ini untuk memastikan kontribusi terjemahan Anda terintegrasi dengan baik, gunakan panduan berikut:

- **Buat folder terjemahan**: Navigasikan ke folder bagian yang sesuai dan buat folder terjemahan untuk bahasa yang Anda kontribusikan. Misalnya:
  - Untuk bagian pengantar: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Untuk bagian quick start: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Lanjutkan pola ini untuk bagian lainnya (03.Inference, 04.Finetuning, dll.)

- **Perbarui path relatif**: Saat menerjemahkan, sesuaikan struktur folder dengan menambahkan `../../` di awal path relatif dalam file markdown agar tautan berfungsi dengan benar. Misalnya, ubah:
  - Dari `(../../imgs/01/phi3aisafety.png)` menjadi `(../../../../imgs/01/phi3aisafety.png)`

- **Atur terjemahan Anda**: Setiap file terjemahan harus ditempatkan di folder terjemahan bagian yang sesuai. Misalnya, jika menerjemahkan bagian pengantar ke bahasa Spanyol, buatlah seperti:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Kirim PR lengkap**: Pastikan semua file terjemahan untuk satu bagian termasuk dalam satu PR. Kami tidak menerima terjemahan parsial untuk satu bagian. Saat mengirim PR terjemahan, pastikan folder terjemahan mencakup terjemahan untuk semua file di folder asli.

### Writing Guidelines

Untuk memastikan konsistensi di semua dokumen, harap gunakan panduan berikut:

- **Format URL**: Bungkus semua URL dalam tanda kurung siku diikuti dengan tanda kurung biasa, tanpa spasi tambahan di sekitar atau di dalamnya. Misalnya: `[example](https://www.microsoft.com)`.

- **Tautan relatif**: Gunakan `./` untuk tautan relatif yang mengarah ke file atau folder di direktori saat ini, dan `../` untuk yang ada di direktori induk. Misalnya: `[example](../../path/to/file)` atau `[example](../../../path/to/file)`.

- **Bukan lokal spesifik negara**: Pastikan tautan Anda tidak menyertakan lokal spesifik negara. Misalnya, hindari `/en-us/` atau `/en/`.

- **Penyimpanan gambar**: Simpan semua gambar di folder `./imgs`.

- **Penamaan gambar deskriptif**: Beri nama gambar secara deskriptif menggunakan karakter Inggris, angka, dan tanda hubung. Misalnya: `example-image.jpg`.

## GitHub Workflows

Saat Anda mengirim pull request, workflow berikut akan dijalankan untuk memvalidasi perubahan. Ikuti instruksi di bawah untuk memastikan pull request Anda lolos pemeriksaan workflow:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Workflow ini memastikan semua path relatif di file Anda benar.

1. Untuk memastikan tautan Anda berfungsi dengan baik, lakukan tugas berikut menggunakan VS Code:
    - Arahkan kursor ke tautan mana saja di file Anda.
    - Tekan **Ctrl + Klik** untuk menavigasi ke tautan tersebut.
    - Jika Anda mengklik tautan dan tidak berfungsi secara lokal, workflow akan dijalankan dan tidak akan bekerja di GitHub.

1. Untuk memperbaiki masalah ini, lakukan tugas berikut menggunakan saran path yang diberikan oleh VS Code:
    - Ketik `./` atau `../`.
    - VS Code akan meminta Anda memilih dari opsi yang tersedia berdasarkan apa yang Anda ketik.
    - Ikuti path dengan mengklik file atau folder yang diinginkan untuk memastikan path Anda benar.

Setelah Anda menambahkan path relatif yang benar, simpan dan dorong perubahan Anda.

### Check URLs Don't Have Locale

Workflow ini memastikan URL web tidak menyertakan lokal spesifik negara. Karena repositori ini dapat diakses secara global, penting memastikan URL tidak mengandung lokal negara Anda.

1. Untuk memverifikasi URL Anda tidak memiliki lokal negara, lakukan tugas berikut:

    - Periksa teks seperti `/en-us/`, `/en/`, atau lokal bahasa lain di URL.
    - Jika tidak ada di URL Anda, maka Anda akan lolos pemeriksaan ini.

1. Untuk memperbaiki masalah ini, lakukan tugas berikut:
    - Buka path file yang disorot oleh workflow.
    - Hapus lokal negara dari URL.

Setelah Anda menghapus lokal negara, simpan dan dorong perubahan Anda.

### Check Broken Urls

Workflow ini memastikan setiap URL web di file Anda berfungsi dan mengembalikan kode status 200.

1. Untuk memverifikasi URL Anda berfungsi dengan benar, lakukan tugas berikut:
    - Periksa status URL di file Anda.

2. Untuk memperbaiki URL yang rusak, lakukan tugas berikut:
    - Buka file yang berisi URL rusak.
    - Perbarui URL ke yang benar.

Setelah Anda memperbaiki URL, simpan dan dorong perubahan Anda.

> [!NOTE]
>
> Mungkin ada kasus di mana pemeriksaan URL gagal meskipun tautan dapat diakses. Hal ini dapat terjadi karena beberapa alasan, termasuk:
>
> - **Pembatasan jaringan:** Server GitHub actions mungkin memiliki pembatasan jaringan yang mencegah akses ke URL tertentu.
> - **Masalah timeout:** URL yang membutuhkan waktu lama untuk merespons dapat memicu error timeout di workflow.
> - **Masalah server sementara:** Kadang-kadang server sedang down atau dalam pemeliharaan sehingga URL sementara tidak tersedia saat validasi.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.