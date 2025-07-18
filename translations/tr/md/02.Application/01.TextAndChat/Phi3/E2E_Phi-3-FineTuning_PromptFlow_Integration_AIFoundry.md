<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-07-17T01:27:22+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "tr"
}
-->
# Azure AI Foundry'de Prompt flow ile özel Phi-3 modellerini ince ayar yapma ve entegre etme

Bu uçtan uca (E2E) örnek, Microsoft Tech Community'den "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" rehberine dayanmaktadır. Azure AI Foundry'de Prompt flow ile özel Phi-3 modellerinin ince ayar, dağıtım ve entegrasyon süreçlerini tanıtmaktadır. Yerel olarak kod çalıştırmayı içeren "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" E2E örneğinin aksine, bu eğitim tamamen Azure AI / ML Studio içinde modelinizi ince ayar yapma ve entegre etmeye odaklanmaktadır.

## Genel Bakış

Bu E2E örnekte, Phi-3 modelini nasıl ince ayar yapacağınızı ve Azure AI Foundry'de Prompt flow ile nasıl entegre edeceğinizi öğreneceksiniz. Azure AI / ML Studio'yu kullanarak özel AI modellerini dağıtmak ve kullanmak için bir iş akışı oluşturacaksınız. Bu E2E örnek üç senaryoya ayrılmıştır:

**Senaryo 1: Azure kaynaklarını kurma ve ince ayar için hazırlık**

**Senaryo 2: Phi-3 modelini ince ayar yapma ve Azure Machine Learning Studio'da dağıtma**

**Senaryo 3: Prompt flow ile entegrasyon ve Azure AI Foundry'de özel modelinizle sohbet etme**

İşte bu E2E örneğin genel görünümü.

![Phi-3-FineTuning_PromptFlow_Integration Genel Bakış.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a2ceacdc6401c688bdf100d874fe8d55169f7723ed024781e.tr.png)

### İçindekiler

