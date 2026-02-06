# AGENTS.md

## Gambaran Proyek

PhiCookBook adalah repositori buku resep yang komprehensif berisi contoh praktis, tutorial, dan dokumentasi untuk bekerja dengan keluarga Small Language Models (SLMs) dari Microsoft, yaitu Phi. Repositori ini menunjukkan berbagai kasus penggunaan termasuk inferensi, fine-tuning, kuantisasi, implementasi RAG, dan aplikasi multimodal di berbagai platform dan kerangka kerja.

**Teknologi Utama:**
- **Bahasa:** Python, C#/.NET, JavaScript/Node.js
- **Kerangka Kerja:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platform:** Azure AI Foundry, GitHub Models, Hugging Face, Ollama
- **Jenis Model:** Phi-3, Phi-3.5, Phi-4 (varian teks, visual, multimodal, penalaran)

**Struktur Repositori:**
- `/code/` - Contoh kode kerja dan implementasi sampel
- `/md/` - Dokumentasi terperinci, tutorial, dan panduan
- `/translations/` - Terjemahan multi-bahasa (50+ bahasa melalui alur kerja otomatis)
- `/.devcontainer/` - Konfigurasi kontainer pengembangan (Python 3.12 dengan Ollama)

## Pengaturan Lingkungan Pengembangan

### Menggunakan GitHub Codespaces atau Dev Containers (Direkomendasikan)

1. Buka di GitHub Codespaces (paling cepat):
   - Klik badge "Open in GitHub Codespaces" di README
   - Kontainer akan dikonfigurasi otomatis dengan Python 3.12 dan Ollama dengan Phi-3

2. Buka di VS Code Dev Containers:
   - Gunakan badge "Open in Dev Containers" dari README
   - Kontainer membutuhkan minimal memori host 16GB

### Pengaturan Lokal

