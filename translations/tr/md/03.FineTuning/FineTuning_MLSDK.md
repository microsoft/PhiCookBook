## Azure ML sistem kayıt defterinden sohbet tamamlama bileşenlerini kullanarak bir modeli ince ayar yapma

Bu örnekte, ultrachat_200k veri kümesini kullanarak 2 kişi arasındaki bir konuşmayı tamamlamak için Phi-3-mini-4k-instruct modelinin ince ayarını yapacağız.

![MLFineTune](../../../../translated_images/tr/MLFineTune.928d4c6b3767dd35.webp)

Örnek, Azure ML SDK ve Python kullanarak ince ayar yapmayı ve ardından ince ayarlı modeli gerçek zamanlı çıkarım için çevrimiçi bir uç noktaya dağıtmayı gösterecek.

### Eğitim verisi

ultrachat_200k veri kümesini kullanacağız. Bu, UltraChat veri kümesinin yoğun filtrelenmiş bir versiyonudur ve çağın en iyisi 7b sohbet modeli Zephyr-7B-β'yi eğitmek için kullanılmıştır.

### Model

Kullanıcının sohbet tamamlama görevi için nasıl bir modeli ince ayar yapabileceğini göstermek üzere Phi-3-mini-4k-instruct modelini kullanacağız. Bu not defterini belirli bir model kartından açtıysanız, lütfen o özel model adını değiştirin.

### Görevler

- İnce ayar yapmak için bir model seçin.
- Eğitim verisini seçip keşfedin.
- İnce ayar işini yapılandırın.
- İnce ayar işini çalıştırın.
- Eğitim ve değerlendirme ölçümleri gözden geçirin.
- İnce ayarlı modeli kaydedin.
- İnce ayarlı modeli gerçek zamanlı çıkarım için dağıtın.
- Kaynakları temizleyin.

## 1. Ön gereksinimleri ayarlama

- Bağımlılıkları yükleyin
- AzureML Çalışma Alanına bağlanın. SDK kimlik doğrulaması ayarlama hakkında daha fazla bilgi edinin. Aşağıdaki <WORKSPACE_NAME>, <RESOURCE_GROUP> ve <SUBSCRIPTION_ID> yerlerini değiştirin.
- azureml sistem kayıt defterine bağlanın
- İsteğe bağlı bir deney adı belirleyin
- Hesaplama kaynaklarını kontrol edin veya oluşturun.

> [!NOTE]
> Gereksinimler tek bir GPU düğümü, birden fazla GPU kartı içerebilir. Örneğin, Standard_NC24rs_v3 bir düğümünde 4 NVIDIA V100 GPU bulunurken Standard_NC12s_v3'de 2 NVIDIA V100 GPU vardır. Bu bilgi için dokümanlara bakınız. Düğüm başına GPU kart sayısı aşağıdaki gpus_per_node parametresinde ayarlanır. Bu değerin doğru ayarlanması düğümdeki tüm GPU'ların kullanımını garanti eder. Önerilen GPU hesaplama SKU'ları şurada ve şurada bulunabilir.

### Python Kütüphaneleri

Aşağıdaki hücreyi çalıştırarak bağımlılıkları yükleyin. Bu, yeni bir ortamda çalıştırılıyorsa isteğe bağlı olmayan bir adımdır.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Azure ML ile Etkileşim

1. Bu Python betiği Azure Machine Learning (Azure ML) servisi ile etkileşimde bulunmak için kullanılır. İşte yaptığı şeylerin dökümü:

    - azure.ai.ml, azure.identity ve azure.ai.ml.entities paketlerinden gerekli modülleri içe aktarır. Ayrıca time modülünü getirir.

    - DefaultAzureCredential() kullanarak kimlik doğrulama yapmaya çalışır; bu, Azure bulutunda çalışan uygulamaları hızlıca geliştirmek için basitleştirilmiş bir kimlik doğrulama deneyimi sağlar. Eğer başarısız olursa InteractiveBrowserCredential() kullanarak interaktif bir giriş istemi sağlar.

    - Ardından from_config yöntemiyle MLClient örneği oluşturmaya çalışır; bu yöntem varsayılan yapılandırma dosyasını (config.json) okur. Başarısız olursa, subscription_id, resource_group_name ve workspace_name bilgilerini manuel vererek MLClient örneği yaratır.

    - "azureml" adlı Azure ML kayıt defteri için başka bir MLClient örneği oluşturur. Bu kayıt defteri modellerin, ince ayar iş akışlarının ve ortamların saklandığı yerdir.

    - experiment_name değişkenini "chat_completion_Phi-3-mini-4k-instruct" olarak ayarlar.

    - Şu anki zaman damgasını tam sayı olarak dönüştürür ve string yapar. Bu zaman damgası, benzersiz isimler ve versiyonlar oluşturmak için kullanılabilir.

    ```python
    # Azure ML ve Azure Identity'den gerekli modülleri içe aktar
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # time modülünü içe aktar
    
    # DefaultAzureCredential kullanarak kimlik doğrulamaya çalış
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # DefaultAzureCredential başarısız olursa, InteractiveBrowserCredential kullan
        credential = InteractiveBrowserCredential()
    
    # Varsayılan yapılandırma dosyasını kullanarak bir MLClient örneği oluşturmaya çalış
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # Bu başarısız olursa, ayrıntıları manuel olarak sağlayarak bir MLClient örneği oluştur
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # "azureml" adlı Azure ML kayıt defteri için başka bir MLClient örneği oluştur
    # Bu kayıt defteri, modellerin, ince ayar pipeline'larının ve ortamların saklandığı yerdir
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Deney adını ayarla
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Benzersiz olması gereken isimler ve sürümler için kullanılabilecek benzersiz bir zaman damgası oluştur
    timestamp = str(int(time.time()))
    ```

## 2. İnce ayar yapmak için temel model seçimi

1. Phi-3-mini-4k-instruct, Phi-2 için kullanılan veri kümeleri üzerine kurulmuş 3.8 milyar parametreli, hafif ve çağın en iyisi açık modeldir. Model Phi-3 model ailesine aittir ve Mini versiyonu, destekleyebileceği bağlam uzunluğu (token cinsinden) olan 4K ve 128K olmak üzere iki varyanta sahiptir. Bu modeli kullanmak için amacımıza göre ince ayar yapmamız gerekir. Bu modelleri AzureML Studio Model Kataloğunda sohbet tamamlama görevi filtresiyle keşfedebilirsiniz. Bu örnekte Phi-3-mini-4k-instruct modelini kullanıyoruz. Eğer farklı bir model için bu not defterini açtıysanız, model adı ve versiyonunu buna göre değiştirin.

