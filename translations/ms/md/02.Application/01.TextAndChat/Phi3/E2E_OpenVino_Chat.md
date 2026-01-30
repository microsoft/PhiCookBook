[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Kod ini mengeksport model ke format OpenVINO, memuatkannya, dan menggunakannya untuk menghasilkan respons berdasarkan arahan yang diberikan.

1. **Mengeksport Model**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - Arahan ini menggunakan alat `optimum-cli` untuk mengeksport model ke format OpenVINO, yang dioptimumkan untuk inferens yang cekap.  
   - Model yang dieksport ialah `"microsoft/Phi-3-mini-4k-instruct"`, dan ia disediakan untuk tugasan menjana teks berdasarkan konteks sebelumnya.  
   - Berat model dikuantisasi kepada integer 4-bit (`int4`), yang membantu mengurangkan saiz model dan mempercepatkan pemprosesan.  
   - Parameter lain seperti `group-size`, `ratio`, dan `sym` digunakan untuk melaraskan proses kuantisasi.  
   - Model yang dieksport disimpan dalam direktori `./model/phi3-instruct/int4`.

2. **Mengimport Pustaka yang Diperlukan**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - Baris ini mengimport kelas dari pustaka `transformers` dan modul `optimum.intel.openvino`, yang diperlukan untuk memuat dan menggunakan model.

3. **Menetapkan Direktori Model dan Konfigurasi**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` menentukan lokasi fail model disimpan.  
   - `ov_config` adalah kamus yang mengkonfigurasi model OpenVINO untuk mengutamakan latensi rendah, menggunakan satu aliran inferens, dan tidak menggunakan direktori cache.

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
   - Baris ini memuat model dari direktori yang ditetapkan, menggunakan tetapan konfigurasi yang telah ditentukan. Ia juga membenarkan pelaksanaan kod jauh jika perlu.

5. **Memuat Tokenizer**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - Baris ini memuat tokenizer, yang bertanggungjawab menukar teks kepada token yang boleh difahami oleh model.

6. **Menetapkan Argumen Tokenizer**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - Kamus ini menetapkan supaya token khas tidak ditambah ke output tokenized.

7. **Mendefinisikan Arahan**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - String ini menyediakan arahan perbualan di mana pengguna meminta pembantu AI untuk memperkenalkan dirinya.

8. **Men-token-kan Arahan**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - Baris ini menukar arahan kepada token yang boleh diproses oleh model, dan mengembalikan hasil sebagai tensor PyTorch.

9. **Menjana Respons**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - Baris ini menggunakan model untuk menjana respons berdasarkan token input, dengan maksimum 1024 token baru.

10. **Mendekod Respons**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - Baris ini menukar token yang dijana kembali kepada string yang boleh dibaca manusia, mengabaikan token khas, dan mengambil hasil pertama.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.