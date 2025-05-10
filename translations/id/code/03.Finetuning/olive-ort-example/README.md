<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:33:21+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "id"
}
-->
# Fine-tune Phi3 menggunakan Olive

Dalam contoh ini Anda akan menggunakan Olive untuk:

1. Fine-tune adapter LoRA untuk mengklasifikasikan frasa menjadi Sad, Joy, Fear, Surprise.
1. Menggabungkan bobot adapter ke dalam model dasar.
1. Mengoptimalkan dan Mengkuantisasi model menjadi `int4`.

Kami juga akan menunjukkan cara melakukan inference pada model yang sudah di-fine-tune menggunakan ONNX Runtime (ORT) Generate API.

> **⚠️ Untuk Fine-tuning, Anda perlu memiliki GPU yang sesuai - misalnya, A10, V100, A100.**

## 💾 Instalasi

Buat lingkungan virtual Python baru (misalnya, menggunakan `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Selanjutnya, instal Olive dan dependensi untuk workflow fine-tuning:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fine-tune Phi3 menggunakan Olive
[File konfigurasi Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) berisi *workflow* dengan *passes* berikut:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Secara garis besar, workflow ini akan:

1. Fine-tune Phi3 (selama 150 langkah, yang bisa Anda ubah) menggunakan data dari [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Menggabungkan bobot adapter LoRA ke dalam model dasar. Ini akan menghasilkan satu artefak model dalam format ONNX.
1. Model Builder akan mengoptimalkan model untuk runtime ONNX *dan* mengkuantisasi model menjadi `int4`.

Untuk menjalankan workflow, jalankan:

```bash
olive run --config phrase-classification.json
```

Setelah Olive selesai, model Phi3 yang sudah di-fine-tune dan dioptimalkan dalam format `int4` dapat ditemukan di: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrasikan Phi3 yang sudah di-fine-tune ke aplikasi Anda

Untuk menjalankan aplikasi:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Respon ini harus berupa klasifikasi satu kata dari frasa (Sad/Joy/Fear/Surprise).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.