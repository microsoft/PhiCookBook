<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-05-09T05:21:05+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "id"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo untuk menampilkan WebGPU dan Pola RAG  
Pola RAG dengan model Phi-3 Onnx Hosted memanfaatkan pendekatan Retrieval-Augmented Generation, menggabungkan kekuatan model Phi-3 dengan hosting ONNX untuk penerapan AI yang efisien. Pola ini sangat berguna dalam menyempurnakan model untuk tugas spesifik domain, menawarkan kombinasi kualitas, biaya yang efektif, dan pemahaman konteks panjang. Ini merupakan bagian dari suite Azure AI, menyediakan berbagai pilihan model yang mudah ditemukan, dicoba, dan digunakan, memenuhi kebutuhan kustomisasi di berbagai industri. Model Phi-3, termasuk Phi-3-mini, Phi-3-small, dan Phi-3-medium, tersedia di Azure AI Model Catalog dan dapat disesuaikan serta diterapkan secara mandiri atau melalui platform seperti HuggingFace dan ONNX, menunjukkan komitmen Microsoft pada solusi AI yang mudah diakses dan efisien.

## Apa itu WebGPU  
WebGPU adalah API grafis web modern yang dirancang untuk memberikan akses efisien ke unit pemrosesan grafis (GPU) perangkat langsung dari browser web. Ini dimaksudkan sebagai penerus WebGL, menawarkan beberapa peningkatan utama:

1. **Kompatibilitas dengan GPU Modern**: WebGPU dibuat untuk bekerja mulus dengan arsitektur GPU kontemporer, memanfaatkan API sistem seperti Vulkan, Metal, dan Direct3D 12.  
2. **Performa yang Ditingkatkan**: Mendukung komputasi GPU tujuan umum dan operasi yang lebih cepat, cocok untuk rendering grafis dan tugas pembelajaran mesin.  
3. **Fitur Lanjutan**: WebGPU memberikan akses ke kemampuan GPU yang lebih maju, memungkinkan beban kerja grafis dan komputasi yang lebih kompleks dan dinamis.  
4. **Beban Kerja JavaScript yang Berkurang**: Dengan memindahkan lebih banyak tugas ke GPU, WebGPU secara signifikan mengurangi beban kerja pada JavaScript, menghasilkan performa lebih baik dan pengalaman yang lebih lancar.

WebGPU saat ini didukung di browser seperti Google Chrome, dengan pekerjaan berkelanjutan untuk memperluas dukungan ke platform lain.

### 03.WebGPU  
Lingkungan yang Dibutuhkan:

**Browser yang Didukung:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Aktifkan WebGPU:

- Di Chrome/Microsoft Edge  

Aktifkan flag `chrome://flags/#enable-unsafe-webgpu`.

#### Buka Browser Anda:  
Jalankan Google Chrome atau Microsoft Edge.

#### Akses Halaman Flags:  
Di bilah alamat, ketik `chrome://flags` dan tekan Enter.

#### Cari Flag:  
Di kotak pencarian di bagian atas halaman, ketik 'enable-unsafe-webgpu'

#### Aktifkan Flag:  
Temukan flag #enable-unsafe-webgpu dalam daftar hasil.

Klik menu dropdown di sebelahnya dan pilih Enabled.

#### Mulai Ulang Browser Anda:  

Setelah mengaktifkan flag, Anda perlu memulai ulang browser agar perubahan berlaku. Klik tombol Relaunch yang muncul di bagian bawah halaman.

- Untuk Linux, jalankan browser dengan `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) sudah mengaktifkan WebGPU secara default.  
- Di Firefox Nightly, masukkan about:config di bilah alamat dan `set dom.webgpu.enabled to true`.

### Mengatur GPU untuk Microsoft Edge  

Berikut langkah-langkah untuk mengatur GPU performa tinggi di Microsoft Edge pada Windows:

- **Buka Pengaturan:** Klik menu Start dan pilih Settings.  
- **Pengaturan Sistem:** Buka System lalu Display.  
- **Pengaturan Grafis:** Gulir ke bawah dan klik Graphics settings.  
- **Pilih Aplikasi:** Di bawah “Choose an app to set preference,” pilih Desktop app lalu Browse.  
- **Pilih Edge:** Arahkan ke folder instalasi Edge (biasanya `C:\Program Files (x86)\Microsoft\Edge\Application`) dan pilih `msedge.exe`.  
- **Atur Preferensi:** Klik Options, pilih High performance, lalu klik Save.  
Ini akan memastikan Microsoft Edge menggunakan GPU performa tinggi Anda untuk performa yang lebih baik.  
- **Restart** komputer Anda agar pengaturan ini berlaku.

### Buka Codespace Anda:  
Navigasi ke repository Anda di GitHub.  
Klik tombol Code dan pilih Open with Codespaces.

Jika Anda belum memiliki Codespace, Anda bisa membuatnya dengan klik New codespace.

**Catatan** Instalasi Node Environment di codespace Anda  
Menjalankan demo npm dari GitHub Codespace adalah cara yang bagus untuk menguji dan mengembangkan proyek Anda. Berikut panduan langkah demi langkah untuk memulai:

### Siapkan Lingkungan Anda:  
Setelah Codespace terbuka, pastikan Node.js dan npm sudah terpasang. Anda bisa cek dengan menjalankan:  
```
node -v
```  
```
npm -v
```

Jika belum terpasang, Anda bisa menginstalnya dengan:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Masuk ke Direktori Proyek Anda:  
Gunakan terminal untuk masuk ke direktori tempat proyek npm Anda berada:  
```
cd path/to/your/project
```

### Instal Dependensi:  
Jalankan perintah berikut untuk menginstal semua dependensi yang diperlukan sesuai daftar di package.json:  

```
npm install
```

### Jalankan Demo:  
Setelah dependensi terinstal, Anda bisa menjalankan skrip demo Anda. Biasanya ditentukan di bagian scripts pada package.json. Misalnya, jika skrip demo bernama start, Anda bisa menjalankan:  

```
npm run build
```  
```
npm run dev
```

### Akses Demo:  
Jika demo Anda melibatkan server web, Codespaces akan menyediakan URL untuk mengaksesnya. Cari notifikasi atau cek tab Ports untuk menemukan URL.

**Catatan:** Model perlu di-cache di browser, jadi mungkin butuh waktu untuk memuat.

### Demo RAG  
Unggah file markdown `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Pilih File Anda:  
Klik tombol “Choose File” untuk memilih dokumen yang ingin Anda unggah.

### Unggah Dokumen:  
Setelah memilih file, klik tombol “Upload” untuk memuat dokumen Anda ke RAG (Retrieval-Augmented Generation).

### Mulai Chat Anda:  
Setelah dokumen terunggah, Anda bisa memulai sesi chat menggunakan RAG berdasarkan isi dokumen Anda.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.