<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-05-09T16:28:04+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "tr"
}
-->
# Azure AI Foundry'de Microsoft'un Sorumlu AI İlkelerine Odaklanarak İncelenmiş Phi-3 / Phi-3.5 Modelini Değerlendirme

Bu uçtan uca (E2E) örnek, Microsoft Tech Community'den "[Microsoft'un Sorumlu AI'sına Odaklanarak Azure AI Foundry'de İncelenmiş Phi-3 / 3.5 Modellerini Değerlendirme](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" rehberine dayanmaktadır.

## Genel Bakış

### Azure AI Foundry'de ince ayarlı Phi-3 / Phi-3.5 modelinin güvenlik ve performansını nasıl değerlendirebilirsiniz?

Bir modeli ince ayarlamak bazen istenmeyen veya beklenmedik yanıtlar ortaya çıkarabilir. Modelin güvenli ve etkili kalmasını sağlamak için, modelin zararlı içerik üretme potansiyelini ve doğru, ilgili ve tutarlı yanıtlar verme yeteneğini değerlendirmek önemlidir. Bu eğitimde, Azure AI Foundry'de Prompt flow ile entegre edilmiş ince ayarlı Phi-3 / Phi-3.5 modelinin güvenlik ve performansını nasıl değerlendireceğinizi öğreneceksiniz.

İşte Azure AI Foundry'nin değerlendirme süreci.

![Eğitimin mimarisi.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.tr.png)

*Resim Kaynağı: [Generatif AI uygulamalarının değerlendirilmesi](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Phi-3 / Phi-3.5 hakkında daha ayrıntılı bilgi ve ek kaynakları keşfetmek için lütfen [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723) sayfasını ziyaret edin.

### Ön Koşullar

- [Python](https://www.python.org/downloads)
- [Azure aboneliği](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- İnce ayarlı Phi-3 / Phi-3.5 modeli

### İçindekiler

1. [**Senaryo 1: Azure AI Foundry'nin Prompt flow değerlendirmesine giriş**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Güvenlik değerlendirmesine giriş](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Performans değerlendirmesine giriş](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Senaryo 2: Azure AI Foundry'de Phi-3 / Phi-3.5 modelini değerlendirme**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Başlamadan önce](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Phi-3 / Phi-3.5 modelini değerlendirmek için Azure OpenAI'yi dağıtma](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure AI Foundry'nin Prompt flow değerlendirmesi ile ince ayarlı Phi-3 / Phi-3.5 modelini değerlendirme](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Tebrikler!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Senaryo 1: Azure AI Foundry'nin Prompt flow değerlendirmesine giriş**

### Güvenlik değerlendirmesine giriş

AI modelinizin etik ve güvenli olduğundan emin olmak için, Microsoft'un Sorumlu AI İlkeleri doğrultusunda değerlendirilmesi çok önemlidir. Azure AI Foundry'de güvenlik değerlendirmeleri, modelinizin jailbreak saldırılarına karşı savunmasızlığını ve zararlı içerik üretme potansiyelini ölçmenize olanak tanır; bu da doğrudan bu ilkelere uygundur.

![Güvenlik değerlendirmesi.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.tr.png)

*Resim Kaynağı: [Generatif AI uygulamalarının değerlendirilmesi](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft'un Sorumlu AI İlkeleri

Teknik adımlara başlamadan önce, AI sistemlerinin sorumlu geliştirilmesi, dağıtımı ve işletilmesi için rehberlik eden etik bir çerçeve olan Microsoft'un Sorumlu AI İlkelerini anlamak önemlidir. Bu ilkeler, AI teknolojilerinin adil, şeffaf ve kapsayıcı şekilde tasarlanmasını, geliştirilmesini ve dağıtılmasını sağlar. Bu ilkeler, AI modellerinin güvenliğini değerlendirmek için temel oluşturur.

Microsoft'un Sorumlu AI İlkeleri şunlardır:

- **Adalet ve Kapsayıcılık**: AI sistemleri herkese adil davranmalı ve benzer durumda olan grupları farklı şekillerde etkilemekten kaçınmalıdır. Örneğin, AI sistemleri tıbbi tedavi, kredi başvuruları veya istihdam konularında rehberlik sağlarken, benzer semptomlara, finansal duruma veya mesleki niteliklere sahip herkese aynı önerileri yapmalıdır.

- **Güvenilirlik ve Güvenlik**: Güven oluşturmak için AI sistemlerinin güvenilir, güvenli ve tutarlı çalışması kritik önemdedir. Bu sistemler, tasarlandığı şekilde çalışabilmeli, beklenmeyen durumlara güvenli yanıt verebilmeli ve zararlı manipülasyona karşı dirençli olmalıdır. Davranışları ve karşılayabildikleri durumlar, geliştiricilerin tasarım ve test aşamasında öngördüğü durumları yansıtır.

- **Şeffaflık**: AI sistemleri insanların hayatlarını derinden etkileyen kararlar alınmasına yardımcı olduğunda, insanların bu kararların nasıl verildiğini anlaması çok önemlidir. Örneğin, bir banka bir kişinin kredi değerliliğini belirlemek için AI sistemi kullanabilir. Bir şirket ise en nitelikli adayları belirlemek için AI sisteminden yararlanabilir.

- **Gizlilik ve Güvenlik**: AI yaygınlaştıkça, gizliliğin korunması ve kişisel ile ticari bilgilerin güvenliği daha önemli ve karmaşık hale geliyor. AI ile gizlilik ve veri güvenliği özel dikkat gerektirir çünkü AI sistemlerinin insanlarla ilgili doğru ve bilinçli tahminler yapabilmesi için verilere erişim şarttır.

- **Hesap Verebilirlik**: AI sistemlerini tasarlayan ve dağıtan kişiler, sistemlerinin nasıl çalıştığından sorumlu olmalıdır. Kuruluşlar, hesap verebilirlik normları geliştirmek için sektör standartlarından yararlanmalıdır. Bu normlar, AI sistemlerinin insanların hayatlarını etkileyen kararların nihai otoritesi olmamasını ve insanların yüksek otonomlu AI sistemleri üzerinde anlamlı kontrol sahibi olmasını sağlar.

![Fill hub.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.tr.png)

*Resim Kaynağı: [Sorumlu AI Nedir?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Microsoft'un Sorumlu AI İlkeleri hakkında daha fazla bilgi edinmek için [Sorumlu AI Nedir?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723) sayfasını ziyaret edin.

#### Güvenlik ölçütleri

Bu eğitimde, Azure AI Foundry'nin güvenlik ölçütlerini kullanarak ince ayarlı Phi-3 modelinin güvenliğini değerlendireceksiniz. Bu ölçütler, modelin zararlı içerik üretme potansiyelini ve jailbreak saldırılarına karşı savunmasızlığını değerlendirmenize yardımcı olur. Güvenlik ölçütleri şunları içerir:

- **Kendine Zarar Verici İçerik**: Modelin kendine zarar verici içerik üretme eğilimini değerlendirir.
- **Nefret ve Adaletsiz İçerik**: Modelin nefret dolu veya adaletsiz içerik üretme eğilimini değerlendirir.
- **Şiddet İçeriği**: Modelin şiddet içeren içerik üretme eğilimini değerlendirir.
- **Cinsel İçerik**: Modelin uygunsuz cinsel içerik üretme eğilimini değerlendirir.

Bu yönleri değerlendirmek, AI modelinin zararlı veya saldırgan içerik üretmemesini sağlar ve toplumsal değerler ile düzenleyici standartlarla uyumlu olmasını garanti eder.

![Güvenliğe dayalı değerlendirme.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.tr.png)

### Performans değerlendirmesine giriş

AI modelinizin beklendiği gibi performans gösterdiğinden emin olmak için, performans ölçütlerine göre değerlendirilmesi önemlidir. Azure AI Foundry'de performans değerlendirmeleri, modelinizin doğru, ilgili ve tutarlı yanıtlar üretme etkinliğini ölçmenize olanak tanır.

![Performans değerlendirmesi.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.tr.png)

*Resim Kaynağı: [Generatif AI uygulamalarının değerlendirilmesi](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Performans ölçütleri

Bu eğitimde, Azure AI Foundry'nin performans ölçütlerini kullanarak ince ayarlı Phi-3 / Phi-3.5 modelinin performansını değerlendireceksiniz. Bu ölçütler, modelin doğru, ilgili ve tutarlı yanıtlar üretme etkinliğini değerlendirmenize yardımcı olur. Performans ölçütleri şunları içerir:

- **Dayanaklılık (Groundedness)**: Üretilen yanıtların giriş kaynağındaki bilgiyle ne kadar uyumlu olduğunu değerlendirir.
- **Alaka Düzeyi (Relevance)**: Üretilen yanıtların sorulara ne kadar uygun olduğunu değerlendirir.
- **Tutarlılık (Coherence)**: Üretilen metnin ne kadar akıcı, doğal ve insan diline benzer olduğunu değerlendirir.
- **Akıcılık (Fluency)**: Üretilen metnin dil yeterliliğini değerlendirir.
- **GPT Benzerliği (GPT Similarity)**: Üretilen yanıt ile gerçek veri arasındaki benzerliği karşılaştırır.
- **F1 Skoru**: Üretilen yanıt ile kaynak veri arasındaki ortak kelimelerin oranını hesaplar.

Bu ölçütler, modelin doğru, ilgili ve tutarlı yanıtlar üretme etkinliğini değerlendirmede size yardımcı olur.

![Performansa dayalı değerlendirme.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.tr.png)

## **Senaryo 2: Azure AI Foundry'de Phi-3 / Phi-3.5 modelini değerlendirme**

### Başlamadan önce

Bu eğitim, önceki blog yazıları "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" ve "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" makalelerinin devamıdır. Bu yazılarda, Azure AI Foundry'de Phi-3 / Phi-3.5 modelinin ince ayar sürecini ve Prompt flow ile entegrasyonunu adım adım inceledik.

Bu eğitimde, Azure AI Foundry'de değerlendirici olarak bir Azure OpenAI modeli dağıtacak ve ince ayarlı Phi-3 / Phi-3.5 modelinizi değerlendirmek için kullanacaksınız.

Bu eğitime başlamadan önce, önceki eğitimlerde anlatıldığı şekilde aşağıdaki ön koşullara sahip olduğunuzdan emin olun:

1. İnce ayarlı Phi-3 / Phi-3.5 modelini değerlendirmek için hazırlanmış bir veri seti.
1. Azure Machine Learning üzerinde ince ayar yapılmış ve dağıtılmış bir Phi-3 / Phi-3.5 modeli.
1. Azure AI Foundry'de ince ayarlı Phi-3 / Phi-3.5 modelinizle entegre edilmiş bir Prompt flow.

> [!NOTE]
> Önceki blog yazılarında indirilen **ULTRACHAT_200k** veri setinin data klasöründe bulunan *test_data.jsonl* dosyasını, ince ayarlı Phi-3 / Phi-3.5 modelini değerlendirmek için veri seti olarak kullanacaksınız.

#### Azure AI Foundry'de Prompt flow ile özel Phi-3 / Phi-3.5 modelini entegre etme (Öncelikle kod yaklaşımı)

> [!NOTE]
> Eğer "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" başlığında anlatılan düşük kod yaklaşımını izlediyseniz, bu alıştırmayı atlayıp bir sonraki adıma geçebilirsiniz.
> Ancak, Phi-3 / Phi-3.5 modelinizi ince ayar yapmak ve dağıtmak için "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" başlığında anlatılan kod öncelikli yaklaşımı kullandıysanız, modelinizi Prompt flow'a bağlama süreci biraz farklıdır. Bu süreci bu alıştırmada öğreneceksiniz.

Devam etmek için, ince ayarlı Phi-3 / Phi-3.5 modelinizi Azure AI Foundry'de Prompt flow'a entegre etmeniz gerekiyor.

#### Azure AI Foundry Hub Oluşturma

Proje oluşturmadan önce bir Hub oluşturmanız gerekir. Hub, Azure AI Foundry içinde birden fazla projeyi düzenlemenize ve yönetmenize olanak tanıyan bir Kaynak Grubu gibi çalışır.

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) sitesine giriş yapın.

1. Sol taraftaki sekmeden **All hubs** seçeneğini seçin.

1. Navigasyon menüsünden **+ New hub** seçeneğini seçin.

    ![Hub oluşturma.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.tr.png)

1. Aşağıdaki işlemleri gerçekleştirin:

    - **Hub name** girin. Bu benzersiz bir değer olmalıdır.
    - Azure **Subscription**'ınızı seçin.
    - Kullanmak istediğiniz **Resource group**'u seçin (gerekirse yeni bir tane oluşturun).
    - Kullanmak istediğiniz **Location**'ı seçin.
    - Kullanmak istediğiniz **Connect Azure AI Services**'i seçin (gerekirse yeni bir tane oluşturun).
    - **Connect Azure AI Search** için **Skip connecting** seçeneğini işaretleyin.
![Fill hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.tr.png)

1. **Next**'i seçin.

#### Azure AI Foundry Projesi Oluşturma

1. Oluşturduğunuz Hub'da, sol taraftaki sekmeden **All projects**'i seçin.

1. Navigasyon menüsünden **+ New project**'i seçin.

    ![Select new project.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.tr.png)

1. **Project name** girin. Benzersiz bir değer olmalıdır.

    ![Create project.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.tr.png)

1. **Create a project**'i seçin.

#### Fine-tuned Phi-3 / Phi-3.5 modeli için özel bağlantı ekleme

Özel Phi-3 / Phi-3.5 modelinizi Prompt flow ile entegre etmek için modelin endpoint ve anahtarını özel bir bağlantıda kaydetmeniz gerekir. Bu ayar, Prompt flow'da özel Phi-3 / Phi-3.5 modelinize erişimi sağlar.

#### Fine-tuned Phi-3 / Phi-3.5 modelinin api anahtarı ve endpoint uri'sini ayarlama

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) adresini ziyaret edin.

1. Oluşturduğunuz Azure Machine learning çalışma alanına gidin.

1. Sol taraftaki sekmeden **Endpoints**'i seçin.

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.tr.png)

1. Oluşturduğunuz endpoint'i seçin.

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.tr.png)

1. Navigasyon menüsünden **Consume**'u seçin.

1. **REST endpoint** ve **Primary key**'i kopyalayın.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.tr.png)

#### Özel Bağlantı Ekleme

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) adresini ziyaret edin.

1. Oluşturduğunuz Azure AI Foundry projesine gidin.

1. Oluşturduğunuz projede, sol taraftaki sekmeden **Settings**'i seçin.

1. **+ New connection**'ı seçin.

    ![Select new connection.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.tr.png)

1. Navigasyon menüsünden **Custom keys**'i seçin.

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.tr.png)

1. Aşağıdaki işlemleri yapın:

    - **+ Add key value pairs**'i seçin.
    - Anahtar adı olarak **endpoint** girin ve Azure ML Studio'dan kopyaladığınız endpoint'i değer alanına yapıştırın.
    - Tekrar **+ Add key value pairs**'i seçin.
    - Anahtar adı olarak **key** girin ve Azure ML Studio'dan kopyaladığınız anahtarı değer alanına yapıştırın.
    - Anahtarları ekledikten sonra, anahtarın görünmemesi için **is secret**'i seçin.

    ![Add connection.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.tr.png)

1. **Add connection**'ı seçin.

#### Prompt flow Oluşturma

Azure AI Foundry'de özel bir bağlantı eklediniz. Şimdi aşağıdaki adımlarla bir Prompt flow oluşturacağız. Ardından, bu Prompt flow'u özel bağlantıya bağlayarak fine-tuned modeli Prompt flow içinde kullanacaksınız.

1. Oluşturduğunuz Azure AI Foundry projesine gidin.

1. Sol taraftaki sekmeden **Prompt flow**'u seçin.

1. Navigasyon menüsünden **+ Create**'i seçin.

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.tr.png)

1. Navigasyon menüsünden **Chat flow**'u seçin.

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.tr.png)

