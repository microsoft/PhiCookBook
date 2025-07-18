<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-07-17T01:42:52+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "id"
}
-->
# Fine-tune dan Integrasikan model Phi-3 kustom dengan Prompt flow di Azure AI Foundry

Contoh end-to-end (E2E) ini didasarkan pada panduan "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" dari Microsoft Tech Community. Panduan ini memperkenalkan proses fine-tuning, deployment, dan integrasi model Phi-3 kustom dengan Prompt flow di Azure AI Foundry.  
Berbeda dengan contoh E2E, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", yang melibatkan menjalankan kode secara lokal, tutorial ini sepenuhnya berfokus pada fine-tuning dan integrasi model Anda di dalam Azure AI / ML Studio.

## Ikhtisar

Dalam contoh E2E ini, Anda akan belajar cara melakukan fine-tuning model Phi-3 dan mengintegrasikannya dengan Prompt flow di Azure AI Foundry. Dengan memanfaatkan Azure AI / ML Studio, Anda akan membangun alur kerja untuk deployment dan penggunaan model AI kustom. Contoh E2E ini dibagi menjadi tiga skenario:

**Skenario 1: Menyiapkan sumber daya Azure dan Persiapan untuk fine-tuning**

**Skenario 2: Fine-tune model Phi-3 dan Deploy di Azure Machine Learning Studio**

**Skenario 3: Integrasi dengan Prompt flow dan Chat dengan model kustom Anda di Azure AI Foundry**

Berikut adalah gambaran umum dari contoh E2E ini.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a2ceacdc6401c688bdf100d874fe8d55169f7723ed024781e.id.png)

### Daftar Isi

1. **[Skenario 1: Menyiapkan sumber daya Azure dan Persiapan untuk fine-tuning](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Membuat Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Meminta kuota GPU di Azure Subscription](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Menambahkan penugasan peran](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Menyiapkan proyek](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Mempersiapkan dataset untuk fine-tuning](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Skenario 2: Fine-tune model Phi-3 dan Deploy di Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Fine-tune model Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Deploy model Phi-3 yang sudah di-fine-tune](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Skenario 3: Integrasi dengan Prompt flow dan Chat dengan model kustom Anda di Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrasikan model Phi-3 kustom dengan Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Chat dengan model Phi-3 kustom Anda](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Skenario 1: Menyiapkan sumber daya Azure dan Persiapan untuk fine-tuning

### Membuat Azure Machine Learning Workspace

1. Ketik *azure machine learning* di **bilah pencarian** di bagian atas halaman portal dan pilih **Azure Machine Learning** dari opsi yang muncul.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b9780de8accc31e4e1de7254e9c34a7836a955d455339e77d.id.png)

2. Pilih **+ Create** dari menu navigasi.

3. Pilih **New workspace** dari menu navigasi.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2cf04946c36873223099fd568e0c3ab0377c096868892fdda.id.png)

4. Lakukan tugas berikut:

    - Pilih **Subscription** Azure Anda.
    - Pilih **Resource group** yang akan digunakan (buat baru jika perlu).
    - Masukkan **Workspace Name**. Harus berupa nilai unik.
    - Pilih **Region** yang ingin Anda gunakan.
    - Pilih **Storage account** yang akan digunakan (buat baru jika perlu).
    - Pilih **Key vault** yang akan digunakan (buat baru jika perlu).
    - Pilih **Application insights** yang akan digunakan (buat baru jika perlu).
    - Pilih **Container registry** yang akan digunakan (buat baru jika perlu).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090ff9ec341c724c1493e7f96726f5c810a89a7409b782a7b04a.id.png)

5. Pilih **Review + Create**.

6. Pilih **Create**.

### Meminta kuota GPU di Azure Subscription

Dalam tutorial ini, Anda akan belajar cara melakukan fine-tuning dan deployment model Phi-3 menggunakan GPU. Untuk fine-tuning, Anda akan menggunakan GPU *Standard_NC24ads_A100_v4*, yang memerlukan permintaan kuota. Untuk deployment, Anda akan menggunakan GPU *Standard_NC6s_v3*, yang juga memerlukan permintaan kuota.