> [!NOTE]
> model id özelliği, ince ayar işine girdi olarak verilecektir. Bu aynı zamanda AzureML Studio Model Kataloğunda model detayları sayfasında Varlık ID alanında da bulunabilir.

2. Bu Python betiği Azure Machine Learning (Azure ML) servisi ile etkileşimde bulunur. İşte yaptığı işlerin dökümü:

    - model_name değişkenini "Phi-3-mini-4k-instruct" olarak ayarlar.

    - registry_ml_client nesnesinin models özelliğinin get yöntemini kullanarak Azure ML kayıt defterinden belirtilen isimdeki modelin en son versiyonunu alır. get yöntemi iki argümanla çağrılır: model adı ve modelin en son versiyonunun alınacağını belirten etiket.

    - İnce ayar için kullanılacak modelin adı, versiyonu ve id'sini konsola yazdırır. String'in format yöntemi kullanılarak bu değerler mesaj içine yerleştirilir. foundation_model nesnesinin özellikleri olarak model adı, versiyon ve id alınır.

    ```python
    # Model adını ayarla
    model_name = "Phi-3-mini-4k-instruct"
    
    # Azure ML kaydından modelin en son sürümünü al
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Model adı, sürümü ve kimliğini yazdır
    # Bu bilgiler takip ve hata ayıklama için faydalıdır
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. İş için kullanılacak hesaplamayı oluşturma

İnce ayar işi SADECE GPU hesaplama ile çalışır. Hesaplamanın büyüklüğü modelin büyüklüğüne bağlıdır ve çoğu durumda doğru hesabı belirlemek zordur. Bu hücrede kullanıcıya işi için doğru hesaplamayı seçmesi için rehberlik edilir.

> [!NOTE]
> Aşağıda listelenen hesaplamalar en optimize yapılandırma ile çalışır. Yapılandırmadaki herhangi bir değişiklik Cuda Bellek Yetersizliği hatasına yol açabilir. Bu tür durumlarda, hesabı daha büyük bir hesaplama boyutuna yükseltmeyi deneyin.

> [!NOTE]
> Aşağıdaki compute_cluster_size seçiminde, hesabın kaynak grubunuzda kullanılabilir olduğundan emin olun. Belli bir hesaplama mevcut değilse, hesaplama kaynaklarına erişim talebinde bulunabilirsiniz.

### İnce Ayar Desteği için Model Kontrolü

1. Bu Python betiği Azure Machine Learning (Azure ML) modeline etkileşimde bulunur. İşte yaptığı işlerin dökümü:

    - Python soyut sözdizimi ağacını işleyen fonksiyonlar sunan ast modülünü içe aktarır.

    - foundation_model nesnesinin (Azure ML'deki bir modeli temsil eder) içinde finetune_compute_allow_list adlı bir etiket olup olmadığını kontrol eder. Azure ML'de etiketler, modelleri filtrelemek ve sıralamak için kullanılan anahtar-değer çiftleridir.

    - finetune_compute_allow_list etiketi mevcutsa, etiketteki değeri (string) güvenli şekilde Python listesine dönüştürmek için ast.literal_eval fonksiyonunu kullanır. Bu liste computes_allow_list değişkenine atanır. Ardından kullanıcıya listenin kullanılarak hesaplama oluşturulması gerektiğini bildiren mesaj yazdırır.

    - finetune_compute_allow_list etiketi yoksa, computes_allow_list'i None olarak ayarlar ve model etiketlerinin bir parçası olmadığını belirten mesaj yazdırır.

    - Özetle, bu betik modelin meta verilerinde belirli bir etiketi arar, var ise değerini listeye çevirir ve kullanıcıyı bilgilendirir.

    ```python
    # Python soyut sözdizimi ağacını işlemek için fonksiyonlar sağlayan ast modülünü içe aktar
    import ast
    
    # Modelin etiketlerinde 'finetune_compute_allow_list' etiketinin olup olmadığını kontrol et
    if "finetune_compute_allow_list" in foundation_model.tags:
        # Eğer etiket varsa, etiketin değerini (bir string) güvenli bir şekilde bir Python listesine dönüştürmek için ast.literal_eval kullan
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # stringi python listesine dönüştür
        # Listeden bir compute oluşturulacağını belirten bir mesaj yazdır
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Eğer etiket yoksa, computes_allow_list'i None olarak ata
        computes_allow_list = None
        # 'finetune_compute_allow_list' etiketinin modelin etiketlerinin bir parçası olmadığını belirten bir mesaj yazdır
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Hesaplama Örneğini Kontrol Etme

