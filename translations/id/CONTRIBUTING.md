<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-07-16T14:43:56+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "id"
}
-->
# Kontribusi

Proyek ini menyambut kontribusi dan saran. Sebagian besar kontribusi mengharuskan Anda menyetujui
Contributor License Agreement (CLA) yang menyatakan bahwa Anda memiliki hak, dan memang memberikan,
hak kepada kami untuk menggunakan kontribusi Anda. Untuk detailnya, kunjungi [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Saat Anda mengirimkan pull request, bot CLA akan secara otomatis menentukan apakah Anda perlu menyediakan
CLA dan menandai PR dengan tepat (misalnya, pemeriksaan status, komentar). Cukup ikuti instruksi
yang diberikan oleh bot. Anda hanya perlu melakukan ini sekali untuk semua repositori yang menggunakan CLA kami.

## Kode Etik

Proyek ini telah mengadopsi [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Untuk informasi lebih lanjut, baca [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) atau hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) jika ada pertanyaan atau komentar tambahan.

## Perhatian dalam Membuat Isu

Mohon jangan membuka isu GitHub untuk pertanyaan dukungan umum karena daftar GitHub sebaiknya digunakan untuk permintaan fitur dan laporan bug. Dengan cara ini, kami dapat lebih mudah melacak isu atau bug yang sebenarnya dari kode dan memisahkan diskusi umum dari kode yang sebenarnya.

## Cara Berkontribusi

### Panduan Pull Request

Saat mengirimkan pull request (PR) ke repositori Phi-3 CookBook, harap gunakan panduan berikut:

- **Fork Repositori**: Selalu fork repositori ke akun Anda sendiri sebelum melakukan modifikasi.

- **Pisahkan pull request (PR)**:
  - Kirim setiap jenis perubahan dalam pull request terpisah. Misalnya, perbaikan bug dan pembaruan dokumentasi harus dikirim dalam PR yang berbeda.
  - Perbaikan typo dan pembaruan dokumentasi minor dapat digabungkan dalam satu PR jika sesuai.

- **Tangani konflik merge**: Jika pull request Anda menunjukkan konflik merge, perbarui cabang `main` lokal Anda agar sesuai dengan repositori utama sebelum melakukan modifikasi.

- **Pengiriman terjemahan**: Saat mengirimkan PR terjemahan, pastikan folder terjemahan mencakup terjemahan untuk semua file di folder asli.

### Panduan Penulisan

Untuk memastikan konsistensi di semua dokumen, harap gunakan panduan berikut:

- **Format URL**: Bungkus semua URL dengan tanda kurung siku diikuti tanda kurung biasa, tanpa spasi tambahan di sekitar atau di dalamnya. Contoh: `[example](https://www.microsoft.com)`.

- **Tautan relatif**: Gunakan `./` untuk tautan relatif yang mengarah ke file atau folder di direktori saat ini, dan `../` untuk yang ada di direktori induk. Contoh: `[example](../../path/to/file)` atau `[example](../../../path/to/file)`.

- **Tidak menggunakan lokal spesifik negara**: Pastikan tautan Anda tidak menyertakan lokal spesifik negara. Contoh, hindari `/en-us/` atau `/en/`.

- **Penyimpanan gambar**: Simpan semua gambar di folder `./imgs`.

- **Penamaan gambar yang deskriptif**: Beri nama gambar dengan deskriptif menggunakan karakter bahasa Inggris, angka, dan tanda hubung. Contoh: `example-image.jpg`.

## Alur Kerja GitHub

Saat Anda mengirimkan pull request, alur kerja berikut akan dijalankan untuk memvalidasi perubahan. Ikuti instruksi di bawah ini agar pull request Anda lolos pemeriksaan alur kerja:

- [Periksa Jalur Relatif yang Rusak](../..)
- [Periksa URL Tidak Mengandung Lokal](../..)

### Periksa Jalur Relatif yang Rusak

Alur kerja ini memastikan semua jalur relatif dalam file Anda benar.

1. Untuk memastikan tautan Anda berfungsi dengan baik, lakukan tugas berikut menggunakan VS Code:
    - Arahkan kursor ke tautan mana pun dalam file Anda.
    - Tekan **Ctrl + Klik** untuk membuka tautan tersebut.
    - Jika Anda mengklik tautan dan tidak berfungsi secara lokal, ini akan memicu alur kerja dan tidak akan berfungsi di GitHub.

1. Untuk memperbaiki masalah ini, lakukan tugas berikut menggunakan saran jalur yang diberikan oleh VS Code:
    - Ketik `./` atau `../`.
    - VS Code akan menampilkan pilihan berdasarkan apa yang Anda ketik.
    - Ikuti jalur dengan mengklik file atau folder yang diinginkan untuk memastikan jalur Anda benar.

Setelah Anda menambahkan jalur relatif yang benar, simpan dan dorong perubahan Anda.

### Periksa URL Tidak Mengandung Lokal

Alur kerja ini memastikan bahwa URL web tidak mengandung lokal spesifik negara. Karena repositori ini dapat diakses secara global, penting untuk memastikan URL tidak mengandung lokal negara Anda.

1. Untuk memeriksa bahwa URL Anda tidak mengandung lokal negara, lakukan tugas berikut:

    - Periksa teks seperti `/en-us/`, `/en/`, atau lokal bahasa lain dalam URL.
    - Jika tidak ada dalam URL Anda, maka Anda akan lolos pemeriksaan ini.

1. Untuk memperbaiki masalah ini, lakukan tugas berikut:
    - Buka file yang ditandai oleh alur kerja.
    - Hapus lokal negara dari URL.

Setelah Anda menghapus lokal negara, simpan dan dorong perubahan Anda.

### Periksa URL Rusak

Alur kerja ini memastikan bahwa setiap URL web dalam file Anda berfungsi dan mengembalikan kode status 200.

1. Untuk memeriksa bahwa URL Anda berfungsi dengan benar, lakukan tugas berikut:
    - Periksa status URL dalam file Anda.

2. Untuk memperbaiki URL yang rusak, lakukan tugas berikut:
    - Buka file yang berisi URL rusak.
    - Perbarui URL ke yang benar.

Setelah Anda memperbaiki URL, simpan dan dorong perubahan Anda.

> [!NOTE]
>
> Ada kemungkinan pemeriksaan URL gagal meskipun tautan dapat diakses. Hal ini bisa terjadi karena beberapa alasan, termasuk:
>
> - **Pembatasan jaringan:** Server GitHub actions mungkin memiliki pembatasan jaringan yang mencegah akses ke URL tertentu.
> - **Masalah timeout:** URL yang membutuhkan waktu lama untuk merespons dapat memicu kesalahan timeout dalam alur kerja.
> - **Masalah server sementara:** Downtime atau pemeliharaan server sesekali dapat membuat URL tidak tersedia sementara saat validasi.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.