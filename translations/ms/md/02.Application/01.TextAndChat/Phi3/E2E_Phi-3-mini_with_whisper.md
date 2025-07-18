<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:21:10+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "ms"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot dengan Whisper

## Gambaran Keseluruhan

Interactive Phi 3 Mini 4K Instruct Chatbot adalah alat yang membolehkan pengguna berinteraksi dengan demo Microsoft Phi 3 Mini 4K instruct menggunakan input teks atau audio. Chatbot ini boleh digunakan untuk pelbagai tugasan, seperti terjemahan, kemas kini cuaca, dan pengumpulan maklumat am.

### Mula Menggunakan

Untuk menggunakan chatbot ini, ikuti arahan berikut:

1. Buka [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Dalam tetingkap utama notebook, anda akan melihat antara muka kotak sembang dengan kotak input teks dan butang "Send".
3. Untuk menggunakan chatbot berasaskan teks, taipkan mesej anda ke dalam kotak input teks dan klik butang "Send". Chatbot akan membalas dengan fail audio yang boleh dimainkan terus dari dalam notebook.

**Note**: Alat ini memerlukan GPU dan akses kepada model Microsoft Phi-3 dan OpenAI Whisper, yang digunakan untuk pengecaman pertuturan dan terjemahan.

### Keperluan GPU

Untuk menjalankan demo ini, anda memerlukan memori GPU sebanyak 12GB.

Keperluan memori untuk menjalankan demo **Microsoft-Phi-3-Mini-4K instruct** pada GPU bergantung kepada beberapa faktor, seperti saiz data input (audio atau teks), bahasa yang digunakan untuk terjemahan, kelajuan model, dan memori yang tersedia pada GPU.

Secara amnya, model Whisper direka untuk dijalankan pada GPU. Jumlah minimum memori GPU yang disyorkan untuk menjalankan model Whisper adalah 8 GB, tetapi ia boleh mengendalikan jumlah memori yang lebih besar jika perlu.

Penting untuk diingat bahawa menjalankan data dalam jumlah besar atau permintaan yang tinggi pada model mungkin memerlukan lebih banyak memori GPU dan/atau boleh menyebabkan isu prestasi. Disyorkan untuk menguji kes penggunaan anda dengan konfigurasi yang berbeza dan memantau penggunaan memori untuk menentukan tetapan optimum mengikut keperluan khusus anda.

## Contoh E2E untuk Interactive Phi 3 Mini 4K Instruct Chatbot dengan Whisper

Notebook jupyter bertajuk [Interactive Phi 3 Mini 4K Instruct Chatbot dengan Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) menunjukkan cara menggunakan Demo Microsoft Phi 3 Mini 4K instruct untuk menjana teks daripada input audio atau teks bertulis. Notebook ini mentakrifkan beberapa fungsi:

1. `tts_file_name(text)`: Fungsi ini menjana nama fail berdasarkan teks input untuk menyimpan fail audio yang dijana.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Fungsi ini menggunakan API Edge TTS untuk menjana fail audio daripada senarai potongan teks input. Parameter input adalah senarai potongan, kadar pertuturan, nama suara, dan laluan output untuk menyimpan fail audio yang dijana.
1. `talk(input_text)`: Fungsi ini menjana fail audio dengan menggunakan API Edge TTS dan menyimpannya ke nama fail rawak dalam direktori /content/audio. Parameter input adalah teks yang akan ditukar kepada pertuturan.
1. `run_text_prompt(message, chat_history)`: Fungsi ini menggunakan demo Microsoft Phi 3 Mini 4K instruct untuk menjana fail audio daripada mesej input dan menambahkannya ke sejarah sembang.
1. `run_audio_prompt(audio, chat_history)`: Fungsi ini menukar fail audio kepada teks menggunakan API model Whisper dan menghantarnya ke fungsi `run_text_prompt()`.
1. Kod ini melancarkan aplikasi Gradio yang membolehkan pengguna berinteraksi dengan demo Phi 3 Mini 4K instruct sama ada dengan menaip mesej atau memuat naik fail audio. Output dipaparkan sebagai mesej teks dalam aplikasi.

## Penyelesaian Masalah

Memasang pemacu Cuda GPU

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

1. Semak saiz memori Nvidia GPU (Diperlukan 12GB Memori GPU)

    ```bash
    nvidia-smi
    ```

1. Kosongkan Cache: Jika anda menggunakan PyTorch, anda boleh panggil torch.cuda.empty_cache() untuk melepaskan semua memori cache yang tidak digunakan supaya boleh digunakan oleh aplikasi GPU lain

    ```python
    torch.cuda.empty_cache() 
    ```

1. Semak Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Lakukan tugasan berikut untuk mencipta token Hugging Face.

    - Pergi ke [Halaman Tetapan Token Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Pilih **New token**.
    - Masukkan **Name** projek yang anda ingin gunakan.
    - Pilih **Type** kepada **Write**.

> **Note**
>
> Jika anda menghadapi ralat berikut:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Untuk menyelesaikannya, taipkan arahan berikut dalam terminal anda.
>
> ```bash
> sudo ldconfig
> ```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.