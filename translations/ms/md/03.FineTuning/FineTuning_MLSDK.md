## Cara menggunakan komponen chat-completion dari daftar sistem Azure ML untuk melatih model dengan lebih tepat

Dalam contoh ini kami akan melaksanakan pelarasan tepat (fine tuning) model Phi-3-mini-4k-instruct untuk melengkapkan perbualan antara 2 orang menggunakan dataset ultrachat_200k.

![MLFineTune](../../../../translated_images/ms/MLFineTune.928d4c6b3767dd35.webp)

Contoh ini akan menunjukkan bagaimana melakukan pelarasan tepat menggunakan Azure ML SDK dan Python dan kemudian mengendalikan model yang telah dilaras tepat ke titik hujung dalam talian untuk inferens masa nyata.

### Data latihan

Kami akan menggunakan dataset ultrachat_200k. Ini adalah versi UltraChat dataset yang sangat ditapis dan digunakan untuk melatih Zephyr-7B-β, model chat 7b terkini.

### Model

Kami akan menggunakan model Phi-3-mini-4k-instruct untuk menunjukkan bagaimana pengguna boleh melaras tepat model untuk tugasan chat-completion. Jika anda membuka buku nota ini daripada kad model tertentu, ingat untuk menggantikan nama model tersebut.

### Tugasan

- Pilih model untuk dilaras tepat.
- Pilih dan terokai data latihan.
- Konfigurasikan tugasan pelarasan tepat.
- Jalankan tugasan pelarasan tepat.
- Semak metrik latihan dan penilaian.
- Daftarkan model yang telah dilaras tepat.
- Kembangkan model yang telah dilaras tepat untuk inferens masa nyata.
- Bersihkan sumber.

## 1. Sediakan pra-syarat

- Pasang kebergantungan
- Sambungkan ke AzureML Workspace. Ketahui lebih lanjut di set up SDK authentication. Gantikan <WORKSPACE_NAME>, <RESOURCE_GROUP> dan <SUBSCRIPTION_ID> di bawah.
- Sambungkan ke daftar sistem azureml
- Tetapkan nama eksperimen pilihan
- Semak atau cipta compute.

> [!NOTE]
> Keperluan adalah satu nod GPU boleh mempunyai berbilang kad GPU. Sebagai contoh, dalam satu nod Standard_NC24rs_v3 terdapat 4 NVIDIA V100 GPUs manakala dalam Standard_NC12s_v3 terdapat 2 NVIDIA V100 GPUs. Rujuk dokumentasi untuk maklumat ini. Bilangan kad GPU per nod ditetapkan dalam parameter gpus_per_node di bawah. Menetapkan nilai ini dengan betul akan memastikan penggunaan semua GPU dalam nod. SKU compute GPU yang disyorkan boleh didapati di sini dan di sini.

### Perpustakaan Python

Pasang kebergantungan dengan menjalankan sel di bawah. Ini bukan langkah pilihan jika menjalankan dalam persekitaran baru.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Berinteraksi dengan Azure ML

1. Skrip Python ini digunakan untuk berinteraksi dengan perkhidmatan Azure Machine Learning (Azure ML). Berikut adalah pecahan apa yang dilakukannya:

    - Ia mengimport modul-modul yang diperlukan dari pakej azure.ai.ml, azure.identity, dan azure.ai.ml.entities. Ia juga mengimport modul time.

    - Ia cuba mengesahkan menggunakan DefaultAzureCredential(), yang menyediakan pengalaman pengesahan yang mudah untuk memulakan pembangunan aplikasi yang dijalankan di awan Azure. Jika gagal, ia beralih ke InteractiveBrowserCredential(), yang menyediakan arahan log masuk interaktif.

    - Ia kemudian cuba membuat instance MLClient menggunakan kaedah from_config, yang membaca konfigurasi dari fail config lalai (config.json). Jika gagal, ia membuat instance MLClient secara manual dengan menyediakan subscription_id, resource_group_name, dan workspace_name.

    - Ia membuat satu lagi instance MLClient, kali ini untuk daftar Azure ML bernama "azureml". Daftar ini adalah tempat di mana model, paip pelarasan tepat, dan persekitaran disimpan.

    - Ia menetapkan experiment_name kepada "chat_completion_Phi-3-mini-4k-instruct".

    - Ia menjana cap waktu unik dengan menukar masa kini (dalam saat sejak epoch, sebagai nombor titik terapung) kepada integer dan kemudian kepada rentetan. Cap waktu ini boleh digunakan untuk mencipta nama dan versi unik.

    ```python
    # Import modul yang diperlukan dari Azure ML dan Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Import modul masa
    
    # Cuba untuk mengesahkan menggunakan DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # Jika DefaultAzureCredential gagal, gunakan InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Cuba untuk membuat contoh MLClient menggunakan fail konfigurasi lalai
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # Jika itu gagal, buat contoh MLClient dengan memberikan butiran secara manual
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Buat contoh MLClient lain untuk pendaftar Azure ML yang dinamakan "azureml"
    # Pendaftar ini adalah tempat model, saluran pemeliharaan halus, dan persekitaran disimpan
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Tetapkan nama eksperimen
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Jana cap masa unik yang boleh digunakan untuk nama dan versi yang perlu unik
    timestamp = str(int(time.time()))
    ```

## 2. Pilih model asas untuk dilaras tepat

1. Phi-3-mini-4k-instruct ialah model ringan 3.8B parameter yang terkini dan dibina berdasarkan dataset yang digunakan untuk Phi-2. Model ini tergolong dalam keluarga model Phi-3, dan versi Mini datang dalam dua varian 4K dan 128K yang menunjukkan panjang konteks (dalam token) yang boleh disokong. Kita perlu melaras tepat model ini untuk tujuan khusus kita bagi menggunakannya. Anda boleh melayari model ini di Katalog Model dalam AzureML Studio, dengan menapis mengikut tugasan chat-completion. Dalam contoh ini, kami menggunakan model Phi-3-mini-4k-instruct. Jika anda membuka buku nota ini untuk model lain, gantikan nama dan versi model mengikut keperluan.

> [!NOTE]
> id model adalah sifat model. Ini akan dihantar sebagai input kepada tugasan pelarasan tepat. Ia juga boleh didapati sebagai medan Asset ID dalam halaman butiran model di Katalog Model AzureML Studio.