1. **[Senaryo 1: Azure kaynaklarını kurma ve ince ayar için hazırlık](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning Workspace oluşturma](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure Aboneliğinde GPU kotası talep etme](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Rol ataması ekleme](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Projeyi kurma](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [İnce ayar için veri setini hazırlama](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Senaryo 2: Phi-3 modelini ince ayar yapma ve Azure Machine Learning Studio'da dağıtma](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Phi-3 modelini ince ayar yapma](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [İnce ayar yapılmış Phi-3 modelini dağıtma](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Senaryo 3: Prompt flow ile entegrasyon ve Azure AI Foundry'de özel modelinizle sohbet etme](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Özel Phi-3 modelini Prompt flow ile entegre etme](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Özel Phi-3 modelinizle sohbet etme](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Senaryo 1: Azure kaynaklarını kurma ve ince ayar için hazırlık

### Azure Machine Learning Workspace oluşturma

1. Portal sayfasının üstündeki **arama çubuğuna** *azure machine learning* yazın ve çıkan seçeneklerden **Azure Machine Learning**'i seçin.

    ![azure machine learning yazın.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b9780de8accc31e4e1de7254e9c34a7836a955d455339e77d.tr.png)

2. Navigasyon menüsünden **+ Create** seçeneğini tıklayın.

3. Navigasyon menüsünden **New workspace** seçeneğini seçin.

    ![Yeni workspace seçin.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2cf04946c36873223099fd568e0c3ab0377c096868892fdda.tr.png)

4. Aşağıdaki işlemleri yapın:

    - Azure **Subscription**'ınızı seçin.
    - Kullanılacak **Resource group**'u seçin (gerekirse yenisini oluşturun).
    - **Workspace Name** girin. Benzersiz bir değer olmalıdır.
    - Kullanmak istediğiniz **Region**'u seçin.
    - Kullanılacak **Storage account**'u seçin (gerekirse yenisini oluşturun).
    - Kullanılacak **Key vault**'u seçin (gerekirse yenisini oluşturun).
    - Kullanılacak **Application insights**'ı seçin (gerekirse yenisini oluşturun).
    - Kullanılacak **Container registry**'yi seçin (gerekirse yenisini oluşturun).

    ![Azure machine learning bilgilerini doldurun.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090ff9ec341c724c1493e7f96726f5c810a89a7409b782a7b04a.tr.png)

5. **Review + Create** seçeneğini tıklayın.

6. **Create** seçeneğini tıklayın.

### Azure Aboneliğinde GPU kotası talep etme

Bu eğitimde, Phi-3 modelini ince ayar yapmak ve dağıtmak için GPU kullanmayı öğreneceksiniz. İnce ayar için *Standard_NC24ads_A100_v4* GPU'sunu kullanacaksınız ve bu GPU için kota talebinde bulunmanız gerekmektedir. Dağıtım için ise *Standard_NC6s_v3* GPU'sunu kullanacaksınız ve bu GPU için de kota talebi gereklidir.

> [!NOTE]
>
> Sadece Pay-As-You-Go abonelikleri (standart abonelik türü) GPU tahsisi için uygundur; avantaj abonelikleri şu anda desteklenmemektedir.
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) adresini ziyaret edin.

1. *Standard NCADSA100v4 Family* kotası talep etmek için aşağıdaki adımları izleyin:

    - Sol taraftaki sekmeden **Quota**'yı seçin.
    - Kullanılacak **Virtual machine family**'yi seçin. Örneğin, *Standard_NC24ads_A100_v4* GPU'sunu içeren **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**'u seçin.
    - Navigasyon menüsünden **Request quota**'yı seçin.

        ![Kota talep et.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd536f2e4a305c8528a34914370813bc2cda4d7bbdd2de873f0.tr.png)

    - Request quota sayfasında, kullanmak istediğiniz **New cores limit** değerini girin. Örneğin, 24.
    - Request quota sayfasında, GPU kotası talebi için **Submit**'i seçin.

1. *Standard NCSv3 Family* kotası talep etmek için aşağıdaki adımları izleyin:

    - Sol taraftaki sekmeden **Quota**'yı seçin.
    - Kullanılacak **Virtual machine family**'yi seçin. Örneğin, *Standard_NC6s_v3* GPU'sunu içeren **Standard NCSv3 Family Cluster Dedicated vCPUs**'u seçin.
    - Navigasyon menüsünden **Request quota**'yı seçin.
    - Request quota sayfasında, kullanmak istediğiniz **New cores limit** değerini girin. Örneğin, 24.
    - Request quota sayfasında, GPU kotası talebi için **Submit**'i seçin.

### Rol ataması ekleme

Modellerinizi ince ayar yapmak ve dağıtmak için önce bir User Assigned Managed Identity (UAI) oluşturmalı ve ona uygun izinleri atamalısınız. Bu UAI, dağıtım sırasında kimlik doğrulama için kullanılacaktır.

#### User Assigned Managed Identity (UAI) oluşturma

1. Portal sayfasının üstündeki **arama çubuğuna** *managed identities* yazın ve çıkan seçeneklerden **Managed Identities**'i seçin.

    ![managed identities yazın.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e52f52a152187b230243fe884f58a9940cd9b534db3dcea383.tr.png)

1. **+ Create** seçeneğini tıklayın.

    ![Create seçin.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f27b6680cd94ef6ec7557394022dafdcfba2a92777b11e4817.tr.png)

1. Aşağıdaki işlemleri yapın:

    - Azure **Subscription**'ınızı seçin.
    - Kullanılacak **Resource group**'u seçin (gerekirse yenisini oluşturun).
    - Kullanmak istediğiniz **Region**'u seçin.
    - **Name** girin. Benzersiz bir değer olmalıdır.

    ![Bilgileri doldurun.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0e313fffaecf7d6ce4ee5e86c0badcd038f03519cac63b76b.tr.png)

1. **Review + create** seçeneğini tıklayın.

1. **+ Create** seçeneğini tıklayın.

#### Managed Identity'ye Contributor rolü atama

1. Oluşturduğunuz Managed Identity kaynağına gidin.

1. Sol taraftaki sekmeden **Azure role assignments**'ı seçin.

1. Navigasyon menüsünden **+Add role assignment**'ı seçin.

1. Add role assignment sayfasında aşağıdaki işlemleri yapın:
    - **Scope**'u **Resource group** olarak seçin.
    - Azure **Subscription**'ınızı seçin.
    - Kullanılacak **Resource group**'u seçin.
    - **Role** olarak **Contributor**'ı seçin.

    ![Contributor rolünü doldurun.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d1d62333e91b4d2719284f0dad14bd9b4c3459510a0c44fab.tr.png)

2. **Save** seçeneğini tıklayın.

#### Managed Identity'ye Storage Blob Data Reader rolü atama

1. Portal sayfasının üstündeki **arama çubuğuna** *storage accounts* yazın ve çıkan seçeneklerden **Storage accounts**'u seçin.

    ![storage accounts yazın.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e55b6b4dda10841d74d1c7463a2e4f23b9c45ffbb84219deb2.tr.png)

1. Oluşturduğunuz Azure Machine Learning workspace ile ilişkili storage hesabını seçin. Örneğin, *finetunephistorage*.

1. Add role assignment sayfasına gitmek için aşağıdaki adımları izleyin:

    - Oluşturduğunuz Azure Storage hesabına gidin.
    - Sol taraftaki sekmeden **Access Control (IAM)**'ı seçin.
    - Navigasyon menüsünden **+ Add**'i seçin.
    - Navigasyon menüsünden **Add role assignment**'ı seçin.

    ![Rol ekle.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c25fb73e63b957e214a2b651375a640a3aa54159a3731f495b.tr.png)

1. Add role assignment sayfasında aşağıdaki işlemleri yapın:

    - Rol sayfasında, **arama çubuğuna** *Storage Blob Data Reader* yazın ve çıkan seçeneklerden **Storage Blob Data Reader**'ı seçin.
    - Rol sayfasında **Next**'i seçin.
    - Üyeler sayfasında, **Assign access to** olarak **Managed identity**'yi seçin.
    - Üyeler sayfasında **+ Select members**'ı seçin.
    - Select managed identities sayfasında Azure **Subscription**'ınızı seçin.
    - Select managed identities sayfasında **Managed identity** olarak **Manage Identity**'yi seçin.
    - Select managed identities sayfasında oluşturduğunuz Manage Identity'yi seçin. Örneğin, *finetunephi-managedidentity*.
    - Select managed identities sayfasında **Select**'i seçin.

    ![Managed identity seçin.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25289f2f121da05d114934d21d26aae9cb779334cbbccdf9e8.tr.png)

1. **Review + assign** seçeneğini tıklayın.

#### Managed Identity'ye AcrPull rolü atama

1. Portal sayfasının üstündeki **arama çubuğuna** *container registries* yazın ve çıkan seçeneklerden **Container registries**'i seçin.

    ![container registries yazın.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a69b003f7a698dac908ffc2f355e675c10939fdd0bb09f790e.tr.png)

1. Azure Machine Learning workspace ile ilişkili container registry'yi seçin. Örneğin, *finetunephicontainerregistry*

1. Add role assignment sayfasına gitmek için aşağıdaki adımları izleyin:

    - Sol taraftaki sekmeden **Access Control (IAM)**'ı seçin.
    - Navigasyon menüsünden **+ Add**'i seçin.
    - Navigasyon menüsünden **Add role assignment**'ı seçin.

1. Add role assignment sayfasında aşağıdaki işlemleri yapın:

    - Rol sayfasında, **arama çubuğuna** *AcrPull* yazın ve çıkan seçeneklerden **AcrPull**'u seçin.
    - Rol sayfasında **Next**'i seçin.
    - Üyeler sayfasında, **Assign access to** olarak **Managed identity**'yi seçin.
    - Üyeler sayfasında **+ Select members**'ı seçin.
    - Select managed identities sayfasında Azure **Subscription**'ınızı seçin.
    - Select managed identities sayfasında **Managed identity** olarak **Manage Identity**'yi seçin.
    - Select managed identities sayfasında oluşturduğunuz Manage Identity'yi seçin. Örneğin, *finetunephi-managedidentity*.
    - Select managed identities sayfasında **Select**'i seçin.
    - **Review + assign** seçeneğini tıklayın.

### Projeyi kurma

İnce ayar için gereken veri setlerini indirmek üzere yerel bir ortam kuracaksınız.

Bu egzersizde,

- İçinde çalışmak için bir klasör oluşturacaksınız.
- Sanal bir ortam oluşturacaksınız.
- Gerekli paketleri yükleyeceksiniz.
- Veri setini indirmek için *download_dataset.py* dosyası oluşturacaksınız.

#### İçinde çalışmak için bir klasör oluşturma

1. Bir terminal penceresi açın ve varsayılan yolda *finetune-phi* adında bir klasör oluşturmak için aşağıdaki komutu yazın.

    ```console
    mkdir finetune-phi
    ```

2. Oluşturduğunuz *finetune-phi* klasörüne gitmek için terminalde aşağıdaki komutu yazın.
#### Sanal ortam oluşturma

1. Terminalinizde *.venv* adlı bir sanal ortam oluşturmak için aşağıdaki komutu yazın.

    ```console
    python -m venv .venv
    ```

2. Sanal ortamı etkinleştirmek için terminalinize aşağıdaki komutu yazın.

    ```console
    .venv\Scripts\activate.bat
    ```


> [!NOTE]
> Eğer başarılı olduysa, komut isteminden önce *(.venv)* görmelisiniz.

#### Gerekli paketleri yükleme

1. Gerekli paketleri yüklemek için terminalinize aşağıdaki komutları yazın.

    ```console
    pip install datasets==2.19.1
    ```

#### `download_dataset.py` dosyasını oluşturma

> [!NOTE]
> Tam klasör yapısı:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code**'u açın.

1. Menü çubuğundan **File** seçeneğini seçin.

1. **Open Folder** seçeneğini seçin.

1. *C:\Users\yourUserName\finetune-phi* konumunda oluşturduğunuz *finetune-phi* klasörünü seçin.

    ![Oluşturduğunuz klasörü seçin.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6f63a0a50961e51a39cc6de7a7ddc86da5f4896e815f28abd.tr.png)

1. Visual Studio Code'un sol panelinde sağ tıklayın ve **New File** seçeneği ile *download_dataset.py* adlı yeni bir dosya oluşturun.

    ![Yeni dosya oluşturun.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff927ede875300e1b5c91ab90d1e486c77a43bb9494880cf9b6f.tr.png)

### İnce ayar için veri setini hazırlama

Bu alıştırmada, *download_dataset.py* dosyasını çalıştırarak *ultrachat_200k* veri setlerini yerel ortamınıza indireceksiniz. Daha sonra bu veri setlerini Azure Machine Learning'de Phi-3 modelini ince ayar yapmak için kullanacaksınız.

Bu alıştırmada şunları yapacaksınız:

- Veri setlerini indirmek için *download_dataset.py* dosyasına kod eklemek.
- *download_dataset.py* dosyasını çalıştırarak veri setlerini yerel ortamınıza indirmek.

#### *download_dataset.py* ile veri setinizi indirin

1. Visual Studio Code'da *download_dataset.py* dosyasını açın.

1. Aşağıdaki kodu *download_dataset.py* dosyasına ekleyin.

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

1. Terminalinize aşağıdaki komutu yazarak scripti çalıştırın ve veri setini yerel ortamınıza indirin.

    ```console
    python download_dataset.py
    ```

1. Veri setlerinin yerel *finetune-phi/data* dizinine başarıyla kaydedildiğini doğrulayın.

> [!NOTE]
>
> #### Veri seti boyutu ve ince ayar süresi hakkında not
>
> Bu eğitimde, veri setinin sadece %1'ini kullanıyorsunuz (`split='train[:1%]'`). Bu, veri miktarını önemli ölçüde azaltarak hem yükleme hem de ince ayar süreçlerini hızlandırır. Eğitim süresi ile model performansı arasında doğru dengeyi bulmak için bu yüzdeyi ayarlayabilirsiniz. Veri setinin daha küçük bir alt kümesini kullanmak, ince ayar için gereken süreyi azaltır ve süreci eğitim için daha yönetilebilir hale getirir.

## Senaryo 2: Phi-3 modelini ince ayar yapma ve Azure Machine Learning Studio'da dağıtma

### Phi-3 modelini ince ayar yapma

Bu alıştırmada, Phi-3 modelini Azure Machine Learning Studio'da ince ayar yapacaksınız.

Bu alıştırmada şunları yapacaksınız:

- İnce ayar için bilgisayar kümesi oluşturma.
- Azure Machine Learning Studio'da Phi-3 modelini ince ayar yapma.

#### İnce ayar için bilgisayar kümesi oluşturma

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) sitesini ziyaret edin.

