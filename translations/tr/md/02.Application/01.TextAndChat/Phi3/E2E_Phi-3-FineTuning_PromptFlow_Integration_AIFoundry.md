<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-05-09T18:05:21+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "tr"
}
-->
# Azure AI Foundry'de Prompt flow ile özel Phi-3 modellerini ince ayar yapma ve entegre etme

Bu uçtan uca (E2E) örnek, Microsoft Tech Community'den "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" rehberine dayanmaktadır. Azure AI Foundry'de özel Phi-3 modellerinin ince ayar yapılması, dağıtılması ve Prompt flow ile entegrasyon süreçlerini tanıtmaktadır. Kodun yerel olarak çalıştırıldığı "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" E2E örneğinin aksine, bu eğitim tamamen Azure AI / ML Studio içinde modelinizi ince ayar yapma ve entegre etmeye odaklanmaktadır.

## Genel Bakış

Bu E2E örnekte, Phi-3 modelini nasıl ince ayar yapacağınızı ve Azure AI Foundry'de Prompt flow ile nasıl entegre edeceğinizi öğreneceksiniz. Azure AI / ML Studio'yu kullanarak, özel AI modellerini dağıtmak ve kullanmak için bir iş akışı oluşturacaksınız. Bu E2E örnek üç senaryoya ayrılmıştır:

**Senaryo 1: Azure kaynaklarını kurma ve ince ayar için hazırlık**

**Senaryo 2: Phi-3 modelini ince ayar yapma ve Azure Machine Learning Studio'da dağıtma**

**Senaryo 3: Prompt flow ile entegrasyon ve Azure AI Foundry'de özel modelinizle sohbet etme**

İşte bu E2E örneğin genel görünümü.

![Phi-3-FineTuning_PromptFlow_Integration Genel Bakış.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.tr.png)

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

    ![Azure machine learning yazın.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.tr.png)

2. Navigasyon menüsünden **+ Create** seçeneğini tıklayın.

3. Navigasyon menüsünden **New workspace** seçeneğini seçin.

    ![Yeni workspace seçin.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.tr.png)

4. Aşağıdaki adımları gerçekleştirin:

    - Azure **Subscription**'ınızı seçin.
    - Kullanılacak **Resource group**'u seçin (gerekirse yenisini oluşturun).
    - **Workspace Name** girin. Benzersiz bir değer olmalıdır.
    - Kullanmak istediğiniz **Region**'u seçin.
    - Kullanılacak **Storage account**'u seçin (gerekirse yenisini oluşturun).
    - Kullanılacak **Key vault**'u seçin (gerekirse yenisini oluşturun).
    - Kullanılacak **Application insights**'ı seçin (gerekirse yenisini oluşturun).
    - Kullanılacak **Container registry**'yi seçin (gerekirse yenisini oluşturun).

    ![Azure machine learning bilgilerini doldurun.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.tr.png)

5. **Review + Create** seçeneğini tıklayın.

6. **Create** seçeneğini tıklayın.

### Azure Aboneliğinde GPU kotası talep etme

Bu eğitimde, Phi-3 modelini ince ayar yapmak ve dağıtmak için GPU'lar kullanılacaktır. İnce ayar için *Standard_NC24ads_A100_v4* GPU kullanılacak ve bu GPU için kota talebi yapılması gerekiyor. Dağıtım için ise *Standard_NC6s_v3* GPU kullanılacak ve bu GPU için de kota talebi yapılmalıdır.

> [!NOTE]
>
> Yalnızca Pay-As-You-Go abonelikleri (standart abonelik türü) GPU tahsisi için uygundur; avantaj abonelikleri şu anda desteklenmemektedir.
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) adresini ziyaret edin.

1. *Standard NCADSA100v4 Family* kotası talep etmek için aşağıdaki adımları izleyin:

    - Sol taraftaki sekmeden **Quota**'yı seçin.
    - Kullanılacak **Virtual machine family**'yi seçin. Örneğin, *Standard NCADSA100v4 Family Cluster Dedicated vCPUs* (bu, *Standard_NC24ads_A100_v4* GPU'yu içerir).
    - Navigasyon menüsünden **Request quota** seçeneğini seçin.

        ![Kota talep edin.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.tr.png)

    - Request quota sayfasında, kullanmak istediğiniz **New cores limit** değerini girin. Örneğin, 24.
    - Request quota sayfasında **Submit** seçeneğini tıklayarak GPU kotası talebinde bulunun.