1. Kullanmak istediğiniz **Folder name** girin.

    ![Select chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.tr.png)

1. **Create**'i seçin.

#### Özel Phi-3 / Phi-3.5 modeli ile sohbet etmek için Prompt flow'u ayarlama

Fine-tuned Phi-3 / Phi-3.5 modelinizi Prompt flow'a entegre etmeniz gerekiyor. Ancak, mevcut Prompt flow bu amaç için tasarlanmamıştır. Bu nedenle, özel modeli entegre etmek için Prompt flow'u yeniden tasarlamanız gerekir.

1. Prompt flow'da mevcut akışı yeniden oluşturmak için aşağıdaki işlemleri yapın:

    - **Raw file mode**'u seçin.
    - *flow.dag.yml* dosyasındaki mevcut tüm kodu silin.
    - *flow.dag.yml* dosyasına aşağıdaki kodu ekleyin.

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

    - **Save**'i seçin.

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.tr.png)

1. Prompt flow'da özel Phi-3 / Phi-3.5 modelini kullanmak için *integrate_with_promptflow.py* dosyasına aşağıdaki kodu ekleyin.

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
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
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
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.tr.png)

> [!NOTE]
> Azure AI Foundry'de Prompt flow kullanımı hakkında daha detaylı bilgi için [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) sayfasına bakabilirsiniz.