1. Sol taraftaki sekmeden **Compute** seçeneğini seçin.

1. Navigasyon menüsünden **Compute clusters** seçeneğini seçin.

1. **+ New** seçeneğini seçin.

    ![Compute seçin.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252d04ffd0142c073486df7d3b7256335964a98b87e28072523.tr.png)

1. Aşağıdaki işlemleri yapın:

    - Kullanmak istediğiniz **Region**'ı seçin.
    - **Virtual machine tier** olarak **Dedicated** seçin.
    - **Virtual machine type** olarak **GPU** seçin.
    - **Virtual machine size** filtresini **Select from all options** olarak ayarlayın.
    - **Virtual machine size** olarak **Standard_NC24ads_A100_v4** seçin.

    ![Küme oluşturun.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e4baa9c5ccf86510f21df87515c231b2a255e1ee545496458.tr.png)

1. **Next** seçeneğini seçin.

1. Aşağıdaki işlemleri yapın:

    - **Compute name** girin. Bu benzersiz bir değer olmalıdır.
    - **Minimum number of nodes** değerini **0** olarak ayarlayın.
    - **Maximum number of nodes** değerini **1** olarak ayarlayın.
    - **Idle seconds before scale down** değerini **120** olarak ayarlayın.

    ![Küme oluşturun.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662edc0f95ad364a869b4dbb7f7be08ff259528fea96312e77e.tr.png)

