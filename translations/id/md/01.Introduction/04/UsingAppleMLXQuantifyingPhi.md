<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-09T13:47:45+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "id"
}
-->
# **Mengkuantisasi Phi-3.5 menggunakan Apple MLX Framework**

MLX adalah framework array untuk riset machine learning di Apple silicon, dibawa oleh riset machine learning Apple.

MLX dirancang oleh peneliti machine learning untuk peneliti machine learning. Framework ini dibuat agar mudah digunakan, namun tetap efisien untuk melatih dan menjalankan model. Desain framework ini juga secara konsep sederhana. Kami bermaksud membuatnya mudah bagi peneliti untuk memperluas dan meningkatkan MLX dengan tujuan cepat mengeksplorasi ide-ide baru.

LLM dapat dipercepat di perangkat Apple Silicon melalui MLX, dan model dapat dijalankan secara lokal dengan sangat mudah.

Sekarang Apple MLX Framework mendukung konversi kuantisasi Phi-3.5-Instruct(**Dukungan Apple MLX Framework**), Phi-3.5-Vision(**Dukungan MLX-VLM Framework**), dan Phi-3.5-MoE(**Dukungan Apple MLX Framework**). Mari coba berikut ini:

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

| Labs    | Perkenalan | Buka |
| -------- | ------- |  ------- |
| 🚀 Lab-Perkenalan Phi-3.5 Instruct  | Pelajari cara menggunakan Phi-3.5 Instruct dengan framework Apple MLX   |  [Buka](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Perkenalan Phi-3.5 Vision (gambar) | Pelajari cara menggunakan Phi-3.5 Vision untuk menganalisis gambar dengan framework Apple MLX     |  [Buka](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Perkenalan Phi-3.5 Vision (moE)   | Pelajari cara menggunakan Phi-3.5 MoE dengan framework Apple MLX  |  [Buka](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Sumber Daya**

1. Pelajari tentang Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Repositori Apple MLX di GitHub [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Repositori MLX-VLM di GitHub [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.