> [!NOTE]
>
> Hanya subscription Pay-As-You-Go (tipe subscription standar) yang memenuhi syarat untuk alokasi GPU; subscription benefit saat ini belum didukung.
>

1. Kunjungi [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Lakukan langkah berikut untuk meminta kuota *Standard NCADSA100v4 Family*:

    - Pilih **Quota** dari tab sebelah kiri.
    - Pilih **Virtual machine family** yang akan digunakan. Misalnya, pilih **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, yang mencakup GPU *Standard_NC24ads_A100_v4*.
    - Pilih **Request quota** dari menu navigasi.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd536f2e4a305c8528a34914370813bc2cda4d7bbdd2de873f0.id.png)

    - Di halaman Request quota, masukkan **New cores limit** yang ingin Anda gunakan. Misalnya, 24.
    - Di halaman Request quota, pilih **Submit** untuk mengajukan permintaan kuota GPU.

1. Lakukan langkah berikut untuk meminta kuota *Standard NCSv3 Family*:

    - Pilih **Quota** dari tab sebelah kiri.
    - Pilih **Virtual machine family** yang akan digunakan. Misalnya, pilih **Standard NCSv3 Family Cluster Dedicated vCPUs**, yang mencakup GPU *Standard_NC6s_v3*.
    - Pilih **Request quota** dari menu navigasi.
    - Di halaman Request quota, masukkan **New cores limit** yang ingin Anda gunakan. Misalnya, 24.
    - Di halaman Request quota, pilih **Submit** untuk mengajukan permintaan kuota GPU.

### Menambahkan penugasan peran

Untuk melakukan fine-tuning dan deployment model Anda, Anda harus terlebih dahulu membuat User Assigned Managed Identity (UAI) dan memberikan izin yang sesuai. UAI ini akan digunakan untuk autentikasi selama deployment.

#### Membuat User Assigned Managed Identity (UAI)

1. Ketik *managed identities* di **bilah pencarian** di bagian atas halaman portal dan pilih **Managed Identities** dari opsi yang muncul.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e52f52a152187b230243fe884f58a9940cd9b534db3dcea383.id.png)

1. Pilih **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f27b6680cd94ef6ec7557394022dafdcfba2a92777b11e4817.id.png)

1. Lakukan tugas berikut:

    - Pilih **Subscription** Azure Anda.
    - Pilih **Resource group** yang akan digunakan (buat baru jika perlu).
    - Pilih **Region** yang ingin Anda gunakan.
    - Masukkan **Name**. Harus berupa nilai unik.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0e313fffaecf7d6ce4ee5e86c0badcd038f03519cac63b76b.id.png)

1. Pilih **Review + create**.

1. Pilih **+ Create**.

#### Menambahkan penugasan peran Contributor ke Managed Identity

1. Navigasikan ke resource Managed Identity yang sudah Anda buat.

1. Pilih **Azure role assignments** dari tab sebelah kiri.

1. Pilih **+Add role assignment** dari menu navigasi.

1. Di halaman Add role assignment, lakukan tugas berikut:
    - Pilih **Scope** ke **Resource group**.
    - Pilih **Subscription** Azure Anda.
    - Pilih **Resource group** yang akan digunakan.
    - Pilih **Role** menjadi **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d1d62333e91b4d2719284f0dad14bd9b4c3459510a0c44fab.id.png)

2. Pilih **Save**.

#### Menambahkan penugasan peran Storage Blob Data Reader ke Managed Identity

1. Ketik *storage accounts* di **bilah pencarian** di bagian atas halaman portal dan pilih **Storage accounts** dari opsi yang muncul.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e55b6b4dda10841d74d1c7463a2e4f23b9c45ffbb84219deb2.id.png)

1. Pilih storage account yang terkait dengan Azure Machine Learning workspace yang Anda buat. Misalnya, *finetunephistorage*.