1. **Create** seçeneğini seçin.

#### Phi-3 modelini ince ayar yapma

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) sitesini ziyaret edin.

1. Oluşturduğunuz Azure Machine Learning çalışma alanını seçin.

    ![Oluşturduğunuz çalışma alanını seçin.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.tr.png)

1. Aşağıdaki işlemleri yapın:

    - Sol taraftaki sekmeden **Model catalog** seçeneğini seçin.
    - **Arama çubuğuna** *phi-3-mini-4k* yazın ve çıkan seçeneklerden **Phi-3-mini-4k-instruct**'i seçin.

    ![phi-3-mini-4k yazın.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b25018a7e7353ce6525d8f5803b0af9bc9a60a9be4204dd77578.tr.png)

1. Navigasyon menüsünden **Fine-tune** seçeneğini seçin.

    ![İnce ayar seçin.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeecb897ac74882792b59086893b8a7448a89be3628aee62fc1b.tr.png)

1. Aşağıdaki işlemleri yapın:

    - **Select task type** olarak **Chat completion** seçin.
    - **+ Select data** seçeneği ile **Training data** yükleyin.
    - Doğrulama verisi yükleme türü olarak **Provide different validation data** seçin.
    - **+ Select data** seçeneği ile **Validation data** yükleyin.

    ![İnce ayar sayfasını doldurun.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0bbc6b248af9e7369ca98379770badec9f73b6bced7a8b7806.tr.png)

    > [!TIP]
    >
    > İnce ayar sürecini ihtiyaçlarınıza göre optimize etmek için **learning_rate** ve **lr_scheduler_type** gibi ayarları değiştirmek üzere **Advanced settings** seçeneğini kullanabilirsiniz.