1. Modelinizle sohbeti etkinleştirmek için **Chat input**, **Chat output**'u seçin.

    ![Select Input Output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.tr.png)

1. Artık özel Phi-3 / Phi-3.5 modelinizle sohbet etmeye hazırsınız. Bir sonraki alıştırmada Prompt flow'u nasıl başlatacağınızı ve fine-tuned Phi-3 / Phi-3.5 modelinizle sohbet etmek için nasıl kullanacağınızı öğreneceksiniz.

> [!NOTE]
>
> Yeniden oluşturulan akış aşağıdaki görünüme benzemelidir:
>
> ![Flow example](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.tr.png)
>

#### Prompt flow'u Başlatma

1. Prompt flow'u başlatmak için **Start compute sessions**'ı seçin.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.tr.png)

1. Parametreleri yenilemek için **Validate and parse input**'u seçin.

    ![Validate input.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.tr.png)

1. Oluşturduğunuz özel bağlantının **connection** değerini seçin. Örneğin, *connection*.

    ![Connection.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.tr.png)

#### Özel Phi-3 / Phi-3.5 modelinizle sohbet etme

1. **Chat**'i seçin.

    ![Select chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.tr.png)

1. İşte sonuçlara bir örnek: Artık özel Phi-3 / Phi-3.5 modelinizle sohbet edebilirsiniz. Fine-tuning için kullanılan verilere dayalı sorular sormanız önerilir.

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.tr.png)