1. *Standard NCSv3 Family* kotası talep etmek için aşağıdaki adımları izleyin:

    - Sol taraftaki sekmeden **Quota**'yı seçin.
    - Kullanılacak **Virtual machine family**'yi seçin. Örneğin, *Standard NCSv3 Family Cluster Dedicated vCPUs* (bu, *Standard_NC6s_v3* GPU'yu içerir).
    - Navigasyon menüsünden **Request quota** seçeneğini seçin.
    - Request quota sayfasında, kullanmak istediğiniz **New cores limit** değerini girin. Örneğin, 24.
    - Request quota sayfasında **Submit** seçeneğini tıklayarak GPU kotası talebinde bulunun.

### Rol ataması ekleme

Modellerinizi ince ayar yapmak ve dağıtmak için öncelikle bir User Assigned Managed Identity (UAI) oluşturmanız ve ona uygun izinleri atamanız gerekir. Bu UAI, dağıtım sırasında kimlik doğrulama için kullanılacaktır.

#### User Assigned Managed Identity (UAI) oluşturma

1. Portal sayfasının üstündeki **arama çubuğuna** *managed identities* yazın ve çıkan seçeneklerden **Managed Identities**'i seçin.

    ![Managed identities yazın.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.tr.png)

1. **+ Create** seçeneğini tıklayın.

    ![Create seçin.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.tr.png)

1. Aşağıdaki adımları gerçekleştirin:

    - Azure **Subscription**'ınızı seçin.
    - Kullanılacak **Resource group**'u seçin (gerekirse yenisini oluşturun).
    - Kullanmak istediğiniz **Region**'u seçin.
    - **Name** girin. Benzersiz bir değer olmalıdır.

    ![Managed identities bilgilerini doldurun.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.tr.png)

1. **Review + create** seçeneğini tıklayın.

1. **+ Create** seçeneğini tıklayın.

#### Managed Identity'ye Contributor rolü atama

1. Oluşturduğunuz Managed Identity kaynağına gidin.

1. Sol taraftaki sekmeden **Azure role assignments** seçeneğini seçin.

1. Navigasyon menüsünden **+Add role assignment** seçeneğini seçin.

1. Add role assignment sayfasında aşağıdaki adımları yapın:
    - **Scope** olarak **Resource group** seçin.
    - Azure **Subscription**'ınızı seçin.
    - Kullanılacak **Resource group**'u seçin.
    - **Role** olarak **Contributor** seçin.

    ![Contributor rolünü doldurun.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.tr.png)

2. **Save** seçeneğini tıklayın.

#### Managed Identity'ye Storage Blob Data Reader rolü atama

1. Portal sayfasının üstündeki **arama çubuğuna** *storage accounts* yazın ve çıkan seçeneklerden **Storage accounts**'u seçin.

    ![Storage accounts yazın.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.tr.png)

1. Oluşturduğunuz Azure Machine Learning workspace ile ilişkili storage hesabını seçin. Örneğin, *finetunephistorage*.

1. Add role assignment sayfasına gitmek için aşağıdaki adımları izleyin:

    - Oluşturduğunuz Azure Storage hesabına gidin.
    - Sol taraftaki sekmeden **Access Control (IAM)**'ı seçin.
    - Navigasyon menüsünden **+ Add** seçeneğini seçin.
    - Navigasyon menüsünden **Add role assignment** seçeneğini seçin.

    ![Rol ekle.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.tr.png)

1. Add role assignment sayfasında aşağıdaki adımları gerçekleştirin:

    - Rol sayfasında, **arama çubuğuna** *Storage Blob Data Reader* yazın ve çıkan seçeneklerden **Storage Blob Data Reader**'ı seçin.
    - Rol sayfasında **Next** seçeneğini tıklayın.
    - Üyeler sayfasında **Assign access to** olarak **Managed identity** seçin.
    - Üyeler sayfasında **+ Select members** seçeneğini tıklayın.
    - Managed identities seçme sayfasında Azure **Subscription**'ınızı seçin.
    - Managed identities seçme sayfasında **Managed identity** olarak **Manage Identity** seçin.
    - Oluşturduğunuz Manage Identity'yi seçin. Örneğin, *finetunephi-managedidentity*.
    - Managed identities seçme sayfasında **Select** seçeneğini tıklayın.

    ![Managed identity seçin.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.tr.png)

