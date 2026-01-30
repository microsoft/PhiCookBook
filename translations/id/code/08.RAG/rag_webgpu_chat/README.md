Phi-3-mini WebGPU RAG Chatbot

## Demo untuk menampilkan WebGPU dan Pola RAG  
Pola RAG dengan model Phi-3 Onnx Hosted memanfaatkan pendekatan Retrieval-Augmented Generation, menggabungkan kekuatan model Phi-3 dengan hosting ONNX untuk penerapan AI yang efisien. Pola ini sangat berguna dalam penyetelan model untuk tugas spesifik domain, menawarkan kombinasi kualitas, biaya yang efektif, dan pemahaman konteks panjang. Ini merupakan bagian dari rangkaian Azure AI, menyediakan berbagai model yang mudah ditemukan, dicoba, dan digunakan, memenuhi kebutuhan kustomisasi berbagai industri. Model Phi-3, termasuk Phi-3-mini, Phi-3-small, dan Phi-3-medium, tersedia di Azure AI Model Catalog dan dapat disetel ulang serta diterapkan secara mandiri atau melalui platform seperti HuggingFace dan ONNX, menunjukkan komitmen Microsoft terhadap solusi AI yang mudah diakses dan efisien.

## Apa itu WebGPU  
WebGPU adalah API grafis web modern yang dirancang untuk memberikan akses efisien ke unit pemrosesan grafis (GPU) perangkat secara langsung dari browser web. Ini dimaksudkan sebagai penerus WebGL, dengan beberapa peningkatan utama:

1. **Kompatibilitas dengan GPU Modern**: WebGPU dibangun untuk bekerja mulus dengan arsitektur GPU kontemporer, memanfaatkan API sistem seperti Vulkan, Metal, dan Direct3D 12.  
2. **Performa yang Ditingkatkan**: Mendukung komputasi GPU tujuan umum dan operasi yang lebih cepat, membuatnya cocok untuk rendering grafis dan tugas pembelajaran mesin.  
3. **Fitur Lanjutan**: WebGPU memberikan akses ke kemampuan GPU yang lebih canggih, memungkinkan beban kerja grafis dan komputasi yang lebih kompleks dan dinamis.  
4. **Beban Kerja JavaScript yang Berkurang**: Dengan memindahkan lebih banyak tugas ke GPU, WebGPU secara signifikan mengurangi beban kerja pada JavaScript, menghasilkan performa yang lebih baik dan pengalaman yang lebih lancar.

WebGPU saat ini didukung di browser seperti Google Chrome, dengan upaya berkelanjutan untuk memperluas dukungan ke platform lain.

### 03.WebGPU  
Lingkungan yang Dibutuhkan:

**Browser yang didukung:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Mengaktifkan WebGPU:

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
- Di Firefox Nightly, masukkan about:config di bilah alamat dan `set dom.webgpu.enabled ke true`.

### Menyiapkan GPU untuk Microsoft Edge  

Berikut langkah-langkah untuk mengatur GPU berperforma tinggi untuk Microsoft Edge di Windows:

- **Buka Pengaturan:** Klik menu Start dan pilih Settings.  
- **Pengaturan Sistem:** Pergi ke System lalu Display.  
- **Pengaturan Grafis:** Gulir ke bawah dan klik Graphics settings.  
- **Pilih Aplikasi:** Di bawah “Choose an app to set preference,” pilih Desktop app lalu Browse.  
- **Pilih Edge:** Arahkan ke folder instalasi Edge (biasanya `C:\Program Files (x86)\Microsoft\Edge\Application`) dan pilih `msedge.exe`.  
- **Atur Preferensi:** Klik Options, pilih High performance, lalu klik Save.  
Ini akan memastikan Microsoft Edge menggunakan GPU berperforma tinggi Anda untuk performa yang lebih baik.  
- **Restart** komputer Anda agar pengaturan ini berlaku.

### Buka Codespace Anda:  
Arahkan ke repositori Anda di GitHub.  
Klik tombol Code dan pilih Open with Codespaces.

Jika Anda belum memiliki Codespace, Anda bisa membuatnya dengan mengklik New codespace.

**Catatan** Menginstal Lingkungan Node di codespace Anda  
Menjalankan demo npm dari GitHub Codespace adalah cara yang bagus untuk menguji dan mengembangkan proyek Anda. Berikut panduan langkah demi langkah untuk memulai:

### Siapkan Lingkungan Anda:  
Setelah Codespace terbuka, pastikan Node.js dan npm sudah terpasang. Anda bisa memeriksanya dengan menjalankan:  
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

### Arahkan ke Direktori Proyek Anda:  
Gunakan terminal untuk masuk ke direktori tempat proyek npm Anda berada:  
```
cd path/to/your/project
```

### Instal Dependensi:  
Jalankan perintah berikut untuk menginstal semua dependensi yang tercantum di file package.json Anda:  

```
npm install
```

### Jalankan Demo:  
Setelah dependensi terpasang, Anda bisa menjalankan skrip demo Anda. Biasanya ini ditentukan di bagian scripts pada package.json. Misalnya, jika skrip demo Anda bernama start, Anda bisa menjalankan:  

```
npm run build
```  
```
npm run dev
```

### Akses Demo:  
Jika demo Anda melibatkan server web, Codespaces akan menyediakan URL untuk mengaksesnya. Cari notifikasi atau periksa tab Ports untuk menemukan URL tersebut.

**Catatan:** Model perlu di-cache di browser, jadi mungkin butuh waktu untuk memuat.

### Demo RAG  
Unggah file markdown `intro_rag.md` untuk menyelesaikan solusi RAG. Jika menggunakan codespaces, Anda bisa mengunduh file yang terletak di `01.InferencePhi3/docs/`

### Pilih File Anda:  
Klik tombol “Choose File” untuk memilih dokumen yang ingin Anda unggah.

### Unggah Dokumen:  
Setelah memilih file, klik tombol “Upload” untuk memuat dokumen Anda ke RAG (Retrieval-Augmented Generation).

### Mulai Chat Anda:  
Setelah dokumen diunggah, Anda bisa memulai sesi chat menggunakan RAG berdasarkan isi dokumen Anda.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.