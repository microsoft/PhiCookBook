<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-07-16T16:18:25+00:00",
  "source_file": "code/04.Finetuning/olive-lab/readme.md",
  "language_code": "ms"
}
-->
# Makmal. Optimumkan model AI untuk inferens peranti

## Pengenalan

> [!IMPORTANT]
> Makmal ini memerlukan **GPU Nvidia A10 atau A100** dengan pemacu berkaitan dan toolkit CUDA (versi 12+) yang dipasang.

> [!NOTE]
> Ini adalah makmal **35 minit** yang akan memberikan anda pengenalan praktikal kepada konsep teras mengoptimumkan model untuk inferens peranti menggunakan OLIVE.

## Objektif Pembelajaran

Menjelang akhir makmal ini, anda akan dapat menggunakan OLIVE untuk:

- Kuantisasi Model AI menggunakan kaedah kuantisasi AWQ.
- Melatih semula model AI untuk tugasan tertentu.
- Menjana penyesuai LoRA (model yang dilatih semula) untuk inferens peranti yang cekap pada ONNX Runtime.

### Apa itu Olive

Olive (*O*NNX *live*) adalah toolkit pengoptimuman model dengan CLI yang membolehkan anda menghantar model untuk ONNX runtime +++https://onnxruntime.ai+++ dengan kualiti dan prestasi.

![Olive Flow](../../../../../translated_images/olive-flow.c4f76d9142c579b2.ms.png)

Input kepada Olive biasanya model PyTorch atau Hugging Face dan outputnya adalah model ONNX yang dioptimumkan yang dijalankan pada peranti (sasaran penyebaran) yang menggunakan ONNX runtime. Olive akan mengoptimumkan model untuk pemecut AI sasaran penyebaran (NPU, GPU, CPU) yang disediakan oleh pembekal perkakasan seperti Qualcomm, AMD, Nvidia atau Intel.

Olive melaksanakan *workflow*, iaitu urutan teratur tugas pengoptimuman model individu yang dipanggil *passes* - contoh passes termasuk: pemampatan model, tangkapan graf, kuantisasi, pengoptimuman graf. Setiap pass mempunyai set parameter yang boleh dilaras untuk mencapai metrik terbaik, contohnya ketepatan dan kelewatan, yang dinilai oleh penilai masing-masing. Olive menggunakan strategi carian yang menggunakan algoritma carian untuk melaras setiap pass satu persatu atau set passes bersama-sama secara automatik.

#### Manfaat Olive

- **Kurangkan kekecewaan dan masa** eksperimen manual cuba-cuba dengan teknik berbeza untuk pengoptimuman graf, pemampatan dan kuantisasi. Tetapkan had kualiti dan prestasi anda dan biarkan Olive secara automatik mencari model terbaik untuk anda.
- **40+ komponen pengoptimuman model terbina dalam** merangkumi teknik terkini dalam kuantisasi, pemampatan, pengoptimuman graf dan latihan semula.
- **CLI yang mudah digunakan** untuk tugasan pengoptimuman model biasa. Contohnya, olive quantize, olive auto-opt, olive finetune.
- Pembungkusan dan penyebaran model terbina dalam.
- Menyokong penjanaan model untuk **Perkhidmatan Multi LoRA**.
- Membina workflow menggunakan YAML/JSON untuk mengatur tugasan pengoptimuman model dan penyebaran.
- Integrasi **Hugging Face** dan **Azure AI**.
- Mekanisme **penyimpanan cache** terbina dalam untuk **menjimatkan kos**.

## Arahan Makmal
> [!NOTE]
> Sila pastikan anda telah menyediakan Azure AI Hub dan Projek anda serta menyediakan pengkomputeran A100 anda seperti dalam Makmal 1.

### Langkah 0: Sambung ke Azure AI Compute anda

Anda akan menyambung ke pengkomputeran Azure AI menggunakan ciri jauh dalam **VS Code.**

1. Buka aplikasi desktop **VS Code** anda:
1. Buka **command palette** menggunakan **Shift+Ctrl+P**
1. Dalam command palette, cari **AzureML - remote: Connect to compute instance in New Window**.
1. Ikuti arahan di skrin untuk menyambung ke Compute. Ini melibatkan memilih Langganan Azure, Kumpulan Sumber, Projek dan nama Compute yang anda sediakan dalam Makmal 1.
1. Setelah anda disambungkan ke nod Azure ML Compute, ia akan dipaparkan di **bahagian bawah kiri Visual Code** `><Azure ML: Compute Name`

### Langkah 1: Klon repo ini

Dalam VS Code, anda boleh buka terminal baru dengan **Ctrl+J** dan klon repo ini:

Dalam terminal anda akan melihat prompt

```
azureuser@computername:~/cloudfiles/code$ 
```
Klon penyelesaian

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Langkah 2: Buka Folder dalam VS Code

