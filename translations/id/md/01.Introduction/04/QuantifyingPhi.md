<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-07-16T21:48:44+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "id"
}
-->
# **Mengkuantifikasi Keluarga Phi**

Kuantisasi model mengacu pada proses memetakan parameter (seperti bobot dan nilai aktivasi) dalam model jaringan saraf dari rentang nilai besar (biasanya rentang nilai kontinu) ke rentang nilai terbatas yang lebih kecil. Teknologi ini dapat mengurangi ukuran dan kompleksitas komputasi model serta meningkatkan efisiensi operasional model di lingkungan dengan sumber daya terbatas seperti perangkat seluler atau sistem tertanam. Kuantisasi model mencapai kompresi dengan mengurangi presisi parameter, namun juga memperkenalkan kehilangan presisi tertentu. Oleh karena itu, dalam proses kuantisasi, perlu menyeimbangkan ukuran model, kompleksitas komputasi, dan presisi. Metode kuantisasi yang umum meliputi kuantisasi fixed-point, kuantisasi floating-point, dan lain-lain. Anda dapat memilih strategi kuantisasi yang sesuai berdasarkan skenario dan kebutuhan spesifik.

Kami berharap dapat menerapkan model GenAI ke perangkat edge dan memungkinkan lebih banyak perangkat masuk ke skenario GenAI, seperti perangkat seluler, AI PC/Copilot+PC, dan perangkat IoT tradisional. Melalui model kuantisasi, kita dapat menerapkannya ke berbagai perangkat edge berdasarkan jenis perangkat yang berbeda. Dikombinasikan dengan kerangka percepatan model dan model kuantisasi yang disediakan oleh produsen perangkat keras, kita dapat membangun skenario aplikasi SLM yang lebih baik.

Dalam skenario kuantisasi, kita memiliki berbagai presisi (INT4, INT8, FP16, FP32). Berikut adalah penjelasan mengenai presisi kuantisasi yang umum digunakan.

### **INT4**

Kuantisasi INT4 adalah metode kuantisasi yang sangat agresif yang mengkuantisasi bobot dan nilai aktivasi model menjadi bilangan bulat 4-bit. Kuantisasi INT4 biasanya menghasilkan kehilangan presisi yang lebih besar karena rentang representasi yang lebih kecil dan presisi yang lebih rendah. Namun, dibandingkan dengan kuantisasi INT8, kuantisasi INT4 dapat lebih mengurangi kebutuhan penyimpanan dan kompleksitas komputasi model. Perlu dicatat bahwa kuantisasi INT4 relatif jarang digunakan dalam aplikasi praktis, karena akurasi yang terlalu rendah dapat menyebabkan penurunan kinerja model yang signifikan. Selain itu, tidak semua perangkat keras mendukung operasi INT4, sehingga kompatibilitas perangkat keras perlu dipertimbangkan saat memilih metode kuantisasi.

### **INT8**

Kuantisasi INT8 adalah proses mengubah bobot dan aktivasi model dari angka floating point menjadi bilangan bulat 8-bit. Meskipun rentang angka yang diwakili oleh bilangan bulat INT8 lebih kecil dan kurang presisi, metode ini dapat secara signifikan mengurangi kebutuhan penyimpanan dan perhitungan. Dalam kuantisasi INT8, bobot dan nilai aktivasi model melewati proses kuantisasi, termasuk penskalaan dan offset, untuk mempertahankan informasi floating point asli sebanyak mungkin. Saat inferensi, nilai-nilai yang telah dikuantisasi ini akan didekuantisasi kembali ke angka floating point untuk perhitungan, kemudian dikuantisasi lagi ke INT8 untuk langkah berikutnya. Metode ini dapat memberikan akurasi yang cukup dalam sebagian besar aplikasi sambil mempertahankan efisiensi komputasi yang tinggi.

### **FP16**

Format FP16, yaitu angka floating point 16-bit (float16), mengurangi penggunaan memori hingga setengah dibandingkan dengan angka floating point 32-bit (float32), yang memberikan keuntungan signifikan dalam aplikasi pembelajaran mendalam skala besar. Format FP16 memungkinkan pemuatan model yang lebih besar atau pemrosesan data lebih banyak dalam batasan memori GPU yang sama. Karena perangkat keras GPU modern terus mendukung operasi FP16, penggunaan format FP16 juga dapat meningkatkan kecepatan komputasi. Namun, format FP16 juga memiliki kekurangan bawaan, yaitu presisi yang lebih rendah, yang dalam beberapa kasus dapat menyebabkan ketidakstabilan numerik atau kehilangan presisi.

### **FP32**

Format FP32 menyediakan presisi yang lebih tinggi dan dapat merepresentasikan rentang nilai yang luas dengan akurat. Dalam skenario di mana operasi matematika kompleks dilakukan atau hasil dengan presisi tinggi diperlukan, format FP32 lebih disukai. Namun, presisi tinggi juga berarti penggunaan memori yang lebih besar dan waktu perhitungan yang lebih lama. Untuk model pembelajaran mendalam skala besar, terutama ketika terdapat banyak parameter model dan data dalam jumlah besar, format FP32 dapat menyebabkan kekurangan memori GPU atau penurunan kecepatan inferensi.

Pada perangkat seluler atau perangkat IoT, kita dapat mengonversi model Phi-3.x ke INT4, sementara AI PC / Copilot PC dapat menggunakan presisi lebih tinggi seperti INT8, FP16, FP32.

Saat ini, berbagai produsen perangkat keras memiliki kerangka kerja yang berbeda untuk mendukung model generatif, seperti OpenVINO dari Intel, QNN dari Qualcomm, MLX dari Apple, dan CUDA dari Nvidia, yang dikombinasikan dengan kuantisasi model untuk menyelesaikan penerapan lokal.

Dari sisi teknologi, kita memiliki dukungan format yang berbeda setelah kuantisasi, seperti format PyTorch / Tensorflow, GGUF, dan ONNX. Saya telah melakukan perbandingan format dan skenario aplikasi antara GGUF dan ONNX. Di sini saya merekomendasikan format kuantisasi ONNX, yang memiliki dukungan baik dari kerangka model hingga perangkat keras. Dalam bab ini, kita akan fokus pada ONNX Runtime untuk GenAI, OpenVINO, dan Apple MLX untuk melakukan kuantisasi model (jika Anda memiliki cara yang lebih baik, Anda juga dapat memberikannya kepada kami dengan mengirimkan PR).

**Bab ini mencakup**

1. [Mengkuantisasi Phi-3.5 / 4 menggunakan llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Mengkuantisasi Phi-3.5 / 4 menggunakan ekstensi Generative AI untuk onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Mengkuantisasi Phi-3.5 / 4 menggunakan Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Mengkuantisasi Phi-3.5 / 4 menggunakan Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.