1. Bu Python betiği Azure Machine Learning (Azure ML) servisi ile etkileşimde bulunur ve bir hesaplama örneği üzerinde çeşitli kontroller yapar. İşte yaptığı şeyler:

    - compute_cluster değişkeninde adı saklanan hesaplama örneğini Azure ML çalışma alanından almaya çalışır. Eğer hesaplama örneğinin provisioning durumu "failed" ise ValueError fırlatır.

    - computes_allow_list değişkeni None değilse, listedeki tüm hesaplama boyutlarını küçük harfe çevirir ve mevcut hesaplama örneğinin boyutunu listedekilerle karşılaştırır. Eğer listede yoksa ValueError fırlatır.

    - computes_allow_list None ise, desteklenmeyen GPU VM boyutları listesinde mevcut hesaplama boyutu olup olmadığını kontrol eder. Varsa ValueError fırlatır.

    - Çalışma alanındaki tüm kullanılabilir hesaplama boyutlarının listesini alır. Listenin üzerinde döner, mevcut hesaplama örneğinin boyutu ile eşleşen ismi bulursa, o hesaplama boyutundaki GPU sayısını alır ve gpu_count_found değişkenini True yapar.

    - gpu_count_found True ise hesaplama örneğindeki GPU sayısını yazdırır. False ise ValueError fırlatır.

    - Özetle, betik Azure ML çalışma alanındaki bir hesaplama örneği üzerinde provisioning durumunu, izin verilen veya karşı çıkılan listeye uygunluğunu ve sahip olduğu GPU sayısını kontrol eder.
    
    ```python
    # İstisna mesajını yazdır
    print(e)
    # İş alanında hesaplama boyutu mevcut değilse ValueError yükselt
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Azure ML iş alanından hesaplama örneğini al
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Hesaplama örneğinin sağlama durumunun "failed" olup olmadığını kontrol et
    if compute.provisioning_state.lower() == "failed":
        # Sağlama durumu "failed" ise ValueError yükselt
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # computes_allow_list'in None olmadığını kontrol et
    if computes_allow_list is not None:
        # computes_allow_list'teki tüm hesaplama boyutlarını küçük harfe çevir
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Hesaplama örneğinin boyutunun computes_allow_list_lower_case içinde olup olmadığını kontrol et
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Hesaplama örneğinin boyutu computes_allow_list_lower_case içinde değilse ValueError yükselt
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Desteklenmeyen GPU VM boyutlarının bir listesini tanımla
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Hesaplama örneğinin boyutunun unsupported_gpu_vm_list içinde olup olmadığını kontrol et
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Hesaplama örneğinin boyutu unsupported_gpu_vm_list içindeyse ValueError yükselt
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Hesaplama örneğinde GPU sayısının bulunup bulunmadığını kontrol etmek için bir bayrak başlat
    gpu_count_found = False
    # İş alanındaki tüm mevcut hesaplama boyutlarının bir listesini al
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Mevcut hesaplama boyutları listesinde döngü oluştur
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Hesaplama boyutunun adı ile hesaplama örneğinin boyutunun eşleşip eşleşmediğini kontrol et
        if compute_sku.name.lower() == compute.size.lower():
            # Eşleşirse, o hesaplama boyutundaki GPU sayısını al ve gpu_count_found değerini True yap
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # gpu_count_found True ise, hesaplama örneğindeki GPU sayısını yazdır
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # gpu_count_found False ise ValueError yükselt
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. Modeli ince ayar yapmak için veri kümesini seçin

1. ultrachat_200k veri kümesini kullanıyoruz. Veri kümesinin dört bölümü vardır ve Denetimli ince ayar (sft) için uygundur.
Oluşturma sıralaması (gen). Bölüm başına örnek sayısı aşağıda gösterilmiştir:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Sonraki birkaç hücre, ince ayar için temel veri hazırlamayı gösterir:

### Bazı veri satırlarını görselleştirme

Bu örneğin hızlı çalışmasını istiyoruz, bu yüzden önceden kırpılmış satırların %5'ini içeren train_sft, test_sft dosyalarını kaydedin. Bu nedenle ince ayarlı model daha düşük doğrulukta olacak, bu yüzden gerçek dünyada kullanılmamalıdır.
download-dataset.py ultrachat_200k veri kümesini indirir ve veri kümesini ince ayar iş akışı bileşeni için kullanılabilir formata dönüştürür. Ayrıca veri kümesi büyük olduğundan burada sadece bir kısmı mevcuttur.

1. Aşağıdaki komut yalnızca verilerin %5'ini indirir. dataset_split_pc parametresini istediğiniz yüzdeye değiştirerek arttırabilirsiniz.

> [!NOTE]
> Bazı dil modellerinin farklı dil kodları vardır, bu nedenle veri kümesindeki sütun adları da aynı olmalıdır.

1. Veri şu şekilde olmalıdır
Sohbet tamamlama veri kümesi parquet formatında saklanır ve her giriş aşağıdaki şemayı kullanır:

    - Bu, JSON (JavaScript Nesne Gösterimi) belgesidir, popüler bir veri değişim formatıdır. Çalıştırılabilir kod değil, veri depolama ve taşımak için kullandığımız bir yapıdır. Yapısının dökümü:

    - "prompt": Bir görevi veya yapay zekâ asistanına sorulan soruyu temsil eden string değer.

    - "messages": Bir dizi nesne içerir. Her nesne kullanıcı ile yapay zekâ asistanı arasındaki konuşmadaki bir mesajı temsil eder. Her mesaj nesnesinde iki anahtar vardır:

    - "content": Mesaj içeriğinin string değeri.
    - "role": Mesajı gönderen türü temsil eden string (kullanıcı ya da asistan).
    - "prompt_id": Her prompt için benzersiz tanımlayıcı string.

1. Bu özel JSON belgesinde, bir kullanıcının distopik bir hikaye için bir baş kahraman yaratmasını istediği ve asistanın yanıt verdiği bir konuşma gösterilmektedir. Kullanıcı daha ayrıntı ister ve asistan onaylar. Tüm konuşma belirli bir prompt_id ile ilişkilidir.

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

### Veriyi İndirme

1. Bu Python betiği download-dataset.py adında yardımcı bir betik kullanarak bir veri kümesini indirir. İşte yaptığı işlerin dökümü:

    - os modülünü içe aktarır; işletim sistemi fonksiyonlarına taşınabilir erişim sağlar.

    - os.system fonksiyonunu kullanarak shell'de download-dataset.py betiğini belirli komut satırı argümanlarıyla çalıştırır. Argümanlar indirilecek veri kümesi (HuggingFaceH4/ultrachat_200k), indirileceği dizin (ultrachat_200k_dataset) ve veri kümesinin yüzde kaçının bölüneceği (5) bilgilerini içerir. os.system komutun çıkış durumunu döndürür; bu değer exit_status değişkenine atanır.

    - exit_status 0 değilse (Unix sistemlerinde 0 komutun başarılı olduğunu gösterir), bir Exception fırlatılır ve veri kümesi indirme hatası olduğu belirtilir.

    - Özetle, betik bir yardımcı betik çalıştırarak veri kümesi indirir ve eğer komut başarısız olursa istisna fırlatır.

    ```python
    # İşletim sistemi bağımlı işlevselliği kullanmanın bir yolunu sağlayan os modülünü içe aktarın
    import os
    
    # Belirli komut satırı argümanlarıyla download-dataset.py betiğini kabukta çalıştırmak için os.system fonksiyonunu kullanın
    # Argümanlar indirilecek veri setini (HuggingFaceH4/ultrachat_200k), indirileceği dizini (ultrachat_200k_dataset) ve veri setinin bölünecek yüzdesini (5) belirtir
    # os.system fonksiyonu çalıştırdığı komutun çıkış durumunu döner; bu durum exit_status değişkeninde saklanır
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # exit_status'un 0 olup olmadığını kontrol edin
    # Unix-benzeri işletim sistemlerinde, çıkış durumu 0 genellikle bir komutun başarıyla tamamlandığını, diğer herhangi bir sayı ise bir hata olduğunu gösterir
    # Eğer exit_status 0 değilse, veri setini indirme sırasında hata olduğunu belirten bir mesajla Exception fırlatın
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### Veriyi DataFrame'e Yükleme