Untuk membuka VS Code dalam folder yang berkaitan, jalankan arahan berikut dalam terminal, yang akan membuka tetingkap baru:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Sebagai alternatif, anda boleh buka folder dengan memilih **File** > **Open Folder**.

### Langkah 3: Pergantungan

Buka tetingkap terminal dalam VS Code pada Azure AI Compute Instance anda (petua: **Ctrl+J**) dan jalankan arahan berikut untuk memasang pergantungan:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> Ia akan mengambil masa kira-kira 5 minit untuk memasang semua pergantungan.

Dalam makmal ini anda akan memuat turun dan memuat naik model ke katalog Model Azure AI. Untuk mengakses katalog model, anda perlu log masuk ke Azure menggunakan:

```bash
az login
```

> [!NOTE]
> Semasa log masuk, anda akan diminta memilih langganan anda. Pastikan anda tetapkan langganan kepada yang disediakan untuk makmal ini.

### Langkah 4: Jalankan arahan Olive

Buka tetingkap terminal dalam VS Code pada Azure AI Compute Instance anda (petua: **Ctrl+J**) dan pastikan persekitaran conda `olive-ai` diaktifkan:

```bash
conda activate olive-ai
```

Seterusnya, jalankan arahan Olive berikut dalam baris arahan.

1. **Periksa data:** Dalam contoh ini, anda akan melatih semula model Phi-3.5-Mini supaya ia khusus menjawab soalan berkaitan perjalanan. Kod di bawah memaparkan beberapa rekod pertama dataset, yang dalam format baris JSON:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **Kuantisasi model:** Sebelum melatih model, anda kuantisasi terlebih dahulu dengan arahan berikut yang menggunakan teknik dipanggil Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ mengkuantisasi berat model dengan mengambil kira aktivasi yang dihasilkan semasa inferens. Ini bermakna proses kuantisasi mengambil kira taburan data sebenar dalam aktivasi, menghasilkan pemeliharaan ketepatan model yang lebih baik berbanding kaedah kuantisasi berat tradisional.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    Ia mengambil masa **~8 minit** untuk melengkapkan kuantisasi AWQ, yang akan **mengurangkan saiz model dari ~7.5GB ke ~2.5GB**.
   
   Dalam makmal ini, kami menunjukkan cara memasukkan model dari Hugging Face (contoh: `microsoft/Phi-3.5-mini-instruct`). Walau bagaimanapun, Olive juga membolehkan anda memasukkan model dari katalog Azure AI dengan mengemas kini argumen `model_name_or_path` kepada ID aset Azure AI (contoh: `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`).

1. **Latih model:** Seterusnya, arahan `olive finetune` melatih semula model yang telah dikuantisasi. Kuantisasi model *sebelum* latihan semula memberikan ketepatan yang lebih baik kerana proses latihan semula memulihkan sebahagian kehilangan akibat kuantisasi.
    
    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```
    
    Ia mengambil masa **~6 minit** untuk melengkapkan latihan semula (dengan 100 langkah).

1. **Optimumkan:** Dengan model yang telah dilatih, anda kini mengoptimumkan model menggunakan arahan `auto-opt` Olive, yang akan menangkap graf ONNX dan secara automatik melakukan beberapa pengoptimuman untuk meningkatkan prestasi model bagi CPU dengan memampatkan model dan melakukan penggabungan. Perlu diingat, anda juga boleh mengoptimumkan untuk peranti lain seperti NPU atau GPU dengan hanya mengemas kini argumen `--device` dan `--provider` - tetapi untuk tujuan makmal ini kita akan gunakan CPU.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```
    
    Ia mengambil masa **~5 minit** untuk melengkapkan pengoptimuman.

### Langkah 5: Ujian pantas inferens model

Untuk menguji inferens model, buat fail Python dalam folder anda bernama **app.py** dan salin tampal kod berikut:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

Jalankan kod menggunakan:

```bash
python app.py
```

### Langkah 6: Muat naik model ke Azure AI

Muat naik model ke repositori model Azure AI membolehkan model dikongsi dengan ahli pasukan pembangunan lain dan juga mengurus kawalan versi model. Untuk memuat naik model, jalankan arahan berikut:

> [!NOTE]
> Kemas kini tempat letak `{}` dengan nama kumpulan sumber dan Nama Projek Azure AI anda.

Untuk mencari kumpulan sumber `"resourceGroup"` dan Nama Projek Azure AI, jalankan arahan berikut

```
az ml workspace show
```

Atau dengan pergi ke +++ai.azure.com+++ dan memilih **management center** **project** **overview**

Kemas kini tempat letak `{}` dengan nama kumpulan sumber dan Nama Projek Azure AI anda.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
Anda kemudian boleh melihat model yang dimuat naik dan menyebarkan model anda di https://ml.azure.com/model/list

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.