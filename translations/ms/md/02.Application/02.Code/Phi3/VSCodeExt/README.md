<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-07-17T03:42:30+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "ms"
}
-->
# **Bina Visual Studio Code GitHub Copilot Chat anda sendiri dengan Keluarga Microsoft Phi-3**

Adakah anda pernah menggunakan agen workspace dalam GitHub Copilot Chat? Adakah anda ingin membina agen kod untuk pasukan anda sendiri? Makmal praktikal ini bertujuan menggabungkan model sumber terbuka untuk membina agen perniagaan kod tahap perusahaan.

## **Asas**

### **Mengapa memilih Microsoft Phi-3**

Phi-3 adalah siri keluarga, termasuk phi-3-mini, phi-3-small, dan phi-3-medium berdasarkan parameter latihan yang berbeza untuk penjanaan teks, penyelesaian dialog, dan penjanaan kod. Terdapat juga phi-3-vision yang berasaskan Vision. Ia sesuai untuk perusahaan atau pasukan yang berbeza untuk mencipta penyelesaian AI generatif secara luar talian.

Disyorkan untuk membaca pautan ini [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Sambungan GitHub Copilot Chat memberikan anda antara muka sembang yang membolehkan anda berinteraksi dengan GitHub Copilot dan menerima jawapan kepada soalan berkaitan pengkodan terus dalam VS Code, tanpa perlu melayari dokumentasi atau mencari di forum dalam talian.

Copilot Chat mungkin menggunakan penyorotan sintaks, indentasi, dan ciri pemformatan lain untuk menambah kejelasan pada jawapan yang dijana. Bergantung pada jenis soalan daripada pengguna, hasilnya boleh mengandungi pautan kepada konteks yang digunakan oleh Copilot untuk menjana jawapan, seperti fail kod sumber atau dokumentasi, atau butang untuk mengakses fungsi VS Code.

- Copilot Chat disepadukan dalam aliran kerja pembangun anda dan memberikan bantuan di mana anda memerlukannya:

- Mulakan perbualan sembang secara langsung dari editor atau terminal untuk mendapatkan bantuan semasa anda menulis kod

- Gunakan paparan Chat untuk mempunyai pembantu AI di sisi yang membantu anda pada bila-bila masa

- Lancarkan Quick Chat untuk bertanya soalan ringkas dan kembali kepada kerja anda dengan cepat

Anda boleh menggunakan GitHub Copilot Chat dalam pelbagai senario, seperti:

- Menjawab soalan pengkodan tentang cara terbaik menyelesaikan masalah

- Menerangkan kod orang lain dan mencadangkan penambahbaikan

- Mencadangkan pembetulan kod

- Menjana kes ujian unit

- Menjana dokumentasi kod

Disyorkan untuk membaca pautan ini [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Merujuk kepada **@workspace** dalam Copilot Chat membolehkan anda bertanya soalan mengenai keseluruhan kod asas anda. Berdasarkan soalan, Copilot secara pintar mengambil fail dan simbol yang berkaitan, yang kemudian dirujuk dalam jawapannya sebagai pautan dan contoh kod.

Untuk menjawab soalan anda, **@workspace** mencari melalui sumber yang sama yang digunakan oleh pembangun apabila menavigasi kod asas dalam VS Code:

- Semua fail dalam workspace, kecuali fail yang diabaikan oleh fail .gitignore

- Struktur direktori dengan folder dan nama fail bersarang

- Indeks carian kod GitHub, jika workspace adalah repositori GitHub dan diindeks oleh carian kod

- Simbol dan definisi dalam workspace

- Teks yang dipilih atau teks yang kelihatan dalam editor aktif

Nota: .gitignore diabaikan jika anda membuka fail atau memilih teks dalam fail yang diabaikan.

Disyorkan untuk membaca pautan ini [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Ketahui lebih lanjut tentang Makmal ini**

GitHub Copilot telah banyak meningkatkan kecekapan pengaturcaraan perusahaan, dan setiap perusahaan berharap untuk menyesuaikan fungsi berkaitan GitHub Copilot. Banyak perusahaan telah menyesuaikan Extensions yang serupa dengan GitHub Copilot berdasarkan senario perniagaan mereka sendiri dan model sumber terbuka. Bagi perusahaan, Extensions yang disesuaikan lebih mudah dikawal, tetapi ini juga mempengaruhi pengalaman pengguna. Lagipun, GitHub Copilot mempunyai fungsi yang lebih kuat dalam menangani senario umum dan profesionalisme. Jika pengalaman dapat dikekalkan konsisten, adalah lebih baik untuk menyesuaikan Extension perusahaan sendiri. GitHub Copilot Chat menyediakan API berkaitan untuk perusahaan mengembangkan pengalaman Chat. Mengekalkan pengalaman yang konsisten dan mempunyai fungsi yang disesuaikan adalah pengalaman pengguna yang lebih baik.

Makmal ini terutamanya menggunakan model Phi-3 digabungkan dengan NPU tempatan dan Azure hibrid untuk membina Agen tersuai dalam GitHub Copilot Chat ***@PHI3*** untuk membantu pembangun perusahaan menyelesaikan penjanaan kod***(@PHI3 /gen)*** dan menjana kod berdasarkan imej ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/cover.1017ebc9a7c46d09.ms.png)

### ***Nota:*** 

Makmal ini kini dilaksanakan dalam AIPC CPU Intel dan Apple Silicon. Kami akan terus mengemas kini versi Qualcomm NPU.


## **Makmal**


| Nama | Penerangan | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Pemasangan(✅) | Konfigurasi dan pasang persekitaran dan alat pemasangan berkaitan | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Jalankan Prompt flow dengan Phi-3-mini (✅) | Digabungkan dengan AIPC / Apple Silicon, menggunakan NPU tempatan untuk mencipta penjanaan kod melalui Phi-3-mini | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Lancarkan Phi-3-vision pada Azure Machine Learning Service(✅) | Jana kod dengan melancarkan Model Catalog Azure Machine Learning Service - imej Phi-3-vision | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Cipta agen @phi-3 dalam GitHub Copilot Chat(✅)  | Cipta agen Phi-3 tersuai dalam GitHub Copilot Chat untuk menyelesaikan penjanaan kod, penjanaan kod graf, RAG, dan lain-lain | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Kod Contoh (✅)  | Muat turun kod contoh | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## **Sumber**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Ketahui lebih lanjut tentang GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Ketahui lebih lanjut tentang GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Ketahui lebih lanjut tentang GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Ketahui lebih lanjut tentang Azure AI Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Ketahui lebih lanjut tentang Model Catalog Azure AI Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.