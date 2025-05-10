<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-05-09T18:54:10+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "id"
}
-->
# Menggunakan Windows GPU untuk membuat solusi Prompt flow dengan Phi-3.5-Instruct ONNX

Dokumen berikut adalah contoh cara menggunakan PromptFlow dengan ONNX (Open Neural Network Exchange) untuk mengembangkan aplikasi AI berbasis model Phi-3.

PromptFlow adalah rangkaian alat pengembangan yang dirancang untuk mempermudah siklus pengembangan end-to-end aplikasi AI berbasis LLM (Large Language Model), mulai dari ideasi dan prototipe hingga pengujian dan evaluasi.

Dengan mengintegrasikan PromptFlow dengan ONNX, pengembang dapat:

- Mengoptimalkan Performa Model: Memanfaatkan ONNX untuk inferensi dan deployment model yang efisien.
- Menyederhanakan Pengembangan: Menggunakan PromptFlow untuk mengelola alur kerja dan mengotomatisasi tugas-tugas berulang.
- Meningkatkan Kolaborasi: Memfasilitasi kolaborasi yang lebih baik antar anggota tim dengan menyediakan lingkungan pengembangan yang terintegrasi.

**Prompt flow** adalah rangkaian alat pengembangan yang dirancang untuk mempermudah siklus pengembangan end-to-end aplikasi AI berbasis LLM, mulai dari ideasi, prototyping, pengujian, evaluasi hingga deployment produksi dan pemantauan. Ini membuat rekayasa prompt menjadi jauh lebih mudah dan memungkinkan Anda membangun aplikasi LLM dengan kualitas produksi.

Prompt flow dapat terhubung ke OpenAI, Azure OpenAI Service, dan model yang dapat dikustomisasi (Huggingface, LLM/SLM lokal). Kami berharap dapat mendepankan model ONNX kuantisasi Phi-3.5 ke aplikasi lokal. Prompt flow dapat membantu kami merencanakan bisnis dengan lebih baik dan menyelesaikan solusi lokal berbasis Phi-3.5. Dalam contoh ini, kami akan menggabungkan ONNX Runtime GenAI Library untuk menyelesaikan solusi Prompt flow berbasis Windows GPU.

## **Instalasi**

### **ONNX Runtime GenAI untuk Windows GPU**

Baca panduan ini untuk mengatur ONNX Runtime GenAI untuk Windows GPU [klik di sini](./ORTWindowGPUGuideline.md)

### **Menyiapkan Prompt flow di VSCode**

1. Instal Ekstensi Prompt flow VS Code

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.id.png)

2. Setelah menginstal Ekstensi Prompt flow VS Code, klik ekstensi tersebut, dan pilih **Installation dependencies** ikuti panduan ini untuk menginstal Prompt flow SDK di lingkungan Anda

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.id.png)

3. Unduh [Sample Code](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) dan gunakan VS Code untuk membuka contoh ini

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.id.png)

4. Buka **flow.dag.yaml** untuk memilih lingkungan Python Anda

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.id.png)

   Buka **chat_phi3_ort.py** untuk mengubah lokasi Model ONNX Phi-3.5-instruct Anda

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.id.png)

5. Jalankan prompt flow Anda untuk pengujian

Buka **flow.dag.yaml** klik visual editor

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.id.png)

setelah klik ini, jalankan untuk menguji

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.id.png)

1. Anda bisa menjalankan batch di terminal untuk memeriksa hasil lebih lanjut


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Anda dapat memeriksa hasil di browser default Anda


![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.id.png)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi yang penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.