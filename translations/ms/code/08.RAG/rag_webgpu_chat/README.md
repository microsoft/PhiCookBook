<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-07-16T17:19:54+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "ms"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo untuk mempamerkan WebGPU dan Corak RAG  
Corak RAG dengan model Phi-3 Onnx Hosted menggunakan pendekatan Retrieval-Augmented Generation, menggabungkan kehebatan model Phi-3 dengan hosting ONNX untuk penyebaran AI yang cekap. Corak ini sangat berguna untuk melatih model bagi tugasan khusus domain, menawarkan gabungan kualiti, kos efektif, dan kefahaman konteks panjang. Ia merupakan sebahagian daripada suite Azure AI, menyediakan pelbagai model yang mudah dicari, dicuba, dan digunakan, memenuhi keperluan penyesuaian pelbagai industri. Model Phi-3, termasuk Phi-3-mini, Phi-3-small, dan Phi-3-medium, tersedia di Azure AI Model Catalog dan boleh dilatih semula serta disebarkan secara kendiri atau melalui platform seperti HuggingFace dan ONNX, menunjukkan komitmen Microsoft terhadap penyelesaian AI yang mudah diakses dan berkesan.

## Apakah WebGPU  
WebGPU adalah API grafik web moden yang direka untuk memberikan akses cekap kepada unit pemprosesan grafik (GPU) peranti secara langsung dari pelayar web. Ia bertujuan menjadi pengganti WebGL, dengan beberapa penambahbaikan utama:

1. **Keserasian dengan GPU Moden**: WebGPU dibina untuk berfungsi lancar dengan seni bina GPU terkini, menggunakan API sistem seperti Vulkan, Metal, dan Direct3D 12.  
2. **Prestasi Dipertingkatkan**: Ia menyokong pengiraan GPU tujuan umum dan operasi lebih pantas, sesuai untuk rendering grafik dan tugasan pembelajaran mesin.  
3. **Ciri-ciri Lanjutan**: WebGPU memberikan akses kepada keupayaan GPU yang lebih maju, membolehkan beban kerja grafik dan pengiraan yang lebih kompleks dan dinamik.  
4. **Beban Kerja JavaScript Dikurangkan**: Dengan memindahkan lebih banyak tugasan ke GPU, WebGPU mengurangkan beban kerja JavaScript dengan ketara, menghasilkan prestasi lebih baik dan pengalaman lebih lancar.

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
- Dalam Firefox Nightly, masukkan about:config di bar alamat dan tetapkan `dom.webgpu.enabled` kepada true.

### Menyediakan GPU untuk Microsoft Edge  

Berikut adalah langkah-langkah untuk menyediakan GPU berprestasi tinggi bagi Microsoft Edge di Windows:

- **Buka Tetapan:** Klik menu Mula dan pilih Tetapan.  
- **Tetapan Sistem:** Pergi ke Sistem dan kemudian Paparan.  
- **Tetapan Grafik:** Skrol ke bawah dan klik pada Tetapan Grafik.  
- **Pilih Aplikasi:** Di bawah “Pilih aplikasi untuk menetapkan keutamaan,” pilih Aplikasi Desktop dan kemudian Semak Imbas.  
- **Pilih Edge:** Navigasi ke folder pemasangan Edge (biasanya `C:\Program Files (x86)\Microsoft\Edge\Application`) dan pilih `msedge.exe`.  
- **Tetapkan Keutamaan:** Klik Pilihan, pilih Prestasi Tinggi, dan kemudian klik Simpan.  
Ini akan memastikan Microsoft Edge menggunakan GPU berprestasi tinggi anda untuk prestasi lebih baik.  
- **Mulakan semula** mesin anda untuk tetapan ini berkuat kuasa.

### Buka Codespace Anda:  
Navigasi ke repositori anda di GitHub.  
Klik butang Code dan pilih Open with Codespaces.

Jika anda belum mempunyai Codespace, anda boleh buat satu dengan klik New codespace.

**Nota** Memasang Persekitaran Node dalam codespace anda  
Menjalankan demo npm dari GitHub Codespace adalah cara terbaik untuk menguji dan membangunkan projek anda. Berikut panduan langkah demi langkah untuk membantu anda bermula:

### Sediakan Persekitaran Anda:  
Setelah Codespace anda dibuka, pastikan Node.js dan npm telah dipasang. Anda boleh periksa dengan menjalankan:  
```
node -v
```  
```
npm -v
```

Jika belum dipasang, anda boleh pasang menggunakan:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Navigasi ke Direktori Projek Anda:  
Gunakan terminal untuk pergi ke direktori di mana projek npm anda berada:  
```
cd path/to/your/project
```

### Pasang Kebergantungan:  
Jalankan arahan berikut untuk memasang semua kebergantungan yang disenaraikan dalam fail package.json anda:  

```
npm install
```

### Jalankan Demo:  
Setelah kebergantungan dipasang, anda boleh jalankan skrip demo anda. Biasanya ia ditentukan dalam bahagian skrip package.json. Contohnya, jika skrip demo anda bernama start, anda boleh jalankan:  

```
npm run build
```  
```
npm run dev
```

### Akses Demo:  
Jika demo anda melibatkan pelayan web, Codespaces akan menyediakan URL untuk mengaksesnya. Cari notifikasi atau periksa tab Ports untuk mendapatkan URL.

**Nota:** Model perlu disimpan dalam cache pelayar, jadi mungkin mengambil masa untuk dimuatkan.

### Demo RAG  
Muat naik fail markdown `intro_rag.md` untuk melengkapkan penyelesaian RAG. Jika menggunakan codespaces, anda boleh muat turun fail yang terletak di `01.InferencePhi3/docs/`

### Pilih Fail Anda:  
Klik butang yang bertulis “Choose File” untuk memilih dokumen yang ingin dimuat naik.

### Muat Naik Dokumen:  
Selepas memilih fail, klik butang “Upload” untuk memuatkan dokumen anda bagi RAG (Retrieval-Augmented Generation).

### Mulakan Sembang Anda:  
Setelah dokumen dimuat naik, anda boleh mula sesi sembang menggunakan RAG berdasarkan kandungan dokumen anda.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.