1. Bu Python betiği bir JSON Lines dosyasını pandas DataFrame olarak yükler ve ilk 5 satırı gösterir. İşte yaptığı işlerin dökümü:

    - Güçlü veri işleme ve analiz kütüphanesi pandas'ı içe aktarır.

    - pandas görüntüleme seçenekleri için maksimum sütun genişliğini 0 olarak ayarlar. Bu, DataFrame yazdırılırken her sütunun tam metninin kesilmeden gösterileceği anlamına gelir.
    - pd.read_json işlevini kullanarak ultrachat_200k_dataset dizinindeki train_sft.jsonl dosyasını bir DataFrame içine yükler. lines=True argümanı, dosyanın her satırında ayrı bir JSON nesnesi bulunan JSON Lines formatında olduğunu belirtir.

    - DataFrame'in ilk 5 satırını göstermek için head metodunu kullanır. DataFrame 5 satırdan azsa, tüm satırları gösterir.

    - Özetle, bu betik bir JSON Lines dosyasını DataFrame'e yükler ve tam sütun metniyle ilk 5 satırı görüntüler.
    
    ```python
    # Güçlü bir veri manipülasyonu ve analiz kütüphanesi olan pandas kütüphanesini içe aktar
    import pandas as pd
    
    # pandas'ın görüntüleme seçenekleri için maksimum sütun genişliğini 0 olarak ayarla
    # Bu, DataFrame yazdırıldığında her sütunun tam metninin kısaltılmadan gösterileceği anlamına gelir
    pd.set_option("display.max_colwidth", 0)
    
    # ultrachat_200k_dataset dizinindeki train_sft.jsonl dosyasını bir DataFrame'e yüklemek için pd.read_json fonksiyonunu kullan
    # lines=True argümanı, dosyanın her satırının ayrı bir JSON nesnesi olduğu JSON Lines formatında olduğunu belirtir
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # DataFrame'in ilk 5 satırını göstermek için head metodunu kullan
    # Eğer DataFrame 5'ten az satıra sahipse, tümünü gösterir
    df.head()
    ```

## 5. Model ve verileri giriş olarak kullanarak ince ayar işini gönderin

Chat-completion pipeline bileşenini kullanan işi oluşturun. İnce ayar için desteklenen tüm parametreler hakkında daha fazla bilgi edinin.

### İnce ayar parametrelerini tanımlayın

1. İnce ayar parametreleri 2 kategoriye ayrılabilir - eğitim parametreleri, optimizasyon parametreleri

1. Eğitim parametreleri aşağıdaki gibi eğitimle ilgili unsurları tanımlar -

    - Kullanılacak optimizasyon, zamanlayıcı
    - İnce ayarı optimize etmek için metrik
    - Eğitim adımları sayısı, batch büyüklüğü vb.
    - Optimizasyon parametreleri GPU belleğini optimize etmeye ve hesaplama kaynaklarını etkin kullanmaya yardımcı olur.

1. Aşağıda bu kategoriye ait bazı parametreler verilmiştir. Optimizasyon parametreleri modelden modele farklılık gösterir ve bu varyasyonları yönetmek için modelle birlikte paketlenir.

    - Deepspeed ve LoRA'yı etkinleştir
    - Karışık hassasiyet eğitimini etkinleştir
    - Çok düğümlü eğitimi etkinleştir

> [!NOTE]
> Gözetimli ince ayar hizalanmanın bozulmasına veya felaket unutmaya yol açabilir. Bu sorunu kontrol etmenizi ve ince ayardan sonra bir hizalama aşaması çalıştırmanızı öneririz.

### İnce Ayar Parametreleri