1. Lakukan langkah berikut untuk menuju halaman Add role assignment:

    - Navigasikan ke Azure Storage account yang Anda buat.
    - Pilih **Access Control (IAM)** dari tab sebelah kiri.
    - Pilih **+ Add** dari menu navigasi.
    - Pilih **Add role assignment** dari menu navigasi.

    ![Add role.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c25fb73e63b957e214a2b651375a640a3aa54159a3731f495b.id.png)

1. Di halaman Add role assignment, lakukan tugas berikut:

    - Di halaman Role, ketik *Storage Blob Data Reader* di **bilah pencarian** dan pilih **Storage Blob Data Reader** dari opsi yang muncul.
    - Di halaman Role, pilih **Next**.
    - Di halaman Members, pilih **Assign access to** **Managed identity**.
    - Di halaman Members, pilih **+ Select members**.
    - Di halaman Select managed identities, pilih **Subscription** Azure Anda.
    - Di halaman Select managed identities, pilih **Managed identity** ke **Manage Identity**.
    - Di halaman Select managed identities, pilih Managed Identity yang Anda buat. Misalnya, *finetunephi-managedidentity*.
    - Di halaman Select managed identities, pilih **Select**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25289f2f121da05d114934d21d26aae9cb779334cbbccdf9e8.id.png)

1. Pilih **Review + assign**.

#### Menambahkan penugasan peran AcrPull ke Managed Identity

1. Ketik *container registries* di **bilah pencarian** di bagian atas halaman portal dan pilih **Container registries** dari opsi yang muncul.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a69b003f7a698dac908ffc2f355e675c10939fdd0bb09f790e.id.png)

1. Pilih container registry yang terkait dengan Azure Machine Learning workspace. Misalnya, *finetunephicontainerregistry*

1. Lakukan langkah berikut untuk menuju halaman Add role assignment:

    - Pilih **Access Control (IAM)** dari tab sebelah kiri.
    - Pilih **+ Add** dari menu navigasi.
    - Pilih **Add role assignment** dari menu navigasi.

1. Di halaman Add role assignment, lakukan tugas berikut:

    - Di halaman Role, ketik *AcrPull* di **bilah pencarian** dan pilih **AcrPull** dari opsi yang muncul.
    - Di halaman Role, pilih **Next**.
    - Di halaman Members, pilih **Assign access to** **Managed identity**.
    - Di halaman Members, pilih **+ Select members**.
    - Di halaman Select managed identities, pilih **Subscription** Azure Anda.
    - Di halaman Select managed identities, pilih **Managed identity** ke **Manage Identity**.
    - Di halaman Select managed identities, pilih Managed Identity yang Anda buat. Misalnya, *finetunephi-managedidentity*.
    - Di halaman Select managed identities, pilih **Select**.
    - Pilih **Review + assign**.

### Menyiapkan proyek

Untuk mengunduh dataset yang dibutuhkan untuk fine-tuning, Anda akan menyiapkan lingkungan lokal.

Dalam latihan ini, Anda akan

- Membuat folder untuk bekerja di dalamnya.
- Membuat virtual environment.
- Menginstal paket yang dibutuhkan.
- Membuat file *download_dataset.py* untuk mengunduh dataset.

#### Membuat folder untuk bekerja di dalamnya

1. Buka jendela terminal dan ketik perintah berikut untuk membuat folder bernama *finetune-phi* di path default.

    ```console
    mkdir finetune-phi
    ```

2. Ketik perintah berikut di terminal Anda untuk masuk ke folder *finetune-phi* yang sudah Anda buat.
#### Buat lingkungan virtual

1. Ketik perintah berikut di terminal Anda untuk membuat lingkungan virtual bernama *.venv*.

    ```console
    python -m venv .venv
    ```

2. Ketik perintah berikut di terminal Anda untuk mengaktifkan lingkungan virtual.

    ```console
    .venv\Scripts\activate.bat
    ```


> [!NOTE]
> Jika berhasil, Anda akan melihat *(.venv)* sebelum prompt perintah.

#### Instal paket yang dibutuhkan

1. Ketik perintah berikut di terminal Anda untuk menginstal paket yang dibutuhkan.

    ```console
    pip install datasets==2.19.1
    ```

#### Buat `download_dataset.py`

> [!NOTE]
> Struktur folder lengkap:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Buka **Visual Studio Code**.

