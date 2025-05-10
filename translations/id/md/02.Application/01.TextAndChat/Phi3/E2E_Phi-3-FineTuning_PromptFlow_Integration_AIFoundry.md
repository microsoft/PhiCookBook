<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-05-09T18:16:40+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "id"
}
-->
# Fine-tune dan Integrasikan model Phi-3 kustom dengan Prompt flow di Azure AI Foundry

Contoh end-to-end (E2E) ini berdasarkan panduan "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" dari Microsoft Tech Community. Panduan ini memperkenalkan proses fine-tuning, deployment, dan integrasi model Phi-3 kustom dengan Prompt flow di Azure AI Foundry.  
Berbeda dengan contoh E2E, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", yang melibatkan eksekusi kode secara lokal, tutorial ini sepenuhnya fokus pada fine-tuning dan integrasi model Anda dalam Azure AI / ML Studio.

## Ikhtisar

Dalam contoh E2E ini, Anda akan mempelajari cara melakukan fine-tuning model Phi-3 dan mengintegrasikannya dengan Prompt flow di Azure AI Foundry. Dengan memanfaatkan Azure AI / ML Studio, Anda akan membangun alur kerja untuk deployment dan penggunaan model AI kustom. Contoh E2E ini dibagi menjadi tiga skenario:

**Skenario 1: Menyiapkan sumber daya Azure dan Mempersiapkan fine-tuning**

**Skenario 2: Fine-tune model Phi-3 dan Deploy di Azure Machine Learning Studio**

**Skenario 3: Integrasi dengan Prompt flow dan Chat dengan model kustom Anda di Azure AI Foundry**

Berikut adalah gambaran umum dari contoh E2E ini.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.id.png)

### Daftar Isi

1. **[Skenario 1: Menyiapkan sumber daya Azure dan Mempersiapkan fine-tuning](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Membuat Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Meminta kuota GPU di Azure Subscription](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Menambahkan penugasan peran](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Menyiapkan proyek](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Mempersiapkan dataset untuk fine-tuning](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Skenario 2: Fine-tune model Phi-3 dan Deploy di Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Fine-tune model Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Deploy model Phi-3 yang sudah di fine-tune](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Skenario 3: Integrasi dengan Prompt flow dan Chat dengan model kustom Anda di Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrasikan model Phi-3 kustom dengan Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Chat dengan model Phi-3 kustom Anda](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Skenario 1: Menyiapkan sumber daya Azure dan Mempersiapkan fine-tuning

### Membuat Azure Machine Learning Workspace

1. Ketik *azure machine learning* di **bar pencarian** di bagian atas halaman portal dan pilih **Azure Machine Learning** dari opsi yang muncul.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.id.png)

2. Pilih **+ Create** dari menu navigasi.

3. Pilih **New workspace** dari menu navigasi.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.id.png)

4. Lakukan tugas berikut:

    - Pilih **Subscription** Azure Anda.
    - Pilih **Resource group** yang akan digunakan (buat yang baru jika perlu).
    - Masukkan **Workspace Name**. Harus bernilai unik.
    - Pilih **Region** yang ingin Anda gunakan.
    - Pilih **Storage account** yang akan digunakan (buat yang baru jika perlu).
    - Pilih **Key vault** yang akan digunakan (buat yang baru jika perlu).
    - Pilih **Application insights** yang akan digunakan (buat yang baru jika perlu).
    - Pilih **Container registry** yang akan digunakan (buat yang baru jika perlu).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.id.png)

5. Pilih **Review + Create**.

6. Pilih **Create**.

### Meminta kuota GPU di Azure Subscription

Dalam tutorial ini, Anda akan mempelajari cara melakukan fine-tuning dan deployment model Phi-3 menggunakan GPU. Untuk fine-tuning, Anda akan menggunakan GPU *Standard_NC24ads_A100_v4*, yang memerlukan permintaan kuota. Untuk deployment, Anda akan menggunakan GPU *Standard_NC6s_v3*, yang juga memerlukan permintaan kuota.

> [!NOTE]
>
> Hanya subscription Pay-As-You-Go (tipe subscription standar) yang berhak mendapatkan alokasi GPU; subscription benefit saat ini belum didukung.
>