2. Skrip Python ini berinteraksi dengan perkhidmatan Azure Machine Learning (Azure ML). Berikut adalah pecahan apa yang dilakukannya:

    - Ia menetapkan model_name kepada "Phi-3-mini-4k-instruct".

    - Ia menggunakan kaedah get daripada properti models objek registry_ml_client untuk mendapatkan versi terkini model dengan nama yang ditentukan dari daftar Azure ML. Kaedah get dipanggil dengan dua argumen: nama model dan label yang menyatakan versi terkini model hendak diambil.

    - Ia mencetak mesej di konsol yang menunjukkan nama, versi, dan id model yang akan digunakan untuk pelarasan tepat. Kaedah format digunakan untuk memasukkan nama, versi, dan id ke dalam mesej. Nama, versi, dan id diakses sebagai properti objek foundation_model.

    ```python
    # Tetapkan nama model
    model_name = "Phi-3-mini-4k-instruct"
    
    # Dapatkan versi terkini model dari registri Azure ML
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Cetak nama model, versi, dan id
    # Maklumat ini berguna untuk penjejakan dan penyahpepijatan
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. Cipta compute untuk tugasan

Tugasan pelarasan tepat BERFUNGSI HANYA dengan compute GPU. Saiz compute bergantung pada saiz model dan dalam kebanyakan kes sukar untuk mengenal pasti compute yang sesuai untuk tugasan. Dalam sel ini, kami membimbing pengguna untuk memilih compute yang betul.

> [!NOTE]
> Compute yang disenaraikan di bawah berfungsi dengan konfigurasi yang paling optimum. Sebarang perubahan kepada konfigurasi mungkin menyebabkan ralat Cuda Out Of Memory. Dalam kes demikian, cuba naik taraf compute kepada saiz yang lebih besar.

> [!NOTE]
> Semasa memilih compute_cluster_size di bawah, pastikan compute tersebut tersedia dalam kumpulan sumber anda. Jika compute tertentu tidak tersedia, anda boleh membuat permintaan akses ke sumber compute tersebut.

### Memeriksa Sokongan Pelarasan Tepat Model

1. Skrip Python ini berinteraksi dengan model Azure Machine Learning (Azure ML). Berikut adalah pecahan apa yang dilakukannya:

    - Ia mengimport modul ast, yang menyediakan fungsi untuk memproses pokok tatabahasa abstrak Python.

    - Ia memeriksa jika objek foundation_model (yang mewakili model di Azure ML) mempunyai tag bernama finetune_compute_allow_list. Tag dalam Azure ML adalah pasangan kunci-nilai yang anda boleh cipta dan gunakan untuk menapis dan menyusun model.

    - Jika tag finetune_compute_allow_list wujud, ia menggunakan fungsi ast.literal_eval untuk selamat mengurai nilai tag (rentetan) ke dalam senarai Python. Senarai ini kemudian ditetapkan ke pembolehubah computes_allow_list. Ia kemudian mencetak mesej bahawa compute harus dicipta dari senarai tersebut.

    - Jika tag finetune_compute_allow_list tidak wujud, ia menetapkan computes_allow_list kepada None dan mencetak mesej bahawa tag finetune_compute_allow_list bukan sebahagian dari tag model.

    - Ringkasnya, skrip ini memeriksa tag tertentu dalam metadata model, menukar nilai tag ke senarai jika wujud, dan memberi maklum balas kepada pengguna.

    ```python
    # Import modul ast, yang menyediakan fungsi untuk memproses pokok tatabahasa abstrak Python
    import ast
    
    # Periksa jika tag 'finetune_compute_allow_list' wujud dalam tag model
    if "finetune_compute_allow_list" in foundation_model.tags:
        # Jika tag wujud, gunakan ast.literal_eval untuk memproses nilai tag (sebuah string) secara selamat ke dalam senarai Python
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # menukar string kepada senarai python
        # Cetak mesej yang menunjukkan bahawa compute harus dibuat dari senarai tersebut
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Jika tag tidak wujud, tetapkan computes_allow_list kepada None
        computes_allow_list = None
        # Cetak mesej yang menunjukkan bahawa tag 'finetune_compute_allow_list' bukan sebahagian daripada tag model
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Memeriksa Compute Instance

