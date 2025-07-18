<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-07-17T08:12:31+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "id"
}
-->
# Ikhtisar Proyek Phi-3-Vision-128K-Instruct

## Model

Phi-3-Vision-128K-Instruct, sebuah model multimodal ringan dan mutakhir, menjadi inti dari proyek ini. Model ini merupakan bagian dari keluarga model Phi-3 dan mendukung panjang konteks hingga 128.000 token. Model ini dilatih menggunakan dataset yang beragam, termasuk data sintetis dan situs web publik yang telah disaring dengan cermat, dengan penekanan pada konten berkualitas tinggi dan yang membutuhkan kemampuan penalaran. Proses pelatihan mencakup fine-tuning terawasi dan optimasi preferensi langsung untuk memastikan kepatuhan yang tepat terhadap instruksi, serta langkah-langkah keamanan yang kuat.

## Membuat data sampel sangat penting karena beberapa alasan:

1. **Pengujian**: Data sampel memungkinkan Anda menguji aplikasi dalam berbagai skenario tanpa memengaruhi data asli. Ini sangat penting terutama pada tahap pengembangan dan staging.

2. **Penyetelan Kinerja**: Dengan data sampel yang meniru skala dan kompleksitas data asli, Anda dapat mengidentifikasi hambatan kinerja dan mengoptimalkan aplikasi sesuai kebutuhan.

3. **Prototyping**: Data sampel dapat digunakan untuk membuat prototipe dan mockup, yang membantu memahami kebutuhan pengguna dan mendapatkan umpan balik.

4. **Analisis Data**: Dalam ilmu data, data sampel sering digunakan untuk analisis eksplorasi, pelatihan model, dan pengujian algoritma.

5. **Keamanan**: Menggunakan data sampel di lingkungan pengembangan dan pengujian dapat membantu mencegah kebocoran data sensitif secara tidak sengaja.

6. **Pembelajaran**: Jika Anda sedang mempelajari teknologi atau alat baru, bekerja dengan data sampel memberikan cara praktis untuk menerapkan apa yang telah dipelajari.

Ingat, kualitas data sampel Anda sangat memengaruhi aktivitas-aktivitas ini. Data tersebut sebaiknya sedekat mungkin dengan data asli dalam hal struktur dan variasi.

### Pembuatan Data Sampel
[Generate DataSet Script](./CreatingSampleData.md)

## Dataset

Contoh dataset sampel yang baik adalah [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (tersedia di Huggingface).  
Dataset sampel produk Burberry ini dilengkapi dengan metadata kategori produk, harga, dan judul dengan total 3.040 baris, masing-masing mewakili produk unik. Dataset ini memungkinkan kita menguji kemampuan model dalam memahami dan menginterpretasi data visual, menghasilkan teks deskriptif yang menangkap detail visual rumit dan karakteristik khusus merek.

**Note:** Anda dapat menggunakan dataset apa pun yang menyertakan gambar.

## Penalaran Kompleks

Model perlu melakukan penalaran tentang harga dan penamaan hanya berdasarkan gambar. Ini mengharuskan model tidak hanya mengenali fitur visual tetapi juga memahami implikasinya dalam hal nilai produk dan branding. Dengan mensintesis deskripsi teks yang akurat dari gambar, proyek ini menyoroti potensi integrasi data visual untuk meningkatkan kinerja dan fleksibilitas model dalam aplikasi dunia nyata.

## Arsitektur Phi-3 Vision

Arsitektur model adalah versi multimodal dari Phi-3. Model ini memproses data teks dan gambar, mengintegrasikan kedua input tersebut ke dalam satu urutan untuk pemahaman dan tugas generasi yang komprehensif. Model menggunakan lapisan embedding terpisah untuk teks dan gambar. Token teks diubah menjadi vektor padat, sementara gambar diproses melalui model visi CLIP untuk mengekstrak embedding fitur. Embedding gambar ini kemudian diproyeksikan agar sesuai dengan dimensi embedding teks, sehingga dapat diintegrasikan dengan mulus.

## Integrasi Embedding Teks dan Gambar

Token khusus dalam urutan teks menunjukkan di mana embedding gambar harus disisipkan. Saat pemrosesan, token khusus ini digantikan dengan embedding gambar yang sesuai, memungkinkan model menangani teks dan gambar sebagai satu urutan. Prompt untuk dataset kami diformat menggunakan token khusus <|image|> sebagai berikut:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Contoh Kode
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.