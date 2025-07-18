<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-07-16T22:03:04+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "id"
}
-->
# **Mengkuantisasi Phi-3.5 menggunakan Intel OpenVINO**

Intel adalah produsen CPU paling tradisional dengan banyak pengguna. Dengan berkembangnya machine learning dan deep learning, Intel juga ikut bersaing dalam akselerasi AI. Untuk inferensi model, Intel tidak hanya menggunakan GPU dan CPU, tetapi juga menggunakan NPU.

Kami berharap dapat menerapkan Keluarga Phi-3.x di sisi akhir, dengan harapan menjadi bagian terpenting dari AI PC dan Copilot PC. Pemuatan model di sisi akhir bergantung pada kerja sama berbagai produsen perangkat keras. Bab ini terutama berfokus pada skenario aplikasi Intel OpenVINO sebagai model kuantitatif.

## **Apa itu OpenVINO**

OpenVINO adalah toolkit open-source untuk mengoptimalkan dan menerapkan model deep learning dari cloud ke edge. Ini mempercepat inferensi deep learning di berbagai kasus penggunaan, seperti generative AI, video, audio, dan bahasa dengan model dari framework populer seperti PyTorch, TensorFlow, ONNX, dan lainnya. Mengonversi dan mengoptimalkan model, serta menerapkannya di berbagai perangkat keras dan lingkungan Intel®, baik secara lokal maupun di perangkat, di browser atau di cloud.

Sekarang dengan OpenVINO, Anda dapat dengan cepat mengkuantisasi model GenAI di perangkat keras Intel dan mempercepat referensi model.

Saat ini OpenVINO mendukung konversi kuantisasi untuk Phi-3.5-Vision dan Phi-3.5 Instruct

### **Pengaturan Lingkungan**

Pastikan ketergantungan lingkungan berikut sudah terpasang, ini adalah requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Mengkuantisasi Phi-3.5-Instruct menggunakan OpenVINO**

Di Terminal, jalankan skrip ini

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Mengkuantisasi Phi-3.5-Vision menggunakan OpenVINO**

Jalankan skrip ini di Python atau Jupyter lab

```python

import requests
from pathlib import Path
from ov_phi3_vision import convert_phi3_model
import nncf

if not Path("ov_phi3_vision.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/ov_phi3_vision.py")
    open("ov_phi3_vision.py", "w").write(r.text)


if not Path("gradio_helper.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/gradio_helper.py")
    open("gradio_helper.py", "w").write(r.text)

if not Path("notebook_utils.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/utils/notebook_utils.py")
    open("notebook_utils.py", "w").write(r.text)



model_id = "microsoft/Phi-3.5-vision-instruct"
out_dir = Path("../model/phi-3.5-vision-128k-instruct-ov")
compression_configuration = {
    "mode": nncf.CompressWeightsMode.INT4_SYM,
    "group_size": 64,
    "ratio": 0.6,
}
if not out_dir.exists():
    convert_phi3_model(model_id, out_dir, compression_configuration)

```

### **🤖 Contoh untuk Phi-3.5 dengan Intel OpenVINO**

| Labs    | Deskripsi | Mulai |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Pelajari cara menggunakan Phi-3.5 Instruct di AI PC Anda    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (gambar) | Pelajari cara menggunakan Phi-3.5 Vision untuk menganalisis gambar di AI PC Anda      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | Pelajari cara menggunakan Phi-3.5 Vision untuk menganalisis video di AI PC Anda    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Sumber Daya**

1. Pelajari lebih lanjut tentang Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.