1. Bu Python betiği bir makine öğrenimi modelini ince ayar yapmak için parametreler ayarlıyor. İşte yaptığı şeylerin özeti:

    - Eğitim epoch sayısı, eğitim ve değerlendirme için batch boyutları, öğrenme hızı ve öğrenme hızı zamanlayıcı türü gibi varsayılan eğitim parametrelerini ayarlar.

    - Layer-wise Relevance Propagation (LoRa) ve DeepSpeed uygulaması ile DeepSpeed aşaması gibi varsayılan optimizasyon parametrelerini ayarlar.

    - Eğitim ve optimizasyon parametrelerini finetune_parameters adlı tek bir sözlükte birleştirir.

    - foundation_model'ın model-spesifik varsayılan parametreleri olup olmadığını kontrol eder. Varsa, bir uyarı mesajı yazdırır ve finetune_parameters sözlüğünü bu model-spesifik varsayılanlarla günceller. ast.literal_eval fonksiyonu model-spesifik varsayılanları string'den Python sözlüğüne dönüştürmek için kullanılır.

    - Çalıştırma için kullanılacak son ince ayar parametrelerini yazdırır.

    - Özetle, bu betik bir makine öğrenimi modelini ince ayar yapmak için parametreleri ayarlar ve gösterir; varsayılan parametrelerin model-spesifik olanlarla üzerine yazılmasına izin verir.

    ```python
    # Eğitim epoch sayısı, eğitim ve değerlendirme için batch boyutları, öğrenme hızı ve öğrenme hızı zamanlayıcı türü gibi varsayılan eğitim parametrelerini ayarla
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Layer-wise Relevance Propagation (LoRa) ve DeepSpeed uygulanıp uygulanmayacağı, ayrıca DeepSpeed aşaması gibi varsayılan optimizasyon parametrelerini ayarla
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Eğitim ve optimizasyon parametrelerini finetune_parameters adlı tek bir sözlükte birleştir
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # foundation_model'in model-özgü varsayılan parametrelerinin olup olmadığını kontrol et
    # Eğer varsa, bir uyarı mesajı yazdır ve finetune_parameters sözlüğünü bu model-özgü varsayılanlarla güncelle
    # ast.literal_eval fonksiyonu model-özgü varsayılanları string'den Python sözlüğüne dönüştürmek için kullanılır
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # string'i python sözlüğüne dönüştür
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Koşu için kullanılacak son ince ayar parametre setini yazdır
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Eğitim Pipeline'ı

1. Bu Python betiği, bir makine öğrenimi eğitim pipeline'ı için bir görüntüleme adı oluşturmak üzere bir fonksiyon tanımlar ve sonra bu fonksiyonu çağırarak görüntüleme adını oluşturur ve yazdırır. İşte yaptığı şeylerin özeti:

1. get_pipeline_display_name fonksiyonu tanımlanır. Bu fonksiyon eğitim pipeline'ı ile ilgili çeşitli parametrelere bağlı olarak bir görüntüleme adı oluşturur.

1. Fonksiyon içinde, cihaz başına batch büyüklüğü, gradyan birikim adımları sayısı, düğüm başına GPU sayısı ve ince ayarda kullanılan düğüm sayısı çarpılarak toplam batch büyüklüğü hesaplanır.

1. Öğrenme hızı zamanlayıcı türü, DeepSpeed uygulanması, DeepSpeed aşaması, Layer-wise Relevance Propagation (LoRa) uygulanması, saklanacak model kontrol noktaları sayısı sınırı ve maksimum sıra uzunluğu gibi diğer parametreler alınır.

1. Bu parametreleri içeren, tireyle ayrılmış bir string oluşturulur. DeepSpeed veya LoRa uygulanıyorsa, string sırasıyla "ds" ve DeepSpeed aşaması ya da "lora" içerir. Uygulanmıyorsa, sırasıyla "nods" veya "nolora" içerir.

1. Fonksiyon bu stringi döndürür ve bu string eğitim pipeline'ı için görüntüleme adı olarak kullanılır.

1. Fonksiyon tanımlandıktan sonra çağrılır, görüntüleme adı oluşturulur ve yazdırılır.

1. Özetle, bu betik, çeşitli parametrelere dayalı olarak bir makine öğrenimi eğitim pipeline'ı için bir görüntüleme adı oluşturur ve bu görüntüleme adını yazdırır.

    ```python
    # Eğitim boru hattı için bir görüntü adı oluşturmak amacıyla bir fonksiyon tanımlayın
    def get_pipeline_display_name():
        # Cihaz başına mini-batch boyutunu, gradyan biriktirme adımlarının sayısını, düğüm başına GPU sayısını ve ince ayar için kullanılan düğüm sayısını çarparak toplam mini-batch boyutunu hesaplayın
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Öğrenme hızı zamanlayıcı türünü alın
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # DeepSpeed'in uygulanıp uygulanmadığını alın
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # DeepSpeed aşamasını alın
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # DeepSpeed uygulanıyorsa, görüntü adına "ds" ve ardından DeepSpeed aşamasını ekleyin; uygulanmıyorsa "nods" ekleyin
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Katman Bazlı Alaka Dağılımı (LoRa) uygulanıp uygulanmadığını alın
        lora = finetune_parameters.get("apply_lora", "false")
        # LoRa uygulanıyorsa, görüntü adına "lora" ekleyin; uygulanmıyorsa "nolora" ekleyin
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Saklanacak model kontrol noktalarının sayısı sınırını alın
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Maksimum sıra uzunluğunu alın
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Tüm bu parametreleri tire ile ayırarak görüntü adını oluşturun
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
    
    # Görüntü adı oluşturmak için fonksiyonu çağırın
    pipeline_display_name = get_pipeline_display_name()
    # Görüntü adını yazdırın
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Pipeline'ı Konfigüre Etme

Bu Python betiği, Azure Machine Learning SDK kullanarak bir makine öğrenimi pipeline'ı tanımlar ve yapılandırır. İşte yaptığı şeylerin özeti:

1. Azure AI ML SDK'dan gerekli modülleri içe aktarır.

1. Kayıt defterinden "chat_completion_pipeline" adlı bir pipeline bileşeni getirir.

1. `@pipeline` dekoratörü ve `create_pipeline` fonksiyonunu kullanarak bir pipeline işi tanımlar. Pipeline adı `pipeline_display_name` olarak ayarlanır.

1. `create_pipeline` fonksiyonu içinde, getirilen pipeline bileşenini model yolu, farklı aşamalar için hesaplama küme kümeleri, eğitim ve test için veri seti bölümleri, ince ayar için kullanılacak GPU sayısı ve diğer ince ayar parametreleri ile başlatır.

1. İnce ayar işinin çıktısını pipeline işinin çıktısına eşler. Bu, ince ayarlanmış modelin kolayca kaydedilmesini sağlar ki bu, modeli çevrimiçi veya toplu uç noktaya dağıtmak için gereklidir.

1. `create_pipeline` fonksiyonunu çağırarak bir pipeline örneği oluşturur.

1. Pipeline'ın `force_rerun` ayarını `True` olarak belirler, yani önceki işlerden önbelleğe alınmış sonuçlar kullanılmayacaktır.

1. Pipeline'ın `continue_on_step_failure` ayarını `False` olarak belirler, yani herhangi bir adım başarısız olursa pipeline duracaktır.

1. Özetle, bu betik Azure Machine Learning SDK ile bir sohbet tamamlama görevi için bir makine öğrenimi pipeline'ı tanımlar ve yapılandırır.

    ```python
    # Azure AI ML SDK'sından gerekli modülleri içe aktar
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Kayıt defterinden "chat_completion_pipeline" adlı boru hattı bileşenini al
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # @pipeline dekoratörü ve create_pipeline fonksiyonunu kullanarak boru hattı işini tanımla
    # Boru hattının adı pipeline_display_name olarak ayarlandı
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Alınan boru hattı bileşenini çeşitli parametrelerle başlat
        # Bunlar model yolu, farklı aşamalar için hesaplama kümeleri, eğitim ve test için veri kümesi bölümleri, ince ayar için kullanılacak GPU sayısı ve diğer ince ayar parametrelerini içerir
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Veri kümesi bölümlerini parametrelere eşleştir
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Eğitim ayarları
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Hesaplamadaki mevcut GPU sayısına ayarlandı
            **finetune_parameters
        )
        return {
            # İnce ayar işinin çıktısını boru hattı işinin çıktısına eşleştir
            # Böylece ince ayarlanmış modeli kolayca kaydedebiliriz
            # Modeli kayıt etmek, modeli çevrimiçi veya toplu uç noktaya dağıtmak için gereklidir
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # create_pipeline fonksiyonunu çağırarak boru hattı örneği oluştur
    pipeline_object = create_pipeline()
    
    # Önceki işlerden önbelleğe alınmış sonuçları kullanma
    pipeline_object.settings.force_rerun = True
    
    # Adım hatasında devam etmeyi False olarak ayarla
    # Bu, herhangi bir adım başarısız olursa boru hattının duracağı anlamına gelir
    pipeline_object.settings.continue_on_step_failure = False
    ```

