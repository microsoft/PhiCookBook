<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "72e00a4ddbe9d6c25907d1eb19d041b8",
  "translation_date": "2025-10-17T10:59:07+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ms"
}
-->
# AGENTS.md

## Gambaran Projek

PhiCookBook adalah repositori buku masakan yang komprehensif yang mengandungi contoh praktikal, tutorial, dan dokumentasi untuk bekerja dengan keluarga Model Bahasa Kecil (SLM) Microsoft Phi. Repositori ini menunjukkan pelbagai kegunaan termasuk inferens, penalaan halus, kuantisasi, pelaksanaan RAG, dan aplikasi multimodal di pelbagai platform dan rangka kerja.

**Teknologi Utama:**
- **Bahasa:** Python, C#/.NET, JavaScript/Node.js
- **Rangka Kerja:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platform:** Azure AI Foundry, GitHub Models, Hugging Face, Ollama
- **Jenis Model:** Phi-3, Phi-3.5, Phi-4 (teks, penglihatan, multimodal, varian penaakulan)

**Struktur Repositori:**
- `/code/` - Contoh kod kerja dan pelaksanaan sampel
- `/md/` - Dokumentasi terperinci, tutorial, dan panduan cara
- `/translations/` - Terjemahan pelbagai bahasa (50+ bahasa melalui aliran kerja automatik)
- `/.devcontainer/` - Konfigurasi kontena pembangunan (Python 3.12 dengan Ollama)

## Persediaan Persekitaran Pembangunan

### Menggunakan GitHub Codespaces atau Dev Containers (Disyorkan)

1. Buka di GitHub Codespaces (paling pantas):
   - Klik lencana "Open in GitHub Codespaces" dalam README
   - Kontena dikonfigurasi secara automatik dengan Python 3.12 dan Ollama dengan Phi-3

2. Buka di VS Code Dev Containers:
   - Gunakan lencana "Open in Dev Containers" dari README
   - Kontena memerlukan memori hos minimum 16GB

### Persediaan Tempatan