1. Skrip Python ini berinteraksi dengan perkhidmatan Azure Machine Learning (Azure ML) dan melakukan beberapa pemeriksaan ke atas compute instance. Berikut adalah pecahan apa yang dilakukannya:

    - Ia cuba mendapatkan compute instance dengan nama yang disimpan dalam compute_cluster dari workspace Azure ML. Jika status penyediaan compute instance adalah "failed", ia membangkitkan ValueError.

    - Ia memeriksa jika computes_allow_list bukan None. Jika tidak, ia menukar semua saiz compute dalam senarai ke huruf kecil dan memeriksa jika saiz compute instance semasa ada dalam senarai. Jika tidak, ia membangkitkan ValueError.

    - Jika computes_allow_list ialah None, ia memeriksa jika saiz compute instance ada dalam senarai saiz VM GPU yang tidak disokong. Jika ada, ia membangkitkan ValueError.

    - Ia mendapatkan senarai semua saiz compute yang tersedia dalam workspace. Ia kemudian mengulangi senarai ini dan untuk setiap saiz compute, ia memeriksa jika namanya sepadan dengan saiz compute instance semasa. Jika sepadan, ia mendapatkan bilangan GPU bagi saiz compute itu dan menetapkan gpu_count_found kepada True.

    - Jika gpu_count_found True, ia mencetak bilangan GPU dalam compute instance. Jika tidak, ia membangkitkan ValueError.

    - Ringkasnya, skrip ini melakukan beberapa pemeriksaan ke atas compute instance dalam workspace Azure ML, termasuk memeriksa status penyediaan, saiz terhadap senarai dibenarkan atau disekat, dan bilangan GPU yang ada.

    ```python
    # Cetak mesej pengecualian
    print(e)
    # Timbulkan ValueError jika saiz pengiraan tidak tersedia dalam ruang kerja
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Dapatkan contoh pengiraan daripada ruang kerja Azure ML
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Semak jika keadaan penyediaan contoh pengiraan adalah "gagal"
    if compute.provisioning_state.lower() == "failed":
        # Timbulkan ValueError jika keadaan penyediaan adalah "gagal"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Semak jika computes_allow_list bukan None
    if computes_allow_list is not None:
        # Tukar semua saiz pengiraan dalam computes_allow_list kepada huruf kecil
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Semak jika saiz contoh pengiraan terdapat dalam computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Timbulkan ValueError jika saiz contoh pengiraan tidak terdapat dalam computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Takrifkan senarai saiz VM GPU yang tidak disokong
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Semak jika saiz contoh pengiraan terdapat dalam unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Timbulkan ValueError jika saiz contoh pengiraan terdapat dalam unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Inisialisasi penanda untuk memeriksa jika bilangan GPU dalam contoh pengiraan telah dijumpai
    gpu_count_found = False
    # Dapatkan senarai semua saiz pengiraan yang tersedia dalam ruang kerja
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Ulang atas senarai saiz pengiraan yang tersedia
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Semak jika nama saiz pengiraan sepadan dengan saiz contoh pengiraan
        if compute_sku.name.lower() == compute.size.lower():
            # Jika ya, dapatkan bilangan GPU untuk saiz pengiraan itu dan tetapkan gpu_count_found kepada True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # Jika gpu_count_found adalah True, cetak bilangan GPU dalam contoh pengiraan
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # Jika gpu_count_found adalah False, timbulkan ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. Pilih dataset untuk laras tepat model

1. Kami menggunakan dataset ultrachat_200k. Dataset ini mempunyai empat pecahan, sesuai untuk pelarasan tepat berarah (supervised fine-tuning, sft).
Peringkat penjanaan (gen). Bilangan contoh bagi setiap pecahan dipaparkan seperti berikut:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Beberapa sel berikut menunjukkan penyediaan data asas untuk pelarasan tepat:

### Visualisasikan beberapa baris data

Kami mahu contoh ini berjalan dengan cepat, jadi simpan fail train_sft, test_sft yang mengandungi 5% daripada baris yang telah dipotong. Ini bermakna model yang dilaras tepat akan mempunyai ketepatan lebih rendah, oleh itu ia tidak seharusnya digunakan dalam dunia sebenar.
download-dataset.py digunakan untuk memuat turun dataset ultrachat_200k dan menukar dataset ke format yang boleh digunakan komponen paip laras tepat. Oleh kerana dataset ini besar, kami hanya memuat sebahagian daripada dataset.

1. Menjalankan skrip berikut hanya memuat turun 5% data. Ini boleh ditingkatkan dengan menukar parameter dataset_split_pc ke peratusan yang dikehendaki.

> [!NOTE]
> Sesetengah model bahasa menggunakan kod bahasa berbeza, dan oleh itu nama lajur dalam dataset perlu mencerminkan perkara tersebut.

1. Berikut adalah contoh bagaimana data sepatutnya kelihatan
Dataset chat-completion disimpan dalam format parquet dengan setiap entri menggunakan skema berikut:

    - Ini adalah dokumen JSON (JavaScript Object Notation), format pertukaran data yang popular. Ia bukan kod yang boleh dilaksanakan, tetapi cara untuk menyimpan dan mengangkut data. Berikut adalah pecahan strukturnya:

    - "prompt": Kekunci ini memegang nilai rentetan yang mewakili tugasan atau soalan yang diberikan kepada pembantu AI.

    - "messages": Kekunci ini memegang susunan objek. Setiap objek mewakili mesej dalam perbualan antara pengguna dan pembantu AI. Setiap objek mesej mempunyai dua kekunci:

    - "content": Kekunci ini memegang nilai rentetan yang menunjukkan isi mesej.
    - "role": Kekunci ini memegang nilai rentetan yang menunjukkan peranan entiti yang menghantar mesej. Ia boleh sama ada "user" atau "assistant".
    - "prompt_id": Kekunci ini memegang nilai rentetan yang mewakili pengecam unik untuk prompt tersebut.

1. Dalam dokumen JSON khusus ini, perbualan ditunjukkan di mana pengguna meminta pembantu AI mencipta protagonis untuk cerita dystopian. Pembantu membalas, dan pengguna kemudian meminta lebih banyak butiran. Pembantu bersetuju untuk menyediakan lebih banyak butiran. Keseluruhan perbualan ini dikaitkan dengan id prompt tertentu.

    ```python
    {
        // The task or question posed to an AI assistant
        "prompt": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
        
        // An array of objects, each representing a message in a conversation between a user and an AI assistant
        "messages":[
            {
                // The content of the user's message
                "content": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
                // The role of the entity that sent the message
                "role": "user"
            },
            {
                // The content of the assistant's message
                "content": "Name: Ava\n\n Ava was just 16 years old when the world as she knew it came crashing down. The government had collapsed, leaving behind a chaotic and lawless society. ...",
                // The role of the entity that sent the message
                "role": "assistant"
            },
            {
                // The content of the user's message
                "content": "Wow, Ava's story is so intense and inspiring! Can you provide me with more details.  ...",
                // The role of the entity that sent the message
                "role": "user"
            }, 
            {
                // The content of the assistant's message
                "content": "Certainly! ....",
                // The role of the entity that sent the message
                "role": "assistant"
            }
        ],
        
        // A unique identifier for the prompt
        "prompt_id": "d938b65dfe31f05f80eb8572964c6673eddbd68eff3db6bd234d7f1e3b86c2af"
    }
    ```

### Muat Turun Data

1. Skrip Python ini digunakan untuk memuat turun dataset menggunakan skrip bantuan bernama download-dataset.py. Berikut adalah pecahan apa yang dilakukannya:

    - Ia mengimport modul os, yang menyediakan cara mudah menggunakan fungsi bergantung kepada sistem operasi.

    - Ia menggunakan fungsi os.system untuk menjalankan skrip download-dataset.py dalam shell dengan argumen baris arahan tertentu. Argumen tersebut menentukan dataset yang hendak dimuat turun (HuggingFaceH4/ultrachat_200k), direktori untuk muat turun (ultrachat_200k_dataset), dan peratusan dataset untuk pecahan (5). Fungsi os.system mengembalikan status keluar perintah yang dijalankan; status ini disimpan dalam pembolehubah exit_status.

    - Ia memeriksa jika exit_status tidak sama dengan 0. Dalam sistem operasi berasaskan Unix, status keluar 0 biasanya menunjukkan perintah berjaya, manakala nombor lain menunjukkan ralat. Jika exit_status bukan 0, ia membangkitkan Exception dengan mesej menunjukkan terdapat ralat semasa memuat turun dataset.

    - Ringkasnya, skrip ini menjalankan perintah untuk memuat turun dataset menggunakan skrip bantuan, dan membangkitkan pengecualian jika perintah gagal.

    ```python
    # Import modul os, yang menyediakan cara menggunakan fungsi bergantung pada sistem operasi
    import os
    
    # Gunakan fungsi os.system untuk menjalankan skrip download-dataset.py dalam shell dengan argumen baris perintah tertentu
    # Argumen tersebut menentukan dataset untuk dimuat turun (HuggingFaceH4/ultrachat_200k), direktori untuk memuat turunnya (ultrachat_200k_dataset), dan peratusan dataset untuk dibahagikan (5)
    # Fungsi os.system mengembalikan status keluar daripada perintah yang dilaksanakannya; status ini disimpan dalam pembolehubah exit_status
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Semak jika exit_status bukan 0
    # Dalam sistem operasi seperti Unix, status keluar 0 biasanya menunjukkan perintah berjaya, manakala nombor lain menunjukkan terdapat ralat
    # Jika exit_status bukan 0, timbulkan Exception dengan mesej yang menunjukkan terdapat ralat ketika memuat turun dataset
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### Memuatkan Data ke dalam DataFrame