1. Kunjungi [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Lakukan langkah berikut untuk meminta kuota *Standard NCADSA100v4 Family*:

    - Pilih **Quota** dari tab sebelah kiri.
    - Pilih **Virtual machine family** yang akan digunakan. Contohnya, pilih **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, yang mencakup GPU *Standard_NC24ads_A100_v4*.
    - Pilih **Request quota** dari menu navigasi.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.id.png)

    - Di halaman Request quota, masukkan **New cores limit** yang ingin Anda gunakan. Contohnya, 24.
    - Di halaman Request quota, pilih **Submit** untuk mengajukan permintaan kuota GPU.

1. Lakukan langkah berikut untuk meminta kuota *Standard NCSv3 Family*:

    - Pilih **Quota** dari tab sebelah kiri.
    - Pilih **Virtual machine family** yang akan digunakan. Contohnya, pilih **Standard NCSv3 Family Cluster Dedicated vCPUs**, yang mencakup GPU *Standard_NC6s_v3*.
    - Pilih **Request quota** dari menu navigasi.
    - Di halaman Request quota, masukkan **New cores limit** yang ingin Anda gunakan. Contohnya, 24.
    - Di halaman Request quota, pilih **Submit** untuk mengajukan permintaan kuota GPU.

### Menambahkan penugasan peran

Untuk melakukan fine-tuning dan deployment model Anda, Anda harus terlebih dahulu membuat User Assigned Managed Identity (UAI) dan memberikan izin yang sesuai. UAI ini akan digunakan untuk autentikasi selama proses deployment.

#### Membuat User Assigned Managed Identity (UAI)

1. Ketik *managed identities* di **bar pencarian** di bagian atas halaman portal dan pilih **Managed Identities** dari opsi yang muncul.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.id.png)

1. Pilih **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.id.png)

1. Lakukan tugas berikut:

    - Pilih **Subscription** Azure Anda.
    - Pilih **Resource group** yang akan digunakan (buat yang baru jika perlu).
    - Pilih **Region** yang ingin Anda gunakan.
    - Masukkan **Name**. Harus bernilai unik.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.id.png)

1. Pilih **Review + create**.

1. Pilih **+ Create**.

#### Menambahkan penugasan peran Contributor ke Managed Identity

1. Navigasikan ke sumber daya Managed Identity yang sudah Anda buat.

1. Pilih **Azure role assignments** dari tab sebelah kiri.

1. Pilih **+Add role assignment** dari menu navigasi.

1. Di halaman Add role assignment, lakukan tugas berikut:
    - Pilih **Scope** menjadi **Resource group**.
    - Pilih **Subscription** Azure Anda.
    - Pilih **Resource group** yang akan digunakan.
    - Pilih **Role** menjadi **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.id.png)

2. Pilih **Save**.

#### Menambahkan penugasan peran Storage Blob Data Reader ke Managed Identity

1. Ketik *storage accounts* di **bar pencarian** di bagian atas halaman portal dan pilih **Storage accounts** dari opsi yang muncul.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.id.png)

1. Pilih storage account yang terkait dengan Azure Machine Learning workspace yang sudah Anda buat. Contohnya, *finetunephistorage*.

1. Lakukan langkah berikut untuk membuka halaman Add role assignment:

    - Navigasikan ke Azure Storage account yang Anda buat.
    - Pilih **Access Control (IAM)** dari tab sebelah kiri.
    - Pilih **+ Add** dari menu navigasi.
    - Pilih **Add role assignment** dari menu navigasi.

    ![Add role.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.id.png)

1. Di halaman Add role assignment, lakukan tugas berikut:

    - Di halaman Role, ketik *Storage Blob Data Reader* di **bar pencarian** dan pilih **Storage Blob Data Reader** dari opsi yang muncul.
    - Di halaman Role, pilih **Next**.
    - Di halaman Members, pilih **Assign access to** menjadi **Managed identity**.
    - Di halaman Members, pilih **+ Select members**.
    - Di halaman Select managed identities, pilih **Subscription** Azure Anda.
    - Di halaman Select managed identities, pilih **Managed identity** menjadi **Manage Identity**.
    - Di halaman Select managed identities, pilih Manage Identity yang sudah Anda buat. Contohnya, *finetunephi-managedidentity*.
    - Di halaman Select managed identities, pilih **Select**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.id.png)

