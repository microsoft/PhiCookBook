<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-09T18:32:55+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "id"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot dengan Whisper

## Ikhtisar

Interactive Phi 3 Mini 4K Instruct Chatbot adalah alat yang memungkinkan pengguna berinteraksi dengan demo Microsoft Phi 3 Mini 4K instruct menggunakan input teks atau audio. Chatbot ini dapat digunakan untuk berbagai tugas, seperti penerjemahan, pembaruan cuaca, dan pengumpulan informasi umum.

### Memulai

Untuk menggunakan chatbot ini, cukup ikuti petunjuk berikut:

1. Buka [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Di jendela utama notebook, Anda akan melihat antarmuka chatbox dengan kotak input teks dan tombol "Send".
3. Untuk menggunakan chatbot berbasis teks, ketik pesan Anda di kotak input teks dan klik tombol "Send". Chatbot akan merespons dengan file audio yang dapat diputar langsung dari dalam notebook.

**Note**: Alat ini membutuhkan GPU dan akses ke model Microsoft Phi-3 dan OpenAI Whisper, yang digunakan untuk pengenalan suara dan penerjemahan.

### Persyaratan GPU

Untuk menjalankan demo ini Anda memerlukan memori GPU sebesar 12GB.

Kebutuhan memori untuk menjalankan demo **Microsoft-Phi-3-Mini-4K instruct** pada GPU akan bergantung pada beberapa faktor, seperti ukuran data input (audio atau teks), bahasa yang digunakan untuk penerjemahan, kecepatan model, dan memori yang tersedia di GPU.

Secara umum, model Whisper dirancang untuk dijalankan di GPU. Jumlah minimum memori GPU yang direkomendasikan untuk menjalankan model Whisper adalah 8 GB, namun dapat menangani memori yang lebih besar jika diperlukan.

Penting untuk dicatat bahwa menjalankan data dalam jumlah besar atau volume permintaan yang tinggi pada model mungkin memerlukan lebih banyak memori GPU dan/atau dapat menyebabkan masalah kinerja. Disarankan untuk menguji kasus penggunaan Anda dengan konfigurasi berbeda dan memantau penggunaan memori untuk menentukan pengaturan optimal sesuai kebutuhan spesifik Anda.

## Contoh E2E untuk Interactive Phi 3 Mini 4K Instruct Chatbot dengan Whisper

Notebook jupyter berjudul [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) menunjukkan cara menggunakan Demo Microsoft Phi 3 Mini 4K instruct untuk menghasilkan teks dari input audio atau teks tertulis. Notebook ini mendefinisikan beberapa fungsi:

1. `tts_file_name(text)`: Fungsi ini menghasilkan nama file berdasarkan teks input untuk menyimpan file audio yang dihasilkan.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Fungsi ini menggunakan Edge TTS API untuk menghasilkan file audio dari daftar potongan teks input. Parameter input adalah daftar potongan, kecepatan bicara, nama suara, dan jalur output untuk menyimpan file audio yang dihasilkan.
1. `talk(input_text)`: Fungsi ini menghasilkan file audio dengan menggunakan Edge TTS API dan menyimpannya ke nama file acak di direktori /content/audio. Parameter input adalah teks yang akan diubah menjadi suara.
1. `run_text_prompt(message, chat_history)`: Fungsi ini menggunakan demo Microsoft Phi 3 Mini 4K instruct untuk menghasilkan file audio dari pesan input dan menambahkannya ke riwayat chat.
1. `run_audio_prompt(audio, chat_history)`: Fungsi ini mengubah file audio menjadi teks menggunakan API model Whisper dan meneruskannya ke fungsi `run_text_prompt()`.
1. Kode ini menjalankan aplikasi Gradio yang memungkinkan pengguna berinteraksi dengan demo Phi 3 Mini 4K instruct dengan mengetik pesan atau mengunggah file audio. Output ditampilkan sebagai pesan teks dalam aplikasi.

## Pemecahan Masalah

Menginstal driver Cuda GPU

1. Pastikan aplikasi Linux Anda sudah diperbarui

    ```bash
    sudo apt update
    ```

1. Instal Driver Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Daftarkan lokasi driver cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Memeriksa ukuran memori Nvidia GPU (Dibutuhkan Memori GPU 12GB)

    ```bash
    nvidia-smi
    ```

1. Kosongkan Cache: Jika Anda menggunakan PyTorch, Anda dapat memanggil torch.cuda.empty_cache() untuk melepaskan semua memori cache yang tidak terpakai agar dapat digunakan oleh aplikasi GPU lain

    ```python
    torch.cuda.empty_cache() 
    ```

1. Memeriksa Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Lakukan langkah berikut untuk membuat token Hugging Face.

    - Buka halaman [Hugging Face Token Settings](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Pilih **New token**.
    - Masukkan **Name** proyek yang ingin Anda gunakan.
    - Pilih **Type** menjadi **Write**.

> **Note**
>
> Jika Anda mengalami error berikut:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Untuk mengatasinya, ketik perintah berikut di terminal Anda.
>
> ```bash
> sudo ldconfig
> ```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk keakuratan, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.