1. Skrip Python ini memuatkan fail JSON Lines ke dalam DataFrame pandas dan memaparkan 5 baris pertama. Berikut adalah pecahan apa yang dilakukannya:

    - Ia mengimport perpustakaan pandas, yang merupakan perpustakaan analisis dan manipulasi data yang kuat.

    - Ia menetapkan lebar lajur maksimum untuk pilihan paparan pandas ke 0. Ini bermakna teks penuh setiap lajur akan dipaparkan tanpa dipotong apabila DataFrame dicetak.
    - Ia menggunakan fungsi pd.read_json untuk memuatkan fail train_sft.jsonl dari direktori ultrachat_200k_dataset ke dalam DataFrame. Argumen lines=True menunjukkan bahawa fail tersebut dalam format JSON Lines, di mana setiap baris adalah objek JSON yang berasingan.

    - Ia menggunakan kaedah head untuk memaparkan 5 baris pertama DataFrame. Jika DataFrame mempunyai kurang daripada 5 baris, ia akan memaparkan semua baris tersebut.

    - Secara ringkas, skrip ini memuatkan fail JSON Lines ke dalam DataFrame dan memaparkan 5 baris pertama dengan teks penuh lajur.
    
    ```python
    # Import perpustakaan pandas, yang merupakan perpustakaan manipulasi dan analisis data yang kuat
    import pandas as pd
    
    # Tetapkan lebar lajur maksimum untuk pilihan paparan pandas kepada 0
    # Ini bermakna teks penuh setiap lajur akan dipaparkan tanpa dipendekkan apabila DataFrame dicetak
    pd.set_option("display.max_colwidth", 0)
    
    # Gunakan fungsi pd.read_json untuk memuatkan fail train_sft.jsonl dari direktori ultrachat_200k_dataset ke dalam DataFrame
    # Argumen lines=True menunjukkan bahawa fail tersebut adalah dalam format JSON Lines, di mana setiap baris adalah objek JSON yang berasingan
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Gunakan kaedah head untuk memaparkan 5 baris pertama DataFrame
    # Jika DataFrame mempunyai kurang daripada 5 baris, ia akan memaparkan kesemuanya
    df.head()
    ```

## 5. Hantar kerja penyetelan halus menggunakan model dan data sebagai input

Cipta kerja yang menggunakan komponen pipeline chat-completion. Ketahui lebih lanjut mengenai semua parameter yang disokong untuk penyetelan halus.

### Definisikan parameter penyetelan halus

1. Parameter penyetelan halus boleh dikelompokkan kepada 2 kategori - parameter latihan, parameter pengoptimuman

1. Parameter latihan mentakrifkan aspek latihan seperti -

    - Optimizer, penjadual yang digunakan
    - Metik untuk mengoptimumkan penyetelan halus
    - Bilangan langkah latihan dan saiz batch dan sebagainya
    - Parameter pengoptimuman membantu dalam mengoptimumkan memori GPU dan menggunakan sumber pengiraan dengan cekap. 

1. Berikut adalah beberapa parameter yang tergolong dalam kategori ini. Parameter pengoptimuman berbeza untuk setiap model dan dibungkus bersama model untuk menangani variasi ini.

    - Aktifkan deepspeed dan LoRA
    - Aktifkan latihan ketepatan bercampur
    - Aktifkan latihan pelbagai nod

> [!NOTE]
> Penyetelan halus tersupervisi mungkin mengakibatkan kehilangan penjajaran atau pelupusan katastropik. Kami mengesyorkan memeriksa perkara ini dan menjalankan peringkat penjajaran selepas anda menyetel halus.

### Parameter Penyetelan Halus