1. **Finish** seçeneğini seçin.

1. Bu alıştırmada, Azure Machine Learning kullanarak Phi-3 modelini başarıyla ince ayar yaptınız. İnce ayar işleminin önemli bir süre alabileceğini unutmayın. İnce ayar işi çalıştıktan sonra tamamlanmasını beklemeniz gerekir. İnce ayar işinin durumunu Azure Machine Learning Çalışma Alanınızın sol tarafındaki Jobs sekmesinden takip edebilirsiniz. Sonraki seride, ince ayar yapılmış modeli dağıtacak ve Prompt flow ile entegre edeceksiniz.

    ![İnce ayar işini görün.](../../../../../../translated_images/06-08-output.2bd32e59930672b1cc1de86056e2fbc91e338f59e2a29d7dac86ede49a9714b2.tr.png)

### İnce ayar yapılmış Phi-3 modelini dağıtma

İnce ayar yapılmış Phi-3 modelini Prompt flow ile entegre etmek için modeli gerçek zamanlı çıkarım için erişilebilir hale getirmek üzere dağıtmanız gerekir. Bu süreç modelin kaydedilmesini, çevrimiçi bir uç nokta oluşturulmasını ve modelin dağıtılmasını içerir.

Bu alıştırmada şunları yapacaksınız:

- İnce ayar yapılmış modeli Azure Machine Learning çalışma alanına kaydetmek.
- Çevrimiçi bir uç nokta oluşturmak.
- Kayıtlı ince ayar yapılmış Phi-3 modelini dağıtmak.

#### İnce ayar yapılmış modeli kaydetme

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) sitesini ziyaret edin.

1. Oluşturduğunuz Azure Machine Learning çalışma alanını seçin.

    ![Oluşturduğunuz çalışma alanını seçin.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.tr.png)

1. Sol taraftaki sekmeden **Models** seçeneğini seçin.
1. **+ Register** seçeneğini seçin.
1. **From a job output** seçeneğini seçin.

    ![Modeli kaydedin.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777c8c39906ce5cd57f16b54fb3887dd4e4de1ce963b26499ad.tr.png)

1. Oluşturduğunuz işi seçin.

    ![İşi seçin.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd09315953b4eb2cc9d62d0d77ab0d9d877e34c6827fa6d2b6be4.tr.png)

1. **Next** seçeneğini seçin.

1. **Model type** olarak **MLflow** seçin.

1. **Job output** seçeneğinin seçili olduğundan emin olun; otomatik seçilmiş olmalıdır.

    ![Çıktıyı seçin.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f267b40f73de77f092a5b02808ade72f8eb94e5fe9723feb3.tr.png)

