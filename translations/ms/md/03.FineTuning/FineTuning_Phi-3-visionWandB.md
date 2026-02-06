# Phi-3-Vision-128K-Instruct Gambaran Projek

## Model

Phi-3-Vision-128K-Instruct, sebuah model multimodal ringan dan terkini, merupakan teras projek ini. Ia adalah sebahagian daripada keluarga model Phi-3 dan menyokong panjang konteks sehingga 128,000 token. Model ini dilatih menggunakan set data yang pelbagai termasuk data sintetik dan laman web awam yang disaring dengan teliti, menekankan kandungan berkualiti tinggi dan berfokus pada pemikiran mendalam. Proses latihan merangkumi penalaan halus secara terkawal dan pengoptimuman keutamaan langsung untuk memastikan pematuhan tepat kepada arahan, serta langkah keselamatan yang kukuh.

## Membuat data contoh adalah penting atas beberapa sebab:

1. **Ujian**: Data contoh membolehkan anda menguji aplikasi anda dalam pelbagai senario tanpa menjejaskan data sebenar. Ini sangat penting dalam fasa pembangunan dan persediaan.

2. **Penalaan Prestasi**: Dengan data contoh yang meniru skala dan kerumitan data sebenar, anda boleh mengenal pasti halangan prestasi dan mengoptimumkan aplikasi anda dengan sewajarnya.

3. **Prototip**: Data contoh boleh digunakan untuk membuat prototaip dan lakaran, yang membantu dalam memahami keperluan pengguna dan mendapatkan maklum balas.

4. **Analisis Data**: Dalam sains data, data contoh sering digunakan untuk analisis data eksploratori, latihan model, dan ujian algoritma.

5. **Keselamatan**: Menggunakan data contoh dalam persekitaran pembangunan dan ujian boleh membantu mengelakkan kebocoran data sebenar yang sensitif secara tidak sengaja.

6. **Pembelajaran**: Jika anda mempelajari teknologi atau alat baru, bekerja dengan data contoh boleh memberikan cara praktikal untuk mengaplikasikan apa yang telah dipelajari.

Ingat, kualiti data contoh anda boleh memberi impak besar kepada aktiviti-aktiviti ini. Ia harus sedekat mungkin dengan data sebenar dari segi struktur dan variasi.

### Penciptaan Data Contoh
[Generate DataSet Script](./CreatingSampleData.md)

## Set Data

Contoh set data yang baik adalah [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (tersedia di Huggingface).  
Set data contoh produk Burberry bersama metadata kategori produk, harga, dan tajuk dengan jumlah 3,040 baris, setiap satu mewakili produk unik. Set data ini membolehkan kita menguji keupayaan model untuk memahami dan mentafsir data visual, menghasilkan teks deskriptif yang menangkap butiran visual yang rumit dan ciri-ciri khusus jenama.

**Note:** Anda boleh menggunakan mana-mana set data yang mengandungi imej.

## Pemikiran Kompleks

Model perlu berfikir tentang harga dan penamaan hanya berdasarkan imej. Ini memerlukan model bukan sahaja mengenal pasti ciri visual tetapi juga memahami implikasinya dari segi nilai produk dan penjenamaan. Dengan mensintesis deskripsi teks yang tepat daripada imej, projek ini menonjolkan potensi integrasi data visual untuk meningkatkan prestasi dan kepelbagaian model dalam aplikasi dunia sebenar.

## Seni Bina Phi-3 Vision

Seni bina model adalah versi multimodal Phi-3. Ia memproses data teks dan imej, menggabungkan input ini ke dalam satu urutan untuk pemahaman dan tugasan penjanaan yang menyeluruh. Model menggunakan lapisan embedding berasingan untuk teks dan imej. Token teks ditukar menjadi vektor padat, manakala imej diproses melalui model visi CLIP untuk mengekstrak embedding ciri. Embedding imej ini kemudian diproyeksikan supaya sepadan dengan dimensi embedding teks, memastikan ia boleh digabungkan dengan lancar.

## Integrasi Embedding Teks dan Imej

Token khas dalam urutan teks menunjukkan di mana embedding imej harus dimasukkan. Semasa pemprosesan, token khas ini digantikan dengan embedding imej yang sepadan, membolehkan model mengendalikan teks dan imej sebagai satu urutan. Prompt untuk set data kami diformat menggunakan token khas <|image|> seperti berikut:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Contoh Kod
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.