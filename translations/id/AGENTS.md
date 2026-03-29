# AGENTS.md

## Gambaran Proyek

PhiCookBook adalah repositori buku masak yang komprehensif yang berisi contoh langsung, tutorial, dan dokumentasi untuk bekerja dengan keluarga Phi dari Small Language Models (SLMs) milik Microsoft. Repositori ini menunjukkan berbagai kasus penggunaan termasuk inferensi, fine-tuning, kuantisasi, implementasi RAG, dan aplikasi multimodal di berbagai platform dan framework.

**Teknologi Kunci:**
- **Bahasa:** Python, C#/.NET, JavaScript/Node.js
- **Framework:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platform:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Jenis Model:** Phi-3, Phi-3.5, Phi-4 (varian teks, visi, multimodal, penalaran)

**Struktur Repositori:**
- `/code/` - Contoh kode kerja dan implementasi sampel
- `/md/` - Dokumentasi detail, tutorial, dan panduan cara pakai  
- `/translations/` - Terjemahan multi-bahasa (50+ bahasa melalui alur kerja otomatis)
- `/.devcontainer/` - Konfigurasi container dev (Python 3.12 dengan Ollama)

## Pengaturan Lingkungan Pengembangan

### Menggunakan GitHub Codespaces atau Dev Containers (Direkomendasikan)

1. Buka di GitHub Codespaces (paling cepat):
   - Klik badge "Open in GitHub Codespaces" di README
   - Container otomatis dikonfigurasi dengan Python 3.12 dan Ollama dengan Phi-3

2. Buka di VS Code Dev Containers:
   - Gunakan badge "Open in Dev Containers" dari README
   - Container memerlukan memori host minimal 16GB

### Pengaturan Lokal

