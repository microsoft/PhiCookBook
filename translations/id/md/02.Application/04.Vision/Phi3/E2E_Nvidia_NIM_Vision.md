<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-07-17T04:57:36+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "id"
}
-->
### Contoh Skenario

Bayangkan Anda memiliki sebuah gambar (`demo.png`) dan ingin menghasilkan kode Python yang memproses gambar ini dan menyimpan versi barunya (`phi-3-vision.jpg`).

Kode di atas mengotomatisasi proses ini dengan cara:

1. Menyiapkan lingkungan dan konfigurasi yang diperlukan.
2. Membuat prompt yang menginstruksikan model untuk menghasilkan kode Python yang dibutuhkan.
3. Mengirim prompt ke model dan mengumpulkan kode yang dihasilkan.
4. Mengekstrak dan menjalankan kode yang dihasilkan.
5. Menampilkan gambar asli dan gambar yang sudah diproses.

Pendekatan ini memanfaatkan kekuatan AI untuk mengotomatisasi tugas pemrosesan gambar, sehingga lebih mudah dan cepat mencapai tujuan Anda.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Mari kita uraikan apa yang dilakukan seluruh kode langkah demi langkah:

1. **Pasang Paket yang Dibutuhkan**:  
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```  
    Perintah ini memasang paket `langchain_nvidia_ai_endpoints`, memastikan versinya yang terbaru.

2. **Impor Modul yang Diperlukan**:  
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```  
    Impor ini membawa modul-modul yang diperlukan untuk berinteraksi dengan endpoint NVIDIA AI, menangani password dengan aman, berinteraksi dengan sistem operasi, dan melakukan encoding/decoding data dalam format base64.

3. **Atur API Key**:  
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```  
    Kode ini memeriksa apakah variabel lingkungan `NVIDIA_API_KEY` sudah diatur. Jika belum, pengguna diminta memasukkan API key secara aman.

4. **Tentukan Model dan Path Gambar**:  
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```  
    Ini mengatur model yang akan digunakan, membuat instance `ChatNVIDIA` dengan model tersebut, dan menentukan path ke file gambar.

5. **Buat Prompt Teks**:  
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```  
    Ini mendefinisikan prompt teks yang menginstruksikan model untuk menghasilkan kode Python untuk memproses gambar.

6. **Encode Gambar ke Base64**:  
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```  
    Kode ini membaca file gambar, meng-encode-nya ke base64, dan membuat tag gambar HTML dengan data yang sudah di-encode.

7. **Gabungkan Teks dan Gambar ke dalam Prompt**:  
    ```python
    prompt = f"{text} {image}"
    ```  
    Ini menggabungkan prompt teks dan tag gambar HTML menjadi satu string.

8. **Hasilkan Kode Menggunakan ChatNVIDIA**:  
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```  
    Kode ini mengirim prompt ke model `ChatNVIDIA` dan mengumpulkan kode yang dihasilkan secara bertahap, mencetak dan menambahkan setiap bagian ke string `code`.

9. **Ekstrak Kode Python dari Konten yang Dihasilkan**:  
    ```python
    begin = code.index('```python') + 9  
    code = code[begin:]  
    end = code.index('```')
    code = code[:end]
    ```  
    Ini mengekstrak kode Python sebenarnya dari konten yang dihasilkan dengan menghapus format markdown.

10. **Jalankan Kode yang Dihasilkan**:  
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```  
    Ini menjalankan kode Python yang sudah diekstrak sebagai subprocess dan menangkap outputnya.

11. **Tampilkan Gambar**:  
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```  
    Baris-baris ini menampilkan gambar menggunakan modul `IPython.display`.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.