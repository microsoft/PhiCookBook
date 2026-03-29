# Microsoft Foundry'de Prompt flow ile özel Phi-3 modellerini ince ayar yapma ve entegre etme

Bu uçtan uca (E2E) örnek, Microsoft Tech Community'deki "[Microsoft Foundry'de Prompt Flow ile Özel Phi-3 Modellerini İnce Ayar Yapma ve Entegre Etme](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" kılavuzuna dayanmaktadır. Bu örnek, Microsoft Foundry'de Prompt flow ile özel Phi-3 modellerinin ince ayar, dağıtım ve entegrasyon süreçlerini tanıtmaktadır. Kodun yerel olarak çalıştırıldığı "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" adlı E2E örneğin aksine, bu öğretici tamamen modelinizi Azure AI / ML Stüdyosu içinde ince ayar yapmak ve entegre etmek üzerine odaklanmaktadır.

## Genel Bakış

Bu E2E örnekte, Phi-3 modelini nasıl ince ayar yapacağınızı ve Microsoft Foundry'de Prompt flow ile nasıl entegre edeceğinizi öğreneceksiniz. Azure AI / ML Stüdyosu'ndan faydalanarak özel AI modellerinizi dağıtma ve kullanma için bir iş akışı oluşturacaksınız. Bu E2E örnek üç senaryoya bölünmüştür:

**Senaryo 1: Azure kaynaklarını kurma ve ince ayara hazırlık**

**Senaryo 2: Phi-3 modelini ince ayar yapma ve Azure Machine Learning Studio'da dağıtma**

**Senaryo 3: Prompt flow ile entegre etme ve Microsoft Foundry'de özel modelinizle sohbet etme**

İşte bu E2E örneğin genel görünümü.

![Phi-3-FineTuning_PromptFlow_Integration Genel Bakış.](../../../../../../translated_images/tr/00-01-architecture.198ba0f1ae6d841a.webp)

### İçindekiler

1. **[Senaryo 1: Azure kaynaklarını kurma ve ince ayara hazırlık](#senaryo-1-azure-kaynaklarını-kurma-ve-ince-ayara-hazırlık)**
    - [Bir Azure Machine Learning Workspace oluşturun](#bir-azure-machine-learning-workspace-oluşturun)
    - [Azure Abonesinde GPU kotası talep edin](#azure-abonesinde-gpu-kotası-talep-edin)
    - [Rol ataması ekleyin](#rol-ataması-ekleyin)
    - [Projeyi kurun](#projeyi-kurun)
    - [İnce ayar için veri kümesini hazırlayın](#i̇nce-ayar-için-veri-setini-hazırlayın)

1. **[Senaryo 2: Phi-3 modelini ince ayar yapma ve Azure Machine Learning Studio'da dağıtma](#senaryo-2-phi-3-modelini-ince-ayar-yapın-ve-azure-machine-learning-studioda-dağıtın)**
    - [Phi-3 modelini ince ayar yapın](#phi-3-modelini-ince-ayar-yapın)
    - [İnce ayar yapılmış Phi-3 modelini dağıtın](#i̇nce-ayar-yapılan-phi-3-modelini-dağıtın)

1. **[Senaryo 3: Prompt flow ile entegre etme ve Microsoft Foundry'de özel modelinizle sohbet etme](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Özel Phi-3 modelini Prompt flow ile entegre edin](#özel-phi-3-modelini-prompt-flow-ile-entegre-edin)
    - [Özel Phi-3 modelinizle sohbet edin](#özel-phi-3-modelinizle-sohbet-edin)

## Senaryo 1: Azure kaynaklarını kurma ve ince ayara hazırlık

### Bir Azure Machine Learning Workspace oluşturun

1. Portal sayfasının üstündeki **aramabarına** *azure machine learning* yazın ve çıkan seçeneklerden **Azure Machine Learning**'i seçin.

    ![azure machine learning yazın.](../../../../../../translated_images/tr/01-01-type-azml.acae6c5455e67b4b.webp)

2. Navigasyon menüsünden **+ Oluştur**'u seçin.

3. Navigasyon menüsünden **Yeni çalışma alanı** seçeneğini seçin.

    ![Yeni çalışma alanı seçin.](../../../../../../translated_images/tr/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Aşağıdaki işlemleri yapın:

    - Azure **Aboneliğinizi** seçin.
    - Kullanılacak **Kaynak grubunu** seçin (gerekirse yenisini oluşturun).
    - **Çalışma Alanı Adı** girin. Benzersiz bir değer olmalıdır.
    - Kullanmak istediğiniz **Bölgeyi** seçin.
    - Kullanılacak **Depolama hesabını** seçin (gerekirse yenisini oluşturun).
    - Kullanılacak **Anahtar kasasını** seçin (gerekirse yenisini oluşturun).
    - Kullanılacak **Uygulama içgörülerini** seçin (gerekirse yenisini oluşturun).
    - Kullanılacak **Konteyner kaydını** seçin (gerekirse yenisini oluşturun).

    ![Azure machine learning doldurun.](../../../../../../translated_images/tr/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. **Gözden geçir + oluştur**'u seçin.

6. **Oluştur**'u seçin.

### Azure Abonesinde GPU kotası talep edin

Bu öğreticide, GPU kullanarak Phi-3 modelini ince ayar yapmayı ve dağıtmayı öğreneceksiniz. İnce ayar için *Standard_NC24ads_A100_v4* GPU'sunu kullanacaksınız ve bu bir kota talebi gerektirir. Dağıtım için ise *Standard_NC6s_v3* GPU'sunu kullanacaksınız, bu da bir kota talebi gerektirir.

> [!NOTE]
>
> Sadece Pay-As-You-Go abonelikleri (standart abonelik türü) GPU tahsisi için uygundur; indirimli abonelikler şu anda desteklenmemektedir.
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) sitesini ziyaret edin.

1. *Standard NCADSA100v4 Family* kotası talep etmek için şu işlemleri yapın:

    - Sol sekmeden **Kota**'yı seçin.
    - Kullanacağınız **Sanal makine ailesini** seçin. Örneğin, *Standard_NC24ads_A100_v4* GPU'yu içeren **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**.
    - Navigasyon menüsünden **Kota talebi**'ni seçin.

        ![Kota talebi.](../../../../../../translated_images/tr/02-02-request-quota.c0428239a63ffdd5.webp)

    - Kota talebi sayfasında kullanmak istediğiniz **Yeni çekirdek limiti** değerini girin. Örneğin, 24.
    - Kota talebi sayfasında **Gönder**'i seçerek GPU kotasını talep edin.

1. *Standard NCSv3 Family* kotası talep etmek için şu işlemleri yapın:

    - Sol sekmeden **Kota**'yı seçin.
    - Kullanacağınız **Sanal makine ailesini** seçin. Örneğin, *Standard_NC6s_v3* GPU'yu içeren **Standard NCSv3 Family Cluster Dedicated vCPUs**.
    - Navigasyon menüsünden **Kota talebi**'ni seçin.
    - Kota talebi sayfasında kullanmak istediğiniz **Yeni çekirdek limiti** değerini girin. Örneğin, 24.
    - Kota talebi sayfasında **Gönder**'i seçerek GPU kotasını talep edin.

### Rol ataması ekleyin

Modellerinizi ince ayar yapmak ve dağıtmak için önce Kullanıcı Atanmış Yönetilen Kimlik (User Assigned Managed Identity - UAI) oluşturmalı ve ona uygun izinler vermelisiniz. Bu UAI, dağıtım sırasında kimlik doğrulama için kullanılacak.

#### Kullanıcı Atanmış Yönetilen Kimlik (UAI) oluşturun

1. Portal sayfasının üstündeki **aramabarına** *managed identities* yazın ve çıkan seçeneklerden **Managed Identities**'i seçin.

    ![managed identities yazın.](../../../../../../translated_images/tr/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. **+ Oluştur**'u seçin.

    ![Oluştur seçin.](../../../../../../translated_images/tr/03-02-select-create.92bf8989a5cd98f2.webp)

1. Aşağıdaki işlemleri yapın:

    - Azure **Aboneliğinizi** seçin.
    - Kullanılacak **Kaynak grubunu** seçin (gerekirse yenisini oluşturun).
    - Kullanmak istediğiniz **Bölgeyi** seçin.
    - Benzersiz bir **Ad** girin.

    ![Oluştur seçin.](../../../../../../translated_images/tr/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. **Gözden geçir + oluştur**'u seçin.

1. **+ Oluştur**'u seçin.

#### Yönetilen Kimliğe Katkıda Bulunan rol ataması ekleyin

1. Oluşturduğunuz Yönetilen Kimlik kaynağına gidin.

1. Sol sekmeden **Azure rol atamaları**'nı seçin.

1. Navigasyon menüsünden **+Rol ataması ekle**'yi seçin.

1. Rol ataması ekleme sayfasında şu işlemleri yapın:
    - **Kapsam** olarak **Kaynak grubu** seçin.
    - Azure **Aboneliğinizi** seçin.
    - Kullanılacak **Kaynak grubunu** seçin.
    - **Rol** olarak **Katkıda Bulunan (Contributor)** seçin.

    ![Katkıda Bulunan rolü seçin.](../../../../../../translated_images/tr/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. **Kaydet**'i seçin.

#### Yönetilen Kimliğe Storage Blob Data Reader rol ataması ekleyin

1. Portal sayfasının üstündeki **aramabarına** *storage accounts* yazın ve çıkan seçeneklerden **Storage accounts**'u seçin.

    ![storage accounts yazın.](../../../../../../translated_images/tr/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Oluşturduğunuz Azure Machine Learning çalışma alanına bağlı depolama hesabını seçin. Örneğin, *finetunephistorage*.

1. Rol ataması ekleme sayfasına gitmek için şu işlemleri yapın:

    - Oluşturduğunuz Azure Depolama hesabına gidin.
    - Sol sekmeden **Erişim Denetimi (IAM)**'yı seçin.
    - Navigasyon menüsünden **+ Ekle**'yi seçin.
    - Navigasyon menüsünden **Rol ataması ekle**'yi seçin.

    ![Rol ekle.](../../../../../../translated_images/tr/03-06-add-role.353ccbfdcf0789c2.webp)

1. Rol ataması ekleme sayfasında şu işlemleri yapın:

    - Rol sayfasında **Arama kutusuna** *Storage Blob Data Reader* yazın ve çıkanlardan **Storage Blob Data Reader**'ı seçin.
    - Rol sayfasında **İleri**'yi seçin.
    - Üyeler sayfasında **Erişimi ata** olarak **Yönetilen kimlik**'i seçin.
    - Üyeler sayfasında **+ Üye seç**'yi seçin.
    - Yönetilen kimlik seçme sayfasında Azure **Aboneliğinizi** seçin.
    - Yönetilen kimlik seçme sayfasında **Yönetilen kimlik** olarak **Manage Identity** seçin.
    - Oluşturduğunuz Manage Identity'yi seçin. Örneğin, *finetunephi-managedidentity*.
    - **Seç**'i seçin.

    ![Yönetilen kimliği seçin.](../../../../../../translated_images/tr/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. **Gözden geçir + ata**'yı seçin.

#### Yönetilen Kimliğe AcrPull rol ataması ekleyin

1. Portal sayfasının üstündeki **aramabarına** *container registries* yazın ve çıkan seçeneklerden **Container registries**'i seçin.

    ![container registries yazın.](../../../../../../translated_images/tr/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Azure Machine Learning çalışma alanına bağlı konteyner kaydını seçin. Örneğin, *finetunephicontainerregistry*

1. Rol ataması ekleme sayfasına gitmek için şu işlemleri yapın:

    - Sol sekmeden **Erişim Denetimi (IAM)**'yı seçin.
    - Navigasyon menüsünden **+ Ekle**'yi seçin.
    - Navigasyon menüsünden **Rol ataması ekle**'yi seçin.

1. Rol ataması ekleme sayfasında şu işlemleri yapın:

    - Rol sayfasında **Arama kutusuna** *AcrPull* yazın ve çıkanlardan **AcrPull**'u seçin.
    - Rol sayfasında **İleri**'yi seçin.
    - Üyeler sayfasında **Erişimi ata** olarak **Yönetilen kimlik**'i seçin.
    - Üyeler sayfasında **+ Üye seç**'yi seçin.
    - Yönetilen kimlik seçme sayfasında Azure **Aboneliğinizi** seçin.
    - Yönetilen kimlik seçme sayfasında **Yönetilen kimlik** olarak **Manage Identity** seçin.
    - Oluşturduğunuz Manage Identity'yi seçin. Örneğin, *finetunephi-managedidentity*.
    - **Seç**'i seçin.
    - **Gözden geçir + ata**'yı seçin.

### Projeyi kurun

İnce ayar için gereken veri kümelerini indirmek üzere yerel bir ortam kuracaksınız.

Bu egzersizde şunları yapacaksınız:

- İçinde çalışmak için bir klasör oluşturacaksınız.
- Sanal bir ortam oluşturacaksınız.
- Gerekli paketleri kuracaksınız.
- Veri kümesini indirmek için *download_dataset.py* dosyası oluşturacaksınız.

#### İçinde çalışmak üzere bir klasör oluşturun

1. Bir terminal penceresi açın ve varsayılan yolda *finetune-phi* adlı bir klasör oluşturmak için aşağıdaki komutu yazın.

    ```console
    mkdir finetune-phi
    ```

2. Terminalde *finetune-phi* klasörüne gitmek için aşağıdaki komutu yazın.

    ```console
    cd finetune-phi
    ```

#### Sanal ortam oluşturun

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

#### Gerekli paketleri yükleyin

1. Gerekli paketleri yüklemek için terminalinize aşağıdaki komutları yazın.

    ```console
    pip install datasets==2.19.1
    ```

#### `donload_dataset.py` dosyasını oluşturun

> [!NOTE]
> Tam klasör yapısı:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code**'u açın.

1. Menü çubuğundan **File**'ı seçin.

1. **Open Folder**'ı seçin.

1. Oluşturduğunuz *finetune-phi* klasörünü seçin, bu klasör *C:\Users\yourUserName\finetune-phi* konumunda bulunur.

    ![Oluşturduğunuz klasörü seçin.](../../../../../../translated_images/tr/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. Visual Studio Code'un sol panelinde, sağ tıklayın ve *download_dataset.py* adlı yeni bir dosya oluşturmak için **New File**'ı seçin.

    ![Yeni bir dosya oluşturun.](../../../../../../translated_images/tr/04-02-create-new-file.cf9a330a3a9cff92.webp)

### İnce ayar için veri setini hazırlayın

Bu alıştırmada, *download_dataset.py* dosyasını çalıştırarak *ultrachat_200k* veri setlerini yerel ortamınıza indireceksiniz. Ardından bu veri setlerini Azure Machine Learning’de Phi-3 modelini ince ayar yapmak için kullanacaksınız.

Bu alıştırmada şunları yapacaksınız:

- Veri setlerini indirmek için *download_dataset.py* dosyasına kod ekleyin.
- Veri setlerini yerel ortamınıza indirmek için *download_dataset.py* dosyasını çalıştırın.

#### *download_dataset.py* kullanarak veri setinizi indirin

1. Visual Studio Code’da *download_dataset.py* dosyasını açın.

1. Aşağıdaki kodu *download_dataset.py* dosyasına ekleyin.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Belirtilen isim, yapılandırma ve bölme oranı ile veri setini yükle
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Veri setini eğitim ve test olarak ayır (yüzde 80 eğitim, yüzde 20 test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Dizin yoksa oluştur
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Dosyayı yazma modunda aç
        with open(filepath, 'w', encoding='utf-8') as f:
            # Veri setindeki her kayıt üzerinde yineleme yap
            for record in dataset:
                # Kaydı JSON nesnesi olarak dök ve dosyaya yaz
                json.dump(record, f)
                # Kayıtları ayırmak için yeni satır karakteri yaz
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # ULTRACHAT_200k veri setini belirli bir yapılandırma ve bölme oranı ile yükle ve ayır
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Bölmeden eğitim ve test veri setlerini çıkar
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Eğitim veri setini JSONL dosyasına kaydet
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Test veri setini ayrı bir JSONL dosyasına kaydet
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
> #### Veri seti boyutu ve ince ayar süresi üzerine not
>
> Bu öğreticide, veri setinin sadece %1'ini kullanıyorsunuz (`split='train[:1%]'`). Bu, veri miktarını önemli ölçüde azaltarak yükleme ve ince ayar işlemlerini hızlandırır. Eğitim süresi ile model performansı arasındaki doğru dengeyi bulmak için bu yüzdeyi ayarlayabilirsiniz. Veri setinin daha küçük bir alt kümesini kullanmak, ince ayar için gereken süreyi azaltır ve süreci bir öğretici için daha yönetilebilir hale getirir.

## Senaryo 2: Phi-3 modelini ince ayar yapın ve Azure Machine Learning Studio'da dağıtın

### Phi-3 modelini ince ayar yapın

Bu alıştırmada, Phi-3 modelini Azure Machine Learning Studio’da ince ayar yapacaksınız.

Bu alıştırmada şunları yapacaksınız:

- İnce ayar için bilgisayar kümesi oluşturun.
- Azure Machine Learning Studio’da Phi-3 modelini ince ayar yapın.

#### İnce ayar için bilgisayar kümesi oluşturun

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) sitesini ziyaret edin.

1. Sol taraftaki sekmeden **Compute**'u seçin.

1. Navigasyon menüsünden **Compute clusters**'ı seçin.

1. **+ New**'i seçin.

    ![Compute'u seçin.](../../../../../../translated_images/tr/06-01-select-compute.a29cff290b480252.webp)

1. Aşağıdaki işlemleri yapın:

    - Kullanmak istediğiniz **Region**'u seçin.
    - **Virtual machine tier**'ı **Dedicated** olarak seçin.
    - **Virtual machine type**'ı **GPU** olarak seçin.
    - **Virtual machine size** filtresini **Select from all options** olarak seçin.
    - **Virtual machine size**'ı **Standard_NC24ads_A100_v4** olarak seçin.

    ![Küme oluşturun.](../../../../../../translated_images/tr/06-02-create-cluster.f221b65ae1221d4e.webp)

1. **Next**'i seçin.

1. Aşağıdaki işlemleri yapın:

    - **Compute name** girin. Bu benzersiz bir değer olmalıdır.
    - **Minimum number of nodes** değerini **0** olarak seçin.
    - **Maximum number of nodes** değerini **1** olarak seçin.
    - **Idle seconds before scale down** değerini **120** olarak seçin.

    ![Küme oluşturun.](../../../../../../translated_images/tr/06-03-create-cluster.4a54ba20914f3662.webp)

1. **Create**'yi seçin.

#### Phi-3 modelini ince ayar yapın

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) sitesini ziyaret edin.

1. Oluşturduğunuz Azure Machine Learning çalışma alanını seçin.

    ![Oluşturduğunuz çalışma alanını seçin.](../../../../../../translated_images/tr/06-04-select-workspace.a92934ac04f4f181.webp)

1. Aşağıdaki işlemleri yapın:

    - Sol taraftaki sekmeden **Model catalog**'u seçin.
    - **Arama barına** *phi-3-mini-4k* yazın ve beliren seçeneklerden **Phi-3-mini-4k-instruct**'u seçin.

    ![phi-3-mini-4k yazın.](../../../../../../translated_images/tr/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Navigasyon menüsünden **Fine-tune**'u seçin.

    ![İnce ayar yapmayı seçin.](../../../../../../translated_images/tr/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Aşağıdaki işlemleri yapın:

    - **Select task type**'ı **Chat completion** olarak seçin.
    - **+ Select data**'yı seçerek **Training data** yükleyin.
    - Validasyon veri yükleme türünü **Provide different validation data** olarak seçin.
    - **+ Select data**'yı seçerek **Validation data** yükleyin.

    ![İnce ayar sayfasını doldurun.](../../../../../../translated_images/tr/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> İnce ayar sürecini optimize etmek için **learning_rate** ve **lr_scheduler_type** gibi ayarları özelleştirmek için **Advanced settings**'i seçebilirsiniz.

1. **Finish**'i seçin.

1. Bu alıştırmada, Phi-3 modelini Azure Machine Learning kullanarak başarıyla ince ayar yaptınız. İnce ayar sürecinin önemli bir zaman alabileceğini unutmayın. İnce ayar işini çalıştırdıktan sonra tamamlanmasını beklemeniz gerekir. İnce ayar işinin durumunu Azure Machine Learning Çalışma Alanınızın sol tarafındaki Jobs sekmesinden izleyebilirsiniz. Sonraki seride, ince ayar yapılan modeli dağıtacak ve Prompt flow ile entegre edeceksiniz.

    ![İnce ayar işini görün.](../../../../../../translated_images/tr/06-08-output.2bd32e59930672b1.webp)

### İnce ayar yapılan Phi-3 modelini dağıtın

İnce ayar yapılan Phi-3 modelini Prompt flow ile entegre etmek için, modeli gerçek zamanlı çıkarım için erişilebilir hale getirmek üzere dağıtmanız gerekir. Bu işlem modeli kaydetmeyi, çevrimiçi uç nokta oluşturmayı ve modeli dağıtmayı içerir.

Bu alıştırmada şunları yapacaksınız:

- İnce ayar yapılan modeli Azure Machine Learning çalışma alanına kaydedin.
- Bir çevrimiçi uç nokta oluşturun.
- Kayıtlı ince ayar yapılmış Phi-3 modelini dağıtın.

#### İnce ayar yapılmış modeli kaydedin

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) sitesini ziyaret edin.

1. Oluşturduğunuz Azure Machine Learning çalışma alanını seçin.

    ![Oluşturduğunuz çalışma alanını seçin.](../../../../../../translated_images/tr/06-04-select-workspace.a92934ac04f4f181.webp)

1. Sol taraftaki sekmeden **Models**'i seçin.
1. **+ Register**'ı seçin.
1. **From a job output**'u seçin.

    ![Modeli kaydedin.](../../../../../../translated_images/tr/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Oluşturduğunuz işi seçin.

    ![İşi seçin.](../../../../../../translated_images/tr/07-02-select-job.3e2e1144cd6cd093.webp)

1. **Next**'i seçin.

1. **Model type**'ı **MLflow** olarak seçin.

1. **Job output**'un seçili olduğundan emin olun; otomatik olarak seçilmiş olmalıdır.

    ![Çıktıyı seçin.](../../../../../../translated_images/tr/07-03-select-output.4cf1a0e645baea1f.webp)

2. **Next**'i seçin.

3. **Register**'ı seçin.

    ![Kaydı seçin.](../../../../../../translated_images/tr/07-04-register.fd82a3b293060bc7.webp)

4. Kayıtlı modelinizi, sol taraftaki sekmeden **Models** menüsüne giderek görüntüleyebilirsiniz.

    ![Kayıtlı model.](../../../../../../translated_images/tr/07-05-registered-model.7db9775f58dfd591.webp)

#### İnce ayar yapılan modeli dağıtın

1. Oluşturduğunuz Azure Machine Learning çalışma alanına gidin.

1. Sol taraftaki sekmeden **Endpoints**'i seçin.

1. Navigasyon menüsünden **Real-time endpoints**'i seçin.

    ![Uç nokta oluşturun.](../../../../../../translated_images/tr/07-06-create-endpoint.1ba865c606551f09.webp)

1. **Create**'yi seçin.

1. Oluşturduğunuz kayıtlı modeli seçin.

    ![Kayıtlı modeli seçin.](../../../../../../translated_images/tr/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. **Select**'i seçin.

1. Aşağıdaki işlemleri yapın:

    - **Virtual machine** olarak *Standard_NC6s_v3*'ü seçin.
    - Kullanmak istediğiniz **Instance count**'ı seçin. Örneğin, *1*.
    - **Endpoint**'i **New** olarak seçin ve yeni bir uç nokta oluşturun.
    - **Endpoint name** girin. Bu benzersiz bir değer olmalıdır.
    - **Deployment name** girin. Bu benzersiz bir değer olmalıdır.

    ![Dağıtım ayarlarını doldurun.](../../../../../../translated_images/tr/07-08-deployment-setting.43ddc4209e673784.webp)

1. **Deploy**'ı seçin.

> [!WARNING]
> Hesabınıza ekstra ücret yansımaması için Azure Machine Learning çalışma alanındaki oluşturduğunuz uç noktayı silmeyi unutmayın.
>

#### Azure Machine Learning Çalışma Alanında dağıtım durumunu kontrol edin

1. Oluşturduğunuz Azure Machine Learning çalışma alanına gidin.

1. Sol taraftaki sekmeden **Endpoints**'i seçin.

1. Oluşturduğunuz uç noktayı seçin.

    ![Uç noktaları seçin](../../../../../../translated_images/tr/07-09-check-deployment.325d18cae8475ef4.webp)

1. Bu sayfada, dağıtım sürecinde uç noktaları yönetebilirsiniz.

> [!NOTE]
> Dağıtım tamamlandıktan sonra, **Live traffic**'in **%100** olarak ayarlandığından emin olun. Eğer değilse, trafik ayarlarını düzenlemek için **Update traffic**'i seçin. Trafik %0 olarak ayarlanmış ise modeli test edemezsiniz.
>
> ![Trafiği ayarlayın.](../../../../../../translated_images/tr/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Senaryo 3: Prompt flow ile entegrasyon ve Microsoft Foundry'de özel modelinizle sohbet

### Özel Phi-3 modelini Prompt flow ile entegre edin

İnce ayar yapılan modelinizi başarıyla dağıttıktan sonra, Prompt Flow ile entegre ederek modelinizi gerçek zamanlı uygulamalarda kullanabilir, özel Phi-3 modelinizle çeşitli etkileşimli görevleri gerçekleştirebilirsiniz.

Bu alıştırmada şunları yapacaksınız:

- Microsoft Foundry Hub oluşturun.
- Microsoft Foundry Proje oluşturun.
- Prompt flow oluşturun.
- İnce ayar yapılan Phi-3 modeli için özel bağlantı ekleyin.
- Özel Phi-3 modelinizle sohbet etmek için Prompt flow’u kurun.

> [!NOTE]
> Promptflow ile entegrasyonu Azure ML Studio kullanarak da yapabilirsiniz. Aynı entegrasyon süreci Azure ML Studio için de geçerlidir.

#### Microsoft Foundry Hub oluşturun

Proje oluşturmadan önce bir Hub oluşturmanız gerekir. Hub, Microsoft Foundry içinde birden fazla projeyi organize edip yönetmenizi sağlayan bir Kaynak Grubu gibi çalışır.
1. [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) sitesini ziyaret edin.

1. Sol taraftaki sekmeden **Tüm hub'lar** seçeneğini seçin.

1. Navigasyon menüsünden **+ Yeni hub** seçeneğini seçin.

    ![Hub oluşturun.](../../../../../../translated_images/tr/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Aşağıdaki görevleri gerçekleştirin:

    - **Hub adı** girin. Bu benzersiz bir değer olmalıdır.
    - Azure **Aboneliğinizi** seçin.
    - Kullanmak istediğiniz **Kaynak grubunu** seçin (gerekirse yeni bir tane oluşturun).
    - Kullanmak istediğiniz **Konumu** seçin.
    - Kullanmak istediğiniz **Azure AI Hizmetlerini Bağla** seçeneğini seçin (gerekirse yeni bir tane oluşturun).
    - **Azure AI Arama Bağla** seçeneğini **Bağlantıyı atla** olarak seçin.

    ![Hub doldurun.](../../../../../../translated_images/tr/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. **İleri** seçeneğini seçin.

#### Microsoft Foundry Projesi Oluşturma

1. Oluşturduğunuz Hub’da sol taraftaki sekmeden **Tüm projeler** seçeneğini seçin.

1. Navigasyon menüsünden **+ Yeni proje** seçeneğini seçin.

    ![Yeni proje seçin.](../../../../../../translated_images/tr/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. **Proje adı** girin. Bu benzersiz bir değer olmalıdır.

    ![Proje oluşturun.](../../../../../../translated_images/tr/08-05-create-project.4d97f0372f03375a.webp)

1. **Bir proje oluştur** seçeneğini seçin.

#### Fine-tuned Phi-3 modeli için özel bağlantı ekleme

Özel Phi-3 modelinizi Prompt flow ile entegre etmek için modelin uç noktasını ve anahtarını özel bağlantıya kaydetmeniz gerekir. Bu ayar, Prompt flow içinde özel Phi-3 modelinize erişimi sağlar.

#### Fine-tuned Phi-3 modelinin api anahtarı ve uç nokta URI'sını ayarlama

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) sitesini ziyaret edin.

1. Oluşturduğunuz Azure Makine öğrenimi çalışma alanına gidin.

1. Sol taraftaki sekmeden **Uç noktalar** seçeneğini seçin.

    ![Uç noktaları seçin.](../../../../../../translated_images/tr/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Oluşturduğunuz uç noktayı seçin.

    ![Uç noktayı seçin.](../../../../../../translated_images/tr/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Navigasyon menüsünden **Tüket** seçeneğini seçin.

1. **REST uç noktası** ve **Birincil anahtar** kopyalayın.

    ![Api anahtarı ve uç nokta URI'sını kopyalayın.](../../../../../../translated_images/tr/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Özel Bağlantı Ekleme

1. [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) sitesini ziyaret edin.

1. Oluşturduğunuz Microsoft Foundry projesine gidin.

1. Oluşturduğunuz Projede sol taraftan **Ayarlar** seçeneğini seçin.

1. **+ Yeni bağlantı** seçeneğini seçin.

    ![Yeni bağlantı seçin.](../../../../../../translated_images/tr/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Navigasyon menüsünden **Özel anahtarlar** seçeneğini seçin.

    ![Özel anahtarları seçin.](../../../../../../translated_images/tr/08-10-select-custom-keys.856f6b2966460551.webp)

1. Aşağıdaki görevleri gerçekleştirin:

    - **+ Anahtar-değer çiftleri ekle** seçeneğini seçin.
    - Anahtar adı için **endpoint** girin ve Azure ML Studio’dan kopyaladığınız uç nokta değerini değer alanına yapıştırın.
    - Tekrar **+ Anahtar-değer çiftleri ekle** seçeneğini seçin.
    - Anahtar adı için **key** girin ve Azure ML Studio’dan kopyaladığınız anahtarı değer alanına yapıştırın.
    - Anahtarları ekledikten sonra, anahtarın görünmemesi için **gizli olarak işaretle** seçeneğini etkinleştirin.

    ![Bağlantı ekleyin.](../../../../../../translated_images/tr/08-11-add-connection.785486badb4d2d26.webp)

1. **Bağlantıyı ekle** seçeneğini seçin.

#### Prompt flow oluşturma

Microsoft Foundry’de özel bağlantı eklediniz. Şimdi aşağıdaki adımları kullanarak Prompt flow oluşturacağız. Ardından bu Prompt flow’u özel bağlantıya bağlayarak fine-tuned modeli Prompt flow içinde kullanabilirsiniz.

1. Oluşturduğunuz Microsoft Foundry projesine gidin.

1. Sol taraftan **Prompt flow** seçeneğini seçin.

1. Navigasyon menüsünden **+ Oluştur** seçeneğini seçin.

    ![Promptflow seçin.](../../../../../../translated_images/tr/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Navigasyon menüsünden **Sohbet akışı** seçeneğini seçin.

    ![Sohbet akışını seçin.](../../../../../../translated_images/tr/08-13-select-flow-type.2ec689b22da32591.webp)

1. Kullanmak istediğiniz **Klasör adı** girin.

    ![Adı girin.](../../../../../../translated_images/tr/08-14-enter-name.ff9520fefd89f40d.webp)

2. **Oluştur** seçeneğini seçin.

#### Fine-tuned Phi-3 modeli ile sohbet için Prompt flow’u ayarlama

Fine-tuned Phi-3 modelini Prompt flow’a entegre etmeniz gerekiyor. Ancak mevcut Prompt flow bu amaç için tasarlanmamıştır. Bu nedenle özel modeli entegre etmek için Prompt flow’u yeniden tasarlamanız gerekir.

1. Prompt flow’da mevcut akışı yeniden oluşturmak için aşağıdaki görevleri gerçekleştirin:

    - **Ham dosya modu** seçeneğini seçin.
    - *flow.dag.yml* dosyasındaki mevcut tüm kodu silin.
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

    - **Kaydet** seçeneğini seçin.

    ![Ham dosya modunu seçin.](../../../../../../translated_images/tr/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Özel Phi-3 modelini Prompt flow’da kullanmak için *integrate_with_promptflow.py* dosyasına aşağıdaki kodu ekleyin.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Günlük kaydı kurulumu
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

        # "connection", Özel Bağlantının adıdır, "endpoint", "key" Özel Bağlantıdaki anahtarlardır
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
            
            # Tam JSON yanıtını kaydedin
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

    ![Prompt flow kodunu yapıştırın.](../../../../../../translated_images/tr/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Microsoft Foundry’de Prompt flow kullanımı hakkında daha ayrıntılı bilgi için [Microsoft Foundry’de Prompt flow](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) sayfasına bakabilirsiniz.

1. Modelinizle sohbet etmek için **Sohbet girişi**, **Sohbet çıkışı** seçeneklerini etkinleştirin.

    ![Girdi Çıktı seçin.](../../../../../../translated_images/tr/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Artık özel Phi-3 modelinizle sohbet etmeye hazırsınız. Bir sonraki alıştırmada, Prompt flow’u başlatmayı ve fine-tuned Phi-3 modelinizle sohbet etmek için nasıl kullanılacağını öğreneceksiniz.

> [!NOTE]
>
> Yeniden oluşturulmuş akış aşağıdaki görüntü gibi görünmelidir:
>
> ![Akış örneği.](../../../../../../translated_images/tr/08-18-graph-example.d6457533952e690c.webp)
>

### Özel Phi-3 modelinizle sohbet edin

Fine-tuned özel Phi-3 modelinizi Prompt flow ile entegre ettiniz, şimdi onunla etkileşime başlamaya hazırsınız. Bu alıştırma, Prompt flow kullanarak modelinizle sohbet etmeyi ayarlama ve başlatma sürecinde size rehberlik edecektir. Bu adımları takip ederek fine-tuned Phi-3 modelinizin yeteneklerini çeşitli görevler ve sohbetler için tam anlamıyla kullanabileceksiniz.

- Özel Phi-3 modelinizle Prompt flow kullanarak sohbet edin.

#### Prompt flow’u başlatma

1. Prompt flow’u başlatmak için **Hesaplama oturumlarını başlat** seçeneğini seçin.

    ![Hesaplama oturumunu başlatın.](../../../../../../translated_images/tr/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Parametreleri yenilemek için **Girdi doğrula ve çözümle** seçeneğini seçin.

    ![Girdiyi doğrula.](../../../../../../translated_images/tr/09-02-validate-input.317c76ef766361e9.webp)

1. Oluşturduğunuz özel bağlantının **connection** değerini seçin. Örneğin, *connection*.

    ![Bağlantı seçin.](../../../../../../translated_images/tr/09-03-select-connection.99bdddb4b1844023.webp)

#### Özel modelinizle sohbet edin

1. **Sohbet** seçeneğini seçin.

    ![Sohbeti seçin.](../../../../../../translated_images/tr/09-04-select-chat.61936dce6612a1e6.webp)

1. İşte sonuçların bir örneği: Artık özel Phi-3 modelinizle sohbet edebilirsiniz. Fine-tuning için kullanılan veriler baz alınarak sorular sormanız önerilir.

    ![Prompt flow ile sohbet edin.](../../../../../../translated_images/tr/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi yerel dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek herhangi bir yanlış anlama veya yanlış yorumdan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->