# Melatih dan Mengintegrasi model Phi-3 khusus dengan Prompt flow dalam Microsoft Foundry

Contoh hujung ke hujung (E2E) ini berdasarkan panduan "[Melatih dan Mengintegrasi Model Phi-3 Khusus dengan Prompt Flow dalam Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" dari Komuniti Teknikal Microsoft. Ia memperkenalkan proses melatih, melaksanakan, dan mengintegrasi model Phi-3 khusus dengan Prompt flow dalam Microsoft Foundry.
Berbeza dengan contoh E2E, "[Melatih dan Mengintegrasi Model Phi-3 Khusus dengan Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", yang melibatkan menjalankan kod secara tempatan, tutorial ini memberi tumpuan sepenuhnya kepada melatih dan mengintegrasi model anda dalam Azure AI / ML Studio.

## Gambaran Keseluruhan

Dalam contoh E2E ini, anda akan belajar bagaimana untuk melatih model Phi-3 dan mengintegrasikannya dengan Prompt flow dalam Microsoft Foundry. Dengan menggunakan Azure AI / ML Studio, anda akan membina aliran kerja untuk melaksanakan dan menggunakan model AI khusus. Contoh E2E ini dibahagikan kepada tiga senario:

**Senario 1: Menyediakan sumber Azure dan Bersedia untuk melatih**

**Senario 2: Melatih model Phi-3 dan Melaksanakan dalam Azure Machine Learning Studio**

**Senario 3: Mengintegrasi dengan Prompt flow dan Berbual dengan model khusus anda dalam Microsoft Foundry**

Berikut adalah gambaran keseluruhan contoh E2E ini.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/ms/00-01-architecture.198ba0f1ae6d841a.webp)

### Jadual Kandungan

