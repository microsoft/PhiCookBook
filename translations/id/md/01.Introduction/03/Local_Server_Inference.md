<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-05-09T12:06:54+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "id"
}
-->
# **Inference Phi-3 di Server Lokal**

Kita bisa menjalankan Phi-3 di server lokal. Pengguna dapat memilih solusi [Ollama](https://ollama.com) atau [LM Studio](https://llamaedge.com), atau mereka bisa menulis kode sendiri. Kamu dapat menghubungkan layanan lokal Phi-3 melalui [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) atau [Langchain](https://www.langchain.com/) untuk membangun aplikasi Copilot.

## **Menggunakan Semantic Kernel untuk mengakses Phi-3-mini**

Dalam aplikasi Copilot, kita membuat aplikasi melalui Semantic Kernel / LangChain. Kerangka aplikasi jenis ini umumnya kompatibel dengan Azure OpenAI Service / model OpenAI, dan juga dapat mendukung model open source di Hugging Face serta model lokal. Apa yang harus kita lakukan jika ingin menggunakan Semantic Kernel untuk mengakses Phi-3-mini? Menggunakan .NET sebagai contoh, kita bisa menggabungkannya dengan Hugging Face Connector di Semantic Kernel. Secara default, ini akan mengacu pada model id di Hugging Face (pertama kali digunakan, model akan diunduh dari Hugging Face, yang memakan waktu lama). Kamu juga bisa menghubungkan ke layanan lokal yang dibangun sendiri. Dibandingkan keduanya, kami merekomendasikan menggunakan yang terakhir karena memiliki tingkat otonomi lebih tinggi, terutama dalam aplikasi perusahaan.

![sk](../../../../../translated_images/sk.c244b32f4811c6f0938b9e95b0b2f4b28105bff6495bdc3b24cd42b3e3e89bb9.id.png)

Dari gambar tersebut, mengakses layanan lokal melalui Semantic Kernel dapat dengan mudah terhubung ke server model Phi-3-mini yang dibangun sendiri. Berikut hasil jalannya:

![skrun](../../../../../translated_images/skrun.fb7a635a22ae8b7919d6e15c0eb27262526ed69728c5a1d2773a97d4562657c7.id.png)

***Sample Code*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.