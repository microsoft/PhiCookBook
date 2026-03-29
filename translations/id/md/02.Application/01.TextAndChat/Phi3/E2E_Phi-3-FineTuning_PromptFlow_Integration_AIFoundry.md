# Fine-tune dan Integrasikan model Phi-3 khusus dengan Prompt flow di Microsoft Foundry

Contoh end-to-end (E2E) ini didasarkan pada panduan "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" dari Microsoft Tech Community. Ini memperkenalkan proses fine-tuning, penerapan, dan integrasi model Phi-3 khusus dengan Prompt flow di Microsoft Foundry.
Berbeda dengan contoh E2E, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", yang melibatkan menjalankan kode secara lokal, tutorial ini sepenuhnya berfokus pada fine-tuning dan mengintegrasikan model Anda dalam Azure AI / ML Studio.

## Ikhtisar

Dalam contoh E2E ini, Anda akan belajar cara melakukan fine-tuning model Phi-3 dan mengintegrasikannya dengan Prompt flow di Microsoft Foundry. Dengan memanfaatkan Azure AI / ML Studio, Anda akan membangun alur kerja untuk menerapkan dan menggunakan model AI khusus. Contoh E2E ini dibagi menjadi tiga skenario:

**Skenario 1: Persiapkan sumber daya Azure dan Siapkan untuk fine-tuning**

**Skenario 2: Fine-tune model Phi-3 dan Terapkan di Azure Machine Learning Studio**

**Skenario 3: Integrasikan dengan Prompt flow dan Chat dengan model khusus Anda di Microsoft Foundry**

Berikut ikhtisar dari contoh E2E ini.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/id/00-01-architecture.198ba0f1ae6d841a.webp)

### Daftar Isi

