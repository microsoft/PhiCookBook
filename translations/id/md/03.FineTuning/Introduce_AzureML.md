<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7fe541373802e33568e94e13226d463c",
  "translation_date": "2025-05-09T22:22:11+00:00",
  "source_file": "md/03.FineTuning/Introduce_AzureML.md",
  "language_code": "id"
}
-->
# **Perkenalkan Azure Machine Learning Service**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo) adalah layanan cloud untuk mempercepat dan mengelola siklus hidup proyek machine learning (ML).

Para profesional ML, ilmuwan data, dan insinyur dapat menggunakannya dalam alur kerja sehari-hari mereka untuk:

- Melatih dan menerapkan model.
- Mengelola operasi machine learning (MLOps).
- Anda dapat membuat model di Azure Machine Learning atau menggunakan model yang dibuat dari platform open-source, seperti PyTorch, TensorFlow, atau scikit-learn.
- Alat MLOps membantu Anda memantau, melatih ulang, dan menerapkan kembali model.

## Untuk siapa Azure Machine Learning?

**Ilmuwan Data dan Insinyur ML**

Mereka dapat menggunakan alat untuk mempercepat dan mengotomatisasi alur kerja sehari-hari mereka.
Azure ML menyediakan fitur untuk keadilan, penjelasan, pelacakan, dan auditabilitas.

**Pengembang Aplikasi:**

Mereka dapat mengintegrasikan model ke dalam aplikasi atau layanan dengan mudah.

**Pengembang Platform**

Mereka memiliki akses ke serangkaian alat yang kuat didukung oleh API Azure Resource Manager yang tahan lama.
Alat ini memungkinkan pembangunan tooling ML yang canggih.

**Perusahaan**

Bekerja di cloud Microsoft Azure, perusahaan mendapatkan manfaat dari keamanan yang sudah dikenal dan kontrol akses berbasis peran.
Mengatur proyek untuk mengontrol akses ke data yang dilindungi dan operasi tertentu.

## Produktivitas untuk Semua Anggota Tim
Proyek ML sering kali membutuhkan tim dengan beragam keahlian untuk membangun dan memelihara.

Azure ML menyediakan alat yang memungkinkan Anda untuk:
- Berkolaborasi dengan tim melalui notebook bersama, sumber daya komputasi, komputasi tanpa server, data, dan lingkungan.
- Mengembangkan model dengan keadilan, penjelasan, pelacakan, dan auditabilitas untuk memenuhi kebutuhan keturunan dan kepatuhan audit.
- Menerapkan model ML dengan cepat dan mudah dalam skala besar, serta mengelola dan mengawasinya secara efisien dengan MLOps.
- Menjalankan beban kerja machine learning di mana saja dengan tata kelola, keamanan, dan kepatuhan yang terintegrasi.

## Alat Platform yang Kompatibel Lintas

Siapa pun dalam tim ML dapat menggunakan alat favorit mereka untuk menyelesaikan pekerjaan.
Apakah Anda menjalankan eksperimen cepat, tuning hyperparameter, membangun pipeline, atau mengelola inferensi, Anda dapat menggunakan antarmuka yang sudah dikenal termasuk:
- Azure Machine Learning Studio
- Python SDK (v2)
- Azure CLI (v2)
- Azure Resource Manager REST APIs

Saat Anda menyempurnakan model dan berkolaborasi sepanjang siklus pengembangan, Anda dapat berbagi dan menemukan aset, sumber daya, dan metrik dalam UI studio Azure Machine Learning.

## **LLM/SLM di Azure ML**

Azure ML telah menambahkan banyak fungsi terkait LLM/SLM, menggabungkan LLMOps dan SLMOps untuk menciptakan platform teknologi kecerdasan buatan generatif tingkat perusahaan.

### **Model Catalog**

Pengguna perusahaan dapat menerapkan berbagai model sesuai dengan skenario bisnis yang berbeda melalui Model Catalog, dan menyediakan layanan sebagai Model as Service bagi pengembang atau pengguna perusahaan untuk mengakses.

![models](../../../../translated_images/models.2450411eac222e539ffb55785a8f550d01be1030bd8eb67c9c4f9ae4ca5d64be.id.png)

