<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-05T08:59:14+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "id"
}
-->
# **Mengkuantifikasi Keluarga Phi**

Kuantisasi model merujuk pada proses pemetaan parameter (seperti bobot dan nilai aktivasi) dalam model jaringan saraf dari rentang nilai besar (biasanya rentang nilai kontinu) ke rentang nilai terbatas yang lebih kecil. Teknologi ini dapat mengurangi ukuran dan kompleksitas komputasi model serta meningkatkan efisiensi operasional model di lingkungan dengan sumber daya terbatas seperti perangkat seluler atau sistem tertanam. Kuantisasi model mencapai kompresi dengan mengurangi presisi parameter, tetapi juga menghadirkan kehilangan presisi tertentu. Oleh karena itu, dalam proses kuantisasi, perlu menyeimbangkan ukuran model, kompleksitas komputasi, dan presisi. Metode kuantisasi umum meliputi kuantisasi titik tetap, kuantisasi titik mengambang, dan lain-lain. Anda dapat memilih strategi kuantisasi yang sesuai berdasarkan skenario dan kebutuhan spesifik.

Kami berharap dapat menerapkan model GenAI ke perangkat edge dan memungkinkan lebih banyak perangkat masuk ke dalam skenario GenAI, seperti perangkat seluler, AI PC/Copilot+PC, dan perangkat IoT tradisional. Melalui model kuantisasi, kita dapat menerapkannya ke berbagai perangkat edge berdasarkan perangkat yang berbeda. Dikombinasikan dengan kerangka akselerasi model dan model kuantisasi yang disediakan oleh produsen perangkat keras, kita dapat membangun skenario aplikasi SLM yang lebih baik.

Dalam skenario kuantisasi, kami memiliki presisi yang berbeda (INT4, INT8, FP16, FP32). Berikut adalah penjelasan mengenai presisi kuantisasi yang umum digunakan

### **INT4**

Kuantisasi INT4 adalah metode kuantisasi radikal yang mengkuantisasi bobot dan nilai aktivasi model menjadi bilangan bulat 4-bit. Kuantisasi INT4 biasanya menghasilkan kehilangan presisi yang lebih besar karena rentang representasi yang lebih kecil dan presisi yang lebih rendah. Namun, dibandingkan dengan kuantisasi INT8, kuantisasi INT4 dapat lebih jauh mengurangi kebutuhan penyimpanan dan kompleksitas komputasi model. Perlu dicatat bahwa kuantisasi INT4 relatif jarang digunakan dalam aplikasi praktis karena akurasi yang terlalu rendah dapat menyebabkan penurunan kinerja model yang signifikan. Selain itu, tidak semua perangkat keras mendukung operasi INT4, sehingga kompatibilitas perangkat keras perlu dipertimbangkan saat memilih metode kuantisasi.

### **INT8**

Kuantisasi INT8 adalah proses mengubah bobot dan aktivasi model dari angka titik mengambang menjadi bilangan bulat 8-bit. Meskipun rentang numerik yang diwakili oleh bilangan bulat INT8 lebih kecil dan kurang presisi, ini dapat secara signifikan mengurangi kebutuhan penyimpanan dan perhitungan. Dalam kuantisasi INT8, bobot dan nilai aktivasi model melewati proses kuantisasi, termasuk penskalaan dan offset, untuk mempertahankan informasi titik mengambang asli sebanyak mungkin. Selama inferensi, nilai-nilai kuantisasi ini akan didekuantisasi kembali ke angka titik mengambang untuk perhitungan, lalu dikuantisasi kembali ke INT8 untuk langkah berikutnya. Metode ini dapat memberikan akurasi yang cukup dalam sebagian besar aplikasi sambil mempertahankan efisiensi komputasi yang tinggi.

### **FP16**

Format FP16, yaitu angka titik mengambang 16-bit (float16), mengurangi jejak memori hingga setengah dibandingkan dengan angka titik mengambang 32-bit (float32), yang memberikan keuntungan signifikan dalam aplikasi pembelajaran mendalam skala besar. Format FP16 memungkinkan memuat model yang lebih besar atau memproses data lebih banyak dalam batasan memori GPU yang sama. Seiring berjalannya waktu dan perangkat keras GPU modern terus mendukung operasi FP16, menggunakan format FP16 juga dapat membawa peningkatan kecepatan komputasi. Namun, format FP16 juga memiliki kekurangan bawaan, yaitu presisi yang lebih rendah, yang dapat menyebabkan ketidakstabilan numerik atau kehilangan presisi dalam beberapa kasus.

### **FP32**

Format FP32 memberikan presisi yang lebih tinggi dan dapat merepresentasikan rentang nilai yang luas secara akurat. Dalam skenario di mana operasi matematis yang kompleks dilakukan atau hasil presisi tinggi diperlukan, format FP32 lebih disukai. Namun, akurasi tinggi juga berarti penggunaan memori yang lebih banyak dan waktu perhitungan yang lebih lama. Untuk model pembelajaran mendalam skala besar, terutama ketika terdapat banyak parameter model dan jumlah data yang sangat besar, format FP32 dapat menyebabkan kekurangan memori GPU atau penurunan kecepatan inferensi.

Pada perangkat seluler atau perangkat IoT, kita dapat mengubah model Phi-3.x menjadi INT4, sedangkan AI PC / Copilot PC dapat menggunakan presisi lebih tinggi seperti INT8, FP16, FP32.

Saat ini, berbagai produsen perangkat keras memiliki kerangka kerja yang berbeda untuk mendukung model generatif, seperti OpenVINO milik Intel, QNN milik Qualcomm, MLX milik Apple, dan CUDA milik Nvidia, yang digabungkan dengan kuantisasi model untuk menyelesaikan penerapan lokal.

Dalam hal teknologi, kami memiliki dukungan format yang berbeda setelah kuantisasi, seperti format PyTorch / TensorFlow, GGUF, dan ONNX. Saya telah membuat perbandingan format dan skenario aplikasi antara GGUF dan ONNX. Di sini saya merekomendasikan format kuantisasi ONNX, yang memiliki dukungan yang baik dari kerangka model hingga perangkat keras. Dalam bab ini, kita akan fokus pada ONNX Runtime untuk GenAI, OpenVINO, dan Apple MLX untuk melakukan kuantisasi model (jika Anda memiliki cara yang lebih baik, Anda juga dapat memberikannya kepada kami dengan mengirimkan PR)

**Bab ini mencakup**

1. [Mengkuantisasi Phi-3.5 / 4 menggunakan llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Mengkuantisasi Phi-3.5 / 4 menggunakan ekstensi Generative AI untuk onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Mengkuantisasi Phi-3.5 / 4 menggunakan Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Mengkuantisasi Phi-3.5 / 4 menggunakan Kerangka Kerja Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->