1. **[Senario 1: Menyediakan sumber Azure dan Bersedia untuk melatih](#senario-1-menyediakan-sumber-azure-dan-bersedia-untuk-melatih)**
    - [Mewujudkan Workspace Azure Machine Learning](#mewujudkan-workspace-azure-machine-learning)
    - [Meminta kuota GPU dalam Langganan Azure](#meminta-kuota-gpu-dalam-langganan-azure)
    - [Tambah penugasan peranan](#tambah-penugasan-peranan)
    - [Menyediakan projek](#menyediakan-projek)
    - [Menyediakan set data untuk melatih](#sediakan-dataset-untuk-penalaan-halus)

1. **[Senario 2: Melatih model Phi-3 dan Melaksanakan dalam Azure Machine Learning Studio](#senario-2-menala-halus-model-phi-3-dan-terbitkan-dalam-azure-machine-learning-studio)**
    - [Melatih model Phi-3](#menala-halus-model-phi-3)
    - [Melaksanakan model Phi-3 yang dilatih](#terbitkan-model-phi-3-yang-telah-ditala-halus)

1. **[Senario 3: Mengintegrasi dengan Prompt flow dan Berbual dengan model khusus anda dalam Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Mengintegrasi model Phi-3 khusus dengan Prompt flow](#integrasikan-model-phi-3-khusus-dengan-prompt-flow)
    - [Berbual dengan model Phi-3 khusus anda](#bersembang-dengan-model-phi-3-tersuai-anda)

## Senario 1: Menyediakan sumber Azure dan Bersedia untuk melatih

### Mewujudkan Workspace Azure Machine Learning

1. Taip *azure machine learning* di **bar carian** di bahagian atas halaman portal dan pilih **Azure Machine Learning** daripada pilihan yang muncul.

    ![Taip azure machine learning.](../../../../../../translated_images/ms/01-01-type-azml.acae6c5455e67b4b.webp)

2. Pilih **+ Create** dari menu navigasi.

3. Pilih **New workspace** dari menu navigasi.

    ![Pilih workspace baru.](../../../../../../translated_images/ms/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Lakukan tugasan berikut:

    - Pilih **Langganan** Azure anda.
    - Pilih **Kumpulan sumber** yang hendak digunakan (cipta yang baru jika perlu).
    - Masukkan **Nama Workspace**. Ia mesti nilai yang unik.
    - Pilih **Wilayah** yang anda ingin gunakan.
    - Pilih **Akaun storan** yang hendak digunakan (cipta yang baru jika perlu).
    - Pilih **Petik kunci** yang hendak digunakan (cipta yang baru jika perlu).
    - Pilih **Insights aplikasi** yang hendak digunakan (cipta yang baru jika perlu).
    - Pilih **Pendaftaran kontena** yang hendak digunakan (cipta yang baru jika perlu).

    ![Isi maklumat azure machine learning.](../../../../../../translated_images/ms/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Pilih **Semak + Cipta**.

6. Pilih **Cipta**.

### Meminta kuota GPU dalam Langganan Azure

Dalam tutorial ini, anda akan belajar bagaimana untuk melatih dan melaksanakan model Phi-3, menggunakan GPU. Untuk melatih, anda akan menggunakan GPU *Standard_NC24ads_A100_v4*, yang memerlukan permintaan kuota. Untuk pelaksanaan, anda akan menggunakan GPU *Standard_NC6s_v3*, yang juga memerlukan permintaan kuota.

> [!NOTE]
>
> Hanya langganan Bayar-Setiap-Penggunaan (jenis langganan standard) yang layak untuk peruntukan GPU; langganan manfaat tidak disokong buat masa ini.
>

1. Layari [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Lakukan tugasan berikut untuk memohon kuota *Standard NCADSA100v4 Family*:

    - Pilih **Kuota** dari tab sebelah kiri.
    - Pilih **Keluarga mesin maya** yang hendak digunakan. Contohnya, pilih **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, yang termasuk GPU *Standard_NC24ads_A100_v4*.
    - Pilih **Meminta kuota** dari menu navigasi.

        ![Meminta kuota.](../../../../../../translated_images/ms/02-02-request-quota.c0428239a63ffdd5.webp)

    - Dalam halaman Meminta kuota, masukkan **Had teras baru** yang ingin digunakan. Contohnya, 24.
    - Dalam halaman Meminta kuota, pilih **Hantar** untuk memohon kuota GPU.

1. Lakukan tugasan berikut untuk memohon kuota *Standard NCSv3 Family*:

    - Pilih **Kuota** dari tab sebelah kiri.
    - Pilih **Keluarga mesin maya** yang hendak digunakan. Contohnya, pilih **Standard NCSv3 Family Cluster Dedicated vCPUs**, yang termasuk GPU *Standard_NC6s_v3*.
    - Pilih **Meminta kuota** dari menu navigasi.
    - Dalam halaman Meminta kuota, masukkan **Had teras baru** yang ingin digunakan. Contohnya, 24.
    - Dalam halaman Meminta kuota, pilih **Hantar** untuk memohon kuota GPU.

### Tambah penugasan peranan

Untuk melatih dan melaksanakan model anda, anda mesti terlebih dahulu membuat Identiti Terkelola Tugasan Pengguna (UAI) dan menetapkan kebenaran yang sesuai. UAI ini akan digunakan untuk pengesahan semasa pelaksanaan.

#### Mewujudkan Identiti Terkelola Tugasan Pengguna (UAI)

1. Taip *managed identities* di **bar carian** di bahagian atas halaman portal dan pilih **Managed Identities** daripada pilihan yang muncul.

    ![Taip managed identities.](../../../../../../translated_images/ms/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Pilih **+ Create**.

    ![Pilih cipta.](../../../../../../translated_images/ms/03-02-select-create.92bf8989a5cd98f2.webp)

1. Lakukan tugasan berikut:

    - Pilih **Langganan** Azure anda.
    - Pilih **Kumpulan sumber** yang hendak digunakan (cipta yang baru jika perlu).
    - Pilih **Wilayah** yang anda ingin gunakan.
    - Masukkan **Nama**. Ia mesti nilai yang unik.

    ![Pilih cipta.](../../../../../../translated_images/ms/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Pilih **Semak + cipta**.

1. Pilih **+ Cipta**.

#### Tambah penugasan peranan Contributor ke Identiti Terkelola

1. Navigasi ke sumber Identiti Terkelola yang anda cipta.

1. Pilih **Penugasan peranan Azure** dari tab sebelah kiri.

1. Pilih **+Tambah penugasan peranan** dari menu navigasi.

1. Dalam halaman Tambah penugasan peranan, lakukan tugasan berikut:
    - Pilih **Skop** ke **Kumpulan sumber**.
    - Pilih **Langganan** Azure anda.
    - Pilih **Kumpulan sumber** yang hendak digunakan.
    - Pilih **Peranan** ke **Contributor**.

    ![Isi peranan contributor.](../../../../../../translated_images/ms/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Pilih **Simpan**.

#### Tambah penugasan peranan Pembaca Data Blob Storan ke Identiti Terkelola

1. Taip *storage accounts* di **bar carian** di bahagian atas halaman portal dan pilih **Storage accounts** daripada pilihan yang muncul.

    ![Taip storage accounts.](../../../../../../translated_images/ms/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Pilih akaun storan yang berkaitan dengan workspace Azure Machine Learning yang anda cipta. Contohnya, *finetunephistorage*.

1. Lakukan tugasan berikut untuk navigasi ke halaman Tambah penugasan peranan:

    - Navigasi ke akaun Storan Azure yang anda cipta.
    - Pilih **Kawalan Akses (IAM)** dari tab sebelah kiri.
    - Pilih **+ Tambah** dari menu navigasi.
    - Pilih **Tambah penugasan peranan** dari menu navigasi.

    ![Tambah peranan.](../../../../../../translated_images/ms/03-06-add-role.353ccbfdcf0789c2.webp)

1. Dalam halaman Tambah penugasan peranan, lakukan tugasan berikut:

    - Dalam halaman Peranan, taip *Storage Blob Data Reader* di **bar carian** dan pilih **Storage Blob Data Reader** daripada pilihan yang muncul.
    - Dalam halaman Peranan, pilih **Seterusnya**.
    - Dalam halaman Ahli, pilih **Tugaskan akses kepada** **Identiti terkelola**.
    - Dalam halaman Ahli, pilih **+ Pilih ahli**.
    - Dalam halaman Pilih identiti terkelola, pilih **Langganan** Azure anda.
    - Dalam halaman Pilih identiti terkelola, pilih **Identiti terkelola** ke **Manage Identity**.
    - Dalam halaman Pilih identiti terkelola, pilih Identiti Terkelola yang anda cipta. Contohnya, *finetunephi-managedidentity*.
    - Dalam halaman Pilih identiti terkelola, pilih **Pilih**.

    ![Pilih identiti terkelola.](../../../../../../translated_images/ms/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Pilih **Semak + tugaskan**.

#### Tambah penugasan peranan AcrPull ke Identiti Terkelola

1. Taip *container registries* di **bar carian** di bahagian atas halaman portal dan pilih **Container registries** daripada pilihan yang muncul.

    ![Taip container registries.](../../../../../../translated_images/ms/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Pilih pendaftaran kontena yang berkaitan dengan workspace Azure Machine Learning. Contohnya, *finetunephicontainerregistry*

1. Lakukan tugasan berikut untuk navigasi ke halaman Tambah penugasan peranan:

    - Pilih **Kawalan Akses (IAM)** dari tab sebelah kiri.
    - Pilih **+ Tambah** dari menu navigasi.
    - Pilih **Tambah penugasan peranan** dari menu navigasi.

1. Dalam halaman Tambah penugasan peranan, lakukan tugasan berikut:

    - Dalam halaman Peranan, taip *AcrPull* di **bar carian** dan pilih **AcrPull** daripada pilihan yang muncul.
    - Dalam halaman Peranan, pilih **Seterusnya**.
    - Dalam halaman Ahli, pilih **Tugaskan akses kepada** **Identiti terkelola**.
    - Dalam halaman Ahli, pilih **+ Pilih ahli**.
    - Dalam halaman Pilih identiti terkelola, pilih **Langganan** Azure anda.
    - Dalam halaman Pilih identiti terkelola, pilih **Identiti terkelola** ke **Manage Identity**.
    - Dalam halaman Pilih identiti terkelola, pilih Identiti Terkelola yang anda cipta. Contohnya, *finetunephi-managedidentity*.
    - Dalam halaman Pilih identiti terkelola, pilih **Pilih**.
    - Pilih **Semak + tugaskan**.

### Menyediakan projek

Untuk memuat turun set data yang diperlukan untuk melatih, anda akan menyediakan persekitaran tempatan.

Dalam latihan ini, anda akan

- Mewujudkan folder untuk bekerja di dalamnya.
- Mewujudkan persekitaran maya.
- Memasang pakej yang diperlukan.
- Mewujudkan fail *download_dataset.py* untuk memuat turun set data.

#### Mewujudkan folder untuk bekerja di dalamnya

1. Buka tetingkap terminal dan taip arahan berikut untuk mewujudkan folder bernama *finetune-phi* di laluan lalai.

    ```console
    mkdir finetune-phi
    ```

2. Taip arahan berikut dalam terminal anda untuk navigasi ke folder *finetune-phi* yang anda cipta.

    ```console
    cd finetune-phi
    ```

#### Mewujudkan persekitaran maya

1. Taip arahan berikut dalam terminal anda untuk mewujudkan persekitaran maya bernama *.venv*.
    ```console
    python -m venv .venv
    ```

2. Taipkan arahan berikut dalam terminal anda untuk mengaktifkan persekitaran maya.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Jika berjaya, anda harus melihat *(.venv)* sebelum prompt arahan.

#### Pasang pakej yang diperlukan

1. Taipkan arahan berikut dalam terminal anda untuk memasang pakej yang diperlukan.

    ```console
    pip install datasets==2.19.1
    ```

#### Buat `donload_dataset.py`

> [!NOTE]
> Struktur folder lengkap:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Buka **Visual Studio Code**.

1. Pilih **File** dari bar menu.

1. Pilih **Open Folder**.

1. Pilih folder *finetune-phi* yang anda buat, yang terletak di *C:\Users\yourUserName\finetune-phi*.

    ![Select the folder that you created.](../../../../../../translated_images/ms/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. Dalam panel kiri Visual Studio Code, klik kanan dan pilih **New File** untuk membuat fail baru bernama *download_dataset.py*.

    ![Create a new file.](../../../../../../translated_images/ms/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Sediakan dataset untuk penalaan halus

Dalam latihan ini, anda akan menjalankan fail *download_dataset.py* untuk memuat turun dataset *ultrachat_200k* ke persekitaran tempatan anda. Kemudian anda akan menggunakan dataset ini untuk menala halus model Phi-3 dalam Azure Machine Learning.

Dalam latihan ini, anda akan:

- Tambah kod ke fail *download_dataset.py* untuk memuat turun dataset.
- Jalankan fail *download_dataset.py* untuk memuat turun dataset ke persekitaran tempatan anda.

#### Muat turun dataset anda menggunakan *download_dataset.py*

1. Buka fail *download_dataset.py* dalam Visual Studio Code.

1. Tambah kod berikut ke dalam fail *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Muatkan set data dengan nama, konfigurasi, dan nisbah pecahan yang ditetapkan
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Bahagikan set data kepada set latih dan uji (80% latih, 20% uji)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Cipta direktori jika ia tidak wujud
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Buka fail dalam mod tulis
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterasi setiap rekod dalam set data
            for record in dataset:
                # Tuangkan rekod sebagai objek JSON dan tulis ke fail
                json.dump(record, f)
                # Tulis aksara baris baru untuk memisahkan rekod
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Muat dan pecahkan set data ULTRACHAT_200k dengan konfigurasi dan nisbah pecahan tertentu
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Ekstrak set data latih dan uji daripada pecahan
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Simpan set data latih ke fail JSONL
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Simpan set data uji ke fail JSONL berasingan
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Taipkan arahan berikut dalam terminal anda untuk menjalankan skrip dan memuat turun dataset ke persekitaran tempatan anda.

    ```console
    python download_dataset.py
    ```

1. Sahkan bahawa dataset berjaya disimpan di direktori *finetune-phi/data* tempatan anda.

> [!NOTE]
>
> #### Nota mengenai saiz dataset dan masa penalaan halus
>
> Dalam tutorial ini, anda hanya menggunakan 1% daripada dataset (`split='train[:1%]'`). Ini secara signifikan mengurangkan jumlah data, mempercepatkan proses muat naik dan penalaan halus. Anda boleh laraskan peratusan untuk mencari keseimbangan antara masa latihan dan prestasi model. Menggunakan subset dataset yang lebih kecil mengurangkan masa yang diperlukan untuk penalaan halus, menjadikan proses lebih mudah diurus untuk tutorial.

## Senario 2: Menala halus model Phi-3 dan Terbitkan dalam Azure Machine Learning Studio

### Menala halus model Phi-3

Dalam latihan ini, anda akan menala halus model Phi-3 dalam Azure Machine Learning Studio.

Dalam latihan ini, anda akan:

- Membuat kluster komputer untuk penalaan halus.
- Menala halus model Phi-3 dalam Azure Machine Learning Studio.

#### Buat kluster komputer untuk penalaan halus

1. Lawati [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pilih **Compute** dari tab sebelah kiri.

1. Pilih **Compute clusters** dari menu navigasi.

1. Pilih **+ New**.

    ![Select compute.](../../../../../../translated_images/ms/06-01-select-compute.a29cff290b480252.webp)

1. Lakukan tugasan berikut:

    - Pilih **Region** yang anda ingin gunakan.
    - Pilih **Virtual machine tier** kepada **Dedicated**.
    - Pilih **Virtual machine type** kepada **GPU**.
    - Pilih penapis **Virtual machine size** kepada **Select from all options**.
    - Pilih **Virtual machine size** kepada **Standard_NC24ads_A100_v4**.

    ![Create cluster.](../../../../../../translated_images/ms/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Pilih **Next**.

1. Lakukan tugasan berikut:

    - Masukkan **Compute name**. Ia mesti nilai unik.
    - Pilih **Minimum number of nodes** kepada **0**.
    - Pilih **Maximum number of nodes** kepada **1**.
    - Pilih **Idle seconds before scale down** kepada **120**.

    ![Create cluster.](../../../../../../translated_images/ms/06-03-create-cluster.4a54ba20914f3662.webp)

1. Pilih **Create**.

#### Menala halus model Phi-3

1. Lawati [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pilih ruang kerja Azure Machine Learning yang anda buat.

    ![Select workspace that you created.](../../../../../../translated_images/ms/06-04-select-workspace.a92934ac04f4f181.webp)

1. Lakukan tugasan berikut:

    - Pilih **Model catalog** dari tab sebelah kiri.
    - Taip *phi-3-mini-4k* dalam **bar carian** dan pilih **Phi-3-mini-4k-instruct** dari pilihan yang muncul.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/ms/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Pilih **Fine-tune** dari menu navigasi.

    ![Select fine tune.](../../../../../../translated_images/ms/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Lakukan tugasan berikut:

    - Pilih **Select task type** kepada **Chat completion**.
    - Pilih **+ Select data** untuk memuat naik **Data Latihan**.
    - Pilih jenis muat naik Data Validasi kepada **Provide different validation data**.
    - Pilih **+ Select data** untuk memuat naik **Data Validasi**.

    ![Fill fine-tuning page.](../../../../../../translated_images/ms/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Anda boleh pilih **Advanced settings** untuk menyesuaikan konfigurasi seperti **learning_rate** dan **lr_scheduler_type** untuk mengoptimumkan proses penalaan halus mengikut keperluan khusus anda.

1. Pilih **Finish**.

1. Dalam latihan ini, anda berjaya menala halus model Phi-3 menggunakan Azure Machine Learning. Harap maklum bahawa proses penalaan halus boleh mengambil masa yang ketara. Selepas menjalankan tugas penalaan halus, anda perlu menunggu sehingga selesai. Anda boleh memantau status tugas penalaan halus dengan pergi ke tab Jobs di sebelah kiri ruang kerja Azure Machine Learning anda. Dalam siri seterusnya, anda akan menerbitkan model yang sudah ditala halus dan mengintegrasikannya dengan Prompt flow.

    ![See finetuning job.](../../../../../../translated_images/ms/06-08-output.2bd32e59930672b1.webp)

### Terbitkan model Phi-3 yang telah ditala halus

Untuk mengintegrasikan model Phi-3 yang telah ditala halus dengan Prompt flow, anda perlu menerbitkan model tersebut supaya ia boleh diakses untuk inferens masa nyata. Proses ini melibatkan pendaftaran model, membuat titik akhir dalam talian, dan menerbitkan model.

Dalam latihan ini, anda akan:

- Mendaftar model yang telah ditala halus di ruang kerja Azure Machine Learning.
- Membuat titik akhir dalam talian.
- Menerbitkan model Phi-3 yang telah didaftarkan dan ditala halus.

#### Daftar model yang ditala halus

1. Lawati [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pilih ruang kerja Azure Machine Learning yang anda buat.

    ![Select workspace that you created.](../../../../../../translated_images/ms/06-04-select-workspace.a92934ac04f4f181.webp)

1. Pilih **Models** dari tab sebelah kiri.
1. Pilih **+ Register**.
1. Pilih **From a job output**.

    ![Register model.](../../../../../../translated_images/ms/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Pilih tugas yang anda cipta.

    ![Select job.](../../../../../../translated_images/ms/07-02-select-job.3e2e1144cd6cd093.webp)

1. Pilih **Next**.

1. Pilih **Model type** kepada **MLflow**.

1. Pastikan **Job output** dipilih; ia sepatutnya dipilih secara automatik.

    ![Select output.](../../../../../../translated_images/ms/07-03-select-output.4cf1a0e645baea1f.webp)

2. Pilih **Next**.

3. Pilih **Register**.

    ![Select register.](../../../../../../translated_images/ms/07-04-register.fd82a3b293060bc7.webp)

4. Anda boleh melihat model yang anda daftarkan dengan pergi ke menu **Models** dari tab sebelah kiri.

    ![Registered model.](../../../../../../translated_images/ms/07-05-registered-model.7db9775f58dfd591.webp)

#### Terbitkan model yang ditala halus

1. Pergi ke ruang kerja Azure Machine Learning yang anda buat.

1. Pilih **Endpoints** dari tab sebelah kiri.

1. Pilih **Real-time endpoints** dari menu navigasi.

    ![Create endpoint.](../../../../../../translated_images/ms/07-06-create-endpoint.1ba865c606551f09.webp)

1. Pilih **Create**.

1. Pilih model terdaftar yang anda cipta.

    ![Select registered model.](../../../../../../translated_images/ms/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Pilih **Select**.

1. Lakukan tugasan berikut:

    - Pilih **Virtual machine** kepada *Standard_NC6s_v3*.
    - Pilih **Instance count** yang anda ingin gunakan. Contohnya, *1*.
    - Pilih **Endpoint** kepada **New** untuk membuat titik akhir.
    - Masukkan **Endpoint name**. Ia mesti nilai unik.
    - Masukkan **Deployment name**. Ia mesti nilai unik.

    ![Fill the deployment setting.](../../../../../../translated_images/ms/07-08-deployment-setting.43ddc4209e673784.webp)

1. Pilih **Deploy**.

> [!WARNING]
> Untuk mengelakkan caj tambahan ke akaun anda, pastikan untuk memadam titik akhir yang dibuat dalam ruang kerja Azure Machine Learning.
>

#### Semak status penerbitan dalam Azure Machine Learning Workspace

1. Pergi ke ruang kerja Azure Machine Learning yang anda buat.

1. Pilih **Endpoints** dari tab sebelah kiri.

1. Pilih titik akhir yang anda cipta.

    ![Select endpoints](../../../../../../translated_images/ms/07-09-check-deployment.325d18cae8475ef4.webp)

1. Pada halaman ini, anda boleh mengurus titik akhir sepanjang proses penerbitan.

> [!NOTE]
> Setelah penerbitan selesai, pastikan **Live traffic** ditetapkan kepada **100%**. Jika tidak, pilih **Update traffic** untuk melaraskan tetapan trafik. Perlu diingat bahawa anda tidak boleh menguji model jika trafik ditetapkan kepada 0%.
>
> ![Set traffic.](../../../../../../translated_images/ms/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Senario 3: Integrasi dengan Prompt flow dan Berbual dengan model khusus anda dalam Microsoft Foundry

### Integrasikan model Phi-3 khusus dengan Prompt flow

Selepas berjaya menerbitkan model yang telah ditala halus, anda kini boleh mengintegrasikannya dengan Prompt Flow untuk menggunakan model anda dalam aplikasi masa nyata, membolehkan pelbagai tugasan interaktif dengan model Phi-3 khusus anda.

Dalam latihan ini, anda akan:

- Buat Microsoft Foundry Hub.
- Buat Microsoft Foundry Project.
- Buat Prompt flow.
- Tambah sambungan khusus untuk model Phi-3 yang telah ditala halus.
- Sediakan Prompt flow untuk berbual dengan model Phi-3 khusus anda.

> [!NOTE]
> Anda juga boleh mengintegrasi dengan Promptflow menggunakan Azure ML Studio. Proses integrasi yang sama boleh digunakan untuk Azure ML Studio.

#### Buat Microsoft Foundry Hub

Anda perlu membuat Hub sebelum membuat Projek. Hub bertindak seperti Kumpulan Sumber, membolehkan anda mengatur dan mengurus beberapa Projek dalam Microsoft Foundry.
1. Lawati [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Pilih **Semua hab** dari tab sebelah kiri.

1. Pilih **+ Hab baru** dari menu navigasi.

    ![Create hub.](../../../../../../translated_images/ms/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Laksanakan tugasan berikut:

    - Masukkan **Nama hab**. Ia mesti nilai yang unik.
    - Pilih **Langganan** Azure anda.
    - Pilih **Kumpulan sumber** yang akan digunakan (cipta satu yang baru jika perlu).
    - Pilih **Lokasi** yang ingin anda gunakan.
    - Pilih **Sambungkan Perkhidmatan Azure AI** yang ingin digunakan (cipta baru jika perlu).
    - Pilih **Sambungkan Azure AI Search** ke **Langkau sambungan**.

    ![Fill hub.](../../../../../../translated_images/ms/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Pilih **Seterusnya**.

#### Cipta Projek Microsoft Foundry

1. Dalam Hab yang anda cipta, pilih **Semua projek** dari tab sebelah kiri.

1. Pilih **+ Projek baru** dari menu navigasi.

    ![Select new project.](../../../../../../translated_images/ms/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Masukkan **Nama projek**. Ia mesti nilai yang unik.

    ![Create project.](../../../../../../translated_images/ms/08-05-create-project.4d97f0372f03375a.webp)

1. Pilih **Cipta projek**.

#### Tambah sambungan tersuai untuk model Phi-3 yang telah disesuaikan

Untuk mengintegrasikan model Phi-3 tersuai anda dengan Prompt flow, anda perlu menyimpan titik akhir dan kunci model dalam sambungan tersuai. Persediaan ini memastikan akses ke model Phi-3 tersuai anda dalam Prompt flow.

#### Tetapkan kunci api dan uri titik akhir model Phi-3 yang telah disesuaikan

1. Lawati [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Navigasi ke ruang kerja Pembelajaran Mesin Azure yang anda cipta.

1. Pilih **Titik akhir** dari tab sebelah kiri.

    ![Select endpoints.](../../../../../../translated_images/ms/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Pilih titik akhir yang anda cipta.

    ![Select endpoints.](../../../../../../translated_images/ms/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Pilih **Gunakan** dari menu navigasi.

1. Salin **Titik akhir REST** dan **Kunci Utama** anda.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/ms/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Tambah Sambungan Tersuai

1. Lawati [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Navigasi ke projek Microsoft Foundry yang anda cipta.

1. Dalam Projek yang anda cipta, pilih **Tetapan** dari tab sebelah kiri.

1. Pilih **+ Sambungan baru**.

    ![Select new connection.](../../../../../../translated_images/ms/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Pilih **Kunci tersuai** dari menu navigasi.

    ![Select custom keys.](../../../../../../translated_images/ms/08-10-select-custom-keys.856f6b2966460551.webp)

1. Lakukan tugasan berikut:

    - Pilih **+ Tambah pasangan nama nilai kunci**.
    - Untuk nama kunci, masukkan **endpoint** dan tampal titik akhir yang anda salin dari Azure ML Studio ke dalam medan nilai.
    - Pilih **+ Tambah pasangan nama nilai kunci** sekali lagi.
    - Untuk nama kunci, masukkan **key** dan tampal kunci yang anda salin dari Azure ML Studio ke dalam medan nilai.
    - Selepas menambah kunci-kunci, pilih **adalah rahsia** untuk mengelakkan pendedahan kunci.

    ![Add connection.](../../../../../../translated_images/ms/08-11-add-connection.785486badb4d2d26.webp)

1. Pilih **Tambah sambungan**.

#### Cipta Prompt flow

Anda telah menambah sambungan tersuai dalam Microsoft Foundry. Sekarang, mari cipta Prompt flow menggunakan langkah berikut. Kemudian, anda akan sambungkan Prompt flow ini ke sambungan tersuai supaya anda boleh menggunakan model yang telah disesuaikan dalam Prompt flow.

1. Navigasi ke projek Microsoft Foundry yang anda cipta.

1. Pilih **Prompt flow** dari tab sebelah kiri.

1. Pilih **+ Cipta** dari menu navigasi.

    ![Select Promptflow.](../../../../../../translated_images/ms/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Pilih **Aliran sembang** dari menu navigasi.

    ![Select chat flow.](../../../../../../translated_images/ms/08-13-select-flow-type.2ec689b22da32591.webp)

1. Masukkan **Nama folder** untuk digunakan.

    ![Enter name.](../../../../../../translated_images/ms/08-14-enter-name.ff9520fefd89f40d.webp)

2. Pilih **Cipta**.

#### Sediakan Prompt flow untuk bersembang dengan model Phi-3 tersuai anda

Anda perlu mengintegrasikan model Phi-3 yang telah disuaikan ke dalam Prompt flow. Walau bagaimanapun, Prompt flow yang sedia ada tidak direka untuk tujuan ini. Oleh itu, anda mesti mereka semula Prompt flow untuk membolehkan integrasi model tersuai.

1. Dalam Prompt flow, jalankan tugasan berikut untuk membina semula aliran sedia ada:

    - Pilih **Mod fail mentah**.
    - Padamkan semua kod sedia ada dalam fail *flow.dag.yml*.
    - Tambah kod berikut ke dalam fail *flow.dag.yml*.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - Pilih **Simpan**.

    ![Select raw file mode.](../../../../../../translated_images/ms/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Tambah kod berikut ke fail *integrate_with_promptflow.py* untuk menggunakan model Phi-3 tersuai dalam Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Persediaan log
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 model endpoint with the given input data using Custom Connection.
        """

        # "connection" adalah nama Sambungan Tersuai, "endpoint", "key" adalah kunci dalam Sambungan Tersuai
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": {
                "input_string": [
                    {"role": "user", "content": input_data}
                ],
                "parameters": {
                    "temperature": 0.7,
                    "max_new_tokens": 128
                }
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log respons JSON penuh
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/ms/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Untuk maklumat lebih terperinci mengenai menggunakan Prompt flow dalam Microsoft Foundry, anda boleh merujuk kepada [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Pilih **Input sembang**, **Output sembang** untuk membolehkan perbualan dengan model anda.

    ![Input Output.](../../../../../../translated_images/ms/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Kini anda sudah bersedia untuk sembang dengan model Phi-3 tersuai anda. Dalam latihan seterusnya, anda akan belajar bagaimana untuk memulakan Prompt flow dan menggunakannya untuk bersembang dengan model Phi-3 yang telah disesuaikan.

> [!NOTE]
>
> Aliran yang dibina semula sepatutnya kelihatan seperti imej di bawah:
>
> ![Flow example.](../../../../../../translated_images/ms/08-18-graph-example.d6457533952e690c.webp)
>

### Bersembang dengan model Phi-3 tersuai anda

Sekarang anda telah menyesuaikan dan mengintegrasikan model Phi-3 tersuai anda dengan Prompt flow, anda sudah bersedia untuk mula berinteraksi dengannya. Latihan ini akan membimbing anda melalui proses menyediakan dan memulakan perbualan dengan model menggunakan Prompt flow. Dengan mengikuti langkah ini, anda dapat memanfaatkan sepenuhnya keupayaan model Phi-3 yang telah disuaikan untuk pelbagai tugasan dan perbualan.

- Bersembang dengan model Phi-3 tersuai anda menggunakan Prompt flow.

#### Mula Prompt flow

1. Pilih **Mula sesi pengkomputeran** untuk memulakan Prompt flow.

    ![Start compute session.](../../../../../../translated_images/ms/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Pilih **Sahkan dan tafsir input** untuk memperbaharui parameter.

    ![Validate input.](../../../../../../translated_images/ms/09-02-validate-input.317c76ef766361e9.webp)

1. Pilih **Nilai** bagi **sambungan** ke sambungan tersuai yang anda cipta. Contohnya, *connection*.

    ![Connection.](../../../../../../translated_images/ms/09-03-select-connection.99bdddb4b1844023.webp)

#### Bersembang dengan model tersuai anda

1. Pilih **Sembang**.

    ![Select chat.](../../../../../../translated_images/ms/09-04-select-chat.61936dce6612a1e6.webp)

1. Berikut adalah contoh hasil: Kini anda boleh bersembang dengan model Phi-3 tersuai anda. Disyorkan untuk bertanya soalan berdasarkan data yang digunakan untuk fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/ms/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->