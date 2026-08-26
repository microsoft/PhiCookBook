# **Mengkuantisasi Keluarga Phi menggunakan ekstensi AI Generatif untuk onnxruntime**

## **Apa itu ekstensi AI Generatif untuk onnxruntime**

Ekstensi ini membantu Anda menjalankan AI generatif dengan ONNX Runtime( [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Ini menyediakan loop AI generatif untuk model ONNX, termasuk inferensi dengan ONNX Runtime, pemrosesan logit, pencarian dan pengambilan sampel, serta manajemen cache KV. Pengembang dapat memanggil metode tingkat tinggi generate(), atau menjalankan setiap iterasi model dalam sebuah loop, menghasilkan satu token pada satu waktu, dan secara opsional memperbarui parameter generasi di dalam loop. Ini mendukung pencarian greedy/beam dan pengambilan sampel TopP, TopK untuk menghasilkan urutan token dan pemrosesan logit bawaan seperti penalti pengulangan. Anda juga dapat dengan mudah menambahkan penilaian khusus.

Pada tingkat aplikasi, Anda dapat menggunakan ekstensi AI Generatif untuk onnxruntime untuk membangun aplikasi menggunakan C++/ C# / Python. Pada tingkat model, Anda dapat menggunakannya untuk menggabungkan model yang telah di-tune ulang dan melakukan pekerjaan penyebaran kuantitatif terkait.


## **Mengkuantisasi Phi-3.5 dengan ekstensi AI Generatif untuk onnxruntime**

### **Model yang Didukung**

Ekstensi AI Generatif untuk onnxruntime mendukung konversi kuantisasi Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Pembuat Model di ekstensi AI Generatif untuk onnxruntime**

Pembuat model sangat mempercepat pembuatan model ONNX yang dioptimalkan dan dikuantisasi yang berjalan dengan API generate() ONNX Runtime.

Melalui Pembuat Model, Anda dapat mengkuantisasi model ke INT4, INT8, FP16, FP32, dan menggabungkan berbagai metode akselerasi perangkat keras seperti CPU, CUDA, DirectML, Mobile, dll.

Untuk menggunakan Pembuat Model, Anda perlu menginstal

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Setelah instalasi, Anda dapat menjalankan skrip Pembuat Model dari terminal untuk melakukan konversi format dan kuantisasi model.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Pahami parameter yang relevan

1. **model_name** Ini adalah model di Hugging face, seperti microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, dll. Ini juga bisa berupa path tempat Anda menyimpan model

2. **path_to_output_folder** Path penyimpanan konversi kuantisasi

3. **execution_provider** Dukungan akselerasi perangkat keras berbeda, seperti cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Kami mengunduh model dari Hugging face dan menyimpannya secara lokal




***Catatan：*** <ul>Meskipun ekstensi AI Generatif untuk onnxruntime masih dalam pratinjau, mereka telah dimasukkan ke dalam Microsoft Olive, dan Anda juga dapat memanggil fungsi Pembuat Model ekstensi AI Generatif untuk onnxruntime melalui Microsoft Olive.</ul>

## **Cara menggunakan Pembuat Model untuk mengkuantisasi Phi-3.5**

Pembuat Model sekarang mendukung kuantisasi model ONNX untuk Phi-3.5 Instruct dan Phi-3.5-Vision

### **Phi-3.5-Instruct**


**Konversi yang dipercepat CPU dari kuantisasi INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Konversi yang dipercepat CUDA dari kuantisasi INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Atur lingkungan di terminal

```bash

mkdir models

cd models 

```

2. Unduh microsoft/Phi-3.5-vision-instruct di folder models
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Harap unduh file-file ini ke folder Phi-3.5-vision-instruct Anda

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Unduh file ini ke folder models
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Buka terminal

    Konversi dukungan ONNX dengan FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Catatan：**

1. Pembuat Model saat ini mendukung konversi Phi-3.5-Instruct dan Phi-3.5-Vision, tetapi tidak untuk Phi-3.5-MoE

2. Untuk menggunakan model kuantisasi ONNX, Anda dapat menggunakannya melalui SDK ekstensi AI Generatif untuk onnxruntime

3. Kita perlu mempertimbangkan AI yang lebih bertanggung jawab, jadi setelah konversi kuantisasi model, disarankan untuk melakukan pengujian hasil yang lebih efektif

4. Dengan mengkuantisasi model CPU INT4, kita dapat menyebarkannya ke Perangkat Edge, yang memiliki skenario aplikasi yang lebih baik, jadi kami telah menyelesaikan Phi-3.5-Instruct di sekitar INT 4


## **Sumber Daya**

1. Pelajari lebih lanjut tentang ekstensi AI Generatif untuk onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Repositori GitHub ekstensi AI Generatif untuk onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->