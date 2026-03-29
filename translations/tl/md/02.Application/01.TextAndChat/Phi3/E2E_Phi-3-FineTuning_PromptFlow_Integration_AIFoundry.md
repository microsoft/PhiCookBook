# Fine-tune at Iintegrate ang custom Phi-3 models gamit ang Prompt flow sa Microsoft Foundry

Ang end-to-end (E2E) na sample na ito ay batay sa gabay na "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" mula sa Microsoft Tech Community. Ipinapakilala nito ang mga proseso ng fine-tuning, pag-deploy, at pag-integrate ng custom Phi-3 models gamit ang Prompt flow sa Microsoft Foundry. Hindi tulad ng E2E sample, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", na nagsasangkot ng pagtakbo ng code nang lokal, ang tutorial na ito ay nakatuon nang buo sa fine-tuning at pag-integrate ng iyong model sa loob ng Azure AI / ML Studio.

## Pangkalahatang-ideya

Sa E2E sample na ito, matututunan mo kung paano i-fine-tune ang Phi-3 model at i-integrate ito gamit ang Prompt flow sa Microsoft Foundry. Sa pamamagitan ng paggamit ng Azure AI / ML Studio, magtatatag ka ng workflow para sa pag-deploy at paggamit ng mga custom AI models. Ang E2E sample na ito ay nahahati sa tatlong mga scenario:

**Scenario 1: Mag-set up ng Azure na mga resources at Maghanda para sa fine-tuning**

**Scenario 2: I-fine-tune ang Phi-3 model at I-deploy sa Azure Machine Learning Studio**

**Scenario 3: I-integrate gamit ang Prompt flow at Makipag-chat gamit ang iyong custom model sa Microsoft Foundry**

Narito ang isang pangkalahatang-ideya ng E2E sample na ito.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/tl/00-01-architecture.198ba0f1ae6d841a.webp)

### Talaan ng Nilalaman