**Prasyarat:**
- Python 3.12 atau lebih baru
- .NET 8.0 SDK (untuk contoh C#)
- Node.js 18+ dan npm (untuk contoh JavaScript)
- Direkomendasikan minimal RAM 16GB

**Instalasi:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Untuk Contoh Python:**
Masuk ke direktori contoh spesifik dan instal dependensi:
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

### Contoh Kode (`/code/`)

- **01.Introduce/** - Pengenalan dasar dan contoh memulai
- **03.Finetuning/** dan **04.Finetuning/** - Contoh fine-tuning dengan berbagai metode
- **03.Inference/** - Contoh inferensi di berbagai perangkat keras (AIPC, MLX)
- **06.E2E/** - Contoh aplikasi end-to-end
- **07.Lab/** - Implementasi laboratorium/eksperimental
- **08.RAG/** - Contoh Retrieval-Augmented Generation
- **09.UpdateSamples/** - Contoh terbaru yang diperbarui

### Dokumentasi (`/md/`)

- **01.Introduction/** - Panduan pengantar, pengaturan lingkungan, panduan platform
- **02.Application/** - Contoh aplikasi yang diorganisasi berdasarkan jenis (Teks, Kode, Visual, Audio, dll.)
- **02.QuickStart/** - Panduan memulai cepat untuk Azure AI Foundry dan GitHub Models
- **03.FineTuning/** - Dokumentasi dan tutorial fine-tuning
- **04.HOL/** - Laboratorium praktis (termasuk contoh .NET)

### Format File

- **Jupyter Notebooks (`.ipynb`)** - Tutorial interaktif Python yang ditandai dengan 📓 di README
- **Script Python (`.py`)** - Contoh Python mandiri
- **Proyek C# (`.csproj`, `.sln`)** - Aplikasi dan contoh .NET
- **JavaScript (`.js`, `package.json`)** - Contoh berbasis web dan Node.js
- **Markdown (`.md`)** - Dokumentasi dan panduan

## Bekerja dengan Contoh

### Menjalankan Jupyter Notebooks

Sebagian besar contoh disediakan sebagai notebook Jupyter:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Menjalankan Script Python

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

Atau bangun seluruh solusi:
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

## Pengujian

Repositori ini berisi kode contoh dan tutorial, bukan proyek perangkat lunak tradisional dengan pengujian unit. Validasi biasanya dilakukan dengan:

1. **Menjalankan contoh** - Setiap contoh harus berjalan tanpa kesalahan
2. **Memverifikasi output** - Periksa apakah respons model sesuai
3. **Mengikuti tutorial** - Panduan langkah demi langkah harus berfungsi seperti yang didokumentasikan

**Pendekatan validasi umum:**
- Uji eksekusi contoh di lingkungan target
- Verifikasi instalasi dependensi berhasil
- Periksa apakah model berhasil diunduh/dimuat
- Konfirmasi perilaku yang diharapkan sesuai dengan dokumentasi

## Gaya dan Konvensi Kode

### Panduan Umum

- Contoh harus jelas, memiliki komentar yang baik, dan edukatif
- Ikuti konvensi spesifik bahasa (PEP 8 untuk Python, standar C# untuk .NET)
- Jaga agar contoh tetap fokus pada demonstrasi kemampuan spesifik model Phi
- Sertakan komentar yang menjelaskan konsep utama dan parameter spesifik model

### Standar Dokumentasi

**Format URL:**
- Gunakan format `[teks](../../url)` tanpa spasi tambahan
- Tautan relatif: Gunakan `./` untuk direktori saat ini, `../` untuk induk
- Hindari lokal spesifik negara dalam URL (hindari `/en-us/`, `/en/`)

**Gambar:**
- Simpan semua gambar di direktori `/imgs/`
- Gunakan nama deskriptif dengan karakter Inggris, angka, dan tanda hubung
- Contoh: `phi-3-architecture.png`

**File Markdown:**
- Referensi contoh kerja aktual di direktori `/code/`
- Sinkronkan dokumentasi dengan perubahan kode
- Gunakan emoji 📓 untuk menandai tautan notebook Jupyter di README

### Organisasi File

- Contoh kode di `/code/` diorganisasi berdasarkan topik/fitur
- Dokumentasi di `/md/` mencerminkan struktur kode jika memungkinkan
- Simpan file terkait (notebook, script, konfigurasi) bersama dalam subdirektori

## Panduan Pull Request

### Sebelum Mengirimkan

1. **Fork repositori** ke akun Anda
2. **Pisahkan PR berdasarkan jenis:**
   - Perbaikan bug dalam satu PR
   - Pembaruan dokumentasi dalam PR lain
   - Contoh baru dalam PR terpisah
   - Perbaikan typo dapat digabungkan

3. **Tangani konflik penggabungan:**
   - Perbarui cabang `main` lokal Anda sebelum membuat perubahan
   - Sinkronkan dengan upstream secara berkala

4. **PR Terjemahan:**
   - Harus menyertakan terjemahan untuk SEMUA file di folder
   - Pertahankan struktur konsisten dengan bahasa asli

### Pemeriksaan yang Diperlukan

PR secara otomatis menjalankan alur kerja GitHub untuk memvalidasi:

1. **Validasi jalur relatif** - Semua tautan internal harus berfungsi
   - Uji tautan secara lokal: Ctrl+Klik di VS Code
   - Gunakan saran jalur dari VS Code (`./` atau `../`)

2. **Pemeriksaan lokal URL** - URL web tidak boleh mengandung kode bahasa negara
   - Hapus `/en-us/`, `/en/`, atau kode bahasa lainnya
   - Gunakan URL internasional umum

3. **Pemeriksaan URL rusak** - Semua URL harus mengembalikan status 200
   - Verifikasi tautan dapat diakses sebelum mengirimkan
   - Catatan: Beberapa kegagalan mungkin disebabkan oleh pembatasan jaringan

### Format Judul PR

```
[component] Brief description
```

Contoh:
- `[docs] Tambahkan tutorial inferensi Phi-4`
- `[code] Perbaiki contoh integrasi ONNX Runtime`
- `[translation] Tambahkan terjemahan Jepang untuk panduan pengantar`

## Pola Pengembangan Umum

### Bekerja dengan Model Phi

**Memuat Model:**
- Contoh menggunakan berbagai kerangka kerja: Transformers, ONNX Runtime, MLX, OpenVINO
- Model biasanya diunduh dari Hugging Face, Azure, atau GitHub Models
- Periksa kompatibilitas model dengan perangkat keras Anda (CPU, GPU, NPU)

**Pola Inferensi:**
- Generasi teks: Sebagian besar contoh menggunakan varian chat/instruct
- Visual: Phi-3-vision dan Phi-4-multimodal untuk pemahaman gambar
- Audio: Phi-4-multimodal mendukung input audio
- Penalaran: Varian Phi-4-reasoning untuk tugas penalaran tingkat lanjut

### Catatan Khusus Platform

**Azure AI Foundry:**
- Membutuhkan langganan Azure dan kunci API
- Lihat `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Tersedia tier gratis untuk pengujian
- Lihat `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Inferensi Lokal:**
- ONNX Runtime: Inferensi lintas platform yang dioptimalkan
- Ollama: Manajemen model lokal yang mudah (pra-konfigurasi di kontainer pengembangan)
- Apple MLX: Dioptimalkan untuk Apple Silicon

## Pemecahan Masalah

### Masalah Umum

**Masalah Memori:**
- Model Phi membutuhkan RAM yang signifikan (terutama varian visual/multimodal)
- Gunakan model yang dikuantisasi untuk lingkungan dengan sumber daya terbatas
- Lihat `/md/01.Introduction/04/QuantifyingPhi.md`

**Konflik Dependensi:**
- Contoh Python mungkin memiliki persyaratan versi spesifik
- Gunakan lingkungan virtual untuk setiap contoh
- Periksa file `requirements.txt` individu

**Kegagalan Unduhan Model:**
- Model besar mungkin timeout pada koneksi lambat
- Pertimbangkan menggunakan lingkungan cloud (Codespaces, Azure)
- Periksa cache Hugging Face: `~/.cache/huggingface/`

**Masalah Proyek .NET:**
- Pastikan .NET 8.0 SDK terinstal
- Gunakan `dotnet restore` sebelum membangun
- Beberapa proyek memiliki konfigurasi spesifik CUDA (Debug_Cuda)

**Contoh JavaScript/Web:**
- Gunakan Node.js 18+ untuk kompatibilitas
- Hapus `node_modules` dan instal ulang jika terjadi masalah
- Periksa konsol browser untuk masalah kompatibilitas WebGPU

### Mendapatkan Bantuan

- **Discord:** Bergabunglah dengan Komunitas Discord Azure AI Foundry
- **GitHub Issues:** Laporkan bug dan masalah di repositori
- **GitHub Discussions:** Ajukan pertanyaan dan berbagi pengetahuan

## Konteks Tambahan

### AI yang Bertanggung Jawab

Semua penggunaan model Phi harus mengikuti prinsip AI yang Bertanggung Jawab dari Microsoft:
- Keadilan, keandalan, keamanan
- Privasi dan keamanan  
- Inklusivitas, transparansi, akuntabilitas
- Gunakan Azure AI Content Safety untuk aplikasi produksi
- Lihat `/md/01.Introduction/01/01.AISafety.md`

### Terjemahan

- Mendukung 50+ bahasa melalui GitHub Action otomatis
- Terjemahan ada di direktori `/translations/`
- Dipelihara oleh alur kerja co-op-translator
- Jangan mengedit file terjemahan secara manual (dihasilkan otomatis)

### Kontribusi

- Ikuti panduan di `CONTRIBUTING.md`
- Setujui Contributor License Agreement (CLA)
- Patuhi Microsoft Open Source Code of Conduct
- Jangan sertakan keamanan dan kredensial dalam commit

### Dukungan Multi-Bahasa

Ini adalah repositori poliglot dengan contoh dalam:
- **Python** - Alur kerja ML/AI, notebook Jupyter, fine-tuning
- **C#/.NET** - Aplikasi perusahaan, integrasi ONNX Runtime
- **JavaScript** - AI berbasis web, inferensi di browser dengan WebGPU

Pilih bahasa yang paling sesuai dengan kasus penggunaan dan target penerapan Anda.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.