### İşi Gönder

1. Bu Python betiği, bir makine öğrenimi pipeline işini bir Azure Machine Learning çalışma alanına gönderir ve işin tamamlanmasını bekler. İşte yaptığı şeylerin özeti:

    - workspace_ml_client içindeki jobs nesnesinin create_or_update metodunu çağırarak pipeline işini gönderir. Çalıştırılacak pipeline pipeline_object ile, işin yürütüleceği deney ise experiment_name ile belirtilir.

    - Daha sonra, workspace_ml_client içindeki jobs nesnesinin stream metodunu çağırarak pipeline işinin tamamlanmasını bekler. Beklenecek iş pipeline_job nesnesinin name özelliğiyle belirtilir.

    - Özetle, bu betik bir makine öğrenimi pipeline işini Azure Machine Learning çalışma alanına gönderir ve işin tamamlanmasını bekler.

    ```python
    # Pipelin işini Azure Makine Öğrenimi çalışma alanına gönder
    # Çalıştırılacak pipeline, pipeline_object tarafından belirtilmiştir
    # İşin çalıştırıldığı deney, experiment_name tarafından belirtilmiştir
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Pipeline işinin tamamlanmasını bekle
    # Beklenecek iş, pipeline_job nesnesinin name özniteliğiyle belirtilmiştir
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. İnce ayarlanmış modeli çalışma alanına kaydedin

Modeli ince ayar işinin çıktısından kaydedeceğiz. Bu, ince ayarlanmış model ile ince ayar işi arasındaki soy ağacını takip eder. İnce ayar işi ayrıca temel model, veri ve eğitim koduna olan soy ağacını takip eder.

### ML Modelini Kaydetme

1. Bu Python betiği, Azure Machine Learning pipeline'ında eğitilmiş bir makine öğrenimi modelini kaydediyor. İşte yaptığı şeylerin özeti:

    - Azure AI ML SDK'dan gerekli modülleri içe aktarır.

    - workspace_ml_client içindeki jobs nesnesinin get metodunu çağırarak pipeline işinin çıktısı olan trained_model'in olup olmadığını kontrol eder.

    - Pipeline işinin adı ve çıktı adı ("trained_model") kullanılarak eğitilmiş modelin yolu oluşturulur.

    - Orijinal model adına "-ultrachat-200k" ekleyerek ve varsa tüm eğik çizgileri tireyle değiştirerek ince ayarlanmış model için bir ad belirler.

    - Model nesnesi oluşturarak modeli kaydetmek üzere hazırlanır; model yolu, model türü (MLflow modeli), adı, sürümü ve açıklaması gibi parametreler içerir.

    - workspace_ml_client içindeki models nesnesinin create_or_update metodunu çağırarak Model nesnesi ile modeli kaydeder.

    - Kayıtlı modeli yazdırır.

1. Özetle, bu betik Azure Machine Learning pipeline'ında eğitilmiş bir makine öğrenimi modelini kaydeder.
    
    ```python
    # Azure AI ML SDK'dan gerekli modülleri içe aktar
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Pipeline işinden `trained_model` çıktısının kullanılabilir olup olmadığını kontrol et
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Pipeline işinin adı ve çıktı adı ("trained_model") ile biçimlendirilmiş bir dize kullanarak eğitilmiş modele giden bir yol oluştur
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Orijinal model adına "-ultrachat-200k" ekleyerek ve varsa eğik çizgileri kısa çizgilerle değiştirerek ince ayarlı model için bir ad tanımla
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Çeşitli parametrelerle bir Model nesnesi oluşturarak modeli kayıt etmeye hazırla
    # Bunlar modele giden yol, model türü (MLflow modeli), modelin adı ve sürümü ile model açıklamasını içerir
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Sürüm çakışmasını önlemek için sürüm olarak zaman damgası kullan
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Model nesnesini argüman olarak kullanarak workspace_ml_client içindeki modeller nesnesinin create_or_update metodunu çağırarak modeli kaydet
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Kayıtlı modeli yazdır
    print("registered model: \n", registered_model)
    ```

## 7. İnce ayarlanmış modeli bir online uç noktaya dağıtın

Online uç noktalar, modeli kullanması gereken uygulamalarla entegre etmek için kullanılabilen kalıcı bir REST API sağlar.

### Uç Noktayı Yönetme

1. Bu Python betiği, Azure Machine Learning'de kayıtlı bir model için yönetilen bir online uç nokta oluşturur. İşte yaptığı şeylerin özeti:

    - Azure AI ML SDK'dan gerekli modülleri içe aktarır.

    - "ultrachat-completion-" dizesine zaman damgası ekleyerek benzersiz bir online uç nokta adı tanımlar.

    - Online uç noktayı oluşturmak üzere ad, açıklama ve kimlik doğrulama modu ("key") içeren bir ManagedOnlineEndpoint nesnesi oluşturur.

    - workspace_ml_client içindeki begin_create_or_update metodunu çağırarak online uç noktayı oluşturur ve wait metodu ile oluşturma işleminin tamamlanmasını bekler.

1. Özetle, bu betik Azure Machine Learning'de kayıtlı bir model için yönetilen bir online uç nokta oluşturur.

    ```python
    # Azure AI ML SDK'dan gerekli modülleri içe aktar
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # "ultrachat-completion-" dizisine zaman damgası ekleyerek çevrimiçi uç nokta için benzersiz bir ad tanımla
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Çeşitli parametrelerle bir ManagedOnlineEndpoint nesnesi oluşturarak çevrimiçi uç nokta oluşturulmaya hazırla
    # Bunlar uç nokta adı, uç nokta açıklaması ve kimlik doğrulama modu ("key") içerir
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Workspace_ml_client'ın begin_create_or_update metodunu ManagedOnlineEndpoint nesnesi argümanı ile çağırarak çevrimiçi uç noktayı oluştur
    # Ardından, oluşturma işleminin tamamlanmasını beklemek için wait metodunu çağır
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> Dağıtım için desteklenen SKU listesine buradan ulaşabilirsiniz - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### ML Modeli Dağıtımı

