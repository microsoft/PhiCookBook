# Selamat datang di Ekstensi VS Code Anda

## Apa saja isi folder ini

* Folder ini berisi semua file yang diperlukan untuk ekstensi Anda.
* `package.json` - ini adalah file manifest tempat Anda mendeklarasikan ekstensi dan perintah Anda.
  * Plugin contoh mendaftarkan sebuah perintah dan mendefinisikan judul serta nama perintahnya. Dengan informasi ini, VS Code dapat menampilkan perintah di command palette. Plugin belum perlu dimuat saat itu.
* `src/extension.ts` - ini adalah file utama tempat Anda akan mengimplementasikan perintah Anda.
  * File ini mengekspor satu fungsi, `activate`, yang dipanggil pertama kali saat ekstensi Anda diaktifkan (dalam kasus ini dengan menjalankan perintah). Di dalam fungsi `activate` kita memanggil `registerCommand`.
  * Kita mengoper fungsi yang berisi implementasi perintah sebagai parameter kedua ke `registerCommand`.

## Pengaturan

* pasang ekstensi yang direkomendasikan (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, dan dbaeumer.vscode-eslint)

## Mulai langsung

* Tekan `F5` untuk membuka jendela baru dengan ekstensi Anda dimuat.
* Jalankan perintah Anda dari command palette dengan menekan (`Ctrl+Shift+P` atau `Cmd+Shift+P` di Mac) dan ketik `Hello World`.
* Pasang breakpoint di kode Anda di dalam `src/extension.ts` untuk melakukan debug ekstensi.
* Temukan output dari ekstensi Anda di debug console.

## Membuat perubahan

* Anda bisa meluncurkan ulang ekstensi dari toolbar debug setelah mengubah kode di `src/extension.ts`.
* Anda juga bisa memuat ulang (`Ctrl+R` atau `Cmd+R` di Mac) jendela VS Code dengan ekstensi Anda untuk memuat perubahan.

## Jelajahi API

* Anda bisa membuka seluruh API kami dengan membuka file `node_modules/@types/vscode/index.d.ts`.

## Menjalankan tes

* Pasang [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Jalankan tugas "watch" melalui perintah **Tasks: Run Task**. Pastikan ini berjalan, atau tes mungkin tidak terdeteksi.
* Buka tampilan Testing dari activity bar dan klik tombol "Run Test", atau gunakan hotkey `Ctrl/Cmd + ; A`
* Lihat hasil tes di tampilan Test Results.
* Buat perubahan pada `src/test/extension.test.ts` atau buat file tes baru di dalam folder `test`.
  * Test runner yang disediakan hanya akan mempertimbangkan file yang sesuai pola nama `**.test.ts`.
  * Anda bisa membuat folder di dalam folder `test` untuk mengatur tes sesuai keinginan.

## Melangkah lebih jauh

* Kurangi ukuran ekstensi dan tingkatkan waktu startup dengan [menggabungkan ekstensi Anda](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Publikasikan ekstensi Anda](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) di marketplace ekstensi VS Code.
* Otomatiskan build dengan mengatur [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.