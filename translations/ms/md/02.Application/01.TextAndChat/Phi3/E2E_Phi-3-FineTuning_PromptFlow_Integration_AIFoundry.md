<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-07-17T01:45:12+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "ms"
}
-->
# Laraskan dan Integrasikan model Phi-3 tersuai dengan Prompt flow dalam Azure AI Foundry

Contoh hujung-ke-hujung (E2E) ini berdasarkan panduan "[Laraskan dan Integrasikan Model Phi-3 Tersuai dengan Prompt Flow dalam Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" dari Microsoft Tech Community. Ia memperkenalkan proses melaraskan, menyebarkan, dan mengintegrasikan model Phi-3 tersuai dengan Prompt flow dalam Azure AI Foundry.  
Berbeza dengan contoh E2E, "[Laraskan dan Integrasikan Model Phi-3 Tersuai dengan Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", yang melibatkan menjalankan kod secara tempatan, tutorial ini memberi tumpuan sepenuhnya kepada melaraskan dan mengintegrasikan model anda dalam Azure AI / ML Studio.

## Gambaran Keseluruhan

Dalam contoh E2E ini, anda akan belajar cara melaraskan model Phi-3 dan mengintegrasikannya dengan Prompt flow dalam Azure AI Foundry. Dengan memanfaatkan Azure AI / ML Studio, anda akan membina aliran kerja untuk menyebarkan dan menggunakan model AI tersuai. Contoh E2E ini dibahagikan kepada tiga senario:

**Senario 1: Sediakan sumber Azure dan Bersedia untuk melaraskan**

**Senario 2: Laraskan model Phi-3 dan Sebarkan dalam Azure Machine Learning Studio**

**Senario 3: Integrasikan dengan Prompt flow dan Berbual dengan model tersuai anda dalam Azure AI Foundry**

Berikut adalah gambaran keseluruhan contoh E2E ini.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a2ceacdc6401c688bdf100d874fe8d55169f7723ed024781e.ms.png)

### Jadual Kandungan