1. Bu Python betiği, kayıtlı bir makine öğrenimi modelini Azure Machine Learning'de yönetilen bir online uç noktaya dağıtıyor. İşte yaptığı şeylerin özeti:

    - Python'un soyut sözdizim ağacı işlem fonksiyonlarını sağlayan ast modülünü içe aktarır.

    - Dağıtım için örnek türünü "Standard_NC6s_v3" olarak ayarlar.

    - foundation_model içinde inference_compute_allow_list etiketi varsa, etiketi string'den Python listesine dönüştürür ve inference_computes_allow_list'e atar. Yoksa bu değişkeni None yapar.

    - Belirtilen örnek türünün izin listesinde olup olmadığını kontrol eder. Yoksa, kullanıcıdan izin listesinden bir örnek türü seçmesini isteyen bir mesaj yazdırır.

    - Dağıtımı oluşturmak için, dağıtım adı, uç nokta adı, model ID'si, örnek türü ve sayısı, canlılık denetimi ayarları ve istek ayarları gibi parametreleri içeren bir ManagedOnlineDeployment nesnesi oluşturur.

    - workspace_ml_client içindeki begin_create_or_update metodunu çağırarak dağıtımı oluşturur ve wait metodu ile işlem tamamlanana kadar bekler.

    - Uç noktanın trafiğini yüzde 100 olarak "demo" dağıtımına yönlendirir.

    - workspace_ml_client içindeki begin_create_or_update metodunu uç nokta nesnesi ile çağırarak günceller ve result metodu ile güncelleme tamamlanana kadar bekler.

