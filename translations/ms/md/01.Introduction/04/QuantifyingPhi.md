<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-07-16T21:48:57+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "ms"
}
-->
# **Mengkuantifikasi Keluarga Phi**

Kuantisasi model merujuk kepada proses memetakan parameter (seperti berat dan nilai pengaktifan) dalam model rangkaian neural dari julat nilai yang besar (biasanya julat nilai berterusan) ke julat nilai terhingga yang lebih kecil. Teknologi ini dapat mengurangkan saiz dan kerumitan pengiraan model serta meningkatkan kecekapan operasi model dalam persekitaran yang terhad sumber seperti peranti mudah alih atau sistem terbenam. Kuantisasi model mencapai pemampatan dengan mengurangkan ketepatan parameter, tetapi ia juga memperkenalkan sedikit kehilangan ketepatan. Oleh itu, dalam proses kuantisasi, perlu ada keseimbangan antara saiz model, kerumitan pengiraan, dan ketepatan. Kaedah kuantisasi yang biasa termasuk kuantisasi titik tetap, kuantisasi titik terapung, dan lain-lain. Anda boleh memilih strategi kuantisasi yang sesuai mengikut senario dan keperluan tertentu.

Kami berharap dapat melaksanakan model GenAI ke peranti edge dan membolehkan lebih banyak peranti memasuki senario GenAI, seperti peranti mudah alih, AI PC/Copilot+PC, dan peranti IoT tradisional. Melalui model kuantisasi, kami boleh melaksanakan model tersebut ke pelbagai peranti edge berdasarkan jenis peranti. Digabungkan dengan rangka kerja pecutan model dan model kuantisasi yang disediakan oleh pengeluar perkakasan, kami dapat membina senario aplikasi SLM yang lebih baik.

Dalam senario kuantisasi, kami mempunyai ketepatan yang berbeza (INT4, INT8, FP16, FP32). Berikut adalah penjelasan mengenai ketepatan kuantisasi yang biasa digunakan

### **INT4**

Kuantisasi INT4 adalah kaedah kuantisasi radikal yang mengkuantisasi berat dan nilai pengaktifan model ke dalam integer 4-bit. Kuantisasi INT4 biasanya menyebabkan kehilangan ketepatan yang lebih besar disebabkan oleh julat perwakilan yang lebih kecil dan ketepatan yang rendah. Namun, berbanding dengan kuantisasi INT8, kuantisasi INT4 boleh mengurangkan keperluan penyimpanan dan kerumitan pengiraan model dengan lebih jauh. Perlu diingat bahawa kuantisasi INT4 agak jarang digunakan dalam aplikasi praktikal kerana ketepatan yang terlalu rendah mungkin menyebabkan penurunan prestasi model yang ketara. Selain itu, tidak semua perkakasan menyokong operasi INT4, jadi keserasian perkakasan perlu dipertimbangkan ketika memilih kaedah kuantisasi.

### **INT8**

Kuantisasi INT8 adalah proses menukar berat dan pengaktifan model dari nombor titik terapung ke integer 8-bit. Walaupun julat nombor yang diwakili oleh integer INT8 lebih kecil dan kurang tepat, ia dapat mengurangkan keperluan penyimpanan dan pengiraan dengan ketara. Dalam kuantisasi INT8, berat dan nilai pengaktifan model melalui proses kuantisasi, termasuk penskalaan dan offset, untuk mengekalkan maklumat titik terapung asal sebanyak mungkin. Semasa inferens, nilai kuantisasi ini akan dinyahkuantisasi kembali ke nombor titik terapung untuk pengiraan, dan kemudian dikuantisasi semula ke INT8 untuk langkah seterusnya. Kaedah ini dapat memberikan ketepatan yang mencukupi dalam kebanyakan aplikasi sambil mengekalkan kecekapan pengiraan yang tinggi.

### **FP16**

Format FP16, iaitu nombor titik terapung 16-bit (float16), mengurangkan penggunaan memori sebanyak separuh berbanding nombor titik terapung 32-bit (float32), yang mempunyai kelebihan ketara dalam aplikasi pembelajaran mendalam berskala besar. Format FP16 membolehkan memuatkan model yang lebih besar atau memproses lebih banyak data dalam had memori GPU yang sama. Oleh kerana perkakasan GPU moden terus menyokong operasi FP16, penggunaan format FP16 juga boleh membawa peningkatan dalam kelajuan pengiraan. Walau bagaimanapun, format FP16 juga mempunyai kekurangan tersendiri, iaitu ketepatan yang lebih rendah, yang mungkin menyebabkan ketidakstabilan nombor atau kehilangan ketepatan dalam beberapa kes.

### **FP32**

Format FP32 menyediakan ketepatan yang lebih tinggi dan boleh mewakili julat nilai yang luas dengan tepat. Dalam senario di mana operasi matematik yang kompleks dilakukan atau keputusan ketepatan tinggi diperlukan, format FP32 adalah pilihan utama. Namun, ketepatan tinggi juga bermakna penggunaan memori yang lebih banyak dan masa pengiraan yang lebih lama. Untuk model pembelajaran mendalam berskala besar, terutamanya apabila terdapat banyak parameter model dan jumlah data yang besar, format FP32 mungkin menyebabkan kekurangan memori GPU atau penurunan kelajuan inferens.

Pada peranti mudah alih atau peranti IoT, kami boleh menukar model Phi-3.x ke INT4, manakala AI PC / Copilot PC boleh menggunakan ketepatan lebih tinggi seperti INT8, FP16, FP32.

Pada masa ini, pengeluar perkakasan yang berbeza mempunyai rangka kerja yang berbeza untuk menyokong model generatif, seperti OpenVINO Intel, QNN Qualcomm, MLX Apple, dan CUDA Nvidia, dan lain-lain, digabungkan dengan kuantisasi model untuk melengkapkan pelaksanaan tempatan.

Dari segi teknologi, kami mempunyai sokongan format yang berbeza selepas kuantisasi, seperti format PyTorch / Tensorflow, GGUF, dan ONNX. Saya telah membuat perbandingan format dan senario aplikasi antara GGUF dan ONNX. Di sini saya mengesyorkan format kuantisasi ONNX, yang mempunyai sokongan baik dari rangka kerja model hingga perkakasan. Dalam bab ini, kami akan fokus pada ONNX Runtime untuk GenAI, OpenVINO, dan Apple MLX untuk melaksanakan kuantisasi model (jika anda mempunyai cara yang lebih baik, anda juga boleh memberikannya kepada kami dengan menghantar PR)

**Bab ini merangkumi**

1. [Mengkuantifikasi Phi-3.5 / 4 menggunakan llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Mengkuantifikasi Phi-3.5 / 4 menggunakan sambungan AI Generatif untuk onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Mengkuantifikasi Phi-3.5 / 4 menggunakan Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Mengkuantifikasi Phi-3.5 / 4 menggunakan Rangka Kerja Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.