### Phi-3 / Phi-3.5 modelini değerlendirmek için Azure OpenAI dağıtımı yapma

Phi-3 / Phi-3.5 modelini Azure AI Foundry'de değerlendirmek için Azure OpenAI modelini dağıtmanız gerekir. Bu model, Phi-3 / Phi-3.5 modelinin performansını değerlendirmek için kullanılacaktır.

#### Azure OpenAI Dağıtımı

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) adresine giriş yapın.

1. Oluşturduğunuz Azure AI Foundry projesine gidin.

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.tr.png)

1. Oluşturduğunuz projede, sol taraftaki sekmeden **Deployments**'ı seçin.

1. Navigasyon menüsünden **+ Deploy model**'i seçin.

1. **Deploy base model**'i seçin.

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.tr.png)

1. Kullanmak istediğiniz Azure OpenAI modelini seçin. Örneğin, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.tr.png)

1. **Confirm**'i seçin.

### Azure AI Foundry'nin Prompt flow değerlendirmesi ile fine-tuned Phi-3 / Phi-3.5 modelini değerlendirme

### Yeni değerlendirme başlatma

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) adresini ziyaret edin.

1. Oluşturduğunuz Azure AI Foundry projesine gidin.

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.tr.png)

1. Oluşturduğunuz projede, sol taraftaki sekmeden **Evaluation**'ı seçin.

