## Senario Penalaan Halus

![FineTuning with MS Services](../../../../translated_images/ms/FinetuningwithMS.3d0cec8ae693e094.webp)

Bahagian ini memberikan gambaran keseluruhan tentang senario penalaan halus dalam Microsoft Foundry dan persekitaran Azure, termasuk model penerapan, lapisan infrastruktur, dan teknik pengoptimuman yang sering digunakan.

**Platform**  
Ini merangkumi perkhidmatan terurus seperti Microsoft Foundry (dahulunya Microsoft Foundry) dan Azure Machine Learning, yang menyediakan pengurusan model, orkestrasi, penjejakan eksperimen, dan aliran kerja penerapan.

**Infrastruktur**  
Penalaan halus memerlukan sumber pengkomputeran yang boleh diskala. Dalam persekitaran Azure, ini biasanya merangkumi mesin maya berasaskan GPU dan sumber CPU untuk beban kerja ringan, serta storan skala untuk set data dan titik pemeriksaan.

**Alat & Rangka Kerja**  
Aliran kerja penalaan halus biasanya bergantung pada rangka kerja dan perpustakaan pengoptimuman seperti Hugging Face Transformers, DeepSpeed, dan PEFT (Parameter-Efficient Fine-Tuning).

Proses penalaan halus dengan teknologi Microsoft merangkumi perkhidmatan platform, infrastruktur pengkomputeran, dan rangka kerja latihan. Dengan memahami bagaimana komponen ini berfungsi bersama, pembangun dapat menyesuaikan model asas dengan berkesan untuk tugas tertentu dan senario produksi.

## Model sebagai Perkhidmatan

Tala halus model menggunakan penalaan halus yang dihoskan, tanpa perlu membuat dan mengurus pengkomputeran.

![MaaS Fine Tuning](../../../../translated_images/ms/MaaSfinetune.3eee4630607aff0d.webp)

Penalaan halus tanpa pelayan kini tersedia untuk keluarga model Phi-3, Phi-3.5, dan Phi-4, membolehkan pembangun dengan cepat dan mudah menyesuaikan model untuk senario awan dan tepi tanpa perlu mengatur pengkomputeran.

## Model sebagai Platform

Pengguna mengurus pengkomputeran mereka sendiri untuk menala halus model mereka.

![Maap Fine Tuning](../../../../translated_images/ms/MaaPFinetune.fd3829c1122f5d1c.webp)

[Contoh Penalaan Halus](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Perbandingan Teknik Penalaan Halus

|Senario|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Menyesuaikan LLM yang telah dilatih untuk tugas atau domain tertentu|Ya|Ya|Ya|Ya|Ya|Ya|
|Penalaan halus untuk tugasan NLP seperti pengkelasan teks, pengecaman entiti bernama, dan penterjemahan mesin|Ya|Ya|Ya|Ya|Ya|Ya|
|Penalaan halus untuk tugasan QA|Ya|Ya|Ya|Ya|Ya|Ya|
|Penalaan halus untuk menghasilkan respons seperti manusia dalam chatbot|Ya|Ya|Ya|Ya|Ya|Ya|
|Penalaan halus untuk menghasilkan muzik, seni, atau bentuk kreativiti lain|Ya|Ya|Ya|Ya|Ya|Ya|
|Mengurangkan kos pengkomputeran dan kewangan|Ya|Ya|Ya|Ya|Ya|Ya|
|Mengurangkan penggunaan memori|Ya|Ya|Ya|Ya|Ya|Ya|
|Menggunakan parameter yang lebih sedikit untuk penalaan halus yang cekap|Ya|Ya|Ya|Tidak|Tidak|Ya|
|Bentuk paralelisme data yang cekap memori yang memberikan akses kepada memori GPU agregat bagi semua peranti GPU yang ada|Tidak|Tidak|Tidak|Ya|Ya|Tidak|

> [!NOTE]
> LoRA, QLoRA, PEFT, dan DoRA adalah kaedah penalaan halus yang cekap parameter, manakala DeepSpeed dan ZeRO memfokuskan pada latihan teragih dan pengoptimuman memori.

## Contoh Prestasi Penalaan Halus

![Finetuning Performance](../../../../translated_images/ms/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->