1. **[Skenario 1: Persiapkan sumber daya Azure dan Siapkan untuk fine-tuning](#skenario-1-persiapkan-sumber-daya-azure-dan-siapkan-untuk-fine-tuning)**
    - [Buat Azure Machine Learning Workspace](#buat-azure-machine-learning-workspace)
    - [Ajukan kuota GPU dalam Azure Subscription](#ajukan-kuota-gpu-dalam-azure-subscription)
    - [Tambah penugasan peran](#tambah-penugasan-peran)
    - [Siapkan proyek](#siapkan-proyek)
    - [Siapkan dataset untuk fine-tuning](#siapkan-dataset-untuk-fine-tuning)

1. **[Skenario 2: Fine-tune model Phi-3 dan Terapkan di Azure Machine Learning Studio](#skenario-2-fine-tune-model-phi-3-dan-deploy-di-azure-machine-learning-studio)**
    - [Fine-tune model Phi-3](#fine-tune-model-phi-3)
    - [Terapkan model Phi-3 yang sudah di-fine-tune](#deploy-model-phi-3-yang-telah-di-fine-tune)

1. **[Skenario 3: Integrasikan dengan Prompt flow dan Chat dengan model khusus Anda di Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Integrasikan model Phi-3 khusus dengan Prompt flow](#integrasi-model-phi-3-kustom-dengan-prompt-flow)
    - [Chat dengan model Phi-3 khusus Anda](#chat-dengan-model-phi-3-kustom-anda)

## Skenario 1: Persiapkan sumber daya Azure dan Siapkan untuk fine-tuning

### Buat Azure Machine Learning Workspace

1. Ketik *azure machine learning* di **bilah pencarian** di bagian atas halaman portal dan pilih **Azure Machine Learning** dari opsi yang muncul.

    ![Type azure machine learning.](../../../../../../translated_images/id/01-01-type-azml.acae6c5455e67b4b.webp)

2. Pilih **+ Create** dari menu navigasi.

3. Pilih **New workspace** dari menu navigasi.

    ![Select new workspace.](../../../../../../translated_images/id/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Lakukan tugas berikut:

    - Pilih **Subscription** Azure Anda.
    - Pilih **Resource group** yang akan digunakan (buat baru jika perlu).
    - Masukkan **Workspace Name**. Harus berupa nilai unik.
    - Pilih **Region** yang ingin Anda gunakan.
    - Pilih **Storage account** yang akan digunakan (buat baru jika perlu).
    - Pilih **Key vault** yang akan digunakan (buat baru jika perlu).
    - Pilih **Application insights** yang akan digunakan (buat baru jika perlu).
    - Pilih **Container registry** yang akan digunakan (buat baru jika perlu).

    ![Fill azure machine learning.](../../../../../../translated_images/id/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Pilih **Review + Create**.

6. Pilih **Create**.

### Ajukan kuota GPU dalam Azure Subscription

Dalam tutorial ini, Anda akan belajar cara melakukan fine-tuning dan menerapkan model Phi-3, menggunakan GPU. Untuk fine-tuning, Anda akan menggunakan GPU *Standard_NC24ads_A100_v4*, yang memerlukan permintaan kuota. Untuk penerapan, Anda akan menggunakan GPU *Standard_NC6s_v3*, yang juga memerlukan permintaan kuota.

> [!NOTE]
>
> Hanya langganan Pay-As-You-Go (tipe langganan standar) yang memenuhi syarat untuk alokasi GPU; langganan manfaat saat ini belum didukung.
>

1. Kunjungi [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Lakukan tugas berikut untuk mengajukan kuota *Standard NCADSA100v4 Family*:

    - Pilih **Quota** dari tab sisi kiri.
    - Pilih **Virtual machine family** yang akan digunakan. Misalnya, pilih **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, yang mencakup GPU *Standard_NC24ads_A100_v4*.
    - Pilih **Request quota** dari menu navigasi.

        ![Request quota.](../../../../../../translated_images/id/02-02-request-quota.c0428239a63ffdd5.webp)

    - Di halaman Request quota, masukkan **New cores limit** yang ingin Anda gunakan. Misalnya, 24.
    - Di halaman Request quota, pilih **Submit** untuk mengajukan kuota GPU.

1. Lakukan tugas berikut untuk mengajukan kuota *Standard NCSv3 Family*:

    - Pilih **Quota** dari tab sisi kiri.
    - Pilih **Virtual machine family** yang akan digunakan. Misalnya, pilih **Standard NCSv3 Family Cluster Dedicated vCPUs**, yang mencakup GPU *Standard_NC6s_v3*.
    - Pilih **Request quota** dari menu navigasi.
    - Di halaman Request quota, masukkan **New cores limit** yang ingin Anda gunakan. Misalnya, 24.
    - Di halaman Request quota, pilih **Submit** untuk mengajukan kuota GPU.

### Tambah penugasan peran

Untuk melakukan fine-tuning dan menerapkan model Anda, Anda harus terlebih dahulu membuat User Assigned Managed Identity (UAI) dan memberikan izin yang sesuai. UAI ini akan digunakan untuk autentikasi selama penerapan.

#### Buat User Assigned Managed Identity (UAI)

1. Ketik *managed identities* di **bilah pencarian** di bagian atas halaman portal dan pilih **Managed Identities** dari opsi yang muncul.

    ![Type managed identities.](../../../../../../translated_images/id/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Pilih **+ Create**.

    ![Select create.](../../../../../../translated_images/id/03-02-select-create.92bf8989a5cd98f2.webp)

1. Lakukan tugas berikut:

    - Pilih **Subscription** Azure Anda.
    - Pilih **Resource group** yang akan digunakan (buat baru jika perlu).
    - Pilih **Region** yang ingin Anda gunakan.
    - Masukkan **Name**. Harus berupa nilai unik.

    ![Select create.](../../../../../../translated_images/id/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Pilih **Review + create**.

1. Pilih **+ Create**.

#### Tambah penugasan peran Contributor ke Managed Identity

1. Navigasikan ke sumber daya Managed Identity yang Anda buat.

1. Pilih **Azure role assignments** dari tab sisi kiri.

1. Pilih **+Add role assignment** dari menu navigasi.

1. Di halaman Add role assignment, lakukan hal berikut:
    - Pilih **Scope** ke **Resource group**.
    - Pilih **Subscription** Azure Anda.
    - Pilih **Resource group** yang akan digunakan.
    - Pilih **Role** menjadi **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/id/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Pilih **Save**.

#### Tambah penugasan peran Storage Blob Data Reader ke Managed Identity

1. Ketik *storage accounts* di **bilah pencarian** di bagian atas halaman portal dan pilih **Storage accounts** dari opsi yang muncul.

    ![Type storage accounts.](../../../../../../translated_images/id/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Pilih akun penyimpanan yang terkait dengan Azure Machine Learning workspace yang Anda buat. Misalnya, *finetunephistorage*.

1. Lakukan tugas berikut untuk membuka halaman Add role assignment:

    - Navigasikan ke akun Azure Storage yang Anda buat.
    - Pilih **Access Control (IAM)** dari tab sisi kiri.
    - Pilih **+ Add** dari menu navigasi.
    - Pilih **Add role assignment** dari menu navigasi.

    ![Add role.](../../../../../../translated_images/id/03-06-add-role.353ccbfdcf0789c2.webp)

1. Di halaman Add role assignment, lakukan hal berikut:

    - Pada halaman Role, ketik *Storage Blob Data Reader* di **bilah pencarian** dan pilih **Storage Blob Data Reader** dari opsi yang muncul.
    - Pada halaman Role, pilih **Next**.
    - Pada halaman Members, pilih **Assign access to** **Managed identity**.
    - Pada halaman Members, pilih **+ Select members**.
    - Pada halaman Select managed identities, pilih **Subscription** Azure Anda.
    - Pada halaman Select managed identities, pilih **Managed identity** menjadi **Manage Identity**.
    - Pada halaman Select managed identities, pilih Manage Identity yang Anda buat. Misalnya, *finetunephi-managedidentity*.
    - Pada halaman Select managed identities, pilih **Select**.

    ![Select managed identity.](../../../../../../translated_images/id/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Pilih **Review + assign**.

#### Tambah penugasan peran AcrPull ke Managed Identity

1. Ketik *container registries* di **bilah pencarian** di bagian atas halaman portal dan pilih **Container registries** dari opsi yang muncul.

    ![Type container registries.](../../../../../../translated_images/id/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Pilih container registry yang terkait dengan Azure Machine Learning workspace Anda. Misalnya, *finetunephicontainerregistry*

1. Lakukan tugas berikut untuk membuka halaman Add role assignment:

    - Pilih **Access Control (IAM)** dari tab sisi kiri.
    - Pilih **+ Add** dari menu navigasi.
    - Pilih **Add role assignment** dari menu navigasi.

1. Di halaman Add role assignment, lakukan hal berikut:

    - Pada halaman Role, ketik *AcrPull* di **bilah pencarian** dan pilih **AcrPull** dari opsi yang muncul.
    - Pada halaman Role, pilih **Next**.
    - Pada halaman Members, pilih **Assign access to** **Managed identity**.
    - Pada halaman Members, pilih **+ Select members**.
    - Pada halaman Select managed identities, pilih **Subscription** Azure Anda.
    - Pada halaman Select managed identities, pilih **Managed identity** menjadi **Manage Identity**.
    - Pada halaman Select managed identities, pilih Manage Identity yang Anda buat. Misalnya, *finetunephi-managedidentity*.
    - Pada halaman Select managed identities, pilih **Select**.
    - Pilih **Review + assign**.

### Siapkan proyek

Untuk mengunduh dataset yang diperlukan untuk fine-tuning, Anda akan menyiapkan lingkungan lokal.

Dalam latihan ini, Anda akan

- Membuat folder untuk bekerja di dalamnya.
- Membuat lingkungan virtual.
- Menginstal paket yang diperlukan.
- Membuat file *download_dataset.py* untuk mengunduh dataset.

#### Buat folder untuk bekerja di dalamnya

1. Buka jendela terminal dan ketik perintah berikut untuk membuat folder bernama *finetune-phi* di jalur default.

    ```console
    mkdir finetune-phi
    ```

2. Ketik perintah berikut di terminal Anda untuk masuk ke folder *finetune-phi* yang Anda buat.

    ```console
    cd finetune-phi
    ```

#### Buat lingkungan virtual

1. Ketik perintah berikut di terminal Anda untuk membuat lingkungan virtual bernama *.venv*.
    ```console
    python -m venv .venv
    ```

2. Ketik perintah berikut di dalam terminal Anda untuk mengaktifkan lingkungan virtual.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Jika berhasil, Anda harus melihat *(.venv)* sebelum prompt perintah.

#### Instal paket yang diperlukan

1. Ketik perintah berikut di dalam terminal Anda untuk menginstal paket yang diperlukan.

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

1. Pilih **File** dari bilah menu.

1. Pilih **Open Folder**.

1. Pilih folder *finetune-phi* yang telah Anda buat, yang terletak di *C:\Users\yourUserName\finetune-phi*.

    ![Pilih folder yang telah Anda buat.](../../../../../../translated_images/id/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. Di panel kiri Visual Studio Code, klik kanan dan pilih **New File** untuk membuat file baru bernama *download_dataset.py*.

    ![Buat file baru.](../../../../../../translated_images/id/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Siapkan dataset untuk fine-tuning

Dalam latihan ini, Anda akan menjalankan file *download_dataset.py* untuk mengunduh dataset *ultrachat_200k* ke lingkungan lokal Anda. Kemudian Anda akan menggunakan dataset ini untuk melakukan fine-tune model Phi-3 di Azure Machine Learning.

Dalam latihan ini, Anda akan:

- Menambahkan kode pada file *download_dataset.py* untuk mengunduh dataset.
- Menjalankan file *download_dataset.py* untuk mengunduh dataset ke lingkungan lokal Anda.

#### Unduh dataset Anda menggunakan *download_dataset.py*

1. Buka file *download_dataset.py* di Visual Studio Code.

1. Tambahkan kode berikut ke dalam file *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Muat dataset dengan nama, konfigurasi, dan rasio pembagian yang ditentukan
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Bagi dataset menjadi set train dan test (80% train, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Buat direktori jika belum ada
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Buka file dalam mode tulis
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterasi setiap record dalam dataset
            for record in dataset:
                # Dump record sebagai objek JSON dan tulis ke file
                json.dump(record, f)
                # Tulis karakter newline untuk memisahkan record
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Muat dan bagi dataset ULTRACHAT_200k dengan konfigurasi dan rasio pembagian tertentu
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Ekstrak dataset train dan test dari pembagian
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Simpan dataset train ke file JSONL
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Simpan dataset test ke file JSONL terpisah
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Ketik perintah berikut di dalam terminal Anda untuk menjalankan skrip dan mengunduh dataset ke lingkungan lokal Anda.

    ```console
    python download_dataset.py
    ```

1. Verifikasi bahwa dataset berhasil disimpan ke direktori lokal *finetune-phi/data*.

> [!NOTE]
>
> #### Catatan tentang ukuran dataset dan waktu fine-tuning
>
> Dalam tutorial ini, Anda hanya menggunakan 1% dari dataset (`split='train[:1%]'`). Ini secara signifikan mengurangi jumlah data, mempercepat proses unggah dan fine-tuning. Anda dapat menyesuaikan persentase untuk menemukan keseimbangan yang tepat antara waktu pelatihan dan performa model. Menggunakan subset dataset yang lebih kecil mengurangi waktu yang diperlukan untuk fine-tuning, membuat proses ini lebih mudah dikelola untuk tutorial.

## Skenario 2: Fine-tune model Phi-3 dan Deploy di Azure Machine Learning Studio

### Fine-tune model Phi-3

Dalam latihan ini, Anda akan melakukan fine-tune model Phi-3 di Azure Machine Learning Studio.

Dalam latihan ini, Anda akan:

- Membuat kluster komputer untuk fine-tuning.
- Melakukan fine-tune model Phi-3 di Azure Machine Learning Studio.

#### Membuat kluster komputer untuk fine-tuning

1. Kunjungi [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pilih **Compute** dari tab sisi kiri.

1. Pilih **Compute clusters** dari menu navigasi.

1. Pilih **+ New**.

    ![Pilih compute.](../../../../../../translated_images/id/06-01-select-compute.a29cff290b480252.webp)

1. Lakukan tugas-tugas berikut:

    - Pilih **Region** yang ingin Anda gunakan.
    - Pilih **Virtual machine tier** ke **Dedicated**.
    - Pilih **Virtual machine type** ke **GPU**.
    - Pilih filter **Virtual machine size** ke **Select from all options**.
    - Pilih **Virtual machine size** ke **Standard_NC24ads_A100_v4**.

    ![Buat kluster.](../../../../../../translated_images/id/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Pilih **Next**.

1. Lakukan tugas-tugas berikut:

    - Masukkan **Compute name**. Harus nilai unik.
    - Pilih **Minimum number of nodes** ke **0**.
    - Pilih **Maximum number of nodes** ke **1**.
    - Pilih **Idle seconds before scale down** ke **120**.

    ![Buat kluster.](../../../../../../translated_images/id/06-03-create-cluster.4a54ba20914f3662.webp)

1. Pilih **Create**.

#### Fine-tune model Phi-3

1. Kunjungi [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pilih workspace Azure Machine Learning yang telah Anda buat.

    ![Pilih workspace yang telah Anda buat.](../../../../../../translated_images/id/06-04-select-workspace.a92934ac04f4f181.webp)

1. Lakukan tugas berikut:

    - Pilih **Model catalog** dari tab sisi kiri.
    - Ketik *phi-3-mini-4k* di **search bar** dan pilih **Phi-3-mini-4k-instruct** dari opsi yang muncul.

    ![Ketik phi-3-mini-4k.](../../../../../../translated_images/id/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Pilih **Fine-tune** dari menu navigasi.

    ![Pilih fine tune.](../../../../../../translated_images/id/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Lakukan tugas berikut:

    - Pilih **Select task type** ke **Chat completion**.
    - Pilih **+ Select data** untuk mengunggah **Training data**.
    - Pilih tipe unggah data validasi ke **Provide different validation data**.
    - Pilih **+ Select data** untuk mengunggah **Validation data**.

    ![Isi halaman fine-tuning.](../../../../../../translated_images/id/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Anda dapat memilih **Advanced settings** untuk menyesuaikan konfigurasi seperti **learning_rate** dan **lr_scheduler_type** guna mengoptimalkan proses fine-tuning sesuai kebutuhan spesifik Anda.

1. Pilih **Finish**.

1. Dalam latihan ini, Anda berhasil melakukan fine-tune model Phi-3 menggunakan Azure Machine Learning. Perlu diperhatikan bahwa proses fine-tuning dapat memakan waktu cukup lama. Setelah menjalankan pekerjaan fine-tuning, Anda harus menunggu hingga selesai. Anda dapat memonitor status pekerjaan fine-tuning dengan membuka tab Jobs di sisi kiri Workspace Azure Machine Learning Anda. Dalam seri berikutnya, Anda akan melakukan deployment pada model yang telah di-fine-tune dan mengintegrasikannya dengan Prompt flow.

    ![Lihat pekerjaan fine tuning.](../../../../../../translated_images/id/06-08-output.2bd32e59930672b1.webp)

### Deploy model Phi-3 yang telah di-fine-tune

Untuk mengintegrasikan model Phi-3 yang telah di-fine-tune dengan Prompt flow, Anda perlu melakukan deployment pada model agar dapat diakses untuk inferensi waktu nyata. Proses ini melibatkan pendaftaran model, membuat endpoint online, dan melakukan deployment model.

Dalam latihan ini, Anda akan:

- Mendaftarkan model yang telah di-fine-tune di workspace Azure Machine Learning.
- Membuat endpoint online.
- Mendeploy model Phi-3 yang telah terdaftar dan di-fine-tune.

#### Daftarkan model yang telah di-fine-tune

1. Kunjungi [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pilih workspace Azure Machine Learning yang telah Anda buat.

    ![Pilih workspace yang telah Anda buat.](../../../../../../translated_images/id/06-04-select-workspace.a92934ac04f4f181.webp)

1. Pilih **Models** dari tab sisi kiri.
1. Pilih **+ Register**.
1. Pilih **From a job output**.

    ![Daftarkan model.](../../../../../../translated_images/id/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Pilih pekerjaan yang telah Anda buat.

    ![Pilih pekerjaan.](../../../../../../translated_images/id/07-02-select-job.3e2e1144cd6cd093.webp)

1. Pilih **Next**.

1. Pilih **Model type** ke **MLflow**.

1. Pastikan **Job output** dipilih; ini harus otomatis terpilih.

    ![Pilih output.](../../../../../../translated_images/id/07-03-select-output.4cf1a0e645baea1f.webp)

2. Pilih **Next**.

3. Pilih **Register**.

    ![Pilih register.](../../../../../../translated_images/id/07-04-register.fd82a3b293060bc7.webp)

4. Anda dapat melihat model yang terdaftar dengan menavigasi ke menu **Models** dari tab sisi kiri.

    ![Model terdaftar.](../../../../../../translated_images/id/07-05-registered-model.7db9775f58dfd591.webp)

#### Deploy model yang telah di-fine-tune

1. Navigasi ke workspace Azure Machine Learning yang telah Anda buat.

1. Pilih **Endpoints** dari tab sisi kiri.

1. Pilih **Real-time endpoints** dari menu navigasi.

    ![Buat endpoint.](../../../../../../translated_images/id/07-06-create-endpoint.1ba865c606551f09.webp)

1. Pilih **Create**.

1. Pilih model terdaftar yang telah Anda buat.

    ![Pilih model terdaftar.](../../../../../../translated_images/id/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Pilih **Select**.

1. Lakukan tugas berikut:

    - Pilih **Virtual machine** ke *Standard_NC6s_v3*.
    - Pilih **Instance count** yang ingin Anda gunakan. Misalnya, *1*.
    - Pilih **Endpoint** ke **New** untuk membuat endpoint.
    - Masukkan **Endpoint name**. Harus nilai unik.
    - Masukkan **Deployment name**. Harus nilai unik.

    ![Isi pengaturan deployment.](../../../../../../translated_images/id/07-08-deployment-setting.43ddc4209e673784.webp)

1. Pilih **Deploy**.

> [!WARNING]
> Untuk menghindari biaya tambahan pada akun Anda, pastikan untuk menghapus endpoint yang dibuat di workspace Azure Machine Learning.
>

#### Periksa status deployment di Azure Machine Learning Workspace

1. Navigasi ke workspace Azure Machine Learning yang Anda buat.

1. Pilih **Endpoints** dari tab sisi kiri.

1. Pilih endpoint yang telah Anda buat.

    ![Pilih endpoints](../../../../../../translated_images/id/07-09-check-deployment.325d18cae8475ef4.webp)

1. Pada halaman ini, Anda dapat mengelola endpoint selama proses deployment.

> [!NOTE]
> Setelah deployment selesai, pastikan bahwa **Live traffic** disetel ke **100%**. Jika belum, pilih **Update traffic** untuk mengatur konfigurasi lalu lintas. Perlu diketahui bahwa Anda tidak dapat menguji model jika lalu lintas disetel ke 0%.
>
> ![Set traffic.](../../../../../../translated_images/id/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Skenario 3: Integrasi dengan Prompt flow dan Chat dengan model kustom Anda di Microsoft Foundry

### Integrasi model Phi-3 kustom dengan Prompt flow

Setelah berhasil mendeploy model yang telah di-fine-tune, Anda sekarang dapat mengintegrasikannya dengan Prompt Flow untuk menggunakan model Anda dalam aplikasi waktu nyata, memungkinkan berbagai tugas interaktif dengan model Phi-3 kustom Anda.

Dalam latihan ini, Anda akan:

- Membuat Microsoft Foundry Hub.
- Membuat Proyek Microsoft Foundry.
- Membuat Prompt flow.
- Menambahkan koneksi kustom untuk model Phi-3 yang telah di-fine-tune.
- Menyiapkan Prompt flow untuk chat dengan model Phi-3 kustom Anda.

> [!NOTE]
> Anda juga dapat melakukan integrasi dengan Promptflow menggunakan Azure ML Studio. Proses integrasi yang sama dapat diterapkan pada Azure ML Studio.

#### Membuat Microsoft Foundry Hub

Anda perlu membuat Hub sebelum membuat Proyek. Hub berperan seperti Resource Group, memungkinkan Anda mengorganisasi dan mengelola beberapa Proyek dalam Microsoft Foundry.
1. Kunjungi [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Pilih **All hubs** dari tab sisi kiri.

1. Pilih **+ New hub** dari menu navigasi.

    ![Create hub.](../../../../../../translated_images/id/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Lakukan tugas berikut:

    - Masukkan **Hub name**. Nilainya harus unik.
    - Pilih **Subscription** Azure Anda.
    - Pilih **Resource group** yang akan digunakan (buat yang baru jika perlu).
    - Pilih **Location** yang ingin Anda gunakan.
    - Pilih **Connect Azure AI Services** untuk digunakan (buat yang baru jika perlu).
    - Pilih **Connect Azure AI Search** ke **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/id/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Pilih **Next**.

#### Buat Proyek Microsoft Foundry

1. Di Hub yang Anda buat, pilih **All projects** dari tab sisi kiri.

1. Pilih **+ New project** dari menu navigasi.

    ![Select new project.](../../../../../../translated_images/id/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Masukkan **Project name**. Nilainya harus unik.

    ![Create project.](../../../../../../translated_images/id/08-05-create-project.4d97f0372f03375a.webp)

1. Pilih **Create a project**.

#### Tambahkan koneksi kustom untuk model Phi-3 yang dituning ulang

Untuk mengintegrasikan model Phi-3 kustom Anda dengan Prompt flow, Anda perlu menyimpan endpoint dan kunci model dalam koneksi kustom. Pengaturan ini memastikan akses ke model Phi-3 kustom Anda di Prompt flow.

#### Atur api key dan endpoint uri model Phi-3 yang dituning ulang

1. Kunjungi [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Navigasikan ke workspace Azure Machine learning yang sudah Anda buat.

1. Pilih **Endpoints** dari tab sisi kiri.

    ![Select endpoints.](../../../../../../translated_images/id/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Pilih endpoint yang sudah Anda buat.

    ![Select endpoints.](../../../../../../translated_images/id/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Pilih **Consume** dari menu navigasi.

1. Salin **REST endpoint** dan **Primary key** Anda.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/id/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Tambahkan Koneksi Kustom

1. Kunjungi [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Navigasikan ke proyek Microsoft Foundry yang Anda buat.

1. Di proyek yang Anda buat, pilih **Settings** dari tab sisi kiri.

1. Pilih **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/id/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Pilih **Custom keys** dari menu navigasi.

    ![Select custom keys.](../../../../../../translated_images/id/08-10-select-custom-keys.856f6b2966460551.webp)

1. Lakukan tugas berikut:

    - Pilih **+ Add key value pairs**.
    - Untuk nama kunci, masukkan **endpoint** dan tempel endpoint yang Anda salin dari Azure ML Studio ke dalam kolom nilai.
    - Pilih **+ Add key value pairs** lagi.
    - Untuk nama kunci, masukkan **key** dan tempel kunci yang Anda salin dari Azure ML Studio ke dalam kolom nilai.
    - Setelah menambahkan kunci, pilih **is secret** agar kunci tidak terekspos.

    ![Add connection.](../../../../../../translated_images/id/08-11-add-connection.785486badb4d2d26.webp)

1. Pilih **Add connection**.

#### Buat Prompt flow

Anda telah menambahkan koneksi kustom di Microsoft Foundry. Sekarang, mari buat Prompt flow dengan langkah-langkah berikut. Kemudian, Anda akan menghubungkan Prompt flow ini ke koneksi kustom agar dapat menggunakan model yang dituning dalam Prompt flow.

1. Navigasikan ke proyek Microsoft Foundry yang Anda buat.

1. Pilih **Prompt flow** dari tab sisi kiri.

1. Pilih **+ Create** dari menu navigasi.

    ![Select Promptflow.](../../../../../../translated_images/id/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Pilih **Chat flow** dari menu navigasi.

    ![Select chat flow.](../../../../../../translated_images/id/08-13-select-flow-type.2ec689b22da32591.webp)

1. Masukkan **Folder name** yang akan digunakan.

    ![Enter name.](../../../../../../translated_images/id/08-14-enter-name.ff9520fefd89f40d.webp)

2. Pilih **Create**.

#### Siapkan Prompt flow untuk chatting dengan model Phi-3 kustom Anda

Anda perlu mengintegrasikan model Phi-3 yang sudah dituning ke dalam Prompt flow. Namun, Prompt flow yang disediakan saat ini tidak dirancang untuk tujuan ini. Oleh karena itu, Anda harus mendesain ulang Prompt flow agar dapat mengintegrasikan model kustom tersebut.

1. Di Prompt flow, lakukan tugas berikut untuk membangun ulang alur yang ada:

    - Pilih **Raw file mode**.
    - Hapus semua kode yang ada di file *flow.dag.yml*.
    - Tambahkan kode berikut ke file *flow.dag.yml*.

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

    - Pilih **Save**.

    ![Select raw file mode.](../../../../../../translated_images/id/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Tambahkan kode berikut ke file *integrate_with_promptflow.py* untuk menggunakan model Phi-3 kustom di Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Pengaturan logging
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

        # "connection" adalah nama dari Custom Connection, "endpoint", "key" adalah kunci dalam Custom Connection
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
            
            # Catat respon JSON lengkap
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

    ![Paste prompt flow code.](../../../../../../translated_images/id/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Untuk informasi lebih rinci tentang penggunaan Prompt flow di Microsoft Foundry, Anda dapat merujuk ke [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Pilih **Chat input**, **Chat output** untuk mengaktifkan chat dengan model Anda.

    ![Input Output.](../../../../../../translated_images/id/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Sekarang Anda siap untuk chatting dengan model Phi-3 kustom Anda. Di latihan berikutnya, Anda akan belajar cara memulai Prompt flow dan menggunakannya untuk chatting dengan model Phi-3 yang dituning ulang.

> [!NOTE]
>
> Alur yang dibangun ulang harus terlihat seperti gambar berikut:
>
> ![Flow example.](../../../../../../translated_images/id/08-18-graph-example.d6457533952e690c.webp)
>

### Chat dengan model Phi-3 kustom Anda

Sekarang Anda telah menuning ulang dan mengintegrasikan model Phi-3 kustom Anda dengan Prompt flow, Anda siap untuk mulai berinteraksi dengannya. Latihan ini akan memandu Anda melalui proses menyiapkan dan memulai chat dengan model menggunakan Prompt flow. Dengan mengikuti langkah-langkah ini, Anda akan dapat memanfaatkan sepenuhnya kemampuan model Phi-3 yang Anda tuning untuk berbagai tugas dan percakapan.

- Chat dengan model Phi-3 kustom Anda menggunakan Prompt flow.

#### Mulai Prompt flow

1. Pilih **Start compute sessions** untuk memulai Prompt flow.

    ![Start compute session.](../../../../../../translated_images/id/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Pilih **Validate and parse input** untuk memperbarui parameter.

    ![Validate input.](../../../../../../translated_images/id/09-02-validate-input.317c76ef766361e9.webp)

1. Pilih **Value** dari **connection** ke koneksi kustom yang Anda buat. Contohnya adalah *connection*.

    ![Connection.](../../../../../../translated_images/id/09-03-select-connection.99bdddb4b1844023.webp)

#### Chat dengan model kustom Anda

1. Pilih **Chat**.

    ![Select chat.](../../../../../../translated_images/id/09-04-select-chat.61936dce6612a1e6.webp)

1. Berikut contoh hasilnya: Sekarang Anda dapat chatting dengan model Phi-3 kustom Anda. Disarankan untuk mengajukan pertanyaan berdasarkan data yang digunakan untuk fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/id/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah dan utama. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->