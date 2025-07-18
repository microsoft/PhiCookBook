<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:06:07+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "id"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Kode ini mengekspor model ke format OpenVINO, memuatnya, dan menggunakannya untuk menghasilkan respons terhadap prompt yang diberikan.

1. **Mengekspor Model**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - Perintah ini menggunakan alat `optimum-cli` untuk mengekspor model ke format OpenVINO, yang dioptimalkan untuk inferensi yang efisien.  
   - Model yang diekspor adalah `"microsoft/Phi-3-mini-4k-instruct"`, dan disiapkan untuk tugas menghasilkan teks berdasarkan konteks sebelumnya.  
   - Bobot model dikwantisasi ke bilangan bulat 4-bit (`int4`), yang membantu mengurangi ukuran model dan mempercepat pemrosesan.  
   - Parameter lain seperti `group-size`, `ratio`, dan `sym` digunakan untuk menyempurnakan proses kwantisasi.  
   - Model yang diekspor disimpan di direktori `./model/phi3-instruct/int4`.

2. **Mengimpor Perpustakaan yang Diperlukan**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - Baris-baris ini mengimpor kelas dari perpustakaan `transformers` dan modul `optimum.intel.openvino`, yang dibutuhkan untuk memuat dan menggunakan model.

3. **Menyiapkan Direktori Model dan Konfigurasi**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` menentukan lokasi penyimpanan file model.  
   - `ov_config` adalah kamus yang mengonfigurasi model OpenVINO agar memprioritaskan latensi rendah, menggunakan satu aliran inferensi, dan tidak menggunakan direktori cache.

4. **Memuat Model**:  
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```  
   - Baris ini memuat model dari direktori yang ditentukan, menggunakan pengaturan konfigurasi yang sudah didefinisikan sebelumnya. Ini juga mengizinkan eksekusi kode jarak jauh jika diperlukan.

5. **Memuat Tokenizer**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - Baris ini memuat tokenizer, yang bertugas mengubah teks menjadi token yang dapat dipahami oleh model.

6. **Menyiapkan Argumen Tokenizer**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - Kamus ini menentukan bahwa token khusus tidak akan ditambahkan ke hasil tokenisasi.

7. **Mendefinisikan Prompt**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - String ini mengatur prompt percakapan di mana pengguna meminta asisten AI untuk memperkenalkan dirinya.

8. **Melakukan Tokenisasi pada Prompt**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - Baris ini mengubah prompt menjadi token yang dapat diproses model, mengembalikan hasil dalam bentuk tensor PyTorch.

9. **Menghasilkan Respons**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - Baris ini menggunakan model untuk menghasilkan respons berdasarkan token input, dengan maksimal 1024 token baru.

10. **Mendekode Respons**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - Baris ini mengubah token yang dihasilkan kembali menjadi string yang dapat dibaca manusia, melewati token khusus, dan mengambil hasil pertama.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.