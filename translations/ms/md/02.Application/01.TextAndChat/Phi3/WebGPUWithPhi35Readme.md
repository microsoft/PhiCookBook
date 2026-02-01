# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo untuk mempamerkan WebGPU dan Corak RAG

Corak RAG dengan model Phi-3.5 Onnx Hosted menggunakan pendekatan Retrieval-Augmented Generation, menggabungkan kehebatan model Phi-3.5 dengan hosting ONNX untuk penyebaran AI yang cekap. Corak ini sangat berguna dalam penalaan halus model untuk tugasan khusus domain, menawarkan gabungan kualiti, kos efektif, dan pemahaman konteks panjang. Ia merupakan sebahagian daripada suite Azure AI, menyediakan pelbagai pilihan model yang mudah dicari, dicuba, dan digunakan, memenuhi keperluan penyesuaian pelbagai industri.

## Apa itu WebGPU  
WebGPU adalah API grafik web moden yang direka untuk memberikan akses cekap kepada unit pemprosesan grafik (GPU) peranti secara langsung dari pelayar web. Ia bertujuan menjadi pengganti WebGL, dengan beberapa penambahbaikan utama:

1. **Keserasian dengan GPU Moden**: WebGPU dibina untuk berfungsi lancar dengan seni bina GPU terkini, menggunakan API sistem seperti Vulkan, Metal, dan Direct3D 12.  
2. **Prestasi Dipertingkatkan**: Ia menyokong pengiraan GPU tujuan umum dan operasi lebih pantas, sesuai untuk rendering grafik dan tugasan pembelajaran mesin.  
3. **Ciri-ciri Lanjutan**: WebGPU memberikan akses kepada keupayaan GPU yang lebih maju, membolehkan beban kerja grafik dan pengiraan yang lebih kompleks dan dinamik.  
4. **Beban Kerja JavaScript Dikurangkan**: Dengan memindahkan lebih banyak tugasan ke GPU, WebGPU mengurangkan beban kerja pada JavaScript, menghasilkan prestasi lebih baik dan pengalaman lebih lancar.

WebGPU kini disokong dalam pelayar seperti Google Chrome, dengan usaha berterusan untuk memperluaskan sokongan ke platform lain.

### 03.WebGPU  
Persekitaran Diperlukan:

**Pelayar yang disokong:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Aktifkan WebGPU:

- Dalam Chrome/Microsoft Edge  

Aktifkan bendera `chrome://flags/#enable-unsafe-webgpu`.

#### Buka Pelayar Anda:  
Lancarkan Google Chrome atau Microsoft Edge.

#### Akses Halaman Flags:  
Di bar alamat, taip `chrome://flags` dan tekan Enter.

#### Cari Bendera:  
Di kotak carian di atas halaman, taip 'enable-unsafe-webgpu'

#### Aktifkan Bendera:  
Cari bendera #enable-unsafe-webgpu dalam senarai keputusan.

Klik menu lungsur di sebelahnya dan pilih Enabled.

#### Mulakan Semula Pelayar Anda:  

Selepas mengaktifkan bendera, anda perlu mulakan semula pelayar untuk perubahan berkuat kuasa. Klik butang Relaunch yang muncul di bahagian bawah halaman.

- Untuk Linux, lancarkan pelayar dengan `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) mempunyai WebGPU diaktifkan secara lalai.  
- Dalam Firefox Nightly, masukkan about:config di bar alamat dan `set dom.webgpu.enabled to true`.

### Menyediakan GPU untuk Microsoft Edge  

Berikut adalah langkah-langkah untuk menyediakan GPU berprestasi tinggi untuk Microsoft Edge di Windows:

- **Buka Tetapan:** Klik menu Mula dan pilih Tetapan.  
- **Tetapan Sistem:** Pergi ke Sistem dan kemudian Paparan.  
- **Tetapan Grafik:** Skrol ke bawah dan klik pada Tetapan Grafik.  
- **Pilih Aplikasi:** Di bawah “Pilih aplikasi untuk tetapkan keutamaan,” pilih Aplikasi Desktop dan kemudian Semak Imbas.  
- **Pilih Edge:** Navigasi ke folder pemasangan Edge (biasanya `C:\Program Files (x86)\Microsoft\Edge\Application`) dan pilih `msedge.exe`.  
- **Tetapkan Keutamaan:** Klik Pilihan, pilih Prestasi Tinggi, dan kemudian klik Simpan.  
Ini akan memastikan Microsoft Edge menggunakan GPU berprestasi tinggi anda untuk prestasi lebih baik.  
- **Mulakan semula** mesin anda supaya tetapan ini berkuat kuasa.

### Contoh : Sila [klik pautan ini](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.