1. **Review + assign** seçeneğini tıklayın.

#### Managed Identity'ye AcrPull rolü atama

1. Portal sayfasının üstündeki **arama çubuğuna** *container registries* yazın ve çıkan seçeneklerden **Container registries**'yi seçin.

    ![Container registries yazın.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.tr.png)

1. Azure Machine Learning workspace ile ilişkili container registry'i seçin. Örneğin, *finetunephicontainerregistry*

1. Add role assignment sayfasına gitmek için aşağıdaki adımları izleyin:

    - Sol taraftaki sekmeden **Access Control (IAM)** seçin.
    - Navigasyon menüsünden **+ Add** seçeneğini seçin.
    - Navigasyon menüsünden **Add role assignment** seçeneğini seçin.

1. Add role assignment sayfasında aşağıdaki adımları gerçekleştirin:

    - Rol sayfasında, **arama çubuğuna** *AcrPull* yazın ve çıkan seçeneklerden **AcrPull**'u seçin.
    - Rol sayfasında **Next** seçeneğini tıklayın.
    - Üyeler sayfasında **Assign access to** olarak **Managed identity** seçin.
    - Üyeler sayfasında **+ Select members** seçeneğini tıklayın.
    - Managed identities seçme sayfasında Azure **Subscription**'ınızı seçin.
    - Managed identities seçme sayfasında **Managed identity** olarak **Manage Identity** seçin.
    - Oluşturduğunuz Manage Identity'yi seçin. Örneğin, *finetunephi-managedidentity*.
    - Managed identities seçme sayfasında **Select** seçeneğini tıklayın.
    - **Review + assign** seçeneğini tıklayın.

### Projeyi kurma

İnce ayar için gereken veri setlerini indirmek üzere yerel bir ortam kuracaksınız.

Bu egzersizde:

- İçinde çalışmak için bir klasör oluşturacaksınız.
- Sanal ortam oluşturacaksınız.
- Gerekli paketleri yükleyeceksiniz.
- Veri setini indirmek için *download_dataset.py* dosyası oluşturacaksınız.

#### Çalışmak için bir klasör oluşturma

1. Bir terminal penceresi açın ve varsayılan dizinde *finetune-phi* adlı bir klasör oluşturmak için aşağıdaki komutu yazın.

    ```console
    mkdir finetune-phi
    ```

2. Terminalde aşağıdaki komutu yazarak oluşturduğunuz *finetune-phi* klasörüne gidin.

    ```console
    cd finetune-phi
    ```

#### Sanal ortam oluşturma

1. Terminalde aşağıdaki komutu yazarak *.venv* adlı bir sanal ortam oluşturun.

    ```console
    python -m venv .venv
    ```

2. Terminalde aşağıdaki komutu yazarak sanal ortamı etkinleştirin.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Eğer başarılı olduysa, komut satırından önce *(.venv)* görünmelidir.

#### Gerekli paketleri yükleme

1. Terminalde aşağıdaki komutları yazarak gerekli paketleri yükleyin.

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

1. Oluşturduğunuz *finetune-phi* klasörünü seçin. Örneğin, *C:\Users\yourUserName\finetune-phi*.

    ![Oluşturduğunuz klasörü seçin.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.tr.png)

1. Visual Studio Code'un sol panelinde sağ tıklayın ve **New File** seçeneğini seçerek *download_dataset.py* adlı yeni bir dosya oluşturun.

    ![Yeni dosya oluşturun.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.tr.png)

### İnce ayar için veri setini hazırlama

Bu egzersizde, *download_dataset.py* dosyasını çalıştırarak *ultrachat_200k* veri setlerini yerel ortamınıza indireceksiniz. Daha sonra bu veri setlerini Azure Machine Learning'de Phi-3 modelini ince ayar yapmak için kullanacaksınız.

Bu egzersizde:

- *download_dataset.py* dosyasına veri setini indirmek için kod ekleyeceksiniz.
- *download_dataset.py* dosyasını çalıştırarak veri setini yerel ortamınıza indireceksiniz.