1. Pilih **Review + assign**.

#### Menambahkan penugasan peran AcrPull ke Managed Identity

1. Ketik *container registries* di **bar pencarian** di bagian atas halaman portal dan pilih **Container registries** dari opsi yang muncul.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.id.png)

1. Pilih container registry yang terkait dengan Azure Machine Learning workspace. Contohnya, *finetunephicontainerregistry*

1. Lakukan langkah berikut untuk membuka halaman Add role assignment:

    - Pilih **Access Control (IAM)** dari tab sebelah kiri.
    - Pilih **+ Add** dari menu navigasi.
    - Pilih **Add role assignment** dari menu navigasi.

1. Di halaman Add role assignment, lakukan tugas berikut:

    - Di halaman Role, ketik *AcrPull* di **bar pencarian** dan pilih **AcrPull** dari opsi yang muncul.
    - Di halaman Role, pilih **Next**.
    - Di halaman Members, pilih **Assign access to** menjadi **Managed identity**.
    - Di halaman Members, pilih **+ Select members**.
    - Di halaman Select managed identities, pilih **Subscription** Azure Anda.
    - Di halaman Select managed identities, pilih **Managed identity** menjadi **Manage Identity**.
    - Di halaman Select managed identities, pilih Manage Identity yang sudah Anda buat. Contohnya, *finetunephi-managedidentity*.
    - Di halaman Select managed identities, pilih **Select**.
    - Pilih **Review + assign**.

### Menyiapkan proyek

Untuk mengunduh dataset yang dibutuhkan untuk fine-tuning, Anda akan menyiapkan lingkungan lokal.

Dalam latihan ini, Anda akan:

- Membuat folder kerja.
- Membuat virtual environment.
- Menginstal paket yang diperlukan.
- Membuat file *download_dataset.py* untuk mengunduh dataset.

#### Membuat folder kerja

1. Buka terminal dan ketik perintah berikut untuk membuat folder bernama *finetune-phi* di jalur default.

    ```console
    mkdir finetune-phi
    ```

2. Ketik perintah berikut di terminal untuk masuk ke folder *finetune-phi* yang sudah dibuat.

    ```console
    cd finetune-phi
    ```

#### Membuat virtual environment

1. Ketik perintah berikut di terminal untuk membuat virtual environment bernama *.venv*.

    ```console
    python -m venv .venv
    ```

2. Ketik perintah berikut di terminal untuk mengaktifkan virtual environment.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Jika berhasil, Anda akan melihat *(.venv)* sebelum prompt perintah.

#### Menginstal paket yang diperlukan

1. Ketik perintah berikut di terminal untuk menginstal paket yang diperlukan.

    ```console
    pip install datasets==2.19.1
    ```

#### Membuat `download_dataset.py`

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

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.id.png)

1. Di panel kiri Visual Studio Code, klik kanan dan pilih **New File** untuk membuat file baru bernama *download_dataset.py*.

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.id.png)

### Mempersiapkan dataset untuk fine-tuning

Dalam latihan ini, Anda akan menjalankan file *download_dataset.py* untuk mengunduh dataset *ultrachat_200k* ke lingkungan lokal Anda. Dataset ini kemudian akan digunakan untuk fine-tuning model Phi-3 di Azure Machine Learning.

Dalam latihan ini, Anda akan:

- Menambahkan kode ke file *download_dataset.py* untuk mengunduh dataset.
- Menjalankan file *download_dataset.py* untuk mengunduh dataset ke lingkungan lokal Anda.

#### Mengunduh dataset menggunakan *download_dataset.py*

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

1. Ketik perintah berikut di terminal untuk menjalankan skrip dan mengunduh dataset ke lingkungan lokal Anda.

    ```console
    python download_dataset.py
    ```

1. Pastikan dataset berhasil tersimpan di direktori lokal *finetune-phi/data* Anda.

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

#### Membuat cluster komputer untuk fine-tuning
1. Kunjungi [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pilih **Compute** dari tab sisi kiri.

1. Pilih **Compute clusters** dari menu navigasi.

1. Pilih **+ New**.

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.id.png)