**Prasyarat:**
- Python 3.12 atau lebih baru
- .NET 8.0 SDK (untuk contoh C#)
- Node.js 18+ dan npm (untuk contoh JavaScript)
- Direkomendasikan RAM minimal 16GB

**Instalasi:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Untuk Contoh Python:**
Navigasi ke direktori contoh tertentu dan instal dependensi:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # jika requirements.txt ada
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
npm run dev  # Mulai server pengembangan
npm run build  # Bangun untuk produksi
```

## Organisasi Repositori

### Contoh Kode (`/code/`)

- **01.Introduce/** - Perkenalan dasar dan contoh memulai
- **03.Finetuning/** dan **04.Finetuning/** - Contoh fine-tuning dengan berbagai metode
- **03.Inference/** - Contoh inferensi pada perangkat keras berbeda (AIPC, MLX)
- **06.E2E/** - Contoh aplikasi end-to-end
- **07.Lab/** - Implementasi laboratorium/ekperimen
- **08.RAG/** - Contoh Retrieval-Augmented Generation
- **09.UpdateSamples/** - Contoh yang paling baru diperbarui

### Dokumentasi (`/md/`)

- **01.Introduction/** - Panduan pengantar, setup lingkungan, panduan platform
- **02.Application/** - Contoh aplikasi yang diorganisasi berdasarkan tipe (Teks, Kode, Visi, Audio, dll.)
- **02.QuickStart/** - Panduan memulai cepat untuk Microsoft Foundry dan GitHub Models
- **03.FineTuning/** - Dokumentasi dan tutorial fine-tuning
- **04.HOL/** - Hands-on labs (termasuk contoh .NET)

### Format Berkas

- **Jupyter Notebooks (`.ipynb`)** - Tutorial Python interaktif dengan emoji 📓 di README
- **Python Scripts (`.py`)** - Contoh Python mandiri
- **C# Projects (`.csproj`, `.sln`)** - Aplikasi dan contoh .NET
- **JavaScript (`.js`, `package.json`)** - Contoh berbasis web dan Node.js
- **Markdown (`.md`)** - Dokumentasi dan panduan

## Bekerja dengan Contoh

### Menjalankan Jupyter Notebooks

Sebagian besar contoh disediakan sebagai notebook Jupyter:
```bash
pip install jupyter notebook
jupyter notebook  # Membuka antarmuka browser
# Navigasi ke file .ipynb yang diinginkan
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

Atau bangun seluruh solusi:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Menjalankan Contoh JavaScript/Web

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Pengembangan dengan pemuatan ulang cepat
```

## Pengujian

Repositori ini mengandung contoh kode dan tutorial, bukan proyek perangkat lunak tradisional dengan unit test. Validasi biasanya dilakukan dengan:

1. **Menjalankan contoh** - Setiap contoh harus berjalan tanpa error
2. **Memverifikasi output** - Periksa respons model apakah sesuai
3. **Mengikuti tutorial** - Panduan langkah-demi-langkah harus berfungsi seperti yang didokumentasikan

**Pendekatan validasi umum:**
- Uji eksekusi contoh di lingkungan target
- Verifikasi instalasi dependensi berhasil
- Periksa model berhasil diunduh/dimuat
- Pastikan perilaku sesuai dokumentasi

## Gaya dan Konvensi Kode

### Panduan Umum

- Contoh harus jelas, berkomentar baik, dan edukatif
- Ikuti konvensi sesuai bahasa (PEP 8 untuk Python, standar C# untuk .NET)
- Fokus contoh pada kemampuan spesifik model Phi
- Sertakan komentar yang menjelaskan konsep kunci dan parameter model

### Standar Dokumentasi

**Format URL:**
- Gunakan format `[text](../../url)` tanpa spasi ekstra
- Tautan relatif: Gunakan `./` untuk direktori saat ini, `../` untuk direktori induk
- Tidak menggunakan locale negara di URL (hindari `/en-us/`, `/en/`)

**Gambar:**
- Simpan semua gambar di direktori `/imgs/`
- Gunakan nama deskriptif dengan karakter bahasa Inggris, angka, dan tanda hubung
- Contoh: `phi-3-architecture.png`

**Berkas Markdown:**
- Referensikan contoh kerja nyata di direktori `/code/`
- Jaga dokumentasi tetap sinkron dengan perubahan kode
- Gunakan emoji 📓 untuk menandai tautan notebook Jupyter di README

### Organisasi Berkas

- Contoh kode di `/code/` diorganisasi berdasarkan topik/fitur
- Dokumentasi di `/md/` mencerminkan struktur kode bila memungkinkan
- Simpan berkas terkait (notebook, skrip, konfigurasi) bersamaan dalam subdirektori

## Pedoman Pull Request

### Sebelum Mengirim

1. **Fork repositori** ke akun Anda
2. **Pisahkan PR berdasarkan jenis:**
   - Perbaikan bug di satu PR
   - Pembaruan dokumentasi di PR lain
   - Contoh baru di PR terpisah
   - Perbaikan typo bisa digabung

3. **Tangani konflik merge:**
   - Perbarui branch `main` lokal Anda sebelum mengubah
   - Sinkronkan dengan upstream secara rutin

4. **PR Terjemahan:**
   - Harus mencakup terjemahan SEMUA berkas di folder
   - Pertahankan struktur konsisten dengan bahasa asli

### Pemeriksaan Wajib

PR secara otomatis menjalankan workflow GitHub untuk memvalidasi:

1. **Validasi path relatif** - Semua tautan internal harus berfungsi
   - Uji tautan secara lokal: Ctrl+Klik di VS Code
   - Gunakan saran path dari VS Code (`./` atau `../`)

2. **Pemeriksaan locale URL** - URL web tidak boleh mengandung locale negara
   - Hapus `/en-us/`, `/en/` atau kode bahasa lain
   - Gunakan URL internasional umum

3. **Pemeriksaan URL rusak** - Semua URL harus mengembalikan status 200
   - Verifikasi tautan dapat diakses sebelum mengirim
   - Catatan: Beberapa kegagalan mungkin akibat pembatasan jaringan

### Format Judul PR

```
[component] Brief description
```

Contoh:
- `[docs] Tambah tutorial inferensi Phi-4`
- `[code] Perbaiki contoh integrasi ONNX Runtime`
- `[translation] Tambah terjemahan Jepang untuk panduan pengantar`

## Pola Pengembangan Umum

### Bekerja dengan Model Phi

**Memuat Model:**
- Contoh menggunakan berbagai framework: Transformers, ONNX Runtime, MLX, OpenVINO
- Model biasanya diunduh dari Hugging Face, Azure, atau GitHub Models
- Periksa kompatibilitas model dengan perangkat keras Anda (CPU, GPU, NPU)

**Pola Inferensi:**
- Generasi teks: Sebagian besar memakai varian chat/instruct
- Visi: Phi-3-vision dan Phi-4-multimodal untuk pemahaman gambar
- Audio: Phi-4-multimodal mendukung input audio
- Penalaran: Varian Phi-4-reasoning untuk tugas penalaran tingkat lanjut

### Catatan Spesifik Platform

**Microsoft Foundry:**
- Memerlukan langganan Azure dan API keys
- Lihat `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Tier gratis tersedia untuk pengujian
- Lihat `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Inferensi Lokal:**
- ONNX Runtime: Lintas platform, inferensi teroptimasi
- Ollama: Manajemen model lokal mudah (pra-konfigurasi di dev container)
- Apple MLX: Optimasi untuk Apple Silicon

## Pemecahan Masalah

### Masalah Umum

**Masalah Memori:**
- Model Phi butuh RAM signifikan (khusus varian visi/multimodal)
- Gunakan model kuantisasi untuk lingkungan dengan sumber daya terbatas
- Lihat `/md/01.Introduction/04/QuantifyingPhi.md`

**Konflik Dependensi:**
- Contoh Python mungkin memerlukan versi spesifik
- Gunakan virtual environment untuk setiap contoh
- Periksa `requirements.txt` individu

**Gagal Unduh Model:**
- Model besar mungkin timeout di koneksi lambat
- Pertimbangkan menggunakan lingkungan cloud (Codespaces, Azure)
- Periksa cache Hugging Face: `~/.cache/huggingface/`

**Masalah Proyek .NET:**
- Pastikan SDK .NET 8.0 terpasang
- Gunakan `dotnet restore` sebelum membangun
- Beberapa proyek punya konfigurasi CUDA spesifik (Debug_Cuda)

**Contoh JavaScript/Web:**
- Gunakan Node.js 18+ untuk kompatibilitas
- Bersihkan `node_modules` dan pasang ulang jika masalah berlanjut
- Cek konsol browser untuk masalah kompatibilitas WebGPU

### Mendapatkan Bantuan

- **Discord:** Gabung Microsoft Foundry Community Discord
- **GitHub Issues:** Laporkan bug dan masalah di repositori
- **GitHub Discussions:** Ajukan pertanyaan dan berbagi pengetahuan

## Konteks Tambahan

### AI yang Bertanggung Jawab

Semua penggunaan model Phi harus mengikuti prinsip Responsible AI Microsoft:
- Keadilan, keandalan, keamanan
- Privasi dan keamanan  
- Inklusivitas, transparansi, akuntabilitas
- Gunakan Azure AI Content Safety untuk aplikasi produksi
- Lihat `/md/01.Introduction/01/01.AISafety.md`

### Terjemahan

- Mendukung 50+ bahasa melalui GitHub Action otomatis
- Terjemahan di direktori `/translations/`
- Dikelola oleh workflow co-op-translator
- Jangan diedit manual (dihasilkan otomatis)

### Kontribusi

- Ikuti pedoman di `CONTRIBUTING.md`
- Setujui Contributor License Agreement (CLA)
- Patuhi Kode Etik Sumber Terbuka Microsoft
- Jaga keamanan dan kredensial agar tidak ikut commit

### Dukungan Multi-Bahasa

Ini repositori poliglot dengan contoh dalam:
- **Python** - Workflow ML/AI, Jupyter notebooks, fine-tuning
- **C#/.NET** - Aplikasi enterprise, integrasi ONNX Runtime
- **JavaScript** - AI berbasis web, inferensi browser dengan WebGPU

Pilih bahasa yang paling sesuai dengan kasus penggunaan dan target deployment Anda.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber otoritatif. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->