2. **Next** seçeneğini seçin.

3. **Register** seçeneğini seçin.

    ![Kaydet seçeneğini seçin.](../../../../../../translated_images/07-04-register.fd82a3b293060bc78399e613293032d3d301c02a6fd8092bec52bfaf4f3104de.tr.png)

4. Kayıtlı modelinizi sol taraftaki sekmeden **Models** menüsüne giderek görüntüleyebilirsiniz.

    ![Kayıtlı model.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591b7995686b95396ffd8c185ba66f0a1f6be18f4aea05e93d5.tr.png)

#### İnce ayar yapılmış modeli dağıtma

1. Oluşturduğunuz Azure Machine Learning çalışma alanına gidin.

1. Sol taraftaki sekmeden **Endpoints** seçeneğini seçin.

1. Navigasyon menüsünden **Real-time endpoints** seçeneğini seçin.

    ![Uç nokta oluşturun.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09618ce29b467276523838b8cc766d79ebfecdb052fef2c4df.tr.png)

1. **Create** seçeneğini seçin.

1. Oluşturduğunuz kayıtlı modeli seçin.

    ![Kayıtlı modeli seçin.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4460f7646dfaa59121fb1384ed1957755427d358462c25225.tr.png)

1. **Select** seçeneğini seçin.

1. Aşağıdaki işlemleri yapın:

    - **Virtual machine** olarak *Standard_NC6s_v3* seçin.
    - Kullanmak istediğiniz **Instance count** değerini seçin. Örneğin, *1*.
    - **Endpoint** olarak **New** seçeneğini seçerek yeni bir uç nokta oluşturun.
    - **Endpoint name** girin. Bu benzersiz bir değer olmalıdır.
    - **Deployment name** girin. Bu benzersiz bir değer olmalıdır.

    ![Dağıtım ayarlarını doldurun.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e67378494bb8d81418bc3bdaceb8c57151727d538594cb378697f36.tr.png)

1. **Deploy** seçeneğini seçin.

> [!WARNING]
> Hesabınıza ek ücret yansımaması için Azure Machine Learning çalışma alanında oluşturduğunuz uç noktayı silmeyi unutmayın.
>

#### Azure Machine Learning Çalışma Alanında dağıtım durumunu kontrol etme

1. Oluşturduğunuz Azure Machine Learning çalışma alanına gidin.

1. Sol taraftaki sekmeden **Endpoints** seçeneğini seçin.

1. Oluşturduğunuz uç noktayı seçin.

    ![Uç noktaları seçin](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4a302f0efc8875002e1c382167083c7fefbdb42ede274d0da.tr.png)

1. Bu sayfada, dağıtım sürecindeki uç noktaları yönetebilirsiniz.

> [!NOTE]
> Dağıtım tamamlandıktan sonra, **Live traffic** değerinin **%100** olarak ayarlandığından emin olun. Eğer değilse, trafik ayarlarını değiştirmek için **Update traffic** seçeneğini kullanın. Trafik %0 olarak ayarlanmışsa modeli test edemezsiniz.
>
> ![Trafiği ayarlayın.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d30c64ecabac4b17a7b5dc004ba52ad387cbaaf7b266eeadf.tr.png)
>

## Senaryo 3: Prompt flow ile entegrasyon ve Azure AI Foundry'de özel modelinizle sohbet

### Özel Phi-3 modelini Prompt flow ile entegre etme

İnce ayar yapılmış modelinizi başarıyla dağıttıktan sonra, modelinizi gerçek zamanlı uygulamalarda kullanmak için Prompt Flow ile entegre edebilirsiniz. Bu sayede özel Phi-3 modelinizle çeşitli etkileşimli görevler gerçekleştirebilirsiniz.

Bu alıştırmada şunları yapacaksınız:

- Azure AI Foundry Hub oluşturma.
- Azure AI Foundry Projesi oluşturma.
- Prompt flow oluşturma.
- İnce ayar yapılmış Phi-3 modeli için özel bağlantı ekleme.
- Prompt flow'u özel Phi-3 modelinizle sohbet edecek şekilde ayarlama.
> [!NOTE]
> Azure ML Studio kullanarak Promptflow ile entegrasyon da yapabilirsiniz. Aynı entegrasyon süreci Azure ML Studio için de geçerlidir.
#### Azure AI Foundry Hub Oluşturma

