<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:40:31+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "id"
}
-->
# Selamat datang di Ekstensi VS Code Anda

## Apa saja isi folder ini

* Folder ini berisi semua file yang diperlukan untuk ekstensi Anda.
* `package.json` - ini adalah file manifest tempat Anda mendeklarasikan ekstensi dan perintah Anda.
  * Plugin contoh mendaftarkan sebuah perintah dan menentukan judul serta nama perintahnya. Dengan informasi ini, VS Code dapat menampilkan perintah di palet perintah. Plugin belum perlu dimuat saat ini.
* `src/extension.ts` - ini adalah file utama tempat Anda akan menyediakan implementasi perintah Anda.
  * File ini mengekspor satu fungsi, `activate`, yang dipanggil pertama kali saat ekstensi Anda diaktifkan (dalam kasus ini dengan menjalankan perintah). Di dalam fungsi `activate` kita memanggil `registerCommand`.
  * Kita mengoper fungsi yang berisi implementasi perintah sebagai parameter kedua ke `registerCommand`.

## Pengaturan

* pasang ekstensi yang direkomendasikan (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, dan dbaeumer.vscode-eslint)


## Mulai dan jalankan langsung

* Tekan `F5` untuk membuka jendela baru dengan ekstensi Anda dimuat.
* Jalankan perintah Anda dari palet perintah dengan menekan (`Ctrl+Shift+P` atau `Cmd+Shift+P` di Mac) dan ketik `Hello World`.
* Pasang breakpoint di kode Anda dalam `src/extension.ts` untuk melakukan debug ekstensi Anda.
* Temukan output dari ekstensi Anda di konsol debug.

## Membuat perubahan

* Anda bisa meluncurkan ulang ekstensi dari toolbar debug setelah mengubah kode di `src/extension.ts`.
* Anda juga bisa memuat ulang (`Ctrl+R` atau `Cmd+R` di Mac) jendela VS Code dengan ekstensi Anda untuk memuat perubahan.

## Jelajahi API

* Anda dapat membuka kumpulan lengkap API kami saat membuka file `node_modules/@types/vscode/index.d.ts`.

## Menjalankan tes

* Pasang [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Jalankan tugas "watch" melalui perintah **Tasks: Run Task**. Pastikan ini berjalan, jika tidak tes mungkin tidak terdeteksi.
* Buka tampilan Testing dari activity bar dan klik tombol Run Test, atau gunakan tombol pintas `Ctrl/Cmd + ; A`
* Lihat hasil output tes di tampilan Test Results.
* Buat perubahan pada `src/test/extension.test.ts` atau buat file tes baru di dalam folder `test`.
  * Test runner yang disediakan hanya akan mempertimbangkan file yang sesuai pola nama `**.test.ts`.
  * Anda bisa membuat folder di dalam folder `test` untuk mengatur tes sesuai keinginan Anda.

## Melangkah lebih jauh

* Kurangi ukuran ekstensi dan tingkatkan waktu startup dengan [menggabungkan ekstensi Anda](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publikasikan ekstensi Anda](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) di marketplace ekstensi VS Code.
* Otomatiskan build dengan mengatur [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi yang penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.