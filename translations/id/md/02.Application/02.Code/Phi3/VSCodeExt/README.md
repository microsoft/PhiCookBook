# **Bangun Chat GitHub Copilot Visual Studio Code Anda Sendiri dengan Keluarga Microsoft Phi-3**

Apakah Anda pernah menggunakan agen workspace di GitHub Copilot Chat? Apakah Anda ingin membangun agen kode untuk tim Anda sendiri? Lab praktikum ini berharap menggabungkan model open source untuk membangun agen bisnis kode tingkat perusahaan.

## **Dasar**

### **Mengapa memilih Microsoft Phi-3**

Phi-3 adalah seri keluarga, termasuk phi-3-mini, phi-3-small, dan phi-3-medium berdasarkan parameter pelatihan yang berbeda untuk generasi teks, penyelesaian dialog, dan generasi kode. Ada juga phi-3-vision yang berbasis Vision. Ini cocok untuk perusahaan atau tim berbeda untuk membuat solusi AI generatif offline.

Disarankan untuk membaca tautan ini [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Ekstensi GitHub Copilot Chat memberi Anda antarmuka chat yang memungkinkan Anda berinteraksi dengan GitHub Copilot dan menerima jawaban atas pertanyaan terkait pengkodean langsung di dalam VS Code, tanpa perlu Anda menelusuri dokumentasi atau mencari di forum daring.

Copilot Chat mungkin menggunakan penyorotan sintaks, indentasi, dan fitur format lainnya untuk menambah kejelasan pada respons yang dihasilkan. Bergantung pada jenis pertanyaan dari pengguna, hasilnya dapat berisi tautan ke konteks yang digunakan Copilot untuk menghasilkan respons, seperti berkas kode sumber atau dokumentasi, atau tombol untuk mengakses fungsi VS Code.

- Copilot Chat terintegrasi dalam alur pengembangan Anda dan memberikan bantuan di mana Anda membutuhkannya:

- Mulai percakapan chat inline langsung dari editor atau terminal untuk bantuan saat Anda mengoding

- Gunakan tampilan Chat untuk memiliki asisten AI di sisi yang membantu kapan saja

- Luncurkan Quick Chat untuk menanyakan pertanyaan cepat dan kembali ke apa yang sedang Anda kerjakan

Anda dapat menggunakan GitHub Copilot Chat dalam berbagai skenario, seperti:

- Menjawab pertanyaan pemrograman tentang cara terbaik menyelesaikan masalah

- Menjelaskan kode orang lain dan menyarankan perbaikan

- Mengusulkan perbaikan kode

- Menghasilkan kasus uji unit

- Menghasilkan dokumentasi kode

Disarankan untuk membaca tautan ini [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Merujuk ke **@workspace** dalam Copilot Chat memungkinkan Anda mengajukan pertanyaan tentang seluruh basis kode Anda. Berdasarkan pertanyaan, Copilot secara cerdas mengambil berkas dan simbol relevan, yang kemudian dirujuk dalam jawabannya sebagai tautan dan contoh kode.

Untuk menjawab pertanyaan Anda, **@workspace** mencari melalui sumber yang sama yang digunakan pengembang saat menavigasi basis kode di VS Code:

- Semua berkas di workspace, kecuali berkas yang diabaikan oleh berkas .gitignore

- Struktur direktori dengan folder dan nama berkas bersarang

- Indeks pencarian kode GitHub, jika workspace adalah repositori GitHub dan diindeks oleh pencarian kode

- Simbol dan definisi di workspace

- Teks yang sedang dipilih atau teks yang terlihat di editor aktif

Catatan: .gitignore dilewati jika Anda membuka berkas atau telah memilih teks dalam berkas yang diabaikan.

Disarankan untuk membaca tautan ini [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Lebih Mengenal Lab Ini**

GitHub Copilot telah sangat meningkatkan efisiensi pemrograman perusahaan, dan setiap perusahaan berharap menyesuaikan fungsi terkait GitHub Copilot. Banyak perusahaan telah menyesuaikan Ekstensi mirip GitHub Copilot berdasarkan skenario bisnis dan model open source mereka sendiri. Bagi perusahaan, Ekstensi yang disesuaikan lebih mudah dikendalikan, tetapi ini juga memengaruhi pengalaman pengguna. Bagaimanapun, GitHub Copilot memiliki fungsi lebih kuat dalam menangani skenario umum dan profesionalisme. Jika pengalaman dapat tetap konsisten, akan lebih baik menyesuaikan Ekstensi perusahaan sendiri. GitHub Copilot Chat menyediakan API terkait untuk perusahaan agar dapat memperluas pengalaman Chat. Mempertahankan pengalaman yang konsisten dan memiliki fungsi yang disesuaikan adalah pengalaman pengguna yang lebih baik.

Lab ini terutama menggunakan model Phi-3 yang dipadukan dengan NPU lokal dan hybrid Azure untuk membangun Agen khusus dalam GitHub Copilot Chat ***@PHI3*** guna membantu pengembang perusahaan menyelesaikan generasi kode***(@PHI3 /gen)*** dan menghasilkan kode berdasarkan gambar ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/id/cover.1017ebc9a7c46d09.webp)

### ***Catatan:*** 

Lab ini saat ini diimplementasikan di AIPC Intel CPU dan Apple Silicon. Kami akan terus memperbarui versi NPU Qualcomm.


## **Lab**


| Nama | Deskripsi | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Instalasi(✅) | Konfigurasi dan instal lingkungan terkait serta alat instalasi | [Pergi](./HOL/AIPC/01.Installations.md) |[Pergi](./HOL/Apple/01.Installations.md) |
| Lab1 - Jalankan alur Prompt dengan Phi-3-mini (✅) | Digabungkan dengan AIPC / Apple Silicon, menggunakan NPU lokal untuk membuat generasi kode melalui Phi-3-mini | [Pergi](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Pergi](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Deploy Phi-3-vision di Azure Machine Learning Service(✅) | Menghasilkan kode dengan menerapkan Katalog Model Azure Machine Learning Service - gambar Phi-3-vision | [Pergi](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Pergi](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Buat agen @phi-3 di GitHub Copilot Chat(✅)  | Buat agen Phi-3 khusus di GitHub Copilot Chat untuk menyelesaikan generasi kode, kode gambar grafik, RAG, dll. | [Pergi](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Pergi](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Kode Contoh (✅)  | Unduh kode contoh | [Pergi](../../../../../../../code/07.Lab/01/AIPC) | [Pergi](../../../../../../../code/07.Lab/01/Apple) |


## **Sumber Daya**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Pelajari lebih lanjut tentang GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Pelajari lebih lanjut tentang GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Pelajari lebih lanjut tentang GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Pelajari lebih lanjut tentang Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Pelajari lebih lanjut tentang Katalog Model Microsoft Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber otoritatif. Untuk informasi penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->