<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f72d7981ed3640865700f51ae407da4",
  "translation_date": "2026-01-14T15:53:19+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "ms"
}
-->
# Chatbot Interaktif Phi 3 Mini 4K Instruct dengan Whisper

## Gambaran Keseluruhan

Chatbot Interaktif Phi 3 Mini 4K Instruct adalah alat yang membolehkan pengguna berinteraksi dengan demo Microsoft Phi 3 Mini 4K Instruct menggunakan input teks atau audio. Chatbot ini boleh digunakan untuk pelbagai tugasan, seperti terjemahan, kemas kini cuaca, dan pengumpulan maklumat umum.

### Memulakan

Untuk menggunakan chatbot ini, ikut arahan berikut:

1. Buka [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) yang baru.
2. Dalam tetingkap utama notebook, anda akan melihat antara muka kotak sembang dengan kotak input teks dan butang "Send".
3. Untuk menggunakan chatbot berasaskan teks, taipkan mesej anda dalam kotak input teks dan klik butang "Send". Chatbot akan membalas dengan fail audio yang boleh dimainkan terus dari dalam notebook.

**Nota**: Alat ini memerlukan GPU dan akses kepada model Microsoft Phi-3 dan OpenAI Whisper, yang digunakan untuk pengecaman pertuturan dan terjemahan.

### Keperluan GPU

Untuk menjalankan demo ini anda memerlukan memori GPU sebanyak 12Gb.

Keperluan memori untuk menjalankan demo **Microsoft-Phi-3-Mini-4K instruct** pada GPU bergantung kepada beberapa faktor, seperti saiz data input (audio atau teks), bahasa yang digunakan untuk terjemahan, kelajuan model, dan memori tersedia pada GPU.

Secara amnya, model Whisper direka untuk dijalankan pada GPU. Jumlah minimum memori GPU yang disyorkan untuk menjalankan model Whisper ialah 8 GB, tetapi ia boleh mengendalikan jumlah memori yang lebih besar jika perlu.

Penting untuk diperhatikan bahawa menjalankan sejumlah besar data atau volum permintaan yang tinggi pada model mungkin memerlukan lebih banyak memori GPU dan/atau mungkin menyebabkan masalah prestasi. Disyorkan untuk menguji kes penggunaan anda dengan konfigurasi yang berbeza dan memantau penggunaan memori untuk menentukan tetapan optimum bagi keperluan khusus anda.

## Contoh E2E untuk Chatbot Interaktif Phi 3 Mini 4K Instruct dengan Whisper

Notebook Jupyter berjudul [Chatbot Interaktif Phi 3 Mini 4K Instruct dengan Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) menunjukkan cara menggunakan Demo Microsoft Phi 3 Mini 4K Instruct untuk menghasilkan teks daripada input audio atau teks bertulis. Notebook ini mendefinisikan beberapa fungsi:

1. `tts_file_name(text)`: Fungsi ini menjana nama fail berdasarkan teks input untuk menyimpan fail audio yang dihasilkan.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Fungsi ini menggunakan API Edge TTS untuk menghasilkan fail audio daripada senarai bahagian teks input. Parameter input adalah senarai bahagian, kadar pertuturan, nama suara, dan laluan output untuk menyimpan fail audio yang dihasilkan.
1. `talk(input_text)`: Fungsi ini menghasilkan fail audio dengan menggunakan API Edge TTS dan menyimpannya ke nama fail rawak di direktori /content/audio. Parameter input adalah teks input yang akan ditukar kepada pertuturan.
1. `run_text_prompt(message, chat_history)`: Fungsi ini menggunakan demo Microsoft Phi 3 Mini 4K instruct untuk menghasilkan fail audio daripada mesej input dan menambahkannya ke sejarah sembang.
1. `run_audio_prompt(audio, chat_history)`: Fungsi ini menukar fail audio kepada teks menggunakan API model Whisper dan menghantarnya ke fungsi `run_text_prompt()`.
1. Kod ini melancarkan aplikasi Gradio yang membolehkan pengguna berinteraksi dengan demo Phi 3 Mini 4K Instruct sama ada dengan menaip mesej atau memuat naik fail audio. Output dipaparkan sebagai mesej teks dalam aplikasi tersebut.

## Penyelesaian Masalah

Memasang pemacu GPU Cuda

1. Pastikan aplikasi Linux anda dikemas kini

    ```bash
    sudo apt update
    ```

1. Pasang Pemacu Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Daftarkan lokasi pemacu cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Semak saiz memori GPU Nvidia (Memerlukan Memori GPU 12GB)

    ```bash
    nvidia-smi
    ```

1. Kosongkan Cache: Jika anda menggunakan PyTorch, anda boleh panggil torch.cuda.empty_cache() untuk melepaskan semua memori cache yang tidak digunakan supaya ia boleh digunakan oleh aplikasi GPU lain

    ```python
    torch.cuda.empty_cache() 
    ```

1. Semak Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Lakukan tugasan berikut untuk membuat token Hugging Face.

    - Navigasi ke [Halaman Tetapan Token Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Pilih **New token**.
    - Masukkan **Name** projek yang anda ingin gunakan.
    - Pilih **Type** kepada **Write**.

> [!NOTE]
>
> Jika anda menghadapi ralat berikut:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Untuk menyelesaikan ini, taip arahan berikut dalam terminal anda.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sah. Untuk maklumat yang kritikal, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->