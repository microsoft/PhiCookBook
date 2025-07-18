<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T03:02:25+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "ms"
}
-->
# Menggunakan Windows GPU untuk mencipta penyelesaian Prompt flow dengan Phi-3.5-Instruct ONNX

Dokumen berikut adalah contoh cara menggunakan PromptFlow dengan ONNX (Open Neural Network Exchange) untuk membangunkan aplikasi AI berdasarkan model Phi-3.

PromptFlow adalah satu set alat pembangunan yang direka untuk memudahkan kitaran pembangunan menyeluruh aplikasi AI berasaskan LLM (Large Language Model), dari idea dan prototaip hingga ujian dan penilaian.

Dengan menggabungkan PromptFlow dengan ONNX, pembangun boleh:

- Mengoptimumkan Prestasi Model: Memanfaatkan ONNX untuk inferens model dan penyebaran yang cekap.
- Memudahkan Pembangunan: Gunakan PromptFlow untuk mengurus aliran kerja dan mengautomasikan tugasan berulang.
- Meningkatkan Kerjasama: Memudahkan kerjasama yang lebih baik antara ahli pasukan dengan menyediakan persekitaran pembangunan yang bersatu.

**Prompt flow** adalah satu set alat pembangunan yang direka untuk memudahkan kitaran pembangunan menyeluruh aplikasi AI berasaskan LLM, dari idea, prototaip, ujian, penilaian hingga penyebaran dan pemantauan produksi. Ia memudahkan kejuruteraan prompt dan membolehkan anda membina aplikasi LLM dengan kualiti produksi.

Prompt flow boleh disambungkan ke OpenAI, Azure OpenAI Service, dan model yang boleh disesuaikan (Huggingface, LLM/SLM tempatan). Kami berharap dapat menyebarkan model ONNX kuantisasi Phi-3.5 ke aplikasi tempatan. Prompt flow boleh membantu kami merancang perniagaan dengan lebih baik dan melengkapkan penyelesaian tempatan berdasarkan Phi-3.5. Dalam contoh ini, kami akan menggabungkan ONNX Runtime GenAI Library untuk melengkapkan penyelesaian Prompt flow berdasarkan Windows GPU.

## **Pemasangan**

### **ONNX Runtime GenAI untuk Windows GPU**

Baca panduan ini untuk menetapkan ONNX Runtime GenAI untuk Windows GPU [klik di sini](./ORTWindowGPUGuideline.md)

### **Sediakan Prompt flow dalam VSCode**

1. Pasang Sambungan Prompt flow VS Code

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.ms.png)

2. Selepas memasang Sambungan Prompt flow VS Code, klik sambungan tersebut, dan pilih **Installation dependencies** ikut panduan ini untuk memasang Prompt flow SDK dalam persekitaran anda

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.ms.png)

3. Muat turun [Kod Contoh](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) dan gunakan VS Code untuk membuka contoh ini

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.ms.png)

4. Buka **flow.dag.yaml** untuk memilih persekitaran Python anda

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.ms.png)

   Buka **chat_phi3_ort.py** untuk menukar lokasi Model Phi-3.5-instruct ONNX anda

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.ms.png)

5. Jalankan prompt flow anda untuk ujian

Buka **flow.dag.yaml** klik editor visual

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.ms.png)

selepas klik ini, dan jalankan untuk menguji

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.ms.png)

1. Anda boleh jalankan batch dalam terminal untuk memeriksa lebih banyak keputusan


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Anda boleh semak keputusan dalam pelayar lalai anda


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.ms.png)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.