1. Navigasyon menüsünden **+ New evaluation**'ı seçin.
![Değerlendirmeyi seçin.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.tr.png)

1. **Prompt flow** değerlendirmesini seçin.

    ![Prompt flow değerlendirmesini seçin.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.tr.png)

1. Aşağıdaki görevleri gerçekleştirin:

    - Değerlendirme adını girin. Benzersiz bir değer olmalıdır.
    - Görev türü olarak **Kontekstsiz soru ve cevap** seçin. Çünkü bu eğitimde kullanılan **UlTRACHAT_200k** veri seti kontekst içermez.
    - Değerlendirmek istediğiniz prompt flow’u seçin.

    ![Prompt flow değerlendirmesi.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.tr.png)

1. **İleri** seçeneğini tıklayın.

1. Aşağıdaki görevleri gerçekleştirin:

    - Veri setinizi yüklemek için **Veri setinizi ekleyin** seçeneğini seçin. Örneğin, **ULTRACHAT_200k** veri setini indirirken dahil edilen *test_data.json1* gibi test veri dosyasını yükleyebilirsiniz.
    - Veri setinize uygun **Veri seti sütununu** seçin. Örneğin, **ULTRACHAT_200k** veri setini kullanıyorsanız, veri seti sütunu olarak **${data.prompt}** seçin.

    ![Prompt flow değerlendirmesi.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.tr.png)

1. **İleri** seçeneğini tıklayın.

1. Performans ve kalite metriklerini yapılandırmak için aşağıdaki görevleri gerçekleştirin:

    - Kullanmak istediğiniz performans ve kalite metriklerini seçin.
    - Değerlendirme için oluşturduğunuz Azure OpenAI modelini seçin. Örneğin, **gpt-4o** seçin.

    ![Prompt flow değerlendirmesi.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.tr.png)