1. **[Scenario 1: Mag-set up ng Azure na mga resources at Maghanda para sa fine-tuning](#scenario-1-mag-set-up-ng-azure-na-mga-resources-at-maghanda-para-sa-fine-tuning)**
    - [Lumikha ng Azure Machine Learning Workspace](#lumikha-ng-azure-machine-learning-workspace)
    - [Humiling ng GPU quotas sa Azure Subscription](#humiling-ng-gpu-quotas-sa-azure-subscription)
    - [Magdagdag ng role assignment](#magdagdag-ng-role-assignment)
    - [I-set up ang proyekto](#i-set-up-ang-proyekto)
    - [Maghanda ng dataset para sa fine-tuning](#ihanda-ang-dataset-para-sa-fine-tuning)

1. **[Scenario 2: I-fine-tune ang Phi-3 model at I-deploy sa Azure Machine Learning Studio](#senaryo-2-fine-tune-ang-phi-3-model-at-i-deploy-ito-sa-azure-machine-learning-studio)**
    - [I-fine-tune ang Phi-3 model](#fine-tune-ang-phi-3-model)
    - [I-deploy ang fine-tuned Phi-3 model](#i-deploy-ang-na-fine-tune-na-phi-3-model)

1. **[Scenario 3: I-integrate gamit ang Prompt flow at Makipag-chat gamit ang iyong custom model sa Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [I-integrate ang custom Phi-3 model gamit ang Prompt flow](#i-integrate-ang-custom-na-phi-3-model-sa-prompt-flow)
    - [Makipag-chat gamit ang iyong custom Phi-3 model](#makipag-chat-sa-iyong-custom-na-phi-3-model)

## Scenario 1: Mag-set up ng Azure na mga resources at Maghanda para sa fine-tuning

### Lumikha ng Azure Machine Learning Workspace

1. I-type ang *azure machine learning* sa **search bar** sa itaas ng portal page at piliin ang **Azure Machine Learning** mula sa mga lumabas na opsyon.

    ![Type azure machine learning.](../../../../../../translated_images/tl/01-01-type-azml.acae6c5455e67b4b.webp)

2. Piliin ang **+ Create** mula sa navigation menu.

3. Piliin ang **New workspace** mula sa navigation menu.

    ![Select new workspace.](../../../../../../translated_images/tl/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Gawin ang mga sumusunod na gawain:

    - Piliin ang iyong Azure **Subscription**.
    - Piliin ang **Resource group** na gagamitin (gumawa ng bago kung kinakailangan).
    - Ilagay ang **Workspace Name**. Dapat itong maging natatanging halaga.
    - Piliin ang **Region** na nais mong gamitin.
    - Piliin ang **Storage account** na gagamitin (gumawa ng bago kung kinakailangan).
    - Piliin ang **Key vault** na gagamitin (gumawa ng bago kung kinakailangan).
    - Piliin ang **Application insights** na gagamitin (gumawa ng bago kung kinakailangan).
    - Piliin ang **Container registry** na gagamitin (gumawa ng bago kung kinakailangan).

    ![Fill azure machine learning.](../../../../../../translated_images/tl/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Piliin ang **Review + Create**.

6. Piliin ang **Create**.

### Humiling ng GPU quotas sa Azure Subscription

Sa tutorial na ito, matututunan mo kung paano i-fine-tune at ideploy ang isang Phi-3 model, gamit ang mga GPU. Para sa fine-tuning, gagamitin mo ang *Standard_NC24ads_A100_v4* GPU, na nangangailangan ng quota request. Para sa deployment, gagamitin mo ang *Standard_NC6s_v3* GPU, na nangangailangan din ng quota request.

> [!NOTE]
>
> Ang mga Pay-As-You-Go subscriptions lamang (ang karaniwang uri ng subscription) ang karapat-dapat para sa GPU allocation; ang mga benefit subscriptions ay hindi suportado sa kasalukuyan.
>

1. Bisitahin ang [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Gawin ang mga sumusunod na hakbang upang humiling ng *Standard NCADSA100v4 Family* quota:

    - Piliin ang **Quota** mula sa kaliwang tab.
    - Piliin ang **Virtual machine family** na gagamitin. Halimbawa, piliin ang **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, na kasama ang *Standard_NC24ads_A100_v4* GPU.
    - Piliin ang **Request quota** mula sa navigation menu.

        ![Request quota.](../../../../../../translated_images/tl/02-02-request-quota.c0428239a63ffdd5.webp)

    - Sa loob ng Request quota page, ilagay ang **New cores limit** na nais mong gamitin. Halimbawa, 24.
    - Sa loob ng Request quota page, piliin ang **Submit** upang humiling ng GPU quota.

1. Gawin ang mga sumusunod na hakbang upang humiling ng *Standard NCSv3 Family* quota:

    - Piliin ang **Quota** mula sa kaliwang tab.
    - Piliin ang **Virtual machine family** na gagamitin. Halimbawa, piliin ang **Standard NCSv3 Family Cluster Dedicated vCPUs**, na kasama ang *Standard_NC6s_v3* GPU.
    - Piliin ang **Request quota** mula sa navigation menu.
    - Sa loob ng Request quota page, ilagay ang **New cores limit** na nais mong gamitin. Halimbawa, 24.
    - Sa loob ng Request quota page, piliin ang **Submit** upang humiling ng GPU quota.

### Magdagdag ng role assignment

Upang ma-fine-tune at ma-deploy ang iyong mga modelo, kailangan mo munang gumawa ng User Assigned Managed Identity (UAI) at bigyan ito ng angkop na mga pahintulot. Ang UAI na ito ang gagamitin para sa authentication sa panahon ng deployment.

#### Gumawa ng User Assigned Managed Identity(UAI)

1. I-type ang *managed identities* sa **search bar** sa itaas ng portal page at piliin ang **Managed Identities** mula sa mga lumabas na opsyon.

    ![Type managed identities.](../../../../../../translated_images/tl/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Piliin ang **+ Create**.

    ![Select create.](../../../../../../translated_images/tl/03-02-select-create.92bf8989a5cd98f2.webp)

1. Gawin ang mga sumusunod na gawain:

    - Piliin ang iyong Azure **Subscription**.
    - Piliin ang **Resource group** na gagamitin (gumawa ng bago kung kinakailangan).
    - Piliin ang **Region** na nais mong gamitin.
    - Ilagay ang **Name**. Dapat itong maging natatanging halaga.

    ![Select create.](../../../../../../translated_images/tl/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Piliin ang **Review + create**.

1. Piliin ang **+ Create**.

#### Magdagdag ng Contributor role assignment sa Managed Identity

1. Pumunta sa Managed Identity na nilikha mo.

1. Piliin ang **Azure role assignments** mula sa kaliwang tab.

1. Piliin ang **+Add role assignment** mula sa navigation menu.

1. Sa loob ng Add role assignment page, gawin ang mga sumusunod na hakbang:
    - Piliin ang **Scope** sa **Resource group**.
    - Piliin ang iyong Azure **Subscription**.
    - Piliin ang **Resource group** na gagamitin.
    - Piliin ang **Role** sa **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/tl/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Piliin ang **Save**.

#### Magdagdag ng Storage Blob Data Reader role assignment sa Managed Identity

1. I-type ang *storage accounts* sa **search bar** sa itaas ng portal page at piliin ang **Storage accounts** mula sa mga lumabas na opsyon.

    ![Type storage accounts.](../../../../../../translated_images/tl/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Piliin ang storage account na kaakibat ng Azure Machine Learning workspace na iyong ginawa. Halimbawa, *finetunephistorage*.

1. Gawin ang mga sumusunod na hakbang upang pumunta sa Add role assignment page:

    - Pumunta sa Azure Storage account na nilikha mo.
    - Piliin ang **Access Control (IAM)** mula sa kaliwang tab.
    - Piliin ang **+ Add** mula sa navigation menu.
    - Piliin ang **Add role assignment** mula sa navigation menu.

    ![Add role.](../../../../../../translated_images/tl/03-06-add-role.353ccbfdcf0789c2.webp)

1. Sa loob ng Add role assignment page, gawin ang mga sumusunod na hakbang:

    - Sa Role page, i-type ang *Storage Blob Data Reader* sa **search bar** at piliin ang **Storage Blob Data Reader** mula sa mga lumabas na opsyon.
    - Sa Role page, piliin ang **Next**.
    - Sa Members page, piliin ang **Assign access to** na **Managed identity**.
    - Sa Members page, piliin ang **+ Select members**.
    - Sa Select managed identities page, piliin ang iyong Azure **Subscription**.
    - Sa Select managed identities page, piliin ang **Managed identity** sa **Manage Identity**.
    - Sa Select managed identities page, piliin ang Manage Identity na iyong nilikha. Halimbawa, *finetunephi-managedidentity*.
    - Sa Select managed identities page, piliin ang **Select**.

    ![Select managed identity.](../../../../../../translated_images/tl/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Piliin ang **Review + assign**.

#### Magdagdag ng AcrPull role assignment sa Managed Identity

1. I-type ang *container registries* sa **search bar** sa itaas ng portal page at piliin ang **Container registries** mula sa mga lumabas na opsyon.

    ![Type container registries.](../../../../../../translated_images/tl/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Piliin ang container registry na kaakibat ng Azure Machine Learning workspace. Halimbawa, *finetunephicontainerregistry*

1. Gawin ang mga sumusunod na hakbang upang pumunta sa Add role assignment page:

    - Piliin ang **Access Control (IAM)** mula sa kaliwang tab.
    - Piliin ang **+ Add** mula sa navigation menu.
    - Piliin ang **Add role assignment** mula sa navigation menu.

1. Sa loob ng Add role assignment page, gawin ang mga sumusunod na hakbang:

    - Sa Role page, i-type ang *AcrPull* sa **search bar** at piliin ang **AcrPull** mula sa mga lumabas na opsyon.
    - Sa Role page, piliin ang **Next**.
    - Sa Members page, piliin ang **Assign access to** na **Managed identity**.
    - Sa Members page, piliin ang **+ Select members**.
    - Sa Select managed identities page, piliin ang iyong Azure **Subscription**.
    - Sa Select managed identities page, piliin ang **Managed identity** sa **Manage Identity**.
    - Sa Select managed identities page, piliin ang Manage Identity na iyong nilikha. Halimbawa, *finetunephi-managedidentity*.
    - Sa Select managed identities page, piliin ang **Select**.
    - Piliin ang **Review + assign**.

### I-set up ang proyekto

Upang ma-download ang mga dataset na kinakailangan para sa fine-tuning, magse-set up ka ng lokal na kapaligiran.

Sa exercise na ito, gagawin mo ang mga sumusunod:

- Lumikha ng folder para magtrabaho sa loob nito.
- Lumikha ng virtual environment.
- I-install ang mga kinakailangang pakete.
- Lumikha ng *download_dataset.py* na file upang ma-download ang dataset.

#### Lumikha ng folder para magtrabaho sa loob nito

1. Buksan ang terminal window at i-type ang sumusunod na command para gumawa ng folder na pinangalanang *finetune-phi* sa default na path.

    ```console
    mkdir finetune-phi
    ```

2. I-type ang sumusunod na command sa loob ng iyong terminal para pumunta sa *finetune-phi* folder na iyong ginawa.

    ```console
    cd finetune-phi
    ```

#### Lumikha ng virtual environment

1. I-type ang sumusunod na command sa loob ng iyong terminal para gumawa ng virtual environment na pinangalanang *.venv*.
    ```console
    python -m venv .venv
    ```

2. I-type ang sumusunod na utos sa loob ng iyong terminal upang paganahin ang virtual environment.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Kung gumana ito, dapat makita mo ang *(.venv)* bago ang command prompt.

#### I-install ang kinakailangang mga pakete

1. I-type ang mga sumusunod na utos sa iyong terminal upang i-install ang mga kinakailangang pakete.

    ```console
    pip install datasets==2.19.1
    ```

#### Lumikha ng `donload_dataset.py`

> [!NOTE]
> Kumpletong istruktura ng folder:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Buksan ang **Visual Studio Code**.

1. Piliin ang **File** mula sa menu bar.

1. Piliin ang **Open Folder**.

1. Piliin ang *finetune-phi* na folder na iyong ginawa, na matatagpuan sa *C:\Users\yourUserName\finetune-phi*.

    ![Piliin ang folder na iyong ginawa.](../../../../../../translated_images/tl/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. Sa kaliwang pane ng Visual Studio Code, i-right click at piliin ang **New File** upang gumawa ng bagong file na pinangalanang *download_dataset.py*.

    ![Gumawa ng bagong file.](../../../../../../translated_images/tl/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Ihanda ang dataset para sa fine-tuning

Sa pagsasanay na ito, patatakbuhin mo ang *download_dataset.py* file upang i-download ang *ultrachat_200k* datasets sa iyong lokal na kapaligiran. Gagamitin mo ang mga dataset na ito upang i-fine-tune ang Phi-3 model sa Azure Machine Learning.

Sa pagsasanay na ito, gagawin mo ang mga sumusunod:

- Magdagdag ng code sa *download_dataset.py* file upang i-download ang mga dataset.
- Patakbuhin ang *download_dataset.py* file upang i-download ang mga dataset sa iyong lokal na kapaligiran.

#### I-download ang iyong dataset gamit ang *download_dataset.py*

1. Buksan ang *download_dataset.py* file sa Visual Studio Code.

1. Idagdag ang sumusunod na code sa *download_dataset.py* file.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # I-load ang dataset gamit ang tinukoy na pangalan, konfigurasyon, at ratio ng hati
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Hatiin ang dataset sa mga train at test na set (80% train, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Gumawa ng direktoryo kung hindi pa ito umiiral
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Buksan ang file sa mode na pagsulat
        with open(filepath, 'w', encoding='utf-8') as f:
            # Ulitin ang bawat tala sa dataset
            for record in dataset:
                # I-dump ang tala bilang isang JSON object at isulat ito sa file
                json.dump(record, f)
                # Isulat ang newline character upang paghiwalayin ang mga tala
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # I-load at hatiin ang ULTRACHAT_200k na dataset gamit ang isang tiyak na konfigurasyon at ratio ng hati
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Kunin ang train at test na mga dataset mula sa paghahati
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # I-save ang train na dataset sa isang JSONL na file
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # I-save ang test na dataset sa isang hiwalay na JSONL na file
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. I-type ang sumusunod na utos sa iyong terminal upang patakbuhin ang script at i-download ang dataset sa iyong lokal na kapaligiran.

    ```console
    python download_dataset.py
    ```

1. Siguraduhing ang mga dataset ay matagumpay na na-save sa iyong lokal na *finetune-phi/data* directory.

> [!NOTE]
>
> #### Tala tungkol sa laki ng dataset at oras ng fine-tuning
>
> Sa tutorial na ito, ginamit mo lamang ang 1% ng dataset (`split='train[:1%]'`). Ito ay malaki ang nabawas sa dami ng data, kaya pinalilipat at pinapabilis ang proseso ng upload at fine-tuning. Maaari mong baguhin ang porsyento upang mahanap ang tamang balanse sa pagitan ng oras ng pagsasanay at performance ng modelo. Ang paggamit ng mas maliit na bahagi ng dataset ay nagpapabawas sa oras na kinakailangan para sa fine-tuning, kaya mas madali itong gawin sa tutorial.

## Senaryo 2: Fine-tune ang Phi-3 model at I-deploy ito sa Azure Machine Learning Studio

### Fine-tune ang Phi-3 model

Sa pagsasanay na ito, i-fine-tune mo ang Phi-3 model sa Azure Machine Learning Studio.

Sa pagsasanay na ito, gagawin mo ang mga sumusunod:

- Lumikha ng computer cluster para sa fine-tuning.
- I-fine-tune ang Phi-3 model sa Azure Machine Learning Studio.

#### Lumikha ng computer cluster para sa fine-tuning

1. Bisitahin ang [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Piliin ang **Compute** mula sa kaliwang tab.

1. Piliin ang **Compute clusters** mula sa navigation menu.

1. Piliin ang **+ New**.

    ![Piliin ang compute.](../../../../../../translated_images/tl/06-01-select-compute.a29cff290b480252.webp)

1. Gawin ang mga sumusunod:

    - Piliin ang **Region** na nais mong gamitin.
    - Piliin ang **Virtual machine tier** bilang **Dedicated**.
    - Piliin ang **Virtual machine type** bilang **GPU**.
    - Piliin ang filter para sa **Virtual machine size** bilang **Select from all options**.
    - Piliin ang **Virtual machine size** na **Standard_NC24ads_A100_v4**.

    ![Gumawa ng cluster.](../../../../../../translated_images/tl/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Piliin ang **Next**.

1. Gawin ang mga sumusunod:

    - Ipasok ang **Compute name**. Dapat ito ay natatanging pangalan.
    - Piliin ang **Minimum number of nodes** sa **0**.
    - Piliin ang **Maximum number of nodes** sa **1**.
    - Piliin ang **Idle seconds before scale down** sa **120**.

    ![Gumawa ng cluster.](../../../../../../translated_images/tl/06-03-create-cluster.4a54ba20914f3662.webp)

1. Piliin ang **Create**.

#### Fine-tune ang Phi-3 model

1. Bisitahin ang [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Piliin ang Azure Machine Learning workspace na iyong ginawa.

    ![Piliin ang workspace na ginawa mo.](../../../../../../translated_images/tl/06-04-select-workspace.a92934ac04f4f181.webp)

1. Gawin ang mga sumusunod:

    - Piliin ang **Model catalog** mula sa kaliwang tab.
    - I-type ang *phi-3-mini-4k* sa **search bar** at piliin ang **Phi-3-mini-4k-instruct** mula sa mga lumabas na pagpipilian.

    ![I-type ang phi-3-mini-4k.](../../../../../../translated_images/tl/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Piliin ang **Fine-tune** mula sa navigation menu.

    ![Piliin ang fine tune.](../../../../../../translated_images/tl/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Gawin ang mga sumusunod:

    - Piliin ang **Select task type** bilang **Chat completion**.
    - Piliin ang **+ Select data** upang mag-upload ng **Training data**.
    - Piliin ang uri ng pag-upload para sa Validation data bilang **Provide different validation data**.
    - Piliin ang **+ Select data** upang mag-upload ng **Validation data**.

    ![Punan ang fine-tuning na pahina.](../../../../../../translated_images/tl/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Maaari mong piliin ang **Advanced settings** upang i-customize ang mga configuration tulad ng **learning_rate** at **lr_scheduler_type** upang mas mapabuti ang fine-tuning ayon sa iyong pangangailangan.

1. Piliin ang **Finish**.

1. Sa pagsasanay na ito, matagumpay mong na-fine-tune ang Phi-3 model gamit ang Azure Machine Learning. Tandaan na ang proseso ng fine-tuning ay maaaring tumagal ng maraming oras. Pagkatapos patakbuhin ang fine-tuning job, kailangang maghintay hanggang matapos ito. Maaari mong subaybayan ang status ng fine-tuning job sa pamamagitan ng pag-navigate sa Jobs tab sa kaliwang bahagi ng iyong Azure Machine Learning Workspace. Sa susunod na bahagi, ide-deploy mo ang na-fine-tune na modelo at i-integrate ito sa Prompt flow.

    ![Tingnan ang fine-tuning job.](../../../../../../translated_images/tl/06-08-output.2bd32e59930672b1.webp)

### I-deploy ang na-fine-tune na Phi-3 model

Para ma-integrate ang na-fine-tune na Phi-3 model sa Prompt flow, kailangan mong i-deploy ang modelo upang maging accessible ito para sa real-time inference. Kabilang dito ang pagrerehistro ng modelo, paggawa ng online endpoint, at pag-deploy ng modelo.

Sa pagsasanay na ito, gagawin mo ang mga sumusunod:

- Irehistro ang na-fine-tune na modelo sa Azure Machine Learning workspace.
- Lumikha ng online endpoint.
- I-deploy ang narehistrong na-fine-tune na Phi-3 model.

#### Irehistro ang na-fine-tune na modelo

1. Bisitahin ang [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Piliin ang Azure Machine Learning workspace na iyong ginawa.

    ![Piliin ang workspace na ginawa mo.](../../../../../../translated_images/tl/06-04-select-workspace.a92934ac04f4f181.webp)

1. Piliin ang **Models** mula sa kaliwang tab.
1. Piliin ang **+ Register**.
1. Piliin ang **From a job output**.

    ![Irehistro ang modelo.](../../../../../../translated_images/tl/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Piliin ang job na iyong ginawa.

    ![Piliin ang job.](../../../../../../translated_images/tl/07-02-select-job.3e2e1144cd6cd093.webp)

1. Piliin ang **Next**.

1. Piliin ang **Model type** bilang **MLflow**.

1. Tiyakin na naka-select ang **Job output**; ito ay awtomatikong dapat naka-select.

    ![Piliin ang output.](../../../../../../translated_images/tl/07-03-select-output.4cf1a0e645baea1f.webp)

2. Piliin ang **Next**.

3. Piliin ang **Register**.

    ![Piliin ang register.](../../../../../../translated_images/tl/07-04-register.fd82a3b293060bc7.webp)

4. Makikita mo ang iyong narehistrong modelo sa pamamagitan ng pag-navigate sa **Models** menu sa kaliwang tab.

    ![Narehistrong modelo.](../../../../../../translated_images/tl/07-05-registered-model.7db9775f58dfd591.webp)

#### I-deploy ang na-fine-tune na modelo

1. Pumunta sa Azure Machine Learning workspace na iyong ginawa.

1. Piliin ang **Endpoints** mula sa kaliwang tab.

1. Piliin ang **Real-time endpoints** mula sa navigation menu.

    ![Gumawa ng endpoint.](../../../../../../translated_images/tl/07-06-create-endpoint.1ba865c606551f09.webp)

1. Piliin ang **Create**.

1. Piliin ang narehistrong modelo na iyong ginawa.

    ![Piliin ang narehistrong modelo.](../../../../../../translated_images/tl/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Piliin ang **Select**.

1. Gawin ang mga sumusunod:

    - Piliin ang **Virtual machine** bilang *Standard_NC6s_v3*.
    - Piliin ang bilang ng **Instance count** na nais mong gamitin. Halimbawa, *1*.
    - Piliin ang **Endpoint** bilang **New** upang gumawa ng endpoint.
    - Ipasok ang **Endpoint name**. Dapat ito ay natatangi.
    - Ipasok ang **Deployment name**. Dapat ito ay natatangi.

    ![Punan ang deployment setting.](../../../../../../translated_images/tl/07-08-deployment-setting.43ddc4209e673784.webp)

1. Piliin ang **Deploy**.

> [!WARNING]
> Upang maiwasan ang dagdag na singil sa iyong account, siguraduhing tanggalin ang ginawa mong endpoint sa Azure Machine Learning workspace.
>

#### Suriin ang status ng deployment sa Azure Machine Learning Workspace

1. Pumunta sa Azure Machine Learning workspace na iyong ginawa.

1. Piliin ang **Endpoints** mula sa kaliwang tab.

1. Piliin ang endpoint na iyong ginawa.

    ![Piliin ang endpoints](../../../../../../translated_images/tl/07-09-check-deployment.325d18cae8475ef4.webp)

1. Sa pahinang ito, maaari mong pamahalaan ang mga endpoint habang nagpapatuloy ang deployment process.

> [!NOTE]
> Kapag natapos na ang deployment, siguraduhing ang **Live traffic** ay nakaset sa **100%**. Kung hindi, piliin ang **Update traffic** upang baguhin ang mga setting ng traffic. Tandaan na hindi mo maaaring subukan ang modelo kapag ang traffic ay nasa 0%.
>
> ![I-set ang traffic.](../../../../../../translated_images/tl/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Senaryo 3: I-integrate sa Prompt flow at Makipag-chat gamit ang iyong custom na modelo sa Microsoft Foundry

### I-integrate ang custom na Phi-3 model sa Prompt flow

Matapos matagumpay na ma-deploy ang iyong na-fine-tune na modelo, maaari mo na itong i-integrate sa Prompt Flow upang magamit ang iyong modelo sa mga real-time na aplikasyon, na nagbibigay-daan sa iba't ibang interactive na gawain gamit ang iyong custom na Phi-3 model.

Sa pagsasanay na ito, gagawin mo ang mga sumusunod:

- Lumikha ng Microsoft Foundry Hub.
- Lumikha ng Microsoft Foundry Project.
- Lumikha ng Prompt flow.
- Magdagdag ng custom na koneksyon para sa na-fine-tune na Phi-3 model.
- I-set up ang Prompt flow upang makipag-chat sa iyong custom na Phi-3 model.

> [!NOTE]
> Maaari ka ring mag-integrate sa Promptflow gamit ang Azure ML Studio. Ang parehong proseso ng integration ay maaari ring gamitin sa Azure ML Studio.

#### Lumikha ng Microsoft Foundry Hub

Kailangan mong gumawa ng Hub bago gumawa ng Project. Ang Hub ay kumikilos tulad ng Resource Group, na nagpapahintulot sa iyong ayusin at pamahalaan ang maraming Project sa loob ng Microsoft Foundry.
1. Bisitahin ang [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Piliin ang **All hubs** mula sa kaliwang tab.

1. Piliin ang **+ New hub** mula sa navigation menu.

    ![Create hub.](../../../../../../translated_images/tl/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Gawin ang mga sumusunod na gawain:

    - Ipasok ang **Hub name**. Dapat ay isang natatanging halaga ito.
    - Piliin ang iyong Azure **Subscription**.
    - Piliin ang **Resource group** na gagamitin (gumawa ng bago kung kinakailangan).
    - Piliin ang **Location** na nais mong gamitin.
    - Piliin ang **Connect Azure AI Services** na gagamitin (gumawa ng bago kung kinakailangan).
    - Piliin ang **Connect Azure AI Search** sa **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/tl/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Piliin ang **Next**.

#### Gumawa ng Microsoft Foundry Project

1. Sa Hub na ginawa mo, piliin ang **All projects** mula sa kaliwang tab.

1. Piliin ang **+ New project** mula sa navigation menu.

    ![Select new project.](../../../../../../translated_images/tl/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Ipasok ang **Project name**. Dapat ay isang natatanging halaga ito.

    ![Create project.](../../../../../../translated_images/tl/08-05-create-project.4d97f0372f03375a.webp)

1. Piliin ang **Create a project**.

#### Magdagdag ng custom na koneksyon para sa fine-tuned na Phi-3 model

Para i-integrate ang iyong custom na Phi-3 model sa Prompt flow, kailangan mong i-save ang endpoint at key ng modelo sa isang custom na koneksyon. Tinitiyak ng setup na ito ang access sa iyong custom na Phi-3 model sa Prompt flow.

#### Itakda ang api key at endpoint uri ng fine-tuned na Phi-3 model

1. Bisitahin ang [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Pumunta sa Azure Machine learning workspace na ginawa mo.

1. Piliin ang **Endpoints** mula sa kaliwang tab.

    ![Select endpoints.](../../../../../../translated_images/tl/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Piliin ang endpoint na ginawa mo.

    ![Select endpoints.](../../../../../../translated_images/tl/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Piliin ang **Consume** mula sa navigation menu.

1. Kopyahin ang iyong **REST endpoint** at **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/tl/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Magdagdag ng Custom Connection

1. Bisitahin ang [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Pumunta sa Microsoft Foundry project na ginawa mo.

1. Sa Project na ginawa mo, piliin ang **Settings** mula sa kaliwang tab.

1. Piliin ang **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/tl/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Piliin ang **Custom keys** mula sa navigation menu.

    ![Select custom keys.](../../../../../../translated_images/tl/08-10-select-custom-keys.856f6b2966460551.webp)

1. Gawin ang mga sumusunod na gawain:

    - Piliin ang **+ Add key value pairs**.
    - Para sa pangalan ng key, ipasok ang **endpoint** at i-paste ang endpoint na kinopya mo mula sa Azure ML Studio sa value field.
    - Piliin muli ang **+ Add key value pairs**.
    - Para sa pangalan ng key, ipasok ang **key** at i-paste ang key na kinopya mo mula sa Azure ML Studio sa value field.
    - Pagkatapos idagdag ang mga keys, piliin ang **is secret** upang maiwasang maipakita ang key.

    ![Add connection.](../../../../../../translated_images/tl/08-11-add-connection.785486badb4d2d26.webp)

1. Piliin ang **Add connection**.

#### Gumawa ng Prompt flow

Nagdagdag ka na ng custom na koneksyon sa Microsoft Foundry. Ngayon, gumawa tayo ng Prompt flow gamit ang mga sumusunod na hakbang. Pagkatapos nito, iko-connect mo ang Prompt flow na ito sa custom connection upang magamit mo ang fine-tuned model sa loob ng Prompt flow.

1. Pumunta sa Microsoft Foundry project na ginawa mo.

1. Piliin ang **Prompt flow** mula sa kaliwang tab.

1. Piliin ang **+ Create** mula sa navigation menu.

    ![Select Promptflow.](../../../../../../translated_images/tl/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Piliin ang **Chat flow** mula sa navigation menu.

    ![Select chat flow.](../../../../../../translated_images/tl/08-13-select-flow-type.2ec689b22da32591.webp)

1. Ipasok ang **Folder name** na gagamitin.

    ![Enter name.](../../../../../../translated_images/tl/08-14-enter-name.ff9520fefd89f40d.webp)

2. Piliin ang **Create**.

#### Itakda ang Prompt flow para makipag-chat sa iyong custom na Phi-3 model

Kailangan mong i-integrate ang fine-tuned Phi-3 model sa Prompt flow. Gayunpaman, ang kasalukuyang ibinigay na Prompt flow ay hindi disenyo para sa layuning ito. Kaya, kailangan mong i-redisenyo ang Prompt flow upang payagan ang integrasyon ng custom na modelo.

1. Sa Prompt flow, gawin ang mga sumusunod upang muling buuin ang umiiral na flow:

    - Piliin ang **Raw file mode**.
    - Burahin ang lahat ng umiiral na code sa *flow.dag.yml* na file.
    - Idagdag ang sumusunod na code sa *flow.dag.yml* na file.

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

    - Piliin ang **Save**.

    ![Select raw file mode.](../../../../../../translated_images/tl/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Idagdag ang sumusunod na code sa *integrate_with_promptflow.py* na file upang magamit ang custom na Phi-3 model sa Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Pagsasaayos ng pag-log
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

        # Ang "connection" ay pangalan ng Custom Connection, ang "endpoint", "key" ay mga susi sa Custom Connection
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
            
            # I-log ang buong tugon ng JSON
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

    ![Paste prompt flow code.](../../../../../../translated_images/tl/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Para sa mas detalyadong impormasyon sa paggamit ng Prompt flow sa Microsoft Foundry, maaari mong tingnan ang [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Piliin ang **Chat input**, **Chat output** upang paganahin ang chat sa iyong modelo.

    ![Input Output.](../../../../../../translated_images/tl/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Handa ka na ngayong makipag-chat sa iyong custom na Phi-3 model. Sa susunod na gawain, matututuhan mo kung paano simulan ang Prompt flow at gamitin ito upang makipag-chat sa iyong fine-tuned na Phi-3 model.

> [!NOTE]
>
> Ang muling binuong flow ay dapat magmukhang tulad ng larawan sa ibaba:
>
> ![Flow example.](../../../../../../translated_images/tl/08-18-graph-example.d6457533952e690c.webp)
>

### Makipag-chat sa iyong custom na Phi-3 model

Ngayon na na-fine-tune at na-integrate mo na ang iyong custom na Phi-3 model sa Prompt flow, handa ka nang simulan ang pakikipag-ugnayan dito. Gagabayan ka ng gawaing ito sa proseso ng pagsasaayos at pagsisimula ng chat gamit ang iyong modelo sa Prompt flow. Sa pagsunod sa mga hakbang na ito, magagamit mo nang lubusan ang kakayahan ng fine-tuned na Phi-3 model para sa iba't ibang gawain at pag-uusap.

- Makipag-chat sa iyong custom na Phi-3 model gamit ang Prompt flow.

#### Simulan ang Prompt flow

1. Piliin ang **Start compute sessions** upang simulan ang Prompt flow.

    ![Start compute session.](../../../../../../translated_images/tl/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Piliin ang **Validate and parse input** upang i-renew ang mga parameter.

    ![Validate input.](../../../../../../translated_images/tl/09-02-validate-input.317c76ef766361e9.webp)

1. Piliin ang **Value** ng **connection** sa custom connection na ginawa mo. Halimbawa, *connection*.

    ![Connection.](../../../../../../translated_images/tl/09-03-select-connection.99bdddb4b1844023.webp)

#### Makipag-chat sa iyong custom na modelo

1. Piliin ang **Chat**.

    ![Select chat.](../../../../../../translated_images/tl/09-04-select-chat.61936dce6612a1e6.webp)

1. Narito ang isang halimbawa ng mga resulta: Ngayon ay maaari ka nang makipag-chat sa iyong custom na Phi-3 model. Inirerekomenda na magtanong batay sa datos na ginamit para sa fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/tl/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagsusuri**:  
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat aming pinagtutuunan ng pansin ang katumpakan, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tiyak na impormasyon. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->