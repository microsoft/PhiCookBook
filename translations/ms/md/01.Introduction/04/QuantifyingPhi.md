# **Mengkuantifikasi Keluarga Phi**

Kuantisasi model merujuk kepada proses memetakan parameter (seperti berat dan nilai pengaktifan) dalam model rangkaian neural dari julat nilai besar (biasanya julat nilai berterusan) kepada julat nilai terhingga yang lebih kecil. Teknologi ini dapat mengurangkan saiz dan kerumitan pengiraan model serta meningkatkan kecekapan operasi model dalam persekitaran yang mempunyai sumber terhad seperti peranti mudah alih atau sistem tersemat. Kuantisasi model mencapai pemampatan dengan mengurangkan ketepatan parameter, tetapi ia juga menyebabkan kehilangan ketepatan tertentu. Oleh itu, dalam proses kuantisasi, perlu untuk mengimbangi saiz model, kerumitan pengiraan, dan ketepatan. Kaedah kuantisasi biasa termasuk kuantisasi titik tetap, kuantisasi nombor titik terapung, dan lain-lain. Anda boleh memilih strategi kuantisasi yang sesuai mengikut senario dan keperluan spesifik.

Kami berharap dapat menggunakan model GenAI pada peranti tepi dan membolehkan lebih banyak peranti memasuki senario GenAI, seperti peranti mudah alih, AI PC/Copilot+PC, dan peranti IoT tradisional. Melalui model kuantisasi, kami dapat mengedarkannya ke peranti tepi yang berbeza berdasarkan peranti yang berbeza. Digabungkan dengan rangka kerja pemecut model dan model kuantisasi yang disediakan oleh pengeluar perkakasan, kami dapat membina senario aplikasi SLM yang lebih baik.

Dalam senario kuantisasi, kami mempunyai ketepatan yang berbeza (INT4, INT8, FP16, FP32). Berikut adalah penjelasan mengenai ketepatan kuantisasi yang biasa digunakan

### **INT4**

Kuantisasi INT4 adalah kaedah kuantisasi radikal yang mengkuantisasi berat dan nilai pengaktifan model menjadi integer 4-bit. Kuantisasi INT4 biasanya mengakibatkan kehilangan ketepatan yang lebih besar disebabkan oleh julat perwakilan yang lebih kecil dan ketepatan yang lebih rendah. Walau bagaimanapun, berbanding dengan kuantisasi INT8, kuantisasi INT4 boleh mengurangkan lagi keperluan penyimpanan dan kerumitan pengiraan model. Perlu diambil perhatian bahawa kuantisasi INT4 agak jarang digunakan dalam aplikasi praktikal kerana ketepatan yang terlalu rendah boleh menyebabkan penurunan prestasi model yang ketara. Selain itu, tidak semua perkakasan menyokong operasi INT4, jadi kesesuaian perkakasan perlu dipertimbangkan apabila memilih kaedah kuantisasi.

### **INT8**

Kuantisasi INT8 adalah proses menukar berat dan pengaktifan model dari nombor titik terapung kepada integer 8-bit. Walaupun julat nombor yang diwakili oleh integer INT8 lebih kecil dan kurang tepat, ia boleh mengurangkan keperluan penyimpanan dan pengiraan dengan ketara. Dalam kuantisasi INT8, berat dan nilai pengaktifan model melalui proses kuantisasi, termasuk penskalaan dan offset, untuk mengekalkan maklumat titik terapung asal sebanyak mungkin. Semasa inferens, nilai yang telah dikuantisasi ini akan didekuantisasi kembali kepada nombor titik terapung untuk pengiraan, dan kemudian dikuantisasi semula kepada INT8 untuk langkah seterusnya. Kaedah ini dapat memberikan ketepatan yang mencukupi dalam kebanyakan aplikasi sambil mengekalkan kecekapan pengiraan yang tinggi.

### **FP16**

Format FP16, iaitu nombor titik terapung 16-bit (float16), mengurangkan penggunaan memori sebanyak separuh berbanding nombor titik terapung 32-bit (float32), yang mempunyai kelebihan yang ketara dalam aplikasi pembelajaran mendalam skala besar. Format FP16 membenarkan pemuatan model yang lebih besar atau pemprosesan data yang lebih banyak dalam batasan memori GPU yang sama. Oleh kerana perkakasan GPU moden terus menyokong operasi FP16, penggunaan format FP16 juga boleh membawa kepada peningkatan kelajuan pengiraan. Walau bagaimanapun, format FP16 juga mempunyai kekurangan yang tersendiri, iaitu ketepatan yang lebih rendah, yang boleh menyebabkan ketidakstabilan nombor atau kehilangan ketepatan dalam beberapa kes.

### **FP32**

Format FP32 menyediakan ketepatan yang lebih tinggi dan boleh mewakili julat nilai yang luas dengan tepat. Dalam senario di mana operasi matematik yang kompleks dilakukan atau keputusan ketepatan tinggi diperlukan, format FP32 adalah pilihan terbaik. Walau bagaimanapun, ketepatan tinggi juga bermakna penggunaan memori yang lebih banyak dan masa pengiraan yang lebih lama. Untuk model pembelajaran mendalam skala besar, terutamanya apabila terdapat banyak parameter model dan jumlah data yang besar, format FP32 mungkin menyebabkan kekurangan memori GPU atau penurunan kelajuan inferens.

Pada peranti mudah alih atau peranti IoT, kami boleh menukar model Phi-3.x kepada INT4, manakala AI PC / Copilot PC boleh menggunakan ketepatan yang lebih tinggi seperti INT8, FP16, FP 32.

Pada masa ini, pengeluar perkakasan yang berbeza mempunyai rangka kerja yang berbeza untuk menyokong model generatif, seperti OpenVINO Intel, QNN Qualcomm, MLX Apple, dan CUDA Nvidia, dan lain-lain, digabungkan dengan kuantisasi model untuk melengkapkan penyebaran tempatan.

Dari segi teknologi, kami mempunyai sokongan format yang berbeza selepas kuantisasi, seperti format PyTorch / TensorFlow, GGUF, dan ONNX. Saya telah membuat perbandingan format dan senario aplikasi antara GGUF dan ONNX. Di sini saya mengesyorkan format kuantisasi ONNX, yang menerima sokongan yang baik dari rangka kerja model ke perkakasan. Dalam bab ini, kami akan memberi tumpuan kepada ONNX Runtime untuk GenAI, OpenVINO, dan Apple MLX untuk melaksanakan kuantisasi model (jika anda mempunyai cara yang lebih baik, anda juga boleh memberikannya kepada kami dengan mengemukakan PR)

**Bab ini merangkumi**

1. [Mengkuantifikasi Phi-3.5 / 4 menggunakan llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Mengkuantifikasi Phi-3.5 / 4 menggunakan sambungan AI Generatif untuk onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Mengkuantifikasi Phi-3.5 / 4 menggunakan Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Mengkuantifikasi Phi-3.5 / 4 menggunakan Rangka Kerja Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk mencapai ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber yang sahih. Untuk maklumat yang penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->