1. Skrip Python ini sedang menyediakan parameter untuk penyetelan halus model pembelajaran mesin. Berikut adalah pecahan apa yang dilakukan:

    - Ia menyediakan parameter latihan lalai seperti bilangan epok latihan, saiz batch untuk latihan dan penilaian, kadar pembelajaran, dan jenis penjadual kadar pembelajaran.

    - Ia menyediakan parameter pengoptimuman lalai seperti sama ada untuk menggunakan Layer-wise Relevance Propagation (LoRa) dan DeepSpeed, dan peringkat DeepSpeed.

    - Ia menggabungkan parameter latihan dan pengoptimuman menjadi satu kamus yang dipanggil finetune_parameters.

    - Ia memeriksa jika foundation_model mempunyai sebarang parameter lalai khusus model. Jika ada, ia mencetak mesej amaran dan mengemas kini kamus finetune_parameters dengan parameter lalai khusus model ini. Fungsi ast.literal_eval digunakan untuk menukar parameter lalai khusus model dari rentetan ke kamus Python.

    - Ia mencetak set parameter penyetelan halus akhir yang akan digunakan untuk jalan kerja tersebut.

    - Secara ringkas, skrip ini menyediakan dan memaparkan parameter untuk penyetelan halus model pembelajaran mesin, dengan keupayaan untuk menggantikan parameter lalai dengan parameter khusus model.

    ```python
    # Tetapkan parameter latihan lalai seperti bilangan epoch latihan, saiz batch untuk latihan dan penilaian, kadar pembelajaran, dan jenis penjadual kadar pembelajaran
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Tetapkan parameter pengoptimuman lalai seperti sama ada untuk menggunakan Layer-wise Relevance Propagation (LoRa) dan DeepSpeed, serta tahap DeepSpeed
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Gabungkan parameter latihan dan pengoptimuman ke dalam satu kamus yang dipanggil finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Periksa jika foundation_model mempunyai sebarang parameter lalai khusus model
    # Jika ada, cetak mesej amaran dan kemaskini kamus finetune_parameters dengan parameter lalai khusus model tersebut
    # Fungsi ast.literal_eval digunakan untuk menukar parameter lalai khusus model daripada string ke kamus Python
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # tukar string kepada kamus Python
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Cetak set parameter penalaan akhir yang akan digunakan untuk larian tersebut
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Pipeline Latihan

1. Skrip Python ini mentakrifkan fungsi untuk menghasilkan nama paparan bagi pipeline latihan pembelajaran mesin, dan kemudian memanggil fungsi ini untuk menjana dan mencetak nama paparan. Berikut adalah pecahan apa yang dilakukan:

1. Fungsi get_pipeline_display_name ditakrifkan. Fungsi ini menjana nama paparan berdasarkan pelbagai parameter berkaitan pipeline latihan.

1. Di dalam fungsi, ia mengira jumlah saiz batch dengan mendarabkan saiz batch per peranti, bilangan langkah pengumpulan kecerunan, bilangan GPU per nod, dan bilangan nod yang digunakan untuk penyetelan halus.

1. Ia mendapatkan pelbagai parameter lain seperti jenis penjadual kadar pembelajaran, sama ada DeepSpeed digunakan, peringkat DeepSpeed, sama ada Layer-wise Relevance Propagation (LoRa) digunakan, had bilangan checkpoint model yang disimpan, dan panjang urutan maksimum.

1. Ia membina rentetan yang merangkumi semua parameter ini, dipisahkan dengan tanda sempang. Jika DeepSpeed atau LoRa digunakan, rentetan itu termasuk "ds" diikuti peringkat DeepSpeed, atau "lora", masing-masing. Jika tidak, ia termasuk "nods" atau "nolora", masing-masing.

1. Fungsi mengembalikan rentetan ini, yang berfungsi sebagai nama paparan untuk pipeline latihan.

1. Selepas fungsi ditakrif, ia dipanggil untuk menjana nama paparan yang kemudian dicetak.

1. Secara ringkas, skrip ini menjana nama paparan untuk pipeline latihan pembelajaran mesin berdasarkan pelbagai parameter, dan kemudian mencetak nama paparan ini.

    ```python
    # Takrifkan fungsi untuk menjana nama paparan untuk saluran latihan
    def get_pipeline_display_name():
        # Kira jumlah saiz kelompok dengan mendarab saiz kelompok per peranti, bilangan langkah pengumpulan kecerunan, bilangan GPU setiap nod, dan bilangan nod yang digunakan untuk penyempurnaan
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Dapatkan jenis penjadual kadar pembelajaran
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Dapatkan sama ada DeepSpeed digunakan
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Dapatkan tahap DeepSpeed
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # Jika DeepSpeed digunakan, sertakan "ds" diikuti dengan tahap DeepSpeed dalam nama paparan; jika tidak, sertakan "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Dapatkan sama ada Penyebaran Relevan Berperingkat (LoRa) digunakan
        lora = finetune_parameters.get("apply_lora", "false")
        # Jika LoRa digunakan, sertakan "lora" dalam nama paparan; jika tidak, sertakan "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Dapatkan had pada bilangan titik semak model yang perlu disimpan
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Dapatkan panjang urutan maksimum
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Bentukkan nama paparan dengan menggabungkan semua parameter ini, dipisahkan dengan tanda sempang
        return (
            model_name
            + "-"
            + "ultrachat"
            + "-"
            + f"bs{batch_size}"
            + "-"
            + f"{scheduler}"
            + "-"
            + ds_string
            + "-"
            + lora_string
            + f"-save_limit{save_limit}"
            + f"-seqlen{seq_len}"
        )
    
    # Panggil fungsi untuk menjana nama paparan
    pipeline_display_name = get_pipeline_display_name()
    # Cetak nama paparan
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Mengkonfigurasi Pipeline

Skrip Python ini mentakrif dan mengkonfigurasi pipeline pembelajaran mesin menggunakan Azure Machine Learning SDK. Berikut adalah pecahan apa yang dilakukan:

1. Ia mengimport modul yang diperlukan dari Azure AI ML SDK.

1. Ia mendapatkan komponen pipeline bernama "chat_completion_pipeline" dari daftar.

1. Ia mentakrifkan kerja pipeline menggunakan dekorator `@pipeline` dan fungsi `create_pipeline`. Nama pipeline ditetapkan kepada `pipeline_display_name`.

1. Di dalam fungsi `create_pipeline`, ia menginisialisasi komponen pipeline yang diperoleh dengan pelbagai parameter, termasuk laluan model, kluster pengkomputeran untuk peringkat berbeza, pembahagian set data untuk latihan dan ujian, bilangan GPU untuk digunakan untuk penyetelan halus, dan parameter penyetelan halus lain.

1. Ia memetakan output kerja penyetelan halus ke output kerja pipeline. Ini dilakukan supaya model yang telah disetel halus boleh didaftarkan dengan mudah, yang diperlukan untuk menggunakan model ke endpoint dalam talian atau batch.

1. Ia mencipta instance pipeline dengan memanggil fungsi `create_pipeline`.

1. Ia menetapkan tetapan `force_rerun` pipeline kepada `True`, bermakna keputusan cache dari kerja terdahulu tidak akan digunakan.

1. Ia menetapkan tetapan `continue_on_step_failure` pipeline kepada `False`, bermakna pipeline akan berhenti jika mana-mana langkah gagal.

