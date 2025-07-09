<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-07-09T18:37:18+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ms"
}
-->
# Menyumbang

Projek ini mengalu-alukan sumbangan dan cadangan. Kebanyakan sumbangan memerlukan anda bersetuju dengan
Perjanjian Lesen Penyumbang (CLA) yang menyatakan bahawa anda mempunyai hak untuk, dan benar-benar memberikan kami
hak untuk menggunakan sumbangan anda. Untuk maklumat lanjut, lawati [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Apabila anda menghantar permintaan tarik, bot CLA akan secara automatik menentukan sama ada anda perlu menyediakan
CLA dan menghias PR dengan sewajarnya (contohnya, pemeriksaan status, komen). Ikuti sahaja arahan
yang diberikan oleh bot. Anda hanya perlu melakukan ini sekali sahaja untuk semua repositori yang menggunakan CLA kami.

## Kod Etika

Projek ini telah mengamalkan [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Untuk maklumat lanjut, baca [Soalan Lazim Kod Etika](https://opensource.microsoft.com/codeofconduct/faq/) atau hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) untuk sebarang soalan atau komen tambahan.

## Amaran untuk Membuat Isu

Sila jangan buka isu GitHub untuk soalan sokongan umum kerana senarai GitHub sepatutnya digunakan untuk permintaan ciri dan laporan pepijat. Dengan cara ini, kami dapat mengesan isu atau pepijat sebenar dari kod dengan lebih mudah dan memisahkan perbincangan umum daripada kod sebenar.

## Cara Menyumbang

### Garis Panduan Permintaan Tarik

Apabila menghantar permintaan tarik (PR) ke repositori Phi-3 CookBook, sila gunakan garis panduan berikut:

- **Fork Repositori**: Sentiasa fork repositori ke akaun anda sendiri sebelum membuat pengubahsuaian.

- **Pisahkan permintaan tarik (PR)**:
  - Hantar setiap jenis perubahan dalam permintaan tarik yang berasingan. Contohnya, pembetulan pepijat dan kemas kini dokumentasi harus dihantar dalam PR yang berasingan.
  - Pembetulan ejaan dan kemas kini dokumentasi kecil boleh digabungkan dalam satu PR jika sesuai.

- **Tangani konflik penggabungan**: Jika permintaan tarik anda menunjukkan konflik penggabungan, kemas kini cawangan `main` tempatan anda supaya selari dengan repositori utama sebelum membuat pengubahsuaian.

- **Penyerahan terjemahan**: Apabila menghantar PR terjemahan, pastikan folder terjemahan merangkumi terjemahan untuk semua fail dalam folder asal.

### Garis Panduan Penulisan

Untuk memastikan konsistensi di semua dokumen, sila gunakan garis panduan berikut:

- **Format URL**: Bungkus semua URL dalam kurungan siku diikuti dengan kurungan bulat, tanpa ruang tambahan di sekeliling atau di dalamnya. Contohnya: `[example](https://www.microsoft.com)`.

- **Pautan relatif**: Gunakan `./` untuk pautan relatif yang menunjuk ke fail atau folder dalam direktori semasa, dan `../` untuk yang berada dalam direktori induk. Contohnya: `[example](../../path/to/file)` atau `[example](../../../path/to/file)`.

- **Bukan lokal khusus negara**: Pastikan pautan anda tidak mengandungi lokal khusus negara. Contohnya, elakkan `/en-us/` atau `/en/`.

- **Penyimpanan imej**: Simpan semua imej dalam folder `./imgs`.

- **Nama imej yang deskriptif**: Namakan imej dengan deskriptif menggunakan aksara Inggeris, nombor, dan tanda sempang. Contohnya: `example-image.jpg`.

## Aliran Kerja GitHub

Apabila anda menghantar permintaan tarik, aliran kerja berikut akan dicetuskan untuk mengesahkan perubahan. Ikuti arahan di bawah untuk memastikan permintaan tarik anda lulus pemeriksaan aliran kerja:

- [Periksa Laluan Relatif Rosak](../..)
- [Periksa URL Tidak Mengandungi Lokal](../..)

### Periksa Laluan Relatif Rosak

Aliran kerja ini memastikan semua laluan relatif dalam fail anda adalah betul.

1. Untuk memastikan pautan anda berfungsi dengan betul, lakukan tugas berikut menggunakan VS Code:
    - Arahkan kursor ke atas mana-mana pautan dalam fail anda.
    - Tekan **Ctrl + Klik** untuk pergi ke pautan tersebut.
    - Jika anda klik pada pautan dan ia tidak berfungsi secara tempatan, ia akan mencetuskan aliran kerja dan tidak berfungsi di GitHub.

1. Untuk membetulkan isu ini, lakukan tugas berikut menggunakan cadangan laluan yang disediakan oleh VS Code:
    - Taip `./` atau `../`.
    - VS Code akan menggesa anda memilih daripada pilihan yang tersedia berdasarkan apa yang anda taip.
    - Ikuti laluan dengan mengklik fail atau folder yang dikehendaki untuk memastikan laluan anda betul.

Setelah anda menambah laluan relatif yang betul, simpan dan tolak perubahan anda.

### Periksa URL Tidak Mengandungi Lokal

Aliran kerja ini memastikan mana-mana URL web tidak mengandungi lokal khusus negara. Oleh kerana repositori ini boleh diakses secara global, adalah penting untuk memastikan URL tidak mengandungi lokal negara anda.

1. Untuk mengesahkan URL anda tidak mengandungi lokal negara, lakukan tugas berikut:

    - Periksa teks seperti `/en-us/`, `/en/`, atau mana-mana lokal bahasa lain dalam URL.
    - Jika ini tidak terdapat dalam URL anda, maka anda akan lulus pemeriksaan ini.

1. Untuk membetulkan isu ini, lakukan tugas berikut:
    - Buka laluan fail yang diserlahkan oleh aliran kerja.
    - Buang lokal negara daripada URL.

Setelah anda membuang lokal negara, simpan dan tolak perubahan anda.

### Periksa URL Rosak

Aliran kerja ini memastikan mana-mana URL web dalam fail anda berfungsi dan mengembalikan kod status 200.

1. Untuk mengesahkan URL anda berfungsi dengan betul, lakukan tugas berikut:
    - Semak status URL dalam fail anda.

2. Untuk membetulkan URL yang rosak, lakukan tugas berikut:
    - Buka fail yang mengandungi URL rosak.
    - Kemas kini URL kepada yang betul.

Setelah anda membetulkan URL, simpan dan tolak perubahan anda.

> [!NOTE]
>
> Mungkin terdapat kes di mana pemeriksaan URL gagal walaupun pautan boleh diakses. Ini boleh berlaku atas beberapa sebab, termasuk:
>
> - **Sekatan rangkaian:** Pelayan tindakan GitHub mungkin mempunyai sekatan rangkaian yang menghalang akses ke URL tertentu.
> - **Isu masa tamat:** URL yang mengambil masa terlalu lama untuk bertindak balas mungkin mencetuskan ralat masa tamat dalam aliran kerja.
> - **Isu pelayan sementara:** Waktu henti pelayan atau penyelenggaraan sementara boleh menyebabkan URL tidak tersedia buat sementara waktu semasa pengesahan.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.