Model Catalog di Azure Machine Learning studio adalah pusat untuk menemukan dan menggunakan berbagai model yang memungkinkan Anda membangun aplikasi Generative AI. Katalog model menampilkan ratusan model dari penyedia model seperti layanan Azure OpenAI, Mistral, Meta, Cohere, Nvidia, Hugging Face, termasuk model yang dilatih oleh Microsoft. Model dari penyedia selain Microsoft adalah Produk Non-Microsoft, seperti yang didefinisikan dalam Ketentuan Produk Microsoft, dan tunduk pada ketentuan yang diberikan bersama model tersebut.

### **Job Pipeline**

Inti dari pipeline machine learning adalah memecah tugas machine learning lengkap menjadi alur kerja multi langkah. Setiap langkah adalah komponen yang dapat dikelola yang dapat dikembangkan, dioptimalkan, dikonfigurasi, dan diotomatisasi secara individual. Langkah-langkah tersebut terhubung melalui antarmuka yang terdefinisi dengan baik. Layanan pipeline Azure Machine Learning secara otomatis mengatur semua ketergantungan antar langkah pipeline.

Dalam fine-tuning SLM / LLM, kita dapat mengelola data, pelatihan, dan proses generasi melalui Pipeline

![finetuning](../../../../translated_images/finetuning.b52e4aa971dfd8d3c668db913a2b419380533bd3a920d227ec19c078b7b3f309.id.png)

### **Prompt flow**

Manfaat menggunakan Azure Machine Learning prompt flow  
Azure Machine Learning prompt flow menawarkan berbagai manfaat yang membantu pengguna beralih dari ideasi ke eksperimen dan akhirnya ke aplikasi LLM siap produksi:

**Kelincahan rekayasa prompt**

Pengalaman pembuatan interaktif: Azure Machine Learning prompt flow menyediakan representasi visual dari struktur alur, memungkinkan pengguna untuk dengan mudah memahami dan menavigasi proyek mereka. Ini juga menawarkan pengalaman pengkodean seperti notebook untuk pengembangan dan debugging alur yang efisien.  
Varian untuk tuning prompt: Pengguna dapat membuat dan membandingkan beberapa varian prompt, memfasilitasi proses penyempurnaan iteratif.

Evaluasi: Alur evaluasi bawaan memungkinkan pengguna menilai kualitas dan efektivitas prompt dan alur mereka.

Sumber daya lengkap: Azure Machine Learning prompt flow mencakup perpustakaan alat bawaan, contoh, dan template yang berfungsi sebagai titik awal pengembangan, menginspirasi kreativitas dan mempercepat proses.

**Kesiapan perusahaan untuk aplikasi berbasis LLM**

Kolaborasi: Azure Machine Learning prompt flow mendukung kolaborasi tim, memungkinkan beberapa pengguna bekerja bersama pada proyek rekayasa prompt, berbagi pengetahuan, dan menjaga kontrol versi.

Platform serba ada: Azure Machine Learning prompt flow menyederhanakan seluruh proses rekayasa prompt, mulai dari pengembangan dan evaluasi hingga penerapan dan pemantauan. Pengguna dapat dengan mudah menerapkan alur mereka sebagai endpoint Azure Machine Learning dan memantau kinerjanya secara real-time, memastikan operasi optimal dan peningkatan berkelanjutan.

Solusi Kesiapan Perusahaan Azure Machine Learning: Prompt flow memanfaatkan solusi kesiapan perusahaan Azure Machine Learning yang kuat, menyediakan fondasi yang aman, skalabel, dan andal untuk pengembangan, eksperimen, dan penerapan alur.

Dengan Azure Machine Learning prompt flow, pengguna dapat melepaskan kelincahan rekayasa prompt mereka, berkolaborasi secara efektif, dan memanfaatkan solusi tingkat perusahaan untuk pengembangan dan penerapan aplikasi berbasis LLM yang sukses.

Menggabungkan kekuatan komputasi, data, dan berbagai komponen Azure ML, pengembang perusahaan dapat dengan mudah membangun aplikasi kecerdasan buatan mereka sendiri.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau kesalahan tafsir yang timbul dari penggunaan terjemahan ini.