1. Lakukan tugas berikut:

    - Pilih **Region** yang ingin Anda gunakan.
    - Pilih **Virtual machine tier** ke **Dedicated**.
    - Pilih **Virtual machine type** ke **GPU**.
    - Pilih filter **Virtual machine size** ke **Select from all options**.
    - Pilih **Virtual machine size** ke **Standard_NC24ads_A100_v4**.

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.id.png)

1. Pilih **Next**.

1. Lakukan tugas berikut:

    - Masukkan **Compute name**. Harus bernilai unik.
    - Pilih **Minimum number of nodes** ke **0**.
    - Pilih **Maximum number of nodes** ke **1**.
    - Pilih **Idle seconds before scale down** ke **120**.

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.id.png)

1. Pilih **Create**.

#### Fine-tune model Phi-3

1. Kunjungi [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pilih Azure Machine Learning workspace yang sudah Anda buat.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.id.png)

1. Lakukan tugas berikut:

    - Pilih **Model catalog** dari tab sisi kiri.
    - Ketik *phi-3-mini-4k* di **search bar** dan pilih **Phi-3-mini-4k-instruct** dari opsi yang muncul.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.id.png)

1. Pilih **Fine-tune** dari menu navigasi.

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.id.png)

1. Lakukan tugas berikut:

    - Pilih **Select task type** ke **Chat completion**.
    - Pilih **+ Select data** untuk mengunggah **Training data**.
    - Pilih tipe unggah Validation data ke **Provide different validation data**.
    - Pilih **+ Select data** untuk mengunggah **Validation data**.

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.id.png)

    > [!TIP]
    >
    > Anda dapat memilih **Advanced settings** untuk mengatur konfigurasi seperti **learning_rate** dan **lr_scheduler_type** agar proses fine-tuning lebih optimal sesuai kebutuhan Anda.

1. Pilih **Finish**.

1. Dalam latihan ini, Anda berhasil melakukan fine-tuning model Phi-3 menggunakan Azure Machine Learning. Harap diperhatikan bahwa proses fine-tuning bisa memakan waktu cukup lama. Setelah menjalankan pekerjaan fine-tuning, Anda perlu menunggu hingga selesai. Anda dapat memantau status pekerjaan fine-tuning dengan membuka tab Jobs di sisi kiri Azure Machine Learning Workspace Anda. Pada seri berikutnya, Anda akan melakukan deployment model yang sudah di-fine-tune dan mengintegrasikannya dengan Prompt flow.

    ![See finetuning job.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.id.png)

### Deploy model Phi-3 yang sudah di-fine-tune

Untuk mengintegrasikan model Phi-3 yang sudah di-fine-tune dengan Prompt flow, Anda perlu melakukan deployment model agar dapat diakses untuk inferensi secara real-time. Proses ini meliputi pendaftaran model, pembuatan endpoint online, dan deployment model.

Dalam latihan ini, Anda akan:

- Mendaftarkan model yang sudah di-fine-tune di Azure Machine Learning workspace.
- Membuat endpoint online.
- Melakukan deployment model Phi-3 yang sudah terdaftar dan di-fine-tune.

#### Mendaftarkan model yang sudah di-fine-tune

1. Kunjungi [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pilih Azure Machine Learning workspace yang sudah Anda buat.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.id.png)

1. Pilih **Models** dari tab sisi kiri.
1. Pilih **+ Register**.
1. Pilih **From a job output**.

    ![Register model.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.id.png)

1. Pilih pekerjaan (job) yang sudah Anda buat.

    ![Select job.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.id.png)

1. Pilih **Next**.

1. Pilih **Model type** ke **MLflow**.

1. Pastikan **Job output** sudah terpilih; ini biasanya terpilih otomatis.

    ![Select output.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.id.png)

2. Pilih **Next**.

3. Pilih **Register**.

    ![Select register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.id.png)

4. Anda dapat melihat model yang sudah terdaftar dengan membuka menu **Models** dari tab sisi kiri.

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.id.png)

#### Deploy model yang sudah di-fine-tune

1. Buka Azure Machine Learning workspace yang sudah Anda buat.

1. Pilih **Endpoints** dari tab sisi kiri.

1. Pilih **Real-time endpoints** dari menu navigasi.

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.id.png)

1. Pilih **Create**.

1. Pilih model yang sudah terdaftar yang Anda buat.

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.id.png)