Proje oluşturmadan önce bir Hub oluşturmanız gerekir. Hub, bir Kaynak Grubu gibi davranır ve Azure AI Foundry içinde birden fazla Projeyi organize edip yönetmenizi sağlar.

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) sitesini ziyaret edin.

1. Sol taraftaki sekmeden **All hubs** seçeneğini seçin.

1. Navigasyon menüsünden **+ New hub** seçeneğini seçin.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834e092dcf9dda773276fbee65f40252ed4a9af4f9aa4fef5d7.tr.png)

1. Aşağıdaki işlemleri yapın:

    - **Hub name** girin. Bu benzersiz bir değer olmalıdır.
    - Azure **Subscription** seçin.
    - Kullanmak istediğiniz **Resource group** seçin (gerekirse yeni bir tane oluşturun).
    - Kullanmak istediğiniz **Location** seçin.
    - Kullanmak istediğiniz **Connect Azure AI Services** seçin (gerekirse yeni bir tane oluşturun).
    - **Connect Azure AI Search** için **Skip connecting** seçeneğini seçin.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c44658a87c2ed01d9e588581f157480ff1ac3312085c51d25.tr.png)

1. **Next** seçeneğini seçin.

#### Azure AI Foundry Projesi Oluşturma

1. Oluşturduğunuz Hub içinde, sol taraftaki sekmeden **All projects** seçeneğini seçin.

1. Navigasyon menüsünden **+ New project** seçeneğini seçin.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f1251c487d98aed0641bd057100b8e5d6fba9062bfb7d752ce9.tr.png)

1. **Project name** girin. Bu benzersiz bir değer olmalıdır.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a192b4ed3dde6b1136c860fc85352d612aa2f3ae8a4d54eb4.tr.png)

1. **Create a project** seçeneğini seçin.

#### İnce Ayarlanmış Phi-3 modeli için özel bağlantı ekleme

Özel Phi-3 modelinizi Prompt flow ile entegre etmek için modelin endpoint ve anahtarını özel bir bağlantıda kaydetmeniz gerekir. Bu yapılandırma, Prompt flow içinde özel Phi-3 modelinize erişimi sağlar.

#### İnce ayarlanmış Phi-3 modelinin api anahtarı ve endpoint uri'sini ayarlama

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) sitesini ziyaret edin.

1. Oluşturduğunuz Azure Machine learning çalışma alanına gidin.

1. Sol taraftaki sekmeden **Endpoints** seçeneğini seçin.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf960519c1ac95116d1a7e5b8d0bdea5cd42281930766fbfad1929.tr.png)

1. Oluşturduğunuz endpoint'i seçin.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275ea16f689f59b70d5b0162fff1781204e389edcb63b42b95b2.tr.png)

1. Navigasyon menüsünden **Consume** seçeneğini seçin.

1. **REST endpoint** ve **Primary key** değerlerini kopyalayın.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cbe30a20b889154d04109bf17c5c09816060a8689933dc0fd7.tr.png)

#### Özel Bağlantı Ekleme

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) sitesini ziyaret edin.

1. Oluşturduğunuz Azure AI Foundry projesine gidin.

1. Oluşturduğunuz Proje içinde, sol taraftaki sekmeden **Settings** seçeneğini seçin.

1. **+ New connection** seçeneğini seçin.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc77130c3a16fbb8ee59407ecbf74fd3502cb8720c61384446.tr.png)

1. Navigasyon menüsünden **Custom keys** seçeneğini seçin.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b29664605513ccc134f1adaefaf27f951981c511783a6a0d1118c9178a5.tr.png)

1. Aşağıdaki işlemleri yapın:

    - **+ Add key value pairs** seçeneğini seçin.
    - Anahtar adı olarak **endpoint** girin ve Azure ML Studio’dan kopyaladığınız endpoint’i değer alanına yapıştırın.
    - Tekrar **+ Add key value pairs** seçeneğini seçin.
    - Anahtar adı olarak **key** girin ve Azure ML Studio’dan kopyaladığınız anahtarı değer alanına yapıştırın.
    - Anahtarları ekledikten sonra, anahtarın görünmesini engellemek için **is secret** seçeneğini işaretleyin.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26e8df1bbd0948e06aa20aa0dc102faa96c8144722ef7f0b72.tr.png)

1. **Add connection** seçeneğini seçin.

#### Prompt flow Oluşturma

Azure AI Foundry içinde özel bir bağlantı eklediniz. Şimdi aşağıdaki adımları izleyerek bir Prompt flow oluşturacağız. Daha sonra bu Prompt flow’u özel bağlantıya bağlayarak ince ayarlı modeli Prompt flow içinde kullanabileceksiniz.