**Keperluan:**
- Python 3.12 atau lebih baru
- .NET 8.0 SDK (untuk contoh C#)
- Node.js 18+ dan npm (untuk contoh JavaScript)
- RAM minimum 16GB disyorkan

**Pemasangan:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Untuk Contoh Python:**
Navigasi ke direktori contoh tertentu dan pasang kebergantungan:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**Untuk Contoh .NET:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Untuk Contoh JavaScript/Web:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Organisasi Repositori

### Contoh Kod (`/code/`)

- **01.Introduce/** - Pengenalan asas dan sampel permulaan
- **03.Finetuning/** dan **04.Finetuning/** - Contoh penalaan halus dengan pelbagai kaedah
- **03.Inference/** - Contoh inferens pada perkakasan berbeza (AIPC, MLX)
- **06.E2E/** - Sampel aplikasi hujung ke hujung
- **07.Lab/** - Pelaksanaan makmal/eksperimen
- **08.RAG/** - Sampel Penjanaan Augmentasi Pengambilan
- **09.UpdateSamples/** - Sampel terkini yang dikemas kini

### Dokumentasi (`/md/`)

- **01.Introduction/** - Panduan pengenalan, persediaan persekitaran, panduan platform
- **02.Application/** - Sampel aplikasi yang diatur mengikut jenis (Teks, Kod, Penglihatan, Audio, dll.)
- **02.QuickStart/** - Panduan permulaan pantas untuk Azure AI Foundry dan GitHub Models
- **03.FineTuning/** - Dokumentasi dan tutorial penalaan halus
- **04.HOL/** - Makmal praktikal (termasuk contoh .NET)

### Format Fail

- **Jupyter Notebooks (`.ipynb`)** - Tutorial Python interaktif yang ditandai dengan 📓 dalam README
- **Skrip Python (`.py`)** - Contoh Python yang berdiri sendiri
- **Projek C# (`.csproj`, `.sln`)** - Aplikasi dan sampel .NET
- **JavaScript (`.js`, `package.json`)** - Contoh berasaskan web dan Node.js
- **Markdown (`.md`)** - Dokumentasi dan panduan

## Bekerja dengan Contoh

### Menjalankan Jupyter Notebooks

Kebanyakan contoh disediakan sebagai Jupyter notebooks:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Menjalankan Skrip Python

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Menjalankan Contoh .NET

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Atau bina keseluruhan penyelesaian:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Menjalankan Contoh JavaScript/Web

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Ujian

Repositori ini mengandungi kod contoh dan tutorial dan bukan projek perisian tradisional dengan ujian unit. Pengesahan biasanya dilakukan dengan:

1. **Menjalankan contoh** - Setiap contoh harus dijalankan tanpa ralat
2. **Mengesahkan output** - Periksa bahawa respons model adalah sesuai
3. **Mengikuti tutorial** - Panduan langkah demi langkah harus berfungsi seperti yang didokumentasikan

**Pendekatan pengesahan biasa:**
- Uji pelaksanaan contoh dalam persekitaran sasaran
- Sahkan kebergantungan dipasang dengan betul
- Periksa bahawa model dimuat turun/dimuat dengan berjaya
- Pastikan tingkah laku yang dijangka sepadan dengan dokumentasi

## Gaya Kod dan Konvensyen

### Garis Panduan Umum

- Contoh harus jelas, mempunyai komen yang baik, dan mendidik
- Ikuti konvensyen khusus bahasa (PEP 8 untuk Python, piawaian C# untuk .NET)
- Kekalkan fokus contoh pada demonstrasi keupayaan model Phi tertentu
- Sertakan komen yang menerangkan konsep utama dan parameter khusus model

### Piawaian Dokumentasi

**Format URL:**
- Gunakan format `[text](../../url)` tanpa ruang tambahan
- Pautan relatif: Gunakan `./` untuk direktori semasa, `../` untuk induk
- Tiada lokal khusus negara dalam URL (elakkan `/en-us/`, `/en/`)

**Imej:**
- Simpan semua imej dalam direktori `/imgs/`
- Gunakan nama deskriptif dengan aksara Inggeris, nombor, dan tanda hubung
- Contoh: `phi-3-architecture.png`

**Fail Markdown:**
- Rujuk contoh kerja sebenar dalam direktori `/code/`
- Kekalkan dokumentasi selaras dengan perubahan kod
- Gunakan emoji 📓 untuk menandai pautan Jupyter notebook dalam README

### Organisasi Fail

- Contoh kod dalam `/code/` diatur mengikut topik/ciri
- Dokumentasi dalam `/md/` mencerminkan struktur kod apabila sesuai
- Simpan fail berkaitan (notebook, skrip, konfigurasi) bersama dalam subdirektori

## Garis Panduan Permintaan Tarik

### Sebelum Menghantar

1. **Fork repositori** ke akaun anda
2. **Pisahkan PR mengikut jenis:**
   - Pembetulan bug dalam satu PR
   - Kemas kini dokumentasi dalam PR lain
   - Contoh baru dalam PR berasingan
   - Pembetulan typo boleh digabungkan

3. **Tangani konflik gabungan:**
   - Kemas kini cawangan `main` tempatan anda sebelum membuat perubahan
   - Selaraskan dengan upstream dengan kerap

4. **PR Terjemahan:**
   - Mesti termasuk terjemahan untuk SEMUA fail dalam folder
   - Kekalkan struktur yang konsisten dengan bahasa asal

### Pemeriksaan Diperlukan

PR secara automatik menjalankan aliran kerja GitHub untuk mengesahkan:

1. **Pengesahan laluan relatif** - Semua pautan dalaman mesti berfungsi
   - Uji pautan secara tempatan: Ctrl+Klik dalam VS Code
   - Gunakan cadangan laluan dari VS Code (`./` atau `../`)

2. **Pemeriksaan lokal URL** - URL web tidak boleh mengandungi lokal negara
   - Buang `/en-us/`, `/en/`, atau kod bahasa lain
   - Gunakan URL antarabangsa generik

3. **Pemeriksaan URL rosak** - Semua URL mesti mengembalikan status 200
   - Sahkan pautan boleh diakses sebelum menghantar
   - Nota: Beberapa kegagalan mungkin disebabkan oleh sekatan rangkaian

### Format Tajuk PR

```
[component] Brief description
```

Contoh:
- `[docs] Tambah tutorial inferens Phi-4`
- `[code] Betulkan contoh integrasi ONNX Runtime`
- `[translation] Tambah terjemahan Jepun untuk panduan pengenalan`

## Corak Pembangunan Biasa

### Bekerja dengan Model Phi

**Pemuatan Model:**
- Contoh menggunakan pelbagai rangka kerja: Transformers, ONNX Runtime, MLX, OpenVINO
- Model biasanya dimuat turun dari Hugging Face, Azure, atau GitHub Models
- Periksa keserasian model dengan perkakasan anda (CPU, GPU, NPU)

**Corak Inferens:**
- Penjanaan teks: Kebanyakan contoh menggunakan varian chat/instruct
- Penglihatan: Phi-3-vision dan Phi-4-multimodal untuk pemahaman imej
- Audio: Phi-4-multimodal menyokong input audio
- Penaakulan: Varian Phi-4-reasoning untuk tugas penaakulan lanjutan

### Nota Khusus Platform

**Azure AI Foundry:**
- Memerlukan langganan Azure dan kunci API
- Lihat `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Tier percuma tersedia untuk ujian
- Lihat `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Inferens Tempatan:**
- ONNX Runtime: Inferens lintas platform yang dioptimumkan
- Ollama: Pengurusan model tempatan yang mudah (pra-konfigurasi dalam kontena pembangunan)
- Apple MLX: Dioptimumkan untuk Apple Silicon

## Penyelesaian Masalah

### Isu Biasa

**Isu Memori:**
- Model Phi memerlukan RAM yang besar (terutamanya varian penglihatan/multimodal)
- Gunakan model kuantisasi untuk persekitaran dengan sumber terhad
- Lihat `/md/01.Introduction/04/QuantifyingPhi.md`

**Konflik Kebergantungan:**
- Contoh Python mungkin mempunyai keperluan versi tertentu
- Gunakan persekitaran maya untuk setiap contoh
- Periksa fail `requirements.txt` individu

**Kegagalan Muat Turun Model:**
- Model besar mungkin tamat masa pada sambungan perlahan
- Pertimbangkan menggunakan persekitaran awan (Codespaces, Azure)
- Periksa cache Hugging Face: `~/.cache/huggingface/`

**Isu Projek .NET:**
- Pastikan .NET 8.0 SDK dipasang
- Gunakan `dotnet restore` sebelum membina
- Sesetengah projek mempunyai konfigurasi khusus CUDA (Debug_Cuda)

**Contoh JavaScript/Web:**
- Gunakan Node.js 18+ untuk keserasian
- Kosongkan `node_modules` dan pasang semula jika terdapat isu
- Periksa konsol pelayar untuk isu keserasian WebGPU

### Mendapatkan Bantuan

- **Discord:** Sertai Komuniti Discord Azure AI Foundry
- **GitHub Issues:** Laporkan bug dan isu dalam repositori
- **GitHub Discussions:** Ajukan soalan dan kongsi pengetahuan

## Konteks Tambahan

### AI Bertanggungjawab

Semua penggunaan model Phi harus mengikuti prinsip AI Bertanggungjawab Microsoft:
- Keadilan, kebolehpercayaan, keselamatan
- Privasi dan keselamatan  
- Keterangkuman, ketelusan, akauntabiliti
- Gunakan Azure AI Content Safety untuk aplikasi pengeluaran
- Lihat `/md/01.Introduction/01/01.AISafety.md`

### Terjemahan

- 50+ bahasa disokong melalui GitHub Action automatik
- Terjemahan dalam direktori `/translations/`
- Diselenggara oleh aliran kerja co-op-translator
- Jangan edit fail terjemahan secara manual (dihasilkan secara automatik)

### Menyumbang

- Ikuti garis panduan dalam `CONTRIBUTING.md`
- Setuju dengan Perjanjian Lesen Penyumbang (CLA)
- Patuhi Kod Etika Sumber Terbuka Microsoft
- Jaga keselamatan dan kelayakan daripada komit

### Sokongan Pelbagai Bahasa

Ini adalah repositori poliglot dengan contoh dalam:
- **Python** - Aliran kerja ML/AI, Jupyter notebooks, penalaan halus
- **C#/.NET** - Aplikasi perusahaan, integrasi ONNX Runtime
- **JavaScript** - AI berasaskan web, inferens pelayar dengan WebGPU

Pilih bahasa yang paling sesuai dengan kegunaan dan sasaran pelaksanaan anda.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.