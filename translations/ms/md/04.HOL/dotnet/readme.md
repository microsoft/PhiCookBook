## Selamat datang ke makmal Phi menggunakan C#

Terdapat beberapa makmal yang mempamerkan cara mengintegrasikan pelbagai versi model Phi yang berkuasa dalam persekitaran .NET.

## Prasyarat

Sebelum menjalankan contoh, pastikan anda telah memasang perkara berikut:

**.NET 9:** Pastikan anda mempunyai [versi terkini .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) dipasang pada mesin anda.

**(Pilihan) Visual Studio atau Visual Studio Code:** Anda memerlukan IDE atau penyunting kod yang mampu menjalankan projek .NET. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) atau [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) adalah disyorkan.

**Menggunakan git** klon secara tempatan salah satu versi Phi-3, Phi3.5 atau Phi-4 yang tersedia dari [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Muat turun model Phi-4 ONNX** ke mesin tempatan anda:

### navigasi ke folder untuk menyimpan model

```bash
cd c:\phi\models
```

### tambah sokongan untuk lfs

```bash
git lfs install 
```

### klon dan muat turun model Phi-4 mini instruct dan model Phi-4 multimodal

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Muat turun model Phi-3 ONNX** ke mesin tempatan anda:

### klon dan muat turun model Phi-3 mini 4K instruct dan model Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Penting:** Demo semasa direka untuk menggunakan versi ONNX model. Langkah-langkah sebelum ini mengklon model-model berikut.

## Mengenai Makmal

Penyelesaian utama mempunyai beberapa makmal contoh yang menunjukkan keupayaan model Phi menggunakan C#.

| Projek | Model | Penerangan |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 atau Phi-3.5 | Contoh chat konsol yang membolehkan pengguna bertanya soalan. Projek memuatkan model ONNX Phi-3 tempatan menggunakan perpustakaan `Microsoft.ML.OnnxRuntime`. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 atau Phi-3.5 | Contoh chat konsol yang membolehkan pengguna bertanya soalan. Projek memuatkan model ONNX Phi-3 tempatan menggunakan perpustakaan `Microsoft.Semantic.Kernel`. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 atau Phi-3.5 | Ini adalah projek contoh yang menggunakan model phi3 vision tempatan untuk menganalisis imej. Projek memuatkan model ONNX Phi-3 Vision tempatan menggunakan perpustakaan `Microsoft.ML.OnnxRuntime`. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 atau Phi-3.5 | Ini adalah projek contoh yang menggunakan model phi3 vision tempatan untuk menganalisis imej. Projek memuatkan model ONNX Phi-3 Vision tempatan menggunakan perpustakaan `Microsoft.ML.OnnxRuntime`. Projek juga memaparkan menu dengan pelbagai pilihan untuk berinteraksi dengan pengguna. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Contoh chat konsol yang membolehkan pengguna bertanya soalan. Projek memuatkan model ONNX Phi-4 tempatan menggunakan perpustakaan `Microsoft.ML.OnnxRuntime`. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Contoh chat konsol yang membolehkan pengguna bertanya soalan. Projek memuatkan model ONNX Phi-4 tempatan menggunakan perpustakaan `Semantic Kernel`. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Contoh chat konsol yang membolehkan pengguna bertanya soalan. Projek memuatkan model ONNX Phi-4 tempatan menggunakan perpustakaan `Microsoft.ML.OnnxRuntimeGenAI` dan melaksanakan `IChatClient` dari `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Contoh chat konsol yang membolehkan pengguna bertanya soalan. Chat ini melaksanakan memori. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Ini adalah projek contoh yang menggunakan model Phi-4 tempatan untuk menganalisis imej dan memaparkan hasil di konsol. Projek memuatkan model Phi-4-`multimodal-instruct-onnx` tempatan menggunakan perpustakaan `Microsoft.ML.OnnxRuntime`. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Ini adalah projek contoh yang menggunakan model Phi-4 tempatan untuk menganalisis fail audio, menjana transkrip fail tersebut dan memaparkan hasil di konsol. Projek memuatkan model Phi-4-`multimodal-instruct-onnx` tempatan menggunakan perpustakaan `Microsoft.ML.OnnxRuntime`. |

## Cara Menjalankan Projek

Untuk menjalankan projek, ikut langkah berikut:

1. Klon repositori ke mesin tempatan anda.

1. Buka terminal dan navigasi ke projek yang dikehendaki. Contohnya, mari jalankan `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Jalankan projek dengan arahan

    ```bash
    dotnet run
    ```

1. Projek contoh akan meminta input pengguna dan membalas menggunakan mod tempatan.

   Demo yang sedang berjalan adalah serupa dengan ini:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.