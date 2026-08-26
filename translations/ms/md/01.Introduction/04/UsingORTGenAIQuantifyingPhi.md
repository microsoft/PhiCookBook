# **Mengkuantifikasi Keluarga Phi menggunakan peluasan Generative AI untuk onnxruntime**

## **Apa itu peluasan Generative AI untuk onnxruntime**

Peluasan ini membantu anda menjalankan generatif AI dengan ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Ia menyediakan gelung generatif AI untuk model ONNX, termasuk inferens dengan ONNX Runtime, pemprosesan logit, pencarian dan pensampelan, serta pengurusan cache KV. Pembangun boleh memanggil kaedah generate() tahap tinggi, atau menjalankan setiap iterasi model dalam gelung, menjana satu token pada satu masa, dan secara pilihan mengemas kini parameter generasi di dalam gelung. Ia menyokong carian tamak/celah rasuk dan pensampelan TopP, TopK untuk menjana urutan token dan pemprosesan logit terbina dalam seperti penalti pengulangan. Anda juga boleh mudah menambah penilaian khas.

Pada peringkat aplikasi, anda boleh menggunakan peluasan Generative AI untuk onnxruntime untuk membina aplikasi menggunakan C++/ C# / Python. Pada peringkat model, anda boleh menggunakannya untuk menggabungkan model yang telah disesuaikan dan melakukan kerja pengeluaran kuantitatif berkaitan.


## **Mengkuantifikasi Phi-3.5 dengan peluasan Generative AI untuk onnxruntime**

### **Model yang Disokong**

Peluasan Generative AI untuk onnxruntime menyokong penukaran kuantisasi Microsoft Phi, Google Gemma, Mistral, Meta LLaMA。


### **Pembina Model dalam peluasan Generative AI untuk onnxruntime**

Pembina model mempercepat dengan ketara penciptaan model ONNX yang dioptimumkan dan dikuantisasi yang berjalan dengan API generate() ONNX Runtime.

Melalui Pembina Model, anda boleh mengkuantisasi model ke INT4, INT8, FP16, FP32, dan menggabungkan pelbagai kaedah pecutan perkakasan seperti CPU, CUDA, DirectML, Mudah Alih, dan lain-lain.

Untuk menggunakan Pembina Model, anda perlu memasang

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Selepas pemasangan, anda boleh menjalankan skrip Pembina Model dari terminal untuk melakukan penukaran format model dan kuantisasi.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Fahami parameter yang berkaitan

1. **model_name** Ini adalah model di Hugging face, seperti microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, dsb. Ia juga boleh menjadi jalan di mana anda menyimpan model

2. **path_to_output_folder** Laluan simpanan penukaran kuantisasi

3. **execution_provider** Sokongan pecutan perkakasan berbeza, seperti cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Kami memuat turun model dari Hugging face dan menyimpannya di cache secara tempatan




***Nota：*** <ul>Walaupun peluasan Generative AI untuk onnxruntime masih dalam pratonton, ia telah dimasukkan ke dalam Microsoft Olive, dan anda juga boleh memanggil fungsi Pembina Model peluasan Generative AI untuk onnxruntime melalui Microsoft Olive.</ul>

## **Cara menggunakan Pembina Model untuk mengkuantifikasi Phi-3.5**

Pembina Model kini menyokong kuantisasi model ONNX untuk Phi-3.5 Instruct dan Phi-3.5-Vision

### **Phi-3.5-Instruct**


**Penukaran dipercepat CPU bagi INT 4 yang dikuantisasi**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Penukaran dipercepat CUDA bagi INT 4 yang dikuantisasi**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Tetapkan persekitaran dalam terminal

```bash

mkdir models

cd models 

```

2. Muat turun microsoft/Phi-3.5-vision-instruct dalam folder model
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Sila muat turun fail-fail ini ke folder Phi-3.5-vision-instruct anda

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Muat turun fail ini ke folder model
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Pergi ke terminal

    Tukar sokongan ONNX dengan FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Nota：**

1. Pembina Model kini menyokong penukaran bagi Phi-3.5-Instruct dan Phi-3.5-Vision, tetapi bukan Phi-3.5-MoE

2. Untuk menggunakan model kuantisasi ONNX, anda boleh menggunakannya melalui SDK peluasan Generative AI untuk onnxruntime

3. Kita perlu mempertimbangkan AI yang lebih bertanggungjawab, jadi selepas penukaran kuantisasi model, disarankan melakukan ujian hasil yang lebih berkesan

4. Dengan mengkuantifikasi model CPU INT4, kita boleh menyebarkannya ke Peranti Edge, yang mempunyai senario aplikasi yang lebih baik, jadi kita telah menyiapkan Phi-3.5-Instruct sekitar INT 4


## **Sumber**

1. Ketahui lebih lanjut mengenai peluasan Generative AI untuk onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Repositori GitHub peluasan Generative AI untuk onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->