#### *download_dataset.py* kullanarak veri setinizi indirme

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

1. Terminalde aşağıdaki komutu yazarak scripti çalıştırın ve veri setini yerel ortamınıza indirin.

    ```console
    python download_dataset.py
    ```

1. Veri setlerinin yerel *finetune-phi/data* dizinine başarıyla kaydedildiğini doğrulayın.

> [!NOTE]
>
> #### Veri seti boyutu ve ince ayar süresi hakkında not
>
> Bu eğitimde, veri setinin yalnızca %1'ini (`split='train[:1%]'`) kullanıyorsunuz. Bu, veri miktarını önemli ölçüde azaltır ve hem yükleme hem de ince ayar süreçlerini hızlandırır. Eğitim süresi ile model performansı arasında doğru dengeyi bulmak için bu yüzdeyi ayarlayabilirsiniz. Veri setinin daha küçük bir alt kümesini kullanmak, ince ayar süresini kısaltarak eğitimi daha yönetilebilir hale getirir.

## Senaryo 2: Phi-3 modelini ince ayar yapma ve Azure Machine Learning Studio
1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) sitesini ziyaret edin.

1. Sol taraftaki sekmeden **Compute** seçeneğini seçin.

1. Navigasyon menüsünden **Compute clusters** seçeneğini seçin.

1. **+ New** seçeneğini seçin.

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.tr.png)

1. Aşağıdaki işlemleri yapın:

    - Kullanmak istediğiniz **Region**'u seçin.
    - **Virtual machine tier** seçeneğini **Dedicated** olarak ayarlayın.
    - **Virtual machine type** seçeneğini **GPU** olarak ayarlayın.
    - **Virtual machine size** filtresini **Select from all options** olarak ayarlayın.
    - **Virtual machine size** olarak **Standard_NC24ads_A100_v4** seçin.

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.tr.png)

1. **Next** seçeneğini seçin.

1. Aşağıdaki işlemleri yapın:

    - **Compute name** girin. Bu değer benzersiz olmalıdır.
    - **Minimum number of nodes** değerini **0** olarak ayarlayın.
    - **Maximum number of nodes** değerini **1** olarak ayarlayın.
    - **Idle seconds before scale down** değerini **120** olarak ayarlayın.

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.tr.png)

1. **Create** seçeneğini seçin.

#### Phi-3 modelini ince ayar yapma

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) sitesini ziyaret edin.

1. Oluşturduğunuz Azure Machine Learning çalışma alanını seçin.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.tr.png)

1. Aşağıdaki işlemleri yapın:

    - Sol taraftaki sekmeden **Model catalog** seçeneğini seçin.
    - **Arama çubuğuna** *phi-3-mini-4k* yazın ve çıkan seçeneklerden **Phi-3-mini-4k-instruct** seçeneğini seçin.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.tr.png)

1. Navigasyon menüsünden **Fine-tune** seçeneğini seçin.

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.tr.png)

1. Aşağıdaki işlemleri yapın:

    - **Select task type** seçeneğini **Chat completion** olarak ayarlayın.
    - **+ Select data** seçeneğini kullanarak **Traning data** yükleyin.
    - Doğrulama verisi yükleme türünü **Provide different validation data** olarak ayarlayın.
    - **+ Select data** seçeneğini kullanarak **Validation data** yükleyin.

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.tr.png)

    > [!TIP]
    >
    > İnce ayar sürecini ihtiyaçlarınıza göre optimize etmek için **learning_rate** ve **lr_scheduler_type** gibi ayarları özelleştirmek üzere **Advanced settings** seçeneğini kullanabilirsiniz.

1. **Finish** seçeneğini seçin.

1. Bu alıştırmada, Azure Machine Learning kullanarak Phi-3 modelini başarıyla ince ayar yaptınız. İnce ayar işleminin oldukça zaman alabileceğini unutmayın. İnce ayar işlemi başladıktan sonra tamamlanmasını beklemeniz gerekmektedir. İnce ayar işleminin durumunu Azure Machine Learning çalışma alanınızdaki sol taraftaki Jobs sekmesinden takip edebilirsiniz. Sonraki bölümde, ince ayar yapılan modeli dağıtacak ve Prompt flow ile entegre edeceksiniz.

    ![See finetuning job.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.tr.png)