1. Pilih **File** dari menu bar.

1. Pilih **Open Folder**.

1. Pilih folder *finetune-phi* yang sudah Anda buat, yang terletak di *C:\Users\yourUserName\finetune-phi*.

    ![Pilih folder yang sudah Anda buat.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6f63a0a50961e51a39cc6de7a7ddc86da5f4896e815f28abd.id.png)

1. Di panel kiri Visual Studio Code, klik kanan dan pilih **New File** untuk membuat file baru bernama *download_dataset.py*.

    ![Buat file baru.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff927ede875300e1b5c91ab90d1e486c77a43bb9494880cf9b6f.id.png)

### Siapkan dataset untuk fine-tuning

Dalam latihan ini, Anda akan menjalankan file *download_dataset.py* untuk mengunduh dataset *ultrachat_200k* ke lingkungan lokal Anda. Dataset ini kemudian akan digunakan untuk melakukan fine-tuning model Phi-3 di Azure Machine Learning.

Dalam latihan ini, Anda akan:

- Menambahkan kode ke file *download_dataset.py* untuk mengunduh dataset.
- Menjalankan file *download_dataset.py* untuk mengunduh dataset ke lingkungan lokal Anda.

#### Unduh dataset menggunakan *download_dataset.py*

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
        # Load the dataset with the specified name, configuration, and split ratio
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Split the dataset into train and test sets (80% train, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Create the directory if it does not exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Open the file in write mode
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterate over each record in the dataset
            for record in dataset:
                # Dump the record as a JSON object and write it to the file
                json.dump(record, f)
                # Write a newline character to separate records
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Load and split the ULTRACHAT_200k dataset with a specific configuration and split ratio
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extract the train and test datasets from the split
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Save the train dataset to a JSONL file
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Ketik perintah berikut di terminal Anda untuk menjalankan skrip dan mengunduh dataset ke lingkungan lokal.

    ```console
    python download_dataset.py
    ```

1. Pastikan dataset berhasil disimpan di direktori lokal *finetune-phi/data* Anda.

> [!NOTE]
>
> #### Catatan tentang ukuran dataset dan waktu fine-tuning
>
> Dalam tutorial ini, Anda hanya menggunakan 1% dari dataset (`split='train[:1%]'`). Ini secara signifikan mengurangi jumlah data, mempercepat proses upload dan fine-tuning. Anda dapat menyesuaikan persentase ini untuk menemukan keseimbangan yang tepat antara waktu pelatihan dan performa model. Menggunakan subset dataset yang lebih kecil mengurangi waktu yang dibutuhkan untuk fine-tuning, sehingga proses ini lebih mudah dikelola dalam tutorial.

## Skenario 2: Fine-tune model Phi-3 dan Deploy di Azure Machine Learning Studio

### Fine-tune model Phi-3

Dalam latihan ini, Anda akan melakukan fine-tuning model Phi-3 di Azure Machine Learning Studio.

Dalam latihan ini, Anda akan:

- Membuat cluster komputer untuk fine-tuning.
- Melakukan fine-tuning model Phi-3 di Azure Machine Learning Studio.

#### Buat cluster komputer untuk fine-tuning

1. Kunjungi [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pilih **Compute** dari tab sebelah kiri.

1. Pilih **Compute clusters** dari menu navigasi.

1. Pilih **+ New**.

    ![Pilih compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252d04ffd0142c073486df7d3b7256335964a98b87e28072523.id.png)

1. Lakukan langkah berikut:

    - Pilih **Region** yang ingin Anda gunakan.
    - Pilih **Virtual machine tier** menjadi **Dedicated**.
    - Pilih **Virtual machine type** menjadi **GPU**.
    - Pilih filter **Virtual machine size** ke **Select from all options**.
    - Pilih **Virtual machine size** menjadi **Standard_NC24ads_A100_v4**.

    ![Buat cluster.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e4baa9c5ccf86510f21df87515c231b2a255e1ee545496458.id.png)

1. Pilih **Next**.

1. Lakukan langkah berikut:

    - Masukkan **Compute name**. Harus unik.
    - Pilih **Minimum number of nodes** menjadi **0**.
    - Pilih **Maximum number of nodes** menjadi **1**.
    - Pilih **Idle seconds before scale down** menjadi **120**.

    ![Buat cluster.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662edc0f95ad364a869b4dbb7f7be08ff259528fea96312e77e.id.png)

1. Pilih **Create**.

#### Fine-tune model Phi-3

1. Kunjungi [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pilih workspace Azure Machine Learning yang sudah Anda buat.

    ![Pilih workspace yang sudah Anda buat.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.id.png)

1. Lakukan langkah berikut:

    - Pilih **Model catalog** dari tab sebelah kiri.
    - Ketik *phi-3-mini-4k* di **search bar** dan pilih **Phi-3-mini-4k-instruct** dari opsi yang muncul.

    ![Ketik phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b25018a7e7353ce6525d8f5803b0af9bc9a60a9be4204dd77578.id.png)

1. Pilih **Fine-tune** dari menu navigasi.

    ![Pilih fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeecb897ac74882792b59086893b8a7448a89be3628aee62fc1b.id.png)

1. Lakukan langkah berikut:

    - Pilih **Select task type** menjadi **Chat completion**.
    - Pilih **+ Select data** untuk mengunggah **Training data**.
    - Pilih tipe unggahan Validation data menjadi **Provide different validation data**.
    - Pilih **+ Select data** untuk mengunggah **Validation data**.

    ![Isi halaman fine-tuning.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0bbc6b248af9e7369ca98379770badec9f73b6bced7a8b7806.id.png)

    > [!TIP]
    >
    > Anda dapat memilih **Advanced settings** untuk menyesuaikan konfigurasi seperti **learning_rate** dan **lr_scheduler_type** agar proses fine-tuning lebih optimal sesuai kebutuhan Anda.

1. Pilih **Finish**.

1. Dalam latihan ini, Anda berhasil melakukan fine-tuning model Phi-3 menggunakan Azure Machine Learning. Perlu diingat bahwa proses fine-tuning bisa memakan waktu cukup lama. Setelah menjalankan pekerjaan fine-tuning, Anda harus menunggu hingga selesai. Anda dapat memantau status pekerjaan fine-tuning dengan membuka tab Jobs di sebelah kiri workspace Azure Machine Learning Anda. Pada seri berikutnya, Anda akan melakukan deploy model yang sudah di-fine-tune dan mengintegrasikannya dengan Prompt flow.

    ![Lihat pekerjaan fine-tuning.](../../../../../../translated_images/06-08-output.2bd32e59930672b1cc1de86056e2fbc91e338f59e2a29d7dac86ede49a9714b2.id.png)

### Deploy model Phi-3 yang sudah di-fine-tune

Untuk mengintegrasikan model Phi-3 yang sudah di-fine-tune dengan Prompt flow, Anda perlu melakukan deploy model agar dapat diakses untuk inferensi secara real-time. Proses ini meliputi pendaftaran model, pembuatan endpoint online, dan deploy model.

Dalam latihan ini, Anda akan:

- Mendaftarkan model yang sudah di-fine-tune di workspace Azure Machine Learning.
- Membuat endpoint online.
- Melakukan deploy model Phi-3 yang sudah didaftarkan.

#### Daftarkan model yang sudah di-fine-tune

1. Kunjungi [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pilih workspace Azure Machine Learning yang sudah Anda buat.

    ![Pilih workspace yang sudah Anda buat.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.id.png)

1. Pilih **Models** dari tab sebelah kiri.

1. Pilih **+ Register**.

1. Pilih **From a job output**.

    ![Daftarkan model.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777c8c39906ce5cd57f16b54fb3887dd4e4de1ce963b26499ad.id.png)

1. Pilih pekerjaan (job) yang sudah Anda buat.

    ![Pilih job.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd09315953b4eb2cc9d62d0d77ab0d9d877e34c6827fa6d2b6be4.id.png)

1. Pilih **Next**.

1. Pilih **Model type** menjadi **MLflow**.

1. Pastikan **Job output** sudah terpilih; biasanya sudah otomatis terpilih.

    ![Pilih output.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f267b40f73de77f092a5b02808ade72f8eb94e5fe9723feb3.id.png)

2. Pilih **Next**.

3. Pilih **Register**.

    ![Pilih register.](../../../../../../translated_images/07-04-register.fd82a3b293060bc78399e613293032d3d301c02a6fd8092bec52bfaf4f3104de.id.png)

4. Anda dapat melihat model yang sudah didaftarkan dengan membuka menu **Models** dari tab sebelah kiri.

    ![Model yang sudah didaftarkan.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591b7995686b95396ffd8c185ba66f0a1f6be18f4aea05e93d5.id.png)

#### Deploy model yang sudah di-fine-tune

1. Buka workspace Azure Machine Learning yang sudah Anda buat.

1. Pilih **Endpoints** dari tab sebelah kiri.

1. Pilih **Real-time endpoints** dari menu navigasi.

    ![Buat endpoint.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09618ce29b467276523838b8cc766d79ebfecdb052fef2c4df.id.png)

1. Pilih **Create**.

1. Pilih model yang sudah Anda daftarkan.

    ![Pilih model yang sudah didaftarkan.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4460f7646dfaa59121fb1384ed1957755427d358462c25225.id.png)

1. Pilih **Select**.

1. Lakukan langkah berikut:

    - Pilih **Virtual machine** menjadi *Standard_NC6s_v3*.
    - Pilih **Instance count** sesuai kebutuhan Anda, misalnya *1*.
    - Pilih **Endpoint** menjadi **New** untuk membuat endpoint baru.
    - Masukkan **Endpoint name**. Harus unik.
    - Masukkan **Deployment name**. Harus unik.

    ![Isi pengaturan deployment.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e67378494bb8d81418bc3bdaceb8c57151727d538594cb378697f36.id.png)

1. Pilih **Deploy**.

> [!WARNING]
> Untuk menghindari biaya tambahan, pastikan untuk menghapus endpoint yang sudah dibuat di workspace Azure Machine Learning setelah selesai digunakan.
>

#### Cek status deployment di Azure Machine Learning Workspace

1. Buka workspace Azure Machine Learning yang sudah Anda buat.

1. Pilih **Endpoints** dari tab sebelah kiri.

1. Pilih endpoint yang sudah Anda buat.

    ![Pilih endpoints](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4a302f0efc8875002e1c382167083c7fefbdb42ede274d0da.id.png)

1. Di halaman ini, Anda dapat mengelola endpoint selama proses deployment.

> [!NOTE]
> Setelah deployment selesai, pastikan **Live traffic** diatur ke **100%**. Jika belum, pilih **Update traffic** untuk menyesuaikan pengaturan traffic. Perlu diketahui, Anda tidak dapat menguji model jika traffic diatur ke 0%.
>
> ![Atur traffic.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d30c64ecabac4b17a7b5dc004ba52ad387cbaaf7b266eeadf.id.png)
>

## Skenario 3: Integrasi dengan Prompt flow dan Chat dengan model kustom Anda di Azure AI Foundry

### Integrasikan model Phi-3 kustom dengan Prompt flow

Setelah berhasil melakukan deploy model yang sudah di-fine-tune, sekarang Anda dapat mengintegrasikannya dengan Prompt Flow untuk menggunakan model Anda dalam aplikasi real-time, memungkinkan berbagai tugas interaktif dengan model Phi-3 kustom Anda.

Dalam latihan ini, Anda akan:

- Membuat Azure AI Foundry Hub.
- Membuat Azure AI Foundry Project.
- Membuat Prompt flow.
- Menambahkan koneksi kustom untuk model Phi-3 yang sudah di-fine-tune.
- Mengatur Prompt flow untuk chat dengan model Phi-3 kustom Anda.
> [!NOTE]  
> Anda juga dapat mengintegrasikan dengan Promptflow menggunakan Azure ML Studio. Proses integrasi yang sama dapat diterapkan pada Azure ML Studio.
#### Membuat Azure AI Foundry Hub

Anda perlu membuat Hub sebelum membuat Proyek. Hub berfungsi seperti Resource Group, memungkinkan Anda mengatur dan mengelola beberapa Proyek dalam Azure AI Foundry.

1. Kunjungi [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Pilih **All hubs** dari tab sisi kiri.

1. Pilih **+ New hub** dari menu navigasi.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834e092dcf9dda773276fbee65f40252ed4a9af4f9aa4fef5d7.id.png)

1. Lakukan tugas berikut:

    - Masukkan **Hub name**. Nilainya harus unik.
    - Pilih **Subscription** Azure Anda.
    - Pilih **Resource group** yang akan digunakan (buat baru jika perlu).
    - Pilih **Location** yang ingin Anda gunakan.
    - Pilih **Connect Azure AI Services** yang akan digunakan (buat baru jika perlu).
    - Pilih **Connect Azure AI Search** ke **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c44658a87c2ed01d9e588581f157480ff1ac3312085c51d25.id.png)

1. Pilih **Next**.

#### Membuat Proyek Azure AI Foundry

1. Di Hub yang Anda buat, pilih **All projects** dari tab sisi kiri.

1. Pilih **+ New project** dari menu navigasi.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f1251c487d98aed0641bd057100b8e5d6fba9062bfb7d752ce9.id.png)

1. Masukkan **Project name**. Nilainya harus unik.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a192b4ed3dde6b1136c860fc85352d612aa2f3ae8a4d54eb4.id.png)

1. Pilih **Create a project**.

#### Menambahkan koneksi kustom untuk model Phi-3 yang sudah di-fine-tune

Untuk mengintegrasikan model Phi-3 kustom Anda dengan Prompt flow, Anda perlu menyimpan endpoint dan kunci model dalam koneksi kustom. Pengaturan ini memastikan akses ke model Phi-3 kustom Anda di Prompt flow.

#### Mengatur api key dan endpoint uri dari model Phi-3 yang sudah di-fine-tune

1. Kunjungi [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Navigasikan ke workspace Azure Machine learning yang Anda buat.

1. Pilih **Endpoints** dari tab sisi kiri.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf960519c1ac95116d1a7e5b8d0bdea5cd42281930766fbfad1929.id.png)

1. Pilih endpoint yang Anda buat.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275ea16f689f59b70d5b0162fff1781204e389edcb63b42b95b2.id.png)