1. Secara ringkas, skrip ini mentakrif dan mengkonfigurasi pipeline pembelajaran mesin untuk tugas chat completion menggunakan Azure Machine Learning SDK.

    ```python
    # Import modul yang diperlukan dari Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Dapatkan komponen pipeline yang dinamakan "chat_completion_pipeline" dari registri
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Takrifkan kerja pipeline menggunakan hiasan @pipeline dan fungsi create_pipeline
    # Nama pipeline ditetapkan kepada pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Inisialisasikan komponen pipeline yang diperoleh dengan pelbagai parameter
        # Ini termasuk laluan model, kluster pengkomputeran untuk pelbagai peringkat, bahagi dataset untuk latihan dan ujian, bilangan GPU yang digunakan untuk penalaan halus, dan parameter penalaan halus lain
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Peta bahagi dataset kepada parameter
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Tetapan latihan
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Ditetapkan kepada bilangan GPU yang tersedia dalam pengkomputeran
            **finetune_parameters
        )
        return {
            # Peta output kerja penalaan halus kepada output kerja pipeline
            # Ini dilakukan supaya kita boleh mendaftar model yang telah ditala halus dengan mudah
            # Pendaftaran model diperlukan untuk menerapkan model ke titik akhir dalam talian atau secara berkumpulan
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Buat satu contoh pipeline dengan memanggil fungsi create_pipeline
    pipeline_object = create_pipeline()
    
    # Jangan gunakan hasil cache dari kerja sebelumnya
    pipeline_object.settings.force_rerun = True
    
    # Tetapkan teruskan pada kegagalan langkah kepada False
    # Ini bermakna pipeline akan berhenti jika mana-mana langkah gagal
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Hantar Kerja

1. Skrip Python ini menghantar kerja pipeline pembelajaran mesin ke ruang kerja Azure Machine Learning dan kemudian menunggu kerja itu selesai. Berikut adalah pecahan apa yang dilakukan:

    - Ia memanggil kaedah create_or_update objek jobs dalam workspace_ml_client untuk menghantar kerja pipeline. Pipeline yang akan dijalankan ditentukan oleh pipeline_object, dan eksperimen di bawah mana kerja dijalankan ditentukan oleh experiment_name.

    - Ia kemudian memanggil kaedah stream objek jobs dalam workspace_ml_client untuk menunggu kerja pipeline selesai. Kerja yang ditunggu ditentukan oleh atribut nama objek pipeline_job.

    - Secara ringkas, skrip ini menghantar kerja pipeline pembelajaran mesin ke ruang kerja Azure Machine Learning, dan kemudian menunggu kerja itu selesai.

    ```python
    # Hantar tugas aliran kerja ke ruang kerja Azure Machine Learning
    # Aliran kerja yang akan dijalankan ditentukan oleh pipeline_object
    # Eksperimen di bawah mana tugas dijalankan ditentukan oleh experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Tunggu tugas aliran kerja selesai
    # Tugas untuk ditunggu ditentukan oleh atribut nama objek pipeline_job
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. Daftarkan model yang disetel halus dengan ruang kerja

Kita akan mendaftarkan model dari output kerja penyetelan halus. Ini akan mengesan keturunan antara model yang disetel halus dan kerja penyetelan halus. Kerja penyetelan halus, seterusnya, mengesan keturunan kepada model asas, data dan kod latihan.

### Mendaftar Model ML

1. Skrip Python ini mendaftarkan model pembelajaran mesin yang telah dilatih dalam pipeline Azure Machine Learning. Berikut adalah pecahan apa yang dilakukan:

    - Ia mengimport modul yang diperlukan dari Azure AI ML SDK.

    - Ia memeriksa jika output trained_model tersedia dari kerja pipeline dengan memanggil kaedah get objek jobs dalam workspace_ml_client dan mengakses atribut outputs.

    - Ia membina laluan ke model yang telah dilatih dengan memformat rentetan dengan nama kerja pipeline dan nama output ("trained_model").

    - Ia mentakrifkan nama untuk model yang disetel halus dengan menambah "-ultrachat-200k" kepada nama model asal dan menggantikan sebarang garis miring dengan tanda sempang.

    - Ia bersedia untuk mendaftarkan model dengan membuat objek Model dengan pelbagai parameter, termasuk laluan ke model, jenis model (model MLflow), nama dan versi model, dan penerangan mengenai model.

    - Ia mendaftarkan model dengan memanggil kaedah create_or_update objek models dalam workspace_ml_client dengan objek Model sebagai argumen.

    - Ia mencetak model yang didaftarkan.

1. Secara ringkas, skrip ini mendaftarkan model pembelajaran mesin yang telah dilatih dalam pipeline Azure Machine Learning.
    
    ```python
    # Import modul yang diperlukan dari Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Semak jika output `trained_model` tersedia dari pekerjaan pipeline
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Bina laluan ke model terlatih dengan memformat string menggunakan nama pekerjaan pipeline dan nama output ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Tetapkan nama untuk model yang disesuaikan dengan menambah "-ultrachat-200k" kepada nama model asal dan menggantikan mana-mana garis miring dengan tanda sempang
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Bersedia untuk mendaftar model dengan membuat objek Model dengan pelbagai parameter
    # Ini termasuk laluan ke model, jenis model (model MLflow), nama dan versi model, dan penerangan model
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Gunakan cap masa sebagai versi untuk mengelakkan konflik versi
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Daftarkan model dengan memanggil kaedah create_or_update objek models dalam workspace_ml_client dengan objek Model sebagai argumen
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Cetak model yang telah didaftarkan
    print("registered model: \n", registered_model)
    ```

## 7. Gunakan model yang disetel halus ke endpoint dalam talian

Endpoint dalam talian menyediakan API REST yang tahan lama yang boleh digunakan untuk integrasi dengan aplikasi yang perlu menggunakan model itu.

### Urus Endpoint

1. Skrip Python ini mencipta endpoint dalam talian terurus dalam Azure Machine Learning untuk model yang didaftarkan. Berikut adalah pecahan apa yang dilakukan:

    - Ia mengimport modul yang diperlukan dari Azure AI ML SDK.

    - Ia mentakrifkan nama unik untuk endpoint dalam talian dengan menambah cap masa kepada rentetan "ultrachat-completion-".

    - Ia bersedia untuk mencipta endpoint dalam talian dengan membuat objek ManagedOnlineEndpoint dengan pelbagai parameter, termasuk nama endpoint, penerangan endpoint, dan mod pengesahan ("key").

    - Ia mencipta endpoint dalam talian dengan memanggil kaedah begin_create_or_update workspace_ml_client dengan objek ManagedOnlineEndpoint sebagai argumen. Kemudian ia menunggu operasi penciptaan selesai dengan memanggil kaedah wait.