1. Oluşturduğunuz Azure AI Foundry projesine gidin.

1. Sol taraftaki sekmeden **Prompt flow** seçeneğini seçin.

1. Navigasyon menüsünden **+ Create** seçeneğini seçin.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5ba79bedfd35e2f2fb430f344844994375680fcfc111a994ae.tr.png)

1. Navigasyon menüsünden **Chat flow** seçeneğini seçin.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591f6cc6360bc35c8fca8d63519c09111c6c431de9b46eed143.tr.png)

1. Kullanmak istediğiniz **Folder name** girin.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d824bad779a54e55d808a09394b6b730fbea55d78421f52ff.tr.png)

2. **Create** seçeneğini seçin.

#### Prompt flow’u özel Phi-3 modelinizle sohbet edecek şekilde ayarlama

İnce ayarlı Phi-3 modelinizi Prompt flow’a entegre etmeniz gerekiyor. Ancak mevcut Prompt flow bu amaç için tasarlanmamıştır. Bu nedenle, özel modelin entegrasyonunu sağlamak için Prompt flow’u yeniden tasarlamanız gerekir.

1. Prompt flow içinde, mevcut akışı yeniden oluşturmak için aşağıdaki işlemleri yapın:

    - **Raw file mode** seçeneğini seçin.
    - *flow.dag.yml* dosyasındaki tüm mevcut kodu silin.
    - Aşağıdaki kodu *flow.dag.yml* dosyasına ekleyin.

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

    - **Save** seçeneğini seçin.

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985b76e070bf170e1d0d0d26b38d93bc635624642191f715a6d.tr.png)

1. Prompt flow içinde özel Phi-3 modelini kullanmak için *integrate_with_promptflow.py* dosyasına aşağıdaki kodu ekleyin.

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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d097779ab1c429be9fc07e3f4171e41fbbfb747a6e755816411e6d.tr.png)

> [!NOTE]
> Azure AI Foundry’de Prompt flow kullanımı hakkında daha ayrıntılı bilgi için [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) sayfasına bakabilirsiniz.

1. Modelinizle sohbeti etkinleştirmek için **Chat input**, **Chat output** seçeneklerini seçin.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03ba022a21159e51d544c6e063e73c10e772c942d4e44da0d30.tr.png)

1. Artık özel Phi-3 modelinizle sohbet etmeye hazırsınız. Bir sonraki alıştırmada, Prompt flow’u nasıl başlatacağınızı ve ince ayarlı Phi-3 modelinizle sohbet etmek için nasıl kullanacağınızı öğreneceksiniz.

> [!NOTE]
>
> Yeniden oluşturulan akış aşağıdaki görseldeki gibi olmalıdır:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c10b7375192511a8e2aba847e442b294a2e65d88ffac8f63b.tr.png)
>

### Özel Phi-3 modelinizle sohbet etme

Artık özel Phi-3 modelinizi ince ayarladınız ve Prompt flow ile entegre ettiniz, modelinizle etkileşime geçmeye hazırsınız. Bu alıştırma, Prompt flow kullanarak modelinizle sohbet başlatma ve ayarlama sürecinde size rehberlik edecektir. Bu adımları takip ederek, ince ayarlı Phi-3 modelinizin çeşitli görevler ve sohbetler için sunduğu yeteneklerden tam olarak faydalanabileceksiniz.

- Prompt flow kullanarak özel Phi-3 modelinizle sohbet edin.

#### Prompt flow’u başlatma

1. Prompt flow’u başlatmak için **Start compute sessions** seçeneğini seçin.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b4809b60d75ce9b0ad53e0729cc1449935ccbe90b954401dc.tr.png)

1. Parametreleri yenilemek için **Validate and parse input** seçeneğini seçin.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e97038d7529b9060a23dc59d7ddbeb38ac9c4562ef4f5b32f7.tr.png)

1. Oluşturduğunuz özel bağlantının **connection** değerini seçin. Örneğin, *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b184402368a6ec383814b139686118331a5b2eefa489678902269dfc.tr.png)

#### Özel modelinizle sohbet etme

1. **Chat** seçeneğini seçin.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e636a5e1516b6c64fdf2345ceb3142db2bed93ab7e6f03bbb2.tr.png)

1. İşte sonuçlara bir örnek: Artık özel Phi-3 modelinizle sohbet edebilirsiniz. İnce ayar için kullanılan verilere dayalı sorular sormanız önerilir.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126fa4886e6fd0e7482cfdc6c907fa36f7f2f13d04126f9eda14.tr.png)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.