1. Pilih **Consume** dari menu navigasi.

1. Salin **REST endpoint** dan **Primary key** Anda.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cbe30a20b889154d04109bf17c5c09816060a8689933dc0fd7.id.png)

#### Menambahkan Koneksi Kustom

1. Kunjungi [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Navigasikan ke proyek Azure AI Foundry yang Anda buat.

1. Di Proyek yang Anda buat, pilih **Settings** dari tab sisi kiri.

1. Pilih **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc77130c3a16fbb8ee59407ecbf74fd3502cb8720c61384446.id.png)

1. Pilih **Custom keys** dari menu navigasi.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b29664605513ccc134f1adaefaf27f951981c511783a6a0d1118c9178a5.id.png)

1. Lakukan tugas berikut:

    - Pilih **+ Add key value pairs**.
    - Untuk nama kunci, masukkan **endpoint** dan tempel endpoint yang Anda salin dari Azure ML Studio ke kolom nilai.
    - Pilih **+ Add key value pairs** lagi.
    - Untuk nama kunci, masukkan **key** dan tempel kunci yang Anda salin dari Azure ML Studio ke kolom nilai.
    - Setelah menambahkan kunci, pilih **is secret** untuk mencegah kunci terekspos.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26e8df1bbd0948e06aa20aa0dc102faa96c8144722ef7f0b72.id.png)