1. **[Senario 1: Sediakan sumber Azure dan Bersedia untuk melaraskan](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Cipta Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Mohon kuota GPU dalam Azure Subscription](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Tambah penugasan peranan](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Sediakan projek](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Sediakan set data untuk melaraskan](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Senario 2: Laraskan model Phi-3 dan Sebarkan dalam Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Laraskan model Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Sebarkan model Phi-3 yang telah dilaraskan](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Senario 3: Integrasikan dengan Prompt flow dan Berbual dengan model tersuai anda dalam Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrasikan model Phi-3 tersuai dengan Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Berbual dengan model Phi-3 tersuai anda](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Senario 1: Sediakan sumber Azure dan Bersedia untuk melaraskan

### Cipta Azure Machine Learning Workspace

1. Taip *azure machine learning* dalam **bar carian** di bahagian atas halaman portal dan pilih **Azure Machine Learning** daripada pilihan yang muncul.

    ![Taip azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b9780de8accc31e4e1de7254e9c34a7836a955d455339e77d.ms.png)

2. Pilih **+ Create** dari menu navigasi.

3. Pilih **New workspace** dari menu navigasi.

    ![Pilih new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2cf04946c36873223099fd568e0c3ab0377c096868892fdda.ms.png)

4. Lakukan tugasan berikut:

    - Pilih **Subscription** Azure anda.
    - Pilih **Resource group** yang ingin digunakan (cipta baru jika perlu).
    - Masukkan **Workspace Name**. Ia mesti nilai unik.
    - Pilih **Region** yang anda ingin gunakan.
    - Pilih **Storage account** yang ingin digunakan (cipta baru jika perlu).
    - Pilih **Key vault** yang ingin digunakan (cipta baru jika perlu).
    - Pilih **Application insights** yang ingin digunakan (cipta baru jika perlu).
    - Pilih **Container registry** yang ingin digunakan (cipta baru jika perlu).

    ![Isikan azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090ff9ec341c724c1493e7f96726f5c810a89a7409b782a7b04a.ms.png)

5. Pilih **Review + Create**.

6. Pilih **Create**.

### Mohon kuota GPU dalam Azure Subscription

Dalam tutorial ini, anda akan belajar cara melaraskan dan menyebarkan model Phi-3 menggunakan GPU. Untuk melaraskan, anda akan menggunakan GPU *Standard_NC24ads_A100_v4*, yang memerlukan permohonan kuota. Untuk penyebaran, anda akan menggunakan GPU *Standard_NC6s_v3*, yang juga memerlukan permohonan kuota.

> [!NOTE]
>
> Hanya langganan Pay-As-You-Go (jenis langganan standard) layak untuk peruntukan GPU; langganan manfaat tidak disokong buat masa ini.
>

1. Lawati [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Lakukan tugasan berikut untuk memohon kuota *Standard NCADSA100v4 Family*:

    - Pilih **Quota** dari tab sebelah kiri.
    - Pilih **Virtual machine family** yang ingin digunakan. Contohnya, pilih **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, yang merangkumi GPU *Standard_NC24ads_A100_v4*.
    - Pilih **Request quota** dari menu navigasi.

        ![Mohon kuota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd536f2e4a305c8528a34914370813bc2cda4d7bbdd2de873f0.ms.png)

    - Dalam halaman Request quota, masukkan **New cores limit** yang anda ingin gunakan. Contohnya, 24.
    - Dalam halaman Request quota, pilih **Submit** untuk memohon kuota GPU.

1. Lakukan tugasan berikut untuk memohon kuota *Standard NCSv3 Family*:

    - Pilih **Quota** dari tab sebelah kiri.
    - Pilih **Virtual machine family** yang ingin digunakan. Contohnya, pilih **Standard NCSv3 Family Cluster Dedicated vCPUs**, yang merangkumi GPU *Standard_NC6s_v3*.
    - Pilih **Request quota** dari menu navigasi.
    - Dalam halaman Request quota, masukkan **New cores limit** yang anda ingin gunakan. Contohnya, 24.
    - Dalam halaman Request quota, pilih **Submit** untuk memohon kuota GPU.

### Tambah penugasan peranan

Untuk melaraskan dan menyebarkan model anda, anda mesti terlebih dahulu mencipta User Assigned Managed Identity (UAI) dan memberikan kebenaran yang sesuai. UAI ini akan digunakan untuk pengesahan semasa penyebaran.

#### Cipta User Assigned Managed Identity (UAI)

1. Taip *managed identities* dalam **bar carian** di bahagian atas halaman portal dan pilih **Managed Identities** daripada pilihan yang muncul.

    ![Taip managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e52f52a152187b230243fe884f58a9940cd9b534db3dcea383.ms.png)

1. Pilih **+ Create**.

    ![Pilih create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f27b6680cd94ef6ec7557394022dafdcfba2a92777b11e4817.ms.png)

1. Lakukan tugasan berikut:

    - Pilih **Subscription** Azure anda.
    - Pilih **Resource group** yang ingin digunakan (cipta baru jika perlu).
    - Pilih **Region** yang anda ingin gunakan.
    - Masukkan **Name**. Ia mesti nilai unik.

    ![Isikan maklumat managed identities.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0e313fffaecf7d6ce4ee5e86c0badcd038f03519cac63b76b.ms.png)

1. Pilih **Review + create**.

1. Pilih **+ Create**.

#### Tambah penugasan peranan Contributor kepada Managed Identity

1. Navigasi ke sumber Managed Identity yang anda cipta.

1. Pilih **Azure role assignments** dari tab sebelah kiri.

1. Pilih **+Add role assignment** dari menu navigasi.

1. Dalam halaman Add role assignment, lakukan tugasan berikut:
    - Pilih **Scope** kepada **Resource group**.
    - Pilih **Subscription** Azure anda.
    - Pilih **Resource group** yang ingin digunakan.
    - Pilih **Role** kepada **Contributor**.

    ![Isikan peranan contributor.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d1d62333e91b4d2719284f0dad14bd9b4c3459510a0c44fab.ms.png)

2. Pilih **Save**.

#### Tambah penugasan peranan Storage Blob Data Reader kepada Managed Identity

1. Taip *storage accounts* dalam **bar carian** di bahagian atas halaman portal dan pilih **Storage accounts** daripada pilihan yang muncul.

    ![Taip storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e55b6b4dda10841d74d1c7463a2e4f23b9c45ffbb84219deb2.ms.png)

1. Pilih akaun storan yang berkaitan dengan Azure Machine Learning workspace yang anda cipta. Contohnya, *finetunephistorage*.

1. Lakukan tugasan berikut untuk navigasi ke halaman Add role assignment:

    - Navigasi ke akaun storan Azure yang anda cipta.
    - Pilih **Access Control (IAM)** dari tab sebelah kiri.
    - Pilih **+ Add** dari menu navigasi.
    - Pilih **Add role assignment** dari menu navigasi.

    ![Tambah peranan.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c25fb73e63b957e214a2b651375a640a3aa54159a3731f495b.ms.png)

1. Dalam halaman Add role assignment, lakukan tugasan berikut:

    - Dalam halaman Role, taip *Storage Blob Data Reader* dalam **bar carian** dan pilih **Storage Blob Data Reader** daripada pilihan yang muncul.
    - Dalam halaman Role, pilih **Next**.
    - Dalam halaman Members, pilih **Assign access to** **Managed identity**.
    - Dalam halaman Members, pilih **+ Select members**.
    - Dalam halaman Select managed identities, pilih **Subscription** Azure anda.
    - Dalam halaman Select managed identities, pilih **Managed identity** kepada **Manage Identity**.
    - Dalam halaman Select managed identities, pilih Managed Identity yang anda cipta. Contohnya, *finetunephi-managedidentity*.
    - Dalam halaman Select managed identities, pilih **Select**.

    ![Pilih managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25289f2f121da05d114934d21d26aae9cb779334cbbccdf9e8.ms.png)

1. Pilih **Review + assign**.

#### Tambah penugasan peranan AcrPull kepada Managed Identity

1. Taip *container registries* dalam **bar carian** di bahagian atas halaman portal dan pilih **Container registries** daripada pilihan yang muncul.

    ![Taip container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a69b003f7a698dac908ffc2f355e675c10939fdd0bb09f790e.ms.png)

1. Pilih container registry yang berkaitan dengan Azure Machine Learning workspace. Contohnya, *finetunephicontainerregistry*

1. Lakukan tugasan berikut untuk navigasi ke halaman Add role assignment:

    - Pilih **Access Control (IAM)** dari tab sebelah kiri.
    - Pilih **+ Add** dari menu navigasi.
    - Pilih **Add role assignment** dari menu navigasi.

1. Dalam halaman Add role assignment, lakukan tugasan berikut:

    - Dalam halaman Role, taip *AcrPull* dalam **bar carian** dan pilih **AcrPull** daripada pilihan yang muncul.
    - Dalam halaman Role, pilih **Next**.
    - Dalam halaman Members, pilih **Assign access to** **Managed identity**.
    - Dalam halaman Members, pilih **+ Select members**.
    - Dalam halaman Select managed identities, pilih **Subscription** Azure anda.
    - Dalam halaman Select managed identities, pilih **Managed identity** kepada **Manage Identity**.
    - Dalam halaman Select managed identities, pilih Managed Identity yang anda cipta. Contohnya, *finetunephi-managedidentity*.
    - Dalam halaman Select managed identities, pilih **Select**.
    - Pilih **Review + assign**.

### Sediakan projek

Untuk memuat turun set data yang diperlukan untuk melaraskan, anda akan menyediakan persekitaran tempatan.

Dalam latihan ini, anda akan

- Cipta folder untuk bekerja di dalamnya.
- Cipta persekitaran maya.
- Pasang pakej yang diperlukan.
- Cipta fail *download_dataset.py* untuk memuat turun set data.

#### Cipta folder untuk bekerja di dalamnya

1. Buka tetingkap terminal dan taip arahan berikut untuk mencipta folder bernama *finetune-phi* dalam laluan lalai.

    ```console
    mkdir finetune-phi
    ```

2. Taip arahan berikut dalam terminal anda untuk menavigasi ke folder *finetune-phi* yang anda cipta.
#### Cipta persekitaran maya

1. Taip arahan berikut dalam terminal anda untuk mencipta persekitaran maya bernama *.venv*.

    ```console
    python -m venv .venv
    ```

2. Taip arahan berikut dalam terminal anda untuk mengaktifkan persekitaran maya.

    ```console
    .venv\Scripts\activate.bat
    ```


> [!NOTE]
> Jika berjaya, anda akan melihat *(.venv)* sebelum prompt arahan.

#### Pasang pakej yang diperlukan

1. Taip arahan berikut dalam terminal anda untuk memasang pakej yang diperlukan.

    ```console
    pip install datasets==2.19.1
    ```

#### Cipta `download_dataset.py`

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

1. Pilih folder *finetune-phi* yang anda cipta, yang terletak di *C:\Users\yourUserName\finetune-phi*.

    ![Pilih folder yang anda cipta.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6f63a0a50961e51a39cc6de7a7ddc86da5f4896e815f28abd.ms.png)

1. Di panel kiri Visual Studio Code, klik kanan dan pilih **New File** untuk mencipta fail baru bernama *download_dataset.py*.

    ![Cipta fail baru.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff927ede875300e1b5c91ab90d1e486c77a43bb9494880cf9b6f.ms.png)

### Sediakan dataset untuk fine-tuning

Dalam latihan ini, anda akan menjalankan fail *download_dataset.py* untuk memuat turun dataset *ultrachat_200k* ke persekitaran tempatan anda. Anda kemudian akan menggunakan dataset ini untuk fine-tune model Phi-3 dalam Azure Machine Learning.

Dalam latihan ini, anda akan:

- Tambah kod ke dalam fail *download_dataset.py* untuk memuat turun dataset.
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

1. Taip arahan berikut dalam terminal anda untuk menjalankan skrip dan memuat turun dataset ke persekitaran tempatan anda.

    ```console
    python download_dataset.py
    ```

1. Sahkan bahawa dataset telah berjaya disimpan ke direktori *finetune-phi/data* tempatan anda.

> [!NOTE]
>
> #### Nota mengenai saiz dataset dan masa fine-tuning
>
> Dalam tutorial ini, anda hanya menggunakan 1% daripada dataset (`split='train[:1%]'`). Ini mengurangkan jumlah data dengan ketara, mempercepatkan proses muat naik dan fine-tuning. Anda boleh laraskan peratusan untuk mencari keseimbangan yang sesuai antara masa latihan dan prestasi model. Menggunakan subset dataset yang lebih kecil mengurangkan masa yang diperlukan untuk fine-tuning, menjadikan proses lebih mudah untuk tutorial.

## Senario 2: Fine-tune model Phi-3 dan Deploy dalam Azure Machine Learning Studio

### Fine-tune model Phi-3

Dalam latihan ini, anda akan fine-tune model Phi-3 dalam Azure Machine Learning Studio.

Dalam latihan ini, anda akan:

- Cipta kluster komputer untuk fine-tuning.
- Fine-tune model Phi-3 dalam Azure Machine Learning Studio.

#### Cipta kluster komputer untuk fine-tuning

1. Lawati [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pilih **Compute** dari tab sebelah kiri.

1. Pilih **Compute clusters** dari menu navigasi.

1. Pilih **+ New**.

    ![Pilih compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252d04ffd0142c073486df7d3b7256335964a98b87e28072523.ms.png)

1. Lakukan tugasan berikut:

    - Pilih **Region** yang anda ingin gunakan.
    - Pilih **Virtual machine tier** kepada **Dedicated**.
    - Pilih **Virtual machine type** kepada **GPU**.
    - Pilih penapis **Virtual machine size** kepada **Select from all options**.
    - Pilih **Virtual machine size** kepada **Standard_NC24ads_A100_v4**.

    ![Cipta kluster.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e4baa9c5ccf86510f21df87515c231b2a255e1ee545496458.ms.png)

1. Pilih **Next**.

1. Lakukan tugasan berikut:

    - Masukkan **Compute name**. Ia mesti nilai unik.
    - Pilih **Minimum number of nodes** kepada **0**.
    - Pilih **Maximum number of nodes** kepada **1**.
    - Pilih **Idle seconds before scale down** kepada **120**.

    ![Cipta kluster.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662edc0f95ad364a869b4dbb7f7be08ff259528fea96312e77e.ms.png)

1. Pilih **Create**.

#### Fine-tune model Phi-3

1. Lawati [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pilih workspace Azure Machine Learning yang anda cipta.

    ![Pilih workspace yang anda cipta.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.ms.png)

1. Lakukan tugasan berikut:

    - Pilih **Model catalog** dari tab sebelah kiri.
    - Taip *phi-3-mini-4k* dalam **bar carian** dan pilih **Phi-3-mini-4k-instruct** dari pilihan yang muncul.

    ![Taip phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b25018a7e7353ce6525d8f5803b0af9bc9a60a9be4204dd77578.ms.png)

1. Pilih **Fine-tune** dari menu navigasi.

    ![Pilih fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeecb897ac74882792b59086893b8a7448a89be3628aee62fc1b.ms.png)

1. Lakukan tugasan berikut:

    - Pilih **Select task type** kepada **Chat completion**.
    - Pilih **+ Select data** untuk memuat naik **Traning data**.
    - Pilih jenis muat naik Validation data kepada **Provide different validation data**.
    - Pilih **+ Select data** untuk memuat naik **Validation data**.

    ![Isi halaman fine-tuning.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0bbc6b248af9e7369ca98379770badec9f73b6bced7a8b7806.ms.png)

    > [!TIP]
    >
    > Anda boleh pilih **Advanced settings** untuk sesuaikan konfigurasi seperti **learning_rate** dan **lr_scheduler_type** bagi mengoptimumkan proses fine-tuning mengikut keperluan anda.

1. Pilih **Finish**.

1. Dalam latihan ini, anda berjaya fine-tune model Phi-3 menggunakan Azure Machine Learning. Sila ambil perhatian bahawa proses fine-tuning boleh mengambil masa yang lama. Selepas menjalankan kerja fine-tuning, anda perlu menunggu sehingga ia selesai. Anda boleh memantau status kerja fine-tuning dengan pergi ke tab Jobs di sebelah kiri Workspace Azure Machine Learning anda. Dalam siri seterusnya, anda akan deploy model yang telah di-fine-tune dan mengintegrasikannya dengan Prompt flow.

    ![Lihat kerja fine-tuning.](../../../../../../translated_images/06-08-output.2bd32e59930672b1cc1de86056e2fbc91e338f59e2a29d7dac86ede49a9714b2.ms.png)

### Deploy model Phi-3 yang telah di-fine-tune

Untuk mengintegrasikan model Phi-3 yang telah di-fine-tune dengan Prompt flow, anda perlu deploy model tersebut supaya ia boleh diakses untuk inferens masa nyata. Proses ini melibatkan pendaftaran model, penciptaan endpoint dalam talian, dan deployment model.

Dalam latihan ini, anda akan:

- Daftarkan model yang telah di-fine-tune dalam workspace Azure Machine Learning.
- Cipta endpoint dalam talian.
- Deploy model Phi-3 yang telah didaftarkan dan di-fine-tune.

#### Daftarkan model yang telah di-fine-tune

1. Lawati [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pilih workspace Azure Machine Learning yang anda cipta.

    ![Pilih workspace yang anda cipta.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.ms.png)

1. Pilih **Models** dari tab sebelah kiri.
1. Pilih **+ Register**.
1. Pilih **From a job output**.

    ![Daftarkan model.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777c8c39906ce5cd57f16b54fb3887dd4e4de1ce963b26499ad.ms.png)

1. Pilih kerja yang anda cipta.

    ![Pilih kerja.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd09315953b4eb2cc9d62d0d77ab0d9d877e34c6827fa6d2b6be4.ms.png)

1. Pilih **Next**.

1. Pilih **Model type** kepada **MLflow**.

1. Pastikan **Job output** dipilih; ia sepatutnya dipilih secara automatik.

    ![Pilih output.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f267b40f73de77f092a5b02808ade72f8eb94e5fe9723feb3.ms.png)

2. Pilih **Next**.

3. Pilih **Register**.

    ![Pilih daftar.](../../../../../../translated_images/07-04-register.fd82a3b293060bc78399e613293032d3d301c02a6fd8092bec52bfaf4f3104de.ms.png)

4. Anda boleh melihat model yang telah didaftarkan dengan pergi ke menu **Models** dari tab sebelah kiri.

    ![Model yang didaftarkan.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591b7995686b95396ffd8c185ba66f0a1f6be18f4aea05e93d5.ms.png)

#### Deploy model yang telah di-fine-tune

1. Pergi ke workspace Azure Machine Learning yang anda cipta.

1. Pilih **Endpoints** dari tab sebelah kiri.

1. Pilih **Real-time endpoints** dari menu navigasi.

    ![Cipta endpoint.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09618ce29b467276523838b8cc766d79ebfecdb052fef2c4df.ms.png)

1. Pilih **Create**.

1. Pilih model yang telah didaftarkan yang anda cipta.

    ![Pilih model yang didaftarkan.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4460f7646dfaa59121fb1384ed1957755427d358462c25225.ms.png)

1. Pilih **Select**.

1. Lakukan tugasan berikut:

    - Pilih **Virtual machine** kepada *Standard_NC6s_v3*.
    - Pilih **Instance count** yang anda ingin gunakan. Contohnya, *1*.
    - Pilih **Endpoint** kepada **New** untuk mencipta endpoint baru.
    - Masukkan **Endpoint name**. Ia mesti nilai unik.
    - Masukkan **Deployment name**. Ia mesti nilai unik.

    ![Isi tetapan deployment.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e67378494bb8d81418bc3bdaceb8c57151727d538594cb378697f36.ms.png)

1. Pilih **Deploy**.

> [!WARNING]
> Untuk mengelakkan caj tambahan pada akaun anda, pastikan anda memadam endpoint yang telah dicipta dalam workspace Azure Machine Learning.
>

#### Semak status deployment dalam Azure Machine Learning Workspace

1. Pergi ke workspace Azure Machine Learning yang anda cipta.

1. Pilih **Endpoints** dari tab sebelah kiri.

1. Pilih endpoint yang anda cipta.

    ![Pilih endpoints](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4a302f0efc8875002e1c382167083c7fefbdb42ede274d0da.ms.png)

1. Pada halaman ini, anda boleh menguruskan endpoints semasa proses deployment.

> [!NOTE]
> Setelah deployment selesai, pastikan **Live traffic** ditetapkan kepada **100%**. Jika tidak, pilih **Update traffic** untuk laraskan tetapan trafik. Perlu diingat anda tidak boleh menguji model jika trafik ditetapkan kepada 0%.
>
> ![Tetapkan trafik.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d30c64ecabac4b17a7b5dc004ba52ad387cbaaf7b266eeadf.ms.png)
>

## Senario 3: Integrasi dengan Prompt flow dan Berbual dengan model khusus anda dalam Azure AI Foundry

### Integrasi model Phi-3 khusus dengan Prompt flow

Selepas berjaya deploy model yang telah di-fine-tune, anda kini boleh mengintegrasikannya dengan Prompt Flow untuk menggunakan model anda dalam aplikasi masa nyata, membolehkan pelbagai tugasan interaktif dengan model Phi-3 khusus anda.

Dalam latihan ini, anda akan:

- Cipta Azure AI Foundry Hub.
- Cipta Projek Azure AI Foundry.
- Cipta Prompt flow.
- Tambah sambungan khusus untuk model Phi-3 yang telah di-fine-tune.
- Sediakan Prompt flow untuk berbual dengan model Phi-3 khusus anda.
> [!NOTE]
> Anda juga boleh mengintegrasikan dengan Promptflow menggunakan Azure ML Studio. Proses integrasi yang sama boleh digunakan untuk Azure ML Studio.
#### Cipta Azure AI Foundry Hub

Anda perlu mencipta Hub sebelum mencipta Projek. Hub berfungsi seperti Kumpulan Sumber, membolehkan anda mengatur dan menguruskan pelbagai Projek dalam Azure AI Foundry.

1. Lawati [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Pilih **All hubs** dari tab sebelah kiri.

1. Pilih **+ New hub** dari menu navigasi.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834e092dcf9dda773276fbee65f40252ed4a9af4f9aa4fef5d7.ms.png)

1. Lakukan tugasan berikut:

    - Masukkan **Hub name**. Ia mesti nilai yang unik.
    - Pilih **Subscription** Azure anda.
    - Pilih **Resource group** yang ingin digunakan (cipta yang baru jika perlu).
    - Pilih **Location** yang anda ingin gunakan.
    - Pilih **Connect Azure AI Services** yang ingin digunakan (cipta yang baru jika perlu).
    - Pilih **Connect Azure AI Search** kepada **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c44658a87c2ed01d9e588581f157480ff1ac3312085c51d25.ms.png)

1. Pilih **Next**.

#### Cipta Projek Azure AI Foundry

1. Dalam Hub yang anda cipta, pilih **All projects** dari tab sebelah kiri.

1. Pilih **+ New project** dari menu navigasi.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f1251c487d98aed0641bd057100b8e5d6fba9062bfb7d752ce9.ms.png)

1. Masukkan **Project name**. Ia mesti nilai yang unik.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a192b4ed3dde6b1136c860fc85352d612aa2f3ae8a4d54eb4.ms.png)

1. Pilih **Create a project**.

#### Tambah sambungan khusus untuk model Phi-3 yang telah ditala

Untuk mengintegrasikan model Phi-3 khusus anda dengan Prompt flow, anda perlu menyimpan endpoint dan kunci model dalam sambungan khusus. Persediaan ini memastikan akses ke model Phi-3 khusus anda dalam Prompt flow.

#### Tetapkan api key dan endpoint uri model Phi-3 yang telah ditala

1. Lawati [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Navigasi ke ruang kerja Azure Machine learning yang anda cipta.

1. Pilih **Endpoints** dari tab sebelah kiri.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf960519c1ac95116d1a7e5b8d0bdea5cd42281930766fbfad1929.ms.png)

1. Pilih endpoint yang anda cipta.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275ea16f689f59b70d5b0162fff1781204e389edcb63b42b95b2.ms.png)

1. Pilih **Consume** dari menu navigasi.

1. Salin **REST endpoint** dan **Primary key** anda.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cbe30a20b889154d04109bf17c5c09816060a8689933dc0fd7.ms.png)