1. Pilih **Select**.

1. Lakukan tugas berikut:

    - Pilih **Virtual machine** ke *Standard_NC6s_v3*.
    - Pilih **Instance count** yang ingin Anda gunakan. Misalnya, *1*.
    - Pilih **Endpoint** ke **New** untuk membuat endpoint baru.
    - Masukkan **Endpoint name**. Harus bernilai unik.
    - Masukkan **Deployment name**. Harus bernilai unik.

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.id.png)

1. Pilih **Deploy**.

> [!WARNING]
> Untuk menghindari biaya tambahan pada akun Anda, pastikan untuk menghapus endpoint yang sudah dibuat di Azure Machine Learning workspace.
>

#### Periksa status deployment di Azure Machine Learning Workspace

1. Buka Azure Machine Learning workspace yang sudah Anda buat.

1. Pilih **Endpoints** dari tab sisi kiri.

1. Pilih endpoint yang sudah Anda buat.

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.id.png)

1. Pada halaman ini, Anda dapat mengelola endpoint selama proses deployment.

> [!NOTE]
> Setelah deployment selesai, pastikan **Live traffic** diatur ke **100%**. Jika belum, pilih **Update traffic** untuk mengatur lalu lintas. Perlu dicatat bahwa Anda tidak bisa menguji model jika lalu lintas diatur ke 0%.
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.id.png)
>

## Skenario 3: Integrasi dengan Prompt flow dan Chat dengan model kustom Anda di Azure AI Foundry

### Integrasikan model Phi-3 kustom dengan Prompt flow

Setelah berhasil melakukan deployment model yang sudah di-fine-tune, sekarang Anda dapat mengintegrasikannya dengan Prompt Flow untuk menggunakan model Anda dalam aplikasi real-time, memungkinkan berbagai tugas interaktif dengan model Phi-3 kustom Anda.

Dalam latihan ini, Anda akan:

- Membuat Azure AI Foundry Hub.
- Membuat Azure AI Foundry Project.
- Membuat Prompt flow.
- Menambahkan koneksi kustom untuk model Phi-3 yang sudah di-fine-tune.
- Mengatur Prompt flow untuk chat dengan model Phi-3 kustom Anda.

> [!NOTE]
> Anda juga dapat mengintegrasikan dengan Promptflow menggunakan Azure ML Studio. Proses integrasi yang sama dapat diterapkan di Azure ML Studio.

#### Buat Azure AI Foundry Hub

Anda perlu membuat Hub sebelum membuat Project. Hub berfungsi seperti Resource Group, memungkinkan Anda mengatur dan mengelola beberapa Project dalam Azure AI Foundry.

1. Kunjungi [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Pilih **All hubs** dari tab sisi kiri.

1. Pilih **+ New hub** dari menu navigasi.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.id.png)

1. Lakukan tugas berikut:

    - Masukkan **Hub name**. Harus bernilai unik.
    - Pilih **Subscription** Azure Anda.
    - Pilih **Resource group** yang akan digunakan (buat baru jika perlu).
    - Pilih **Location** yang ingin digunakan.
    - Pilih **Connect Azure AI Services** yang akan digunakan (buat baru jika perlu).
    - Pilih **Connect Azure AI Search** ke **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.id.png)

1. Pilih **Next**.

#### Buat Azure AI Foundry Project

1. Di Hub yang sudah Anda buat, pilih **All projects** dari tab sisi kiri.

1. Pilih **+ New project** dari menu navigasi.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.id.png)

1. Masukkan **Project name**. Harus bernilai unik.

    ![Create project.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.id.png)

1. Pilih **Create a project**.

#### Tambahkan koneksi kustom untuk model Phi-3 yang sudah di-fine-tune

Untuk mengintegrasikan model Phi-3 kustom Anda dengan Prompt flow, Anda perlu menyimpan endpoint dan kunci model dalam koneksi kustom. Pengaturan ini memastikan akses ke model Phi-3 kustom Anda di Prompt flow.

#### Atur api key dan endpoint uri model Phi-3 yang sudah di-fine-tune

1. Kunjungi [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Buka Azure Machine Learning workspace yang sudah Anda buat.

1. Pilih **Endpoints** dari tab sisi kiri.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.id.png)

