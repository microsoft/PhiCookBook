<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-09T04:57:46+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "id"
}
-->
# Selamat datang di Ekstensi VS Code Anda

## Apa saja yang ada di folder

* Folder ini berisi semua file yang diperlukan untuk ekstensi Anda.
* `package.json` - ini adalah file manifest di mana Anda mendeklarasikan ekstensi dan perintah Anda.
  * Plugin contoh mendaftarkan sebuah perintah dan menentukan judul serta nama perintahnya. Dengan informasi ini VS Code dapat menampilkan perintah di command palette. Plugin belum perlu dimuat saat ini.
* `src/extension.ts` - ini adalah file utama di mana Anda akan menyediakan implementasi perintah Anda.
  * File ini mengekspor satu fungsi, `activate`, yang dipanggil pertama kali saat ekstensi Anda diaktifkan (dalam kasus ini dengan menjalankan perintah). Di dalam fungsi `activate` kita memanggil `registerCommand`.
  * Kita mengoper fungsi yang berisi implementasi perintah sebagai parameter kedua ke `registerCommand`.

## Pengaturan

* pasang ekstensi yang direkomendasikan (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, dan dbaeumer.vscode-eslint)


## Mulai langsung dan berjalan

* Tekan `F5` untuk membuka jendela baru dengan ekstensi Anda yang sudah dimuat.
* Jalankan perintah Anda dari command palette dengan menekan (`Ctrl+Shift+P` atau `Cmd+Shift+P` di Mac) dan ketik `Hello World`.
* Pasang breakpoint di kode Anda di dalam `src/extension.ts` untuk melakukan debug ekstensi Anda.
* Temukan output dari ekstensi Anda di debug console.

## Membuat perubahan

* Anda dapat meluncurkan ulang ekstensi dari toolbar debug setelah mengubah kode di `src/extension.ts`.
* Anda juga dapat memuat ulang (`Ctrl+R` atau `Cmd+R` di Mac) jendela VS Code dengan ekstensi Anda untuk memuat perubahan.

## Jelajahi API

* Anda dapat membuka seluruh kumpulan API kami saat membuka file `node_modules/@types/vscode/index.d.ts`.

## Menjalankan pengujian

* Pasang [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Jalankan tugas "watch" melalui perintah **Tasks: Run Task**. Pastikan ini berjalan, jika tidak pengujian mungkin tidak terdeteksi.
* Buka tampilan Testing dari activity bar dan klik tombol Run Test, atau gunakan hotkey `Ctrl/Cmd + ; A`
* Lihat hasil output pengujian di tampilan Test Results.
* Lakukan perubahan pada `src/test/extension.test.ts` atau buat file pengujian baru di dalam folder `test`.
  * Test runner yang disediakan hanya akan mempertimbangkan file yang sesuai pola nama `**.test.ts`.
  * Anda dapat membuat folder di dalam folder `test` untuk mengatur pengujian sesuai keinginan Anda.

## Melangkah lebih jauh

* Kurangi ukuran ekstensi dan tingkatkan waktu startup dengan [menggabungkan ekstensi Anda](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Terbitkan ekstensi Anda](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) di marketplace ekstensi VS Code.
* Otomatiskan proses build dengan mengatur [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.