### İnce ayar yapılan Phi-3 modelini dağıtma

İnce ayar yapılan Phi-3 modelini Prompt flow ile entegre etmek için modeli gerçek zamanlı çıkarım için erişilebilir hale getirmek üzere dağıtmanız gerekir. Bu işlem, modelin kaydedilmesini, çevrimiçi bir uç nokta oluşturulmasını ve modelin dağıtılmasını içerir.

Bu alıştırmada şunları yapacaksınız:

- İnce ayar yapılan modeli Azure Machine Learning çalışma alanına kaydetmek.
- Çevrimiçi bir uç nokta oluşturmak.
- Kaydedilen ince ayar yapılan Phi-3 modelini dağıtmak.

#### İnce ayar yapılan modeli kaydetme

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) sitesini ziyaret edin.

1. Oluşturduğunuz Azure Machine Learning çalışma alanını seçin.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.tr.png)

1. Sol taraftaki sekmeden **Models** seçeneğini seçin.
1. **+ Register** seçeneğini seçin.
1. **From a job output** seçeneğini seçin.

    ![Register model.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.tr.png)

1. Oluşturduğunuz işi seçin.

    ![Select job.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.tr.png)

1. **Next** seçeneğini seçin.

1. **Model type** olarak **MLflow** seçeneğini ayarlayın.

1. **Job output** seçeneğinin seçili olduğundan emin olun; otomatik olarak seçilmiş olmalıdır.

    ![Select output.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.tr.png)

2. **Next** seçeneğini seçin.

3. **Register** seçeneğini seçin.

    ![Select register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.tr.png)

4. Kaydettiğiniz modeli sol taraftaki sekmeden **Models** menüsüne giderek görüntüleyebilirsiniz.

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.tr.png)

#### İnce ayar yapılan modeli dağıtma

1. Oluşturduğunuz Azure Machine Learning çalışma alanına gidin.

1. Sol taraftaki sekmeden **Endpoints** seçeneğini seçin.

1. Navigasyon menüsünden **Real-time endpoints** seçeneğini seçin.

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.tr.png)

1. **Create** seçeneğini seçin.

1. Oluşturduğunuz kayıtlı modeli seçin.

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.tr.png)

1. **Select** seçeneğini seçin.

1. Aşağıdaki işlemleri yapın:

    - **Virtual machine** olarak *Standard_NC6s_v3* seçin.
    - Kullanmak istediğiniz **Instance count** değerini seçin. Örneğin, *1*.
    - **Endpoint** olarak **New** seçeneğini seçerek yeni bir uç nokta oluşturun.
    - **Endpoint name** girin. Bu benzersiz bir değer olmalıdır.
    - **Deployment name** girin. Bu da benzersiz olmalıdır.

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.tr.png)

1. **Deploy** seçeneğini seçin.

> [!WARNING]
> Hesabınıza ek ücret yansımaması için, Azure Machine Learning çalışma alanında oluşturduğunuz uç noktayı silmeyi unutmayın.
>

#### Azure Machine Learning Workspace içinde dağıtım durumunu kontrol etme

1. Oluşturduğunuz Azure Machine Learning çalışma alanına gidin.

1. Sol taraftaki sekmeden **Endpoints** seçeneğini seçin.

1. Oluşturduğunuz uç noktayı seçin.

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.tr.png)

1. Bu sayfada, dağıtım sürecinde uç noktaları yönetebilirsiniz.

> [!NOTE]
> Dağıtım tamamlandığında, **Live traffic** değerinin **%100** olduğundan emin olun. Eğer değilse, trafiği ayarlamak için **Update traffic** seçeneğini kullanın. Trafik %0 olarak ayarlanmışsa modeli test edemezsiniz.
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.tr.png)
>

## Senaryo 3: Prompt flow ile entegrasyon ve Azure AI Foundry’de özel modelinizle sohbet

### Özel Phi-3 modelini Prompt flow ile entegre etme

İnce ayar yaptığınız modeli başarıyla dağıttıktan sonra, Prompt Flow ile entegre ederek modelinizi gerçek zamanlı uygulamalarda kullanabilir ve özel Phi-3 modelinizle çeşitli etkileşimli görevler gerçekleştirebilirsiniz.

Bu alıştırmada şunları yapacaksınız:

