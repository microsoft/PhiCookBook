## Selamat datang di Phi labs menggunakan C#

Terdapat beberapa lab yang menunjukkan cara mengintegrasikan berbagai versi model Phi yang kuat dalam lingkungan .NET.

## Prasyarat

Sebelum menjalankan contoh, pastikan Anda telah menginstal hal berikut:

**.NET 9:** Pastikan Anda memiliki [versi terbaru .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) terpasang di komputer Anda.

**(Opsional) Visual Studio atau Visual Studio Code:** Anda memerlukan IDE atau editor kode yang mampu menjalankan proyek .NET. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) atau [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) direkomendasikan.

**Menggunakan git** kloning secara lokal salah satu versi Phi-3, Phi3.5, atau Phi-4 yang tersedia dari [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Unduh model Phi-4 ONNX** ke mesin lokal Anda:

### navigasikan ke folder untuk menyimpan model

```bash
cd c:\phi\models
```

### tambahkan dukungan untuk lfs

```bash
git lfs install 
```

### kloning dan unduh model Phi-4 mini instruct dan model Phi-4 multimodal

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Unduh model Phi-3 ONNX** ke mesin lokal Anda:

### kloning dan unduh model Phi-3 mini 4K instruct dan model Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Penting:** Demo saat ini dirancang untuk menggunakan versi ONNX dari model. Langkah-langkah sebelumnya mengkloning model-model berikut.

## Tentang Labs

Solusi utama memiliki beberapa Lab contoh yang menunjukkan kemampuan model Phi menggunakan C#.

| Proyek | Model | Deskripsi |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 atau Phi-3.5 | Contoh chat konsol yang memungkinkan pengguna mengajukan pertanyaan. Proyek memuat model ONNX Phi-3 lokal menggunakan pustaka `Microsoft.ML.OnnxRuntime`. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 atau Phi-3.5 | Contoh chat konsol yang memungkinkan pengguna mengajukan pertanyaan. Proyek memuat model ONNX Phi-3 lokal menggunakan pustaka `Microsoft.Semantic.Kernel`. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 atau Phi-3.5 | Ini adalah proyek contoh yang menggunakan model phi3 vision lokal untuk menganalisis gambar. Proyek memuat model ONNX Phi-3 Vision lokal menggunakan pustaka `Microsoft.ML.OnnxRuntime`. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 atau Phi-3.5 | Ini adalah proyek contoh yang menggunakan model phi3 vision lokal untuk menganalisis gambar. Proyek memuat model ONNX Phi-3 Vision lokal menggunakan pustaka `Microsoft.ML.OnnxRuntime`. Proyek juga menampilkan menu dengan berbagai opsi untuk berinteraksi dengan pengguna. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Contoh chat konsol yang memungkinkan pengguna mengajukan pertanyaan. Proyek memuat model ONNX Phi-4 lokal menggunakan pustaka `Microsoft.ML.OnnxRuntime`. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Contoh chat konsol yang memungkinkan pengguna mengajukan pertanyaan. Proyek memuat model ONNX Phi-4 lokal menggunakan pustaka `Semantic Kernel`. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Contoh chat konsol yang memungkinkan pengguna mengajukan pertanyaan. Proyek memuat model ONNX Phi-4 lokal menggunakan pustaka `Microsoft.ML.OnnxRuntimeGenAI` dan mengimplementasikan `IChatClient` dari `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Contoh chat konsol yang memungkinkan pengguna mengajukan pertanyaan. Chat ini mengimplementasikan memori. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Ini adalah proyek contoh yang menggunakan model Phi-4 lokal untuk menganalisis gambar dan menampilkan hasilnya di konsol. Proyek memuat model Phi-4-`multimodal-instruct-onnx` lokal menggunakan pustaka `Microsoft.ML.OnnxRuntime`. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Ini adalah proyek contoh yang menggunakan model Phi-4 lokal untuk menganalisis file audio, menghasilkan transkrip file tersebut, dan menampilkan hasilnya di konsol. Proyek memuat model Phi-4-`multimodal-instruct-onnx` lokal menggunakan pustaka `Microsoft.ML.OnnxRuntime`. |

## Cara Menjalankan Proyek

Untuk menjalankan proyek, ikuti langkah-langkah berikut:

1. Kloning repositori ke mesin lokal Anda.

1. Buka terminal dan navigasikan ke proyek yang diinginkan. Contohnya, mari jalankan `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Jalankan proyek dengan perintah

    ```bash
    dotnet run
    ```

1. Proyek contoh akan meminta input dari pengguna dan membalas menggunakan model lokal.

   Demo yang berjalan akan terlihat seperti ini:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.