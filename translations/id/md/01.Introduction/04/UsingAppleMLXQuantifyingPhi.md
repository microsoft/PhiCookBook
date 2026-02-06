# **Mengkuantisasi Phi-3.5 menggunakan Apple MLX Framework**

MLX adalah framework array untuk riset machine learning di Apple silicon, dibawa oleh riset machine learning Apple.

MLX dirancang oleh peneliti machine learning untuk peneliti machine learning. Framework ini dibuat agar mudah digunakan, namun tetap efisien untuk melatih dan menjalankan model. Desain framework ini juga secara konsep sederhana. Kami bertujuan agar peneliti dapat dengan mudah mengembangkan dan meningkatkan MLX untuk mempercepat eksplorasi ide-ide baru.

LLM dapat dipercepat di perangkat Apple Silicon melalui MLX, dan model dapat dijalankan secara lokal dengan sangat mudah.

Sekarang Apple MLX Framework mendukung konversi kuantisasi untuk Phi-3.5-Instruct (**dukungan Apple MLX Framework**), Phi-3.5-Vision (**dukungan MLX-VLM Framework**), dan Phi-3.5-MoE (**dukungan Apple MLX Framework**). Mari kita coba selanjutnya:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 Contoh untuk Phi-3.5 dengan Apple MLX**

| Labs    | Perkenalan | Mulai |
| -------- | ------- |  ------- |
| 🚀 Lab-Perkenalan Phi-3.5 Instruct  | Pelajari cara menggunakan Phi-3.5 Instruct dengan Apple MLX framework   |  [Mulai](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Perkenalan Phi-3.5 Vision (gambar) | Pelajari cara menggunakan Phi-3.5 Vision untuk menganalisis gambar dengan Apple MLX framework     |  [Mulai](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Perkenalan Phi-3.5 Vision (moE)   | Pelajari cara menggunakan Phi-3.5 MoE dengan Apple MLX framework  |  [Mulai](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Sumber Daya**

1. Pelajari tentang Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Repositori GitHub Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Repositori GitHub MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.