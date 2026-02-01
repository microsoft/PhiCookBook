# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo untuk menampilkan WebGPU dan Pola RAG

Pola RAG dengan model Phi-3.5 Onnx Hosted memanfaatkan pendekatan Retrieval-Augmented Generation, menggabungkan kekuatan model Phi-3.5 dengan hosting ONNX untuk penyebaran AI yang efisien. Pola ini sangat berguna dalam penyetelan model untuk tugas khusus domain, menawarkan kombinasi kualitas, biaya yang efektif, dan pemahaman konteks panjang. Ini merupakan bagian dari rangkaian Azure AI, menyediakan berbagai model yang mudah ditemukan, dicoba, dan digunakan, memenuhi kebutuhan kustomisasi berbagai industri.

## Apa itu WebGPU  
WebGPU adalah API grafis web modern yang dirancang untuk memberikan akses efisien ke unit pemrosesan grafis (GPU) perangkat secara langsung dari browser web. WebGPU dimaksudkan sebagai penerus WebGL, dengan beberapa peningkatan utama:

1. **Kompatibilitas dengan GPU Modern**: WebGPU dibangun agar bekerja mulus dengan arsitektur GPU kontemporer, memanfaatkan API sistem seperti Vulkan, Metal, dan Direct3D 12.
2. **Performa yang Ditingkatkan**: Mendukung komputasi GPU tujuan umum dan operasi yang lebih cepat, sehingga cocok untuk rendering grafis dan tugas pembelajaran mesin.
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
Di bilah alamat, ketik `chrome://flags` lalu tekan Enter.

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

Berikut langkah-langkah untuk mengatur GPU berperforma tinggi di Microsoft Edge pada Windows:

- **Buka Pengaturan:** Klik menu Start dan pilih Settings.  
- **Pengaturan Sistem:** Buka System lalu Display.  
- **Pengaturan Grafis:** Gulir ke bawah dan klik Graphics settings.  
- **Pilih Aplikasi:** Di bawah “Choose an app to set preference,” pilih Desktop app lalu klik Browse.  
- **Pilih Edge:** Arahkan ke folder instalasi Edge (biasanya `C:\Program Files (x86)\Microsoft\Edge\Application`) dan pilih `msedge.exe`.  
- **Atur Preferensi:** Klik Options, pilih High performance, lalu klik Save.  
Ini akan memastikan Microsoft Edge menggunakan GPU berperforma tinggi Anda untuk performa yang lebih baik.  
- **Restart** komputer Anda agar pengaturan ini berlaku.

### Contoh : Silakan [klik tautan ini](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.