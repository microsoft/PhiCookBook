<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-05-09T13:32:44+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "id"
}
-->
# **Mengkuantifikasi Keluarga Phi**

Kuantisasi model mengacu pada proses pemetaan parameter (seperti bobot dan nilai aktivasi) dalam model jaringan saraf dari rentang nilai besar (biasanya rentang nilai kontinu) ke rentang nilai terbatas yang lebih kecil. Teknologi ini dapat mengurangi ukuran dan kompleksitas komputasi model serta meningkatkan efisiensi operasional model di lingkungan dengan sumber daya terbatas seperti perangkat mobile atau sistem tertanam. Kuantisasi model mencapai kompresi dengan mengurangi presisi parameter, namun juga memperkenalkan kehilangan presisi tertentu. Oleh karena itu, dalam proses kuantisasi, perlu menyeimbangkan ukuran model, kompleksitas komputasi, dan presisi. Metode kuantisasi umum meliputi kuantisasi fixed-point, kuantisasi floating-point, dan lain-lain. Anda dapat memilih strategi kuantisasi yang sesuai berdasarkan skenario dan kebutuhan spesifik.

Kami berharap dapat menerapkan model GenAI ke perangkat edge dan memungkinkan lebih banyak perangkat masuk ke skenario GenAI, seperti perangkat mobile, AI PC/Copilot+PC, dan perangkat IoT tradisional. Melalui model kuantisasi, kita dapat menerapkannya ke berbagai perangkat edge berdasarkan perangkat yang berbeda. Dikombinasikan dengan kerangka percepatan model dan model kuantisasi yang disediakan oleh produsen perangkat keras, kita dapat membangun skenario aplikasi SLM yang lebih baik.

Dalam skenario kuantisasi, kita memiliki berbagai tingkat presisi (INT4, INT8, FP16, FP32). Berikut adalah penjelasan tentang presisi kuantisasi yang umum digunakan.

### **INT4**

Kuantisasi INT4 adalah metode kuantisasi yang radikal yang mengkuantisasi bobot dan nilai aktivasi model menjadi bilangan bulat 4-bit. Kuantisasi INT4 biasanya menghasilkan kehilangan presisi yang lebih besar karena rentang representasi yang lebih kecil dan presisi yang lebih rendah. Namun, dibandingkan dengan kuantisasi INT8, kuantisasi INT4 dapat lebih mengurangi kebutuhan penyimpanan dan kompleksitas komputasi model. Perlu dicatat bahwa kuantisasi INT4 relatif jarang digunakan dalam aplikasi praktis, karena akurasi yang terlalu rendah dapat menyebabkan penurunan kinerja model yang signifikan. Selain itu, tidak semua perangkat keras mendukung operasi INT4, sehingga kompatibilitas perangkat keras perlu dipertimbangkan saat memilih metode kuantisasi.

### **INT8**

Kuantisasi INT8 adalah proses mengubah bobot dan aktivasi model dari angka floating point menjadi bilangan bulat 8-bit. Meskipun rentang angka yang diwakili oleh bilangan bulat INT8 lebih kecil dan kurang presisi, ini dapat secara signifikan mengurangi kebutuhan penyimpanan dan perhitungan. Dalam kuantisasi INT8, bobot dan nilai aktivasi model melewati proses kuantisasi, termasuk penskalaan dan offset, untuk mempertahankan informasi floating point asli sebanyak mungkin. Saat inferensi, nilai-nilai kuantisasi ini akan didekuantisasi kembali menjadi angka floating point untuk perhitungan, kemudian dikuantisasi kembali ke INT8 untuk langkah berikutnya. Metode ini dapat memberikan akurasi yang cukup dalam sebagian besar aplikasi sambil mempertahankan efisiensi komputasi yang tinggi.

### **FP16**

Format FP16, yaitu angka floating point 16-bit (float16), mengurangi jejak memori hingga setengah dibandingkan dengan angka floating point 32-bit (float32), yang memiliki keuntungan signifikan dalam aplikasi pembelajaran mendalam berskala besar. Format FP16 memungkinkan memuat model yang lebih besar atau memproses lebih banyak data dalam batasan memori GPU yang sama. Seiring dengan dukungan operasi FP16 yang terus berkembang pada perangkat keras GPU modern, penggunaan format FP16 juga dapat meningkatkan kecepatan komputasi. Namun, format FP16 juga memiliki kekurangan bawaan, yaitu presisi yang lebih rendah, yang dapat menyebabkan ketidakstabilan numerik atau kehilangan presisi dalam beberapa kasus.

### **FP32**

Format FP32 menyediakan presisi yang lebih tinggi dan dapat merepresentasikan rentang nilai yang luas dengan akurat. Dalam skenario di mana operasi matematis kompleks dilakukan atau hasil dengan presisi tinggi dibutuhkan, format FP32 lebih disukai. Namun, presisi tinggi juga berarti penggunaan memori yang lebih besar dan waktu perhitungan yang lebih lama. Untuk model pembelajaran mendalam berskala besar, terutama ketika terdapat banyak parameter model dan data yang sangat besar, format FP32 dapat menyebabkan memori GPU tidak mencukupi atau penurunan kecepatan inferensi.

Pada perangkat mobile atau perangkat IoT, kita dapat mengonversi model Phi-3.x ke INT4, sementara AI PC / Copilot PC dapat menggunakan presisi yang lebih tinggi seperti INT8, FP16, FP32.

Saat ini, berbagai produsen perangkat keras memiliki kerangka kerja yang berbeda untuk mendukung model generatif, seperti OpenVINO dari Intel, QNN dari Qualcomm, MLX dari Apple, dan CUDA dari Nvidia, yang dikombinasikan dengan kuantisasi model untuk menyelesaikan penerapan lokal.

Dari segi teknologi, kita memiliki dukungan format yang berbeda setelah kuantisasi, seperti format PyTorch / Tensorflow, GGUF, dan ONNX. Saya telah melakukan perbandingan format dan skenario aplikasi antara GGUF dan ONNX. Di sini saya merekomendasikan format kuantisasi ONNX, yang memiliki dukungan baik dari kerangka model hingga perangkat keras. Pada bab ini, kita akan fokus pada ONNX Runtime untuk GenAI, OpenVINO, dan Apple MLX untuk melakukan kuantisasi model (jika Anda memiliki cara yang lebih baik, Anda juga dapat memberikannya kepada kami dengan mengirimkan PR).

**Bab ini mencakup**

1. [Quantizing Phi-3.5 / 4 using llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizing Phi-3.5 / 4 using Generative AI extensions for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizing Phi-3.5 / 4 using Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizing Phi-3.5 / 4 using Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.