#### Tambah Sambungan Khusus

1. Lawati [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Navigasi ke projek Azure AI Foundry yang anda cipta.

1. Dalam Projek yang anda cipta, pilih **Settings** dari tab sebelah kiri.

1. Pilih **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc77130c3a16fbb8ee59407ecbf74fd3502cb8720c61384446.ms.png)

1. Pilih **Custom keys** dari menu navigasi.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b29664605513ccc134f1adaefaf27f951981c511783a6a0d1118c9178a5.ms.png)

1. Lakukan tugasan berikut:

    - Pilih **+ Add key value pairs**.
    - Untuk nama kunci, masukkan **endpoint** dan tampal endpoint yang anda salin dari Azure ML Studio ke dalam medan nilai.
    - Pilih **+ Add key value pairs** sekali lagi.
    - Untuk nama kunci, masukkan **key** dan tampal kunci yang anda salin dari Azure ML Studio ke dalam medan nilai.
    - Selepas menambah kunci, pilih **is secret** untuk mengelakkan kunci didedahkan.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26e8df1bbd0948e06aa20aa0dc102faa96c8144722ef7f0b72.ms.png)

1. Pilih **Add connection**.

#### Cipta Prompt flow

Anda telah menambah sambungan khusus dalam Azure AI Foundry. Sekarang, mari cipta Prompt flow menggunakan langkah berikut. Kemudian, anda akan sambungkan Prompt flow ini ke sambungan khusus supaya anda boleh menggunakan model yang telah ditala dalam Prompt flow.

