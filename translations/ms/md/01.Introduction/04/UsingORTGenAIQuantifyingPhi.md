## **Cara menggunakan Model Builder untuk mengkuantisasi Phi-3.5**

Model Builder kini menyokong kuantisasi model ONNX untuk Phi-3.5 Instruct dan Phi-3.5-Vision

### **Phi-3.5-Instruct**

**Penukaran kuantisasi INT 4 dipercepatkan oleh CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Penukaran kuantisasi INT 4 dipercepatkan oleh CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Tetapkan persekitaran di terminal

```bash

mkdir models

cd models 

```

2. Muat turun microsoft/Phi-3.5-vision-instruct ke dalam folder models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Sila muat turun fail-fail ini ke folder Phi-3.5-vision-instruct anda

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Muat turun fail ini ke dalam folder models  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Pergi ke terminal

    Tukar sokongan ONNX dengan FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Nota：**

1. Model Builder kini menyokong penukaran Phi-3.5-Instruct dan Phi-3.5-Vision, tetapi tidak untuk Phi-3.5-MoE

2. Untuk menggunakan model kuantisasi ONNX, anda boleh menggunakannya melalui Generative AI extensions for onnxruntime SDK

3. Kita perlu mengambil kira AI yang lebih bertanggungjawab, jadi selepas penukaran kuantisasi model, disarankan untuk melakukan ujian hasil yang lebih berkesan

4. Dengan mengkuantisasi model CPU INT4, kita boleh melaksanakan pada Peranti Edge, yang mempunyai senario aplikasi yang lebih baik, jadi kami telah menyiapkan Phi-3.5-Instruct sekitar INT 4

## **Sumber**

1. Ketahui lebih lanjut mengenai Generative AI extensions for onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Repositori GitHub Generative AI extensions for onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.