1. Pilih **Add connection**.

#### Membuat Prompt flow

Anda telah menambahkan koneksi kustom di Azure AI Foundry. Sekarang, mari buat Prompt flow dengan langkah-langkah berikut. Kemudian, Anda akan menghubungkan Prompt flow ini ke koneksi kustom agar dapat menggunakan model yang sudah di-fine-tune dalam Prompt flow.

1. Navigasikan ke proyek Azure AI Foundry yang Anda buat.

1. Pilih **Prompt flow** dari tab sisi kiri.

1. Pilih **+ Create** dari menu navigasi.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5ba79bedfd35e2f2fb430f344844994375680fcfc111a994ae.id.png)

1. Pilih **Chat flow** dari menu navigasi.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591f6cc6360bc35c8fca8d63519c09111c6c431de9b46eed143.id.png)

1. Masukkan **Folder name** yang akan digunakan.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d824bad779a54e55d808a09394b6b730fbea55d78421f52ff.id.png)

2. Pilih **Create**.

#### Mengatur Prompt flow untuk mengobrol dengan model Phi-3 kustom Anda

Anda perlu mengintegrasikan model Phi-3 yang sudah di-fine-tune ke dalam Prompt flow. Namun, Prompt flow yang ada saat ini tidak dirancang untuk tujuan ini. Oleh karena itu, Anda harus mendesain ulang Prompt flow agar dapat mengintegrasikan model kustom tersebut.