1. Risk ve güvenlik metriklerini yapılandırmak için aşağıdaki görevleri gerçekleştirin:

    - Kullanmak istediğiniz risk ve güvenlik metriklerini seçin.
    - Kusur oranını hesaplamak için kullanmak istediğiniz eşik değerini seçin. Örneğin, **Orta** seçin.
    - **question** için **Veri kaynağı** olarak **{$data.prompt}** seçin.
    - **answer** için **Veri kaynağı** olarak **{$run.outputs.answer}** seçin.
    - **ground_truth** için **Veri kaynağı** olarak **{$data.message}** seçin.

    ![Prompt flow değerlendirmesi.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.tr.png)

1. **İleri** seçeneğini tıklayın.

1. Değerlendirmeyi başlatmak için **Gönder** seçeneğini tıklayın.

1. Değerlendirme tamamlanması biraz zaman alacaktır. İlerlemeyi **Değerlendirme** sekmesinden takip edebilirsiniz.

### Değerlendirme Sonuçlarını İnceleyin

> [!NOTE]
> Aşağıda sunulan sonuçlar değerlendirme sürecini göstermek amacıyla verilmiştir. Bu eğitimde, nispeten küçük bir veri seti üzerinde ince ayar yapılmış bir model kullandık; bu nedenle sonuçlar ideal olmayabilir. Gerçek sonuçlar, kullanılan veri setinin boyutu, kalitesi ve çeşitliliği ile modelin özel yapılandırmasına bağlı olarak önemli ölçüde değişebilir.

Değerlendirme tamamlandıktan sonra performans ve güvenlik metrikleri için sonuçları inceleyebilirsiniz.

1. Performans ve kalite metrikleri:

    - Modelin tutarlı, akıcı ve ilgili yanıtlar üretme etkinliğini değerlendirin.

    ![Değerlendirme sonucu.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.tr.png)

1. Risk ve güvenlik metrikleri:

    - Modelin çıktılarının güvenli olduğundan ve Sorumlu AI İlkeleri ile uyumlu olduğundan emin olun; zararlı veya saldırgan içeriklerden kaçının.

    ![Değerlendirme sonucu.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.tr.png)

1. **Detaylı metrik sonuçlarını** görmek için aşağı kaydırabilirsiniz.

    ![Değerlendirme sonucu.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.tr.png)

1. Performans ve güvenlik metrikleri açısından özel Phi-3 / Phi-3.5 modelinizi değerlendirerek, modelin sadece etkili olmadığını aynı zamanda sorumlu AI uygulamalarına da uyduğunu doğrulayabilir ve gerçek dünya kullanımına hazır hale getirebilirsiniz.

## Tebrikler!

### Bu eğitimi tamamladınız

Azure AI Foundry’de Prompt flow ile entegre edilmiş ince ayarlı Phi-3 modelini başarıyla değerlendirdiniz. Bu, AI modellerinizin sadece iyi performans göstermesini değil, aynı zamanda Microsoft’un Sorumlu AI ilkelerine uymasını sağlayarak güvenilir ve sağlam AI uygulamaları oluşturmanıza yardımcı olan önemli bir adımdır.

![Mimari.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.tr.png)

## Azure Kaynaklarını Temizleyin

Hesabınıza ek ücret yansımaması için Azure kaynaklarınızı temizleyin. Azure portalına gidin ve aşağıdaki kaynakları silin:

- Azure Machine learning kaynağı.
- Azure Machine learning model uç noktası.
- Azure AI Foundry Proje kaynağı.
- Azure AI Foundry Prompt flow kaynağı.

### Sonraki Adımlar

#### Dokümantasyon

- [Responsible AI dashboard kullanarak AI sistemlerini değerlendirme](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Generatif AI için değerlendirme ve izleme metrikleri](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry dokümantasyonu](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow dokümantasyonu](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Eğitim İçeriği

- [Microsoft’un Sorumlu AI Yaklaşımına Giriş](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Azure AI Foundry’a Giriş](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referans

- [Sorumlu AI nedir?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Daha güvenli ve güvenilir generatif AI uygulamaları oluşturmanıza yardımcı olacak Azure AI’daki yeni araçların duyurusu](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Generatif AI uygulamalarının değerlendirilmesi](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.