- Azure AI Foundry Hub oluşturma.
- Azure AI Foundry Projesi oluşturma.
- Prompt flow oluşturma.
- İnce ayar yapılan Phi-3 modeli için özel bağlantı ekleme.
- Prompt flow'u özel Phi-3 modelinizle sohbet edecek şekilde ayarlama.

> [!NOTE]
> Azure ML Studio kullanarak da Promptflow ile entegrasyon yapabilirsiniz. Aynı entegrasyon süreci Azure ML Studio için de geçerlidir.

#### Azure AI Foundry Hub oluşturma

Proje oluşturmadan önce bir Hub oluşturmanız gerekir. Hub, Azure AI Foundry içinde birden fazla projeyi organize edip yönetmenizi sağlayan bir Kaynak Grubu gibi çalışır.

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) sitesini ziyaret edin.

1. Sol taraftaki sekmeden **All hubs** seçeneğini seçin.

1. Navigasyon menüsünden **+ New hub** seçeneğini seçin.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.tr.png)

1. Aşağıdaki işlemleri yapın:

    - **Hub name** girin. Bu benzersiz bir değer olmalıdır.
    - Azure **Subscription** seçin.
    - Kullanılacak **Resource group** seçin (gerekirse yenisini oluşturun).
    - Kullanmak istediğiniz **Location** seçin.
    - Kullanılacak **Connect Azure AI Services** seçeneğini seçin (gerekirse yenisini oluşturun).
    - **Connect Azure AI Search** seçeneğini **Skip connecting** olarak ayarlayın.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.tr.png)

1. **Next** seçeneğini seçin.

#### Azure AI Foundry Projesi oluşturma

1. Oluşturduğunuz Hub’da sol taraftaki sekmeden **All projects** seçeneğini seçin.

1. Navigasyon menüsünden **+ New project** seçeneğini seçin.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.tr.png)

1. **Project name** girin. Bu benzersiz bir değer olmalıdır.

    ![Create project.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.tr.png)

1. **Create a project** seçeneğini seçin.

#### İnce ayar yapılan Phi-3 modeli için özel bağlantı ekleme

Özel Phi-3 modelinizi Prompt flow ile entegre etmek için modelin uç noktası ve anahtarını özel bir bağlantıda kaydetmeniz gerekir. Bu ayar, Prompt flow’da özel Phi-3 modelinize erişimi sağlar.

#### İnce ayar yapılan Phi-3 modelinin api anahtarı ve uç nokta URI’sini ayarlama

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) sitesini ziyaret edin.

1. Oluşturduğunuz Azure Machine Learning çalışma alanına gidin.

1. Sol taraftaki sekmeden **Endpoints** seçeneğini seçin.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.tr.png)

1. Oluşturduğunuz uç noktayı seçin.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.tr.png)

1. Navigasyon menüsünden **Consume** seçeneğini seçin.

1. **REST endpoint** ve **Primary key** değerlerinizi kopyalayın.
![API anahtarını ve uç nokta URI'sini kopyalayın.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.tr.png)

#### Özel Bağlantıyı Ekle

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) sitesini ziyaret edin.

1. Oluşturduğunuz Azure AI Foundry projesine gidin.

1. Oluşturduğunuz projede, sol taraftaki sekmeden **Ayarlar**'ı seçin.

1. **+ Yeni bağlantı** seçeneğini tıklayın.

    ![Yeni bağlantı seçin.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.tr.png)

1. Navigasyon menüsünden **Özel anahtarlar**'ı seçin.

    ![Özel anahtarları seçin.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.tr.png)

1. Aşağıdaki işlemleri gerçekleştirin:

    - **+ Anahtar-değer çiftleri ekle**'yi seçin.
    - Anahtar adı olarak **endpoint** yazın ve Azure ML Studio’dan kopyaladığınız uç noktayı değer alanına yapıştırın.
    - Tekrar **+ Anahtar-değer çiftleri ekle**'yi seçin.
    - Anahtar adı olarak **key** yazın ve Azure ML Studio’dan kopyaladığınız anahtarı değer alanına yapıştırın.
    - Anahtarları ekledikten sonra, anahtarın görünmesini engellemek için **gizli olarak işaretle** seçeneğini işaretleyin.

    ![Bağlantı ekle.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.tr.png)