1. Secara ringkas, skrip ini mencipta endpoint dalam talian terurus dalam Azure Machine Learning untuk model yang didaftarkan.

    ```python
    # Import modul yang diperlukan dari SDK Azure AI ML
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Tetapkan nama unik untuk titik akhir dalam talian dengan menambah cap masa ke string "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Bersedia untuk mencipta titik akhir dalam talian dengan membuat objek ManagedOnlineEndpoint dengan pelbagai parameter
    # Ini termasuk nama titik akhir, penerangan tentang titik akhir, dan mod pengesahan ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Cipta titik akhir dalam talian dengan memanggil kaedah begin_create_or_update pada workspace_ml_client dengan objek ManagedOnlineEndpoint sebagai argumen
    # Kemudian tunggu operasi penciptaan selesai dengan memanggil kaedah wait
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> Anda boleh dapati senarai SKU yang disokong untuk pengeluaran di sini - [Senarai SKU endpoint dalam talian terurus](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Menggunakan Model ML

1. Skrip Python ini menggunakan model pembelajaran mesin yang didaftarkan ke endpoint dalam talian terurus di Azure Machine Learning. Berikut adalah pecahan apa yang dilakukan:

    - Ia mengimport modul ast, yang menyediakan fungsi untuk memproses pokok tatabahasa abstrak Python.

    - Ia menetapkan jenis instans untuk penggunaan kepada "Standard_NC6s_v3".

    - Ia memeriksa jika tag inference_compute_allow_list terdapat dalam model asas. Jika ada, ia menukar nilai tag dari rentetan ke senarai Python dan menetapkannya kepada inference_computes_allow_list. Jika tiada, ia menetapkan inference_computes_allow_list kepada None.

    - Ia memeriksa jika jenis instans yang ditetapkan terdapat dalam senarai dibenarkan. Jika tidak, ia mencetak mesej yang meminta pengguna memilih jenis instans dari senarai dibenarkan.

    - Ia bersedia untuk mencipta penggunaan dengan membuat objek ManagedOnlineDeployment dengan pelbagai parameter, termasuk nama penggunaan, nama endpoint, ID model, jenis dan bilangan instans, tetapan pemeriksaan kesihatan (liveness probe), dan tetapan permintaan.

    - Ia mencipta penggunaan dengan memanggil kaedah begin_create_or_update workspace_ml_client dengan objek ManagedOnlineDeployment sebagai argumen. Kemudian ia menunggu operasi penciptaan selesai dengan memanggil kaedah wait.

    - Ia menetapkan trafik endpoint untuk mengarahkan 100% trafik ke penggunaan "demo".

    - Ia mengemaskini endpoint dengan memanggil kaedah begin_create_or_update workspace_ml_client dengan objek endpoint sebagai argumen. Kemudian ia menunggu operasi kemaskini selesai dengan memanggil kaedah result.

1. Secara ringkas, skrip ini menggunakan model pembelajaran mesin yang didaftarkan ke endpoint dalam talian terurus di Azure Machine Learning.

    ```python
    # Import modul ast, yang menyediakan fungsi untuk memproses pokok tatabahasa sintaks abstrak Python
    import ast
    
    # Tetapkan jenis instans untuk pengedaran
    instance_type = "Standard_NC6s_v3"
    
    # Periksa jika tag `inference_compute_allow_list` hadir dalam model asas
    if "inference_compute_allow_list" in foundation_model.tags:
        # Jika ya, tukar nilai tag dari string kepada senarai Python dan tetapkan kepada `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Jika tidak, tetapkan `inference_computes_allow_list` kepada `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Periksa jika jenis instans yang ditetapkan ada dalam senarai yang dibenarkan
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Bersiap sedia untuk membuat pengedaran dengan mencipta objek `ManagedOnlineDeployment` dengan pelbagai parameter
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Buat pengedaran dengan memanggil kaedah `begin_create_or_update` daripada `workspace_ml_client` dengan objek `ManagedOnlineDeployment` sebagai argumen
    # Kemudian tunggu operasi penciptaan selesai dengan memanggil kaedah `wait`
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Tetapkan trafik titik akhir untuk mengarahkan 100% trafik ke pengedaran "demo"
    endpoint.traffic = {"demo": 100}
    
    # Kemas kini titik akhir dengan memanggil kaedah `begin_create_or_update` daripada `workspace_ml_client` dengan objek `endpoint` sebagai argumen
    # Kemudian tunggu operasi kemas kini selesai dengan memanggil kaedah `result`
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. Uji endpoint dengan data contoh

Kita akan mengambil beberapa data contoh dari set data ujian dan menghantar ke endpoint dalam talian untuk inferens. Kita kemudian akan memaparkan label yang dinilai bersama dengan label kebenaran sebenar

### Membaca keputusan

1. Skrip Python ini membaca fail JSON Lines ke dalam DataFrame pandas, mengambil sampel rawak, dan menetapkan semula indeks. Berikut adalah pecahan apa yang dilakukan:

    - Ia membaca fail ./ultrachat_200k_dataset/test_gen.jsonl ke dalam DataFrame pandas. Fungsi read_json digunakan dengan argumen lines=True kerana fail tersebut dalam format JSON Lines, di mana setiap baris adalah objek JSON yang berasingan.

    - Ia mengambil sampel rawak 1 baris dari DataFrame. Fungsi sample digunakan dengan argumen n=1 untuk menentukan bilangan baris rawak yang dipilih.

    - Ia menetapkan semula indeks DataFrame. Fungsi reset_index digunakan dengan argumen drop=True untuk membuang indeks asal dan menggantikannya dengan indeks baru yang bernilai bulat lalai.

    - Ia memaparkan 2 baris pertama DataFrame menggunakan fungsi head dengan argumen 2. Namun, kerana DataFrame hanya mengandungi satu baris selepas pengambilan sampel, ini hanya akan memaparkan satu baris itu sahaja.

1. Secara ringkas, skrip ini membaca fail JSON Lines ke dalam DataFrame pandas, mengambil sampel rawak 1 baris, menetapkan semula indeks, dan memaparkan baris pertama.
    
    ```python
    # Import perpustakaan pandas
    import pandas as pd
    
    # Baca fail JSON Lines './ultrachat_200k_dataset/test_gen.jsonl' ke dalam DataFrame pandas
    # Argumen 'lines=True' menunjukkan bahawa fail ini dalam format JSON Lines, di mana setiap baris adalah objek JSON yang berasingan
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Ambil sampel rawak sebanyak 1 baris dari DataFrame
    # Argumen 'n=1' menentukan bilangan baris rawak yang akan dipilih
    test_df = test_df.sample(n=1)
    
    # Tetapkan semula indeks DataFrame
    # Argumen 'drop=True' menunjukkan bahawa indeks asal harus dibuang dan digantikan dengan indeks baru berangka lalai
    # Argumen 'inplace=True' menunjukkan bahawa DataFrame harus diubah di tempat (tanpa membuat objek baru)
    test_df.reset_index(drop=True, inplace=True)
    
    # Paparkan 2 baris pertama DataFrame
    # Walau bagaimanapun, kerana DataFrame hanya mengandungi satu baris selepas pensampelan, ini hanya akan memaparkan satu baris tersebut
    test_df.head(2)
    ```

