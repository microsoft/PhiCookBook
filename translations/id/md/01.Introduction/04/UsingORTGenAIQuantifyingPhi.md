## **Cara menggunakan Model Builder untuk mengkuantisasi Phi-3.5**

Model Builder sekarang mendukung kuantisasi model ONNX untuk Phi-3.5 Instruct dan Phi-3.5-Vision

### **Phi-3.5-Instruct**

**Konversi kuantisasi INT4 dengan akselerasi CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Konversi kuantisasi INT4 dengan akselerasi CUDA**

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

2. Unduh microsoft/Phi-3.5-vision-instruct ke folder models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Silakan unduh file-file ini ke folder Phi-3.5-vision-instruct Anda

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

1. Model Builder saat ini mendukung konversi Phi-3.5-Instruct dan Phi-3.5-Vision, tetapi belum untuk Phi-3.5-MoE

2. Untuk menggunakan model kuantisasi ONNX, Anda dapat menggunakannya melalui SDK Generative AI extensions for onnxruntime

3. Kita perlu mempertimbangkan AI yang lebih bertanggung jawab, jadi setelah konversi kuantisasi model, disarankan melakukan pengujian hasil yang lebih efektif

4. Dengan mengkuantisasi model CPU INT4, kita dapat menerapkannya ke Edge Device yang memiliki skenario aplikasi lebih baik, sehingga kami telah menyelesaikan Phi-3.5-Instruct di sekitar INT4

## **Sumber Daya**

1. Pelajari lebih lanjut tentang Generative AI extensions for onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Repositori GitHub Generative AI extensions for onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.