1. Di Prompt flow, lakukan tugas berikut untuk membangun ulang flow yang ada:

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

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985b76e070bf170e1d0d0d26b38d93bc635624642191f715a6d.id.png)

1. Tambahkan kode berikut ke file *integrate_with_promptflow.py* untuk menggunakan model Phi-3 kustom di Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
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

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
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
            
            # Log the full JSON response
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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d097779ab1c429be9fc07e3f4171e41fbbfb747a6e755816411e6d.id.png)

> [!NOTE]
> Untuk informasi lebih rinci tentang menggunakan Prompt flow di Azure AI Foundry, Anda dapat merujuk ke [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Pilih **Chat input**, **Chat output** untuk mengaktifkan fitur obrolan dengan model Anda.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03ba022a21159e51d544c6e063e73c10e772c942d4e44da0d30.id.png)

1. Sekarang Anda siap untuk mengobrol dengan model Phi-3 kustom Anda. Pada latihan berikutnya, Anda akan belajar cara memulai Prompt flow dan menggunakannya untuk mengobrol dengan model Phi-3 yang sudah di-fine-tune.

> [!NOTE]
>
> Flow yang dibangun ulang seharusnya terlihat seperti gambar di bawah ini:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c10b7375192511a8e2aba847e442b294a2e65d88ffac8f63b.id.png)
>

