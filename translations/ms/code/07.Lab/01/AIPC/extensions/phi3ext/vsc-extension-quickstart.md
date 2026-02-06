# Selamat datang ke Sambungan VS Code anda

## Apa yang ada dalam folder

* Folder ini mengandungi semua fail yang diperlukan untuk sambungan anda.
* `package.json` - ini adalah fail manifest di mana anda mengisytiharkan sambungan dan perintah anda.
  * Plugin contoh mendaftar satu perintah dan menetapkan tajuk serta nama perintahnya. Dengan maklumat ini, VS Code boleh memaparkan perintah dalam palet perintah. Ia belum perlu memuatkan plugin.
* `src/extension.ts` - ini adalah fail utama di mana anda akan menyediakan pelaksanaan perintah anda.
  * Fail ini mengeksport satu fungsi, `activate`, yang dipanggil kali pertama sambungan anda diaktifkan (dalam kes ini dengan menjalankan perintah). Di dalam fungsi `activate` kita memanggil `registerCommand`.
  * Kita menghantar fungsi yang mengandungi pelaksanaan perintah sebagai parameter kedua kepada `registerCommand`.

## Persediaan

* pasang sambungan yang disyorkan (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, dan dbaeumer.vscode-eslint)

## Mulakan dengan segera

* Tekan `F5` untuk membuka tetingkap baru dengan sambungan anda dimuatkan.
* Jalankan perintah anda dari palet perintah dengan menekan (`Ctrl+Shift+P` atau `Cmd+Shift+P` pada Mac) dan taip `Hello World`.
* Tetapkan titik henti dalam kod anda di dalam `src/extension.ts` untuk debug sambungan anda.
* Cari output dari sambungan anda dalam konsol debug.

## Buat perubahan

* Anda boleh melancarkan semula sambungan dari bar alat debug selepas menukar kod dalam `src/extension.ts`.
* Anda juga boleh memuat semula (`Ctrl+R` atau `Cmd+R` pada Mac) tetingkap VS Code dengan sambungan anda untuk memuatkan perubahan anda.

## Terokai API

* Anda boleh membuka set penuh API kami apabila anda membuka fail `node_modules/@types/vscode/index.d.ts`.

## Jalankan ujian

* Pasang [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Jalankan tugas "watch" melalui perintah **Tasks: Run Task**. Pastikan ia berjalan, jika tidak ujian mungkin tidak ditemui.
* Buka paparan Testing dari bar aktiviti dan klik butang "Run Test", atau gunakan kekunci pintas `Ctrl/Cmd + ; A`
* Lihat output keputusan ujian dalam paparan Test Results.
* Buat perubahan pada `src/test/extension.test.ts` atau cipta fail ujian baru dalam folder `test`.
  * Test runner yang disediakan hanya akan mempertimbangkan fail yang sepadan dengan corak nama `**.test.ts`.
  * Anda boleh mencipta folder dalam folder `test` untuk menyusun ujian anda mengikut cara yang anda mahu.

## Terokai lebih jauh

* Kurangkan saiz sambungan dan tingkatkan masa permulaan dengan [menggabungkan sambungan anda](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Terbitkan sambungan anda](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) di pasaran sambungan VS Code.
* Automatikkan binaan dengan menyediakan [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.