### Cipta Objek JSON

1. Skrip Python ini mencipta objek JSON dengan parameter tertentu dan menyimpannya ke dalam fail. Berikut adalah pecahan apa yang dilakukan:

    - Ia mengimport modul json, yang menyediakan fungsi untuk bekerja dengan data JSON.
    - Ia mencipta kamus parameters dengan kunci dan nilai yang mewakili parameter untuk model pembelajaran mesin. Kunci tersebut ialah "temperature", "top_p", "do_sample", dan "max_new_tokens", dan nilai yang sepadan adalah 0.6, 0.9, True, dan 200 masing-masing.

    - Ia mencipta satu lagi kamus test_json dengan dua kunci: "input_data" dan "params". Nilai "input_data" adalah satu lagi kamus dengan kunci "input_string" dan "parameters". Nilai "input_string" adalah satu senarai yang mengandungi mesej pertama dari DataFrame test_df. Nilai "parameters" adalah kamus parameters yang dicipta tadi. Nilai "params" adalah kamus kosong.

    - Ia membuka satu fail bernama sample_score.json
    
    ```python
    # Import modul json, yang menyediakan fungsi untuk bekerja dengan data JSON
    import json
    
    # Buat sebuah kamus `parameters` dengan kunci dan nilai yang mewakili parameter untuk model pembelajaran mesin
    # Kunci-kuncinya adalah "temperature", "top_p", "do_sample", dan "max_new_tokens", dan nilai sepadan mereka adalah 0.6, 0.9, True, dan 200 masing-masing
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Buat satu lagi kamus `test_json` dengan dua kunci: "input_data" dan "params"
    # Nilai bagi "input_data" adalah satu kamus lain dengan kunci "input_string" dan "parameters"
    # Nilai bagi "input_string" adalah senarai yang mengandungi mesej pertama dari DataFrame `test_df`
    # Nilai bagi "parameters" adalah kamus `parameters` yang dicipta sebelum ini
    # Nilai bagi "params" adalah kamus kosong
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Buka fail bernama `sample_score.json` dalam direktori `./ultrachat_200k_dataset` dalam mod tulis
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Tulis kamus `test_json` ke dalam fail dalam format JSON menggunakan fungsi `json.dump`
        json.dump(test_json, f)
    ```

### Memanggil Endpoint

1. Skrip Python ini memanggil satu endpoint dalam talian di Azure Machine Learning untuk menilai fail JSON. Berikut adalah penerangan tentang apa yang ia lakukan:

    - Ia memanggil kaedah invoke dari sifat online_endpoints objek workspace_ml_client. Kaedah ini digunakan untuk menghantar permintaan ke endpoint dalam talian dan mendapat respons.

    - Ia menentukan nama endpoint dan penyebaran dengan argumen endpoint_name dan deployment_name. Dalam kes ini, nama endpoint disimpan dalam pembolehubah online_endpoint_name dan nama penyebaran ialah "demo".

    - Ia menentukan laluan ke fail JSON untuk dinilai dengan argumen request_file. Dalam kes ini, failnya ialah ./ultrachat_200k_dataset/sample_score.json.

    - Ia menyimpan respons dari endpoint dalam pembolehubah response.

    - Ia mencetak respons mentah.

1. Secara ringkas, skrip ini memanggil satu endpoint dalam talian di Azure Machine Learning untuk menilai fail JSON dan mencetak respons tersebut.

    ```python
    # Panggil titik akhir dalam talian di Azure Machine Learning untuk menilai fail `sample_score.json`
    # Kaedah `invoke` bagi sifat `online_endpoints` objek `workspace_ml_client` digunakan untuk menghantar permintaan ke titik akhir dalam talian dan mendapatkan respons
    # Argumen `endpoint_name` menentukan nama titik akhir, yang disimpan dalam pembolehubah `online_endpoint_name`
    # Argumen `deployment_name` menentukan nama penempatan, iaitu "demo"
    # Argumen `request_file` menentukan laluan ke fail JSON yang akan dinilai, iaitu `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Cetak respons mentah dari titik akhir
    print("raw response: \n", response, "\n")
    ```

## 9. Padam endpoint dalam talian

1. Jangan lupa untuk memadam endpoint dalam talian, jika tidak anda akan membiarkan meter bil berjalan untuk pengkomputeran yang digunakan oleh endpoint tersebut. Baris kod Python ini memadamkan satu endpoint dalam talian di Azure Machine Learning. Berikut adalah penjelasan tentang apa yang ia lakukan:

    - Ia memanggil kaedah begin_delete dari sifat online_endpoints objek workspace_ml_client. Kaedah ini digunakan untuk memulakan proses memadam satu endpoint dalam talian.

    - Ia menentukan nama endpoint yang hendak dipadam dengan argumen name. Dalam kes ini, nama endpoint disimpan dalam pembolehubah online_endpoint_name.

    - Ia memanggil kaedah wait untuk menunggu operasi pemadaman selesai. Ini adalah operasi penghalang, yang bermaksud ia akan menghalang skrip daripada meneruskan sehingga pemadaman selesai.

    - Secara ringkas, baris kod ini memulakan proses memadam satu endpoint dalam talian di Azure Machine Learning dan menunggu operasi itu selesai.

    ```python
    # Padamkan titik akhir dalam talian di Azure Machine Learning
    # Kaedah `begin_delete` dari sifat `online_endpoints` objek `workspace_ml_client` digunakan untuk memulakan pemadaman titik akhir dalam talian
    # Argumen `name` menetapkan nama titik akhir yang akan dipadam, yang disimpan dalam pembolehubah `online_endpoint_name`
    # Kaedah `wait` dipanggil untuk menunggu operasi pemadaman selesai. Ini adalah operasi yang menghalang, bermakna ia akan menghalang skrip daripada diteruskan sehingga pemadaman selesai
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->