1. Özetle, bu betik Azure Machine Learning'de kayıtlı bir makine öğrenimi modelini yönetilen bir online uç noktaya dağıtır.

    ```python
    # Python soyut sözdizimi ağacı işlemleri için işlevler sağlayan ast modülünü içe aktar
    import ast
    
    # Dağıtım için örnek tipini ayarla
    instance_type = "Standard_NC6s_v3"
    
    # Foundation modelde `inference_compute_allow_list` etiketinin olup olmadığını kontrol et
    if "inference_compute_allow_list" in foundation_model.tags:
        # Eğer varsa, etiket değerini bir stringden Python listesine dönüştür ve `inference_computes_allow_list`'e ata
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Yoksa, `inference_computes_allow_list`'i `None` olarak ayarla
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Belirtilen örnek tipinin izin listesinde olup olmadığını kontrol et
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Çeşitli parametrelerle bir `ManagedOnlineDeployment` nesnesi oluşturarak dağıtımı hazırlamaya başla
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # `workspace_ml_client`'ın `begin_create_or_update` metodunu `ManagedOnlineDeployment` nesnesi ile çağırarak dağıtımı oluştur
    # Ardından oluşturma işleminin tamamlanmasını `wait` metodunu çağırarak bekle
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Endpoint trafiğini "demo" dağıtımına %100 yönlendirecek şekilde ayarla
    endpoint.traffic = {"demo": 100}
    
    # `workspace_ml_client`'ın `begin_create_or_update` metodunu `endpoint` nesnesi ile çağırarak endpoint'i güncelle
    # Ardından güncelleme işleminin tamamlanmasını `result` metodunu çağırarak bekle
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. Örnek verilerle uç noktayı test etme

Test veri setinden bazı örnek verileri alıp online uç noktaya çıkarım için göndeririz. Sonra skorlanan etiketleri gerçek etiketlerle birlikte gösteririz.

### Sonuçları Okuma

1. Bu Python betiği, bir JSON Lines dosyasını pandas DataFrame'e okur, rastgele örnek alır ve indeksleri sıfırlar. İşte yaptığı şeylerin özeti:

    - ./ultrachat_200k_dataset/test_gen.jsonl dosyasını pandas DataFrame'e okur. read_json işlevi lines=True argümanı ile kullanılır çünkü dosya JSON Lines formatındadır ve her satır ayrı bir JSON nesnesidir.

    - DataFrame'den rastgele 1 satır örneği alır. sample işlevi n=1 argümanı ile seçilen rastgele satır sayısını belirtir.

    - DataFrame indeksini sıfırlar. reset_index işlevi drop=True argümanı ile orijinal indeks bırakılır ve yerine varsayılan tam sayı indeks verilir.

    - head işlevi 2 argümanı ile DataFrame'in ilk 2 satırını gösterir. Ancak örnekleme sonrası DataFrame sadece 1 satır içerdiğinden sadece o satır gösterilecektir.

1. Özetle, bu betik bir JSON Lines dosyasını pandas DataFrame'e okur, rastgele 1 satır örnek alır, indeksi sıfırlar ve ilk satırı gösterir.
    
    ```python
    # pandas kütüphanesini içe aktar
    import pandas as pd
    
    # JSON Lines dosyası './ultrachat_200k_dataset/test_gen.jsonl' dosyasını pandas DataFrame olarak oku
    # 'lines=True' argümanı dosyanın her satırın ayrı bir JSON nesnesi olduğu JSON Lines formatında olduğunu belirtir
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # DataFrame'den rastgele 1 satır örnek al
    # 'n=1' argümanı seçilecek rastgele satır sayısını belirtir
    test_df = test_df.sample(n=1)
    
    # DataFrame'in indeksini sıfırla
    # 'drop=True' argümanı orijinal indeksin atılacağını ve yerine varsayılan tam sayı değerlerinden oluşan yeni bir indeks konacağını belirtir
    # 'inplace=True' argümanı DataFrame'in yerinde değiştirilmesi gerektiğini (yeni bir nesne oluşturulmadan) belirtir
    test_df.reset_index(drop=True, inplace=True)
    
    # DataFrame'in ilk 2 satırını göster
    # Ancak, örnekleme sonrası DataFrame yalnızca bir satır içerdiği için bu sadece o bir satırı gösterecektir
    test_df.head(2)
    ```

### JSON Nesnesi Oluşturma

1. Bu Python betiği, belirli parametrelerle bir JSON nesnesi oluşturur ve bir dosyaya kaydeder. İşte yaptığı şeylerin özeti:

    - JSON verileriyle çalışmak için fonksiyonlar sağlayan json modülünü içe aktarır.
    - Bir makine öğrenimi modeli için parametreleri temsil eden anahtarlar ve değerlerle bir sözlük parameters oluşturur. Anahtarlar "temperature", "top_p", "do_sample" ve "max_new_tokens" olup karşılık gelen değerleri sırasıyla 0.6, 0.9, True ve 200'dür.

    - İki anahtara sahip başka bir sözlük test_json oluşturur: "input_data" ve "params". "input_data" değeri, "input_string" ve "parameters" anahtarlarına sahip başka bir sözlüktür. "input_string" değeri, test_df DataFrame'inden alınan ilk mesajı içeren bir listedir. "parameters" değeri, önceden oluşturulan parameters sözlüğüdür. "params" değeri ise boş bir sözlüktür.

    - sample_score.json adlı bir dosya açar.
    
    ```python
    # JSON verileriyle çalışmak için işlevler sağlayan json modülünü içe aktar
    import json
    
    # Bir makine öğrenimi modeli için parametreleri temsil eden anahtarlar ve değerlerle bir sözlük `parameters` oluştur
    # Anahtarlar "temperature", "top_p", "do_sample" ve "max_new_tokens" olup, karşılık gelen değerleri sırasıyla 0.6, 0.9, True ve 200'dür
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # "input_data" ve "params" olmak üzere iki anahtarı olan başka bir sözlük `test_json` oluştur
    # "input_data" değeri, "input_string" ve "parameters" anahtarlarına sahip başka bir sözlüktür
    # "input_string" değeri, `test_df` Veri Çerçevesinden ilk mesajı içeren bir listedir
    # "parameters" değeri, daha önce oluşturulan `parameters` sözlüğüdür
    # "params" değeri boş bir sözlüktür
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # `./ultrachat_200k_dataset` dizininde `sample_score.json` adlı dosyayı yazma modunda aç
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # `test_json` sözlüğünü JSON formatında `json.dump` fonksiyonunu kullanarak dosyaya yaz
        json.dump(test_json, f)
    ```

### Uç Noktayı Çağırma

1. Bu Python betiği, Azure Machine Learning'de bir çevrimiçi uç noktayı, bir JSON dosyasını puanlamak için çağırmaktadır. İşte yaptığı şeyin bir özeti:

    - workspace_ml_client nesnesinin online_endpoints özelliğinin invoke metodunu çağırır. Bu metod, çevrimiçi bir uç noktaya istek göndermek ve yanıt almak için kullanılır.

    - endpoint_name ve deployment_name argümanları ile uç noktanın ve dağıtımın adını belirtir. Bu durumda, uç nokta adı online_endpoint_name değişkeninde saklanır ve dağıtım adı "demo"dur.

    - İsteği yapılacak JSON dosyasının yolunu request_file argümanı ile belirtir. Bu durumda dosya ./ultrachat_200k_dataset/sample_score.json'dur.

    - Uç noktadan gelen yanıtı response değişkenine kaydeder.

    - Ham yanıtı yazdırır.

1. Özetle, bu betik Azure Machine Learning'de bir çevrimiçi uç noktayı JSON dosyasını puanlamak için çağırmakta ve yanıtı yazdırmaktadır.

    ```python
    # Azure Machine Learning'de çevrimiçi uç noktayı çağırarak `sample_score.json` dosyasını puanlayın
    # `workspace_ml_client` nesnesinin `online_endpoints` özelliğinin `invoke` metodu, bir çevrimiçi uç noktaya istek göndermek ve yanıt almak için kullanılır
    # `endpoint_name` argümanı, uç noktanın adını belirtir ve bu ad `online_endpoint_name` değişkeninde saklanır
    # `deployment_name` argümanı, dağıtımın adını belirtir, bu da "demo"dur
    # `request_file` argümanı, puanlanacak JSON dosyasının yolunu belirtir; bu yol `./ultrachat_200k_dataset/sample_score.json`'dur
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Uç noktadan alınan ham yanıtı yazdırır
    print("raw response: \n", response, "\n")
    ```

## 9. Çevrimiçi uç noktayı silme

1. Çevrimiçi uç noktayı silmeyi unutmayın, aksi takdirde uç noktanın kullandığı hesaplama için faturalandırma sayacı çalışmaya devam eder. Bu Python kod satırı, Azure Machine Learning'de bir çevrimiçi uç noktayı silmektedir. İşte yaptığı şeyin bir özeti:

    - workspace_ml_client nesnesinin online_endpoints özelliğinin begin_delete metodunu çağırır. Bu metot, bir çevrimiçi uç noktanın silinmesini başlatmak için kullanılır.

    - Silinecek uç noktanın adını name argümanı ile belirtir. Bu durumda, uç nokta adı online_endpoint_name değişkeninde tutulmaktadır.

    - Silme işlemi tamamlanana kadar beklemek için wait metodunu çağırır. Bu işlem engelleme işlemi olup, silme bitene kadar betiğin devamını engeller.

    - Özetle, bu kod satırı Azure Machine Learning'de bir çevrimiçi uç noktanın silinmesini başlatmakta ve işlemin tamamlanmasını beklemektedir.

    ```python
    # Azure Machine Learning'de çevrimiçi uç noktayı sil
    # `workspace_ml_client` nesnesinin `online_endpoints` özelliğinin `begin_delete` metodu, çevrimiçi uç noktanın silinmesini başlatmak için kullanılır
    # `name` argümanı, silinecek uç noktanın adını belirtir ve bu ad `online_endpoint_name` değişkeninde saklanır
    # Silme işlemi tamamlanana kadar beklemek için `wait` metodu çağrılır. Bu engelleme işlemi olup, silme işlemi tamamlanana kadar betiğin devam etmesini engeller
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belgeler, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerde hatalar veya yanlışlıklar bulunabilir. Orijinal belge, kendi ana dilindeki haliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum farklılıklarından sorumlu tutulamayız.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->