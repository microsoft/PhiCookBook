Demo ini mempamerkan cara menggunakan model terlatih untuk menjana kod Python berdasarkan imej dan arahan teks.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Berikut adalah penjelasan langkah demi langkah:

1. **Imports and Setup**:
   - Pustaka dan modul yang diperlukan diimport, termasuk `requests`, `PIL` untuk pemprosesan imej, dan `transformers` untuk mengendalikan model dan pemprosesan.

2. **Loading and Displaying the Image**:
   - Fail imej (`demo.png`) dibuka menggunakan pustaka `PIL` dan dipaparkan.

3. **Defining the Prompt**:
   - Satu mesej dibuat yang merangkumi imej dan permintaan untuk menjana kod Python bagi memproses imej tersebut dan menyimpannya menggunakan `plt` (matplotlib).

4. **Loading the Processor**:
   - `AutoProcessor` dimuatkan dari model terlatih yang ditentukan oleh direktori `out_dir`. Pemproses ini akan mengendalikan input teks dan imej.

5. **Creating the Prompt**:
   - Kaedah `apply_chat_template` digunakan untuk memformat mesej menjadi arahan yang sesuai untuk model.

6. **Processing the Inputs**:
   - Arahan dan imej diproses menjadi tensor yang boleh difahami oleh model.

7. **Setting Generation Arguments**:
   - Argumen untuk proses penjanaan model ditetapkan, termasuk bilangan maksimum token baru yang akan dijana dan sama ada untuk membuat sampel output.

8. **Generating the Code**:
   - Model menjana kod Python berdasarkan input dan argumen penjanaan. `TextStreamer` digunakan untuk mengendalikan output, dengan mengabaikan arahan dan token khas.

9. **Output**:
   - Kod yang dijana dicetak, yang sepatutnya mengandungi kod Python untuk memproses imej dan menyimpannya seperti yang ditetapkan dalam arahan.

Demo ini menunjukkan cara memanfaatkan model terlatih menggunakan OpenVino untuk menjana kod secara dinamik berdasarkan input pengguna dan imej.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.