1. Navigasi ke projek Azure AI Foundry yang anda cipta.

1. Pilih **Prompt flow** dari tab sebelah kiri.

1. Pilih **+ Create** dari menu navigasi.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5ba79bedfd35e2f2fb430f344844994375680fcfc111a994ae.ms.png)

1. Pilih **Chat flow** dari menu navigasi.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591f6cc6360bc35c8fca8d63519c09111c6c431de9b46eed143.ms.png)

1. Masukkan **Folder name** yang ingin digunakan.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d824bad779a54e55d808a09394b6b730fbea55d78421f52ff.ms.png)

2. Pilih **Create**.

#### Sediakan Prompt flow untuk bersembang dengan model Phi-3 khusus anda

Anda perlu mengintegrasikan model Phi-3 yang telah ditala ke dalam Prompt flow. Walau bagaimanapun, Prompt flow sedia ada yang disediakan tidak direka untuk tujuan ini. Oleh itu, anda mesti mereka semula Prompt flow untuk membolehkan integrasi model khusus tersebut.

1. Dalam Prompt flow, lakukan tugasan berikut untuk membina semula aliran sedia ada:

    - Pilih **Raw file mode**.
    - Padam semua kod sedia ada dalam fail *flow.dag.yml*.
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

    - Pilih **Save**.

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985b76e070bf170e1d0d0d26b38d93bc635624642191f715a6d.ms.png)

