# AGENTS.md

## Gambaran Projek

PhiCookBook ialah repositori buku masakan yang komprehensif mengandungi contoh-contoh praktikal, tutorial, dan dokumentasi untuk bekerja dengan keluarga Model Bahasa Kecil (SLM) Microsoft Phi. Repositori ini mempamerkan pelbagai kes penggunaan termasuk inferens, penalaan halus, kuantisasi, pelaksanaan RAG, dan aplikasi multimodal merentas pelbagai platform dan rangka kerja.

**Teknologi Utama:**
- **Bahasa:** Python, C#/.NET, JavaScript/Node.js
- **Rangka Kerja:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platform:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Jenis Model:** Phi-3, Phi-3.5, Phi-4 (teks, visi, multimodal, variasi penaakulan)

**Struktur Repositori:**
- `/code/` - Contoh kod bekerja dan pelaksanaan sampel
- `/md/` - Dokumentasi terperinci, tutorial, dan panduan cara
- `/translations/` - Terjemahan pelbagai bahasa (50+ bahasa melalui aliran kerja automatik)
- `/.devcontainer/` - Konfigurasi kontena pembangunan (Python 3.12 dengan Ollama)

## Persediaan Persekitaran Pembangunan

### Menggunakan GitHub Codespaces atau Dev Containers (Disyorkan)

1. Buka dalam GitHub Codespaces (paling pantas):
   - Klik lencana "Open in GitHub Codespaces" dalam README
   - Kontena secara automatik dikonfigurasi dengan Python 3.12 dan Ollama dengan Phi-3

2. Buka dalam VS Code Dev Containers:
   - Gunakan lencana "Open in Dev Containers" dari README
   - Kontena memerlukan memori hos minimum 16GB

### Persediaan Tempatan

