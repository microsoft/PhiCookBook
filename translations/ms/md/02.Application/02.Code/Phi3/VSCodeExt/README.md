# **Bina Visual Studio Code GitHub Copilot Chat anda sendiri dengan Keluarga Microsoft Phi-3**

Adakah anda pernah menggunakan ejen ruang kerja dalam GitHub Copilot Chat? Adakah anda ingin membina ejen kod pasukan anda sendiri? Makmal praktikal ini berharap dapat menggabungkan model sumber terbuka untuk membina ejen perniagaan kod tahap perusahaan.

## **Asas**

### **Mengapa memilih Microsoft Phi-3**

Phi-3 adalah siri keluarga, termasuk phi-3-mini, phi-3-small, dan phi-3-medium berdasarkan parameter latihan yang berbeza untuk penjanaan teks, pemenuhan dialog, dan penjanaan kod. Terdapat juga phi-3-vision berdasarkan Vision. Ia sesuai untuk perusahaan atau pasukan yang berbeza untuk mencipta penyelesaian AI generatif luar talian.

Disyorkan untuk membaca pautan ini [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Sambungan GitHub Copilot Chat memberikan anda antara muka sembang yang membolehkan anda berinteraksi dengan GitHub Copilot dan menerima jawapan kepada soalan berkaitan pengekodan secara langsung dalam VS Code, tanpa memerlukan anda melayari dokumentasi atau mencari forum dalam talian.

Copilot Chat mungkin menggunakan penyorotan sintaks, inden, dan ciri pemformatan lain untuk menambah kejelasan pada respons yang dijana. Bergantung kepada jenis soalan dari pengguna, hasilnya boleh mengandungi pautan ke konteks yang digunakan oleh Copilot untuk menjana respons, seperti fail kod sumber atau dokumentasi, atau butang untuk mengakses fungsi VS Code.

- Copilot Chat berintegrasi dalam aliran pembangun anda dan memberi bantuan di mana anda memerlukannya:

- Mulakan perbualan sembang dalam talian terus dari penyunting atau terminal untuk bantuan semasa anda mengekod

- Gunakan pandangan Sembang untuk mempunyai pembantu AI di sebelah untuk membantu anda pada bila-bila masa

- Lancarkan Sembang Pantas untuk bertanya soalan cepat dan kembali ke apa yang anda lakukan

Anda boleh menggunakan GitHub Copilot Chat dalam pelbagai senario, seperti:

- Menjawab soalan pengekodan mengenai cara terbaik untuk menyelesaikan masalah

- Menerangkan kod orang lain dan mencadangkan penambahbaikan

- Mencadangkan pembaikan kod

- Menjana kes ujian unit

- Menjana dokumentasi kod

Disyorkan untuk membaca pautan ini [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Merujuk kepada **@workspace** dalam Copilot Chat membolehkan anda bertanya soalan mengenai keseluruhan pangkalan kod anda. Berdasarkan soalan, Copilot dengan bijak mengambil fail dan simbol yang relevan, yang kemudian dirujuk dalam jawapannya sebagai pautan dan contoh kod. 

Untuk menjawab soalan anda, **@workspace** mencari melalui sumber yang sama seperti yang digunakan oleh pembangun apabila menavigasi pangkalan kod dalam VS Code:

- Semua fail dalam ruang kerja, kecuali fail yang diabaikan oleh fail .gitignore

- Struktur direktori dengan folder bertingkat dan nama fail

- Indeks carian kod GitHub, jika ruang kerja adalah repositori GitHub dan diindeks oleh carian kod

- Simbol dan definisi dalam ruang kerja

- Teks yang dipilih sedang atau teks yang kelihatan dalam penyunting aktif

Nota: .gitignore diabaikan jika anda membuka fail atau mempunyai teks yang dipilih dalam fail yang diabaikan.

Disyorkan untuk membaca pautan ini [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Ketahui lebih lanjut tentang Makmal ini**

GitHub Copilot telah banyak meningkatkan kecekapan pengaturcaraan perusahaan, dan setiap perusahaan berharap dapat menyesuaikan fungsi relevan GitHub Copilot. Banyak perusahaan telah menyesuaikan Sambungan serupa GitHub Copilot berdasarkan senario perniagaan mereka sendiri dan model sumber terbuka. Bagi perusahaan, Sambungan yang disesuaikan lebih mudah dikawal, tetapi ini juga mempengaruhi pengalaman pengguna. Lagipun, GitHub Copilot mempunyai fungsi yang lebih kuat dalam menangani senario umum dan profesionalisme. Jika pengalaman dapat dikekalkan konsisten, adalah lebih baik untuk menyesuaikan Sambungan perusahaan sendiri. GitHub Copilot Chat menyediakan API relevan untuk perusahaan mengembangkan pengalaman Sembang. Mengekalkan pengalaman konsisten dan mempunyai fungsi yang disesuaikan adalah pengalaman pengguna yang lebih baik.

Makmal ini terutamanya menggunakan model Phi-3 yang digabungkan dengan NPU tempatan dan hibrid Azure untuk membina Ejen khusus dalam GitHub Copilot Chat ***@PHI3*** untuk membantu pembangun perusahaan melengkapkan penjanaan kod***(@PHI3 /gen)*** dan menjana kod berdasarkan imej ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/ms/cover.1017ebc9a7c46d09.webp)

### ***Nota:*** 

Makmal ini kini dilaksanakan dalam AIPC CPU Intel dan Apple Silicon. Kami akan terus mengemas kini versi Qualcomm NPU.


## **Makmal**


| Nama | Penerangan | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Pemasangan(✅) | Konfigurasi dan pasang persekitaran dan alat pemasangan berkaitan | [Pergi](./HOL/AIPC/01.Installations.md) |[Pergi](./HOL/Apple/01.Installations.md) |
| Lab1 - Jalankan aliran Prompt dengan Phi-3-mini (✅) | Digabungkan dengan AIPC / Apple Silicon, menggunakan NPU tempatan untuk mencipta penjanaan kod melalui Phi-3-mini | [Pergi](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Pergi](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Lancarkan Phi-3-vision di Azure Machine Learning Service(✅) | Jana kod dengan melancarkan Katalog Model Azure Machine Learning Service - imej Phi-3-vision | [Pergi](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Pergi](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Cipta ejen @phi-3 dalam GitHub Copilot Chat(✅)  | Cipta ejen Phi-3 khusus dalam GitHub Copilot Chat untuk melengkapkan penjanaan kod, kod penjanaan grafik, RAG, dan lain-lain. | [Pergi](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Pergi](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Kod Contoh (✅)  | Muat turun kod contoh | [Pergi](../../../../../../../code/07.Lab/01/AIPC) | [Pergi](../../../../../../../code/07.Lab/01/Apple) |


## **Sumber**

1. Resepi Phi-3 [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Ketahui lebih lanjut mengenai GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Ketahui lebih lanjut mengenai GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Ketahui lebih lanjut mengenai GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Ketahui lebih lanjut mengenai Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Ketahui lebih lanjut mengenai Katalog Model Microsoft Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->