1. Tambah kod berikut ke dalam fail *integrate_with_promptflow.py* untuk menggunakan model Phi-3 khusus dalam Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d097779ab1c429be9fc07e3f4171e41fbbfb747a6e755816411e6d.ms.png)

> [!NOTE]
> Untuk maklumat lebih terperinci mengenai penggunaan Prompt flow dalam Azure AI Foundry, anda boleh rujuk [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Pilih **Chat input**, **Chat output** untuk membolehkan sembang dengan model anda.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03ba022a21159e51d544c6e063e73c10e772c942d4e44da0d30.ms.png)

1. Kini anda sudah bersedia untuk bersembang dengan model Phi-3 khusus anda. Dalam latihan seterusnya, anda akan belajar cara memulakan Prompt flow dan menggunakannya untuk bersembang dengan model Phi-3 yang telah ditala.

> [!NOTE]
>
> Aliran yang dibina semula sepatutnya kelihatan seperti imej di bawah:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c10b7375192511a8e2aba847e442b294a2e65d88ffac8f63b.ms.png)
>

### Bersembang dengan model Phi-3 khusus anda

Kini anda telah menala dan mengintegrasikan model Phi-3 khusus anda dengan Prompt flow, anda sudah bersedia untuk mula berinteraksi dengannya. Latihan ini akan membimbing anda melalui proses menyediakan dan memulakan sembang dengan model anda menggunakan Prompt flow. Dengan mengikuti langkah-langkah ini, anda akan dapat menggunakan sepenuhnya keupayaan model Phi-3 yang telah ditala untuk pelbagai tugasan dan perbualan.

- Bersembang dengan model Phi-3 khusus anda menggunakan Prompt flow.

#### Mulakan Prompt flow

1. Pilih **Start compute sessions** untuk memulakan Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b4809b60d75ce9b0ad53e0729cc1449935ccbe90b954401dc.ms.png)

1. Pilih **Validate and parse input** untuk memperbaharui parameter.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e97038d7529b9060a23dc59d7ddbeb38ac9c4562ef4f5b32f7.ms.png)

1. Pilih **Value** bagi **connection** kepada sambungan khusus yang anda cipta. Contohnya, *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b184402368a6ec383814b139686118331a5b2eefa489678902269dfc.ms.png)

#### Bersembang dengan model khusus anda

1. Pilih **Chat**.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e636a5e1516b6c64fdf2345ceb3142db2bed93ab7e6f03bbb2.ms.png)

1. Berikut adalah contoh hasilnya: Kini anda boleh bersembang dengan model Phi-3 khusus anda. Disarankan untuk bertanya soalan berdasarkan data yang digunakan untuk penalaan.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126fa4886e6fd0e7482cfdc6c907fa36f7f2f13d04126f9eda14.ms.png)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.