**Prasyarat:**
- Python 3.12 atau lebih baru
- .NET 8.0 SDK (untuk contoh C#)
- Node.js 18+ dan npm (untuk contoh JavaScript)
- 16GB RAM minimum disyorkan

**Pemasangan:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Untuk Contoh Python:**
Navigasi ke direktori contoh tertentu dan pasang kebergantungan:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # jika requirements.txt wujud
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
npm run dev  # Mulakan pelayan pembangunan
npm run build  # Bina untuk pengeluaran
```

## Organisasi Repositori

### Contoh Kod (`/code/`)

- **01.Introduce/** - Pengenalan asas dan sampel memulakan
- **03.Finetuning/** dan **04.Finetuning/** - Contoh penalaan halus dengan pelbagai kaedah
- **03.Inference/** - Contoh inferens pada perkakasan berbeza (AIPC, MLX)
- **06.E2E/** - Sampel aplikasi hujung ke hujung
- **07.Lab/** - Pelaksanaan makmal/eksperimen
- **08.RAG/** - Sampel Penjanaan Dipertingkatkan Pengambilan
- **09.UpdateSamples/** - Sampel terbaharu yang dikemaskini

### Dokumentasi (`/md/`)

- **01.Introduction/** - Panduan pengenalan, persediaan persekitaran, panduan platform
- **02.Application/** - Sampel aplikasi yang disusun mengikut jenis (Teks, Kod, Visi, Audio, dll.)
- **02.QuickStart/** - Panduan mula cepat untuk Microsoft Foundry dan GitHub Models
- **03.FineTuning/** - Dokumentasi dan tutorial penalaan halus
- **04.HOL/** - Makmal praktikal (termasuk contoh .NET)

### Format Fail

- **Jupyter Notebooks (`.ipynb`)** - Tutorial Python interaktif yang ditandakan dengan 📓 dalam README
- **Skrip Python (`.py`)** - Contoh Python berdiri sendiri
- **Projek C# (`.csproj`, `.sln`)** - Aplikasi dan sampel .NET
- **JavaScript (`.js`, `package.json`)** - Contoh berasaskan web dan Node.js
- **Markdown (`.md`)** - Dokumentasi dan panduan

## Bekerja dengan Contoh

### Menjalankan Jupyter Notebooks

Kebanyakan contoh disediakan sebagai buku nota Jupyter:
```bash
pip install jupyter notebook
jupyter notebook  # Buka antara muka pelayar
# Navigasi ke fail .ipynb yang dikehendaki
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
npm run dev  # Pembangunan dengan muat semula panas
```

## Ujian

Repositori ini mengandungi kod contoh dan tutorial daripada projek perisian tradisional dengan ujian unit. Pengesahan biasanya dilakukan dengan:

1. **Menjalankan contoh** - Setiap contoh harus berjalan tanpa ralat
2. **Memeriksa keluaran** - Semak respons model adalah sesuai
3. **Mengikuti tutorial** - Panduan langkah demi langkah harus berfungsi seperti didokumentasikan

**Pendekatan pengesahan biasa:**
- Uji pelaksanaan contoh dalam persekitaran sasaran
- Sahkan pemasangan kebergantungan dengan betul
- Periksa muat turun/pemuatan model berjaya
- Sahkan tingkah laku dijangka sepadan dengan dokumentasi

## Gaya Kod dan Konvensyen

### Garis Panduan Umum

- Contoh mesti jelas, diterangkan dengan baik, dan mendidik
- Ikut konvensyen khusus bahasa (PEP 8 untuk Python, piawaian C# untuk .NET)
- Fokus contoh pada menunjukkan keupayaan model Phi tertentu
- Sertakan komen menerangkan konsep utama dan parameter model khusus

### Standard Dokumentasi

**Format URL:**
- Gunakan format `[text](../../url)` tanpa ruang tambahan
- Pautan relatif: Gunakan `./` untuk direktori semasa, `../` untuk induk
- Tiada lokasi khusus negara dalam URL (elakkan `/en-us/`, `/en/`)

**Imej:**
- Simpan semua imej dalam direktori `/imgs/`
- Gunakan nama deskriptif dengan aksara Inggeris, nombor, dan tanda sengkang
- Contoh: `phi-3-architecture.png`

**Fail Markdown:**
- Rujuk contoh sebenar dalam direktori `/code/`
- Kekalkan penyelarasan dokumentasi dengan perubahan kod
- Gunakan emoji 📓 untuk menandakan pautan buku nota Jupyter dalam README

### Pengurusan Fail

- Contoh kod dalam `/code/` disusun mengikut topik/ciri
- Dokumentasi dalam `/md/` mencerminkan struktur kod bila berkenaan
- Simpan fail berkaitan (buku nota, skrip, konfigurasi) bersama dalam subdirektori

## Garis Panduan Permintaan Tarik

### Sebelum Menghantar

1. **Fork repositori** ke akaun anda
2. **Pisahkan PR mengikut jenis:**
   - Pembetulan pepijat dalam satu PR
   - Kemas kini dokumentasi dalam satu lagi
   - Contoh baharu dalam PR berasingan
   - Pembetulan typo boleh digabungkan

3. **Menangani konflik penggabungan:**
   - Kemas kini cawangan `main` tempatan sebelum membuat perubahan
   - Selaraskan dengan upstream secara kerap

4. **PR Terjemahan:**
   - Mesti termasuk terjemahan untuk SEMUA fail dalam folder
   - Kekalkan struktur konsisten dengan bahasa asal

### Semakan Diperlukan

PR secara automatik menjalankan aliran kerja GitHub untuk mengesahkan:

1. **Pengesahan laluan relatif** - Semua pautan dalaman mesti berfungsi
   - Uji pautan secara tempatan: Ctrl+Klik dalam VS Code
   - Gunakan cadangan laluan dari VS Code (`./` atau `../`)

2. **Semakan lokasi URL** - URL web mesti tiada lokasi negara
   - Alih keluar `/en-us/`, `/en/`, atau kod bahasa lain
   - Gunakan URL antarabangsa generik

3. **Semakan URL rosak** - Semua URL mesti pulang status 200
   - Sahkan pautan boleh diakses sebelum menghantar
   - Nota: Sesetengah kegagalan mungkin disebabkan sekatan rangkaian

### Format Tajuk PR

```
[component] Brief description
```

Contoh:
- `[docs] Tambah tutorial inferens Phi-4`
- `[code] Betulkan contoh integrasi ONNX Runtime`
- `[translation] Tambah terjemahan Jepun untuk panduan pengenalan`

## Corak Pembangunan Lazim

### Bekerja dengan Model Phi

**Pemuat Model:**
- Contoh menggunakan pelbagai rangka kerja: Transformers, ONNX Runtime, MLX, OpenVINO
- Model biasanya dimuat turun dari Hugging Face, Azure, atau GitHub Models
- Semak keserasian model dengan perkakasan anda (CPU, GPU, NPU)

**Corak Inferens:**
- Penjanaan teks: Kebanyakan contoh menggunakan variasi chat/instruct
- Visi: Phi-3-vision dan Phi-4-multimodal untuk pemahaman imej
- Audio: Phi-4-multimodal menyokong input audio
- Penaakulan: Variasi Phi-4-reasoning untuk tugas penaakulan lanjutan

### Nota Khusus Platform

**Microsoft Foundry:**
- Memerlukan langganan Azure dan kekunci API
- Lihat `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Tahap percuma tersedia untuk ujian
- Lihat `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Inferens Tempatan:**
- ONNX Runtime: Lintas platform, inferens dioptimumkan
- Ollama: Pengurusan model tempatan mudah (pra-konfigurasi dalam kontena pembangunan)
- Apple MLX: Dioptimumkan untuk Apple Silicon

## Penyelesaian Masalah

### Isu Lazim

**Isu Memori:**
- Model Phi memerlukan RAM yang besar (terutamanya variasi visi/multimodal)
- Gunakan model kuantisasi untuk persekitaran berhad sumber
- Lihat `/md/01.Introduction/04/QuantifyingPhi.md`

**Konflik Kebergantungan:**
- Contoh Python mungkin ada keperluan versi khusus
- Gunakan persekitaran maya untuk setiap contoh
- Semak fail `requirements.txt` individu

**Kegagalan Muat Turun Model:**
- Model besar mungkin tamat masa pada sambungan perlahan
- Pertimbangkan menggunakan persekitaran awan (Codespaces, Azure)
- Semak cache Hugging Face: `~/.cache/huggingface/`

**Isu Projek .NET:**
- Pastikan .NET 8.0 SDK dipasang
- Gunakan `dotnet restore` sebelum bina
- Sesetengah projek ada konfigurasi khusus CUDA (Debug_Cuda)

**Contoh JavaScript/Web:**
- Gunakan Node.js 18+ untuk keserasian
- Bersihkan `node_modules` dan pasang semula jika isu berterusan
- Semak konsol pelayar untuk isu keserasian WebGPU

### Mendapatkan Bantuan

- **Discord:** Sertai Microsoft Foundry Community Discord
- **GitHub Issues:** Laporkan pepijat dan isu dalam repositori
- **GitHub Discussions:** Tanyakan soalan dan kongsi pengetahuan

## Konteks Tambahan

### AI Bertanggungjawab

Semua penggunaan model Phi perlu mengikuti prinsip AI Bertanggungjawab Microsoft:
- Keadilan, kebolehpercayaan, keselamatan
- Privasi dan keselamatan  
- Inklusiviti, ketelusan, akauntabiliti
- Gunakan Azure AI Content Safety untuk aplikasi produksi
- Lihat `/md/01.Introduction/01/01.AISafety.md`

### Terjemahan

- Menyokong 50+ bahasa melalui GitHub Action automatik
- Terjemahan dalam direktori `/translations/`
- Diselenggara oleh aliran kerja co-op-translator
- Jangan edit fail terjemahan secara manual (dijana automatik)

### Menyumbang

- Ikut garis panduan dalam `CONTRIBUTING.md`
- Setuju dengan Perjanjian Lesen Penyumbang (CLA)
- Patuhi Kod Etika Sumber Terbuka Microsoft
- Jaga keselamatan dan kelayakan dari kemas kini

### Sokongan Pelbagai Bahasa

Ini adalah repositori poliglot dengan contoh dalam:
- **Python** - Aliran kerja ML/AI, buku nota Jupyter, penalaan halus
- **C#/.NET** - Aplikasi perusahaan, integrasi ONNX Runtime
- **JavaScript** - AI berasaskan web, inferens pelayar dengan WebGPU

Pilih bahasa yang paling sesuai untuk kes penggunaan dan sasaran pelaksanaan anda.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat kritikal, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->