<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-05-09T20:01:26+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "id"
}
-->
Demo ini menampilkan cara menggunakan model pretrained untuk menghasilkan kode Python berdasarkan gambar dan teks prompt.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Berikut penjelasan langkah demi langkah:

1. **Imports dan Setup**:
   - Library dan modul yang diperlukan diimpor, termasuk `requests`, `PIL` untuk pemrosesan gambar, dan `transformers` untuk menangani model dan pemrosesan.

2. **Memuat dan Menampilkan Gambar**:
   - File gambar (`demo.png`) dibuka menggunakan library `PIL` dan ditampilkan.

3. **Mendefinisikan Prompt**:
   - Sebuah pesan dibuat yang mencakup gambar dan permintaan untuk menghasilkan kode Python guna memproses gambar dan menyimpannya menggunakan `plt` (matplotlib).

4. **Memuat Processor**:
   - `AutoProcessor` dimuat dari model pretrained yang ditentukan oleh direktori `out_dir`. Processor ini akan menangani input teks dan gambar.

5. **Membuat Prompt**:
   - Metode `apply_chat_template` digunakan untuk memformat pesan menjadi prompt yang sesuai untuk model.

6. **Memproses Input**:
   - Prompt dan gambar diubah menjadi tensor yang dapat dipahami oleh model.

7. **Mengatur Argumen Generasi**:
   - Argumen untuk proses generasi model didefinisikan, termasuk jumlah maksimum token baru yang akan dihasilkan dan apakah output akan disampling.

8. **Menghasilkan Kode**:
   - Model menghasilkan kode Python berdasarkan input dan argumen generasi. `TextStreamer` digunakan untuk menangani output, melewati prompt dan token khusus.

9. **Output**:
   - Kode yang dihasilkan dicetak, yang seharusnya berisi kode Python untuk memproses gambar dan menyimpannya sesuai dengan prompt.

Demo ini menggambarkan cara memanfaatkan model pretrained menggunakan OpenVino untuk menghasilkan kode secara dinamis berdasarkan input pengguna dan gambar.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.