### Mengobrol dengan model Phi-3 kustom Anda

Setelah Anda melakukan fine-tuning dan mengintegrasikan model Phi-3 kustom Anda dengan Prompt flow, Anda siap untuk mulai berinteraksi dengannya. Latihan ini akan memandu Anda melalui proses pengaturan dan memulai obrolan dengan model menggunakan Prompt flow. Dengan mengikuti langkah-langkah ini, Anda dapat memanfaatkan sepenuhnya kemampuan model Phi-3 yang sudah di-fine-tune untuk berbagai tugas dan percakapan.

- Mengobrol dengan model Phi-3 kustom Anda menggunakan Prompt flow.

#### Memulai Prompt flow

1. Pilih **Start compute sessions** untuk memulai Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b4809b60d75ce9b0ad53e0729cc1449935ccbe90b954401dc.id.png)

1. Pilih **Validate and parse input** untuk memperbarui parameter.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e97038d7529b9060a23dc59d7ddbeb38ac9c4562ef4f5b32f7.id.png)

1. Pilih **Value** dari **connection** ke koneksi kustom yang Anda buat. Contohnya, *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b184402368a6ec383814b139686118331a5b2eefa489678902269dfc.id.png)

#### Mengobrol dengan model kustom Anda

1. Pilih **Chat**.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e636a5e1516b6c64fdf2345ceb3142db2bed93ab7e6f03bbb2.id.png)

1. Berikut contoh hasilnya: Sekarang Anda dapat mengobrol dengan model Phi-3 kustom Anda. Disarankan untuk mengajukan pertanyaan berdasarkan data yang digunakan untuk fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126fa4886e6fd0e7482cfdc6c907fa36f7f2f13d04126f9eda14.id.png)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.