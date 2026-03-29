# Microsoft Foundry'de Microsoft'un Sorumlu AI İlkelerine Odaklanarak Fine-Tuned Phi-3 / Phi-3.5 Modelini Değerlendirme

Bu uçtan uca (E2E) örnek, Microsoft Tech Community'deki "[Microsoft'un Sorumlu AI'sına Odaklanarak Microsoft Foundry'de Fine-Tuned Phi-3 / 3.5 Modelleri Değerlendirme](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" rehberine dayanmaktadır.

## Genel Bakış

### Microsoft Foundry'de fine-tuned Phi-3 / Phi-3.5 modelinin güvenlik ve performansını nasıl değerlendirirsiniz?

Bir modeli fine-tune etmek bazen istenmeyen veya beklenmedik yanıtlarla sonuçlanabilir. Modelin güvenli ve etkili kalmasını sağlamak için, modelin zararlı içerik üretme potansiyelini ve doğru, ilgili ve tutarlı cevaplar üretme yeteneğini değerlendirmek önemlidir. Bu eğitimde, Microsoft Foundry'de Prompt flow ile entegre edilmiş fine-tuned Phi-3 / Phi-3.5 modelinin güvenlik ve performansını nasıl değerlendireceğinizi öğreneceksiniz.

İşte Microsoft Foundry'nin değerlendirme süreci.

![Architecture of tutorial.](../../../../../../translated_images/tr/architecture.10bec55250f5d6a4.webp)

*Görsel Kaynağı: [Üretken AI uygulamalarının değerlendirilmesi](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Phi-3 / Phi-3.5 hakkında daha ayrıntılı bilgi ve ek kaynakları keşfetmek için [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723) adresini ziyaret edin.

### Önkoşullar

- [Python](https://www.python.org/downloads)
- [Azure aboneliği](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fine-tuned Phi-3 / Phi-3.5 modeli

### İçindekiler

1. [**Senaryo 1: Microsoft Foundry'nin Prompt flow değerlendirmesine giriş**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Güvenlik değerlendirmesine giriş](#güvenlik-değerlendirmesine-giriş)
    - [Performans değerlendirmesine giriş](#performans-değerlendirmesine-giriş)

1. [**Senaryo 2: Microsoft Foundry'de Phi-3 / Phi-3.5 modelinin değerlendirilmesi**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Başlamadan önce](#başlamadan-önce)
    - [Phi-3 / Phi-3.5 modelini değerlendirmek için Azure OpenAI'yi dağıtın](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Fine-tuned Phi-3 / Phi-3.5 modelini Microsoft Foundry'nin Prompt flow değerlendirmesi ile değerlendirin](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Tebrikler!](#tebrikler)

## **Senaryo 1: Microsoft Foundry'nin Prompt flow değerlendirmesine giriş**

### Güvenlik değerlendirmesine giriş

AI modelinizin etik ve güvenli olmasını sağlamak için, Microsoft'un Sorumlu AI İlkeleri doğrultusunda değerlendirilmesi çok önemlidir. Microsoft Foundry'de güvenlik değerlendirmeleri, modelinizin jailbreak saldırılarına karşı savunmasızlığını ve zararlı içerik üretme potansiyelini değerlendirmenize olanak tanır; bu doğrudan bu ilkelerle uyumludur.

![Safaty evaluation.](../../../../../../translated_images/tr/safety-evaluation.083586ec88dfa950.webp)

*Görsel Kaynağı: [Üretken AI uygulamalarının değerlendirilmesi](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft’un Sorumlu AI İlkeleri

Teknik adımlara başlamadan önce, AI sistemlerinin sorumlu geliştirilmesi, dağıtımı ve işletilmesini yönlendirmek için tasarlanmış etik bir çerçeve olan Microsoft'un Sorumlu AI İlkelerini anlamak esastır. Bu ilkeler, AI teknolojilerinin adil, şeffaf ve kapsayıcı bir şekilde inşa edilmesini sağlar. Bu ilkeler, AI modellerinin güvenliğini değerlendirmek için temel oluşturur.

Microsoft'un Sorumlu AI İlkeleri şunları içerir:

- **Adalet ve Kapsayıcılık**: AI sistemleri herkese adil davranmalı ve benzer durumdaki insan gruplarını farklı şekillerde etkilemekten kaçınmalıdır. Örneğin, AI sistemleri tıbbi tedavi rehberliği, kredi başvuruları veya istihdamda rehberlik sağlarken, benzer semptomlara, mali durumlara veya mesleki niteliklere sahip herkese aynı önerileri yapmalıdır.

- **Güvenilirlik ve Güvenlik**: Güven oluşturmak için AI sistemlerinin güvenilir, güvenli ve tutarlı bir şekilde çalışması kritik önem taşır. Bu sistemler, ilk tasarlandıkları şekilde çalışabilmeli, beklenmedik durumlara güvenli yanıt verebilmeli ve zararlı manipülasyona direnç gösterebilmelidir. Davranışları ve karşılayabilecekleri koşullar, geliştiricilerin tasarım ve test sırasında öngördüğü durumların ve koşulların çeşitliliğini yansıtır.

- **Şeffaflık**: AI sistemleri insanların hayatları üzerinde büyük etkisi olan kararları desteklediğinde, insanların bu kararların nasıl alındığını anlaması kritiktir. Örneğin, bir banka, bir kişinin kredi değerliliğini belirlemek için AI sistemi kullanabilir. Bir şirket, en nitelikli adayları belirlemek için AI sistemi kullanabilir.

- **Gizlilik ve Güvenlik**: AI daha yaygın hale geldikçe, gizlilik ve kişisel ile kurumsal bilgilerin güvenliği daha önemli ve karmaşık olmaktadır. AI ile gizlilik ve veri güvenliği yakından dikkat gerektirir çünkü AI sistemlerinin doğru ve bilinçli tahminler yapması için verilere erişim şarttır.

- **Hesap Verebilirlik**: AI sistemlerini tasarlayan ve dağıtan kişiler, sistemlerinin nasıl çalıştığından sorumlu olmalıdır. Kuruluşlar, hesap verebilirlik normlarını geliştirmek için sektör standartlarından faydalanmalıdır. Bu normlar, AI sistemlerinin insanların hayatlarını etkileyen kararlar üzerinde nihai otorite olmamasını sağlayabilir. Ayrıca, insanlar tarafından yüksek derecede özerk AI sistemleri üzerinde anlamlı kontrolün sürdürülmesini temin edebilir.

![Fill hub.](../../../../../../translated_images/tr/responsibleai2.c07ef430113fad8c.webp)

*Görsel Kaynağı: [Sorumlu AI Nedir?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Microsoft'un Sorumlu AI İlkeleri hakkında daha fazla bilgi edinmek için [Sorumlu AI Nedir?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723) sayfasını ziyaret edin.

#### Güvenlik metrikleri

Bu eğitimde, Microsoft Foundry'nin güvenlik metriklerini kullanarak fine-tuned Phi-3 modelinin güvenliğini değerlendireceksiniz. Bu metrikler, modelin zararlı içerik oluşturma potansiyelini ve jailbreak saldırılarına karşı savunmasızlığını değerlendirmenize yardımcı olur. Güvenlik metrikleri şunları içerir:

- **Kendine zarar verme ile ilgili içerik**: Modelin kendine zarar verme ile ilgili içerik üretme eğilimini değerlendirir.
- **Nefret içeren ve adaletsiz içerik**: Modelin nefret içerikli veya adaletsiz içerik üretme eğilimini değerlendirir.
- **Şiddet içerikli içerik**: Modelin şiddet içerikli içerik üretme eğilimini değerlendirir.
- **Cinsel içerik**: Modelin uygunsuz cinsel içerik üretme eğilimini değerlendirir.

Bu yönlerin değerlendirilmesi, AI modelinin toplum değerleri ve düzenleyici standartlarla uyumlu olarak zararlı veya saldırgan içerik üretmemesini sağlar.

![Evaluate based on safety.](../../../../../../translated_images/tr/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Performans değerlendirmesine giriş

AI modelinizin beklendiği gibi performans gösterdiğinden emin olmak için, performans metriklerine karşı değerlendirilmesi önemlidir. Microsoft Foundry'de performans değerlendirmeleri, modelinizin doğru, ilgili ve tutarlı yanıtlar üretmedeki etkinliğini değerlendirme olanağı sağlar.

![Safaty evaluation.](../../../../../../translated_images/tr/performance-evaluation.48b3e7e01a098740.webp)

*Görsel Kaynağı: [Üretken AI uygulamalarının değerlendirilmesi](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Performans metrikleri

Bu eğitimde, Microsoft Foundry'nin performans metriklerini kullanarak fine-tuned Phi-3 / Phi-3.5 modelinin performansını değerlendireceksiniz. Bu metrikler, modelin doğru, ilgili ve tutarlı yanıtlar üretmedeki etkinliğini değerlendirmenize yardımcı olur. Performans metrikleri şunlardır:

- **Temellendirme (Groundedness)**: Üretilen yanıtların giriş kaynağı bilgilerle ne kadar uyumlu olduğunu değerlendirir.
- **İlgililik**: Üretilen yanıtların verilen sorulara olan uygunluğunu değerlendirir.
- **Tutarlılık**: Üretilen metnin akıcılığını, doğal okunabilirliğini ve insan benzeri dil özelliklerini değerlendirir.
- **Akıcılık**: Üretilen metnin dil yeterliliğini değerlendirir.
- **GPT Benzerliği**: Üretilen yanıtı gerçek doğru yanıt ile karşılaştırır.
- **F1 Skoru**: Üretilen yanıt ile kaynak veri arasındaki paylaşılan kelimelerin oranını hesaplar.

Bu metrikler, modelinizin doğru, ilgili ve tutarlı yanıtlar üretmedeki etkinliğini değerlendirmenize yardımcı olur.

![Evaluate based on performance.](../../../../../../translated_images/tr/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Senaryo 2: Microsoft Foundry'de Phi-3 / Phi-3.5 modelinin değerlendirilmesi**

### Başlamadan önce

Bu eğitim, daha önceki blog yazılarının devamıdır: "[Fine-Tune ve Prompt Flow ile Özel Phi-3 Modellerini Entegre Etme: Adım Adım Kılavuz](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" ve "[Microsoft Foundry'de Fine-Tune ve Prompt Flow ile Özel Phi-3 Modellerini Entegre Etme](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Bu yazılarda, Microsoft Foundry'de Phi-3 / Phi-3.5 modelinin nasıl fine-tune edildiğini ve Prompt flow ile nasıl entegre edildiğini inceledik.

Bu eğitimde, Microsoft Foundry'de bir Azure OpenAI modelini değerlendirici olarak dağıtacak ve fine-tuned Phi-3 / Phi-3.5 modelinizi değerlendirmek için kullanacaksınız.

Bu eğitime başlamadan önce, önceki eğitimlerde açıklandığı şekilde aşağıdaki önkoşullara sahip olduğunuzdan emin olun:

1. Fine-tuned Phi-3 / Phi-3.5 modelini değerlendirmek için hazırlanmış bir veri kümesi.
1. Azure Machine Learning'e fine-tune edilip dağıtılmış bir Phi-3 / Phi-3.5 modeli.
1. Microsoft Foundry'de fine-tuned Phi-3 / Phi-3.5 modelinizle entegre edilmiş bir Prompt flow.

> [!NOTE]
> Önceki blog yazılarında indirilen **ULTRACHAT_200k** veri setindeki data klasöründe bulunan *test_data.jsonl* dosyasını, fine-tuned Phi-3 / Phi-3.5 modelini değerlendirmek için veri kümesi olarak kullanacaksınız.

#### Microsoft Foundry'de custom Phi-3 / Phi-3.5 modelini Prompt flow ile entegre etme (Öncelikle kod yaklaşımı)

> [!NOTE]
> Eğer "[Microsoft Foundry'de Fine-Tune ve Prompt Flow ile Özel Phi-3 Modellerini Entegre Etme](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" yazısında açıklanan düşük kod yaklaşımını izlediyseniz, bu egzersizi atlayabilir ve bir sonrakine geçebilirsiniz.
> Ancak, "[Fine-Tune ve Prompt Flow ile Özel Phi-3 Modellerini Entegre Etme: Adım Adım Kılavuz](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" yazısında açıklanan kod öncelikli yaklaşımı kullanarak Phi-3 / Phi-3.5 modelinizi fine-tune ve dağıttıysanız, modelinizi Prompt flow'a bağlama süreci biraz farklıdır. Bu egzersizde bu süreci öğreneceksiniz.

Devam etmek için, fine-tuned Phi-3 / Phi-3.5 modelinizi Microsoft Foundry'de Prompt flow'a entegre etmeniz gerekir.

#### Microsoft Foundry Hub Oluşturun

Project oluşturmadan önce bir Hub oluşturmanız gerekir. Hub, kaynak grubu gibi davranır ve Microsoft Foundry içinde birden fazla Project'i organize etmenize ve yönetmenize olanak tanır.
1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) adresine giriş yapın.

1. Sol taraftaki sekmeden **All hubs**'u seçin.

1. Gezinme menüsünden **+ New hub**'ı seçin.

    ![Create hub.](../../../../../../translated_images/tr/create-hub.5be78fb1e21ffbf1.webp)

1. Aşağıdaki görevleri gerçekleştirin:

    - **Hub name** girin. Benzersiz bir değer olmalıdır.
    - Azure **Subscription** seçin.
    - Kullanılacak **Resource group**'u seçin (gerekirse yenisini oluşturun).
    - Kullanmak istediğiniz **Location**'ı seçin.
    - Kullanılacak **Connect Azure AI Services**'i seçin (gerekirse yenisini oluşturun).
    - **Connect Azure AI Search** seçeneğinde **Skip connecting**'i seçin.

    ![Fill hub.](../../../../../../translated_images/tr/fill-hub.baaa108495c71e34.webp)

1. **Next**'i seçin.

#### Microsoft Foundry Projesi Oluşturma

1. Oluşturduğunuz Hub içinde, sol taraftaki sekmeden **All projects**'ı seçin.

1. Gezinme menüsünden **+ New project**'i seçin.

    ![Select new project.](../../../../../../translated_images/tr/select-new-project.cd31c0404088d7a3.webp)

1. **Project name** girin. Benzersiz bir değer olmalıdır.

    ![Create project.](../../../../../../translated_images/tr/create-project.ca3b71298b90e420.webp)

1. **Create a project**'i seçin.

#### Ince Ayarlı Phi-3 / Phi-3.5 modeli için özel bağlantı ekleme

Özel Phi-3 / Phi-3.5 modelinizi Prompt flow ile entegre etmek için modelin endpoint ve anahtarını özel bağlantıda kaydetmeniz gerekir. Bu yapılandırma, Prompt flow içinde özel Phi-3 / Phi-3.5 modelinize erişimi sağlar.

#### İnce ayarlı Phi-3 / Phi-3.5 modelinin api anahtarı ve endpoint uri'sini ayarlama

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) sitesini ziyaret edin.

1. Oluşturduğunuz Azure Machine learning çalışma alanına gidin.

1. Sol taraftaki sekmeden **Endpoints**'i seçin.

    ![Select endpoints.](../../../../../../translated_images/tr/select-endpoints.ee7387ecd68bd18d.webp)

1. Oluşturduğunuz endpoint'i seçin.

    ![Select endpoints.](../../../../../../translated_images/tr/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Gezinme menüsünden **Consume**'yi seçin.

1. **REST endpoint** ve **Primary key**'inizi kopyalayın.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/tr/copy-endpoint-key.0650c3786bd646ab.webp)

#### Özel Bağlantı Ekleme

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) adresine gidin.

1. Oluşturduğunuz Microsoft Foundry projesine gidin.

1. Oluşturduğunuz Projede, sol taraftaki sekmeden **Settings**'i seçin.

1. **+ New connection**'ı seçin.

    ![Select new connection.](../../../../../../translated_images/tr/select-new-connection.fa0f35743758a74b.webp)

1. Gezinme menüsünden **Custom keys**'i seçin.

    ![Select custom keys.](../../../../../../translated_images/tr/select-custom-keys.5a3c6b25580a9b67.webp)

1. Aşağıdaki görevleri gerçekleştirin:

    - **+ Add key value pairs**'i seçin.
    - Anahtar adı için **endpoint** yazın ve Azure ML Studio'dan kopyaladığınız endpoint'i değer alanına yapıştırın.
    - Tekrar **+ Add key value pairs**'i seçin.
    - Anahtar adı için **key** yazın ve Azure ML Studio'dan kopyaladığınız anahtarı değer alanına yapıştırın.
    - Anahtarları ekledikten sonra, anahtarın açığa çıkmasını önlemek için **is secret**'i seçin.

    ![Add connection.](../../../../../../translated_images/tr/add-connection.ac7f5faf8b10b0df.webp)

1. **Add connection**'ı seçin.

#### Prompt flow Oluşturma

Microsoft Foundry'de özel bir bağlantı eklediniz. Şimdi, aşağıdaki adımları izleyerek bir Prompt flow oluşturacağız. Ardından, bu Prompt flow'u özel bağlantıya bağlayarak ince ayarlı modeli Prompt flow içinde kullanacaksınız.

1. Oluşturduğunuz Microsoft Foundry projesine gidin.

1. Sol taraftaki sekmeden **Prompt flow**'u seçin.

1. Gezinme menüsünden **+ Create**'i seçin.

    ![Select Promptflow.](../../../../../../translated_images/tr/select-promptflow.18ff2e61ab9173eb.webp)

1. Gezinme menüsünden **Chat flow**'u seçin.

    ![Select chat flow.](../../../../../../translated_images/tr/select-flow-type.28375125ec9996d3.webp)

1. Kullanmak için **Folder name** girin.

    ![Select chat flow.](../../../../../../translated_images/tr/enter-name.02ddf8fb840ad430.webp)

1. **Create**'i seçin.

#### Prompt flow'u özel Phi-3 / Phi-3.5 modelinizle sohbet edecek şekilde ayarlama

İnce ayarlı Phi-3 / Phi-3.5 modelini Prompt flow'a entegre etmeniz gerekir. Ancak, mevcut Prompt flow bu amaç için tasarlanmamıştır. Bu nedenle, özel model entegrasyonunu etkinleştirmek için Prompt flow'u yeniden tasarlamanız gerekiyor.

1. Prompt flow'da mevcut akışı yeniden oluşturmak için aşağıdaki görevleri yapın:

    - **Raw file mode**'u seçin.
    - *flow.dag.yml* dosyasındaki tüm mevcut kodu silin.
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

    ![Select raw file mode.](../../../../../../translated_images/tr/select-raw-file-mode.06c1eca581ce4f53.webp)

1. *integrate_with_promptflow.py* dosyasına aşağıdaki kodu ekleyin, bu kod Prompt flow'da özel Phi-3 / Phi-3.5 modelini kullanmanızı sağlar.

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
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" Özel Bağlantının adıdır, "endpoint" ve "key" ise Özel Bağlantıdaki anahtarlardır
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
            
            # Tam JSON yanıtını günlükle
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

    ![Paste prompt flow code.](../../../../../../translated_images/tr/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Microsoft Foundry'de Prompt flow kullanımı hakkında daha ayrıntılı bilgi için [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) bağlantısını inceleyebilirsiniz.

1. Modelinizle sohbeti etkinleştirmek için sırasıyla **Chat input**, **Chat output**'u seçin.

    ![Select Input Output.](../../../../../../translated_images/tr/select-input-output.c187fc58f25fbfc3.webp)

1. Artık özel Phi-3 / Phi-3.5 modelinizle sohbet etmeye hazırsınız. Bir sonraki alıştırmada, Prompt flow'u nasıl başlatacağınızı ve ince ayarlı Phi-3 / Phi-3.5 modelinizle nasıl sohbet edeceğinizi öğreneceksiniz.

> [!NOTE]
>
> Yeniden oluşturulan akış aşağıdaki görüntüdeki gibi olmalıdır:
>
> ![Flow example](../../../../../../translated_images/tr/graph-example.82fd1bcdd3fc545b.webp)
>

#### Prompt flow'u Başlatma

1. Prompt flow'u başlatmak için **Start compute sessions**'ı seçin.

    ![Start compute session.](../../../../../../translated_images/tr/start-compute-session.9acd8cbbd2c43df1.webp)

1. Parametreleri yenilemek için **Validate and parse input**'ı seçin.

    ![Validate input.](../../../../../../translated_images/tr/validate-input.c1adb9543c6495be.webp)

1. Oluşturduğunuz özel bağlantının **connection** değerini seçin. Örnek olarak *connection*.

    ![Connection.](../../../../../../translated_images/tr/select-connection.1f2b59222bcaafef.webp)

#### Özel Phi-3 / Phi-3.5 modelinizle sohbet etme

1. **Chat**'i seçin.

    ![Select chat.](../../../../../../translated_images/tr/select-chat.0406bd9687d0c49d.webp)

1. İşte sonuçlara ait bir örnek: Artık özel Phi-3 / Phi-3.5 modelinizle sohbet edebilirsiniz. İnce ayar için kullanılan verilere dayanarak sorular sormanız önerilir.

    ![Chat with prompt flow.](../../../../../../translated_images/tr/chat-with-promptflow.1cf8cea112359ada.webp)

### Phi-3 / Phi-3.5 modelini değerlendirmek için Azure OpenAI'yi dağıtma

Phi-3 / Phi-3.5 modelini Microsoft Foundry'de değerlendirmek için bir Azure OpenAI modeli dağıtmanız gerekir. Bu model, Phi-3 / Phi-3.5 modelinin performansını değerlendirmek amacıyla kullanılacaktır.

#### Azure OpenAI Dağıtma

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) adresine giriş yapın.

1. Oluşturduğunuz Microsoft Foundry projesine gidin.

    ![Select Project.](../../../../../../translated_images/tr/select-project-created.5221e0e403e2c9d6.webp)

1. Oluşturduğunuz Projede, sol taraftaki sekmeden **Deployments**'ı seçin.

1. Gezinme menüsünden **+ Deploy model**'i seçin.

1. **Deploy base model**'i seçin.

    ![Select Deployments.](../../../../../../translated_images/tr/deploy-openai-model.95d812346b25834b.webp)

1. Kullanmak istediğiniz Azure OpenAI modelini seçin. Örneğin, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/tr/select-openai-model.959496d7e311546d.webp)

1. **Confirm**'i seçin.

### Microsoft Foundry'nin Prompt flow değerlendirmesi ile ince ayarlı Phi-3 / Phi-3.5 modelini değerlendirme

### Yeni bir değerlendirme başlatma

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) adresini ziyaret edin.

1. Oluşturduğunuz Microsoft Foundry projesine gidin.

    ![Select Project.](../../../../../../translated_images/tr/select-project-created.5221e0e403e2c9d6.webp)

1. Oluşturduğunuz Projede, sol taraftaki sekmeden **Evaluation**'ı seçin.

1. Gezinme menüsünden **+ New evaluation**'ı seçin.

    ![Select evaluation.](../../../../../../translated_images/tr/select-evaluation.2846ad7aaaca7f4f.webp)

1. **Prompt flow** değerlendirmesini seçin.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/tr/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Aşağıdaki görevleri yapın:

    - Değerlendirme adını girin. Benzersiz bir değer olmalıdır.
    - Görev türü olarak **Question and answer without context**'i seçin. Çünkü bu eğitimde kullanılan **UlTRACHAT_200k** veri seti bağlam içermemektedir.
    - Değerlendirmek istediğiniz prompt flow'u seçin.

    ![Prompt flow evaluation.](../../../../../../translated_images/tr/evaluation-setting1.4aa08259ff7a536e.webp)

1. **Next**'i seçin.

1. Aşağıdaki görevleri yapın:

    - Veri setini yüklemek için **Add your dataset**'i seçin. Örneğin, **ULTRACHAT_200k** veri setini indirirken dahil olan *test_data.json1* gibi test veri dosyasını yükleyebilirsiniz.
    - Veri setinize uygun **Dataset column** seçin. Örneğin, **ULTRACHAT_200k** veri setini kullanıyorsanız, veri seti sütunu olarak **${data.prompt}** seçin.

    ![Prompt flow evaluation.](../../../../../../translated_images/tr/evaluation-setting2.07036831ba58d64e.webp)

1. **Next**'i seçin.

1. Performans ve kalite metriklerini yapılandırmak için aşağıdaki görevleri yapın:

    - Kullanmak istediğiniz performans ve kalite metriklerini seçin.
    - Değerlendirme için oluşturduğunuz Azure OpenAI modelini seçin. Örneğin, **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/tr/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Risk ve güvenlik metriklerini yapılandırmak için aşağıdaki görevleri yapın:

    - Kullanmak istediğiniz risk ve güvenlik metriklerini seçin.
    - Hata oranını hesaplamak için kullanmak istediğiniz eşik değerini seçin. Örneğin, **Medium**.
    - **question** için, **Data source**'u **{$data.prompt}** olarak seçin.
    - **answer** için, **Data source**'u **{$run.outputs.answer}** olarak seçin.
    - **ground_truth** için, **Data source**'u **{$data.message}** olarak seçin.

    ![Prompt flow evaluation.](../../../../../../translated_images/tr/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. **Next**'i seçin.

1. Değerlendirmeyi başlatmak için **Submit**'i seçin.

1. Değerlendirme tamamlanana kadar biraz zaman alacaktır. İlerlemesini **Evaluation** sekmesinden takip edebilirsiniz.

### Değerlendirme Sonuçlarını İnceleme

> [!NOTE]
> Aşağıda sunulan sonuçlar değerlendirme sürecini göstermek amacıyla verilmiştir. Bu eğitimde nispeten küçük bir veri seti üzerinde ince ayar yapılmış bir model kullanılmıştır ve bu nedenle sonuçlar ideal olmayabilir. Kullanılan veri setinin büyüklüğü, kalitesi ve çeşitliğinin yanı sıra modelin spesifik yapılandırmasına bağlı olarak gerçek sonuçlar önemli ölçüde değişebilir.

Değerlendirme tamamlandıktan sonra, hem performans hem de güvenlik metriklerine ilişkin sonuçları inceleyebilirsiniz.
1. Performans ve kalite metrikleri:

    - Modelin tutarlı, akıcı ve ilgili yanıtlar üretmedeki etkinliğini değerlendirin.

    ![Değerlendirme sonucu.](../../../../../../translated_images/tr/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Risk ve güvenlik metrikleri:

    - Model çıktılarının güvenli olduğunu ve Sorumlu Yapay Zeka İlkeleri ile uyumlu olup zararlı veya saldırgan içerik içermediğini sağlayın.

    ![Değerlendirme sonucu.](../../../../../../translated_images/tr/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. **Ayrıntılı metrik sonuçlarını** görmek için aşağı kaydırabilirsiniz.

    ![Değerlendirme sonucu.](../../../../../../translated_images/tr/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Özelleştirilmiş Phi-3 / Phi-3.5 modelinizi hem performans hem de güvenlik metriklerine göre değerlendirerek, modelin yalnızca etkili olmadığını, aynı zamanda sorumlu yapay zeka uygulamalarına uygun olduğunu doğrulayabilir ve gerçek dünya dağıtımına hazır hale getirebilirsiniz.

## Tebrikler!

### Bu eğitimi tamamladınız

Microsoft Foundry’da Prompt flow ile entegre edilmiş ince ayarlı Phi-3 modelini başarıyla değerlendirdiniz. Bu, yapay zeka modellerinizin yalnızca iyi performans göstermesini değil, aynı zamanda Microsoft’un Sorumlu Yapay Zeka prensiplerine uyduğundan emin olarak güvenilir ve sağlam yapay zeka uygulamaları oluşturmanıza yardımcı olacak önemli bir adımdır.

![Mimari.](../../../../../../translated_images/tr/architecture.10bec55250f5d6a4.webp)

## Azure Kaynaklarını Temizleyin

Hesabınıza ek ücretlerin yansımaması için Azure kaynaklarınızı temizleyin. Azure portalına gidip aşağıdaki kaynakları silin:

- Azure Machine Learning kaynağı.
- Azure Machine Learning model uç noktası.
- Microsoft Foundry Proje kaynağı.
- Microsoft Foundry Prompt flow kaynağı.

### Sonraki Adımlar

#### Belgeler

- [Sorumlu Yapay Zeka panosunu kullanarak AI sistemlerini değerlendirme](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Üretken AI için değerlendirme ve izleme metrikleri](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry belgeleri](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow belgeleri](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Eğitim İçeriği

- [Microsoft’un Sorumlu Yapay Zeka Yaklaşımına Giriş](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Microsoft Foundry’e Giriş](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referans

- [Sorumlu Yapay Zeka nedir?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Daha güvenli ve güvenilir üretken AI uygulamaları oluşturmanız için Azure AI’da yeni araçlar duyuruldu](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Üretken AI uygulamalarının değerlendirilmesi](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstermekle birlikte, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi diliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımıyla ortaya çıkabilecek yanlış anlamalar veya yorum hataları nedeniyle sorumluluk kabul edilmemektedir.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->