1. Pilih endpoint yang sudah Anda buat.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.id.png)

1. Pilih **Consume** dari menu navigasi.

1. Salin **REST endpoint** dan **Primary key** Anda.
![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.id.png)

#### Tambahkan Koneksi Kustom

1. Kunjungi [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Arahkan ke proyek Azure AI Foundry yang telah Anda buat.

1. Di proyek yang Anda buat, pilih **Settings** dari tab sebelah kiri.

1. Pilih **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.id.png)

1. Pilih **Custom keys** dari menu navigasi.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.id.png)

1. Lakukan tugas berikut:

    - Pilih **+ Add key value pairs**.
    - Untuk nama kunci, masukkan **endpoint** dan tempel endpoint yang Anda salin dari Azure ML Studio ke dalam kolom nilai.
    - Pilih **+ Add key value pairs** lagi.
    - Untuk nama kunci, masukkan **key** dan tempel key yang Anda salin dari Azure ML Studio ke dalam kolom nilai.
    - Setelah menambahkan kunci, pilih **is secret** untuk mencegah kunci terekspos.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.id.png)

1. Pilih **Add connection**.

#### Buat Prompt flow

Anda telah menambahkan koneksi kustom di Azure AI Foundry. Sekarang, mari buat Prompt flow dengan langkah-langkah berikut. Kemudian, Anda akan menghubungkan Prompt flow ini ke koneksi kustom agar bisa menggunakan model fine-tuned dalam Prompt flow.

1. Arahkan ke proyek Azure AI Foundry yang telah Anda buat.

1. Pilih **Prompt flow** dari tab sebelah kiri.

1. Pilih **+ Create** dari menu navigasi.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.id.png)

1. Pilih **Chat flow** dari menu navigasi.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.id.png)

1. Masukkan **Folder name** yang akan digunakan.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.id.png)

2. Pilih **Create**.

#### Siapkan Prompt flow untuk chat dengan model Phi-3 kustom Anda

Anda perlu mengintegrasikan model Phi-3 yang sudah di-fine-tune ke dalam Prompt flow. Namun, Prompt flow yang ada saat ini tidak dirancang untuk tujuan ini. Oleh karena itu, Anda harus mendesain ulang Prompt flow agar bisa mengintegrasikan model kustom tersebut.

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

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.id.png)

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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.id.png)

> [!NOTE]
> Untuk informasi lebih lengkap tentang penggunaan Prompt flow di Azure AI Foundry, Anda dapat merujuk ke [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Pilih **Chat input**, **Chat output** untuk mengaktifkan chat dengan model Anda.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.id.png)

1. Sekarang Anda siap untuk chat dengan model Phi-3 kustom Anda. Pada latihan berikutnya, Anda akan belajar cara memulai Prompt flow dan menggunakannya untuk chat dengan model Phi-3 yang sudah di-fine-tune.

> [!NOTE]
>
> Flow yang telah dibangun ulang seharusnya terlihat seperti gambar berikut:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.id.png)
>

### Chat dengan model Phi-3 kustom Anda

Sekarang setelah Anda berhasil melakukan fine-tuning dan mengintegrasikan model Phi-3 kustom dengan Prompt flow, Anda siap untuk mulai berinteraksi dengannya. Latihan ini akan memandu Anda dalam proses pengaturan dan memulai chat dengan model menggunakan Prompt flow. Dengan mengikuti langkah-langkah ini, Anda akan dapat memanfaatkan sepenuhnya kemampuan model Phi-3 yang sudah di-fine-tune untuk berbagai tugas dan percakapan.

- Chat dengan model Phi-3 kustom Anda menggunakan Prompt flow.

#### Mulai Prompt flow

1. Pilih **Start compute sessions** untuk memulai Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.id.png)

1. Pilih **Validate and parse input** untuk memperbarui parameter.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.id.png)

1. Pilih **Value** dari **connection** ke koneksi kustom yang sudah Anda buat. Contohnya, *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.id.png)

#### Chat dengan model kustom Anda

1. Pilih **Chat**.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.id.png)

1. Berikut contoh hasilnya: Sekarang Anda bisa chat dengan model Phi-3 kustom Anda. Disarankan untuk mengajukan pertanyaan berdasarkan data yang digunakan untuk fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.id.png)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.