1. **Bağlantı ekle**'yi seçin.

#### Prompt flow Oluşturma

Azure AI Foundry’de özel bağlantı eklediniz. Şimdi aşağıdaki adımları izleyerek bir Prompt flow oluşturacağız. Daha sonra bu Prompt flow’u özel bağlantıya bağlayarak, ince ayarlı modeli Prompt flow içinde kullanabileceksiniz.

1. Oluşturduğunuz Azure AI Foundry projesine gidin.

1. Sol taraftaki sekmeden **Prompt flow**'u seçin.

1. Navigasyon menüsünden **+ Oluştur**'u seçin.

    ![Promptflow seçin.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.tr.png)

1. Navigasyon menüsünden **Sohbet akışı**'nı seçin.

    ![Sohbet akışını seçin.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.tr.png)

1. Kullanmak istediğiniz **Klasör adı**'nı girin.

    ![İsim girin.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.tr.png)

2. **Oluştur**'u seçin.

#### Prompt flow’u özel Phi-3 modelinizle sohbet edecek şekilde ayarlama

İnce ayarlı Phi-3 modelini Prompt flow’a entegre etmeniz gerekiyor. Ancak mevcut Prompt flow bu amaç için tasarlanmamış. Bu nedenle, özel modeli entegre etmek için Prompt flow’u yeniden tasarlamanız gerekmektedir.

1. Prompt flow’da mevcut akışı yeniden oluşturmak için şu işlemleri yapın:

    - **Ham dosya modu**'nu seçin.
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

    - **Kaydet**'i seçin.

    ![Ham dosya modunu seçin.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.tr.png)

1. Özel Phi-3 modelini Prompt flow’da kullanmak için *integrate_with_promptflow.py* dosyasına aşağıdaki kodu ekleyin.

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

    ![Prompt flow kodunu yapıştırın.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.tr.png)

> [!NOTE]
> Azure AI Foundry’de Prompt flow kullanımı hakkında daha ayrıntılı bilgi için [Azure AI Foundry'de Prompt flow](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) sayfasına bakabilirsiniz.

1. Modelinizle sohbeti etkinleştirmek için **Sohbet girişi**, **Sohbet çıkışı** seçeneklerini seçin.

    ![Giriş ve çıkışı seçin.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.tr.png)

1. Artık özel Phi-3 modelinizle sohbet etmeye hazırsınız. Bir sonraki alıştırmada Prompt flow’u nasıl başlatacağınızı ve ince ayarlı Phi-3 modelinizle sohbet etmek için nasıl kullanacağınızı öğreneceksiniz.

> [!NOTE]
>
> Yeniden oluşturulan akış aşağıdaki görünüme benzemelidir:
>
> ![Akış örneği.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.tr.png)
>

### Özel Phi-3 modelinizle sohbet edin

Artık özel Phi-3 modelinizi ince ayarladınız ve Prompt flow ile entegre ettiniz, modelle etkileşime geçmeye hazırsınız. Bu alıştırma, Prompt flow kullanarak modelinizle sohbet başlatma ve ayarlama sürecinde size rehberlik edecektir. Bu adımları takip ederek, ince ayarlı Phi-3 modelinizin çeşitli görevler ve sohbetler için tüm yeteneklerinden faydalanabileceksiniz.

- Prompt flow kullanarak özel Phi-3 modelinizle sohbet edin.

#### Prompt flow’u başlatma

1. Prompt flow’u başlatmak için **Hesaplama oturumlarını başlat**'ı seçin.

    ![Hesaplama oturumunu başlat.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.tr.png)

1. Parametreleri yenilemek için **Girişi doğrula ve çözümle**'yi seçin.

    ![Girişi doğrula.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.tr.png)

1. Oluşturduğunuz özel bağlantıya ait **connection** değerini seçin. Örneğin, *connection*.

    ![Bağlantı seçin.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.tr.png)

#### Özel modelinizle sohbet edin

1. **Sohbet**'i seçin.

    ![Sohbeti seçin.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.tr.png)

1. İşte sonuçlardan bir örnek: Artık özel Phi-3 modelinizle sohbet edebilirsiniz. İnce ayar için kullanılan verilere dayalı sorular sormanız önerilir.

    ![Prompt flow ile sohbet.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.tr.png)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.