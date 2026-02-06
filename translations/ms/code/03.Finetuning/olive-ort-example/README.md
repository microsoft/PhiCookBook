# Laraskan Phi3 menggunakan Olive

Dalam contoh ini, anda akan menggunakan Olive untuk:

1. Laraskan penyesuai LoRA untuk mengklasifikasikan frasa kepada Sedih, Gembira, Takut, Terkejut.
1. Gabungkan berat penyesuai ke dalam model asas.
1. Optimumkan dan Kuantisasi model ke dalam `int4`.

Kami juga akan tunjukkan cara untuk inferens model yang telah dilaras menggunakan ONNX Runtime (ORT) Generate API.

> **⚠️ Untuk Larasan, anda perlu mempunyai GPU yang sesuai - contohnya, A10, V100, A100.**

## 💾 Pasang

Buat persekitaran maya Python baru (contohnya, menggunakan `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Seterusnya, pasang Olive dan kebergantungan untuk aliran kerja larasan:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Laraskan Phi3 menggunakan Olive
Fail [konfigurasi Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) mengandungi *aliran kerja* dengan *langkah* berikut:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Secara ringkas, aliran kerja ini akan:

1. Laraskan Phi3 (selama 150 langkah, yang boleh anda ubah) menggunakan data [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Gabungkan berat penyesuai LoRA ke dalam model asas. Ini akan menghasilkan satu artifak model dalam format ONNX.
1. Model Builder akan mengoptimumkan model untuk runtime ONNX *dan* mengkuantisasi model ke dalam `int4`.

Untuk menjalankan aliran kerja, jalankan:

```bash
olive run --config phrase-classification.json
```

Apabila Olive selesai, model Phi3 yang telah dilaras dan dioptimumkan `int4` anda boleh didapati di: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrasikan Phi3 yang telah dilaras ke dalam aplikasi anda

Untuk menjalankan aplikasi:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Respons ini sepatutnya berupa klasifikasi satu perkataan bagi frasa tersebut (Sedih/Gembira/Takut/Terkejut).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.