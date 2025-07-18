<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-07-16T21:56:26+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "ms"
}
-->
# **Pengkuantitian Phi-3.5 menggunakan Rangka Kerja Apple MLX**

MLX adalah rangka kerja tatasusunan untuk penyelidikan pembelajaran mesin pada cip Apple silicon, dibawa kepada anda oleh penyelidikan pembelajaran mesin Apple.

MLX direka oleh penyelidik pembelajaran mesin untuk penyelidik pembelajaran mesin. Rangka kerja ini bertujuan untuk mesra pengguna, tetapi masih cekap untuk melatih dan melaksanakan model. Reka bentuk rangka kerja itu sendiri juga mudah dari segi konsep. Kami berhasrat untuk memudahkan penyelidik mengembangkan dan memperbaiki MLX dengan matlamat untuk meneroka idea baru dengan pantas.

LLM boleh dipercepatkan pada peranti Apple Silicon melalui MLX, dan model boleh dijalankan secara tempatan dengan sangat mudah.

Kini Rangka Kerja Apple MLX menyokong penukaran kuantisasi bagi Phi-3.5-Instruct (**Sokongan Rangka Kerja Apple MLX**), Phi-3.5-Vision (**Sokongan Rangka Kerja MLX-VLM**), dan Phi-3.5-MoE (**Sokongan Rangka Kerja Apple MLX**). Mari cuba seterusnya:

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

| Makmal    | Pengenalan | Pergi |
| -------- | ------- |  ------- |
| 🚀 Makmal-Pengenalan Phi-3.5 Instruct  | Pelajari cara menggunakan Phi-3.5 Instruct dengan rangka kerja Apple MLX   |  [Pergi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Makmal-Pengenalan Phi-3.5 Vision (imej) | Pelajari cara menggunakan Phi-3.5 Vision untuk menganalisis imej dengan rangka kerja Apple MLX     |  [Pergi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Makmal-Pengenalan Phi-3.5 Vision (moE)   | Pelajari cara menggunakan Phi-3.5 MoE dengan rangka kerja Apple MLX  |  [Pergi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Sumber**

1. Ketahui tentang Rangka Kerja Apple MLX [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Repositori GitHub Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Repositori GitHub MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.